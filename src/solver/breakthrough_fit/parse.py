"""CSV parser for two lab formats.

Format A — raw multi-sensor log. Header rows 1–2 declare sensors; data rows are
those where every channel has a value (we restrict to the CO2 channel).
Format B — pre-processed spreadsheet with C0 in row 1, col E and named columns.

Both formats are detected automatically.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable, Optional

import numpy as np
import pandas as pd


@dataclass
class ParsedRun:
    """Container for a single breakthrough run."""

    df: pd.DataFrame
    c0_ppm: float
    flow_ml_min: Optional[float]
    temperature_K: Optional[float]
    pressure_Pa: Optional[float]
    filename: str
    run_id: str
    fmt: str  # "A", "B", "C", or "D"
    mass_g: Optional[float] = None
    bed_height_cm: Optional[float] = None
    tube_diameter_mm: Optional[float] = None


_DATETIME_FMT_A = "%m/%d/%y %H:%M:%S.%f"


class DataParser:
    """Parse breakthrough CSV files written in either format A or B."""

    # ------------------------------------------------------------------ #
    # Public API
    # ------------------------------------------------------------------ #
    def parse(self, path: str | Path, c0_override: Optional[float] = None) -> ParsedRun:
        path = Path(path)
        fmt = self.auto_detect(path)
        if fmt == "A":
            return self.parse_format_a(path, c0_override=c0_override)
        if fmt == "C":
            return self.parse_format_c(path, c0_override=c0_override)
        if fmt == "D":
            return self.parse_format_d(path, c0_override=c0_override)
        return self.parse_format_b(path, c0_override=c0_override)

    def parse_many(
        self, paths: Iterable[str | Path], c0_override: Optional[float] = None
    ) -> list[ParsedRun]:
        return [self.parse(p, c0_override=c0_override) for p in paths]

    # ------------------------------------------------------------------ #
    # Format detection
    # ------------------------------------------------------------------ #
    @staticmethod
    def auto_detect(path: Path) -> str:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            head = [next(fh, "") for _ in range(5)]
        blob = "".join(head).lower()
        # Format D: self-describing newest-runs CSVs carry a quoted prose
        # block naming "Bed height:"/"Tube diameter:" — unique to this format.
        if "bed height:" in blob or "tube diameter:" in blob:
            return "D"
        first = head[0].lower()
        # Format B header contains "c0" and "time (s)" labels in row 1.
        if "c0" in first and "time" in first:
            return "B"
        # Format A row-1 mentions "sensor" or includes channel keyword in row 2.
        if "sensor" in first or "co2" in head[1].lower():
            return "A"
        # Fallback heuristic: 8 comma-separated cells with datetime in col 0.
        if head[1].count(",") >= 7:
            return "A"
        # Format C: simple datetime + concentration (2–4 columns, no metadata).
        # Detected by: ≤ 4 comma-separated fields and a datetime-like string
        # in the first data row (row 1 if headerless, row 2 if header present).
        _data_row = head[1] if head[1].strip() else head[2]
        _parts = [p.strip().strip('"') for p in _data_row.split(",") if p.strip()]
        if len(_parts) <= 4 and _parts:
            try:
                datetime.strptime(_parts[0], _DATETIME_FMT_A)
                return "C"
            except ValueError:
                pass
        return "B"

    # ------------------------------------------------------------------ #
    # Format A
    # ------------------------------------------------------------------ #
    def parse_format_a(
        self, path: Path, c0_override: Optional[float] = None
    ) -> ParsedRun:
        # Row 2 declares the channel order.  Read it first so we can adapt to
        # files with anywhere between 5 and 8 sensor columns.
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            _ = next(fh, "")
            header_row = next(fh, "").rstrip("\n").split(",")
        channel_names = [c.strip() for c in header_row]
        n_cols = len(channel_names)
        # Column 0 is always datetime in this format.
        col_names = ["dt"] + [
            (c or f"col{i}") for i, c in enumerate(channel_names[1:], start=1)
        ]
        # Ensure CO2 column exists.
        if "CO2" not in col_names:
            col_names[1] = "CO2"

        df = pd.read_csv(
            path,
            header=None,
            skiprows=2,
            names=col_names,
            usecols=range(n_cols),
            engine="python",
            on_bad_lines="skip",
        )
        df["CO2"] = pd.to_numeric(df["CO2"], errors="coerce")
        df = df.dropna(subset=["CO2"]).copy()
        df["dt_parsed"] = pd.to_datetime(
            df["dt"].str.strip(), format=_DATETIME_FMT_A, errors="coerce"
        )
        df = df.dropna(subset=["dt_parsed"]).copy()
        df = df.sort_values("dt_parsed").drop_duplicates("dt_parsed", keep="first")
        t0 = df["dt_parsed"].min()
        df["t"] = (df["dt_parsed"] - t0).dt.total_seconds()
        c0 = c0_override if c0_override else float(df["CO2"].max())
        df["C_C0"] = df["CO2"] / c0
        out = df[["t", "C_C0"]].reset_index(drop=True)
        out["C0_ppm"] = c0
        out["filename"] = path.name
        out["run_id"] = path.stem
        out = self._despike(out)
        # Temperature/pressure averages if available.
        temp_col = "Temperature" if "Temperature" in df.columns else None
        pres_col = "Pressure" if "Pressure" in df.columns else None
        temp = (
            pd.to_numeric(df[temp_col], errors="coerce").mean()
            if temp_col else float("nan")
        )
        pres = (
            pd.to_numeric(df[pres_col], errors="coerce").mean()
            if pres_col else float("nan")
        )
        return ParsedRun(
            df=out,
            c0_ppm=c0,
            flow_ml_min=None,
            temperature_K=(temp + 273.15) if pd.notna(temp) else None,
            pressure_Pa=float(pres) * 100.0 if pd.notna(pres) else None,
            filename=path.name,
            run_id=path.stem,
            fmt="A",
        )

    # ------------------------------------------------------------------ #
    # Format B
    # ------------------------------------------------------------------ #
    def parse_format_b(
        self, path: Path, c0_override: Optional[float] = None
    ) -> ParsedRun:
        # Two-pass: first read row 1 for C0 + named columns, then read data.
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            row1 = next(fh).rstrip("\n").split(",")
        c0_ppm = c0_override
        if c0_ppm is None:
            try:
                c0_ppm = float(row1[4])
            except (IndexError, ValueError):
                c0_ppm = None

        df = pd.read_csv(
            path,
            header=None,
            skiprows=1,
            engine="python",
            on_bad_lines="skip",
        )
        # Identify columns by header keywords in row1.
        col_map: dict[str, int] = {}
        for i, label in enumerate(row1):
            label_lc = label.strip().lower()
            if label_lc == "time (s)":
                col_map["t"] = i
            elif label_lc == "c/c0":
                col_map["C_C0"] = i
            elif label_lc == "co2":
                col_map["CO2"] = i

        if "t" not in col_map or "C_C0" not in col_map:
            # Best-effort fallback to fixed positions.
            col_map.setdefault("t", 5)
            col_map.setdefault("C_C0", 8)

        out = pd.DataFrame(
            {
                "t": pd.to_numeric(df.iloc[:, col_map["t"]], errors="coerce"),
                "C_C0": pd.to_numeric(df.iloc[:, col_map["C_C0"]], errors="coerce"),
            }
        )
        if "CO2" in col_map:
            out["CO2"] = pd.to_numeric(df.iloc[:, col_map["CO2"]], errors="coerce")
        else:
            out["CO2"] = np.nan
        out = out.dropna(subset=["t", "C_C0"]).copy()
        out = out.sort_values("t").drop_duplicates("t", keep="first")
        # Drop any baseline glitches but keep legitimate pre-breakthrough zeros.
        if c0_ppm is None and "CO2" in out:
            c0_ppm = float(out["CO2"].max()) if out["CO2"].notna().any() else 1.0
        out["C0_ppm"] = c0_ppm
        out["filename"] = path.name
        out["run_id"] = path.stem
        out = out[["t", "C_C0", "C0_ppm", "filename", "run_id"]].reset_index(drop=True)
        out = self._despike(out)

        # Metadata (cols N–P) — labels in col 13, values 14, units 15 (0-indexed).
        meta = self._parse_metadata_b(df)
        return ParsedRun(
            df=out,
            c0_ppm=c0_ppm,
            flow_ml_min=meta.get("v"),
            temperature_K=meta.get("T"),
            pressure_Pa=meta.get("P"),
            filename=path.name,
            run_id=path.stem,
            fmt="B",
        )

    # ------------------------------------------------------------------ #
    # Format C — simple datetime + raw ppm  (new lab runs)
    # ------------------------------------------------------------------ #
    def parse_format_c(
        self, path: Path, c0_override: Optional[float] = None
    ) -> ParsedRun:
        """Parse 2–4-column files: datetime in col 0, ppm in last non-empty col.

        Auto-detects:
          * ``C0``  — 92nd-percentile of concentration (plateau median).
          * ``t=0`` — first pair of consecutive points above 2 % of C0.

        ``C/C0 = (C_raw − baseline) / (C0 − baseline)`` where baseline is the
        median of the first 10 data points.
        """
        content = path.read_text(encoding="utf-8", errors="replace").splitlines()
        # Skip header row if it contains "Time" or "time".
        start = 1 if content and "ime" in content[0] else 0
        times: list[datetime] = []
        raw: list[float] = []
        for line in content[start:]:
            parts = [p.strip().strip('"') for p in line.split(",")]
            parts = [p for p in parts if p]
            if len(parts) < 2:
                continue
            try:
                dt = datetime.strptime(parts[0], _DATETIME_FMT_A)
                c = float(parts[-1])
                times.append(dt)
                raw.append(c)
            except (ValueError, IndexError):
                continue

        if not times:
            raise ValueError(f"No parseable rows in {path}")

        conc = np.array(raw, dtype=float)
        # Baseline = median of first 10 points.
        baseline = float(np.median(conc[:min(10, len(conc))]))
        # C0 = 92nd percentile (avoids sensor noise spikes at top).
        c0 = c0_override if c0_override else float(np.percentile(conc, 92))

        # Detect t=0: first pair of consecutive points above 2 % of C0.
        thresh = baseline + 0.02 * (c0 - baseline)
        t0_idx = 0
        for i in range(len(conc) - 1):
            if conc[i] > thresh and conc[i + 1] > thresh:
                t0_idx = max(0, i - 1)
                break
        t0 = times[t0_idx]

        t_sec = np.array([(t - t0).total_seconds() for t in times], dtype=float)
        span = max(c0 - baseline, 1.0)
        c_c0 = np.clip((conc - baseline) / span, 0.0, 1.05)

        out = pd.DataFrame({"t": t_sec, "C_C0": c_c0})
        out["C0_ppm"] = c0
        out["filename"] = path.name
        out["run_id"] = path.stem
        out = out.reset_index(drop=True)
        out = self._despike(out)

        return ParsedRun(
            df=out,
            c0_ppm=c0,
            flow_ml_min=None,
            temperature_K=None,
            pressure_Pa=None,
            filename=path.name,
            run_id=path.stem,
            fmt="C",
        )

    # ------------------------------------------------------------------ #
    # Format D — self-describing newest-runs CSV (prose header + label/
    # value/unit table at cols 8-10, real header row further down, then
    # a pre-processed data block).
    # ------------------------------------------------------------------ #
    def parse_format_d(
        self, path: Path, c0_override: Optional[float] = None
    ) -> ParsedRun:
        df_raw = pd.read_csv(path, header=None, engine="python", on_bad_lines="skip")

        # Locate the real header row by content, not a fixed offset.
        hdr_idx = None
        for i in range(min(20, len(df_raw))):
            if (
                str(df_raw.iat[i, 0]).strip() == "Time"
                and df_raw.shape[1] > 1
                and str(df_raw.iat[i, 1]).strip() == "Time (min)"
            ):
                hdr_idx = i
                break
        if hdr_idx is None:
            raise ValueError(f"Format D: header row not found in {path}")

        # Label/value/unit metadata table at cols 8-10, rows above the header.
        meta: dict[str, float] = {}
        if df_raw.shape[1] > 9:
            labels = df_raw.iloc[:hdr_idx, 8].astype(str).str.strip().str.lower()
            values = pd.to_numeric(df_raw.iloc[:hdr_idx, 9], errors="coerce")
            for label, value in zip(labels, values):
                if pd.notna(value):
                    meta[label] = float(value)

        # Prose block (row 0, col 0) — bed height & tube diameter live only here.
        prose = str(df_raw.iat[0, 0])
        bed_height_m = re.search(r"Bed height:\s*([\d.]+)\s*mm", prose, re.IGNORECASE)
        tube_dia_m = re.search(r"Tube diameter:\s*([\d.]+)\s*mm", prose, re.IGNORECASE)
        mass_m = re.search(r"Mass:\s*([\d.]+)\s*g", prose, re.IGNORECASE)

        mass_g = meta.get("mass")
        if mass_m is not None:
            mass_prose = float(mass_m.group(1))
            if mass_g is not None and abs(mass_prose - mass_g) > 0.05:
                print(
                    f"[WARN] {path.name}: prose mass {mass_prose:g} g vs "
                    f"table mass {mass_g:g} g disagree"
                )
            elif mass_g is None:
                mass_g = mass_prose

        c0_ppm = c0_override if c0_override is not None else meta.get("c0")

        # Data rows: Time (min) -> t [s]; recompute C/C0 ourselves.
        data = df_raw.iloc[hdr_idx + 1 :]
        t_sec = pd.to_numeric(data.iloc[:, 1], errors="coerce") * 60.0
        co2 = pd.to_numeric(data.iloc[:, 2], errors="coerce")

        out = pd.DataFrame({"t": t_sec, "C_C0": co2 / c0_ppm if c0_ppm else np.nan})
        out["CO2"] = co2
        out = out.dropna(subset=["t", "C_C0"]).copy()
        out = out.sort_values("t").drop_duplicates("t", keep="first")
        if c0_ppm is None and out["CO2"].notna().any():
            c0_ppm = float(out["CO2"].max())
            out["C_C0"] = out["CO2"] / c0_ppm
        out["C0_ppm"] = c0_ppm
        out["filename"] = path.name
        out["run_id"] = path.stem
        out = out[["t", "C_C0", "C0_ppm", "filename", "run_id"]].reset_index(drop=True)
        out = self._despike(out)

        temp_col = 5  # Temperature, by position
        temp = (
            pd.to_numeric(data.iloc[:, temp_col], errors="coerce").mean()
            if data.shape[1] > temp_col
            else float("nan")
        )

        return ParsedRun(
            df=out,
            c0_ppm=c0_ppm,
            flow_ml_min=(meta["v"] * 1000.0) if "v" in meta else None,
            temperature_K=(temp + 273.15) if pd.notna(temp) else None,
            pressure_Pa=meta.get("p"),
            filename=path.name,
            run_id=path.stem,
            fmt="D",
            mass_g=mass_g,
            bed_height_cm=(float(bed_height_m.group(1)) / 10.0) if bed_height_m else None,
            tube_diameter_mm=float(tube_dia_m.group(1)) if tube_dia_m else None,
        )

    # ------------------------------------------------------------------ #
    # Helpers
    # ------------------------------------------------------------------ #
    @staticmethod
    def _parse_metadata_b(df: pd.DataFrame) -> dict[str, float]:
        meta: dict[str, float] = {}
        if df.shape[1] < 16:
            return meta
        labels = df.iloc[:, 13].astype(str).str.strip().str.lower()
        values = pd.to_numeric(df.iloc[:, 14], errors="coerce")
        for label, value in zip(labels, values):
            if pd.isna(value):
                continue
            if label == "p":
                meta["P"] = float(value)
            elif label == "r":
                meta["R"] = float(value)
            elif label == "v":
                meta["v"] = float(value)
            elif label == "t":
                meta["T"] = float(value)
        return meta

    @staticmethod
    def _despike(df: pd.DataFrame, threshold: float = 0.15) -> pd.DataFrame:
        """Flag and interpolate transient sensor jumps > threshold."""
        y = df["C_C0"].to_numpy(dtype=float)
        if y.size < 3:
            return df
        d = np.abs(np.diff(y))
        bad = np.zeros_like(y, dtype=bool)
        bad[1:][d > threshold] = True
        # Only treat point-wise spikes (returns to neighbourhood next step).
        for i in np.where(bad)[0]:
            if 0 < i < y.size - 1 and abs(y[i + 1] - y[i - 1]) < threshold:
                y[i] = 0.5 * (y[i - 1] + y[i + 1])
        out = df.copy()
        out["C_C0"] = y
        return out

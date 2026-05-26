"""CSV parser for two lab formats.

Format A — raw multi-sensor log. Header rows 1–2 declare sensors; data rows are
those where every channel has a value (we restrict to the CO2 channel).
Format B — pre-processed spreadsheet with C0 in row 1, col E and named columns.

Both formats are detected automatically.
"""

from __future__ import annotations

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
    fmt: str  # "A" or "B"


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
            head = [next(fh, "") for _ in range(2)]
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

"""Material passport for the `newest runs/` breakthrough campaign.

Emits a machine-readable provenance ledger for every experiment in
``src/solver/data/newest runs/`` and renders the tables that §5 "Experiments" of
``src/T32_PI05_Final_Report.docx`` is built from.

    python src/solver/build_experiments_passport.py

Outputs
-------
``src/docs/experiments_passport.json``
    ``experiments_provenance[]`` — one entry per record: source file + SHA-256,
    the metadata each file states about itself, the metadata the fitting pipeline
    actually used, and the derived performance metrics read back out of the
    committed ``breakthrough_out/<run_id>/results_<run_id>.csv``.
``src/docs/experiments_passport.md``
    Tables 3-5 of the report, as Markdown. The docx writer consumes this file, so
    no number in §5 is ever hand-typed.

Nothing is refitted here. Every derived value is read from a committed artefact,
so running this cannot move a number that the report already quotes.

Two metadata sources per file, deliberately kept separate
---------------------------------------------------------
Each Format-D CSV states its flow rate twice: once in the prose block at cell
(0, 0) (``Flow rate: N ml/min``) and once in the numeric label/value table at
columns 8-10 (key ``v``, in L/min). ``breakthrough_fit.parse`` reads ``v``. Four
files disagree with themselves. This script reports both values and resolves
neither -- the disagreement is the finding.
"""

from __future__ import annotations

import glob
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from breakthrough_fit.parse import DataParser  # noqa: E402

REPO = Path(__file__).resolve().parents[2]
DATA_DIR = REPO / "src/solver/data/newest runs"
OUT_DIR = REPO / "breakthrough_out"
JSON_OUT = REPO / "src/docs/experiments_passport.json"
MD_OUT = REPO / "src/docs/experiments_passport.md"

FLOW_LEVELS_ML_MIN = (50, 100, 150)
CONC_LEVELS_PCT = (5, 10, 15)

# Where each run's numbers already appear in the manuscript. Established by
# matching each run's derived t_b against the values printed in the report's own
# replicate-I and replicate-II tables; every mapping below is re-verified against
# the committed artefacts at run time (see _check_reported_in), so a stale entry
# fails loudly instead of being published.
REPORTED_IN = {
    # run_id: (replicate, row, t_b printed in the report, min)
    "2026-06-26-conc5-flow0.05": ("I", 1, 23.958),
    "2026-07-03-conc5-flow0.10": ("I", 2, 10.651),
    "2026-07-08-conc5-flow0.15": ("I", 3, 4.198),
    "2026-07-08-conc10-flow0.05": ("I", 4, 19.050),
    "2026-07-08-conc10-flow0.10": ("I", 5, 5.430),
    "2026-07-08-conc10-flow0.15": ("I", 6, 3.550),
    "2026-07-10-conc15-flow0.05": ("I", 7, 17.677),
    "2026-07-10-conc15-flow0.10": ("I", 8, 4.295),
    "2026-07-15-conc15-flow0.15": ("I", 9, 2.588),
    "2026-07-29-conc5-flow0.05": ("II", 1, 30.521),
    "2026-07-29-conc5-flow0.10": ("II", 2, 9.360),
    "2026-07-31-conc5-flow0.15": ("II", 3, 3.415),
    "2026-07-22-conc10-flow0.05": ("II", 4, 20.166),
    "2026-07-31-conc10-flow0.10": ("II", 5, 4.153),
    "2026-07-22-conc10-flow0.10": ("II", 6, 3.081),
    "2026-07-17-conc15-flow0.10": ("II", 8, 5.189),
}

# Replicate-II rows with no committed CSV behind them (see §5.3 of the report).
UNTRACEABLE_ROWS = {
    ("II", 7): 17.967,
    ("II", 9): 2.843,
}


# --------------------------------------------------------------------------- #
# Raw-header reading (independent of the fitting parser, on purpose)
# --------------------------------------------------------------------------- #
def read_raw_header(path: Path) -> dict:
    """Both metadata blocks a Format-D file carries, read separately."""
    raw = pd.read_csv(path, header=None, engine="python", on_bad_lines="skip")

    hdr = None
    for i in range(min(20, len(raw))):
        if (
            str(raw.iat[i, 0]).strip() == "Time"
            and raw.shape[1] > 1
            and str(raw.iat[i, 1]).strip() == "Time (min)"
        ):
            hdr = i
            break
    if hdr is None:
        return {"format_d": False}

    table: dict[str, float] = {}
    if raw.shape[1] > 9:
        labels = raw.iloc[:hdr, 8].astype(str).str.strip().str.lower()
        values = pd.to_numeric(raw.iloc[:hdr, 9], errors="coerce")
        for label, value in zip(labels, values):
            if pd.notna(value):
                table[label] = float(value)

    prose = str(raw.iat[0, 0])

    def grab(pattern: str) -> float | None:
        m = re.search(pattern, prose, re.IGNORECASE)
        return float(m.group(1)) if m else None

    return {
        "format_d": True,
        "prose_flow_ml_min": grab(r"Flow rate:\s*([\d.]+)\s*ml"),
        "prose_mass_g": grab(r"Mass:\s*([\d.]+)\s*g"),
        "prose_bed_height_mm": grab(r"Bed height:\s*([\d.]+)\s*mm"),
        "prose_tube_diameter_mm": grab(r"Tube diameter:\s*([\d.]+)\s*mm"),
        "table_flow_ml_min": table["v"] * 1000.0 if "v" in table else None,
        "table_c0_ppm": table.get("c0"),
    }


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def nearest(value: float | None, levels: tuple) -> float | None:
    if value is None or not np.isfinite(value):
        return None
    return min(levels, key=lambda lv: abs(lv - value))


def git_commit() -> str:
    try:
        return subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=REPO, capture_output=True, text=True, check=True,
        ).stdout.strip()
    except Exception:
        return "unknown"


# --------------------------------------------------------------------------- #
# Derived metrics, read back out of the committed fit artefacts
# --------------------------------------------------------------------------- #
def read_derived(run_id: str) -> dict | None:
    hits = glob.glob(str(OUT_DIR / run_id / f"results_{run_id}.csv"))
    if not hits:
        return None
    df = pd.read_csv(hits[0])
    best = df.loc[df["AICc"].idxmin()]

    def minutes(seconds) -> float | None:
        return round(float(seconds) / 60.0, 3) if pd.notna(seconds) else None

    return {
        "n_points": int(best["n"]),
        "t_b_min": minutes(best["t_b_s"]),
        "t_E_min": minutes(best["t_E_s"]),
        "t50_min": minutes(best["t50_s"]),
        "q_dyn_mol_per_kg": round(float(best["q_dyn_mol_per_kg"]), 4),
        "L_MTZ_cm": (
            round(float(best["L_MTZ_m"]) * 100.0, 2)
            if pd.notna(best["L_MTZ_m"]) else None
        ),
        "psi": round(float(best["efficiency"]), 4) if pd.notna(best["efficiency"]) else None,
        "best_model_code": str(best["code"]),
        "best_model_name": str(best["name"]),
        "results_csv": str(Path(hits[0]).relative_to(REPO)).replace("\\", "/"),
    }


def build() -> dict:
    parser = DataParser()
    entries, excluded = [], []

    for path in sorted(DATA_DIR.glob("*.csv")):
        run_id = path.stem
        rel = str(path.relative_to(REPO)).replace("\\", "/")
        raw = read_raw_header(path)
        date = run_id[:10] if re.match(r"^\d{4}-\d{2}-\d{2}", run_id) else None

        if not raw["format_d"]:
            excluded.append({
                "run_id": run_id,
                "source_file": rel,
                "sha256": sha256(path),
                "bytes": path.stat().st_size,
                "date": date,
                "reason": "no embedded metadata header (raw Format-A sensor log): "
                          "mass, bed height and tube diameter are absent",
                "action": "excluded by the pipeline's own metadata guard, not fabricated",
                "owner": "lab",
            })
            continue

        derived = read_derived(run_id)
        if derived is None:
            excluded.append({
                "run_id": run_id,
                "source_file": rel,
                "sha256": sha256(path),
                "bytes": path.stat().st_size,
                "date": date,
                "reason": "no committed fit artefact in breakthrough_out/",
                "action": "excluded",
                "owner": "lab",
            })
            continue

        run = parser.parse(path)
        prose_flow = raw["prose_flow_ml_min"]
        table_flow = raw["table_flow_ml_min"]
        used_flow = run.flow_ml_min
        conflict = (
            prose_flow is not None
            and table_flow is not None
            and abs(prose_flow - table_flow) > 1.0
        )

        name_m = re.search(r"conc(\d+)-flow([\d.]+)", run_id)
        entries.append({
            "run_id": run_id,
            "source_file": rel,
            "sha256": sha256(path),
            "bytes": path.stat().st_size,
            "date": date,
            "filename_states": {
                "C0_pct": int(name_m.group(1)) if name_m else None,
                "Q_lpm": float(name_m.group(2)) if name_m else None,
            },
            "measured": {
                "C0_ppm": round(float(run.c0_ppm), 0) if run.c0_ppm else None,
                "mass_g": run.mass_g,
                "L_bed_cm": run.bed_height_cm,
                "d_col_mm": run.tube_diameter_mm,
                "T_K": round(float(run.temperature_K), 1) if run.temperature_K else None,
                "P_Pa": run.pressure_Pa,
                "n_points": derived["n_points"],
            },
            "flow_ml_min": {
                "prose_header": prose_flow,
                "metadata_table": table_flow,
                "used_by_pipeline": used_flow,
                "status": "CONFLICT" if conflict else "consistent",
                "owner": "lab" if conflict else None,
            },
            "design_cell": {
                "C0_nominal_pct": nearest(
                    (run.c0_ppm or 0) / 1e4, CONC_LEVELS_PCT
                ),
                "Q_nominal_ml_min": nearest(prose_flow, FLOW_LEVELS_ML_MIN),
                "basis": "prose header flow + measured C0",
            },
            "derived": {
                **{k: v for k, v in derived.items() if k != "results_csv"},
                "definitions": {"t_b": "C/C0 = 0.05", "t_E": "C/C0 = 0.95"},
                "provisional": bool(conflict),
                "provisional_reason": (
                    "q_dyn, L_MTZ and psi scale with volumetric flow; this run was "
                    "fitted at the numeric-table flow, which its own prose header "
                    "contradicts" if conflict else None
                ),
            },
            "reported_in": None,   # filled below
            "artefacts": {
                "results_csv": derived["results_csv"],
                "plots": sorted(
                    str(p.relative_to(REPO)).replace("\\", "/")
                    for p in (OUT_DIR / run_id).glob("P?_*.png")
                ),
            },
            "status": "included",
        })

    _attach_reported_in(entries)
    _check_reported_in(entries)

    return {
        "passport_version": "1.0",
        "campaign": "newest runs (2026-06-26 to 2026-07-31)",
        "column_id_mm": 8.2,
        "generated_by": "src/solver/build_experiments_passport.py",
        "generated_at_commit": git_commit(),
        "source_of_derived_values": "breakthrough_out/<run_id>/results_<run_id>.csv "
                                    "(committed; nothing is refitted here)",
        "n_records": len(entries) + len(excluded),
        "n_included": len(entries),
        "n_excluded": len(excluded),
        "experiments_provenance": entries,
        "excluded": excluded,
        "untraceable_reported_rows": [
            {
                "replicate": rep,
                "row": row,
                "t_b_min_printed": t_b,
                "issue": "no committed CSV in `newest runs/` reproduces this row",
                "owner": "author / lab",
            }
            for (rep, row), t_b in sorted(UNTRACEABLE_ROWS.items())
        ],
    }


def _attach_reported_in(entries: list[dict]) -> None:
    for e in entries:
        hit = REPORTED_IN.get(e["run_id"])
        if hit:
            rep, row, printed = hit
            e["reported_in"] = {
                "replicate": rep,
                "row": row,
                "t_b_min_printed": printed,
            }


def _check_reported_in(entries: list[dict]) -> None:
    """Fail loudly if a hardcoded report mapping no longer matches the artefacts."""
    problems = []
    for e in entries:
        r = e["reported_in"]
        if r is None:
            problems.append(f"{e['run_id']}: not mapped to any reported row")
            continue
        derived = e["derived"]["t_b_min"]
        if derived is None or abs(derived - r["t_b_min_printed"]) > 0.05:
            problems.append(
                f"{e['run_id']}: report prints t_b={r['t_b_min_printed']} min, "
                f"artefact gives {derived} min"
            )
    if problems:
        raise SystemExit(
            "report-mapping check failed:\n  " + "\n  ".join(problems)
        )
    print(f"[check] all {len(entries)} runs map to a printed t_b within 0.05 min  OK")


# --------------------------------------------------------------------------- #
# Markdown rendering -- this is what the docx writer reads
# --------------------------------------------------------------------------- #
def design_matrix(entries: list[dict]) -> list[list[str]]:
    counts: dict[tuple, int] = {}
    for e in entries:
        cell = (e["design_cell"]["Q_nominal_ml_min"], e["design_cell"]["C0_nominal_pct"])
        counts[cell] = counts.get(cell, 0) + 1
    rows = [["Flow rate (ml/min)", "5 % CO2", "10 % CO2", "15 % CO2", "Total"]]
    for q in FLOW_LEVELS_ML_MIN:
        cells = [counts.get((q, c), 0) for c in CONC_LEVELS_PCT]
        rows.append([f"{q} ({q/1000:.2f} lpm)"] + [str(n) for n in cells] + [str(sum(cells))])
    totals = [sum(counts.get((q, c), 0) for q in FLOW_LEVELS_ML_MIN) for c in CONC_LEVELS_PCT]
    rows.append(["Total"] + [str(n) for n in totals] + [str(sum(totals))])
    return rows


def inventory_rows(entries: list[dict]) -> list[list[str]]:
    # The source file is <run>.csv, so a separate column would only repeat the run
    # id; the directory is given in the caption instead. Page width is 5.9 in.
    header = [
        "No.", "Run (date-conc-flow)", "Q header (ml/min)",
        "Q fitted (ml/min)", "C0 (ppm)", "m (g)", "L_bed (cm)", "d_col (mm)",
        "n pts", "Best model (AICc)", "Reported in",
    ]
    rows = [header]
    order = sorted(entries, key=lambda e: (e["reported_in"]["replicate"], e["reported_in"]["row"]))
    for i, e in enumerate(order, start=1):
        f = e["flow_ml_min"]
        m = e["measured"]
        r = e["reported_in"]
        q_hdr = f"{f['prose_header']:.0f}" if f["prose_header"] else "--"
        q_fit = f"{f['used_by_pipeline']:.0f}" if f["used_by_pipeline"] else "--"
        if f["status"] == "CONFLICT":
            q_hdr += " *"
            q_fit += " *"
        rows.append([
            str(i),
            e["run_id"],
            q_hdr,
            q_fit,
            f"{m['C0_ppm']:,.0f}".replace(",", " "),
            f"{m['mass_g']:.1f}",
            f"{m['L_bed_cm']:.1f}",
            f"{m['d_col_mm']:.1f}",
            str(m["n_points"]),
            e["derived"]["best_model_code"],
            f"Table 10, row {r['row']}" if r["replicate"] == "II" else f"Table 9, row {r['row']}",
        ])
    return rows


def flagged_rows(passport: dict) -> list[list[str]]:
    rows = [["Record", "Issue", "Consequence", "Owner"]]
    for e in passport["excluded"]:
        rows.append([
            Path(e["source_file"]).name,
            e["reason"],
            e["action"],
            e["owner"] or "--",
        ])
    conflicts = [
        e for e in passport["experiments_provenance"]
        if e["flow_ml_min"]["status"] == "CONFLICT"
    ]
    for e in conflicts:
        f = e["flow_ml_min"]
        rows.append([
            Path(e["source_file"]).name,
            f"prose header states {f['prose_header']:.0f} ml/min; the numeric "
            f"metadata cell the parser reads states {f['metadata_table']:.0f} ml/min",
            f"fitted at {f['used_by_pipeline']:.0f} ml/min, so q_dyn, L_MTZ and psi "
            f"for this run are provisional; t_b is unaffected",
            "lab",
        ])
    for e in passport["experiments_provenance"]:
        if e["derived"]["t_E_min"] is None:
            rows.append([
                Path(e["source_file"]).name,
                "outlet never reaches C/C0 = 0.95",
                "t_E and L_MTZ undefined; capacity integrated over a truncated "
                "window; dropped pairwise, never imputed",
                "lab",
            ])
    for u in passport["untraceable_reported_rows"]:
        rows.append([
            f"Table 10, row {u['row']} (replicate {u['replicate']})",
            u["issue"] + f" (t_b = {u['t_b_min_printed']} min as printed)",
            "retained as recorded; not reproducible from the committed data set",
            u["owner"],
        ])
    return rows


def render_md(passport: dict) -> str:
    def table(rows: list[list[str]]) -> str:
        head, *body = rows
        out = ["| " + " | ".join(head) + " |",
               "|" + "|".join("---" for _ in head) + "|"]
        out += ["| " + " | ".join(r) + " |" for r in body]
        return "\n".join(out)

    entries = passport["experiments_provenance"]
    n_conflict = sum(
        1 for e in entries if e["flow_ml_min"]["status"] == "CONFLICT"
    )
    return f"""# Experiments passport — rendered tables

Generated by `{passport['generated_by']}` at commit `{passport['generated_at_commit'][:12]}`.
Do not edit by hand; edit the generator.

Campaign: {passport['campaign']} · {passport['n_records']} records ·
{passport['n_included']} usable · {passport['n_excluded']} excluded ·
{n_conflict} with a self-contradicting flow header.

## Table 3 — design as executed

{table(design_matrix(entries))}

## Table 4 — run inventory and provenance

{table(inventory_rows(entries))}

`*` = the file's prose header and its numeric metadata cell state different flow
rates; the fitted value is the one the pipeline used. See Table 5.

## Table 5 — excluded and flagged records

{table(flagged_rows(passport))}
"""


def main() -> int:
    if not DATA_DIR.is_dir():
        raise SystemExit(f"data directory not found: {DATA_DIR}")
    passport = build()

    JSON_OUT.write_text(json.dumps(passport, indent=2), encoding="utf-8")
    MD_OUT.write_text(render_md(passport), encoding="utf-8")

    print(f"\n{passport['n_records']} records: {passport['n_included']} included, "
          f"{passport['n_excluded']} excluded")
    print(f"wrote {JSON_OUT.relative_to(REPO)}")
    print(f"wrote {MD_OUT.relative_to(REPO)}\n")

    for line in render_md(passport).splitlines():
        print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

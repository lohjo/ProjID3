"""Redraw P1-P7 for the sixteen grid runs without touching any results CSV.

    python src/solver/regen_grid_figs.py            # dry run
    python src/solver/regen_grid_figs.py --apply    # write the PNGs

Why a separate driver
---------------------
``plots.py`` draws from :class:`FitResult` objects -- it needs ``y_pred`` -- so
there is no draw-from-CSV path and the runs genuinely have to be refitted. But
``new_runs_pipeline.run_one`` also rewrites ``results_<run_id>.csv``, and nine of
the sixteen results files in the repo-root ``breakthrough_out/`` tree carry
unresolved git merge-conflict markers whose resolution is the author's call
(CLAUDE.md, data-basis section). A figure-only pass must not overwrite them.

So, following ``src/docs/review/_source/regen_truncated_p7.py``: point the
pipeline's ``OUT_DIR`` at a scratch directory, let it write whatever it likes
*there*, and copy only the PNGs back. Nothing under the repo is written by the
pipeline itself.

The reproduction gate
---------------------
The refit is seeded (``ModelFitter(n_starts=12, seed=42)``) and must land on the
committed optimum. Every run's scratch CSV is compared against the committed
``src/solver/breakthrough_out/<run_id>/results_<run_id>.csv`` -- the clean tree,
per CLAUDE.md -- across all numeric columns. If any run drifts past ``TOL`` the
whole pass aborts and nothing is written, because a figure that disagrees with
the committed statistics is worse than an ugly one. ``regen_truncated_p7.py``
reproduced to 8.6e-7 on this same code path, so the tolerance is set to match.

Both ``breakthrough_out`` trees receive the same PNG: one fit, two writes.
"""

from __future__ import annotations

import argparse
import shutil
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(HERE))

import pandas as pd  # noqa: E402

DATA_DIR = REPO / "src" / "solver" / "data" / "newest runs"
TREES = [REPO / "breakthrough_out", REPO / "src" / "solver" / "breakthrough_out"]
REFERENCE_TREE = REPO / "src" / "solver" / "breakthrough_out"

# Column set from regen_truncated_p7.py, but split by tolerance.
#
# Everything that decides what a figure shows -- the sums of squares and the
# information criteria -- must reproduce tightly, and does: measured worst case
# over 16 runs x 24 models is RSS 6.1e-9, R2 9.7e-12, RMSE 3.0e-9, AICc 6.8e-10.
#
# AAD is the exception, drifting up to 5.4e-5. That is expected rather than
# alarming: AAD averages |residual|, and the kink of the absolute value at zero
# means residuals that straddle zero amplify last-bit differences in the fitted
# parameters, where RSS squares the same noise away. It is a reported diagnostic,
# not an input to any ranking or curve, so it gets its own looser bound instead of
# relaxing the bound on everything.
NUMERIC = ["n", "p", "RSS", "R2", "AdjR2", "RMSE", "chi2_red", "AIC", "AICc"]
TOL = 1e-6
LOOSE = {"AAD": 1e-3}

PLOTS = [f"P{i}" for i in range(1, 8)]


def _rel(a: pd.DataFrame, b: pd.DataFrame, col: str) -> pd.Series:
    x, y = a[col].astype(float), b[col].astype(float)
    denom = x.abs().where(x.abs() > 0, 1.0)
    return ((x - y).abs() / denom).fillna(0.0)


def compare(reference: Path, fresh: Path) -> tuple[float, str, list[str]]:
    """Compare two results tables.

    Returns the worst relative difference among the tight columns, where it sits,
    and a list of gate violations (tight columns, loose columns, and the AICc
    ranking, which is what P1's top-8 selection and the ranked tables depend on).
    """
    a = pd.read_csv(reference).set_index("code").sort_index()
    b = pd.read_csv(fresh).set_index("code").sort_index()
    if list(a.index) != list(b.index):
        raise SystemExit(f"model set changed for {reference.parent.name}")

    violations: list[str] = []
    worst, where = 0.0, ""
    for col in NUMERIC:
        rel = _rel(a, b, col)
        if rel.max() > worst:
            worst, where = float(rel.max()), f"{col} @ {rel.idxmax()}"
        if rel.max() > TOL:
            violations.append(f"{col} {rel.max():.3e} @ {rel.idxmax()} (> {TOL:g})")
    for col, tol in LOOSE.items():
        rel = _rel(a, b, col)
        if rel.max() > tol:
            violations.append(f"{col} {rel.max():.3e} @ {rel.idxmax()} (> {tol:g})")

    # Ranking identity: same winner and same full AICc order, not just close numbers.
    if list(a["AICc"].sort_values().index) != list(b["AICc"].sort_values().index):
        violations.append(
            f"AICc ranking changed ({a['AICc'].idxmin()} -> {b['AICc'].idxmin()})")

    return worst, where, violations


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true",
                    help="copy the regenerated PNGs into both trees "
                         "(default: refit, gate, and report only)")
    args = ap.parse_args(argv)

    import new_runs_pipeline as P
    from breakthrough_fit.fit import ModelFitter
    from breakthrough_fit.parse import DataParser
    from PIL import Image

    scratch = Path(tempfile.mkdtemp(prefix="regen_grid_"))
    P.OUT_DIR = scratch
    print(f"scratch out_dir: {scratch}")
    print(f"reference tree : {REFERENCE_TREE.relative_to(REPO)}")
    print(f"tolerance      : {TOL:g} relative\n")

    sources = sorted(DATA_DIR.glob("*.csv"))
    print(f"{len(sources)} source CSVs in '{DATA_DIR.name}'")

    parser, fitter = DataParser(), ModelFitter(n_starts=12, seed=42)
    for fpath in sources:
        P.run_one(fpath, parser, fitter)

    produced = sorted(d for d in scratch.iterdir() if d.is_dir())
    print(f"\n{'=' * 78}\nREPRODUCTION GATE\n{'=' * 78}")
    print(f"{len(produced)} runs produced output "
          f"({len(sources) - len(produced)} skipped for missing metadata)\n")

    failures: list[str] = []
    worst_overall, worst_run = 0.0, ""
    for d in produced:
        run_id = d.name
        fresh_csv = d / f"results_{run_id}.csv"
        ref_csv = REFERENCE_TREE / run_id / f"results_{run_id}.csv"
        if not ref_csv.exists():
            failures.append(f"{run_id}: no committed reference at {ref_csv}")
            continue
        worst, where, violations = compare(ref_csv, fresh_csv)
        if worst > worst_overall:
            worst_overall, worst_run = worst, run_id

        missing = [p for p in PLOTS if not (d / f"{p}_{run_id}.png").exists()]
        bad = []
        for p in PLOTS:
            png = d / f"{p}_{run_id}.png"
            if png.exists():
                try:
                    im = Image.open(png)
                    im.load()
                except Exception as exc:      # truncated / corrupt write
                    bad.append(f"{p} ({exc})")

        status = "ok"
        if violations:
            status = "DRIFT"
            failures.extend(f"{run_id}: {v}" for v in violations)
        if missing:
            status = "MISSING"
            failures.append(f"{run_id}: missing {', '.join(missing)}")
        if bad:
            status = "CORRUPT"
            failures.append(f"{run_id}: undecodable {', '.join(bad)}")
        print(f"  {status:<8} {run_id:<28} max rel {worst:.3e}  ({where})")

    print(f"\nworst across all runs (tight columns): {worst_overall:.3e} in {worst_run}")

    if failures:
        print(f"\n[ABORT] {len(failures)} problem(s); nothing written:", file=sys.stderr)
        for f in failures:
            print(f"  {f}", file=sys.stderr)
        return 1
    print("gate PASSED — every refit reproduces the committed optimum")

    print(f"\n{'=' * 78}\n{'COPY' if args.apply else 'DRY RUN'}\n{'=' * 78}")
    copied = 0
    for d in produced:
        run_id = d.name
        for p in PLOTS:
            src = d / f"{p}_{run_id}.png"
            for tree in TREES:
                dst = tree / run_id / f"{p}_{run_id}.png"
                if not dst.parent.is_dir():
                    print(f"  [skip] no such run dir: {dst.parent.relative_to(REPO)}")
                    continue
                if args.apply:
                    shutil.copy2(src, dst)
                copied += 1
    print(f"  {'copied' if args.apply else 'would copy'} {copied} PNGs "
          f"into {len(TREES)} trees")

    if args.apply:
        checked = 0
        for d in produced:
            run_id = d.name
            for p in PLOTS:
                for tree in TREES:
                    dst = tree / run_id / f"{p}_{run_id}.png"
                    if dst.exists():
                        im = Image.open(dst)
                        im.load()
                        checked += 1
        print(f"  verified: {checked} written PNGs decode cleanly")
        shutil.rmtree(scratch, ignore_errors=True)
    else:
        print(f"\ndry run: nothing written. Scratch kept at {scratch}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

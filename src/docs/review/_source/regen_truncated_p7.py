"""Regenerate the one truncated figure: P7_2026-07-03-conc5-flow0.10.png.

The committed PNG is 852,244 bytes and ends mid-stream ("image file is
truncated"), in both `breakthrough_out/` and `src/solver/breakthrough_out/`.
Nothing else about that run is damaged.

This re-runs the pipeline for that single CSV into a scratch directory, then
(a) verifies the regenerated results CSV matches the committed one, so we know
the refit landed on the same optimum, and (b) copies only the P7 PNG back over
the two truncated copies. No committed results CSV is touched.

    python src/docs/review/_source/regen_truncated_p7.py [--apply]
"""
from __future__ import annotations

import argparse
import shutil
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
sys.path.insert(0, str(REPO / "src" / "solver"))

import pandas as pd  # noqa: E402

RUN_ID = "2026-07-03-conc5-flow0.10"
SRC_CSV = REPO / "src/solver/data/newest runs" / f"{RUN_ID}.csv"
TARGETS = [
    REPO / "breakthrough_out" / RUN_ID / f"P7_{RUN_ID}.png",
    REPO / "src/solver/breakthrough_out" / RUN_ID / f"P7_{RUN_ID}.png",
]
REFERENCE_CSV = REPO / "src/solver/breakthrough_out" / RUN_ID / f"results_{RUN_ID}.csv"

NUMERIC = ["n", "p", "RSS", "R2", "AdjR2", "RMSE", "chi2_red", "AIC", "AICc", "AAD"]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true",
                    help="overwrite the two truncated PNGs (default: dry run)")
    args = ap.parse_args()

    if not SRC_CSV.exists():
        raise SystemExit(f"raw run not found: {SRC_CSV}")

    import new_runs_pipeline as P
    from breakthrough_fit.fit import ModelFitter
    from breakthrough_fit.parse import DataParser

    scratch = Path(tempfile.mkdtemp(prefix="regen_p7_"))
    P.OUT_DIR = scratch
    print(f"scratch out_dir: {scratch}")

    P.run_one(SRC_CSV, DataParser(), ModelFitter(n_starts=12, seed=42))

    new_png = scratch / RUN_ID / f"P7_{RUN_ID}.png"
    new_csv = scratch / RUN_ID / f"results_{RUN_ID}.csv"
    if not new_png.exists():
        raise SystemExit("P7 was not produced")

    # Sanity: the refit must land on the committed optimum, or we do not use it.
    a = pd.read_csv(REFERENCE_CSV).set_index("code").sort_index()
    b = pd.read_csv(new_csv).set_index("code").sort_index()
    assert list(a.index) == list(b.index), "model set changed"
    worst = 0.0
    worst_where = ""
    for col in NUMERIC:
        x, y = a[col].astype(float), b[col].astype(float)
        denom = x.abs().where(x.abs() > 0, 1.0)
        rel = ((x - y).abs() / denom).fillna(0.0)
        if rel.max() > worst:
            worst, worst_where = float(rel.max()), f"{col} @ {rel.idxmax()}"
    print(f"\nrefit vs committed: max relative difference "
          f"{worst:.3e} ({worst_where}) over {len(a)} models x {len(NUMERIC)} columns")
    if worst > 1e-6:
        raise SystemExit("refit does not reproduce the committed optimum - not applying")

    # Verify the new PNG actually decodes end to end.
    from PIL import Image
    im = Image.open(new_png)
    im.load()
    print(f"regenerated P7: {im.size[0]}x{im.size[1]} px, {new_png.stat().st_size:,} bytes")

    for t in TARGETS:
        old = t.stat().st_size if t.exists() else 0
        print(f"  {'overwrite' if args.apply else 'would overwrite'} "
              f"{t.relative_to(REPO)}  {old:,} -> {new_png.stat().st_size:,} bytes")
        if args.apply:
            shutil.copy2(new_png, t)

    if args.apply:
        for t in TARGETS:
            im = Image.open(t)
            im.load()
        print("\nboth copies decode cleanly")
    else:
        print("\ndry run: nothing written (pass --apply)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

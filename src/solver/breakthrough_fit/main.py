"""Command-line entry point.

Usage::

    python -m breakthrough_fit.main \
        --data "src/solver/data/*.csv" \
        --c0 39900 \
        --flow 50 \
        --mass 4 \
        --column-diameter 3.37 \
        --column-length 32.5 \
        --temperature 296.15 \
        --pressure 101325 \
        --bed-void 0.37

Outputs (per run):
    * a ranked statistics table printed to stdout (tabulate, plain text);
    * 7 PNG figures ``P1_<run>.png … P7_<run>.png``;
    * a CSV ``results_<run>.csv`` with parameters and statistics.
"""

from __future__ import annotations

import argparse
import glob
import sys
from pathlib import Path

import numpy as np
import pandas as pd

try:
    from tabulate import tabulate as _tabulate
except ImportError:  # pragma: no cover
    def _tabulate(rows, headers, tablefmt="plain"):
        return pd.DataFrame(rows, columns=list(headers)).to_string(index=False)

try:
    from tqdm import tqdm as _tqdm  # type: ignore
except ImportError:  # pragma: no cover
    def _tqdm(it, **_kwargs):
        return it

from . import isotherm, performance
from .fit import ModelFitter, NESTED_PAIRS, nested_ftests
from .parse import DataParser
from .plots import plot_P1, plot_P2, plot_P3, plot_P4, plot_P5, plot_P6, plot_P7


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def _build_argparser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(description="Fit breakthrough models to CO2 data.")
    ap.add_argument("--data", required=True,
                    help="Glob pattern or path to CSV file(s).")
    ap.add_argument("--c0", type=float, default=None,
                    help="Inlet C0 in ppm.  Overrides anything in the CSV.")
    ap.add_argument("--flow", type=float, default=None,
                    help="Volumetric flow rate in mL/min.")
    ap.add_argument("--mass", type=float, default=None,
                    help="Adsorbent mass in grams.")
    ap.add_argument("--column-diameter", type=float, default=3.37,
                    help="Column inner diameter in cm.")
    ap.add_argument("--column-length", type=float, default=32.5,
                    help="Packed-bed length in cm.")
    ap.add_argument("--temperature", type=float, default=298.0,
                    help="Operating temperature in K.")
    ap.add_argument("--pressure", type=float, default=101_325.0,
                    help="Operating pressure in Pa.")
    ap.add_argument("--bed-void", type=float, default=0.37,
                    help="Bed void fraction.")
    ap.add_argument("--rho-b", type=float, default=700.0,
                    help="Bulk density of the packed bed in kg/m³ "
                         "(used by Chern–Chien only).")
    ap.add_argument("--out", default="breakthrough_out",
                    help="Output directory for figures and CSVs.")
    ap.add_argument("--top-n", type=int, default=8,
                    help="How many models to overlay in P1.")
    ap.add_argument("--no-plots", action="store_true",
                    help="Skip figure generation (statistics only).")
    return ap


def _resolve_paths(pattern: str) -> list[Path]:
    p = Path(pattern)
    if p.exists():
        return [p]
    matches = [Path(m) for m in glob.glob(pattern)]
    if not matches:
        raise FileNotFoundError(f"No files match {pattern!r}")
    return sorted(matches)


def _print_versions() -> None:
    import scipy
    import matplotlib
    print(f"python    {sys.version.split()[0]}")
    print(f"numpy     {np.__version__}")
    print(f"scipy     {scipy.__version__}")
    print(f"pandas    {pd.__version__}")
    print(f"mpl       {matplotlib.__version__}")


# ---------------------------------------------------------------------------
# Per-run pipeline
# ---------------------------------------------------------------------------
def run_one(args, path: Path, parser: DataParser, fitter: ModelFitter) -> None:
    run = parser.parse(path, c0_override=args.c0)
    df = run.df
    print(f"\n=== {run.run_id}  ({run.fmt})  n={len(df)}  C0={run.c0_ppm:.1f} ppm ===")
    if len(df) < 10:
        print(f"  skipped: only {len(df)} usable rows.")
        return

    # Geometry & flow conversions.
    d_c_m = args.column_diameter * 1e-2
    L_bed_m = args.column_length * 1e-2
    A_c = np.pi * (d_c_m / 2.0) ** 2
    flow_ml_min = args.flow if args.flow is not None else run.flow_ml_min
    if flow_ml_min is None:
        flow_m3_s = float("nan")
        u = float("nan")
        v = float("nan")
    else:
        flow_m3_s = flow_ml_min * 1e-6 / 60.0
        u = flow_m3_s / A_c
        v = u / max(args.bed_void, 1e-9)
    T_K = run.temperature_K or args.temperature
    P_Pa = run.pressure_Pa or args.pressure
    c0_mol_m3 = isotherm.ppm_to_mol_m3(run.c0_ppm, T_K=T_K, P_Pa=P_Pa)
    mass_kg = (args.mass / 1000.0) if args.mass else float("nan")

    # Fit every model.
    results = fitter.fit_all(df, progress=lambda it: _tqdm(it, desc="fit", leave=False))

    # Ranked statistics table.
    rows: list[dict] = []
    for code, r in results.items():
        s = r.stats
        rows.append({
            "code": code,
            "name": r.name,
            "p": r.stats.p,
            "R2": s.r2,
            "AdjR2": s.adj_r2,
            "RMSE": s.rmse,
            "chi2_red": s.chi2_red,
            "AICc": s.aicc,
            "W_AICc": s.aic_weight,
            "AAD": s.aad,
            "ok": r.converged,
        })
    table = (
        pd.DataFrame(rows)
        .sort_values("AICc", na_position="last")
        .reset_index(drop=True)
    )
    print(
        _tabulate(
            table.values.tolist(),
            headers=list(table.columns),
            tablefmt="plain",
        )
    )

    # Nested F-tests.
    ftests = nested_ftests(results, n=len(df))
    if not ftests.empty:
        print("\nNested F-tests:")
        print(
            _tabulate(
                ftests.values.tolist(),
                headers=list(ftests.columns),
                tablefmt="plain",
            )
        )

    # Performance metrics + isotherm-back-calc.
    t_arr = df["t"].to_numpy(dtype=float)
    y_arr = df["C_C0"].to_numpy(dtype=float)
    perf = performance.metrics(
        t_arr, y_arr, flow_m3_s, c0_mol_m3, mass_kg, L_bed_m
    )
    print(
        f"\nPerformance: t_b={perf.t_b:0.1f}s  t_E={perf.t_E:0.1f}s  "
        f"t50={perf.t50:0.1f}s  q_dyn={perf.q_dyn_mol_per_kg:0.4g} mol/kg  "
        f"L_MTZ={perf.L_MTZ_m*100:0.2f} cm  psi={perf.efficiency:0.3f}"
    )

    r01 = results.get("M01")
    if r01 is not None and r01.converged and np.isfinite(flow_m3_s) and np.isfinite(mass_kg):
        k_YN, tau = r01.params
        q0_YN = isotherm.back_calculate_q0(tau, flow_m3_s, c0_mol_m3, mass_kg)
        print(f"q0 from YN tau : {q0_YN:0.4g} mol/kg")

    # Persist results.
    out_dir = Path(args.out) / run.run_id
    out_dir.mkdir(parents=True, exist_ok=True)
    _write_csv(out_dir / f"results_{run.run_id}.csv", run, results, perf)

    if args.no_plots:
        return

    # Diagnostic plots.
    plot_P1(run.run_id, results, out_dir=out_dir, top_n=args.top_n)
    plot_P2(run.run_id, df, results, out_dir=out_dir)
    plot_P3(run.run_id, df, results, out_dir=out_dir)
    plot_P4(run.run_id, df, results, out_dir=out_dir)
    if np.isfinite(v):
        plot_P5(run.run_id, results, L_bed_m=L_bed_m,
                v_interstitial=v, out_dir=out_dir)
    plot_P6(run.run_id, df, results, out_dir=out_dir)
    plot_P7(run.run_id, df, results, out_dir=out_dir)


# ---------------------------------------------------------------------------
# CSV export
# ---------------------------------------------------------------------------
def _write_csv(path: Path, run, results, perf) -> None:
    rows: list[dict] = []
    for code, r in results.items():
        s = r.stats
        param_blob = ";".join(
            f"{n}={v:0.6g}" for n, v in zip(r.param_names, r.params)
        )
        stderr_blob = ";".join(
            f"{n}={se:0.6g}" for n, se in zip(r.param_names, r.stderr)
        )
        rows.append({
            "run_id": run.run_id,
            "fmt": run.fmt,
            "code": code,
            "name": r.name,
            "converged": r.converged,
            "n": s.n,
            "p": s.p,
            "RSS": s.rss,
            "R2": s.r2,
            "AdjR2": s.adj_r2,
            "RMSE": s.rmse,
            "chi2_red": s.chi2_red,
            "AIC": s.aic,
            "AICc": s.aicc,
            "W_AICc": s.aic_weight,
            "AAD": s.aad,
            "params": param_blob,
            "stderr": stderr_blob,
            "message": r.message,
            "t_b": perf.t_b,
            "t_E": perf.t_E,
            "t50": perf.t50,
            "q_dyn_mol_per_kg": perf.q_dyn_mol_per_kg,
            "L_MTZ_m": perf.L_MTZ_m,
            "efficiency": perf.efficiency,
        })
    pd.DataFrame(rows).to_csv(path, index=False)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
def main(argv=None) -> int:
    args = _build_argparser().parse_args(argv)
    _print_versions()
    parser = DataParser()
    fitter = ModelFitter(n_starts=10, seed=42)

    paths = _resolve_paths(args.data)
    print(f"\nFound {len(paths)} file(s).")
    for path in paths:
        try:
            run_one(args, path, parser, fitter)
        except Exception as exc:  # noqa: BLE001
            print(f"!! {path}: {exc}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

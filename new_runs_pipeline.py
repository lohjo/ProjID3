"""Pipeline for new experimental runs (runs 3/4/5/6/8).

Usage (from repo root, venv activated)::

    python new_runs_pipeline.py

Outputs per run in ``breakthrough_out/run <N>/``:
    * results_run <N>.csv  — all 24 model fits + performance metrics
    * P1–P7 plots at 150 dpi
    * console: ranked AICc table + nested F-tests + performance summary
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Per-run metadata (measurements block: per-run mass/length + pressure-drop
# table). Column geometry fixed: d_c = 8.5 mm, T = 298 K, P = 101325 Pa.
# Inlet flow (Q_lpm) is the authoritative "inlet flow" column of the
# adsorption pressure-drop table: run3=0.15, run4=0.05, run5=0.10,
# run6=0.15, run8=0.10 lpm. (run6/run8 corrected 2026-05-31 from 0.05/0.125.)
# ---------------------------------------------------------------------------
RUN_META: dict[str, dict] = {
    "run 3": dict(Q_lpm=0.15, m_g=8.0076, L_bed_cm=21.0),
    "run 4": dict(Q_lpm=0.05, m_g=8.0000, L_bed_cm=21.3),
    "run 5": dict(Q_lpm=0.10, m_g=8.0000, L_bed_cm=21.2),
    "run 6": dict(Q_lpm=0.15, m_g=8.0000, L_bed_cm=21.5),
    "run 8": dict(Q_lpm=0.10, m_g=8.0000, L_bed_cm=21.5),
}

D_COL_M   = 0.0085          # inner diameter [m]
T_K       = 298.0            # operating temperature [K]
P_PA      = 101_325.0        # operating pressure [Pa]
DATA_DIR  = Path("src/solver/data/new runs")
OUT_DIR   = Path("breakthrough_out")

# ---------------------------------------------------------------------------
# Imports (after venv path is set)
# ---------------------------------------------------------------------------
try:
    from tabulate import tabulate as _tabulate
except ImportError:
    def _tabulate(rows, headers, tablefmt="plain"):
        return pd.DataFrame(rows, columns=list(headers)).to_string(index=False)

try:
    from tqdm import tqdm as _tqdm
except ImportError:
    def _tqdm(it, **_kwargs): return it

from breakthrough_fit import isotherm, performance
from breakthrough_fit.fit import ModelFitter, nested_ftests
from breakthrough_fit.parse import DataParser
from breakthrough_fit.plots import plot_P1, plot_P2, plot_P3, plot_P4, plot_P5, plot_P6, plot_P7


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def _write_csv(path: Path, run, results, perf) -> None:
    rows = []
    for code, r in results.items():
        s = r.stats
        param_blob  = ";".join(f"{n}={v:.6g}" for n, v in zip(r.param_names, r.params))
        stderr_blob = ";".join(f"{n}={se:.6g}" for n, se in zip(r.param_names, r.stderr))
        rows.append({
            "run_id": run.run_id, "fmt": run.fmt, "code": code, "name": r.name,
            "converged": r.converged, "n": s.n, "p": s.p, "RSS": s.rss,
            "R2": s.r2, "AdjR2": s.adj_r2, "RMSE": s.rmse, "chi2_red": s.chi2_red,
            "AIC": s.aic, "AICc": s.aicc, "W_AICc": s.aic_weight, "AAD": s.aad,
            "params": param_blob, "stderr": stderr_blob, "message": r.message,
            "t_b_s": perf.t_b, "t_E_s": perf.t_E, "t50_s": perf.t50,
            "q_dyn_mol_per_kg": perf.q_dyn_mol_per_kg,
            "L_MTZ_m": perf.L_MTZ_m, "efficiency": perf.efficiency,
        })
    pd.DataFrame(rows).to_csv(path, index=False)


# ---------------------------------------------------------------------------
# Per-run processing
# ---------------------------------------------------------------------------
def run_one(run_id: str, fpath: Path, parser: DataParser, fitter: ModelFitter) -> None:
    meta = RUN_META[run_id]
    Q_lpm    = meta["Q_lpm"]
    m_g      = meta["m_g"]
    L_bed_cm = meta["L_bed_cm"]

    run = parser.parse(fpath)
    df  = run.df
    print(f"\n{'='*70}")
    print(f"Run: {run.run_id}  fmt={run.fmt}  n={len(df)}  C0={run.c0_ppm:.0f} ppm")
    print(f"     Q={Q_lpm} lpm | m={m_g} g | L_bed={L_bed_cm} cm | d_c={D_COL_M*1000:.1f} mm")
    if len(df) < 10:
        print(f"  skipped: only {len(df)} usable rows.")
        return

    # Geometry
    A_c       = np.pi * (D_COL_M / 2.0) ** 2
    L_bed_m   = L_bed_cm * 1e-2
    flow_m3_s = Q_lpm * 1e-3 / 60.0
    u         = flow_m3_s / A_c
    rho_b     = (m_g * 1e-3) / (A_c * L_bed_m)
    eps_b     = max(1.0 - rho_b / 800.0, 0.3)   # ρ_p = 800 kg/m³ assumed
    v_int     = u / max(eps_b, 1e-6)
    c0_mol_m3 = isotherm.ppm_to_mol_m3(run.c0_ppm, T_K=T_K, P_Pa=P_PA)
    mass_kg   = m_g * 1e-3

    print(f"     A_c={A_c*1e4:.4f} cm2  rho_b={rho_b:.1f} kg/m3  eps={eps_b:.4f}")
    print(f"     u={u*100:.4f} cm/s  v_int={v_int*100:.4f} cm/s")

    # Fit all models
    results = fitter.fit_all(df, progress=lambda it: _tqdm(it, desc=run_id, leave=False))

    # Ranked AICc table
    rows = []
    for code, r in results.items():
        s = r.stats
        rows.append({
            "code": code, "name": r.name, "p": s.p,
            "AdjR2": s.adj_r2, "RMSE": s.rmse, "AICc": s.aicc,
            "W_AICc": s.aic_weight, "chi2_nu": s.chi2_red, "ok": r.converged,
        })
    table = (
        pd.DataFrame(rows)
        .sort_values("AICc", na_position="last")
        .reset_index(drop=True)
    )
    print("\nModel rankings (sorted by AICc):")
    print(_tabulate(table.values.tolist(), headers=list(table.columns), tablefmt="plain"))

    # Nested F-tests
    ftests = nested_ftests(results, n=len(df))
    if not ftests.empty:
        print("\nNested F-tests (logistic family):")
        print(_tabulate(ftests.values.tolist(), headers=list(ftests.columns), tablefmt="plain"))

    # Performance metrics
    t_arr = df["t"].to_numpy(dtype=float)
    y_arr = df["C_C0"].to_numpy(dtype=float)
    perf  = performance.metrics(t_arr, y_arr, flow_m3_s, c0_mol_m3, mass_kg, L_bed_m)
    print(f"\nPerformance:")
    print(f"  t_BT(5%)={perf.t_b/60:.1f} min  t_E(95%)={perf.t_E/60:.1f} min  "
          f"t50={perf.t50/60:.1f} min")
    print(f"  q_dyn={perf.q_dyn_mol_per_kg:.4g} mol/kg  "
          f"L_MTZ={perf.L_MTZ_m*100:.2f} cm  psi={perf.efficiency:.3f}")

    # YN back-calculated q0
    r01 = results.get("M01")
    if r01 and r01.converged:
        k_YN, tau = r01.params
        q0_YN = isotherm.back_calculate_q0(tau, flow_m3_s, c0_mol_m3, mass_kg)
        print(f"  q0 (from YN tau) = {q0_YN:.4g} mol/kg")

    # Persist
    out_dir = OUT_DIR / run.run_id
    out_dir.mkdir(parents=True, exist_ok=True)
    _write_csv(out_dir / f"results_{run.run_id}.csv", run, results, perf)

    # Plots
    plot_P1(run.run_id, results, out_dir=out_dir, top_n=8)
    plot_P2(run.run_id, df, results, out_dir=out_dir)
    plot_P3(run.run_id, df, results, out_dir=out_dir)
    plot_P4(run.run_id, df, results, out_dir=out_dir)
    plot_P5(run.run_id, results, L_bed_m=L_bed_m, v_interstitial=v_int, out_dir=out_dir)
    f_p = None
    if not ftests.empty:
        sel = ftests[(ftests["simple"] == "M01") & (ftests["complex"] == "M23")]
        if not sel.empty:
            f_p = float(sel["p_value"].iloc[0])
    plot_P6(run.run_id, df, results, f_p_ba_vs_fractal=f_p, out_dir=out_dir)
    plot_P7(run.run_id, df, results, out_dir=out_dir)
    print(f"  -> Saved to {out_dir}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    import scipy, matplotlib
    print("=== New Runs Pipeline ===")
    print(f"numpy {np.__version__}  scipy {scipy.__version__}  "
          f"matplotlib {matplotlib.__version__}")

    parser = DataParser()
    fitter = ModelFitter(n_starts=12, seed=42)

    for run_id in sorted(RUN_META):
        fpath = DATA_DIR / f"{run_id}.csv"
        if not fpath.exists():
            print(f"\n[SKIP] {fpath} not found.", file=sys.stderr)
            continue
        try:
            run_one(run_id, fpath, parser, fitter)
        except Exception as exc:
            print(f"\n[ERROR] {run_id}: {exc}", file=sys.stderr)
            import traceback; traceback.print_exc()

    print("\n=== Pipeline complete ===")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

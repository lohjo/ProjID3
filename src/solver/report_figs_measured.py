"""Measured-data cross-run figures for the Final Report.

    python src/solver/report_figs_measured.py

Why this exists. `breakthrough_fit/cross_run_figs.py` writes fig9-fig12, but its
"clean runs" selector is ``^(\\d+)ml_(\\d+)g$`` -- the twelve **synthetic**
parametric CSVs -- and fig11/fig12 draw the `May-*` records. CLAUDE.md rule 1
forbids presenting either as measured results, so none of those four figures can
go in the report. These four replace them on the real 21-run basis.

Outputs (300 dpi, headless) to ``src/img/generated/report/``:

  R1_grid_small_multiples.png  the 3x3 design as it was actually measured: one
                               panel per (concentration, flow) cell, every run in
                               that cell overlaid
  R2_grid_overlay.png          all sixteen grid runs on one axis
  R3_model_ranking.png         mean adjusted R2 per registry model, the two
                               campaigns as separate series (never pooled)
  R4_metrics_vs_flow.png       t_b, t_E, t50, q_dyn, L_MTZ and psi against flow

Nothing is fitted here. Curves come from the raw CSVs through the pipeline's own
``DataParser``; every statistic and metric is read back out of the committed
``src/solver/breakthrough_out/<run>/results_<run>.csv``. Figures carry no fitted
statistics on their faces (supervisor comment 3) except R3, whose entire subject
is the ranking statistic; its numbers are tabulated in report Tables 15 and 16.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(HERE))

from breakthrough_fit.axes_origin import snap_origin  # noqa: E402
from breakthrough_fit.parse import DataParser  # noqa: E402

OUT = REPO / "src/img/generated/report"
BT = REPO / "src/solver/breakthrough_out"
GRID_DIR = REPO / "src/solver/data/newest runs"
OLD_DIR = REPO / "src/solver/data/new runs"
PASSPORT = REPO / "src/docs/experiments_passport.json"

RUNS_OLD = ["run 3", "run 4", "run 5", "run 6", "run 8"]
OLD_Q = {"run 3": 150, "run 4": 50, "run 5": 100, "run 6": 150, "run 8": 100}

CONCS = [5, 10, 15]
FLOWS = [50, 100, 150]
C_COLOUR = {5: "#2b6cb0", 10: "#c53030", 15: "#2f855a"}
DPI = 300


def load_passport() -> list[dict]:
    return json.loads(PASSPORT.read_text(encoding="utf8"))["experiments_provenance"]


def load_curve(run_id: str, folder: Path):
    run = DataParser().parse(folder / f"{run_id}.csv")
    df = run.df
    return df["t"].to_numpy(float) / 60.0, df["C_C0"].to_numpy(float)


def results(run_id: str) -> pd.DataFrame:
    df = pd.read_csv(BT / run_id / f"results_{run_id}.csv")
    if len(df) != 24:
        raise SystemExit(f"{run_id}: expected 24 rows, got {len(df)}")
    return df


def short(run_id: str) -> str:
    return (run_id.replace("2026-", "").replace("-conc", " c").replace("-flow", " f")
            if run_id.startswith("2026-") else run_id)


# --------------------------------------------------------------------------- #
def fig_R1(entries: list[dict]) -> None:
    """The 3x3 design as measured: one panel per cell, replicates overlaid."""
    by_cell: dict[tuple[int, int], list[dict]] = {}
    for e in entries:
        key = (e["design_cell"]["C0_nominal_pct"], e["design_cell"]["Q_nominal_ml_min"])
        by_cell.setdefault(key, []).append(e)

    fig, axes = plt.subplots(3, 3, figsize=(11.0, 9.0), sharex=False, sharey=True)
    for i, c in enumerate(CONCS):
        for j, q in enumerate(FLOWS):
            ax = axes[i, j]
            runs = by_cell.get((c, q), [])
            for k, e in enumerate(runs):
                t, y = load_curve(e["run_id"], GRID_DIR)
                mark = ""
                if e["flow_ml_min"]["status"] != "consistent":
                    mark = " *"
                if e["derived"]["t_E_min"] is None:
                    mark += " †"
                ax.plot(t, y, lw=1.2, alpha=0.85,
                        color=C_COLOUR[c], ls=["-", "--", ":"][k % 3],
                        label=f"{e['date']}{mark}")
            ax.axhline(0.05, color="0.4", ls=":", lw=0.7)
            ax.axhline(0.95, color="0.4", ls="-.", lw=0.7)
            ax.set_ylim(-0.05, 1.08)
            ax.grid(alpha=0.25, lw=0.5)
            ax.tick_params(labelsize=7)
            n = len(runs)
            ax.set_title(f"{c} % CO₂, {q} mL/min  (n = {n})", fontsize=9)
            if n:
                ax.legend(fontsize=6, loc="lower right")
            else:
                ax.text(0.5, 0.5, "not measured", ha="center", va="center",
                        transform=ax.transAxes, fontsize=9, color="0.45")
            if j == 0:
                ax.set_ylabel("C/C₀  [—]", fontsize=8)
            if i == 2:
                ax.set_xlabel("time [min]", fontsize=8)
    fig.suptitle("Measured breakthrough curves, 3×3 flow × concentration design "
                 "(16 runs; dotted/dash-dot rules are C/C₀ = 0.05 and 0.95)",
                 fontsize=11)
    snap_origin(fig, label="R1")
    fig.tight_layout(rect=(0, 0, 1, 0.965))
    fig.savefig(OUT / "R1_grid_small_multiples.png", dpi=DPI)
    plt.close(fig)
    print("  wrote R1_grid_small_multiples.png")


def fig_R2(entries: list[dict]) -> None:
    """All sixteen grid runs on one axis."""
    ls = {50: ":", 100: "-", 150: "--"}
    fig, ax = plt.subplots(figsize=(10.0, 6.0))
    for e in entries:
        c = e["design_cell"]["C0_nominal_pct"]
        q = e["design_cell"]["Q_nominal_ml_min"]
        t, y = load_curve(e["run_id"], GRID_DIR)
        ax.plot(t, y, lw=1.1, alpha=0.85, color=C_COLOUR[c], ls=ls[q],
                label=short(e["run_id"]))
    ax.axhline(0.05, color="k", ls=":", lw=0.7)
    ax.axhline(0.95, color="k", ls="-.", lw=0.7)
    ax.set_xlabel("time [min]")
    ax.set_ylabel("C/C₀  [—]")
    ax.set_ylim(-0.05, 1.1)
    ax.set_title("All sixteen grid runs overlaid\n"
                 "colour = inlet CO₂ (blue 5 %, red 10 %, green 15 %); "
                 "line style = flow (dotted 50, solid 100, dashed 150 mL/min)")
    ax.legend(fontsize=6, ncol=2, loc="lower right")
    ax.grid(alpha=0.3)
    snap_origin(fig, label="R2")
    fig.tight_layout()
    fig.savefig(OUT / "R2_grid_overlay.png", dpi=DPI)
    plt.close(fig)
    print("  wrote R2_grid_overlay.png")


def fig_R3(grid_ids: list[str]) -> None:
    """Mean adjusted R2 per model, the two campaigns kept apart."""
    def means(ids):
        acc: dict[str, list] = {}
        names: dict[str, str] = {}
        for r in ids:
            for _, m in results(r).iterrows():
                names[m["code"]] = m["name"]
                v = float(m["AdjR2"])
                if math.isfinite(v):
                    acc.setdefault(m["code"], []).append(v)
        return {k: float(np.mean(v)) for k, v in acc.items()}, names

    g, names = means(grid_ids)
    o, _ = means(RUNS_OLD)
    codes = sorted(set(g) | set(o), key=lambda c: -g.get(c, -9e9))
    ypos = np.arange(len(codes))
    fig, ax = plt.subplots(figsize=(10.0, 8.0))
    ax.barh(ypos - 0.2, [g.get(c, np.nan) for c in codes], height=0.38,
            color="#2b6cb0", label="newest runs, 3×3 grid (n = 16)")
    ax.barh(ypos + 0.2, [o.get(c, np.nan) for c in codes], height=0.38,
            color="#c53030", label="new runs, run 3/4/5/6/8 (n = 5)")
    ax.set_yticks(ypos)
    ax.set_yticklabels([f"{c}  {names[c]}" for c in codes], fontsize=7)
    ax.invert_yaxis()
    ax.set_xlim(0.0, 1.02)
    ax.set_xlabel("mean adjusted R²   (a model with a non-finite or negative mean "
                  "has no bar)", fontsize=9)
    fig.suptitle("Registry models ranked by mean adjusted R²\n"
                 "campaigns reported side by side, never pooled "
                 "(numeric values: Tables 15 and 16)", fontsize=11)
    ax.legend(fontsize=8, loc="lower left")
    ax.grid(alpha=0.3, axis="x")
    snap_origin(fig, label="R3")
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    fig.savefig(OUT / "R3_model_ranking.png", dpi=DPI)
    plt.close(fig)
    print("  wrote R3_model_ranking.png")


def fig_R4(entries: list[dict]) -> None:
    """Every measured performance metric against flow, grid campaign."""
    metrics = [("t_b_min", "t_b  [min]"), ("t_E_min", "t_E  [min]"),
               ("t50_min", "t₅₀  [min]"), ("q_dyn_mol_per_kg", "q_dyn  [mol/kg]"),
               ("L_MTZ_cm", "L_MTZ  [cm]"), ("psi", "ψ  [—]")]
    fig, axes = plt.subplots(2, 3, figsize=(12.0, 7.0))
    for ax, (key, lab) in zip(axes.ravel(), metrics):
        for c in CONCS:
            xs, ys, prov = [], [], []
            for e in entries:
                if e["design_cell"]["C0_nominal_pct"] != c:
                    continue
                v = e["derived"].get(key)
                if v is None:
                    continue
                xs.append(e["design_cell"]["Q_nominal_ml_min"])
                ys.append(v)
                prov.append(e["flow_ml_min"]["status"] != "consistent")
            if not xs:
                continue
            xs, ys, prov = np.array(xs), np.array(ys), np.array(prov)
            ax.scatter(xs[~prov], ys[~prov], s=42, color=C_COLOUR[c],
                       edgecolors="k", linewidths=0.5, label=f"{c} % CO₂")
            if prov.any():
                ax.scatter(xs[prov], ys[prov], s=42, facecolors="none",
                           edgecolors=C_COLOUR[c], linewidths=1.4)
        ax.set_xticks(FLOWS)
        ax.set_xlabel("nominal flow  [mL/min]", fontsize=8)
        ax.set_ylabel(lab, fontsize=8)
        ax.tick_params(labelsize=7)
        ax.grid(alpha=0.25, lw=0.5)
    axes[0, 0].legend(fontsize=7)
    fig.suptitle("Measured performance metrics against flow, 3×3 grid campaign\n"
                 "open markers: the four runs whose source file states its flow "
                 "twice and disagrees with itself (q_dyn, L_MTZ, ψ provisional)",
                 fontsize=11)
    snap_origin(fig, label="R4")
    fig.tight_layout(rect=(0, 0, 1, 0.93))
    fig.savefig(OUT / "R4_metrics_vs_flow.png", dpi=DPI)
    plt.close(fig)
    print("  wrote R4_metrics_vs_flow.png")


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    entries = load_passport()
    grid_ids = [e["run_id"] for e in entries]
    print(f"measured basis: {len(grid_ids)} grid runs + {len(RUNS_OLD)} earlier runs")
    fig_R1(entries)
    fig_R2(entries)
    fig_R3(grid_ids)
    fig_R4(entries)
    print(f"-> {OUT.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

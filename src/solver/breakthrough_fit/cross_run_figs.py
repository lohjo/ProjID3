"""Cross-run aggregation and figure driver for the experimental-results section.

Read-only with respect to the existing pipeline: it consumes the per-run
``breakthrough_out/<run>/results_<run>.csv`` files and the raw inputs in
``src/solver/data/``, and writes new aggregate figures to ``src/img/generated/``.
It does NOT modify ``main.py``/``plots.py`` or any results CSV.

What it produces
----------------
* A summary table (printed to stdout) with one row per run: flow, mass, C0, n,
  best model (min AICc), its R2, the single-logistic (M01) and two-component
  (M24) R2 for contrast, the run-level performance metrics, and the observed
  saturation level actually reached.
* fig9  — psi, t_b, q_dyn versus flow, grouped by sorbent mass (clean runs).
* fig10 — model-ranking bar chart: mean R2 per model across the clean runs.
* fig11 — representative breakthrough curves, each drawn across C/C0 in
          [0.05, 0.95]; the observed points are overlaid and the fitted best
          model completes the span up to saturation.
* fig12 — a degenerate diagnostic run (conc10, low flow) that never broke
          through, kept for the troubleshooting discussion.

All breakthrough curves honour the C/C0 in [0.05, 0.95] window requirement.
"""

from __future__ import annotations

import re
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from breakthrough_fit import models as M
from breakthrough_fit.parse import DataParser

# .../src/solver/breakthrough_fit/cross_run_figs.py -> repo root is parents[3].
REPO = Path(__file__).resolve().parents[3]
OUT_DIR = REPO / "src" / "img" / "generated"
RESULTS_GLOB = REPO / "src" / "solver" / "breakthrough_out"
DATA_DIR = REPO / "src" / "solver" / "data"

CLEAN_RE = re.compile(r"^(\d+)ml_(\d+)g$")
MASS_MARKERS = {2: "o", 4: "s", 6: "^"}
MASS_COLORS = {2: "#1f77b4", 4: "#d62728", 6: "#2ca02c"}


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #
def parse_params(param_str: str) -> dict[str, float]:
    out: dict[str, float] = {}
    if not isinstance(param_str, str):
        return out
    for piece in param_str.split(";"):
        if "=" not in piece:
            continue
        k, v = piece.split("=", 1)
        try:
            out[k.strip()] = float(v)
        except ValueError:
            pass
    return out


def model_curve(code: str, param_str: str, t: np.ndarray) -> np.ndarray | None:
    """Reconstruct C/C0(t) for one model from its stored parameter string."""
    func = getattr(M, f"model_{code}", None)
    if func is None:
        return None
    try:
        spec = M.get_model(code)
    except KeyError:
        return None
    pd_ = parse_params(param_str)
    try:
        vals = [pd_[name] for name in spec.param_names]
    except KeyError:
        return None
    try:
        return np.asarray(func(t, *vals), dtype=float)
    except Exception:
        return None


def t_at_level(t: np.ndarray, y: np.ndarray, level: float) -> float:
    """First time at which monotone-ish y crosses level (NaN if never)."""
    finite = np.isfinite(y)
    t, y = t[finite], y[finite]
    if y.size < 2 or y.max() < level:
        return float("nan")
    idx = int(np.argmax(y >= level))
    if idx == 0:
        return float(t[0])
    y0, y1 = y[idx - 1], y[idx]
    t0, t1 = t[idx - 1], t[idx]
    if y1 == y0:
        return float(t1)
    return float(t0 + (level - y0) * (t1 - t0) / (y1 - y0))


def classify(run_id: str) -> tuple[str, float | None, float | None]:
    m = CLEAN_RE.match(run_id)
    if m:
        return "clean", float(m.group(1)), float(m.group(2))
    return "diagnostic", None, None


# --------------------------------------------------------------------------- #
# Load everything
# --------------------------------------------------------------------------- #
def load_runs() -> list[dict]:
    parser = DataParser()
    rows: list[dict] = []
    for csv in sorted(RESULTS_GLOB.glob("*/results_*.csv")):
        run_id = csv.parent.name
        df = pd.read_csv(csv)
        if df.empty:
            continue
        kind, flow, mass = classify(run_id)

        conv = df[df["converged"] & np.isfinite(df["AICc"])].copy()
        conv = conv[conv["R2"].notna()]
        best = None
        if not conv.empty:
            best = conv.loc[conv["AICc"].idxmin()]

        def r2_of(code: str) -> float:
            sub = df[df["code"] == code]
            if sub.empty:
                return float("nan")
            return float(sub.iloc[0]["R2"])

        # Run-level performance metrics repeat on every row; take the first.
        first = df.iloc[0]

        # Raw data for C0 / flow metadata / observed saturation.
        data_path = DATA_DIR / f"{run_id}.csv"
        c0_ppm = float("nan")
        flow_meta = float("nan")
        temp_K = float("nan")
        ymax = float("nan")
        raw = None
        if data_path.exists():
            try:
                run = parser.parse(data_path)
                raw = run.df
                c0_ppm = float(run.c0_ppm) if run.c0_ppm else float("nan")
                flow_meta = (
                    float(run.flow_ml_min)
                    if run.flow_ml_min is not None
                    else float("nan")
                )
                temp_K = (
                    float(run.temperature_K)
                    if run.temperature_K is not None
                    else float("nan")
                )
                ymax = float(np.nanmax(raw["C_C0"].to_numpy(dtype=float)))
            except Exception as exc:  # noqa: BLE001
                print(f"[warn] raw parse failed for {run_id}: {exc}")

        rows.append(
            {
                "run_id": run_id,
                "kind": kind,
                "flow_ml_min": flow if flow is not None else flow_meta,
                "mass_g": mass,
                "C0_ppm": c0_ppm,
                "n": int(first["n"]) if np.isfinite(first["n"]) else 0,
                "best_code": None if best is None else str(best["code"]),
                "best_name": None if best is None else str(best["name"]),
                "best_R2": float("nan") if best is None else float(best["R2"]),
                "best_AICc": float("nan") if best is None else float(best["AICc"]),
                "best_params": None if best is None else str(best["params"]),
                "R2_M01": r2_of("M01"),
                "R2_M24": r2_of("M24"),
                "R2_M10": r2_of("M10"),
                "R2_M11": r2_of("M11"),
                "t_b_s": float(first["t_b"]) if pd.notna(first["t_b"]) else float("nan"),
                "t_E_s": float(first["t_E"]) if pd.notna(first["t_E"]) else float("nan"),
                "t50_s": float(first["t50"]) if pd.notna(first["t50"]) else float("nan"),
                "q_dyn": float(first["q_dyn_mol_per_kg"])
                if pd.notna(first["q_dyn_mol_per_kg"])
                else float("nan"),
                "psi": float(first["efficiency"])
                if pd.notna(first["efficiency"])
                else float("nan"),
                "obs_ymax": ymax,
                "_raw": raw,
                "_results_df": df,
            }
        )
    return rows


# --------------------------------------------------------------------------- #
# Figures
# --------------------------------------------------------------------------- #
def fig9_param_trends(rows: list[dict]) -> None:
    clean = [r for r in rows if r["kind"] == "clean"]
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.6))
    panels = [
        ("psi", "Stoichiometric efficiency  ψ  [-]", 1.0),
        ("t_b_s", "Breakthrough time  t_b  [min]", 1 / 60.0),
        ("q_dyn", "Dynamic capacity  q_dyn  [mol kg$^{-1}$]", 1.0),
    ]
    for ax, (key, ylabel, scale) in zip(axes, panels):
        for mass in (2, 4, 6):
            pts = sorted(
                [r for r in clean if r["mass_g"] == mass and np.isfinite(r[key])],
                key=lambda r: r["flow_ml_min"],
            )
            if not pts:
                continue
            xs = [r["flow_ml_min"] for r in pts]
            ys = [r[key] * scale for r in pts]
            ax.plot(
                xs,
                ys,
                marker=MASS_MARKERS[mass],
                color=MASS_COLORS[mass],
                label=f"{mass} g",
                linewidth=1.6,
                markersize=7,
            )
        ax.set_xlabel("Volumetric flow  [mL min$^{-1}$]")
        ax.set_ylabel(ylabel)
        ax.grid(alpha=0.3)
        ax.legend(title="sorbent mass", fontsize=8)
    fig.suptitle(
        "Parametric response of the packed-bed column (C$_0$ ≈ 4 % CO$_2$, "
        "L = 32.5 cm, d = 3.37 cm)",
        fontsize=11,
    )
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    path = OUT_DIR / "fig9_param_trends_vs_flow.png"
    fig.savefig(path, dpi=300)
    plt.close(fig)
    print(f"[fig] wrote {path}")


def fig10_model_ranking(rows: list[dict]) -> None:
    clean = [r for r in rows if r["kind"] == "clean"]
    codes = [m.code for m in M.REGISTRY]
    names = {m.code: m.name for m in M.REGISTRY}
    mean_r2: dict[str, float] = {}
    win_count: dict[str, int] = {c: 0 for c in codes}
    for r in clean:
        if r["best_code"] in win_count:
            win_count[r["best_code"]] += 1
    for c in codes:
        vals = []
        for r in clean:
            sub = r["_results_df"]
            row = sub[sub["code"] == c]
            if not row.empty and pd.notna(row.iloc[0]["R2"]):
                vals.append(float(row.iloc[0]["R2"]))
        mean_r2[c] = float(np.mean(vals)) if vals else float("nan")

    order = sorted(codes, key=lambda c: (np.nan_to_num(mean_r2[c], nan=-1e9)))
    y = np.arange(len(order))
    vals = [mean_r2[c] for c in order]
    colors = ["#2ca02c" if win_count[c] > 0 else "#7f7f7f" for c in order]

    fig, ax = plt.subplots(figsize=(8.5, 9))
    ax.barh(y, vals, color=colors)
    ax.set_yticks(y)
    ax.set_yticklabels([f"{c}  {names[c][:34]}" for c in order], fontsize=7.5)
    ax.set_xlabel("Mean R$^2$ across 12 clean parametric runs")
    ax.set_xlim(-0.05, 1.0)
    ax.axvline(0.0, color="k", linewidth=0.6)
    ax.grid(axis="x", alpha=0.3)
    ax.set_title("Model performance ranking", fontsize=10)
    fig.tight_layout()
    path = OUT_DIR / "fig10_model_ranking.png"
    fig.savefig(path, dpi=300)
    plt.close(fig)
    print(f"[fig] wrote {path}")


def fig11_breakthrough_window(rows: list[dict]) -> None:
    by_id = {r["run_id"]: r for r in rows}
    picks = ["50ml_2g", "100ml_4g", "250ml_4g"]
    picks = [p for p in picks if p in by_id and by_id[p]["_raw"] is not None]

    fig, ax = plt.subplots(figsize=(8.5, 5.6))
    palette = ["#1f77b4", "#d62728", "#2ca02c", "#9467bd"]
    for color, run_id in zip(palette, picks):
        r = by_id[run_id]
        raw = r["_raw"]
        t_obs = raw["t"].to_numpy(dtype=float)
        y_obs = raw["C_C0"].to_numpy(dtype=float)
        if r["best_code"] is None:
            continue
        t_end = max(np.nanmax(t_obs) * 1.5, (r["t50_s"] or 1.0) * 3.0)
        grid = np.linspace(max(np.nanmin(t_obs), 1.0), t_end, 4000)
        curve = model_curve(r["best_code"], r["best_params"], grid)
        if curve is None:
            continue
        t05 = t_at_level(grid, curve, 0.05)
        t95 = t_at_level(grid, curve, 0.95)
        if not (np.isfinite(t05) and np.isfinite(t95)):
            continue
        win = (grid >= t05) & (grid <= t95)
        ax.plot(
            grid[win] / 60.0,
            curve[win],
            color=color,
            linewidth=2.0,
            label=f"{run_id}  (best: {r['best_code']})",
        )
        # Observed points only within the [0.05, 0.95] band.
        band = (y_obs >= 0.05) & (y_obs <= 0.95)
        ax.scatter(
            t_obs[band] / 60.0,
            y_obs[band],
            s=10,
            color=color,
            alpha=0.35,
            edgecolors="none",
        )
    ax.axhline(0.05, color="k", linestyle=":", linewidth=0.8)
    ax.axhline(0.95, color="k", linestyle=":", linewidth=0.8)
    ax.set_ylim(0.0, 1.0)
    ax.set_xlabel("Time  [min]")
    ax.set_ylabel("C/C$_0$  [-]")
    ax.set_title(
        "Breakthrough curves over the C/C$_0$ ∈ [0.05, 0.95] service window\n"
        "(markers = measured points in band; line = best AICc model)",
        fontsize=10,
    )
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8, loc="lower right")
    fig.tight_layout()
    path = OUT_DIR / "fig11_breakthrough_window.png"
    fig.savefig(path, dpi=300)
    plt.close(fig)
    print(f"[fig] wrote {path}")


def fig12_degenerate(rows: list[dict]) -> None:
    by_id = {r["run_id"]: r for r in rows}
    candidates = [
        "May-22-2026-conc10-flow0.1",
        "May-22-2026-conc10-flow0.05",
        "May-22-2026-conc10_flow-0.1(2)",
    ]
    picks = [c for c in candidates if c in by_id and by_id[c]["_raw"] is not None]
    if not picks:
        print("[fig] no degenerate runs found; skipping fig12")
        return
    fig, ax = plt.subplots(figsize=(8.5, 5.0))
    palette = ["#d62728", "#ff7f0e", "#8c564b"]
    for color, run_id in zip(palette, picks):
        r = by_id[run_id]
        raw = r["_raw"]
        t_obs = raw["t"].to_numpy(dtype=float)
        y_obs = raw["C_C0"].to_numpy(dtype=float)
        ax.plot(
            t_obs / 60.0,
            y_obs,
            color=color,
            linewidth=1.3,
            label=f"{run_id}  (max C/C₀={r['obs_ymax']:.2f})",
        )
    ax.axhline(0.05, color="k", linestyle=":", linewidth=0.8)
    ax.set_ylim(-0.05, 1.0)
    ax.set_xlabel("Time  [min]")
    ax.set_ylabel("C/C$_0$  [-]")
    ax.set_title(
        "Unsuccessful runs retained for troubleshooting:\n"
        "high-concentration (~10 % CO$_2$) tests whose anomalous fronts no model fitted",
        fontsize=9.5,
    )
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8, loc="upper right")
    fig.tight_layout()
    path = OUT_DIR / "fig12_degenerate_runs.png"
    fig.savefig(path, dpi=300)
    plt.close(fig)
    print(f"[fig] wrote {path}")


# --------------------------------------------------------------------------- #
# Summary table
# --------------------------------------------------------------------------- #
def print_summary(rows: list[dict]) -> None:
    cols = [
        "run_id",
        "kind",
        "flow_ml_min",
        "mass_g",
        "C0_ppm",
        "n",
        "best_code",
        "best_R2",
        "R2_M01",
        "R2_M24",
        "R2_M10",
        "R2_M11",
        "t_b_s",
        "t50_s",
        "t_E_s",
        "q_dyn",
        "psi",
        "obs_ymax",
    ]
    print("\n=== CROSS-RUN SUMMARY ===")
    print(",".join(cols))
    for r in sorted(rows, key=lambda r: (r["kind"], r["run_id"])):
        cells = []
        for c in cols:
            v = r[c]
            if isinstance(v, float):
                cells.append("" if not np.isfinite(v) else f"{v:.5g}")
            else:
                cells.append("" if v is None else str(v))
        print(",".join(cells))
    print("=== END SUMMARY ===\n")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    rows = load_runs()
    print_summary(rows)
    fig9_param_trends(rows)
    fig10_model_ranking(rows)
    fig11_breakthrough_window(rows)
    fig12_degenerate(rows)


if __name__ == "__main__":
    main()

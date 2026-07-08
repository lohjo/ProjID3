"""Required plots P1 – P7.

Every function takes the parsed-run data plus the per-model :class:`FitResult`
dictionary, returns the ``matplotlib`` figure, and writes a 300-dpi PNG to
``out_dir / "P{n}_{run_id}.png"`` when ``out_dir`` is provided.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, Optional

import numpy as np

import matplotlib
matplotlib.use("Agg")  # headless backend; figures saved to disk
import matplotlib.pyplot as plt

from .fit import FitResult
from .models import weibull_derivative
from .mtz_fem import project_snapshots
from .performance import t_breakthrough


_DPI = 300
_FIGSIZE_S = (6.5, 5.0)
_FIGSIZE_M = (9.0, 5.5)
_FIGSIZE_L = (10.0, 7.0)


def _save(fig: plt.Figure, out_dir: Optional[Path], stem: str) -> plt.Figure:
    if out_dir is not None:
        out_dir = Path(out_dir)
        out_dir.mkdir(parents=True, exist_ok=True)
        fig.tight_layout()
        fig.savefig(out_dir / f"{stem}.png", dpi=_DPI)
    return fig


# ---------------------------------------------------------------------------
# P1 — predicted vs observed
# ---------------------------------------------------------------------------
def plot_P1(
    run_id: str,
    results: dict[str, FitResult],
    out_dir: Optional[Path] = None,
    top_n: int = 8,
) -> plt.Figure:
    fig, ax = plt.subplots(figsize=_FIGSIZE_M)
    ranked = sorted(
        (r for r in results.values() if r.converged),
        key=lambda r: -r.stats.r2 if np.isfinite(r.stats.r2) else 1.0,
    )[:top_n]
    cmap = plt.get_cmap("tab10")
    for i, r in enumerate(ranked):
        mask = np.isfinite(r.y_pred)
        ax.scatter(
            r.y_obs[mask], r.y_pred[mask],
            s=10, alpha=0.55, color=cmap(i % 10),
            label=f"{r.code}  R²={r.stats.r2:0.4f}",
        )
    ax.plot([0, 1], [0, 1], "k--", lw=1)
    ax.set_xlim(-0.02, 1.05)
    ax.set_ylim(-0.02, 1.05)
    ax.set_xlabel("Observed C/C₀")
    ax.set_ylabel("Predicted C/C₀")
    ax.set_title(f"P1 — predicted vs observed ({run_id})")
    ax.legend(fontsize=7, loc="lower right")
    return _save(fig, out_dir, f"P1_{run_id}")


# ---------------------------------------------------------------------------
# P2 — breakthrough curves grouped by isotherm assumption
# ---------------------------------------------------------------------------
def _vlines(ax: plt.Axes, t: np.ndarray, y: np.ndarray) -> None:
    tb = t_breakthrough(t, y, level=0.05)
    te = t_breakthrough(t, y, level=0.95)
    if np.isfinite(tb):
        ax.axvline(tb / 60.0, color="grey", ls=":", lw=1, label="t_b (C/C₀=0.05)")
    if np.isfinite(te):
        ax.axvline(te / 60.0, color="black", ls=":", lw=1, label="t_E (C/C₀=0.95)")


def plot_P2(
    run_id: str,
    df,
    results: dict[str, FitResult],
    out_dir: Optional[Path] = None,
) -> plt.Figure:
    fig, axes = plt.subplots(1, 2, figsize=_FIGSIZE_L, sharey=True)
    t = df["t"].to_numpy(dtype=float)
    y = df["C_C0"].to_numpy(dtype=float)
    t_min = t / 60.0

    langmuir_codes = ("M01", "M02", "M16", "M17")
    freundlich_codes = ("M04", "M19")
    for ax, codes, title in (
        (axes[0], langmuir_codes, "Langmuir-isotherm fits"),
        (axes[1], freundlich_codes, "Freundlich-isotherm fits"),
    ):
        ax.scatter(t_min, y, s=10, color="black", alpha=0.6, label="data")
        for code in codes:
            r = results.get(code)
            if r is None or not r.converged:
                continue
            mask = np.isfinite(r.y_pred)
            param_str = ", ".join(
                f"{n}={v:0.3g}" for n, v in zip(r.param_names, r.params)
            )
            ax.plot(
                t_min[mask], r.y_pred[mask], lw=1.5,
                label=f"{r.code}  R²={r.stats.r2:0.3f}\n  {param_str}",
            )
        _vlines(ax, t, y)
        ax.set_xlabel("time [min]")
        ax.set_title(title)
        ax.set_ylim(-0.02, 1.05)
        ax.legend(fontsize=7, loc="lower right")
    axes[0].set_ylabel("C/C₀")
    fig.suptitle(f"P2 — breakthrough curves ({run_id})")
    return _save(fig, out_dir, f"P2_{run_id}")


# ---------------------------------------------------------------------------
# P3 — Weibull two-panel
# ---------------------------------------------------------------------------
def plot_P3(
    run_id: str,
    df,
    results: dict[str, FitResult],
    out_dir: Optional[Path] = None,
) -> plt.Figure:
    fig, axes = plt.subplots(1, 2, figsize=_FIGSIZE_L)
    t = df["t"].to_numpy(dtype=float)
    y = df["C_C0"].to_numpy(dtype=float)
    t_min = t / 60.0

    r = results.get("M14")
    axes[0].scatter(t_min, y, s=10, color="black", alpha=0.6, label="data")
    if r is not None and r.converged:
        axes[0].plot(t_min, r.y_pred, "r-", lw=1.5, label="Weibull (M14)")
        tau, k = r.params
        rate = weibull_derivative(t, tau, k)
        axes[1].plot(t_min, rate * 60.0, "r-", lw=1.5)
        # Mode of Weibull: t_peak = tau (1 - 1/k)^{1/k} for k > 1.
        if k > 1.0:
            t_peak = tau * (1.0 - 1.0 / k) ** (1.0 / k)
            axes[1].axvline(t_peak / 60.0, color="grey", ls="--",
                            label=f"t_peak = {t_peak/60.0:0.1f} min")
    axes[0].set_xlabel("time [min]")
    axes[0].set_ylabel("C/C₀")
    axes[0].set_title("Weibull fit")
    axes[0].legend(fontsize=8)
    axes[1].set_xlabel("time [min]")
    axes[1].set_ylabel("d(C/C₀)/dt  [min⁻¹]")
    axes[1].set_title("Wave-front rate (Weibull derivative)")
    axes[1].legend(fontsize=8)
    fig.suptitle(f"P3 — Weibull ({run_id})")
    return _save(fig, out_dir, f"P3_{run_id}")


# ---------------------------------------------------------------------------
# P4 — Thomas vs Dose-Response with residuals
# ---------------------------------------------------------------------------
def plot_P4(
    run_id: str,
    df,
    results: dict[str, FitResult],
    out_dir: Optional[Path] = None,
) -> plt.Figure:
    fig, axes = plt.subplots(
        2, 1, figsize=_FIGSIZE_L, sharex=True,
        gridspec_kw={"height_ratios": [3, 1]},
    )
    t = df["t"].to_numpy(dtype=float)
    y = df["C_C0"].to_numpy(dtype=float)
    t_min = t / 60.0

    axes[0].scatter(t_min, y, s=10, color="black", alpha=0.6, label="data")
    r01 = results.get("M01")
    r04 = results.get("M04")
    y1 = r01.y_pred if (r01 and r01.converged) else None
    y4 = r04.y_pred if (r04 and r04.converged) else None
    if y1 is not None:
        axes[0].plot(t_min, y1, "b-", lw=1.5, label=f"M01 Thomas/YN  R²={r01.stats.r2:0.3f}")
    if y4 is not None:
        axes[0].plot(t_min, y4, "g-", lw=1.5, label=f"M04 Dose-Response  R²={r04.stats.r2:0.3f}")
    if y1 is not None and y4 is not None:
        lower = np.minimum(y1, y4)
        upper = np.maximum(y1, y4)
        axes[0].fill_between(t_min, lower, upper, color="grey", alpha=0.2,
                             label="asymmetry band")
    axes[0].set_ylabel("C/C₀")
    axes[0].legend(fontsize=8)

    if y1 is not None:
        axes[1].plot(t_min, y - y1, "b-", lw=0.8, label="M01 residual")
    if y4 is not None:
        axes[1].plot(t_min, y - y4, "g-", lw=0.8, label="M04 residual")
    axes[1].axhline(0.0, color="black", lw=0.6)
    axes[1].set_xlabel("time [min]")
    axes[1].set_ylabel("residual")
    axes[1].legend(fontsize=8)
    fig.suptitle(f"P4 — Thomas vs Dose-Response ({run_id})")
    return _save(fig, out_dir, f"P4_{run_id}")


# ---------------------------------------------------------------------------
# P5 — MTZ propagation snapshots (FEM travelling wave)
# ---------------------------------------------------------------------------
def plot_P5(
    run_id: str,
    results: dict[str, FitResult],
    L_bed_m: float,
    v_interstitial: float,
    out_dir: Optional[Path] = None,
) -> plt.Figure:
    r = results.get("M01")
    if r is None or not r.converged:
        fig, ax = plt.subplots(figsize=_FIGSIZE_M)
        ax.text(0.5, 0.5, "M01 fit unavailable — P5 skipped",
                ha="center", va="center")
        ax.set_axis_off()
        return _save(fig, out_dir, f"P5_{run_id}")

    k_YN, tau = r.params  # tau acts as t_half proxy
    t_E_idx = np.searchsorted(r.y_pred, 0.95)
    t_E = float(r.t[min(t_E_idx, r.t.size - 1)]) if t_E_idx > 0 else float(r.t[-1])
    snap_times = np.array([0.2, 0.4, 0.6, 0.8, 1.0]) * t_E

    fig, axes = plt.subplots(1, 3, figsize=(14.0, 4.5), sharey=True)

    sweeps = [
        ("Baseline L", [(L_bed_m, v_interstitial, k_YN)]),
        ("Vary u (±50%)",
         [(L_bed_m, 0.5 * v_interstitial, k_YN),
          (L_bed_m, v_interstitial, k_YN),
          (L_bed_m, 1.5 * v_interstitial, k_YN)]),
        ("Vary L (×0.5, ×1, ×2)",
         [(0.5 * L_bed_m, v_interstitial, k_YN),
          (L_bed_m, v_interstitial, k_YN),
          (2.0 * L_bed_m, v_interstitial, k_YN)]),
    ]
    cmap = plt.get_cmap("viridis")
    for ax, (title, cases) in zip(axes, sweeps):
        for j, (L_use, v_use, k_use) in enumerate(cases):
            x, C = project_snapshots(
                L=L_use, v=v_use, k_ad_c_in=k_use, t_half=tau,
                t_snapshots=snap_times, n_nodes=100,
            )
            for i, t_snap in enumerate(snap_times):
                ax.plot(
                    x / max(L_use, 1e-9), C[i],
                    color=cmap(i / max(len(snap_times) - 1, 1)),
                    alpha=0.4 + 0.2 * j,
                    lw=1.0 + 0.3 * j,
                    label=(
                        f"t={t_snap/60.0:0.1f} min"
                        if j == len(cases) - 1 else None
                    ),
                )
        ax.set_xlabel("x / L")
        ax.set_title(title)
        ax.set_ylim(-0.02, 1.05)
        if title.startswith("Baseline"):
            ax.set_ylabel("C/C₀")
        ax.legend(fontsize=7, loc="lower right")
    fig.suptitle(f"P5 — MTZ propagation ({run_id})")
    return _save(fig, out_dir, f"P5_{run_id}")


# ---------------------------------------------------------------------------
# P6 — Fractal YN (M23) vs standard YN (M01)
# ---------------------------------------------------------------------------
def plot_P6(
    run_id: str,
    df,
    results: dict[str, FitResult],
    f_p_ba_vs_fractal: Optional[float],
    out_dir: Optional[Path] = None,
) -> plt.Figure:
    fig, axes = plt.subplots(
        2, 2, figsize=_FIGSIZE_L, sharex=True,
        gridspec_kw={"height_ratios": [3, 1]},
    )
    t = df["t"].to_numpy(dtype=float)
    y = df["C_C0"].to_numpy(dtype=float)
    t_min = t / 60.0
    pairs = (("M01", "Standard YN"), ("M23", "Fractal YN"))

    for col, (code, title) in enumerate(pairs):
        ax_top = axes[0, col]
        ax_bot = axes[1, col]
        r = results.get(code)
        ax_top.scatter(t_min, y, s=10, color="black", alpha=0.5, label="data")
        if r is not None and r.converged:
            ax_top.plot(t_min, r.y_pred, "r-", lw=1.5,
                        label=f"{code}  R²={r.stats.r2:0.3f}")
            resid = y - r.y_pred
            ax_bot.bar(t_min, resid, width=(t_min[-1] - t_min[0]) / max(t.size, 1),
                       color="grey")
            if code == "M23" and "h" in r.param_names:
                h_idx = r.param_names.index("h")
                h_val = r.params[h_idx]
                p_str = (f"  F-test p={f_p_ba_vs_fractal:0.3g}"
                         if f_p_ba_vs_fractal is not None and
                         np.isfinite(f_p_ba_vs_fractal)
                         else "")
                ax_top.text(
                    0.02, 0.95, f"h = {h_val:0.3f}{p_str}",
                    transform=ax_top.transAxes, fontsize=9, va="top",
                    bbox=dict(facecolor="white", alpha=0.6),
                )
        ax_top.set_title(title)
        ax_top.set_ylim(-0.02, 1.05)
        ax_top.legend(fontsize=8)
        ax_bot.axhline(0, color="black", lw=0.6)
        ax_bot.set_xlabel("time [min]")
        if col == 0:
            ax_top.set_ylabel("C/C₀")
            ax_bot.set_ylabel("residual")
    fig.suptitle(f"P6 — Standard YN vs Fractal YN ({run_id})")
    return _save(fig, out_dir, f"P6_{run_id}")


# ---------------------------------------------------------------------------
# P7 — residual plots (one panel grid for all models)
# ---------------------------------------------------------------------------
def _rolling_mean(x: np.ndarray, window: int = 11) -> np.ndarray:
    if x.size < window:
        return np.full_like(x, np.nan, dtype=float)
    kernel = np.ones(window) / window
    return np.convolve(x, kernel, mode="same")


def plot_P7(
    run_id: str,
    df,
    results: dict[str, FitResult],
    out_dir: Optional[Path] = None,
    codes: Optional[Iterable[str]] = None,
) -> plt.Figure:
    t = df["t"].to_numpy(dtype=float)
    y = df["C_C0"].to_numpy(dtype=float)
    t_min = t / 60.0
    converged = [r for r in results.values() if r.converged]
    if codes is not None:
        converged = [r for r in converged if r.code in codes]
    if not converged:
        fig, ax = plt.subplots(figsize=_FIGSIZE_M)
        ax.text(0.5, 0.5, "no converged fits", ha="center", va="center")
        ax.set_axis_off()
        return _save(fig, out_dir, f"P7_{run_id}")

    n = len(converged)
    cols = 4
    rows = int(np.ceil(n / cols))
    fig, axes = plt.subplots(rows, cols, figsize=(4.0 * cols, 2.8 * rows),
                             sharex=True)
    axes = np.atleast_2d(axes).ravel()
    for ax, r in zip(axes, converged):
        resid = y - r.y_pred
        ax.scatter(t_min, resid, s=6, alpha=0.5, color="steelblue")
        ax.plot(t_min, _rolling_mean(resid, 11), color="orange", lw=1.0)
        ax.axhline(0.0, color="black", lw=0.6)
        ax.set_title(f"{r.code}  χ²_red={r.stats.chi2_red:0.3g}", fontsize=9)
        ax.tick_params(labelsize=7)
    for ax in axes[len(converged):]:
        ax.set_axis_off()
    fig.suptitle(f"P7 — residual diagnostics ({run_id})")
    fig.supxlabel("time [min]")
    fig.supylabel("y_obs − y_pred")
    return _save(fig, out_dir, f"P7_{run_id}")

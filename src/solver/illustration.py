"""
Numerical illustration for the Experimental Results & Analysis section of
"CO2 Adsorption in Packed-Bed Column Using Polymer-Based Sorbent: Parametric
Study and Model Prediction".

Walks a scholar from the linear transport equation up to fitted Chern--Chien
breakthrough curves on the SUTD PEI@SiO2 dataset, recreating the diagnostic
plots from Hu et al. (2020, 2024) on the project's own measurements.

Outputs PNGs to src/img/generated/.  Annotation style follows the screenshots
in src/img/Screenshot 2026-05-26 13*.png:
  - 2x2 panel labels (a, b, c, d) in upper-left corner
  - dashed model curves, coloured marker series
  - dotted reference lines at C/C0 = 0.2 / 0.5 / 0.8 / 1.0
  - coordinate callouts and "arrow + label" overlays

Run from repo root:
    python src/solver/illustration.py
"""

from __future__ import annotations

import csv
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

import matplotlib

matplotlib.use("Agg")  # headless backend; figures are written, never shown
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import curve_fit
from scipy.special import erf

# This script lives in src/solver/, which Python puts on sys.path when it is run
# as `python src/solver/illustration.py`, so this package import resolves.
from breakthrough_fit.axes_origin import snap_origin

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = REPO_ROOT / "src" / "solver" / "data"
OUT_DIR = REPO_ROOT / "src" / "img" / "generated"
OUT_DIR.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.labelsize": 11,
    "axes.titlesize": 11,
    "axes.spines.top": True,
    "axes.spines.right": True,
    "xtick.direction": "in",
    "ytick.direction": "in",
    "xtick.top": True,
    "ytick.right": True,
    "legend.frameon": False,
    "legend.fontsize": 9,
})

CMAP = {"green": "#2ca02c", "blue": "#1f77b4", "red": "#d62728",
        "orange": "#ff7f0e", "purple": "#9467bd", "grey": "#555555"}


# ---------------------------------------------------------------------------
# Data ingestion
# ---------------------------------------------------------------------------

@dataclass
class BTRun:
    flow_mlmin: float
    mass_g: float
    C0_ppm: float
    t_min: np.ndarray
    CC0: np.ndarray
    label: str

    @property
    def Q_mol_per_min(self) -> float:
        # Q_vol at STP-ish. 1 mol = 24.45 L at 25 C, 1 atm => 24450 mL.
        return self.flow_mlmin / 24450.0

    @property
    def mdot_CO2_mol_per_min(self) -> float:
        return self.Q_mol_per_min * (self.C0_ppm / 1e6)


def _load_clean_csv(path: Path) -> BTRun | None:
    """Load a CSV from src/solver/data/ that follows the cleaned schema
    (cols: time_s, time_min, CO2_ppm, C/C0)."""
    flow, mass = _parse_flow_mass(path.name)
    if flow is None:
        return None
    with path.open("r", newline="") as fh:
        reader = csv.reader(fh)
        rows = list(reader)
    header = rows[0]
    try:
        C0 = float(header[4])
    except (ValueError, IndexError):
        return None
    t_min, cc0 = [], []
    for r in rows[1:]:
        if len(r) < 9 or not r[6] or not r[8]:
            continue
        try:
            tm = float(r[6])
            ratio = float(r[8])
        except ValueError:
            continue
        if not np.isfinite(tm) or not np.isfinite(ratio):
            continue
        t_min.append(tm)
        cc0.append(ratio)
    if len(t_min) < 20:
        return None
    t_arr = np.asarray(t_min)
    c_arr = np.clip(np.asarray(cc0), 0.0, 1.05)
    # Dedupe identical timestamps (sensor logs at >1 Hz, some duplicates exist)
    t_arr, uniq_idx = np.unique(t_arr, return_index=True)
    c_arr = c_arr[uniq_idx]
    # Trim leading dead band: keep one anchor at t=0, drop the rest of the
    # baseline below 1% C0 so the logistic fitter doesn't get pinned to 0.
    rise_idx = np.argmax(c_arr > 0.01)
    if rise_idx > 1:
        keep_lead = max(0, rise_idx - 2)
        t_arr = np.concatenate([[t_arr[0]], t_arr[keep_lead:]])
        c_arr = np.concatenate([[c_arr[0]], c_arr[keep_lead:]])
        t_arr, uniq_idx = np.unique(t_arr, return_index=True)
        c_arr = c_arr[uniq_idx]
    return BTRun(flow, mass, C0,
                 t_arr, c_arr,
                 f"{int(flow)} mL/min, {int(mass)} g")


def _parse_flow_mass(name: str) -> tuple[float | None, float | None]:
    # e.g. "150ml_4g.csv"
    base = name.lower().replace(".csv", "")
    try:
        flow_part, mass_part = base.split("_")
        flow = float(flow_part.replace("ml", ""))
        mass = float(mass_part.replace("g", ""))
        return flow, mass
    except ValueError:
        return None, None


def load_runs() -> list[BTRun]:
    runs = []
    for p in sorted(DATA_DIR.glob("*ml_*g.csv")):
        run = _load_clean_csv(p)
        if run is not None:
            runs.append(run)
    return runs


# ---------------------------------------------------------------------------
# Step 1 -- Linear transport equation u_t + a u_x = 0 with periodic BC
# ---------------------------------------------------------------------------

def solve_linear_transport(a: float = 1.0, N: int = 400, t_end: float = 1.0,
                           snapshots: tuple[float, ...] = (0.0, 0.25, 0.5, 0.75)):
    """First-order upwind on x in [0, 1], periodic BC, smooth bump initial."""
    x = np.linspace(0, 1, N, endpoint=False)
    dx = x[1] - x[0]
    u0 = np.exp(-((x - 0.25) / 0.08) ** 2)

    def rhs(t, u):
        return -a * (u - np.roll(u, 1)) / dx

    sol = solve_ivp(rhs, (0, t_end), u0, method="RK45",
                    t_eval=snapshots, rtol=1e-7, atol=1e-9)
    return x, sol


def fig_linear_transport():
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    # Panel (a) pure advection -- characteristic lines
    ax = axes[0]
    x, sol = solve_linear_transport(a=1.0, t_end=0.75,
                                    snapshots=(0.0, 0.25, 0.5, 0.75))
    cmap = plt.get_cmap("viridis")
    for i, t in enumerate(sol.t):
        ax.plot(x, sol.y[:, i], color=cmap(i / max(1, len(sol.t) - 1)),
                label=f"t = {t:.2f}")
    ax.text(0.03, 0.95, "a", transform=ax.transAxes, fontsize=14,
            fontweight="bold", va="top")
    ax.set_xlabel("x")
    ax.set_ylabel("u(x, t)")
    ax.set_title(r"$u_t + a\,u_x = 0$,  $a = 1$,  periodic BC")
    ax.legend(loc="upper right")
    ax.set_xlim(0, 1)
    ax.set_ylim(-0.05, 1.1)

    # Panel (b) characteristics in (x, t)
    ax = axes[1]
    a_val = 1.0
    for x0 in np.linspace(0.05, 0.95, 10):
        t_line = np.linspace(0, 0.6, 50)
        x_line = (x0 + a_val * t_line) % 1.0
        # Break wrap-around into segments
        jumps = np.where(np.abs(np.diff(x_line)) > 0.5)[0]
        start = 0
        for j in jumps:
            ax.plot(x_line[start:j + 1], t_line[start:j + 1],
                    color=CMAP["grey"], lw=0.8)
            start = j + 1
        ax.plot(x_line[start:], t_line[start:], color=CMAP["grey"], lw=0.8)
    ax.annotate("characteristic\n" r"$x - at = \mathrm{const.}$",
                xy=(0.55, 0.45), xytext=(0.15, 0.5), color=CMAP["red"],
                arrowprops=dict(arrowstyle="->", color=CMAP["red"]))
    ax.text(0.03, 0.95, "b", transform=ax.transAxes, fontsize=14,
            fontweight="bold", va="top")
    ax.set_xlabel("x")
    ax.set_ylabel("t")
    ax.set_title("Method-of-characteristics solution")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 0.6)

    snap_origin(fig, label="fig1")
    fig.tight_layout()
    fig.savefig(OUT_DIR / "fig1_linear_transport.png", dpi=200)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Step 2 -- Advection-diffusion + LDF sink, emergence of breakthrough
# ---------------------------------------------------------------------------

def solve_adv_diff_retarded(u=0.05, D=2e-4, R=1.0, L=0.325, N=200,
                            t_end=10.0, n_out=6):
    """Linear-isotherm retardation model:

        R * dC/dt = -u * dC/dz + D * d^2C/dz^2

    where R = 1 + (1-eps)/eps * rho_p * K is the retardation factor.
    R = 1 reduces to pure advection-diffusion; R >> 1 mimics strong adsorption."""
    z = np.linspace(0, L, N)
    dz = z[1] - z[0]
    C_in = 1.0

    def rhs(t, C):
        dCdz = np.zeros_like(C); d2 = np.zeros_like(C)
        dCdz[1:] = (C[1:] - C[:-1]) / dz
        d2[1:-1] = (C[2:] - 2 * C[1:-1] + C[:-2]) / dz ** 2
        dC = (-u * dCdz + D * d2) / R
        dC[0] = 0.0
        return dC

    C0 = np.zeros(N); C0[0] = C_in
    t_eval = np.linspace(0, t_end, n_out)
    sol = solve_ivp(rhs, (0, t_end), C0, method="LSODA",
                    t_eval=t_eval, rtol=1e-6, atol=1e-9)
    return z, sol


def fig_adv_diff_ldf():
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    cmap = plt.get_cmap("plasma")

    # Panel (a) inert bed (R = 1): front travels at u, broadens by D
    ax = axes[0]
    z, sol = solve_adv_diff_retarded(u=0.05, D=2e-4, R=1.0, t_end=6.0, n_out=7)
    for i, t in enumerate(sol.t):
        ax.plot(z, sol.y[:, i], color=cmap(i / (len(sol.t) - 1)),
                label=f"t = {t:.1f} s")
    ax.text(0.03, 0.95, "a", transform=ax.transAxes, fontsize=14,
            fontweight="bold", va="top")
    ax.set_xlabel("z [m]")
    ax.set_ylabel(r"C / $C_\mathrm{in}$")
    ax.set_title("Inert bed (R = 1): front at u, broadened by D")
    ax.legend(loc="upper right", ncol=2)
    ax.set_xlim(0, 0.325)
    ax.set_ylim(-0.05, 1.1)

    # Panel (b) retarded bed (R = 8): front velocity = u/R, MTZ thickens
    ax = axes[1]
    R_ret = 8.0
    z, sol = solve_adv_diff_retarded(u=0.05, D=2e-4, R=R_ret,
                                     t_end=50.0, n_out=7)
    for i, t in enumerate(sol.t):
        ax.plot(z, sol.y[:, i], color=cmap(i / (len(sol.t) - 1)),
                label=f"t = {t:.0f} s")
    # Mark the theoretical front position v_front * t at the last snapshot
    v_front = 0.05 / R_ret
    z_pred = v_front * sol.t[-1]
    ax.axvline(z_pred, color=CMAP["red"], ls=":", lw=0.8)
    ax.annotate(f"front at $z = u\\,t/R$\n= {z_pred:.3f} m",
                xy=(z_pred, 0.5), xytext=(z_pred + 0.03, 0.7),
                color=CMAP["red"], fontsize=9,
                arrowprops=dict(arrowstyle="->", color=CMAP["red"], lw=0.8))
    ax.text(0.03, 0.95, "b", transform=ax.transAxes, fontsize=14,
            fontweight="bold", va="top")
    ax.set_xlabel("z [m]")
    ax.set_ylabel(r"C / $C_\mathrm{in}$")
    ax.set_title(f"Retarded bed (R = {R_ret:.0f}): MTZ formation, breakthrough delayed")
    ax.legend(loc="upper right", ncol=2)
    ax.set_xlim(0, 0.325)
    ax.set_ylim(-0.05, 1.1)

    snap_origin(fig, label="fig2")
    fig.tight_layout()
    fig.savefig(OUT_DIR / "fig2_advdiff_ldf.png", dpi=200)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Step 3 -- Sigmoidal kernels: logistic, Gudermannian, error function
# ---------------------------------------------------------------------------

def fig_sigmoid_kernels():
    """Recreate Hu et al. (2024) Fig. 1: before vs after normalization."""
    x = np.linspace(-6, 6, 600)

    logistic = 1.0 / (1.0 + np.exp(-x))         # range (0, 1)
    gd = 2.0 * np.arctan(np.tanh(x / 2.0))      # range (-pi/2, pi/2)
    er = erf(x)                                 # range (-1, 1)

    # Normalised: shift+scale all to (0, 1) with f(0) = 0.5
    logistic_n = logistic
    gd_n = (gd / np.pi) + 0.5
    er_n = 0.5 * (er + 1)

    fig, axes = plt.subplots(1, 2, figsize=(10, 4.2))

    ax = axes[0]
    ax.plot(x, logistic, color=CMAP["green"], label="Logistic function")
    ax.plot(x, er, color=CMAP["blue"], label="Error function")
    ax.plot(x, gd, color=CMAP["red"], label="Gudermannian function")
    ax.axhline(1, color="k", ls=":", lw=0.8)
    ax.axhline(-1, color="k", ls=":", lw=0.8)
    ax.axhline(np.pi / 2, color="k", ls=":", lw=0.8)
    ax.axhline(-np.pi / 2, color="k", ls=":", lw=0.8)
    ax.axhline(0, color="k", lw=0.5)
    ax.axvline(0, color="k", lw=0.5)
    ax.text(5.5, 1.05, "1", fontsize=9)
    ax.text(5.5, np.pi / 2 + 0.05, r"$\pi/2$", fontsize=9)
    ax.text(5.5, -1.2, r"$-1$", fontsize=9)
    ax.text(5.5, -np.pi / 2 - 0.25, r"$-\pi/2$", fontsize=9)
    ax.text(0.03, 0.95, "a", transform=ax.transAxes, fontsize=14,
            fontweight="bold", va="top")
    ax.set_xlabel("x"); ax.set_ylabel("y")
    ax.set_title("Before normalization")
    ax.legend(loc="lower right")
    ax.set_xlim(-6, 6); ax.set_ylim(-2, 2)

    ax = axes[1]
    ax.plot(x, logistic_n, color=CMAP["green"], label="Logistic function")
    ax.plot(x, er_n, color=CMAP["blue"], label="Error function")
    ax.plot(x, gd_n, color=CMAP["red"], label="Gudermannian function")
    ax.axhline(1, color="k", ls=":", lw=0.8)
    ax.axhline(0.5, color="k", ls=":", lw=0.8)
    ax.axhline(0, color="k", lw=0.5)
    ax.axvline(0, color="k", lw=0.5)
    ax.text(0.03, 0.95, "b", transform=ax.transAxes, fontsize=14,
            fontweight="bold", va="top")
    ax.set_xlabel("x"); ax.set_ylabel("y")
    ax.set_title("After normalization to (0, 1) with f(0) = 0.5")
    ax.legend(loc="lower right")
    ax.set_xlim(-6, 6); ax.set_ylim(-0.05, 1.1)

    snap_origin(fig, label="fig3")
    fig.tight_layout()
    fig.savefig(OUT_DIR / "fig3_sigmoid_kernels.png", dpi=200)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Step 4 -- BA / Thomas / Yoon-Nelson algebraic equivalence on real data
# ---------------------------------------------------------------------------

def thomas_yn(t, k, tau):
    return 1.0 / (1.0 + np.exp(k * (tau - t)))


def clark_model(t, A, r, n, C_inf=1.0):
    # Clark (1987): C/C0 = C_inf * (1 / (1 + A * exp(-r t)))^(1/(n-1))
    n_eff = max(n, 1.05)
    return C_inf * (1.0 / (1.0 + A * np.exp(-r * t))) ** (1.0 / (n_eff - 1.0))


def _resample(t, y, n_target: int = 60):
    """Thin to n_target evenly-spaced-in-time points with linear interp; helps
    the noisy SUTD CSVs fit cleanly without 1000+ point oversampling."""
    if len(t) <= n_target:
        return t, y
    t_new = np.linspace(t.min(), t.max(), n_target)
    y_new = np.interp(t_new, t, y)
    return t_new, y_new


def _tau_seed(t, y, target=0.5) -> float:
    if y.max() < target or y.min() > target:
        return float(t[len(t) // 2])
    # interp wants increasing x; y may be noisy non-monotonic -> sort
    order = np.argsort(y)
    return float(np.interp(target, y[order], t[order]))


def fit_thomas_yn(t, y):
    t2, y2 = _resample(t, y, 60)
    p0 = [0.1, _tau_seed(t2, y2)]
    bounds = ([1e-4, 1e-3], [10, t2.max() * 4])
    popt, _ = curve_fit(thomas_yn, t2, y2, p0=p0, bounds=bounds, maxfev=5000)
    return popt


def fit_clark(t, y):
    t2, y2 = _resample(t, y, 60)
    Cinf0 = float(max(0.6, min(1.0, np.percentile(y2, 95))))
    p0 = [50.0, 0.05, 2.0, Cinf0]
    bounds = ([1e-2, 1e-4, 1.05, 0.3], [1e6, 10, 20, 1.05])
    popt, _ = curve_fit(clark_model, t2, y2, p0=p0, bounds=bounds, maxfev=20000)
    return popt  # (A, r, n, C_inf)


def fig_ba_thomas_yn_equivalence(runs: list[BTRun]):
    """Fig. 2 schematic + empirical proof on three SUTD runs."""
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.4))

    # Panel (a) -- schematic redraw of Hu (2024) Fig. 2 with our parameters
    ax = axes[0]
    t = np.linspace(0, 150, 500)
    sym = thomas_yn(t, k=0.10, tau=50.0)
    asym = clark_model(t, A=300, r=0.06, n=4.0)
    ax.plot(t, sym, color=CMAP["red"], label="Thomas / B-A / Y-N (symmetric)")
    ax.plot(t, asym, color=CMAP["green"], label="Clark, $n = 4$ (asymmetric)")
    ax.axhline(0.5, color="k", ls=":", lw=0.8)
    ax.text(125, 0.55, r"$C/C_0 = 0.5$", fontsize=9)
    ax.axvline(50, color=CMAP["red"], ls=":", lw=0.8)
    ax.fill_between(t[t <= 50], 0, sym[t <= 50], color="#caa6e8", alpha=0.5)
    ax.fill_between(t[t <= 50], sym[t <= 50], asym[t <= 50],
                    where=(asym[t <= 50] > sym[t <= 50]),
                    color="#f4b8c4", alpha=0.6)
    ax.annotate(r"$(q_0 m / v c_0,\ 0.5)$", xy=(50, 0.5),
                xytext=(8, 0.62), color=CMAP["red"],
                arrowprops=dict(arrowstyle="->", color=CMAP["red"]))
    ax.annotate(r"$(b/v,\ 0.5)$", xy=(50, 0.5),
                xytext=(60, 0.42), color=CMAP["blue"])
    ax.text(0.03, 0.95, "a", transform=ax.transAxes, fontsize=14,
            fontweight="bold", va="top")
    ax.set_xlabel("t  [min]"); ax.set_ylabel(r"$C/C_0$")
    ax.set_title("B-A / Thomas / Y-N collapse to a single logistic")
    ax.legend(loc="lower right")
    ax.set_xlim(0, 150); ax.set_ylim(0, 1.05)

    # Panel (b) -- fit same logistic to three SUTD runs; show k_YN, k_BA, k_T
    ax = axes[1]
    if runs:
        # pick three runs spanning flow
        chosen = _pick_runs(runs, [(50, 2), (100, 4), (150, 6)])
        colors = [CMAP["green"], CMAP["blue"], CMAP["red"]]
        for run, col in zip(chosen, colors):
            mask = run.CC0 > 0.001
            t = run.t_min[mask]; y = run.CC0[mask]
            try:
                k, tau = fit_thomas_yn(t, y)
            except RuntimeError:
                continue
            t_fit = np.linspace(0, t.max(), 400)
            ax.plot(t, y, "o", ms=3, color=col, alpha=0.6, label=run.label)
            ax.plot(t_fit, thomas_yn(t_fit, k, tau), "--", color=col, lw=1.2)
            # report equivalence: k_T = k / C0,  k_BA = k / C0,  k_YN = k
            print(f"  fit {run.label}: k_YN = {k:.4f} 1/min, "
                  f"k_T = k_BA = {k / run.C0_ppm:.3e} L/(mg.min equiv), "
                  f"tau = {tau:.1f} min")
    ax.axhline(0.5, color="k", ls=":", lw=0.8)
    ax.text(0.03, 0.95, "b", transform=ax.transAxes, fontsize=14,
            fontweight="bold", va="top")
    ax.set_xlabel("t  [min]"); ax.set_ylabel(r"$C/C_0$")
    ax.set_title("PEI@SiO$_2$ runs fitted with the common logistic")
    ax.legend(loc="lower right")
    ax.set_xlim(left=0); ax.set_ylim(-0.05, 1.1)

    snap_origin(fig, label="fig4")
    fig.tight_layout()
    fig.savefig(OUT_DIR / "fig4_ba_thomas_yn_equivalence.png", dpi=200)
    plt.close(fig)


def _pick_runs(runs: list[BTRun], wanted: list[tuple[float, float]]) -> list[BTRun]:
    out = []
    for fw, mw in wanted:
        for r in runs:
            if abs(r.flow_mlmin - fw) < 1 and abs(r.mass_g - mw) < 0.1:
                out.append(r); break
    return out


# ---------------------------------------------------------------------------
# Step 5 -- Chern-Chien breakthrough: Langmuir vs Freundlich isotherm closures
# ---------------------------------------------------------------------------

def chernchien_langmuir(t, tau, K, C_inf=1.0):
    """Symmetric Chern--Chien (single-MTZ asymptote) with Langmuir kernel.

    C_inf is the operational plateau (= 1 in theory, but < 1 in practice when
    the run is truncated before the slow PEI bulk-diffusion tail saturates).
    """
    z = K * (t - tau)
    return C_inf * np.where(z > -700, 1.0 / (1.0 + np.exp(-z)), 0.0)


def chernchien_freundlich(t, tau, K, n, C_inf=1.0):
    """Freundlich-type Chern--Chien.  n > 1 sharpens, n < 1 lengthens the tail.

    Functional form: c/c0 = C_inf * [1 + (n - 1) * exp(-K(t - tau))]^(1/(1 - n))
    Recovers Langmuir-type logistic as n -> 1.
    """
    if abs(n - 1.0) < 1e-3:
        return chernchien_langmuir(t, tau, K, C_inf)
    arg = 1.0 + (n - 1.0) * np.exp(-K * (t - tau))
    arg = np.where(arg > 1e-9, arg, 1e-9)
    return C_inf * arg ** (1.0 / (1.0 - n))


def fit_chernchien_langmuir(t, y):
    t2, y2 = _resample(t, y, 60)
    Cinf0 = float(max(0.6, min(1.0, np.percentile(y2, 95))))
    p0 = [_tau_seed(t2, y2 / Cinf0), 0.1, Cinf0]
    bounds = ([1e-2, 1e-4, 0.3], [t2.max() * 4, 10, 1.05])
    popt, _ = curve_fit(chernchien_langmuir, t2, y2, p0=p0, bounds=bounds,
                        maxfev=10000)
    return popt  # (tau, K, C_inf)


def fit_chernchien_freundlich(t, y):
    t2, y2 = _resample(t, y, 60)
    Cinf0 = float(max(0.6, min(1.0, np.percentile(y2, 95))))
    p0 = [_tau_seed(t2, y2 / Cinf0), 0.1, 1.5, Cinf0]
    bounds = ([1e-2, 1e-4, 1.05, 0.3], [t2.max() * 4, 10, 8, 1.05])
    popt, _ = curve_fit(chernchien_freundlich, t2, y2, p0=p0, bounds=bounds,
                        maxfev=20000)
    return popt  # (tau, K, n, C_inf)


def fig_chernchien(runs: list[BTRun]):
    chosen = _pick_runs(runs, [(50, 4), (100, 4), (150, 4)])
    if len(chosen) < 2:
        chosen = runs[:3]
    colors = [CMAP["green"], CMAP["blue"], CMAP["red"]]

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.4))

    summary = {"langmuir": [], "freundlich": []}

    for panel_idx, (ax, kind) in enumerate(zip(axes, ["langmuir", "freundlich"])):
        for run, col in zip(chosen, colors):
            mask = run.CC0 > 0.001
            t = run.t_min[mask]; y = run.CC0[mask]
            try:
                if kind == "langmuir":
                    tau, K, Cinf = fit_chernchien_langmuir(t, y)
                    t_fit = np.linspace(0, t.max(), 400)
                    y_fit = chernchien_langmuir(t_fit, tau, K, Cinf)
                    summary["langmuir"].append((run.label, tau, K, Cinf,
                        _r2(y, chernchien_langmuir(t, tau, K, Cinf))))
                else:
                    tau, K, n, Cinf = fit_chernchien_freundlich(t, y)
                    t_fit = np.linspace(0, t.max(), 400)
                    y_fit = chernchien_freundlich(t_fit, tau, K, n, Cinf)
                    summary["freundlich"].append((run.label, tau, K, n, Cinf,
                        _r2(y, chernchien_freundlich(t, tau, K, n, Cinf))))
            except RuntimeError:
                continue
            ax.plot(t, y, "o", ms=3, color=col, alpha=0.55, label=run.label)
            ax.plot(t_fit, y_fit, "--", color=col, lw=1.4)
        ax.axhline(0.5, color="k", ls=":", lw=0.7)
        ax.axhline(1.0, color="k", ls=":", lw=0.7)
        ax.text(0.03, 0.95, "ab"[panel_idx], transform=ax.transAxes,
                fontsize=14, fontweight="bold", va="top")
        ax.set_xlabel("t  [min]"); ax.set_ylabel(r"$C/C_0$")
        ax.set_xlim(left=0); ax.set_ylim(-0.05, 1.1)
        ax.legend(loc="lower right")
        ax.set_title("Langmuir-type Chern-Chien"
                     if kind == "langmuir" else
                     "Freundlich-type Chern-Chien")
        # Annotate operational saturation on each fit
        if kind == "langmuir" and summary["langmuir"]:
            last_Cinf = summary["langmuir"][-1][3]
            ax.annotate(f"operational plateau\n$C_\\infty/C_0 \\approx$ {last_Cinf:.2f}",
                        xy=(t.max() * 0.95, last_Cinf),
                        xytext=(t.max() * 0.4, 0.55), fontsize=8,
                        color=CMAP["grey"],
                        arrowprops=dict(arrowstyle="->", color=CMAP["grey"], lw=0.8))

    snap_origin(fig, label="fig5")
    fig.tight_layout()
    fig.savefig(OUT_DIR / "fig5_chernchien_langmuir_freundlich.png", dpi=200)
    plt.close(fig)

    # Echo fit summary -- useful for the discussion of hidden parameters
    print("\nChern-Chien Langmuir fits (tau_BT, K, C_inf, R^2):")
    for lab, tau, K, Cinf, r2 in summary["langmuir"]:
        print(f"  {lab:18s}  tau = {tau:6.1f} min   K = {K:.4f} 1/min   "
              f"C_inf = {Cinf:.2f}   R^2 = {r2:.4f}")
    print("\nChern-Chien Freundlich fits (tau_BT, K, n, C_inf, R^2):")
    for lab, tau, K, n, Cinf, r2 in summary["freundlich"]:
        print(f"  {lab:18s}  tau = {tau:6.1f} min   K = {K:.4f} 1/min   "
              f"n = {n:.2f}   C_inf = {Cinf:.2f}   R^2 = {r2:.4f}")

    return summary


def _r2(y, yhat):
    ss_res = float(np.sum((y - yhat) ** 2))
    ss_tot = float(np.sum((y - np.mean(y)) ** 2))
    return 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")


# ---------------------------------------------------------------------------
# Step 6 -- 2x2 model-comparison grid on PEI@SiO2 data with Hu (2020) curve diagnostics
# ---------------------------------------------------------------------------

def fig_pei_model_comparison(runs: list[BTRun]):
    """Mirror Screenshot 2026-05-26 135001.png layout (a/b/c/d panels), but use
    SUTD data and the four families: Langmuir-Chern-Chien (logistic),
    Freundlich-Chern-Chien, Clark, and fractal-like Gudermannian dose-response.
    """
    chosen = _pick_runs(runs, [(50, 4), (100, 4), (150, 4), (200, 6)])
    if len(chosen) < 4:
        chosen = (runs * 4)[:4]

    fig, axes = plt.subplots(2, 2, figsize=(11, 8.2))
    axes = axes.flatten()
    labels = ["a", "b", "c", "d"]
    reference_lines = [None, 0.8, 0.5, 0.2]

    for ax, run, lab, ref in zip(axes, chosen, labels, reference_lines):
        mask = run.CC0 > 0.001
        t = run.t_min[mask]; y = run.CC0[mask]
        t_fit = np.linspace(0, t.max(), 500)

        # Color: green, blue, red, orange for the four runs
        col = CMAP["green"] if "50 mL" in run.label else (
            CMAP["blue"] if "100 mL" in run.label else (
                CMAP["red"] if "150 mL" in run.label else CMAP["orange"]))

        ax.plot(t, y, "o", ms=3.5, color=col, alpha=0.7, label="experiment")

        try:
            tau_L, K_L, Cinf_L = fit_chernchien_langmuir(t, y)
            ax.plot(t_fit, chernchien_langmuir(t_fit, tau_L, K_L, Cinf_L), "--",
                    color="k", lw=1.0,
                    label=f"Chern-Chien Langmuir (C$_\\infty$={Cinf_L:.2f})")
        except RuntimeError:
            pass
        try:
            tau_F, K_F, n_F, Cinf_F = fit_chernchien_freundlich(t, y)
            ax.plot(t_fit, chernchien_freundlich(t_fit, tau_F, K_F, n_F, Cinf_F), "-.",
                    color=CMAP["purple"], lw=1.0,
                    label=f"Chern-Chien Freundlich (n={n_F:.2f})")
        except RuntimeError:
            pass
        try:
            A_C, r_C, n_C, Cinf_C = fit_clark(t, y)
            ax.plot(t_fit, clark_model(t_fit, A_C, r_C, n_C, Cinf_C), ":",
                    color=CMAP["red"], lw=1.4, label=f"Clark (n={n_C:.2f})")
        except RuntimeError:
            pass

        if ref is not None:
            ax.axhline(ref, color="k", ls=":", lw=0.7)
            ax.text(0.04 * t.max(), ref + 0.02, f"C/C$_0$ = {ref}", fontsize=8)

        ax.text(0.03, 0.95, lab, transform=ax.transAxes, fontsize=14,
                fontweight="bold", va="top")
        ax.text(0.97, 0.05, run.label, transform=ax.transAxes, ha="right",
                fontsize=9)
        ax.set_xlabel("t  [min]"); ax.set_ylabel(r"$C/C_0$")
        ax.set_xlim(left=0); ax.set_ylim(-0.05, 1.1)
        if ax is axes[0]:
            ax.legend(loc="lower right")

    fig.suptitle("PEI@SiO$_2$ breakthrough -- model comparison "
                 "(C$_0$ $\\approx$ 4% CO$_2$ on SUTD rig)", y=0.995)
    snap_origin(fig, label="fig6")
    fig.tight_layout()
    fig.savefig(OUT_DIR / "fig6_pei_model_grid.png", dpi=200)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Step 7 -- Hu (2020) curve-shape diagnostics: t_i, t_50, mu_max, lambda
# ---------------------------------------------------------------------------

def curve_diagnostics(t, y) -> dict:
    t = np.asarray(t); y = np.asarray(y)
    # t_50: time at C/C0 = 0.5
    if y.max() < 0.5 or y.min() > 0.5:
        t50 = float("nan")
    else:
        t50 = float(np.interp(0.5, y, t))
    # mu_max and t_i: max slope + its location
    dydt = np.gradient(y, t)
    i_max = int(np.argmax(dydt))
    mu_max = float(dydt[i_max])
    t_i = float(t[i_max])
    # lambda: intersection of max-slope tangent with y = 0
    y_i = float(y[i_max])
    lam = float(t_i - y_i / mu_max) if mu_max > 0 else float("nan")
    return {"t_50": t50, "t_i": t_i, "mu_max": mu_max, "lambda": lam,
            "skew": (t_i - t50)}


def fig_curve_diagnostics(runs: list[BTRun]):
    chosen = _pick_runs(runs, [(50, 4), (100, 4), (150, 4)])
    if len(chosen) < 2:
        chosen = runs[:3]
    colors = [CMAP["green"], CMAP["blue"], CMAP["red"]]

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.4))

    ax = axes[0]
    diag_rows = []
    for run, col in zip(chosen, colors):
        mask = run.CC0 > 0.001
        t = run.t_min[mask]; y = run.CC0[mask]
        d = curve_diagnostics(t, y)
        diag_rows.append((run.label, d))
        ax.plot(t, y, "-", color=col, lw=1.2, label=run.label)
        if np.isfinite(d["t_50"]):
            ax.axvline(d["t_50"], color=col, ls=":", lw=0.7)
        if np.isfinite(d["t_i"]):
            ax.plot(d["t_i"], np.interp(d["t_i"], t, y), "x", color=col,
                    ms=8, mew=2)
    ax.axhline(0.5, color="k", ls=":", lw=0.7)
    ax.text(0.03, 0.95, "a", transform=ax.transAxes, fontsize=14,
            fontweight="bold", va="top")
    ax.set_xlabel("t  [min]"); ax.set_ylabel(r"$C/C_0$")
    ax.set_title("Breakthrough curves with $t_i$ (x) and $t_{50}$ (dotted)")
    ax.legend(loc="lower right")
    ax.set_xlim(left=0); ax.set_ylim(-0.05, 1.1)

    ax = axes[1]
    for run, col in zip(chosen, colors):
        mask = run.CC0 > 0.001
        t = run.t_min[mask]; y = run.CC0[mask]
        # Smooth derivative: fit a logistic and differentiate analytically
        try:
            tau, K, Cinf = fit_chernchien_langmuir(t, y)
            t_grid = np.linspace(t.min(), t.max(), 400)
            y_smooth = chernchien_langmuir(t_grid, tau, K, Cinf)
            dydt = np.gradient(y_smooth, t_grid)
            ax.plot(t_grid, dydt, color=col, lw=1.4, label=run.label)
            i_peak = int(np.argmax(dydt))
            ax.plot(t_grid[i_peak], dydt[i_peak], "x", color=col, ms=9, mew=2)
        except RuntimeError:
            continue
    ax.text(0.03, 0.95, "b", transform=ax.transAxes, fontsize=14,
            fontweight="bold", va="top")
    ax.set_xlabel("t  [min]"); ax.set_ylabel(r"$\mathrm{d}(C/C_0)/\mathrm{d}t$")
    ax.set_title(r"Rate profile -- diagnostic for symmetry ($\mu_\mathrm{max}$ at $t_i$)")
    ax.legend(loc="upper right")
    ax.set_xlim(left=0)

    snap_origin(fig, label="fig7")
    fig.tight_layout()
    fig.savefig(OUT_DIR / "fig7_curve_diagnostics.png", dpi=200)
    plt.close(fig)

    print("\nCurve-shape diagnostics (Hu, Xie & Zhang 2020):")
    print(f"  {'run':18s}  {'t_50':>8s}  {'t_i':>8s}  {'mu_max':>10s}  "
          f"{'lambda':>8s}  {'skew = t_i - t_50':>18s}")
    for lab, d in diag_rows:
        print(f"  {lab:18s}  {d['t_50']:8.2f}  {d['t_i']:8.2f}  "
              f"{d['mu_max']:10.4f}  {d['lambda']:8.2f}  {d['skew']:18.2f}")


# ---------------------------------------------------------------------------
# Step 8 -- Residual plots across model families (Hu 2024 Fig. 4 analogue)
# ---------------------------------------------------------------------------

def fig_residuals(runs: list[BTRun]):
    chosen = _pick_runs(runs, [(100, 4)])
    if not chosen:
        chosen = runs[:1]
    run = chosen[0]
    mask = run.CC0 > 0.001
    t = run.t_min[mask]; y = run.CC0[mask]

    fits = {}
    try:
        tau_L, K_L, Cinf_L = fit_chernchien_langmuir(t, y)
        fits[f"Chern-Chien Langmuir (C$_\\infty$={Cinf_L:.2f})"] = \
            chernchien_langmuir(t, tau_L, K_L, Cinf_L)
    except RuntimeError:
        pass
    try:
        tau_F, K_F, n_F, Cinf_F = fit_chernchien_freundlich(t, y)
        fits[f"Chern-Chien Freundlich (n={n_F:.2f})"] = \
            chernchien_freundlich(t, tau_F, K_F, n_F, Cinf_F)
    except RuntimeError:
        pass
    try:
        A_C, r_C, n_C, Cinf_C = fit_clark(t, y)
        fits[f"Clark (n={n_C:.2f}, C$_\\infty$={Cinf_C:.2f})"] = \
            clark_model(t, A_C, r_C, n_C, Cinf_C)
    except RuntimeError:
        pass

    fig, ax = plt.subplots(figsize=(7, 4.4))
    cols = [CMAP["green"], CMAP["blue"], CMAP["red"]]
    for (label, yhat), col in zip(fits.items(), cols):
        ax.plot(yhat, y - yhat, "o", ms=4, color=col, alpha=0.65, label=label)
    ax.axhline(0, color="k", lw=0.7)
    ax.axhline(0.02, color="k", ls=":", lw=0.6)
    ax.axhline(-0.02, color="k", ls=":", lw=0.6)
    ax.set_xlabel("Predicted $C/C_0$")
    ax.set_ylabel("Residual (experiment - model)")
    ax.set_title(f"Residuals on {run.label}  --  thinner residual band wins")
    ax.legend(loc="upper right")
    snap_origin(fig, label="fig8")
    fig.tight_layout()
    fig.savefig(OUT_DIR / "fig8_residuals.png", dpi=200)
    plt.close(fig)

    print("\nResidual summary:")
    for label, yhat in fits.items():
        print(f"  {label:38s}  RMSE = {np.sqrt(np.mean((y - yhat)**2)):.4f}   "
              f"R^2 = {_r2(y, yhat):.4f}")


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

def main():
    print(f"Output dir: {OUT_DIR}")
    runs = load_runs()
    print(f"Loaded {len(runs)} cleaned breakthrough runs:")
    for r in runs:
        print(f"  - {r.label}  (n = {len(r.t_min)}, t_max = {r.t_min.max():.1f} min, "
              f"C/C0_max = {r.CC0.max():.2f})")

    fig_linear_transport()
    fig_adv_diff_ldf()
    fig_sigmoid_kernels()
    fig_ba_thomas_yn_equivalence(runs)
    fig_chernchien(runs)
    fig_pei_model_comparison(runs)
    fig_curve_diagnostics(runs)
    fig_residuals(runs)

    print("\nDone. Figures written to:", OUT_DIR)


if __name__ == "__main__":
    main()

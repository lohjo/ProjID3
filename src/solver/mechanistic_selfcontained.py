"""Self-contained mechanistic packed-bed CO2 breakthrough solver.

Implements the model of src/docs/mechanistic-model.md (mass A.1, LDF A.2,
Toth A.3, energy A.5) with the finite-volume / Danckwerts MOL scheme (b) of
Part E. Verifies against the closed-form limits of Part D — in particular the
Rankine–Hugoniot jump condition (D.3) for the isothermal equilibrium shock —
and globally fits the isothermal Toth triple (n_s, b, t) plus LDF k across the
five measured bench runs (run 3/4/5/6/8) by integrating the PDE.

Self-contained: reads ONLY the CSVs in src/solver/data/new runs/. No imports
from breakthrough_fit/ or any other repo module.

Usage (repo root, venv active):
    python src/solver/mechanistic_selfcontained.py            # all stages
    python src/solver/mechanistic_selfcontained.py v1 v2      # subset: v1 v2 v3 v4 fit
"""

import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
from datetime import datetime
from pathlib import Path

import numpy as np
from scipy import sparse
from scipy.integrate import solve_ivp
from scipy.optimize import least_squares
from scipy.special import erfc

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

DATA_DIR = Path(__file__).parent / "data" / "new runs"
OUT_DIR = Path(__file__).parents[1] / "img" / "generated" / "mechanistic_selfcontained"

R_GAS = 8.314  # J mol-1 K-1

# ---------------------------------------------------------------------------
# 1. Constants & run metadata (measurements block; audited 2026-05-31 values)
# ---------------------------------------------------------------------------
D_COL = 8.2e-3                      # m, column i.d. (measured)
A_COL = np.pi * (D_COL / 2) ** 2    # m2 bed cross-section
M_SORB = 8.00e-3                    # kg sorbent (measured, ~8.00 g)
T_AMB = 298.0                       # K  — ambient, FLAG: uncontrolled
P_TOT = 101325.0                    # Pa — FLAG: assumed
C_TOT = P_TOT / (R_GAS * T_AMB)     # mol m-3 total gas

# FLAGGED PLACEHOLDERS (repo open items — owner: lab / Stampi-Bombelli):
EPS = 0.40        # bed voidage; rho_p unknown so eps is NOT physical yet
D_M = 1.6e-5      # m2/s molecular diffusivity CO2-air (literature order)
D_P_PART = 2e-3   # m particle size placeholder for D_L correlation
DH0 = 70e3        # J/mol heat of adsorption (literature order, amine-CO2)
CHI = 0.0         # Toth n_s(T) exponent — non-identifiable at single T
H_W = 30.0        # W m-2 K-1 wall coefficient (literature order)
RHO_G = 1.2       # kg/m3 gas density
CP_G = 1.0e3      # J/kg/K gas cp
CP_S = 1.0e3      # J/kg/K sorbent cp placeholder
LAM_EFF = 0.2     # W/m/K effective axial bed conductivity placeholder

FLAGS = [
    ("eps", EPS, "bed voidage — rho_p open item, eps not physical"),
    ("D_L corr", "0.7*Dm+0.5*dp*vi", "axial dispersion correlation, no tracer run"),
    ("DH0", DH0, "literature order; non-identifiable at single T"),
    ("chi", CHI, "fixed 0; non-identifiable at single T"),
    ("h_w", H_W, "literature packed-bed order"),
    ("c_ps", CP_S, "solid cp placeholder"),
    ("T_amb,P", (T_AMB, P_TOT), "ambient assumed 298 K / 101.325 kPa"),
]

# run name -> (flow mL/min, bed length m)  — measurements block, post-audit
RUNS = {
    "run 1": (50.0, 0.235),
    "run 2": (100.0, 0.240),
    "run 3": (150.0, 0.235),
    "run 4": (50.0, 0.230),
    "run 5": (100.0, 0.233),
    "run 6": (150.0, 0.240),
    "run 7": (50.0, 0.245),
    "run 8": (100.0, 0.240),
    "run 9": (150.0, 0.240),
}


def superficial_u(flow_ml_min):
    return flow_ml_min * 1e-6 / 60.0 / A_COL  # m/s


def d_axial(u):
    """D_L ~ 0.7 Dm + 0.5 dp v_i (flagged correlation, doc §C.4)."""
    return 0.7 * D_M + 0.5 * D_P_PART * (u / EPS)


def ppm_to_molm3(ppm):
    return ppm * 1e-6 * P_TOT / (R_GAS * T_AMB)


# ---------------------------------------------------------------------------
# 2. CSV parser (formats: Time,,,C / Time,,C / Time,C ; last col = ppm)
# ---------------------------------------------------------------------------
def parse_run(name):
    path = DATA_DIR / f"{name}.csv"
    times, conc = [], []
    with open(path) as fh:
        next(fh)  # header
        for line in fh:
            parts = line.strip().split(",")
            if len(parts) < 2 or not parts[0]:
                continue
            try:
                ts = datetime.strptime(parts[0], "%m/%d/%y %H:%M:%S.%f")
                c = float(parts[-1])
            except ValueError:
                continue
            times.append(ts)
            conc.append(c)
    t0 = times[0]
    t = np.array([(ts - t0).total_seconds() for ts in times])
    c = np.array(conc)
    # 5-point median despike
    if len(c) >= 5:
        pad = np.pad(c, 2, mode="edge")
        med = np.median(np.lib.stride_tricks.sliding_window_view(pad, 5), axis=1)
        spikes = np.abs(c - med) > 0.1 * max(np.max(med), 1.0)
        c = np.where(spikes, med, c)
    n_tail = max(5, len(c) // 20)
    plateau = float(np.mean(c[-n_tail:]))
    # baseline: mean of samples before rise (first 10 or pre-2% crossing)
    thresh = 0.02 * plateau
    rise = np.argmax(c > thresh) if np.any(c > thresh) else 0
    baseline = float(np.mean(c[: max(3, rise)])) if rise > 0 else 0.0
    # step-time guess: first crossing of baseline + 2% of span
    span_thresh = baseline + 0.02 * (plateau - baseline)
    idx = np.argmax(c > span_thresh)
    t0_guess = float(t[idx]) if np.any(c > span_thresh) else 0.0
    return {
        "t": t, "ppm": c, "plateau": plateau, "baseline": baseline,
        "t0_guess": t0_guess,
        "cf": ppm_to_molm3(plateau - baseline),
        "y_norm": (c - baseline) / (plateau - baseline),
    }


# ---------------------------------------------------------------------------
# 3. Isotherm closures (isothermal pressure basis; Toth eq. A.3)
#    q*(p) = n_s * b p / (1+(b p)^t)^(1/t),  p in kPa, b in kPa^-1
# ---------------------------------------------------------------------------
def p_kpa(c, T=T_AMB):
    return c * R_GAS * T / 1e3


def toth_q(c, ns, bP, tt, T=T_AMB):
    bp = np.maximum(bP * p_kpa(c, T), 0.0)
    return ns * bp / (1.0 + bp ** tt) ** (1.0 / tt)


def toth_dqdc(c, ns, bP, tt, T=T_AMB):
    """dq*/dc = n_s b_c / (1+(b_c c)^t)^((1+t)/t)  (Lemma A.1), b_c = bP R T/1e3."""
    bc = bP * R_GAS * T / 1e3
    s = np.maximum(bc * c, 0.0) ** tt
    return ns * bc / (1.0 + s) ** ((1.0 + tt) / tt)


def toth_bP_T(bP0, T):
    """van't Hoff b(T), reference T_AMB (A.3); used only in non-isothermal demo."""
    return bP0 * np.exp(DH0 / (R_GAS * T_AMB) * (T_AMB / T - 1.0))


# ---------------------------------------------------------------------------
# 4. Solver core — FV scheme (b), Danckwerts flux inlet (Part E)
# ---------------------------------------------------------------------------
def rhs_iso(t, y, N, dz, u, DL, k, alpha_b, cf, qstar, variable_u):
    c, q = y[:N], y[N:]
    dq = k * (qstar(c) - q)
    if variable_u:
        # Remark A.1: u(z) = u_in - (alpha_b/c_tot) * int_0^z q_t dz'
        u_face = u - (alpha_b / C_TOT) * np.cumsum(dq) * dz  # faces 1/2..N-1/2
    else:
        u_face = np.full(N, u)
    F = np.empty(N + 1)
    F[0] = u * cf                                   # Danckwerts: exact inlet flux
    F[1:N] = u_face[:-1] * c[:-1] - EPS * DL * np.diff(c) / dz
    F[N] = u_face[-1] * c[-1]                       # zero-gradient outlet
    dc = (-np.diff(F) / dz - alpha_b * dq) / EPS
    return np.concatenate([dc, dq])


def rhs_noniso(t, y, N, dz, u, DL, k, alpha_b, cf, ns, bP, tt, hw, Tf):
    c, q, T = y[:N], y[N:2 * N], y[2 * N:]
    qs = toth_q(c, ns, toth_bP_T(bP, T), tt, T)
    dq = k * (qs - q)
    Ch = EPS * RHO_G * CP_G + alpha_b * CP_S
    F = np.empty(N + 1)
    F[0] = u * cf
    F[1:N] = u * c[:-1] - EPS * DL * np.diff(c) / dz
    F[N] = u * c[-1]
    dc = (-np.diff(F) / dz - alpha_b * dq) / EPS
    G = np.empty(N + 1)
    G[0] = u * RHO_G * CP_G * Tf
    G[1:N] = u * RHO_G * CP_G * T[:-1] - LAM_EFF * np.diff(T) / dz
    G[N] = u * RHO_G * CP_G * T[-1]
    dT = (-np.diff(G) / dz + alpha_b * DH0 * dq - 4 * hw / D_COL * (T - Tf)) / Ch
    return np.concatenate([dc, dq, dT])


def jac_pattern(N, nblk):
    """Block sparsity: tridiagonal in c (and T), pointwise couplings."""
    tri = sparse.diags([np.ones(N - 1), np.ones(N), np.ones(N - 1)], [-1, 0, 1])
    eye = sparse.eye(N)
    blocks = [[tri if (i == j and i != 1) else eye for j in range(nblk)]
              for i in range(nblk)]
    return sparse.bmat(blocks, format="csr")


def simulate(N, L, u, DL, k, alpha_b, cf, qstar, t_end, t_eval=None,
             variable_u=False, rtol=1e-6, events=None):
    dz = L / N
    y0 = np.zeros(2 * N)
    qf = float(qstar(np.array([cf]))[0])
    atol = np.concatenate([np.full(N, 1e-6 * cf), np.full(N, 1e-6 * max(qf, 1e-9))])
    # variable_u: cumsum(dq) couples every cell to all upstream cells — the
    # tridiagonal pattern is then WRONG and cripples Newton; use dense FD.
    sparsity = None if variable_u else jac_pattern(N, 2)
    sol = solve_ivp(
        rhs_iso, (0.0, t_end), y0, method="BDF", t_eval=t_eval,
        rtol=rtol, atol=atol, jac_sparsity=sparsity, events=events,
        args=(N, dz, u, DL, k, alpha_b, cf, qstar, variable_u))
    if not sol.success:
        raise RuntimeError(f"solve_ivp failed: {sol.message}")
    sol.N, sol.dz = N, dz
    return sol


def mass_drift(sol, u, alpha_b, cf, dz, N):
    """Inventory identity (B.3): dM/dt = u cf - u c_out; relative drift."""
    c = sol.y[:N, :]
    q = sol.y[N:2 * N, :]
    M = dz * np.sum(EPS * c + alpha_b * q, axis=0)
    inflow = np.trapezoid(np.full_like(sol.t, u * cf), sol.t)
    outflow = np.trapezoid(u * c[-1, :], sol.t)
    return abs((M[-1] - M[0]) - (inflow - outflow)) / (u * cf * sol.t[-1])


# ---------------------------------------------------------------------------
# 5. Verification stages
# ---------------------------------------------------------------------------
def stage_v1():
    """Gate-A analogue: k=0 ADE vs Ogata–Banks (D.5)."""
    print("\n=== V1: no-adsorption ADE vs Ogata–Banks erfc (Gate A analogue) ===")
    u = superficial_u(100.0)          # run-5-like
    L = 0.212
    DL = 5e-5                          # doc §C.4 value for comparability
    cf = ppm_to_molm3(95000.0)
    vi, Deff = u / EPS, DL
    print(f"  u={u:.4g} m/s  v_i={vi:.4g}  Pe_i={vi*L/DL:.0f}")
    t_end = 2.5 * L / vi
    t_eval = np.linspace(1e-3, t_end, 400)

    def exact(tv):
        a1 = (L - vi * tv) / (2 * np.sqrt(Deff * tv))
        a2 = (L + vi * tv) / (2 * np.sqrt(Deff * tv))
        # second term with exp-log guard against overflow (Pe large)
        with np.errstate(over="ignore"):
            second = np.exp(np.minimum(vi * L / Deff, 700)) * erfc(a2)
        return cf * (0.5 * erfc(a1) + 0.5 * second)

    ce = exact(t_eval)
    errs = {}
    fig, ax = plt.subplots(figsize=(7, 4.5))
    for N in (500, 1000, 2000, 4000):
        sol = simulate(N, L, u, DL, 0.0, 0.0, cf, lambda c: np.zeros_like(c),
                       t_end, t_eval=t_eval)
        cn = sol.y[N - 1, :]
        errs[N] = np.sqrt(np.sum((cn - ce) ** 2) / np.sum(ce ** 2))
        ax.plot(t_eval, cn / cf, lw=1, label=f"FV N={N} (L2 {errs[N]*100:.2f}%)")
    ax.plot(t_eval, ce / cf, "k--", lw=1.5, label="Ogata–Banks (D.5)")
    ax.set_xlabel("t [s]"); ax.set_ylabel("c(L,t)/c_f")
    ax.set_title("V1 — k=0 advection–dispersion vs exact erfc solution")
    ax.legend(); fig.tight_layout()
    fig.savefig(OUT_DIR / "V1_ade_vs_erfc.png", dpi=300); plt.close(fig)

    for N, e in errs.items():
        print(f"  N={N:5d}  L2 error = {e*100:.3f} %")
    ratio = errs[500] / errs[1000]
    print(f"  error ratio N500/N1000 = {ratio:.2f} (first-order upwind -> ~2)")
    assert errs[4000] < 0.01, "Gate A analogue FAILED: L2 >= 1% at N=4000"
    print("  PASS: Gate A analogue (<1 % L2)")


def stage_v2(iso):
    """RH jump condition (D.3) + first-moment invariance (Cor. B.1)."""
    print("\n=== V2: Rankine–Hugoniot shock speed + stoichiometric time ===")
    ns, bP, tt = iso
    u = superficial_u(100.0)
    L = 0.212
    alpha_b = M_SORB / (A_COL * L)
    cf = ppm_to_molm3(95000.0)
    DL = 1e-6
    k = 20.0 * u / L                   # Da = kL/u = 20 -> near-equilibrium
    qstar = lambda c: toth_q(c, ns, bP, tt)
    qf = float(qstar(np.array([cf]))[0])
    v_rh = u * cf / (EPS * cf + alpha_b * qf)             # (D.3)
    t_st = L / v_rh                                        # (D.4)
    print(f"  q*(c_f)={qf:.4g} mol/kg  v_RH={v_rh:.4e} m/s  t_st={t_st:.1f} s")

    N = 800
    t_end = 2.0 * t_st
    t_eval = np.linspace(0, t_end, 800)
    sol = simulate(N, L, u, DL, k, alpha_b, cf, qstar, t_end, t_eval=t_eval)
    z = (np.arange(N) + 0.5) * sol.dz
    # z50(t): front position where c = cf/2, only while fully interior
    z50, tz = [], []
    for j, tj in enumerate(t_eval):
        prof = sol.y[:N, j]
        if prof[0] > 0.9 * cf and prof[-1] < 0.1 * cf:
            i = np.argmax(prof < 0.5 * cf)
            if 0 < i < N:
                frac = (prof[i - 1] - 0.5 * cf) / (prof[i - 1] - prof[i])
                zj = z[i - 1] + frac * sol.dz
                if 0.2 * L < zj < 0.8 * L:
                    z50.append(zj); tz.append(tj)
    slope, icpt = np.polyfit(tz, z50, 1)
    err_v = abs(slope / v_rh - 1)
    cout = sol.y[N - 1, :] / cf
    moment = np.trapezoid(1.0 - cout, t_eval)
    err_m = abs(moment / t_st - 1)
    drift = mass_drift(sol, u, alpha_b, cf, sol.dz, N)
    print(f"  numerical front speed = {slope:.4e} m/s  (error {err_v*100:.3f} %)")
    print(f"  first moment = {moment:.1f} s vs t_st = {t_st:.1f} s "
          f"(error {err_m*100:.3f} %)")
    print(f"  mass-balance drift = {drift:.2e}")

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
    for frac in (0.25, 0.5, 0.75):
        j = np.argmin(np.abs(t_eval - frac * t_st))
        axes[0].plot(z * 100, sol.y[:N, j] / cf, label=f"t={t_eval[j]:.0f} s")
        zsh = v_rh * t_eval[j]
        axes[0].plot([zsh * 100] * 2, [0, 1], ":", color="gray", lw=1)
    axes[0].set_xlabel("z [cm]"); axes[0].set_ylabel("c/c_f")
    axes[0].set_title("Profiles vs RH shock position (dotted)")
    axes[0].legend()
    axes[1].plot(tz, np.array(z50) * 100, "o", ms=3, label="numerical z50(t)")
    tfit = np.array([tz[0], tz[-1]])
    axes[1].plot(tfit, (slope * tfit + icpt) * 100, "-",
                 label=f"fit {slope:.3e} m/s")
    axes[1].plot(tfit, (v_rh * tfit + icpt) * 100, "k--",
                 label=f"v_RH {v_rh:.3e} m/s")
    axes[1].set_xlabel("t [s]"); axes[1].set_ylabel("z50 [cm]")
    axes[1].set_title(f"RH speed check: err {err_v*100:.3f} %")
    axes[1].legend()
    fig.suptitle("V2 — isothermal equilibrium shock: Rankine–Hugoniot verification")
    fig.tight_layout()
    fig.savefig(OUT_DIR / "V2_rh_front.png", dpi=300); plt.close(fig)

    assert err_v < 0.10, "RH speed outside ±10 %"
    assert err_m < 0.02, "first-moment identity violated"
    assert drift < 1e-4, "mass drift >= 1e-4"
    print("  PASS: RH jump condition (±10 % gate; achieved "
          f"{err_v*100:.3f} %), moment identity, mass conservation")


def stage_v3(iso):
    """Exact LDF travelling wave (D.8), Langmuir closure."""
    print("\n=== V3: constant-pattern travelling wave vs closed form (D.8) ===")
    ns, bP, _ = iso
    tt = 1.0                              # D.8 is the Langmuir closed form
    # Verification operating point (feed/flow are operating conditions, not
    # sorbent parameters): b*c_f = 3 so the wave is strongly nonlinear (a
    # weakly nonlinear front is smeared mostly by numerical diffusion and the
    # comparison tests the grid, not (D.8)); low flow so the sample time is
    # >> 1/k and the transient has converged to the constant pattern.
    u = superficial_u(30.0)
    L = 0.212
    alpha_b = M_SORB / (A_COL * L)
    k = 0.02
    bc = bP * R_GAS * T_AMB / 1e3        # concentration-basis b [m3/mol]
    cf = 3.0 / bc
    print(f"  verification point: c_f={cf:.3f} mol/m3 (b*c_f=3), "
          f"u={u*100:.2f} cm/s")
    qstar = lambda c: toth_q(c, ns, bP, tt)
    qf = float(qstar(np.array([cf]))[0])
    v_rh = u * cf / (EPS * cf + alpha_b * qf)
    t_st = L / v_rh
    N = 3000
    t_samp = 0.65 * t_st
    sol = simulate(N, L, u, 1e-9, k, alpha_b, cf, qstar, t_samp,
                   t_eval=[0, t_samp])
    z = (np.arange(N) + 0.5) * (L / N)
    w_num = sol.y[:N, -1] / cf
    eta = z - v_rh * t_samp
    # closed form (D.8): eta(w) = eta0 - (v_rh/(k bc cf)) * phi(w),
    # phi(w) = ln w - (1+bc cf) ln(1-w). Anchor: exact curve through the
    # numeric 50 % crossing (phi(0.5) != 0, so eta0 is NOT the 50 % location).
    phi = lambda w: np.log(w) - (1 + bc * cf) * np.log(1 - w)
    scale = v_rh / (k * bc * cf)
    # numeric 50 % location (w_num decreasing in z)
    eta_num50 = np.interp(0.5, w_num[::-1], eta[::-1])
    eta0 = eta_num50 + scale * phi(0.5)
    mask = (w_num > 0.02) & (w_num < 0.98)
    w_m = np.clip(w_num[mask], 1e-12, 1 - 1e-12)
    eta_exact = eta0 - scale * phi(w_m)
    # compare w at same eta: interpolate exact w(eta) onto numeric eta
    order = np.argsort(eta_exact)
    w_exact_at = np.interp(eta[mask], eta_exact[order], w_m[order])
    rms = np.sqrt(np.mean((w_num[mask] - w_exact_at) ** 2))
    print(f"  b*c_f = {bc*cf:.3f}  v_RH = {v_rh:.3e} m/s  sample t = {t_samp:.0f} s")
    print(f"  RMS deviation (0.02<w<0.98) = {rms*100:.3f} %")

    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot(eta[mask] * 100, w_num[mask], lw=1.5, label="FV numerical profile")
    ax.plot(eta_exact * 100, w_m, "k--", lw=1.2,
            label="implicit closed form (D.8)")
    ax.set_xlabel("η = z − v_RH t [cm]"); ax.set_ylabel("c/c_f")
    ax.set_title(f"V3 — exact LDF travelling wave, RMS {rms*100:.2f}% "
                 f"(tail asymmetry ×{1+bc*cf:.2f})")
    ax.legend(); fig.tight_layout()
    fig.savefig(OUT_DIR / "V3_travelling_wave.png", dpi=300); plt.close(fig)
    assert rms < 0.01, "travelling-wave RMS >= 1 %"
    print("  PASS: travelling wave matches closed form")


def stage_v4(iso):
    """Non-isothermal Toth demo: isothermal / wall-coupled / adiabatic."""
    print("\n=== V4: non-isothermal demo (ILLUSTRATIVE — DH0, h_w, c_ps flagged) ===")
    ns, bP, tt = iso
    u = superficial_u(100.0)
    L = 0.212
    alpha_b = M_SORB / (A_COL * L)
    cf = ppm_to_molm3(95000.0)
    DL = d_axial(u)
    k = 5e-3
    qstar = lambda c: toth_q(c, ns, bP, tt)
    qf = float(qstar(np.array([cf]))[0])
    Ch = EPS * RHO_G * CP_G + alpha_b * CP_S
    dT_ad = alpha_b * DH0 * qf / Ch
    t_st = L * (EPS * cf + alpha_b * qf) / (u * cf)
    print(f"  q_f={qf:.3f} mol/kg  t_st={t_st:.0f} s  ΔT_ad={dT_ad:.1f} K")

    N = 300
    t_end = 3.0 * t_st
    t_eval = np.linspace(0, t_end, 600)
    dz = L / N
    results = {}
    for label, hw in (("wall-coupled", H_W), ("adiabatic", 0.0)):
        y0 = np.concatenate([np.zeros(2 * N), np.full(N, T_AMB)])
        atol = np.concatenate([np.full(N, 1e-6 * cf),
                               np.full(N, 1e-6 * qf), np.full(N, 1e-6)])
        sol = solve_ivp(rhs_noniso, (0, t_end), y0, method="BDF",
                        t_eval=t_eval, rtol=1e-6, atol=atol,
                        jac_sparsity=jac_pattern(N, 3),
                        args=(N, dz, u, DL, k, alpha_b, cf, ns, bP, tt, hw, T_AMB))
        if not sol.success:
            raise RuntimeError(sol.message)
        results[label] = sol
    sol_iso = simulate(N, L, u, DL, k, alpha_b, cf, qstar, t_end, t_eval=t_eval)
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
    axes[0].plot(t_eval, sol_iso.y[N - 1, :] / cf, label="isothermal")
    report = {}
    for label, sol in results.items():
        cout = sol.y[N - 1, :] / cf
        Tmax = sol.y[2 * N:, :].max() - T_AMB
        axes[0].plot(t_eval, cout, label=label)
        axes[1].plot(t_eval, sol.y[3 * N - 1, :] - T_AMB, label=f"{label} T_out")
        tbt = np.interp(0.05, cout, t_eval)
        report[label] = (tbt, Tmax, cout.max())
    tbt_iso = np.interp(0.05, sol_iso.y[N - 1, :] / cf, t_eval)
    axes[0].axhline(0.05, color="gray", ls=":", lw=0.8)
    axes[0].set_xlabel("t [s]"); axes[0].set_ylabel("c(L,t)/c_f")
    axes[0].set_title("Outlet breakthrough"); axes[0].legend()
    axes[1].set_xlabel("t [s]"); axes[1].set_ylabel("T_out − T_0 [K]")
    axes[1].set_title("Outlet temperature excursion"); axes[1].legend()
    fig.suptitle("V4 — non-isothermal Toth demo (placeholder thermal parameters)")
    fig.tight_layout()
    fig.savefig(OUT_DIR / "V4_nonisothermal.png", dpi=300); plt.close(fig)

    print(f"  isothermal    t_BT = {tbt_iso:6.0f} s")
    for label, (tbt, Tmax, cmax) in report.items():
        print(f"  {label:13s} t_BT = {tbt:6.0f} s  ΔT_max = {Tmax:5.1f} K  "
              f"max c/c_f = {cmax:.3f}")
    assert report["adiabatic"][0] < tbt_iso, "adiabatic should break through earlier"
    assert report["adiabatic"][1] > report["wall-coupled"][1]
    print("  PASS: qualitative non-isothermal structure (early BT, thermal excursion)")


# ---------------------------------------------------------------------------
# 6. Global fit to the five measured runs
# ---------------------------------------------------------------------------
def run_conditions(name):
    flow, L = RUNS[name]
    u = superficial_u(flow)
    alpha_b = M_SORB / (A_COL * L)
    return u, L, alpha_b


def prep_fit_data(max_pts=100):
    data = {}
    for name in RUNS:
        d = parse_run(name)
        # cap the fit window shortly after saturation — the flat tail carries
        # no shape information but dominates the ODE solve time
        y = d["y_norm"]
        i_sat = int(np.argmax(y > 0.985)) if np.any(y > 0.985) else len(y) - 1
        t_cap = min(d["t"][i_sat] * 1.10, d["t"][-1])
        sel = d["t"] <= t_cap
        tt, yy = d["t"][sel], y[sel]
        idx = np.linspace(0, len(tt) - 1, min(max_pts, len(tt))).astype(int)
        data[name] = {**d, "tf": tt[idx], "yf": yy[idx], "t_cap": t_cap}
    return data


def model_curves(theta_iso, k, data, N=96, rtol=1e-4, full_span=False):
    """Simulate each run once; return dict name -> (t_grid, C_out(t))."""
    out = {}
    for name in RUNS:
        u, L, alpha_b = run_conditions(name)
        cf = data[name]["cf"]
        qstar = lambda c: toth_q(c, *theta_iso)
        t_end = float(data[name]["t"][-1] if full_span
                      else data[name]["t_cap"]) * 1.05
        t_grid = np.linspace(0, t_end, 200)
        sol = simulate(N, L, u, d_axial(u), k, alpha_b, cf, qstar, t_end,
                       t_eval=t_grid, variable_u=True, rtol=rtol)
        out[name] = (t_grid, sol.y[N - 1, :] / cf)
    return out


def residuals(x, data, fit_t, N=96):
    """x = [ln ns, ln bP, (t), ln k, t0_1..t0_5]; stacked residual vector."""
    ns, bP = np.exp(x[0]), np.exp(x[1])
    if fit_t:
        tt, k = x[2], np.exp(x[3])
        t0s = x[4:]
    else:
        tt, k = 1.0, np.exp(x[2])
        t0s = x[3:]
    try:
        curves = model_curves((ns, bP, tt), k, data, N=N)
    except RuntimeError:
        return np.full(sum(len(data[n]["tf"]) for n in RUNS), 10.0)
    res = []
    for t0, name in zip(t0s, RUNS):
        tg, cg = curves[name]
        ym = np.interp(np.maximum(data[name]["tf"] - t0, 0.0), tg, cg)
        res.append(ym - data[name]["yf"])
    return np.concatenate(res)


def aicc(rss, n, kpar):
    return n * np.log(rss / n) + 2 * kpar + 2 * kpar * (kpar + 1) / (n - kpar - 1)


def fit_model(data, fit_t, label):
    print(f"\n  --- global fit: {label} ---")
    rng = np.random.default_rng(42)
    t0g = [data[n]["t0_guess"] for n in RUNS]
    # multi-start screening over (ns, bP, k); t start 0.5
    cands = []
    for ns0 in (1.0, 2.5):
        for bP0 in (0.1, 1.0):
            for k0 in (1e-3, 8e-3):
                cands.append((ns0, bP0, k0))
    scored = []
    for ns0, bP0, k0 in cands:
        x = [np.log(ns0), np.log(bP0)] + ([0.5] if fit_t else []) + [np.log(k0)] + t0g
        r = residuals(np.array(x), data, fit_t, N=64)
        scored.append((np.sum(r ** 2), x))
        print(f"    screen ns={ns0:.1f} bP={bP0:.2g} k={k0:.1g}: "
              f"SSR={scored[-1][0]:.2f}", flush=True)
    scored.sort(key=lambda s: s[0])
    lo = [np.log(0.1), np.log(1e-3)] + ([0.05] if fit_t else []) + \
         [np.log(1e-5)] + [t - 300 for t in t0g]
    hi = [np.log(10.0), np.log(1e2)] + ([1.0] if fit_t else []) + \
         [np.log(1.0)] + [t + 300 for t in t0g]
    best = None
    for ssr0, x0 in scored[:1]:
        # ponytail: diff_step=1e-3 + screened start — least_squares over
        # solve_ivp residuals stalls at x0 with the default step (repo gotcha);
        # single polished start from the best of 8 screens, add starts if flat
        r = least_squares(residuals, np.array(x0), args=(data, fit_t),
                          bounds=(lo, hi), diff_step=1e-3, max_nfev=120,
                          xtol=1e-6, ftol=1e-6, verbose=2)
        print(f"    start SSR={ssr0:.2f} -> final SSR={2*r.cost:.4f} "
              f"({r.nfev} evals)", flush=True)
        if best is None or r.cost < best.cost:
            best = r
    x = best.x
    ns, bP = np.exp(x[0]), np.exp(x[1])
    if fit_t:
        tt, k, t0s = x[2], np.exp(x[3]), x[4:]
    else:
        tt, k, t0s = 1.0, np.exp(x[2]), x[3:]
    n = len(best.fun)
    rss = float(np.sum(best.fun ** 2))
    kpar = len(x)
    # Jacobian-based 1-sigma (linearised, log-space where applicable)
    try:
        J = best.jac
        cov = np.linalg.inv(J.T @ J) * rss / max(n - kpar, 1)
        sig = np.sqrt(np.abs(np.diag(cov)))
    except np.linalg.LinAlgError:
        sig = np.full(kpar, np.nan)
    return {"ns": ns, "bP": bP, "t": tt, "k": k, "t0s": np.array(t0s),
            "rss": rss, "n": n, "kpar": kpar, "aicc": aicc(rss, n, kpar),
            "sig": sig, "x": x}


def stage_fit():
    print("\n=== FIT: global isothermal Toth + LDF k across runs 3/4/5/6/8 ===")
    print("  FLAG: eps placeholder, D_L correlation, T=298 K assumed —"
          " fitted values conditional on these")
    data = prep_fit_data()
    for name in RUNS:
        d = data[name]
        u, L, alpha_b = run_conditions(name)
        print(f"  {name}: c_f={d['plateau']-d['baseline']:8.0f} ppm "
              f"({d['cf']:.3f} mol/m3)  u={u*100:.2f} cm/s  L={L*100:.1f} cm  "
              f"rho_b={alpha_b:.0f} kg/m3  t0~{d['t0_guess']:.0f} s")

    toth = fit_model(data, fit_t=True, label="Toth (ns, bP, t, k)")
    lang = fit_model(data, fit_t=False, label="Langmuir (ns, bP, k)")

    print("\n  fitted parameters (1-sigma in log-space for ns,bP,k):")
    for label, m in (("Toth", toth), ("Langmuir", lang)):
        print(f"    {label:9s} n_s={m['ns']:.3f} mol/kg  b={m['bP']:.4g} kPa^-1  "
              f"t={m['t']:.3f}  k={m['k']:.3e} s^-1  "
              f"RSS={m['rss']:.4f}  AICc={m['aicc']:.1f}")
    d_aicc = toth["aicc"] - lang["aicc"]
    sig_t = toth["sig"][2] if len(toth["sig"]) > 2 else np.nan
    toth_wins = d_aicc < -2 and (toth["t"] + 2 * sig_t) < 1.0
    verdict = "Toth" if toth_wins else "Langmuir"
    print(f"  ΔAICc(Toth−Langmuir) = {d_aicc:+.1f}; fitted t = {toth['t']:.3f}"
          f" ± {sig_t:.3f}")
    print(f"  VERDICT: retain {verdict} "
          f"({'AICc favors Toth and t<1 resolved' if toth_wins else 'Toth not justified: keep the simpler model'})")
    best = toth if toth_wins else lang

    # per-run diagnostics with the retained model
    print("\n  per-run diagnostics (retained model):")
    curves = model_curves((best["ns"], best["bP"], best["t"]), best["k"], data,
                          N=240, rtol=1e-6, full_span=True)
    fig, axes = plt.subplots(2, 3, figsize=(14, 8))
    for ax, (name, t0) in zip(axes.flat, zip(RUNS, best["t0s"])):
        d = data[name]
        u, L, alpha_b = run_conditions(name)
        cf = d["cf"]
        qf = float(toth_q(np.array([cf]), best["ns"], best["bP"], best["t"])[0])
        t_st = L * (EPS * cf + alpha_b * qf) / (u * cf)
        tg, cg = curves[name]
        # measured first moment (Cor. B.1 cross-check), on despiked full data
        tm = d["t"] - t0
        sel = tm >= 0
        mom = np.trapezoid(np.clip(1 - d["y_norm"][sel], 0, None), tm[sel])
        tbt = np.interp(0.05, cg, tg)
        t50 = np.interp(0.50, cg, tg)
        te = np.interp(0.95, cg, tg)
        print(f"    {name}: q*(c_f)={qf:.3f} mol/kg  t_st={t_st:6.0f} s  "
              f"measured moment={mom:6.0f} s ({mom/t_st*100:5.1f} % of t_st)  "
              f"model t_BT={tbt:5.0f} t50={t50:5.0f} t_E={te:5.0f} s")
        ax.plot(tm[sel] / 60, d["y_norm"][sel], ".", ms=2, alpha=0.5,
                label="measured")
        ax.plot(tg / 60, cg, "r-", lw=1.5, label="mechanistic fit")
        for tv, lab in ((tbt, "t_BT"), (t50, "t50"), (te, "t_E")):
            ax.axvline(tv / 60, color="gray", ls=":", lw=0.7)
        ax.set_title(f"{name}  (c_f={d['plateau']-d['baseline']:.0f} ppm)")
        ax.set_xlabel("t − t0 [min]"); ax.set_ylabel("c/c_f")
        ax.legend(fontsize=8)
    axes.flat[-1].axis("off")
    axes.flat[-1].text(0.05, 0.5,
        f"Global {verdict} fit\n"
        f"n_s = {best['ns']:.3f} mol/kg\nb = {best['bP']:.4g} kPa$^{{-1}}$\n"
        f"t = {best['t']:.3f}\nk = {best['k']:.3e} s$^{{-1}}$\n"
        f"AICc: Toth {toth['aicc']:.1f} / Langmuir {lang['aicc']:.1f}\n"
        f"eps = {EPS} (placeholder, flagged)", fontsize=11, va="center")
    fig.suptitle("F5 — measured breakthrough vs global mechanistic fit "
                 "(runs 3/4/5/6/8)")
    fig.tight_layout()
    fig.savefig(OUT_DIR / "F5_run_overlays.png", dpi=300); plt.close(fig)

    # isotherm figure
    p = np.linspace(0, 20, 400)  # kPa
    c_from_p = p * 1e3 / (R_GAS * T_AMB)
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot(p, toth_q(c_from_p, toth["ns"], toth["bP"], toth["t"]),
            label=f"Toth fit (t={toth['t']:.2f})")
    ax.plot(p, toth_q(c_from_p, lang["ns"], lang["bP"], 1.0), "--",
            label="Langmuir fit")
    # measured q_dyn reference points — NON-equilibrium, reference only
    qdyn = {"run 3": 0.555, "run 4": 0.810, "run 5": 0.552,
            "run 6": 0.885, "run 8": 0.787}
    for name in RUNS:
        d = parse_run(name)
        pco2 = (d["plateau"] - d["baseline"]) * 1e-6 * P_TOT / 1e3
        ax.plot(pco2, qdyn[name], "kx")
        ax.annotate(name, (pco2, qdyn[name]), fontsize=7,
                    textcoords="offset points", xytext=(4, 4))
    ax.plot([], [], "kx", label="measured q_dyn (dynamic, NOT equilibrium)")
    ax.set_xlabel("p_CO2 [kPa]"); ax.set_ylabel("q* [mol/kg]")
    ax.set_title("F6 — fitted isothermal isotherms at T_amb (flagged: single-T fit)")
    ax.legend(); fig.tight_layout()
    fig.savefig(OUT_DIR / "F6_isotherm.png", dpi=300); plt.close(fig)

    # grid-convergence guard on the fit-resolution choice
    name = "run 5"
    u, L, alpha_b = run_conditions(name)
    cf = data[name]["cf"]
    qstar = lambda c: toth_q(c, best["ns"], best["bP"], best["t"])
    t_end = float(data[name]["t_cap"])
    tbts = {}
    for N in (96, 192, 384):
        tg = np.linspace(0, t_end, 300)
        sol = simulate(N, L, u, d_axial(u), best["k"], alpha_b, cf, qstar,
                       t_end, t_eval=tg, variable_u=True)
        tbts[N] = np.interp(0.5, sol.y[N - 1, :] / cf, tg)
    dev = abs(tbts[96] / tbts[384] - 1)
    print(f"\n  grid check (run 5 t50): N96={tbts[96]:.0f} s  "
          f"N192={tbts[192]:.0f} s  N384={tbts[384]:.0f} s  "
          f"(N96 vs N384: {dev*100:.2f} %)")
    if dev > 0.01:
        print("  WARNING: fit-resolution t50 not grid-converged below 1 %")
    return best


# ---------------------------------------------------------------------------
def main(argv):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    stages = [a.lower() for a in argv] or ["v1", "fit", "v2", "v3", "v4"]
    print("Self-contained mechanistic solver — flagged placeholders:")
    for nm, val, why in FLAGS:
        print(f"  FLAG {nm} = {val}  ({why})")

    best = None
    # default isotherm for v2/v3/v4 if fit not run: illustrative, FLAGGED
    iso_default = (2.5, 0.4, 0.5)
    for st in stages:
        if st == "v1":
            stage_v1()
        elif st == "fit":
            best = stage_fit()
        elif st in ("v2", "v3", "v4"):
            if best is not None:
                iso = (best["ns"], best["bP"], best["t"])
            else:
                iso = iso_default
                print(f"\n  (no fit stage run — {st} uses ILLUSTRATIVE isotherm "
                      f"ns={iso[0]}, bP={iso[1]} kPa^-1, t={iso[2]}: flagged)")
            {"v2": stage_v2, "v3": stage_v3, "v4": stage_v4}[st](iso)
        else:
            print(f"unknown stage '{st}' (valid: v1 v2 v3 v4 fit)")
    print("\nAll requested stages complete. Figures in", OUT_DIR)


if __name__ == "__main__":
    main(sys.argv[1:])

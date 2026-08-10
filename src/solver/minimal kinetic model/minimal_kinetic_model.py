"""Minimal kinetic model — isothermal 1-D plug flow + LDF + Langmuir (A1–A7).

Derivation source: src/docs/mechanistic_model_report.md, section "Minimal Kinetic
Model for CO2 Adsorption with Amine Sorbents in Dry Condition" — assumptions
A1–A7 and Eqs (1)–(5). Numerics follow the Danckwerts finite-volume
Method-of-Lines scheme (b) of src/docs/mechanistic-model.md Part E (inlet face
flux F_{-1/2} = u*c_f exactly; upwind convection; the discrete inventory identity
telescopes). Fully self-contained: references ONLY the measured data in
``src/solver/data/new runs/`` (runs 3/4/5/6/8). No project imports.

Model (report Eqs (1)–(5); isothermal, so b is a constant):
    eps*dc/dt = -u_s*dc/dz - rho_b*dq/dt          (1)  [FV form, D_L = 0 per A1]
    dq/dt     = k*(q_e - q)                        (2)
    q_e       = qm*b*P / (1 + b*P),  P = c*R*T     (3),(4)
    b(T)      = b0*exp(-dH/(R*T))                  (5)  [NOT exercised — see below]

Global fit of (qm, b, k) across all five runs; b and k are FITTED, not
literature values (report Table 1 b is a deliberate unknown).

Verification: Rankine–Hugoniot isothermal equilibrium shock speed
    v_RH = u_s*c_f / (eps*c_f + rho_b*q*(c_f))          [doc D.3]
against the tracked half-height front in the large-k limit (±10 %).

Run from repo root:  python "src/solver/minimal kinetic model/minimal_kinetic_model.py"
Figures -> src/img/generated/minimal_kinetic/
"""

from __future__ import annotations

import csv
import os
from dataclasses import dataclass
from datetime import datetime

import sys

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import least_squares

# This script sits one level below src/solver/, so unlike its siblings it has to
# put src/solver on sys.path itself before the shared figure helper resolves.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from breakthrough_fit.axes_origin import snap_origin  # noqa: E402

# ---------------------------------------------------------------- constants
R_GAS = 8.314          # J/(mol K)
D_COL_M = 0.0085       # column i.d. [m]  (1-D axial model, A3: no radial gradients)
T_K = 298.0            # operating temperature [K]  (isothermal, A2)
P_PA = 101_325.0       # operating pressure [Pa]    (A5: negligible pressure drop)
DATA_DIR = os.path.join("src", "solver", "data", "new runs")
FIGDIR = os.path.join("src", "img", "generated", "minimal_kinetic")
N_CELLS = 100
RHO_P_PLACEHOLDER = 800.0  # kg/m3 — OPEN ITEM (owner: lab / Stampi-Bombelli);
#                            eps derived from it is NOT physical, floored at 0.30.
DT_FMT = "%m/%d/%y %H:%M:%S.%f"

# Measured basis: the five bench runs ONLY (flow lpm / sorbent mass g / bed cm).
RUN_META = {
    "run 3": dict(Q_lpm=0.15, m_g=8.0076, L_bed_cm=21.0),
    "run 4": dict(Q_lpm=0.05, m_g=8.0000, L_bed_cm=21.3),
    "run 5": dict(Q_lpm=0.10, m_g=8.0000, L_bed_cm=21.2),
    "run 6": dict(Q_lpm=0.15, m_g=8.0000, L_bed_cm=21.5),
    "run 8": dict(Q_lpm=0.10, m_g=8.0000, L_bed_cm=21.5),
}


# ---------------------------------------------------------------- data ingest
def parse_run_csv(path):
    """datetime col 0, ppm in last non-empty col; header row optional.

    Mirrors the pipeline's Format-C conventions so C0 matches the audited
    values: baseline = median of first 10 pts, C0 = 92nd percentile,
    t=0 = first pair of consecutive points above baseline + 2 % of span.
    """
    times, raw = [], []
    with open(path, newline="", encoding="utf-8", errors="replace") as fh:
        for row in csv.reader(fh):
            parts = [p.strip().strip('"') for p in row if p.strip()]
            if len(parts) < 2:
                continue
            try:
                times.append(datetime.strptime(parts[0], DT_FMT))
                raw.append(float(parts[-1]))
            except ValueError:  # header / junk row
                continue
    if not times:
        raise ValueError(f"No parseable rows in {path}")
    conc = np.asarray(raw, float)
    baseline = float(np.median(conc[: min(10, len(conc))]))
    c0_ppm = float(np.percentile(conc, 92))
    thresh = baseline + 0.02 * (c0_ppm - baseline)
    t0_idx = 0
    for i in range(len(conc) - 1):
        if conc[i] > thresh and conc[i + 1] > thresh:
            t0_idx = max(0, i - 1)
            break
    t = np.array([(x - times[t0_idx]).total_seconds() for x in times])
    c_c0 = np.clip((conc - baseline) / max(c0_ppm - baseline, 1.0), 0.0, 1.05)
    # despike: interpolate single-point jumps > 0.15 that return to neighbourhood
    d = np.abs(np.diff(c_c0))
    for i in np.where(d > 0.15)[0] + 1:
        if 0 < i < c_c0.size - 1 and abs(c_c0[i + 1] - c_c0[i - 1]) < 0.15:
            c_c0[i] = 0.5 * (c_c0[i - 1] + c_c0[i + 1])
    keep = t >= 0.0  # IC c = q = 0 at feed-step onset
    return t[keep], c_c0[keep], c0_ppm


def ppm_to_mol_m3(ppm):
    """Let the gas phase be ideal (A4). Report Eq (4), P = cRT, applied to the
    CO2 partial pressure y*P gives the molar concentration c = y*P/(R*T)."""
    return ppm * 1e-6 * P_PA / (R_GAS * T_K)


@dataclass
class Bed:
    L: float      # m
    eps: float    # bed voidage (placeholder-derived, see RHO_P_PLACEHOLDER)
    u: float      # m/s superficial
    rho_b: float  # kg/m3 bulk density
    cf: float     # mol/m3 feed
    T: float = T_K


def load_run(run_id):
    meta = RUN_META[run_id]
    t, c_c0, c0_ppm = parse_run_csv(os.path.join(DATA_DIR, f"{run_id}.csv"))
    A_c = np.pi * (D_COL_M / 2.0) ** 2
    L = meta["L_bed_cm"] * 1e-2
    u = meta["Q_lpm"] * 1e-3 / 60.0 / A_c
    rho_b = meta["m_g"] * 1e-3 / (A_c * L)
    eps = max(1.0 - rho_b / RHO_P_PLACEHOLDER, 0.3)
    cf = ppm_to_mol_m3(c0_ppm)
    return Bed(L=L, eps=eps, u=u, rho_b=rho_b, cf=cf), t, c_c0 * cf, c0_ppm


# ---------------------------------------------------------------- model core
def q_eq(c, qm, b, T=T_K):
    """Let the surface carry identical elementary sites, each hosting one adsorbed
    molecule. Report Eq (3), Langmuir on the CO2 partial pressure:
        q_e = qm*b*P / (1 + b*P),   with P = cRT from report Eq (4).
    Only CO2 adsorbs (A6); the carrier is inert.
    """
    P = np.maximum(c, 0.0) * R_GAS * T
    return qm * b * P / (1.0 + b * P)


def rhs(t, y, bed, qm, b, k, N, dz):
    """Report Eqs (1)+(2) in finite-volume form; scheme (b) of doc Part E.

    Let there be a control volume [z, z+dz] of cross-section A: gas occupies
    eps*A*dz, sorbent mass is rho_b*A*dz. Accumulation = in - out - sink gives
    report Eq (1), eps*dc/dt = -u_s*dc/dz - rho_b*dq/dt, with D_L = 0 because A1
    puts plug flow at constant u_s and no axial dispersion. The sink is the LDF
    closure, report Eq (2), dq/dt = k(q_e - q) (A7): a single first-order
    relaxation lumping film + macropore + micropore resistances into one k.

    Interleaved y = [c0,q0,c1,q1,...]; face fluxes F[0..N]:
    F[0] = u*cf is the Danckwerts inlet flux EXACTLY (not an approximated BC),
    upwind interior faces, zero-gradient outlet. Summing telescopes to the
    discrete inventory identity d/dt[dz*sum(eps*c+rho_b*q)] = u*cf - u*c_out.
    """
    c = y[0::2]
    q = y[1::2]
    dq = k * (q_eq(c, qm, b, bed.T) - q)
    F = np.empty(N + 1)
    F[0] = bed.u * bed.cf
    F[1:] = bed.u * c          # upwind: face value = upstream cell
    dc = ((F[:-1] - F[1:]) / dz - bed.rho_b * dq) / bed.eps
    out = np.empty_like(y)
    out[0::2] = dc
    out[1::2] = dq
    return out


def solve_bed(bed, qm, b, k, t_eval, N=N_CELLS):
    dz = bed.L / N
    sol = solve_ivp(rhs, (0.0, t_eval[-1]), np.zeros(2 * N), t_eval=t_eval,
                    args=(bed, qm, b, k, N, dz), method="LSODA",
                    rtol=1e-6, atol=1e-9 * max(bed.cf, 1.0), lband=2, uband=2)
    assert sol.success, sol.message
    return sol


def solve_outlet(bed, qm, b, k, t_eval, N=N_CELLS):
    return solve_bed(bed, qm, b, k, t_eval, N).y[2 * (N - 1)]


# ---------------------------------------------------------------- global fit
def global_residual(x, runs):
    qm, b, k = np.exp(x)
    return np.concatenate([
        (solve_outlet(bed, qm, b, k, t) - c_meas) / bed.cf
        for bed, t, c_meas, _ in runs])


# ------------------------------------------------- Rankine–Hugoniot check
def verify_rankine_hugoniot(bed, qm, b, ax=None):
    """Equilibrium-limit shock: track c = cf/2 front, compare to v_RH.

    Let k -> inf so report Eq (2) collapses to local equilibrium q = q_e(c)
    pointwise. Report Eq (1) then becomes a scalar conservation law in
    m = eps*c + rho_b*q_e(c) with flux u*c, whose jump from the clean bed
    (m = 0) to the fed state (m = m_f) travels at the Rankine-Hugoniot speed

        v_RH = [F(m_f) - F(0)] / (m_f - 0) = u*cf / (eps*cf + rho_b*q_e(cf))

    (src/docs/mechanistic-model.md D.3; not covered by the report). Equivalently
    v_RH = L / t_st with t_st the stoichiometric time below. q_e is concave, so
    this shock is the entropy solution and the front must move at v_RH.
    """
    k_eq = 2.0  # ponytail: fixed large k, equilibrium limit; wave width u/(eps*k) ~ 0.06 m < L
    qf = q_eq(bed.cf, qm, b)
    # Stoichiometric time: total capacity L*(eps*cf + rho_b*qf) per unit area fed at u*cf.
    t_st = bed.L * (bed.eps * bed.cf + bed.rho_b * qf) / (bed.u * bed.cf)
    v_rh = bed.L / t_st
    N = 800
    t_eval = np.linspace(0.0, 1.6 * t_st, 900)
    sol = solve_bed(bed, qm, b, k_eq, t_eval, N)
    c = sol.y[0::2]
    dz = bed.L / N
    zc = (np.arange(N) + 0.5) * dz
    ts = np.linspace(0.35 * t_st, 0.85 * t_st, 12)
    zs = []
    for tt in ts:
        prof = c[:, np.argmin(np.abs(t_eval - tt))] / bed.cf
        i = np.where(prof <= 0.5)[0][0]
        zs.append(np.interp(0.5, [prof[i], prof[i - 1]], [zc[i], zc[i - 1]]))
    v_num = np.polyfit(ts, zs, 1)[0]
    err = abs(v_num - v_rh) / v_rh
    if ax is not None:
        a0, a1 = ax
        for tt in np.linspace(0.2, 1.0, 5) * t_st:
            j = np.argmin(np.abs(t_eval - tt))
            a0.plot(zc * 100, c[:, j] / bed.cf, lw=1.2, label=f"t = {tt:.0f} s")
        for tt in ts:
            a0.axvline(v_rh * tt * 100, color="0.85", lw=0.6, zorder=0)
        a0.set(xlabel="z [cm]", ylabel="c/c_f",
               title="equilibrium shock vs v_RH prediction (grey)")
        a0.legend(fontsize=7)
        a1.plot(t_eval / t_st, c[N - 1] / bed.cf, "b-")
        a1.axvline(1.0, color="k", ls=":", label="t_st")
        a1.set(xlabel="t/t_st", ylabel="c(L,t)/c_f", title="outlet breakthrough")
        a1.legend()
    return v_rh, v_num, err, t_st


# ---------------------------------------------------------------- main
def main():
    os.makedirs(FIGDIR, exist_ok=True)
    run_ids = sorted(RUN_META)
    runs = [load_run(r) for r in run_ids]

    print("=" * 72)
    print("Minimal kinetic model — measured basis: runs 3/4/5/6/8 only")
    for rid, (bed, t, c_meas, c0_ppm) in zip(run_ids, runs):
        print(f"  {rid}: C0={c0_ppm:8.0f} ppm  u_s={bed.u*100:.3f} cm/s  "
              f"L={bed.L*100:.1f} cm  rho_b={bed.rho_b:.0f} kg/m3  "
              f"eps={bed.eps:.2f} (placeholder rho_p={RHO_P_PLACEHOLDER:.0f})")

    # Report Eq (5), the van't Hoff b(T) = b0*exp(-dH/(R*T)), is NOT exercised:
    # every run sits at one ambient T (A2), so only the lumped b(T_K) is
    # identifiable. The fitted b below is b(298 K), NOT b0 — and report Table 1
    # lists b as a deliberate unknown, so there is nothing to compare it against.
    #
    # diff_step >> solver rtol: default FD step (~1e-8) sits below the LSODA
    # integration noise floor, giving a garbage Jacobian and a stalled fit.
    # The cost valley along the qm*b ridge is shallow — multi-start, keep best.
    starts = [(1.0, 0.5 / (R_GAS * T_K), 5e-3),   # qm mol/kg, b 1/Pa, k 1/s
              (3.0, 2e-5, 1e-3),
              (0.5, 4e-4, 1e-2)]
    fit = min((least_squares(global_residual, np.log(x0), args=(runs,),
                             method="trf", diff_step=1e-3, xtol=1e-8, ftol=1e-8)
               for x0 in starts), key=lambda f: f.cost)
    qm, b, k = np.exp(fit.x)
    print("-" * 72)
    print("Global fit (one qm, b, k across all runs) — FITTED, not literature:")
    print(f"  qm = {qm:.4f} mol/kg")
    print(f"  b  = {b:.4e} 1/Pa  ({b*R_GAS*T_K:.4f} m3/mol at {T_K:.0f} K)")
    print(f"  k  = {k:.4e} 1/s")
    print(f"  cost = {fit.cost:.4e}   nfev = {fit.nfev}")

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    # Fig 1 — fitted model vs measured breakthrough, all runs
    fg, ax = plt.subplots(figsize=(7, 4.5))
    print("-" * 72)
    for rid, (bed, t, c_meas, _) in zip(run_ids, runs):
        c_model = solve_outlet(bed, qm, b, k, t)
        rmse = np.sqrt(np.mean((c_model - c_meas) ** 2)) / bed.cf
        print(f"  {rid}: cf={bed.cf:.2f} mol/m3  RMSE(C/C0) = {rmse:.4f}")
        ln, = ax.plot(t / 60, c_meas / bed.cf, "o", ms=2, alpha=0.35)
        ax.plot(t / 60, c_model / bed.cf, "-", color=ln.get_color(), label=rid)
    ax.set(xlabel="t [min]", ylabel="C/C0",
           title="Minimal kinetic model (global qm,b,k) vs measured")
    ax.legend(fontsize=8)
    snap_origin(fg, label="minimal_kinetic_fit")
    fg.tight_layout()
    fg.savefig(os.path.join(FIGDIR, "minimal_kinetic_fit.png"), dpi=150)
    plt.close(fg)

    # Fig 2 + R-H verification on run 5 geometry (mid-flow, ~10 % CO2)
    fg, ax = plt.subplots(1, 2, figsize=(10, 3.8))
    bed = runs[run_ids.index("run 5")][0]
    v_rh, v_num, err, t_st = verify_rankine_hugoniot(bed, qm, b, ax)
    fg.suptitle("Rankine–Hugoniot check, run 5 geometry (fitted isotherm, k -> eq.)",
                fontsize=10)
    snap_origin(fg, label="minimal_kinetic_rh")
    fg.tight_layout()
    fg.savefig(os.path.join(FIGDIR, "minimal_kinetic_rh.png"), dpi=150)
    plt.close(fg)

    print("-" * 72)
    print("Rankine–Hugoniot isothermal equilibrium shock (run 5 geometry):")
    print(f"  v_RH  = {v_rh:.4e} m/s   (t_st = {t_st:.0f} s)")
    print(f"  v_num = {v_num:.4e} m/s")
    print(f"  error = {err*100:.3f} %   {'PASS (<10%)' if err < 0.10 else 'FAIL (>=10%)'}")
    assert err < 0.10, "R-H front speed outside +/-10 %"
    print("=" * 72)
    print(f"Figures -> {FIGDIR}/minimal_kinetic_fit.png, minimal_kinetic_rh.png")


if __name__ == "__main__":
    main()

"""
psi_quadrature_verify.py — Danilov et al. (2019) psi-quadrature implemented as the
constant-pattern / travelling-wave limit of the full mechanistic model
(src/docs/mechanistic-model.md, Part D.3).

Danilov's construction (danilov2019.txt): the LDF driving force psi = q* - q obeys
d(psi)/dt = -beta*k_f*psi (their Appendix B, Eq. B.5-B.8); a *symmetric* front ansatz
around the stoichiometric time (their Eq. 1 / B.9-B.11) is then marched through the
coupled mass/heat balances by the z-quadratures of Eqs. 2-8, closed by the Sips
isotherm Eq. 10.  MM D.3 solves the same limiting problem the other way round: it
*derives* the wave shape from an ODE with a proven closed form in the Langmuir
sub-case (MM D.8).  This script turns that comparison into numbers and pictures.

Runs (select on argv, default all):
  r1  Danilov Fig.-1 reproduction (Table 2, Moeller 2017 CO2/CH4/He on Shirasagi
      MSC CT, Sips), Pe_G = 10 and Pe_G -> inf (plug flow).  OCR-reconstruction
      sanity check, qualitative visual verdict only.
  r2  Isothermal Langmuir (b*c_f = 2.045, reused from mechanistic_verify.test3_wave):
      three-way outlet-trace + 0.65*t_st profile comparison psi-quadrature vs
      (a) MM D.8 exact closed form, (b) FV-MOL (solve_iso).  RMS deviations reported
      as numbers, no pass/fail threshold (open question, Part 2).  Includes the
      Gate-B-style front-speed / first-moment check and the wall-clock table.
  r3  Non-isothermal Toth demo at mechanistic_verify.test5_full's illustrative
      parameters; overlay against MM V5 (adiabatic + wall-coupled).  Danilov's
      dilute-feed validity (danilov2019.txt:473-481) is exceeded here and the
      printed output says so explicitly.

--------------------------------------------------------------------------------
Section-3 errata (of the accompanying prompt document), restated by reference.
Each is anchored to a code line by an inline [S3-E#] tag — grep for the tag.
  E1  Printed Eq. B.11 ("0.5 + 0.5(1 - exp(-k_f*theta))") must read
      0.5*exp(-beta*k_f*theta): re-derivation from the control volume (the flux
      quadrature Eq. 2 diverges and the supply/consumption balance fails with the
      printed sigmoid; the tent form reproduces the exact LDF decay B.8 behind the
      front).  -> [S3-E1]
  E2  The printed corrected time theta = (t - z/u_f) - t_s double-counts the bed
      transit: with u_f = L/t_s it puts the outlet mid-front at 2*t_s.  The
      control-volume-consistent form is theta = t - z/u_f with t_s = L/u_f
      built in (outlet mid-front at t_s, theta=0 locus travels at u_f).  -> [S3-E2]
  E3  Energy bookkeeping: A.12 carries eps_b*alpha_v on the interphase source while
      A.14 omits eps_b — inconsistent by a factor eps_b.  Re-derived so that the
      product (heat into the gas per unit z) is alpha_b*(-dH)*k*psi, in which
      alpha_v cancels identically; alpha_v only sets the T_S - T_G split.  -> [S3-E3]
  E4  "(1-eps_b)*rho_b" with rho_b = 588.5 kg/m3 (Table 2 *bulk* density) would
      double-count the solid fraction; the sorbent mass per bed volume is
      alpha_b = rho_bulk (= (1-eps_total)*rho_S, MM notation alpha_b).  -> [S3-E4]
  E5  t_s and u_f are not free/fitted inputs: they are fixed by MM's closed forms
      t_st (Cor. B.1 / D.4) and v_RH (D.3).  Don't refit what MM derives.  -> [S3-E5]

Section-5 verification findings, restated by reference (tags [S5-#]):
  F1  t_s = (eps*L/u)*(1 + Lambda) = t_st identity (Lambda = alpha_b*q_f/(eps*c_f)):
      Danilov's front time is set from MM's closed form, never fitted.  -> [S5-1]
  F2  gamma_q ~ 1 and beta ~ 1 are validated only for the Langmuir/Table-2 regime;
      they are explicit keyword defaults here, not silent hard-codes.  -> [S5-2]
  F3  gamma_shape (Eq.-1 front-shape exponent), gamma_q (isotherm-shape coefficient
      in Eq. 2/A.8) and beta_psi (psi-ODE decay coefficient, B.5) are three distinct
      named quantities that the paper's final form conflates.  -> [S5-3]
  F4  No printed sign in Eqs. A.1-A.8 / B.1-B.5 is trusted; every flux/source sign
      here is re-derived from the control volume (see E1-E3 anchors).  -> [S5-4]
  F5  The Damkohler number is normalised as Da = k*L/u throughout; Danilov-style
      N = k*eps*L/u is converted at the Fig.-1 boundary only.  -> [S5-5]

Imports Bed / Langmuir / Toth / solve_iso / solve_full from mechanistic_verify.py
(single parameter source of truth; that file is not modified).
Figures -> src/img/generated/psi_quadrature/.   Run from repo root:
    python src/solver/psi_quadrature_verify.py [r1 r2 r3]
"""

from __future__ import annotations

import os
import sys
import time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mechanistic_verify import (  # noqa: E402  (shared source of truth, task 1)
    Bed, Langmuir, Toth, solve_iso, solve_full, trapz, R_GAS,
    # `crossing_time` was renamed to `crossing` in 42b2ad7 (2026-08-03) without
    # updating this caller, which has been unrunnable since. Same signature and
    # same rising=True default, so this is an alias, not a substitution; the six
    # call sites below are untouched. Owner of the proper rename: author.
    crossing as crossing_time)
from breakthrough_fit.axes_origin import snap_origin  # noqa: E402

FIGDIR = os.path.join("src", "img", "generated", "psi_quadrature")

# ============================================================================
# Core: single-component psi-quadrature in MM's concentration basis
# ============================================================================


def _recover_backward(g, a, dz):
    """Recover x(z) from x' = a*(x - g(z)) by the exact integrating factor,
    marched BACKWARD from the zero-gradient outlet x(L) = g(L).

    This replaces Danilov's printed Eq. 5/6 forward march from the inlet, which
    is the exponentially UNSTABLE direction: any error in the forcing (roundoff,
    or the psi-ansatz error itself) is amplified by e^{a*L} = e^{Pe}, and with the
    isotherm T-feedback it diverges already at Pe = 10 (verified numerically).
    Backward integration has multiplier e^{-a*dz} < 1 (unconditionally stable),
    imposes the physically correct outlet condition x'(L) = 0, and lets the
    Danckwerts inlet value x(0+) < x_in EMERGE instead of over-determining the
    inlet (their A.9 sets both F(0) = Ft*y_in and y_0 = y_in) — the same
    re-derive-don't-trust discipline as the sign errata.  [S5-4]

    g: (N+1, nt) forcing (the plug-flow target F/u resp. Q/Hflux).
    """
    x = np.empty_like(g)
    x[-1] = g[-1]
    fac = np.exp(-a * dz)
    for j in range(g.shape[0] - 2, -1, -1):
        gm = 0.5 * (g[j] + g[j + 1])
        x[j] = gm + (x[j + 1] - gm) * fac
    return x


def psi_quadrature(bed: Bed, iso, N: int, t_eval,
                   gamma_q: float = 1.0,       # [S5-2] Langmuir/Table-2 default, explicit
                   beta_psi: float = 1.0,      # [S5-2] idem
                   gamma_shape: float | None = None,   # [S5-3] distinct from beta_psi
                   thermal: bool = False,
                   T_feedback: bool = True,
                   inlet_foldback: bool = True,
                   alpha_v: float = 1.68e5):   # W m-3 K-1, Danilov Table 2 (split only, E3)
    """Danilov et al. (2019) Eqs. 1-8 for a single component, MM basis.

    State recovered at nodes z_j = j*dz (j = 0..N) for every t in t_eval; the
    construction is a pure z-quadrature at each time (no time integration), which
    is exactly why it is cheap — and exactly why it can only represent one
    travelling front (MM D.6).

    gamma_shape = leading-edge growth exponent of the Eq.-1 ansatz; beta_psi =
    trailing-edge decay from the psi-ODE (B.5-B.8).  The symmetric ansatz REQUIRES
    gamma_shape == beta_psi; keeping both named makes that assumption visible
    rather than silent.  [S5-3]
    """
    if gamma_shape is None:
        gamma_shape = beta_psi                       # symmetry assumption, visible [S5-3]
    t = np.asarray(t_eval, float)
    L, u, eps, k, cf = bed.L, bed.u, bed.eps, bed.k, bed.cf

    # --- front time & velocity from MM closed forms, never fitted  [S3-E5]
    qf = iso.q(cf, bed.T0)
    Lam = bed.alpha_b * qf / (eps * cf)              # capacity ratio Lambda
    t_st = (eps * L / u) * (1.0 + Lam)               # == L(eps cf + alpha_b qf)/(u cf) [S5-1]
    u_f = L / t_st                                   # == v_RH (MM D.3)              [S5-1]
    Da = k * L / u                                   # Da = kL/u normalisation       [S5-5]

    dz = L / N
    z = np.linspace(0.0, L, N + 1)

    # dispersion/conduction recovery exponents (MM flux basis: F = u c - eps DL c_z)
    a_c = u / (eps * bed.DL) if bed.DL > 0 else np.inf
    a_T = u * bed.rho_g * bed.cpg / bed.lam if bed.lam > 0 else np.inf
    Hflux = u * bed.rho_g * bed.cpg                  # gas volumetric heat flux coeff.

    nt = t.size
    q = np.zeros((N + 1, nt)); psi_all = np.zeros((N + 1, nt))
    F = np.empty((N + 1, nt)); Qh = np.empty((N + 1, nt))
    F[0] = u * cf                                    # Danckwerts flux F(0)=u*c_f (A.9),
    Qh[0] = Hflux * bed.Tf                           # exact — kept; the printed y_0=y_in
    #                                                  over-determination is NOT imposed:
    #                                                  see _recover_backward.  [S5-4]
    # --- inlet fold-back (this work, not Danilov). The symmetric ansatz truncates
    # the trailing (already-saturated) half of the tent at the inlet boundary at
    # early times, so a clean bed would leak up to half the feed at t=0.  The
    # truncated mass is folded back as an extra inlet sink S_miss(t) =
    # alpha_b*gamma_q*u_f*psi_ref_in*0.5*e^{-beta k t}/beta — exactly the LDF decay
    # of fresh sorbent at z=0 (psi(0,t) = q_f e^{-beta k t}; the ansatz supplies
    # only half of it), and it restores the Cor. B.1 first-moment stoichiometry.
    # Capped by the fresh-bed uptake bound alpha_b*k*L*psi_ref_in*e^{-beta k t}
    # (relevant only when the tent is wider than the bed, Da << 1).  [S3-E1]
    psi_ref_in = iso.q(np.full(nt, cf), np.full(nt, bed.T0))
    if inlet_foldback:
        S_miss = bed.alpha_b * gamma_q * u_f * psi_ref_in * 0.5 \
            * np.exp(-beta_psi * k * t) / beta_psi
        S_miss = np.minimum(S_miss, bed.alpha_b * k * L * psi_ref_in
                            * np.exp(-beta_psi * k * t))
    else:
        S_miss = np.zeros(nt)
    for j in range(1, N + 1):
        # corrected time: theta = t - z/u_f, t_s = L/u_f built in       [S3-E2]
        theta = t - z[j] / u_f
        # symmetric tent ansatz (Eq. 1 / B.9-B.11 re-derived):          [S3-E1]
        #   theta<=0 : 0.5*exp(+gamma_shape*k*theta)   (leading edge)
        #   theta> 0 : 0.5*exp(-beta_psi   *k*theta)   (LDF decay B.8)
        Om = np.where(theta <= 0.0,
                      0.5 * np.exp(np.minimum(gamma_shape * k * theta, 0.0)),
                      0.5 * np.exp(-beta_psi * k * theta))
        # reference driving force: B.12 states psi_ref is the MAXIMUM driving
        # force, i.e. q_eq at FEED conditions (minus q_ini = 0), not at the local
        # leaked concentration — evaluating Eq. 9 on the local cascade state
        # collapses the sink ahead of the front and leaks ~half the feed through
        # a clean bed (verified numerically).  Local T (plug-consistent, previous
        # node) is retained so the thermal feedback on capacity survives.  [S3-E1]
        Tref = Qh[j - 1] / Hflux if (thermal and T_feedback) else np.full(nt, bed.T0)
        psi_ref = iso.q(np.full(nt, cf), Tref)
        psi = Om * psi_ref                           # dimensional driving force
        psi_all[j] = psi
        c_prev = np.maximum(F[j - 1] / u, 0.0)       # local state, for Eq. 7 output only
        # flux quadrature (Eq. 2 / A.18); sorbent mass per bed volume = alpha_b,
        # NOT (1-eps)*rho_bulk                                          [S3-E4]
        F[j] = F[j - 1] - bed.alpha_b * gamma_q * k * psi * dz          # [S5-3] gamma_q here
        if j == 1:
            F[j] = F[j] - S_miss                     # fold-back sink at the inlet [S3-E1]
        F[j] = np.maximum(F[j], 0.0)
        # solid loading output (B.13): q = q_eq(local) - psi, clipped
        q[j] = np.maximum(iso.q(c_prev, Tref) - psi, 0.0)
        if thermal:
            # heat into the gas per unit z = alpha_b*(-dH)*k*psi — alpha_v cancels
            # between A.14 and A.16 once the eps_b bookkeeping is consistent [S3-E3]
            Qh[j] = Qh[j - 1] + bed.alpha_b * bed.dH * k * psi * dz     # Eq. 3 / A.19
            if j == 1:
                Qh[j] = Qh[j] + bed.dH * S_miss                          # fold-back heat
        else:
            Qh[j] = Qh[0]
    # field recovery (Eq. 5 / Eq. 6): plug relation if hyperbolic, otherwise the
    # stable backward integrating-factor march (see _recover_backward)  [S5-4]
    if bed.DL > 0:
        c = _recover_backward(F / u, a_c, dz)
    else:
        c = F / u                                    # their A.20 plug branch
    c = np.maximum(c, 0.0)
    if thermal and bed.lam > 0:
        TG = _recover_backward(Qh / Hflux, a_T, dz)
    else:
        TG = Qh / Hflux
    TS = TG + bed.alpha_b * bed.dH * k * psi_all / alpha_v              # Eq. 4+8 / A.15
    return dict(z=z, t=t, c=c, q=q, F=F, TG=TG, TS=TS,
                t_st=t_st, u_f=u_f, Da=Da, Lam=Lam, qf=qf)


# ============================================================================
# r1 — Danilov Fig. 1 reproduction (Table 2 binary Sips system)
# ============================================================================

# ---- Table 2 of danilov2019.txt (lines 2280-2380), reproduced verbatim -------
TABLE2 = {
    "system":       "CO2/CH4/He / Shirasagi MSC CT (Moeller et al. 2017)",
    "y_CO2":        0.05,
    "y_CH4":        0.15,
    "Ft [mol/s]":   1.89e-3,
    "T [K]":        293.0,
    "P [MPa]":      0.5,
    "eps_b":        0.34,
    "rho_b [kg/m3]": 588.5,
    "L [mm]":       200.0,
    "d_col [mm]":   30.0,
    "kf_CO2 [1/s]": 1.3e-2,
    "kf_CH4 [1/s]": 1.2e-4,
    "kf_He [1/s]":  0.0,
    "qmax_CO2":     "4.263*exp(0.8303*(1-T/293))            [mol/kg]",
    "b_CO2":        "1.013e-5*exp(21.5e3*(1/T-1/293)/R)     [1/Pa]",
    "t_CO2":        "0.7176 + 0.5077*(1-293/T)",
    "qmax_CH4":     "3.082*exp(1.4639*(1-T/293))            [mol/kg]",
    "b_CH4":        "2.42e-5*exp(9.6e3*(1/T-1/293)/R)       [1/Pa]",
    "t_CH4":        "0.7730 + 0.6792*(1-293/T)",
    "Pe_G":         10.0,
    "Pe_T":         10.0,
    "dH_CO2 [J/mol]": -21.5e3,
    "dH_CH4 [J/mol]": -9.6e3,
    "alpha_v [W/m3K]": 1.68e5,
    "Cp_S [J/kgK]": 880.0,
    "rho_S [kg/m3]": 1.2e3,
}


def _sips(T, species, pP):
    """Sips numerator term s = (b(T)*p_partial)^t(T) and qmax(T) (Eq. 10, Table 2)."""
    if species == "CO2":
        qm = 4.263 * np.exp(0.8303 * (1.0 - T / 293.0))
        b = 1.013e-5 * np.exp(21.5e3 * (1.0 / T - 1.0 / 293.0) / R_GAS)
        tt = 0.7176 + 0.5077 * (1.0 - 293.0 / T)
    else:  # CH4
        qm = 3.082 * np.exp(1.4639 * (1.0 - T / 293.0))
        b = 2.42e-5 * np.exp(9.6e3 * (1.0 / T - 1.0 / 293.0) / R_GAS)
        tt = 0.7730 + 0.6792 * (1.0 - 293.0 / T)
    s = np.power(np.maximum(b * pP, 0.0), tt)
    return qm, s


def qeq_sips(y_co2, y_ch4, T, P, species, competition=True):
    """Multicomponent Sips (Danilov Eq. 10).

    competition=False drops the *other* species from the denominator of the CO2
    site balance — the kinetically-frozen-CH4 reading (Danilov's own text: CH4
    'is nearly not adsorbed in dynamic conditions'; Da_CH4 = kL/u ~ 2e-3).
    """
    qm_c, s_c = _sips(T, "CO2", P * np.maximum(y_co2, 0.0))
    qm_m, s_m = _sips(T, "CH4", P * np.maximum(y_ch4, 0.0))
    if species == "CO2":
        den = 1.0 + s_c + (s_m if competition else 0.0)
        return qm_c * s_c / den
    den = 1.0 + s_c + s_m
    return qm_m * s_m / den


def run_fig1(fig=True, competition=False):
    """Reproduce Danilov Fig. 1 (CO2 breakthrough + gas T at outlet), Pe_G=10 & plug."""
    P = TABLE2["P [MPa]"] * 1e6
    T0 = TABLE2["T [K]"]
    rho_mol = P / (R_GAS * T0)                       # 205.3 mol/m3
    A = np.pi * (TABLE2["d_col [mm]"] / 2e3) ** 2
    Fa = TABLE2["Ft [mol/s]"] / A                    # 2.674 mol/m2/s (per bed area)
    u = Fa / rho_mol                                 # superficial, 0.01303 m/s
    eps_b = TABLE2["eps_b"]
    alpha_b = TABLE2["rho_b [kg/m3]"]                # bulk sorbent mass / bed volume [S3-E4]
    L = TABLE2["L [mm]"] / 1e3
    # gas mixture molar heat capacity (LITERATURE values, not in Table 2 — flagged):
    cp_mol = 0.80 * 20.79 + 0.15 * 35.69 + 0.05 * 37.13   # ~23.9 J/mol/K at 293 K
    Hflux = rho_mol * cp_mol * u
    PeG, PeT = TABLE2["Pe_G"], TABLE2["Pe_T"]
    alpha_v = TABLE2["alpha_v [W/m3K]"]

    species = ("CO2", "CH4")
    yf = {"CO2": TABLE2["y_CO2"], "CH4": TABLE2["y_CH4"]}
    kf = {"CO2": TABLE2["kf_CO2 [1/s]"], "CH4": TABLE2["kf_CH4 [1/s]"]}
    dH = {"CO2": -TABLE2["dH_CO2 [J/mol]"], "CH4": -TABLE2["dH_CH4 [J/mol]"]}  # (-dH)>0

    # per-component stoichiometric front time / velocity from the MM identity
    # t_s = (eps L/u)(1 + Lambda) = t_st  [S5-1][S3-E5]; NOT fitted to the figure.
    def front(sp, comp):
        qfs = qeq_sips(yf["CO2"], yf["CH4"], T0, P, sp, competition=comp)
        cfs = yf[sp] * rho_mol
        Lam = alpha_b * qfs / (eps_b * cfs)
        ts = (eps_b * L / u) * (1.0 + Lam)
        return qfs, ts, L / ts

    qf_c, ts_c, uf_c = front("CO2", competition)
    qf_c_comp, ts_c_comp, _ = front("CO2", True)     # printed for comparison
    qf_m, ts_m, uf_m = front("CH4", True)
    Da = {sp: kf[sp] * L / u for sp in species}      # Da = kL/u          [S5-5]
    N_dan = {sp: Da[sp] * eps_b for sp in species}   # Danilov-style N = k eps L/u,
    #                                                  converted here at the boundary [S5-5]

    N = 400
    dz = L / N
    z = np.linspace(0.0, L, N + 1)
    t = np.arange(0.0, 45.0 * 60.0, 5.0)
    nt = t.size
    out = {}
    for tag, disp in (("plug", False), ("Pe10", True)):
        F = {sp: np.full((N + 1, nt), Fa * yf[sp]) for sp in species}
        Qh = np.full((N + 1, nt), Hflux * T0)
        F_He = Fa * (1.0 - sum(yf.values()))         # inert carrier flux, constant
        ufv = {"CO2": uf_c, "CH4": uf_m}
        qf_feed = {"CO2": qf_c, "CH4": qf_m}
        # inlet fold-back per component (see psi_quadrature core)       [S3-E1]
        S_miss = {}
        for sp in species:
            sm = alpha_b * ufv[sp] * qf_feed[sp] * 0.5 * np.exp(-kf[sp] * t)
            S_miss[sp] = np.minimum(sm, alpha_b * kf[sp] * L * qf_feed[sp]
                                    * np.exp(-kf[sp] * t))
        for j in range(1, N + 1):
            # psi_ref = MAX driving force (their B.12): q_eq at FEED composition —
            # see the core for why the local-concentration reading of Eq. 9 fails
            # on a clean bed.  Capacity is evaluated at T0, NOT at the marched gas
            # temperature: the printed quasi-steady-solid energy shortcut makes the
            # entire downstream gas spuriously hot (+~40 K, right panel), and
            # feeding that into b(T) suppresses q_eq and leaks ~1/3 of the feed
            # through a clean bed (verified numerically).  In Danilov's own dilute
            # regime the measured excursion is ~6 K (capacity shift ~15%), so the
            # decoupling is consistent with their stated validity.  [S3-E1][S3-E3]
            Tp = np.full(nt, T0)
            dQ = np.zeros(nt)
            for sp in species:
                theta = t - z[j] / ufv[sp]           # [S3-E2]
                bk = kf[sp]                          # beta_psi = gamma_shape = 1 [S5-2]
                Om = np.where(theta <= 0.0,
                              0.5 * np.exp(np.minimum(bk * theta, 0.0)),
                              0.5 * np.exp(-bk * theta))                 # [S3-E1]
                psi_ref = qeq_sips(np.full(nt, yf["CO2"]), np.full(nt, yf["CH4"]),
                                   Tp, P, sp,
                                   competition=(competition if sp == "CO2" else True))
                psi = Om * psi_ref
                F[sp][j] = F[sp][j - 1] - alpha_b * kf[sp] * psi * dz    # Eq. 2, gamma_q=1
                if j == 1:
                    F[sp][j] = F[sp][j] - S_miss[sp]                     # fold-back [S3-E1]
                F[sp][j] = np.maximum(F[sp][j], 0.0)
                dQ += alpha_b * dH[sp] * kf[sp] * psi                    # [S3-E3]
                if j == 1:
                    dQ += dH[sp] * S_miss[sp] / dz                       # fold-back heat
            Qh[j] = Qh[j - 1] + dQ * dz                                  # Eq. 3
        Ftot = F["CO2"] + F["CH4"] + F_He
        if disp:
            # Eq. 5 / Eq. 6 recovered by the stable backward march (their forward
            # form diverges at Pe=10 with T-feedback — verified)         [S5-4]
            y_co2 = _recover_backward(F["CO2"] / (rho_mol * u), PeG / L, dz)
            TG = _recover_backward(Qh / Hflux, PeT / L, dz)
        else:
            y_co2 = F["CO2"] / np.maximum(Ftot, 1e-30)                   # A.20 plug
            TG = Qh / Hflux
        out[tag] = dict(y=np.clip(y_co2[N], 0.0, 1.0), T=TG[N])

    # energy-consistent rescale (this work, NOT Danilov): the quasi-steady-solid
    # shortcut (A.13-A.16) convects ALL adsorption heat with the gas; retaining bed
    # heat storage C_bed = rho_b*Cp_S moving with the front at u_f rescales the gas
    # excursion by Hflux/(Hflux + C_bed*u_f).                            [S3-E3]
    C_bed = TABLE2["rho_b [kg/m3]"] * TABLE2["Cp_S [J/kgK]"]
    scale = Hflux / (Hflux + C_bed * uf_c)
    T_corr = T0 + (out["Pe10"]["T"] - T0) * scale

    if fig:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fg, ax = plt.subplots(1, 2, figsize=(11, 4.0))
        tm = t / 60.0
        ax[0].plot(tm, out["plug"]["y"], "r-", lw=1.6, label="AADM plug flow")
        ax[0].plot(tm, out["Pe10"]["y"], "g:", lw=2.0, label="AADM Pe$_G$ = 10")
        ax[0].axhline(yf["CO2"], color="0.8", lw=0.6)
        ax[0].set(xlabel="t (min)", ylabel="y$^{CO_2}$", xlim=(0, 45), ylim=(0, 0.06),
                  title="Danilov Fig. 1 (left): CO$_2$ breakthrough")
        ax[0].legend(loc="lower right", fontsize=8)
        ax[1].plot(tm, out["plug"]["T"] - 273.15, "r-", lw=1.6, label="AADM plug flow")
        ax[1].plot(tm, out["Pe10"]["T"] - 273.15, "g:", lw=2.0, label="AADM Pe$_T$ = 10")
        ax[1].plot(tm, T_corr - 273.15, color="0.4", ls="-.", lw=1.2,
                   label="+ bed-storage rescale (this work; shape still wrong)")
        ax[1].axhline(26.1, color="b", ls="--", lw=0.8,
                      label="published AADM/exp. peak 26.1 $^\\circ$C")
        ax[1].set(xlabel="t (min)", ylabel="T ($^\\circ$C)", xlim=(0, 45),
                  title="Danilov Fig. 1 (right): outlet gas T")
        ax[1].legend(fontsize=7)
        snap_origin(fg, label="F1_danilov_fig1_reproduction")
        fg.tight_layout()
        fg.savefig(os.path.join(FIGDIR, "F1_danilov_fig1_reproduction.png"), dpi=150)
        plt.close(fg)

    y10 = out["Pe10"]["y"]
    t50 = crossing_time(t, y10 / yf["CO2"], 0.5)
    t10 = crossing_time(t, y10 / yf["CO2"], 0.1)
    t90 = crossing_time(t, y10 / yf["CO2"], 0.9)
    return dict(t=t, out=out, T_corr=T_corr, t50=t50, w1090=t90 - t10,
                ts_CO2=ts_c, ts_CO2_competitive=ts_c_comp, qf=qf_c, qf_comp=qf_c_comp,
                uf=uf_c, Da=Da, N_dan=N_dan, dT_peak=float(out["Pe10"]["T"].max() - T0),
                dT_peak_corr=float(T_corr.max() - T0), u=u, rho_mol=rho_mol)


# ============================================================================
# r2 — three-way isothermal Langmuir comparison + Gate-B check + wall clock
# ============================================================================


def d8_exact_wave(iso: Langmuir, cf, v_rh, k):
    """MM D.8 closed form: eta(w) with the 50%-point at eta=0 (no fitted params)."""
    w = np.linspace(1e-6, 1 - 1e-6, 4001)
    eta = -(v_rh / (k * iso.b * cf)) * (np.log(w) - (1 + iso.b * cf) * np.log1p(-w))
    eta -= eta[np.argmin(np.abs(w - 0.5))]
    return w, eta


def _z_half(zc, prof):
    """z where a monotone-decreasing front profile crosses 0.5."""
    idx = np.where(prof <= 0.5)[0]
    if len(idx) == 0 or idx[0] == 0:
        return np.nan
    i = idx[0]
    return float(np.interp(0.5, [prof[i], prof[i - 1]], [zc[i], zc[i - 1]]))


def run_langmuir(fig=True):
    """Tasks 4+5+8: psi-quadrature vs MM D.8 exact wave vs FV-MOL, bc_f = 2.045."""
    p = Bed(k=2e-2, DL=0.0)                          # == mechanistic_verify.test3_wave
    iso = Langmuir(qm=1.0, b=0.5)                    # b*c_f = 2.045 (asymmetry visible)
    qf = iso.q(p.cf)
    t_st = p.L * (p.eps * p.cf + p.alpha_b * qf) / (p.u * p.cf)
    v_rh = p.L / t_st
    N = 3000                                         # matched resolution (wall-clock)
    t_eval = np.linspace(0.0, 2.0 * t_st, 800)

    t0 = time.perf_counter()
    sol, dz = solve_iso(p, iso, N, t_eval, rtol=1e-8)
    wt_fv = time.perf_counter() - t0
    c_fv = sol.y[0::2]
    zc = (np.arange(N) + 0.5) * dz

    t0 = time.perf_counter()
    r = psi_quadrature(p, iso, N, t_eval)            # gamma_q=beta_psi=1 [S5-2]
    wt_psi = time.perf_counter() - t0

    # ---- profile snapshot at 0.65 t_st (same instant for all three) ----------
    jsnap = int(np.argmin(np.abs(t_eval - 0.65 * t_st)))
    prof_fv = c_fv[:, jsnap] / p.cf
    prof_ps = r["c"][:, jsnap][1:] / p.cf            # node j=1..N -> cell-ish grid
    zps = r["z"][1:]
    zh_fv, zh_ps = _z_half(zc, prof_fv), _z_half(zps, prof_ps)
    w_ex, eta_ex = d8_exact_wave(iso, p.cf, v_rh, p.k)

    def on_eta(zgrid, zh, prof, eta):
        return np.interp(eta, zgrid - zh, prof)      # profiles are functions of z - z50

    eta_cmp = np.linspace(-0.06, 0.06, 601)          # window around the front [m]
    f_fv = on_eta(zc, zh_fv, prof_fv, eta_cmp)
    f_ps = on_eta(zps, zh_ps, prof_ps, eta_cmp)
    f_ex = np.interp(eta_cmp, eta_ex[::-1], w_ex[::-1], left=1.0, right=0.0)
    m = (f_ex > 0.02) & (f_ex < 0.98)
    rms_ps_ex = float(np.sqrt(np.mean((f_ps[m] - f_ex[m]) ** 2)))
    rms_ps_fv = float(np.sqrt(np.mean((f_ps[m] - f_fv[m]) ** 2)))
    rms_fv_ex = float(np.sqrt(np.mean((f_fv[m] - f_ex[m]) ** 2)))

    # ---- outlet traces --------------------------------------------------------
    x_fv = c_fv[N - 1] / p.cf
    x_ps = r["c"][N] / p.cf
    rms_out = float(np.sqrt(np.mean((x_ps - x_fv) ** 2)))

    # ---- Gate-B-style check (mechanistic_verify.test2_rh pattern) -------------
    ts_fit = np.linspace(0.35 * t_st, 0.85 * t_st, 12)
    zs = []
    for tt in ts_fit:
        jj = int(np.argmin(np.abs(t_eval - tt)))
        zs.append(_z_half(r["z"], r["c"][:, jj] / p.cf))
    v_num = float(np.polyfit(ts_fit, zs, 1)[0])
    mom = float(trapz(1.0 - x_ps, t_eval))
    gate = dict(v_rh=v_rh, v_num=v_num, err_v=abs(v_num - v_rh) / v_rh,
                t_st=t_st, mom=mom, err_mom=abs(mom - t_st) / t_st)

    if fig:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fg, ax = plt.subplots(1, 2, figsize=(11, 4.0))
        ax[0].plot(zc - zh_fv, prof_fv, "r-", lw=1.4, label=f"FV-MOL, N={N}")
        ax[0].plot(eta_ex, w_ex, "k--", lw=1.2, label="exact travelling wave (MM D.8)")
        ax[0].plot(zps - zh_ps, prof_ps, "b-.", lw=1.4,
                   label="$\\psi$-quadrature (Danilov Eqs. 1-8)")
        ax[0].set(xlabel="$\\eta-\\eta_0$ [m]", ylabel="c/c$_f$", xlim=(-0.07, 0.07),
                  title=f"profiles at t = 0.65 t$_{{st}}$  (bc$_f$ = {iso.b*p.cf:.3f})")
        ax[0].legend(fontsize=8)
        ax[1].plot(t_eval / t_st, x_fv, "r-", lw=1.4, label="FV-MOL outlet")
        ax[1].plot(t_eval / t_st, x_ps, "b-.", lw=1.4, label="$\\psi$-quadrature outlet")
        ax[1].axvline(1.0, color="k", ls=":", lw=0.8, label="t$_{st}$ (Cor. B.1)")
        ax[1].set(xlabel="t/t$_{st}$", ylabel="c(L,t)/c$_f$",
                  title="outlet breakthrough (symmetric ansatz vs asymmetric exact)")
        ax[1].legend(fontsize=8)
        snap_origin(fg, label="F2_three_way_langmuir_wave")
        fg.tight_layout()
        fg.savefig(os.path.join(FIGDIR, "F2_three_way_langmuir_wave.png"), dpi=150)
        plt.close(fg)
    return dict(rms_ps_ex=rms_ps_ex, rms_ps_fv=rms_ps_fv, rms_fv_ex=rms_fv_ex,
                rms_out=rms_out, gate=gate, wt_fv=wt_fv, wt_psi=wt_psi,
                Da=r["Da"], t_st=t_st, bcf=iso.b * p.cf)


# ============================================================================
# r3 — non-isothermal Toth demo vs MM V5
# ============================================================================


def run_noniso(fig=True):
    """Task 6: Toth closure at test5_full's illustrative parameters (flagged there;
    no Toth parameter is silently substituted — same source of truth, task 10)."""
    iso = Toth(ns0=2.5, b0=0.49, t0=0.4, Qiso=70e3, T0=298.0)
    curves = {}
    for tag, hw in (("MM adiabatic", 0.0), ("MM wall h=30", 30.0)):
        p = Bed(k=5e-3, DL=5e-5, hw=hw)
        qf = iso.q(p.cf, p.T0)
        t_st = p.L * (p.eps * p.cf + p.alpha_b * qf) / (p.u * p.cf)
        Nn = 600
        t_eval = np.linspace(0.0, 3.0 * t_st, 1600)
        # solve_full returns just `sol` (mechanistic_verify.py:258, and see its own
        # call site at :394); only solve_iso returns the (sol, dz) pair. This caller
        # went stale in the same 42b2ad7 pass as crossing_time above. The unpacked
        # `dzn` was never used, so dropping it changes no number here.
        sol = solve_full(p, iso, Nn, t_eval)
        curves[tag] = (t_eval, sol.y[3 * (Nn - 1)] / p.cf,
                       sol.y[2::3][Nn - 1] - p.T0)
    p = Bed(k=5e-3, DL=5e-5, hw=0.0)                 # Danilov has no wall term: adiabatic-
    #                                                  comparable, but see note below
    qf = iso.q(p.cf, p.T0)
    t_st = p.L * (p.eps * p.cf + p.alpha_b * qf) / (p.u * p.cf)
    t_eval = np.linspace(0.0, 3.0 * t_st, 1600)
    rT = psi_quadrature(p, iso, 600, t_eval, thermal=True, T_feedback=True)
    rF = psi_quadrature(p, iso, 600, t_eval, thermal=True, T_feedback=False)
    y_f = p.cf * R_GAS * p.T0 / 101325.0             # feed mole fraction at 1 atm

    if fig:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fg, ax = plt.subplots(1, 2, figsize=(11, 4.0))
        for tag, (tv, x, dT) in curves.items():
            ax[0].plot(tv / 60, x, lw=1.3, label=tag)
        ax[0].plot(t_eval / 60, rF["c"][-1] / p.cf, "b-.", lw=1.4,
                   label="$\\psi$-quad (capacity frozen at T$_0$)")
        ax[0].plot(t_eval / 60, rT["c"][-1] / p.cf, "m:", lw=1.6,
                   label="$\\psi$-quad (full T feedback)")
        ax[0].axhline(0.05, color="0.7", lw=0.6)
        ax[0].set(xlabel="t [min]", ylabel="c(L,t)/c$_f$",
                  title="non-isothermal Toth: outlet breakthrough")
        ax[0].legend(fontsize=7)
        for tag, (tv, x, dT) in curves.items():
            ax[1].plot(tv / 60, dT, lw=1.3, label=tag)
        ax[1].plot(t_eval / 60, rT["TG"][-1] - p.T0, "m:", lw=1.6,
                   label="$\\psi$-quad T$^G$ (full feedback)")
        ax[1].plot(t_eval / 60, rF["TG"][-1] - p.T0, "b-.", lw=1.4,
                   label="$\\psi$-quad T$^G$ (frozen capacity)")
        ax[1].set(xlabel="t [min]", ylabel="T(L,t) $-$ T$_0$ [K]",
                  title="outlet temperature excursion (note the $\\psi$-quad scale)")
        ax[1].legend(fontsize=7)
        snap_origin(fg, label="F3_nonisothermal_overlay")
        fg.tight_layout()
        fg.savefig(os.path.join(FIGDIR, "F3_nonisothermal_overlay.png"), dpi=150)
        plt.close(fg)

    x_ps = rT["c"][-1] / p.cf
    x_psf = rF["c"][-1] / p.cf
    x_mm = curves["MM adiabatic"][1]
    return dict(t_st=t_st, y_f=y_f,
                dT_mm_ad=float(curves["MM adiabatic"][2].max()),
                dT_mm_w=float(curves["MM wall h=30"][2].max()),
                dT_ps=float(rT["TG"][-1].max() - p.T0),
                dT_ps_frozen=float(rF["TG"][-1].max() - p.T0),
                tbt_mm=crossing_time(curves["MM adiabatic"][0], x_mm, 0.05),
                tbt_ps=crossing_time(t_eval, x_ps, 0.05),
                tbt_psf=crossing_time(t_eval, x_psf, 0.05),
                rms_out=float(np.sqrt(np.mean((x_ps - x_mm) ** 2))),
                rms_out_f=float(np.sqrt(np.mean((x_psf - x_mm) ** 2))))


# ============================================================================
# driver
# ============================================================================


def main():
    os.makedirs(FIGDIR, exist_ok=True)
    sel = set(a.lower() for a in sys.argv[1:]) or {"r1", "r2", "r3"}
    W = 80
    print("=" * W)
    print("psi_quadrature_verify — Danilov (2019) Eqs. 1-8 as the constant-pattern")
    print("limit of mechanistic-model.md Part D.3 (t_s = t_st, u_f = v_RH; [S5-1])")
    print("=" * W)

    if "r1" in sel:
        print("R1  Danilov Fig.-1 reproduction (Table 2 system, Sips, Pe_G=10 & plug)")
        print("    Table 2 inputs (danilov2019.txt:2280-2380):")
        for kk, vv in TABLE2.items():
            print(f"      {kk:22s} {vv}")
        r1 = run_fig1()
        print(f"    Da(CO2) = kL/u = {r1['Da']['CO2']:.3f}   Da(CH4) = {r1['Da']['CH4']:.2e}"
              f"   (Danilov-style N = eps*Da: {r1['N_dan']['CO2']:.3f} / "
              f"{r1['N_dan']['CH4']:.2e})   [S5-5]")
        print(f"    q_eq(feed): CO2-only-site basis {r1['qf']:.3f} mol/kg -> "
              f"t_s = {r1['ts_CO2']:.0f} s ({r1['ts_CO2']/60:.1f} min); "
              f"full-competition {r1['qf_comp']:.3f} -> t_s = "
              f"{r1['ts_CO2_competitive']:.0f} s ({r1['ts_CO2_competitive']/60:.1f} min)")
        print("      (primary run uses the CO2-only basis: Danilov's own text notes CH4")
        print("       'is nearly not adsorbed in dynamic conditions', Da_CH4 ~ 2e-3;")
        print("       t_s is the MM identity t_st in either basis — never fitted [S3-E5])")
        print(f"    outlet mid-front t50 = {r1['t50']/60:.1f} min "
              f"(published Fig. 1: ~14-15 min; experimental circles: ~14.7 min)")
        print(f"    outlet 10-90% rise width = {r1['w1090']/60:.1f} min (published curve:")
        print("      ~10 min — the beta_psi=1 default gives 2ln5/k_f = 4.1 min; matching")
        print("      the published width needs beta_psi ~ 0.4, i.e. their gamma(t) time-")
        print("      series generalisation (B.14-B.16) was likely active — the Langmuir/")
        print("      Table-2 'beta ~ 1' claim is NOT quantitatively self-consistent [S5-2])")
        print(f"    outlet T peak: +{r1['dT_peak']:.1f} K as printed Eqs. give "
              f"(published: +6.1 K); with bed heat storage retained: "
              f"+{r1['dT_peak_corr']:.1f} K")
        print("    VERDICT (qualitative, OCR-sanity): concentration panel — sigmoid")
        print("      shape and 0.05 saturation REPRODUCED, mid-front within ~16% of")
        print("      published (17.1 vs ~14.7 min; the CH4-competition ambiguity brackets")
        print("      it: 8.0-17.1 min), rise narrower (see width note);")
        print("      temperature panel — NOT reproduced, and demonstrably NOT reproducible")
        print("      from the printed equation set: the quasi-steady-solid shortcut")
        print("      (A.13-A.16) convects ALL adsorption heat out with the gas instantly,")
        print("      so the outlet sits at +50 K from t=0 and STEPS DOWN at breakthrough,")
        print("      whereas the published curve is a 6-K PULSE peaking near breakthrough.")
        print("      A pulse requires the solid heat-capacity term (rho_S*Cp_S*dT_S/dt,")
        print("      their A.13) that A.14 sets to zero; the adiabatic two-wave estimate")
        print("      WITH storage still gives a ~76 K plateau, so the measured 6 K also")
        print("      needs wall losses — absent from their Table 1 entirely.  Their")
        print("      plotted AADM T-curve therefore cannot come from Eqs. 1-8 as printed;")
        print("      their implementation evidently retained solid storage.  [S3-E3]")

    if "r2" in sel:
        print("-" * W)
        print("R2  three-way isothermal Langmuir comparison (bc_f = 2.045, MM test3 set)")
        r2 = run_langmuir()
        print(f"    Da = {r2['Da']:.2f}   t_st = {r2['t_st']:.1f} s")
        print("    RMS (0.65 t_st profile, 0.02<c/cf<0.98):")
        print(f"      psi-quadrature vs MM D.8 exact : {r2['rms_ps_ex']*100:6.2f} %"
              f"   <- the Part-2 open number (no pass/fail gate)")
        print(f"      psi-quadrature vs FV-MOL       : {r2['rms_ps_fv']*100:6.2f} %")
        print(f"      FV-MOL vs MM D.8 exact         : {r2['rms_fv_ex']*100:6.2f} %"
              f"   (V3 baseline: 0.30 %)")
        print(f"    RMS outlet trace psi vs FV-MOL   : {r2['rms_out']*100:6.2f} %")
        g = r2["gate"]
        print(f"    Gate-B-style: v_front = {g['v_num']:.4e} vs v_RH = {g['v_rh']:.4e}"
              f" m/s  (err {g['err_v']*100:.3f} %)")
        print(f"                  first moment = {g['mom']:.1f} s vs t_st = {g['t_st']:.1f} s"
              f"  (err {g['err_mom']*100:.3f} %)")
        print(f"    wall-clock at matched N=3000, 800 outputs:  FV-MOL {r2['wt_fv']:.2f} s"
              f"   psi-quadrature {r2['wt_psi']:.2f} s"
              f"   (speed-up x{r2['wt_fv']/max(r2['wt_psi'],1e-9):.0f})")

    if "r3" in sel:
        print("-" * W)
        print("R3  non-isothermal Toth demo (illustrative test5_full parameters)")
        r3 = run_noniso()
        print(f"    feed mole fraction y_f = {r3['y_f']*100:.1f} % — Danilov's Eq.-1 ansatz")
        print("    is stated valid only for LOW adsorbate concentration")
        print("    (danilov2019.txt:473-481); that restriction IS EXCEEDED here — the")
        print("    result is shown as a limit-breaking demonstration, not applied silently.")
        print(f"    dT_max at OUTLET (V5's table quotes field max 18.9/4.9 K):")
        print(f"      MM adiabatic {r3['dT_mm_ad']:.1f} K | MM wall {r3['dT_mm_w']:.1f} K"
              f" | psi-quad {r3['dT_ps']:.1f} K (frozen-capacity "
              f"{r3['dT_ps_frozen']:.1f} K)")
        print(f"    t_BT (5%):  MM adiabatic {r3['tbt_mm']:.0f} s | psi-quad feedback "
              f"{r3['tbt_ps']:.0f} s | psi-quad frozen {r3['tbt_psf']:.0f} s"
              f"   (t_st = {r3['t_st']:.0f} s)")
        print(f"    RMS outlet trace vs MM adiabatic: psi-quad feedback "
              f"{r3['rms_out']*100:.1f} % | frozen {r3['rms_out_f']*100:.1f} %")
        print("    (feedback t_BT = 0: the spuriously hot gas of the printed energy")
        print("     shortcut suppresses q_eq and leaks feed through the clean bed —")
        print("     the mass and energy errors compound outside the dilute regime)")
        print("    Reading: the quasi-steady-solid energy shortcut has no bed thermal")
        print("    capacitance, so the psi-quadrature cannot represent MM V5's two-front")
        print("    structure (hot plateau, roll-up; MM D.6) — a single symmetric ansatz")
        print("    is structurally unable to, regardless of parameter choice.")

    print("=" * W)
    print(f"figures -> {FIGDIR}")


if __name__ == "__main__":
    main()

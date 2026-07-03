"""
mechanistic_verify.py — numerical verification of every closed-form claim in
src/docs/mechanistic-model.md (Parts B, D, E).

Scheme: finite-volume Method of Lines, upwind convection, central dispersion,
Danckwerts inlet as the exact inlet-face flux (scheme (b), doc §E.1) -> the
discrete inventory identity dM/dt = u*cf - u*c_out holds to solver tolerance.

Tests
  T1  no-adsorption ADE vs Ogata-Banks erfc solution (doc D.5), grid convergence
  T2  isothermal Langmuir, large Da: front speed vs v_RH (D.3); first moment vs t_st (Cor. B.1)
  T3  finite-k travelling wave vs exact implicit Langmuir profile (D.8)
  T4  discrete mass-balance drift (B.3 / E.5-5) on the T2 run
  T5  full non-isothermal Toth demo (adiabatic + wall-coupled): t_BT, t_sat, dT_max, roll-up

Parameters are ILLUSTRATIVE (doc §C.4 flag): they verify mathematics, not sorbent data.
Figures -> src/img/generated/mechanistic/    Summary -> printed table.

Run from repo root:  python src/solver/mechanistic_verify.py
"""

from __future__ import annotations

import os
import numpy as np
from dataclasses import dataclass
from scipy.integrate import solve_ivp
from scipy.special import erfc

FIGDIR = os.path.join("src", "img", "generated", "mechanistic")
R_GAS = 8.314

# ----------------------------------------------------------------------------- utilities


def l2_rel(a, b):
    """Relative L2 error of a vs reference b."""
    return np.sqrt(np.trapz((a - b) ** 2, dx=1.0) / max(np.trapz(b**2, dx=1.0), 1e-300))


def ogata_banks(z, t, v, D, cf):
    """Doc (D.5). Semi-infinite step-input ADE solution."""
    t = np.maximum(t, 1e-12)
    s = 2.0 * np.sqrt(D * t)
    term1 = 0.5 * erfc((z - v * t) / s)
    # exp*erfc computed stably in log space
    arg = v * z / D
    term2 = np.where(arg < 700, 0.5 * np.exp(np.minimum(arg, 700)) * erfc((z + v * t) / s), 0.0)
    return cf * (term1 + term2)


# ----------------------------------------------------------------------------- model


@dataclass
class Bed:
    L: float = 0.21          # m
    eps: float = 0.4         # bed voidage (placeholder, doc C.4)
    u: float = 0.0294        # m/s superficial
    DL: float = 5e-5         # m^2/s
    alpha_b: float = 660.0   # (1-eps)*rho_p = bulk density kg/m^3
    cf: float = 4.09         # mol/m^3 feed
    k: float = 5e-3          # 1/s LDF
    # thermal
    rho_g: float = 1.15
    cpg: float = 1050.0
    cps: float = 1000.0
    lam: float = 0.15        # W/mK
    dH: float = 70e3         # (-ΔH) J/mol
    hw: float = 0.0          # wall coeff (0 = adiabatic)
    dcol: float = 8.5e-3
    T0: float = 298.0
    Tf: float = 298.0
    Twall: float = 298.0

    @property
    def Ch(self):
        return self.eps * self.rho_g * self.cpg + self.alpha_b * self.cps


class Langmuir:
    def __init__(self, qm, b):
        self.qm, self.b = qm, b

    def q(self, c, T=None):
        c = np.maximum(c, 0.0)
        return self.qm * self.b * c / (1.0 + self.b * c)


class Toth:
    """Concentration-basis Toth with van't Hoff b(T) (doc A.3); chi = alphaT = 0."""

    def __init__(self, ns0, b0, t0, Qiso, T0):
        self.ns0, self.b0, self.t0, self.Qiso, self.T0 = ns0, b0, t0, Qiso, T0

    def q(self, c, T):
        c = np.maximum(c, 0.0)
        b = self.b0 * np.exp((self.Qiso / (R_GAS * self.T0)) * (self.T0 / T - 1.0))
        s = np.power(np.maximum(b * c, 0.0), self.t0)
        return self.ns0 * b * c / np.power(1.0 + s, 1.0 / self.t0)


def rhs_iso(t, y, p: Bed, iso, N, dz):
    """Isothermal FV scheme (b): y = interleaved [c0,q0,c1,q1,...]."""
    c = y[0::2]
    q = y[1::2]
    dq = p.k * (iso.q(c) - q) if p.k > 0 else np.zeros_like(c)
    # face fluxes F[0..N]; F[0] Danckwerts, F[N] zero-gradient outlet
    F = np.empty(N + 1)
    F[0] = p.u * p.cf
    F[1:N] = p.u * c[:-1] - p.eps * p.DL * (c[1:] - c[:-1]) / dz
    F[N] = p.u * c[-1]
    dc = ((F[:-1] - F[1:]) / dz - p.alpha_b * dq) / p.eps
    out = np.empty_like(y)
    out[0::2] = dc
    out[1::2] = dq
    return out


def rhs_full(t, y, p: Bed, iso, N, dz):
    """Non-isothermal FV scheme (b): y = interleaved [c,q,T]*N."""
    c = y[0::3]
    q = y[1::3]
    T = y[2::3]
    dq = p.k * (iso.q(c, T) - q)
    F = np.empty(N + 1)
    F[0] = p.u * p.cf
    F[1:N] = p.u * c[:-1] - p.eps * p.DL * (c[1:] - c[:-1]) / dz
    F[N] = p.u * c[-1]
    dc = ((F[:-1] - F[1:]) / dz - p.alpha_b * dq) / p.eps
    G = np.empty(N + 1)  # heat fluxes
    G[0] = p.u * p.rho_g * p.cpg * p.Tf
    G[1:N] = p.u * p.rho_g * p.cpg * T[:-1] - p.lam * (T[1:] - T[:-1]) / dz
    G[N] = p.u * p.rho_g * p.cpg * T[-1]
    dT = ((G[:-1] - G[1:]) / dz + p.alpha_b * p.dH * dq
          - (4.0 * p.hw / p.dcol) * (T - p.Twall)) / p.Ch
    out = np.empty_like(y)
    out[0::3] = dc
    out[1::3] = dq
    out[2::3] = dT
    return out


def solve_iso(p, iso, N, t_eval, rtol=1e-8, atol=None):
    dz = p.L / N
    y0 = np.zeros(2 * N)
    if atol is None:
        atol = 1e-9 * max(p.cf, 1.0)
    sol = solve_ivp(rhs_iso, (0.0, t_eval[-1]), y0, t_eval=t_eval, args=(p, iso, N, dz),
                    method="LSODA", rtol=rtol, atol=atol, lband=2, uband=2)
    assert sol.success, sol.message
    return sol, dz


def solve_full(p, iso, N, t_eval, rtol=1e-7):
    dz = p.L / N
    y0 = np.zeros(3 * N)
    y0[2::3] = p.T0
    atol = np.tile([1e-9 * p.cf, 1e-9, 1e-7 * p.T0], N)
    sol = solve_ivp(rhs_full, (0.0, t_eval[-1]), y0, t_eval=t_eval, args=(p, iso, N, dz),
                    method="LSODA", rtol=rtol, atol=atol, lband=3, uband=3)
    assert sol.success, sol.message
    return sol, dz


def crossing_time(t, s, level):
    """First time s(t) crosses level (linear interpolation)."""
    idx = np.where(s >= level)[0]
    if len(idx) == 0:
        return np.nan
    i = idx[0]
    if i == 0:
        return t[0]
    return t[i - 1] + (level - s[i - 1]) * (t[i] - t[i - 1]) / (s[i] - s[i - 1])


# ----------------------------------------------------------------------------- tests


def test1_ade(fig):
    """T1: k=0 pure advection-dispersion vs Ogata-Banks; grid convergence."""
    p = Bed(k=0.0, DL=5.1e-5)          # Pe_i = (u/eps)L/DL ~ 300 -> BC effects O(e^-Pe) negligible
    v, D = p.u / p.eps, p.DL           # interstitial frame: c_t + v c_z = D c_zz
    t_end = 2.2 * p.L / v
    t_eval = np.linspace(0.0, t_end, 400)
    rows = []
    for N in (500, 1000, 2000, 4000):
        sol, dz = solve_iso(p, Langmuir(0.0, 1.0), N, t_eval)
        c_out = sol.y[2 * (N - 1)]     # last cell centre z = L - dz/2
        z_out = p.L - dz / 2.0
        ref = ogata_banks(z_out, t_eval, v, D, p.cf)
        err = np.sqrt(np.trapz((c_out - ref) ** 2, t_eval) / np.trapz(ref**2, t_eval))
        rows.append((N, err))
    if fig:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fg, ax = plt.subplots(1, 2, figsize=(10, 3.6))
        ax[0].plot(t_eval, ref / p.cf, "k-", lw=2, label="Ogata–Banks (D.5)")
        ax[0].plot(t_eval, c_out / p.cf, "r--", label=f"FV-MOL N={N}")
        ax[0].set(xlabel="t [s]", ylabel="c(L,t)/c_f", title="T1: Gate-A advection–dispersion")
        ax[0].legend()
        Ns = np.array([r[0] for r in rows], float)
        es = np.array([r[1] for r in rows])
        ax[1].loglog(Ns, es, "o-", label="L² error")
        ax[1].loglog(Ns, es[0] * Ns[0] / Ns, "k:", label="slope −1 (1st order)")
        ax[1].set(xlabel="N", ylabel="rel. L² error", title="grid convergence")
        ax[1].legend()
        fg.tight_layout()
        fg.savefig(os.path.join(FIGDIR, "V1_ade_vs_erfc.png"), dpi=150)
        plt.close(fg)
    return rows


def test2_rh(fig):
    """T2: sharp-front speed vs v_RH; first-moment vs t_st. T4: mass drift."""
    p = Bed(k=2.0, DL=1e-6)
    iso = Langmuir(qm=1.0, b=0.5)                    # b*cf = 2.045
    qf = iso.q(p.cf)
    t_st = p.L * (p.eps * p.cf + p.alpha_b * qf) / (p.u * p.cf)
    v_rh = p.L / t_st
    N = 800
    t_eval = np.linspace(0.0, 2.0 * t_st, 1200)
    sol, dz = solve_iso(p, iso, N, t_eval)
    c = sol.y[0::2]                                   # (N, nt)
    q = sol.y[1::2]
    zc = (np.arange(N) + 0.5) * dz
    # front position (c = cf/2) at a series of times in mid-column
    ts = np.linspace(0.35 * t_st, 0.85 * t_st, 12)
    zs = []
    for tt in ts:
        j = np.argmin(np.abs(t_eval - tt))
        prof = c[:, j] / p.cf
        # first z where prof drops through 0.5 (monotone decreasing front)
        idx = np.where(prof <= 0.5)[0]
        i = idx[0]
        z_half = np.interp(0.5, [prof[i], prof[i - 1]], [zc[i], zc[i - 1]])
        zs.append(z_half)
    v_num = np.polyfit(ts, zs, 1)[0]
    # first-moment invariance (Cor. B.1): trapz of (1 - c_out/cf) up to full saturation
    c_out = c[N - 1]
    mom = np.trapz(1.0 - c_out / p.cf, t_eval)
    # T4: discrete inventory drift
    M_fv = (p.eps * c + p.alpha_b * q).sum(axis=0) * dz     # exact FV inventory
    inflow = p.u * p.cf * t_eval
    outflow = np.concatenate([[0.0], np.cumsum(0.5 * (c_out[1:] + c_out[:-1]) * np.diff(t_eval))]) * p.u
    drift = np.abs(M_fv - M_fv[0] - (inflow - outflow)) / np.maximum(inflow, 1e-30)
    drift_max = np.nanmax(drift[10:])
    if fig:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fg, ax = plt.subplots(1, 2, figsize=(10, 3.6))
        for tt in np.linspace(0.2, 1.0, 5) * t_st:
            j = np.argmin(np.abs(t_eval - tt))
            ax[0].plot(zc, c[:, j] / p.cf, lw=1.2, label=f"t={tt:.0f}s")
        for tt in ts:
            ax[0].axvline(v_rh * tt, color="0.8", lw=0.5, zorder=0)
        ax[0].set(xlabel="z [m]", ylabel="c/c_f", title="T2: shock at v_RH (grey = RH prediction)")
        ax[0].legend(fontsize=7)
        ax[1].plot(t_eval / t_st, c_out / p.cf, "b-")
        ax[1].axvline(1.0, color="k", ls=":", label="t_st (B.1/D.4)")
        ax[1].set(xlabel="t/t_st", ylabel="c(L,t)/c_f", title="outlet breakthrough")
        ax[1].legend()
        fg.tight_layout()
        fg.savefig(os.path.join(FIGDIR, "V2_rh_front.png"), dpi=150)
        plt.close(fg)
    return dict(v_rh=v_rh, v_num=v_num, err_v=abs(v_num - v_rh) / v_rh,
                t_st=t_st, moment=mom, err_mom=abs(mom - t_st) / t_st, drift=drift_max)


def test3_wave(fig):
    """T3: finite-k outlet/profile vs exact Langmuir travelling wave (D.8)."""
    p = Bed(k=2e-2, DL=0.0)                 # k chosen so the wave (width ~ v/k) sits interior to the bed
    iso = Langmuir(qm=1.0, b=0.5)
    qf = iso.q(p.cf)
    t_st = p.L * (p.eps * p.cf + p.alpha_b * qf) / (p.u * p.cf)
    v = p.L / t_st
    N = 3000
    t_eval = np.linspace(0.0, 2.6 * t_st, 1400)
    sol, dz = solve_iso(p, iso, N, t_eval, rtol=1e-8)
    c = sol.y[0::2]
    zc = (np.arange(N) + 0.5) * dz
    # numerical profile at a time when the front is fully developed & interior
    j = np.argmin(np.abs(t_eval - 0.65 * t_st))
    prof = c[:, j] / p.cf
    # exact wave (D.8): eta - eta0 = -(v/(k b cf)) [ln w - (1+b cf) ln(1-w)]
    # eta(w) is strictly decreasing: w->0 gives eta->+inf, w->1 gives eta->-inf.
    w = np.linspace(1e-6, 1 - 1e-6, 4001)
    eta = -(v / (p.k * iso.b * p.cf)) * (np.log(w) - (1 + iso.b * p.cf) * np.log1p(-w))
    # align both at w = 0.5
    idx = np.where(prof <= 0.5)[0]
    i0 = idx[0]
    z_half = np.interp(0.5, [prof[i0], prof[i0 - 1]], [zc[i0], zc[i0 - 1]])
    eta_half = np.interp(0.5, w, eta[::-1][::-1]) if False else eta[np.argmin(np.abs(w - 0.5))]
    # w as a function of eta: xp must ascend -> use reversed arrays
    w_theory = np.interp(zc - z_half, (eta - eta_half)[::-1], w[::-1], left=1.0, right=0.0)
    mask = (w_theory > 0.02) & (w_theory < 0.98)
    err = np.sqrt(np.mean((prof[mask] - w_theory[mask]) ** 2))
    if fig:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fg, ax = plt.subplots(figsize=(6.4, 3.8))
        ax.plot(zc - z_half, prof, "r-", lw=1.4, label=f"FV-MOL, N={N}, t=0.62 t_st")
        ax.plot(eta - eta_half, w, "k--", lw=1.2, label="exact travelling wave (D.8)")
        ax.set(xlabel="η − η₀ [m]", ylabel="c/c_f",
               title=f"T3: LDF constant-pattern wave  (RMS dev {err*100:.2f}%)")
        ax.legend()
        fg.tight_layout()
        fg.savefig(os.path.join(FIGDIR, "V3_travelling_wave.png"), dpi=150)
        plt.close(fg)
    return dict(rms=err, t_st=t_st)


def test5_full(fig):
    """T5: non-isothermal Toth demo, adiabatic vs wall-coupled vs isothermal."""
    iso = Toth(ns0=2.5, b0=0.49, t0=0.4, Qiso=70e3, T0=298.0)
    results = {}
    curves = {}
    for tag, hw in (("adiabatic", 0.0), ("wall h=30", 30.0)):
        p = Bed(k=5e-3, DL=5e-5, hw=hw)
        qf = iso.q(p.cf, p.T0)
        t_st = p.L * (p.eps * p.cf + p.alpha_b * qf) / (p.u * p.cf)
        N = 600
        t_eval = np.linspace(0.0, 3.0 * t_st, 1600)
        sol, dz = solve_full(p, iso, N, t_eval)
        c_out = sol.y[3 * (N - 1)]
        T = sol.y[2::3]
        x = c_out / p.cf
        t_bt = crossing_time(t_eval, x, 0.05)
        t_sat = crossing_time(t_eval, x, 0.95)
        jbt = np.searchsorted(t_eval, t_bt)
        q_dyn = p.u * np.trapz(p.cf - c_out[:jbt + 1], t_eval[:jbt + 1]) / (p.alpha_b * p.L)
        results[tag] = dict(t_st=t_st, t_bt=t_bt, t_sat=t_sat, q_dyn=q_dyn,
                            dT_max=float(T.max() - p.T0), rollup=float(x.max()))
        curves[tag] = (t_eval, x, T[N - 1] - p.T0)
    # isothermal reference (same isotherm at T0)
    p = Bed(k=5e-3, DL=5e-5)

    class IsoT:
        def q(self, c, T=None):
            return iso.q(c, p.T0 * np.ones_like(np.atleast_1d(c)))
    qf = iso.q(p.cf, p.T0)
    t_st = p.L * (p.eps * p.cf + p.alpha_b * qf) / (p.u * p.cf)
    t_eval = np.linspace(0.0, 3.0 * t_st, 1600)
    sol, dz = solve_iso(p, IsoT(), 600, t_eval)
    x_iso = sol.y[2 * 599] / p.cf
    if fig:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fg, ax = plt.subplots(1, 2, figsize=(10, 3.8))
        ax[0].plot(t_eval / 60, x_iso, "k-", label="isothermal")
        for tag, (tv, x, dT) in curves.items():
            ax[0].plot(tv / 60, x, "--", label=tag)
        ax[0].axhline(0.05, color="0.7", lw=0.6)
        ax[0].set(xlabel="t [min]", ylabel="c(L,t)/c_f", title="T5: Toth breakthrough (illustrative params)")
        ax[0].legend(fontsize=8)
        for tag, (tv, x, dT) in curves.items():
            ax[1].plot(tv / 60, dT, label=tag)
        ax[1].set(xlabel="t [min]", ylabel="T(L,t) − T₀ [K]", title="outlet temperature excursion")
        ax[1].legend(fontsize=8)
        fg.tight_layout()
        fg.savefig(os.path.join(FIGDIR, "V4_nonisothermal.png"), dpi=150)
        plt.close(fg)
    results["isothermal t_bt"] = crossing_time(t_eval, x_iso, 0.05)
    return results


def main():
    os.makedirs(FIGDIR, exist_ok=True)
    fig = True
    print("=" * 78)
    print("T1  no-adsorption ADE vs Ogata-Banks (D.5)")
    for N, e in test1_ade(fig):
        print(f"    N={N:5d}   rel L2 err = {e*100:8.4f} %   {'PASS(<1%)' if e < 0.01 else ''}")
    print("T2  Rankine-Hugoniot front speed (D.3) + first moment (B.1)  [T4 drift]")
    r = test2_rh(fig)
    print(f"    v_RH = {r['v_rh']:.4e} m/s   v_num = {r['v_num']:.4e} m/s   err = {r['err_v']*100:.3f} %")
    print(f"    t_st = {r['t_st']:.1f} s     moment = {r['moment']:.1f} s     err = {r['err_mom']*100:.3f} %")
    print(f"    T4 mass-balance drift (rel.) = {r['drift']:.2e}")
    print("T3  travelling wave vs exact implicit profile (D.8)")
    r3 = test3_wave(fig)
    print(f"    RMS profile deviation = {r3['rms']*100:.3f} %  (t_st = {r3['t_st']:.1f} s)")
    print("T5  non-isothermal Toth demo")
    r5 = test5_full(fig)
    for tag, d in r5.items():
        if isinstance(d, dict):
            print(f"    {tag:12s}: t_st={d['t_st']:.0f}s  t_BT={d['t_bt']:.0f}s  t_sat={d['t_sat']:.0f}s  "
                  f"q_dyn={d['q_dyn']:.3f} mol/kg  dT_max={d['dT_max']:.1f}K  max c/cf={d['rollup']:.3f}")
        else:
            print(f"    {tag}: {d:.0f}s")
    print("=" * 78)


if __name__ == "__main__":
    main()

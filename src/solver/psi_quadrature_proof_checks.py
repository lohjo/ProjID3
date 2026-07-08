"""psi_quadrature_proof_checks.py — numerical verification of every quantitative claim in
src/docs/psi-quadrature-consistency-proof.md (Part 2 deliverable).

Pure numpy/scipy, no fitted parameters, no repo imports. Nondimensional units: k=1
(except section 8, which uses k=25 to match a resolved front in a unit bed), c_f=1,
lam = b*c_f.  Section numbers below match the doc's Appendix (section 8) table.

Route A outlet curve in stretched units:  s(w) = ln w - (1+lam) ln(1-w)   (MM D.8)
Route B tent CDF (rate a, centered 0):    B(t) = .5 e^{a t} (t<0), 1-.5 e^{-a t} (t>=0)

Run:  python src/solver/psi_quadrature_proof_checks.py       (~40 s)
"""
import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq, minimize_scalar, minimize

Z3 = 1.2020569031595942854  # zeta(3)
PI2 = np.pi**2

def s_of_w(w, lam):
    return np.log(w) - (1.0 + lam) * np.log1p(-w)

def tent(x, a):
    return np.where(x < 0, .5 * np.exp(a * x), 1 - .5 * np.exp(-a * x))

def half(x, a):
    return .5 * np.exp(-a * np.abs(x))

# ---------- 1. Lemma 2.5: moment formulas ----------
print("== 1. Moments of route-A profile (s-units), quadrature vs closed form ==")
print(f"{'lam':>8} {'E1 num':>10} {'E1=lam':>10} {'Var num':>12} {'Var form':>12} {'mu3 num':>12} {'mu3 form':>12}")
for lam in [0.05, 0.5, 1.0, 2.045, 5.0, 20.0]:
    E1 = quad(lambda w: s_of_w(w, lam), 0, 1, points=[0, 1])[0]
    E2 = quad(lambda w: s_of_w(w, lam)**2, 0, 1, points=[0, 1])[0]
    E3 = quad(lambda w: s_of_w(w, lam)**3, 0, 1, points=[0, 1])[0]
    var, mu3 = E2 - E1**2, E3 - 3 * E1 * E2 + 2 * E1**3
    var_f = lam**2 + PI2 / 3 * (1 + lam)
    mu3_f = 2 * lam**3 + 6 * lam**2 + 6 * lam + 6 * (Z3 - 1) * lam * (1 + lam)
    print(f"{lam:8.3f} {E1:10.5f} {lam:10.5f} {var:12.6f} {var_f:12.6f} {mu3:12.5f} {mu3_f:12.5f}")

# ---------- 2. Corollary 2.6: skewness limits, slope, monotonicity ----------
print("\n== 2. Skewness gamma1(lam): slope at 0, limit 2, strict monotonicity ==")
def g1(lam):
    v = lam**2 + PI2 / 3 * (1 + lam)
    m = 2 * lam**3 + 6 * lam**2 + 6 * lam + 6 * (Z3 - 1) * lam * (1 + lam)
    return m / v**1.5
print(f"slope at 0: num {g1(1e-6)/1e-6:.6f}  formula 6*zeta3/(pi^2/3)^1.5 = {6*Z3/(PI2/3)**1.5:.6f}")
g = np.geomspace(1e-5, 1e5, 4000)
d = np.diff([g1(x) for x in g])
print(f"gamma1(400) = {g1(400):.4f} (-> 2); strictly increasing on geomspace(1e-5,1e5): {bool(np.all(d > 0))}")
print("gamma1 at lam = 0.5, 1, 2.045, 5:", [round(g1(x), 4) for x in (0.5, 1, 2.045, 5)])

# ---------- 3. Theorem 4.3 constant ----------
print("\n== 3. sup |logistic - tent| (equal unit rates, common center) = 3/2 - sqrt(2) ==")
ss = np.linspace(-30, 30, 400001)
gap = np.max(np.abs(1 / (1 + np.exp(-ss)) - tent(ss, 1.0)))
print(f"num {gap:.8f}   exact = {1.5 - np.sqrt(2):.8f}")

# ---------- 4. (D.7)<->(D.8); Lemma 2.4 beta(c) identity ----------
print("\n== 4. Shape ODE vs implicit form; exact driving-force law psi_t = -k beta(c) psi ==")
lam = 2.045
sol = solve_ivp(lambda s, w: w * (1 - w) / (1 + lam * w), [0, 25], [0.5],
                dense_output=True, rtol=1e-11, atol=1e-13)
werr = []
for sv in np.linspace(0, 20, 50):
    w_imp = brentq(lambda w: s_of_w(w, lam) - s_of_w(0.5, lam) - sv, 1e-15, 1 - 1e-15, xtol=1e-14)
    werr.append(abs(sol.sol(sv)[0] - w_imp))
print(f"max |w_ODE - w_implicit| = {max(werr):.2e}")
qf = lam / (1 + lam)  # qm = cf = 1
psi_w = lambda w: lam * w / (1 + lam * w) - qf * w
beta_c = lambda w: 1 - (1 + lam) / (1 + lam * w)**2
w0 = 0.37
dwds = w0 * (1 - w0) / (1 + lam * w0)
lhs = (lam / (1 + lam * w0)**2 - qf) * dwds
rhs = -beta_c(w0) * psi_w(w0) / lam
print(f"identity at w=0.37: dpsi/ds = {lhs:.10f} vs -beta(c)psi/lam = {rhs:.10f}")
print(f"beta(cf) = {beta_c(1.0):.6f} = lam/(1+lam) = {lam/(1+lam):.6f};  beta(0+) = {beta_c(1e-12):.4f} = -lam")

# ---------- 5. Lemma 2.3 tail rates ----------
print("\n== 5. Tail e-folding rates: leading k*lam, trailing k*lam/(1+lam), ratio 1+lam ==")
for lam in [0.5, 2.045, 8.0]:
    wA, wB = 1e-5, 2e-5
    r_lead = (s_of_w(wB, lam) - s_of_w(wA, lam)) / np.log(wB / wA)
    r_tail = (s_of_w(1 - wA, lam) - s_of_w(1 - wB, lam)) / np.log(wB / wA)
    print(f"lam={lam:6.3f}: ds/dlnw|lead = {r_lead:.5f} (->1);  ds/dln(1-w)|tail = {r_tail:.5f} (->{1+lam:.3f})")

# ---------- 6. Theorem 5.2 sup-norm floors (Cor. B.1 centering; k=1) ----------
print("\n== 6. sup-norm floor |W_A - tent| in t-units, first-moment centred ==")
def routeA_c_of_t(lam):
    def w_of_t(t):
        s = lam * t + lam
        try:
            return brentq(lambda w: s_of_w(w, lam) - s, 1e-300, 1 - 1e-16, xtol=1e-15)
        except ValueError:
            return 0.0 if s < 0 else 1.0
    return np.vectorize(w_of_t)
print(f"{'lam':>8} {'frozen beta=1':>14} {'beta=lam/(1+lam)':>18} {'free-shift, beta=1':>20}")
for lam in [0.1, 0.5, 1.0, 2.045, 5.0, 20.0]:
    tt = np.linspace(-12 / lam - 12, 12 / lam + 12, 6001)
    wa = routeA_c_of_t(lam)(tt)
    f1 = np.max(np.abs(wa - tent(tt, 1.0)))
    f2 = np.max(np.abs(wa - tent(tt, lam / (1 + lam))))
    sh = minimize_scalar(lambda dd: np.max(np.abs(wa - tent(tt - dd, 1.0))), bounds=(-10, 10), method='bounded')
    print(f"{lam:8.3f} {f1:14.5f} {f2:18.5f} {sh.fun:20.5f}")

# ---------- 7. variance ratios ----------
print("\n== 7. Var_A/Var_B: pi^2/(6 lam^2) divergence (frozen) and 1/2 saturation ==")
for lam in [0.1, 1.0, 2.045, 20.0, 1e4]:
    varA = (lam**2 + PI2 / 3 * (1 + lam)) / lam**2
    print(f"lam={lam:9.1f}: frozen = {varA/2:9.4f}   corrected = {varA*lam**2/(2*(1+lam)**2):8.4f}")

# ---------- 8. Theorem 5.1 three-way split (k=25, lam=2.045, matches test3_wave) ----------
print("\n== 8. Discretisation error -> 0 (O(dz)); model error -> floor ==")
lam = 2.045; k = 25.; eps = .4; u = 1.; ab = 1.; qm = 1.; cf = 1.
b = lam; qf = qm * b * cf / (1 + b * cf)
vRH = u * cf / (eps * cf + ab * qf); Lb = 1.; tst = Lb / vRH
t = np.linspace(0, 3.2, 2500); mwin = t >= 0.5   # exclude the start-up window t < 3/k
B_inf = tent(t - tst, k)
def march(nz):
    """Eq.-2-type flux quadrature seeded by the tent (incl. gas-storage term)."""
    zj = np.linspace(0, Lb, nz + 1); F = np.full(len(t), u * cf)
    for j in range(1, nz + 1):
        th = t - zj[j] / vRH
        F = F - (ab * k * qf * half(th, k) + eps * cf * k * half(th, k)) * (zj[j] - zj[j - 1])
    return F / (u * cf)
outs = [march(n) for n in (40, 160, 640, 2560)]
print("|march - own continuum limit|_sup (t>=0.5):",
      [round(float(np.max(np.abs(o[mwin] - B_inf[mwin]))), 5) for o in outs], " => O(dz)")
print("start-up deficit at t=0 (analytic 1 - tent(0) = 0.5):",
      round(float(abs(outs[-1][0] - B_inf[0])), 4))
N = 900; z = np.linspace(0, Lb, N); dz = z[1] - z[0]
def rhs(tt, y):
    c, q = y[:N], y[N:]
    dq = k * (qm * b * c / (1 + b * c) - q)
    dc = np.empty_like(c)
    dc[1:] = (-u * (c[1:] - c[:-1]) / dz - ab * dq[1:]) / eps
    dc[0] = 0.
    return np.concatenate([dc, dq])
y0 = np.zeros(2 * N); y0[0] = cf
s8 = solve_ivp(rhs, [0, 3.2], y0, t_eval=t, method='LSODA', rtol=1e-8, atol=1e-10)
cp = s8.y[N - 1, :]
def wave_t(tv):
    s = k * lam * (tv - tst) + lam
    try:
        return brentq(lambda w: s_of_w(w, lam) - s, 1e-300, 1 - 1e-16)
    except ValueError:
        return 0.0 if s < 0 else 1.0
w_ex = np.array([wave_t(tv) for tv in t])
print("|march(2560) - PDE|_sup =", round(float(np.max(np.abs(outs[-1][mwin] - cp[mwin]))), 4),
      "; |tent limit - PDE|_sup =", round(float(np.max(np.abs(B_inf[mwin] - cp[mwin]))), 4),
      "(predicted floor 0.14918)")
print("|PDE - exact D.8 wave|_sup =", round(float(np.max(np.abs(cp - w_ex))), 4), "(finite-N/Da)")

# ---------- 9. Theorem 6.2 plateau bound ----------
print("\n== 9. Two-front: best single tent (shift AND rate free) vs plateau bound ==")
cI = .955
def best(Tsep):
    tt = np.linspace(-15, Tsep + 15, 12001)
    truth = cI / (1 + np.exp(-8 * tt)) + (1 - cI) / (1 + np.exp(-8 * (tt - Tsep)))
    f = lambda p: np.max(np.abs(tent(tt - p[0], np.exp(p[1])) - truth))
    return minimize(f, [Tsep * .05, 0.], method='Nelder-Mead',
                    options={'xatol': 1e-4, 'fatol': 1e-6, 'maxiter': 400}).fun
for Ts in [.5, 2, 5, 10, 30]:
    print(f"Tsep={Ts:5.1f}: best single-front sup = {best(Ts):.4f}   plateau deficit (cf-cI) = {1-cI:.3f}")
print("\nALL CHECKS DONE")

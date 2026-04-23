# Repo: github.com/<you>/co2-regen-design-proj
# File: solver/pde_mol.py

import numpy as np
from scipy.integrate import solve_ivp

# ---- Parameters (load from yaml / supervisor inputs) ----
eps, rho_p, rho_g = 0.4, 1200.0, 1.2
c_pg, c_ps = 1040.0, 900.0
u, L, d_c = 0.05, 0.15, 0.02
D_ax, lam_ax = 1e-4, 0.2
k_a, a_p = 0.1, 1.5e4
h_f, h_w = 50.0, 30.0
dH_ads = 75e3                # J/mol
q_m0, b0 = 2.5, 1e-5
chi, T_ref = 0.0, 298.15

N = 200
z = np.linspace(0, L, N)
dz = z[1] - z[0]

def langmuir(C, T):
    b = b0 * np.exp(dH_ads / (8.314 * T))
    q_m = q_m0 * np.exp(chi / T)
    return q_m * b * C / (1 + b * C)

def rhs(t, y):
    C, q, Tg, Ts = np.split(y, 4)
    # First-order upwind for convection; central for diffusion
    dCdz = np.zeros_like(C); dTdz = np.zeros_like(Tg)
    dCdz[1:]  = (C[1:] - C[:-1]) / dz
    dTdz[1:]  = (Tg[1:] - Tg[:-1]) / dz
    d2Cdz2 = np.zeros_like(C);  d2Tdz2 = np.zeros_like(Tg)
    d2Cdz2[1:-1] = (C[2:] - 2*C[1:-1] + C[:-2]) / dz**2
    d2Tdz2[1:-1] = (Tg[2:] - 2*Tg[1:-1] + Tg[:-2]) / dz**2

    C_star = inverse_langmuir(q, Ts)   # implemented separately
    rate   = k_a * a_p * (C - C_star)

    dCdt = (-u*dCdz + D_ax*d2Cdz2 - rate*(1-eps)) / eps
    dqdt = rate / rho_p
    dTgdt = (-rho_g*c_pg*u*dTdz + lam_ax*d2Tdz2
             + h_f*a_p*(Ts - Tg) + Q_wall(z, t)) / (eps*rho_g*c_pg)
    dTsdt = (h_f*a_p*(Tg - Ts) + dH_ads*rho_p*(1-eps)*dqdt) / ((1-eps)*rho_p*c_ps)

    # Inlet BC (Dirichlet via strong form on i=0)
    dCdt[0] = 0.0;  dTgdt[0] = 0.0
    return np.concatenate([dCdt, dqdt, dTgdt, dTsdt])

# Initial condition: saturated at 400 ppm, ambient; purge starts at t=0
y0 = np.concatenate([np.full(N, 0.0),         # gas-phase C at inlet-purge = 0
                     np.full(N, q_sat_400ppm),
                     np.full(N, 298.15),
                     np.full(N, 298.15)])

sol = solve_ivp(rhs, (0, 1200), y0, method='LSODA',
                rtol=1e-6, atol=1e-9, t_eval=np.linspace(0, 1200, 241))

# The snippet above is a scaffold, not working production code. Expect to spend-
# -Weeks 4–5 turning this into a Gate-A-passing implementation.
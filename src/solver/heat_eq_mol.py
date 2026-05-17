# File: solver/heat_eq_mol.py
# Task: solve ∂T/∂t + u·∂T/∂z = α·∂²T/∂z²
# Step input at z=0, watch it propagate rightward

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

"""
Solves 1-D advection-diffusion PDE (heat equation): ∂T/∂t + u·∂T/∂z = α·∂²T/∂z²

  Setup:
  - 100 grid points over 1 m column
  - Velocity u = 0.05 m/s, diffusivity α = 1e-4 m²/s
  - Step input at z = 0: T_inlet = 1.0 K

  Method of Lines (MOL):
  - Discretize z-axis; integrate t with solve_ivp (LSODA, implicit multistep)
  - Advection (line 22): first-order upwind — (T[i] - T[i-1])/dz
  - Diffusion (line 23): central differences — (T[i+1] - 2T[i] + T[i-1])/dz²
  - Inlet BC (line 25): fix dT/dt[0] = 0 to lock T[0] = T_inlet

  Output:
  Snapshots at t = 0, 2, 5, 8, 10 s. Plots thermal front propagating rightward with dispersion. Save to
  heat_eq_output.png.

  Why this scaffold? Validates upwind + central discretization at low Péclet (Pe = u·L/α = 500). Start for your 4-PDE
  coupling in pde_mol.py.
"""


# Parameters
L = 1.0       # column length [m]
N = 100       # grid points
u = 0.05      # advection velocity [m/s]
alpha = 1e-4  # thermal diffusivity [m²/s]
T_inlet = 1.0 # step input temperature

z = np.linspace(0, L, N) # Gridpoints in the z-direction
dz = z[1] - z[0]

def rhs(t, T):
    dTdt = np.zeros_like(T)
    # Upwind for advection, central for diffusion
    dTdt[1:] += -u * (T[1:] - T[:-1]) / dz
    dTdt[1:-1] += alpha * (T[2:] - 2*T[1:-1] + T[:-2]) / dz**2
    # Inlet BC: fix T[0] = T_inlet
    dTdt[0] = 0.0
    return dTdt

T0 = np.zeros(N)
T0[0] = T_inlet  # initial step at inlet

t_span = (0, 10)
t_eval = np.linspace(0, 10, 50) # Gridpoints in the t-direction

sol = solve_ivp(rhs, t_span, T0, method='LSODA',
                rtol=1e-6, atol=1e-9, t_eval=t_eval)

# Plot
for i in [0, 10, 25, 40, 49]:
    plt.plot(z, sol.y[:, i], label=f't={sol.t[i]:.1f}s')
plt.xlabel('z [m]'); plt.ylabel('T')
plt.title('1-D advection-diffusion: MOL solver')
plt.legend(); plt.tight_layout(); plt.savefig('heat_eq_output.png', dpi=150)
plt.show()
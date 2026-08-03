"""1-D linear-FEM travelling-wave projection of the MTZ.

The travelling-wave solution (Myers 2023, eq. 130)::

    C/C_in = 1 / { 1 + exp[ k_ad · c_in · ( (x - L)/v + (t_{1/2} - t) ) ] }

is projected onto a uniform mesh of ``N`` linear basis functions over
``x ∈ [0, L]``.  Time stepping uses Crank–Nicolson on the upwind
advection equation, but because the exact solution is known and stable
we evaluate it directly at the mesh nodes — the FEM scaffold here is
useful for visualisation and for verifying the solver, not for replacing
the closed-form expression.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import numpy as np


# ---------------------------------------------------------------------------
# Mesh + assembly (kept lightweight; not actually time-stepping in P5)
# ---------------------------------------------------------------------------
@dataclass
class FEMesh:
    n_nodes: int
    L: float
    x: np.ndarray
    dx: float


def build_mesh(L: float, n_nodes: int = 100) -> FEMesh:
    x = np.linspace(0.0, L, n_nodes)
    return FEMesh(n_nodes=n_nodes, L=L, x=x, dx=float(x[1] - x[0]))


# ---------------------------------------------------------------------------
# Travelling-wave evaluation
# ---------------------------------------------------------------------------
def travelling_wave(
    x: np.ndarray,
    t: float,
    L: float,
    v: float,
    k_ad_c_in: float,
    t_half: float,
) -> np.ndarray:
    """Exact travelling-wave profile (Myers 2023, eq. 130)."""
    arg = k_ad_c_in * ((x - L) / max(v, 1e-12) + (t_half - t))
    arg = np.clip(arg, -700.0, 700.0)
    return 1.0 / (1.0 + np.exp(arg))


def project_snapshots(
    L: float,
    v: float,
    k_ad_c_in: float,
    t_half: float,
    t_snapshots: Sequence[float],
    n_nodes: int = 100,
) -> tuple[np.ndarray, np.ndarray]:
    """Return ``(x, C)`` where ``C`` has shape ``(len(t_snapshots), n_nodes)``."""
    mesh = build_mesh(L=L, n_nodes=n_nodes)
    C = np.empty((len(t_snapshots), n_nodes), dtype=float)
    for i, t in enumerate(t_snapshots):
        C[i, :] = travelling_wave(
            mesh.x, float(t), L=L, v=v, k_ad_c_in=k_ad_c_in, t_half=t_half
        )
    return mesh.x, C

"""Column-performance metrics from a single breakthrough curve.

Definitions (Hu et al. 2025, eqs. 72–76 of the compendium):
    t_b     time at C/C0 = 0.05
    t_E     time at C/C0 = 0.95
    t50     time at C/C0 = 0.50
    q_dyn   (ν C0 / m) ∫₀^{t_E} (1 - C/C0) dt           [mol/kg]
    L_MTZ   [1 - (t_E - t_b) / (2 t_E)] · L_bed         [m]
    ψ       t_b / t*,   t* = ∫₀^∞ (1 - C/C0) dt          [-]
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import numpy as np
import pandas as pd


@dataclass
class PerformanceMetrics:
    t_b: float
    t_E: float
    t50: float
    q_dyn_mol_per_kg: float
    L_MTZ_m: float
    efficiency: float
    t_star: float


def _interp_time(t: np.ndarray, y: np.ndarray, level: float) -> float:
    """Return the first ``t`` at which ``y`` crosses ``level``.

    Uses linear interpolation between adjacent samples.
    """
    if y.size == 0:
        return float("nan")
    above = np.where(y >= level)[0]
    if above.size == 0:
        return float("nan")
    i = int(above[0])
    if i == 0:
        return float(t[0])
    y0, y1 = float(y[i - 1]), float(y[i])
    t0, t1 = float(t[i - 1]), float(t[i])
    if y1 == y0:
        return t1
    return float(t0 + (level - y0) * (t1 - t0) / (y1 - y0))


def t_breakthrough(t: np.ndarray, y: np.ndarray, level: float = 0.05) -> float:
    return _interp_time(t, y, level)


def q_dyn_trapz(
    t: np.ndarray,
    y: np.ndarray,
    flow_vol_m3_s: float,
    c0_mol_m3: float,
    mass_kg: float,
    t_E: Optional[float] = None,
) -> float:
    """Integral dynamic capacity by trapezoidal rule.

    The integrand ``1 - C/C0`` is integrated from 0 to ``t_E``; supply ``t_E``
    to truncate (otherwise the full time range is used).
    """
    if mass_kg <= 0 or flow_vol_m3_s <= 0:
        return float("nan")
    t = np.asarray(t, dtype=float)
    y = np.asarray(y, dtype=float)
    if t_E is not None and np.isfinite(t_E):
        mask = t <= t_E
        t_use = t[mask]
        y_use = y[mask]
    else:
        t_use, y_use = t, y
    if t_use.size < 2:
        return float("nan")
    integrand = 1.0 - y_use
    integral = float(np.trapezoid(integrand, t_use))
    return flow_vol_m3_s * c0_mol_m3 * integral / (mass_kg * 1000.0)


def l_mtz(t: np.ndarray, y: np.ndarray, L_bed_m: float) -> float:
    """Mass-transfer-zone length from the breakthrough/saturation pair."""
    tb = _interp_time(t, y, 0.05)
    te = _interp_time(t, y, 0.95)
    if not (np.isfinite(tb) and np.isfinite(te) and te > 0):
        return float("nan")
    return (1.0 - (te - tb) / (2.0 * te)) * L_bed_m


def column_efficiency(t: np.ndarray, y: np.ndarray) -> tuple[float, float]:
    """Return ``(ψ, t*)`` — Stoichiometric efficiency and equilibrium time."""
    t = np.asarray(t, dtype=float)
    y = np.asarray(y, dtype=float)
    if t.size < 2:
        return float("nan"), float("nan")
    t_star = float(np.trapezoid(1.0 - y, t))
    tb = _interp_time(t, y, 0.05)
    if t_star <= 0 or not np.isfinite(tb):
        return float("nan"), t_star
    return tb / t_star, t_star


def metrics(
    t: np.ndarray,
    y: np.ndarray,
    flow_vol_m3_s: float,
    c0_mol_m3: float,
    mass_kg: float,
    L_bed_m: float,
) -> PerformanceMetrics:
    tb = _interp_time(t, y, 0.05)
    te = _interp_time(t, y, 0.95)
    t50 = _interp_time(t, y, 0.5)
    q = q_dyn_trapz(t, y, flow_vol_m3_s, c0_mol_m3, mass_kg, t_E=te)
    L = l_mtz(t, y, L_bed_m)
    eff, t_star = column_efficiency(t, y)
    return PerformanceMetrics(
        t_b=tb, t_E=te, t50=t50, q_dyn_mol_per_kg=q,
        L_MTZ_m=L, efficiency=eff, t_star=t_star,
    )

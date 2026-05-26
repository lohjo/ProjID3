"""Back-calculation of equilibrium loadings and linearised isotherm fits.

Linearised forms (eqs. 11 & 14 of the compendium):
    Langmuir:    1/q_e = 1/q_m + 1/(q_m K_L C_in)
    Freundlich:  log q_e = log K_F + (1/n) log C_e
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import numpy as np


# Universal gas constant (J/mol/K) used for ppm → mol/m³ conversion.
_R = 8.314


def ppm_to_mol_m3(c_ppm: float, T_K: float = 298.0, P_Pa: float = 101_325.0) -> float:
    """Ideal-gas conversion ppm (vol) → mol/m³."""
    return c_ppm * 1e-6 * P_Pa / (_R * T_K)


def back_calculate_q0(
    tau_YN: float,
    flow_vol_m3_s: float,
    c0_mol_m3: float,
    mass_kg: float,
) -> float:
    """Equilibrium loading from the Yoon–Nelson half-time.

    ``q0 = tau · ν · C0 / m``  [mol/kg].
    """
    if mass_kg <= 0 or flow_vol_m3_s <= 0:
        return float("nan")
    return tau_YN * flow_vol_m3_s * c0_mol_m3 / mass_kg


def back_calculate_q0_from_kT(
    k_T: float, flow_vol_m3_s: float, mass_kg: float
) -> float:
    """Thomas form: ``q0 = ν / (k_T · m)``."""
    if k_T <= 0 or mass_kg <= 0:
        return float("nan")
    return flow_vol_m3_s / (k_T * mass_kg)


def back_calculate_a0_from_kBA(
    k_BA: float, c0_mol_m3: float
) -> float:
    """Bohart–Adams capacity: ``a0 = 1 / k_BA``  [mol/m³]."""
    if k_BA <= 0 or c0_mol_m3 <= 0:
        return float("nan")
    return 1.0 / k_BA


@dataclass
class LangmuirFit:
    q_m: float
    K_L: float
    r2: float


def langmuir_linear_fit(
    c_in: np.ndarray, q_e: np.ndarray
) -> LangmuirFit:
    """Linearised Langmuir fit across multiple C_in runs."""
    c_in = np.asarray(c_in, dtype=float)
    q_e = np.asarray(q_e, dtype=float)
    mask = (c_in > 0) & (q_e > 0)
    if mask.sum() < 2:
        return LangmuirFit(np.nan, np.nan, np.nan)
    x = 1.0 / c_in[mask]
    y = 1.0 / q_e[mask]
    slope, intercept = np.polyfit(x, y, 1)
    q_m = 1.0 / intercept
    K_L = intercept / slope
    y_pred = slope * x + intercept
    ss_res = np.sum((y - y_pred) ** 2)
    ss_tot = np.sum((y - y.mean()) ** 2)
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else np.nan
    return LangmuirFit(float(q_m), float(K_L), float(r2))


@dataclass
class FreundlichFit:
    K_F: float
    inv_n: float
    r2: float


def freundlich_log_fit(
    c_e: np.ndarray, q_e: np.ndarray
) -> FreundlichFit:
    """Linearised Freundlich fit across multiple equilibrium points."""
    c_e = np.asarray(c_e, dtype=float)
    q_e = np.asarray(q_e, dtype=float)
    mask = (c_e > 0) & (q_e > 0)
    if mask.sum() < 2:
        return FreundlichFit(np.nan, np.nan, np.nan)
    x = np.log10(c_e[mask])
    y = np.log10(q_e[mask])
    slope, intercept = np.polyfit(x, y, 1)
    K_F = 10.0 ** intercept
    inv_n = slope
    y_pred = slope * x + intercept
    ss_res = np.sum((y - y_pred) ** 2)
    ss_tot = np.sum((y - y.mean()) ** 2)
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else np.nan
    return FreundlichFit(float(K_F), float(inv_n), float(r2))

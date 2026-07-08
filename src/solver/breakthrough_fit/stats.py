"""Goodness-of-fit statistics and nested-model F-tests.

All formulas follow the equation-compendium numbering in the project brief
(eqs. 140–148).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

import numpy as np
from scipy import stats as _scistats


@dataclass
class FitStats:
    """Container for all reported statistics."""

    n: int
    p: int
    rss: float
    tss: float
    r2: float
    adj_r2: float
    rmse: float
    chi2_red: float
    aic: float
    aicc: float
    aad: float
    aic_weight: float = float("nan")  # filled in by ``rank_aicc``


def compute_stats(
    y_obs: np.ndarray,
    y_pred: np.ndarray,
    n_params: int,
    sigma: Optional[np.ndarray] = None,
) -> FitStats:
    """Return all required statistics for one (model, dataset) pair.

    Parameters
    ----------
    y_obs, y_pred
        Observation and prediction arrays of identical shape.
    n_params
        Number of free parameters in the model.
    sigma
        Optional per-point standard deviation; when supplied the reduced
        chi-squared is weighted as ``Σ((y - ŷ)/σ)² / (n - p)``.
    """
    y_obs = np.asarray(y_obs, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)
    # Drop NaNs (implicit-model solver failures) from comparison.
    mask = np.isfinite(y_obs) & np.isfinite(y_pred)
    y_obs = y_obs[mask]
    y_pred = y_pred[mask]
    n = y_obs.size
    if n == 0:
        return FitStats(0, n_params, np.inf, np.inf, np.nan, np.nan, np.inf,
                        np.inf, np.inf, np.inf, np.inf)

    resid = y_obs - y_pred
    rss = float(np.sum(resid ** 2))
    ybar = float(np.mean(y_obs))
    tss = float(np.sum((y_obs - ybar) ** 2))

    r2 = 1.0 - rss / tss if tss > 0 else np.nan
    dof = max(n - n_params, 1)
    adj_r2 = (
        1.0 - (1.0 - r2) * (n - 1) / dof if np.isfinite(r2) else np.nan
    )

    rmse = float(np.sqrt(rss / max(n - 2, 1)))

    if sigma is not None:
        sigma = np.asarray(sigma, dtype=float)[mask]
        chi2 = float(np.sum((resid / np.maximum(sigma, 1e-12)) ** 2))
    else:
        chi2 = rss
    chi2_red = chi2 / dof

    log_term = np.log(max(rss / n, 1e-300))
    aic = n * log_term + 2.0 * n_params
    if n - n_params - 1 > 0:
        aicc = aic + 2.0 * n_params * (n_params + 1) / (n - n_params - 1)
    else:
        aicc = aic + np.inf

    with np.errstate(divide="ignore", invalid="ignore"):
        rel = np.where(np.abs(y_obs) > 1e-6, np.abs(resid / y_obs), 0.0)
    aad = float(np.mean(rel))

    return FitStats(n, n_params, rss, tss, r2, adj_r2, rmse, chi2_red,
                    aic, aicc, aad)


def f_test(rss1: float, rss2: float, df1: int, df2: int) -> float:
    """Nested-model F-test p-value.

    ``rss1, df1`` correspond to the **simpler** model, ``rss2, df2`` to the
    more flexible one (df = n − p, so df2 < df1).  Returns the survival p.
    """
    delta_df = df1 - df2
    if delta_df <= 0 or rss2 <= 0 or df2 <= 0:
        return float("nan")
    f_stat = ((rss1 - rss2) / delta_df) / (rss2 / df2)
    if f_stat <= 0 or not np.isfinite(f_stat):
        return float("nan")
    return float(_scistats.f.sf(f_stat, delta_df, df2))


def rank_aicc(results: dict) -> dict:
    """Populate ``aic_weight`` in-place using ΔAICc against the best model."""
    aiccs = [(name, r.stats.aicc) for name, r in results.items()
             if np.isfinite(r.stats.aicc)]
    if not aiccs:
        return results
    aicc_min = min(a for _, a in aiccs)
    for name, r in results.items():
        if np.isfinite(r.stats.aicc):
            delta = float(r.stats.aicc - aicc_min)
            r.stats.aic_weight = 1.0 / (1.0 + np.exp(min(0.5 * delta, 700.0)))
    return results

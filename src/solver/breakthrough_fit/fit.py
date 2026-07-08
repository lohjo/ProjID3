"""Nonlinear-least-squares fitting with multi-start sampling.

Each model in :mod:`breakthrough_fit.models` is fitted to one parsed run via
:func:`ModelFitter.fit_one`.  The driver :func:`ModelFitter.fit_all` runs
every model in the registry and returns a mapping from model code to
:class:`FitResult`.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

import numpy as np
import pandas as pd
from scipy.optimize import OptimizeWarning, curve_fit, minimize
import warnings

from .models import REGISTRY, BreakthroughModel, get_model
from .stats import FitStats, compute_stats, f_test, rank_aicc


@dataclass
class FitResult:
    """Output of one model fit on one run."""

    code: str
    name: str
    params: np.ndarray
    param_names: tuple[str, ...]
    cov: Optional[np.ndarray]
    stderr: np.ndarray
    stats: FitStats
    converged: bool
    message: str
    y_pred: np.ndarray
    t: np.ndarray
    y_obs: np.ndarray
    extras: dict = field(default_factory=dict)


class ModelFitter:
    """Multi-start fitter for breakthrough models."""

    def __init__(
        self,
        n_starts: int = 10,
        seed: int = 42,
        registry: tuple[BreakthroughModel, ...] = REGISTRY,
        extra_kwargs: Optional[dict[str, dict]] = None,
    ):
        self.n_starts = n_starts
        self.seed = seed
        self.registry = registry
        self.extra_kwargs = extra_kwargs or {}

    # ------------------------------------------------------------------ #
    # Driver
    # ------------------------------------------------------------------ #
    def fit_all(
        self,
        df: pd.DataFrame,
        progress: Optional[callable] = None,
    ) -> dict[str, FitResult]:
        """Fit every model to ``df`` (columns ``t`` and ``C_C0``)."""
        t = df["t"].to_numpy(dtype=float)
        y = df["C_C0"].to_numpy(dtype=float)
        results: dict[str, FitResult] = {}
        iterator = self.registry
        if progress is not None:
            iterator = progress(iterator)
        for model in iterator:
            try:
                res = self.fit_one(model, t, y)
            except Exception as exc:  # noqa: BLE001
                res = self._failed(model, t, y, str(exc))
            results[model.code] = res
        rank_aicc(results)
        return results

    # ------------------------------------------------------------------ #
    # Single-model fit
    # ------------------------------------------------------------------ #
    def fit_one(
        self,
        model: BreakthroughModel,
        t: np.ndarray,
        y: np.ndarray,
    ) -> FitResult:
        rng = np.random.default_rng(self.seed)

        # Filter early-region for Wolborska.
        if model.early_only:
            mask = (y > 0.005) & (y <= 0.15)
            if mask.sum() < 3:
                return self._failed(model, t, y, "insufficient early-region points")
            t_fit, y_fit = t[mask], y[mask]
        else:
            t_fit, y_fit = t, y

        kwargs = self.extra_kwargs.get(model.code, {})

        def f(t_in: np.ndarray, *params: float) -> np.ndarray:
            return model.func(t_in, *params, **kwargs)

        bounds_lo = np.array([b[0] for b in model.bounds])
        bounds_hi = np.array([b[1] for b in model.bounds])
        bounds = (bounds_lo, bounds_hi)

        # Seed with the data-driven guess plus N random starts inside bounds.
        starts = [np.array(model.init_strategy(t_fit, y_fit), dtype=float)]
        for _ in range(self.n_starts - 1):
            sample = rng.uniform(bounds_lo, bounds_hi)
            starts.append(sample)

        best_params = None
        best_cov = None
        best_rss = np.inf
        best_msg = "no successful fit"
        for s0 in starts:
            s0_clipped = np.clip(s0, bounds_lo, bounds_hi)
            try:
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore", OptimizeWarning)
                    warnings.simplefilter("ignore", RuntimeWarning)
                    if model.needs_implicit:
                        # Use L-BFGS-B on RSS (curve_fit chokes on NaNs).
                        params, cov, rss = self._minimize(
                            f, t_fit, y_fit, s0_clipped, bounds_lo, bounds_hi
                        )
                    else:
                        params, cov = curve_fit(
                            f,
                            t_fit,
                            y_fit,
                            p0=s0_clipped,
                            bounds=bounds,
                            maxfev=5000,
                        )
                        rss = float(np.sum((y_fit - f(t_fit, *params)) ** 2))
            except Exception as exc:  # noqa: BLE001
                best_msg = str(exc)
                continue

            if np.isfinite(rss) and rss < best_rss:
                best_rss = rss
                best_params = params
                best_cov = cov
                best_msg = "converged"

        if best_params is None:
            return self._failed(model, t, y, best_msg)

        y_pred_full = f(t, *best_params)
        if model.early_only:
            mask_eval = (y > 0.005) & (y <= 0.15)
            if mask_eval.sum() >= 3:
                stats = compute_stats(y[mask_eval], y_pred_full[mask_eval], model.p)
            else:
                stats = compute_stats(y, y_pred_full, model.p)
        else:
            stats = compute_stats(y, y_pred_full, model.p)
        if best_cov is not None and np.all(np.isfinite(best_cov)):
            stderr = np.sqrt(np.clip(np.diag(best_cov), 0.0, None))
        else:
            stderr = np.full_like(best_params, np.nan, dtype=float)

        return FitResult(
            code=model.code,
            name=model.name,
            params=np.asarray(best_params, dtype=float),
            param_names=model.param_names,
            cov=best_cov,
            stderr=stderr,
            stats=stats,
            converged=True,
            message=best_msg,
            y_pred=y_pred_full,
            t=t,
            y_obs=y,
            extras={"early_only": model.early_only, "kwargs": kwargs},
        )

    # ------------------------------------------------------------------ #
    # Helpers
    # ------------------------------------------------------------------ #
    @staticmethod
    def _minimize(f, t, y, x0, lo, hi):
        """L-BFGS-B fallback for implicit / NaN-prone models."""

        def rss_fn(theta: np.ndarray) -> float:
            try:
                pred = f(t, *theta)
            except Exception:  # noqa: BLE001
                return 1e12
            mask = np.isfinite(pred)
            if mask.sum() < 3:
                return 1e12
            return float(np.sum((y[mask] - pred[mask]) ** 2))

        res = minimize(
            rss_fn,
            x0,
            method="L-BFGS-B",
            bounds=list(zip(lo, hi)),
            options={"maxiter": 200, "ftol": 1e-9},
        )
        # Approximate covariance via numerical Hessian (skip if singular).
        cov = None
        try:
            from scipy.optimize import approx_fprime

            eps = 1e-4 * np.maximum(np.abs(res.x), 1.0)
            n = len(res.x)
            H = np.zeros((n, n))
            grad0 = approx_fprime(res.x, rss_fn, eps)
            for i in range(n):
                xp = res.x.copy()
                xp[i] += eps[i]
                grad_i = approx_fprime(xp, rss_fn, eps)
                H[:, i] = (grad_i - grad0) / eps[i]
            H = 0.5 * (H + H.T)
            cov = np.linalg.pinv(H) * (2.0 * res.fun / max(len(y) - n, 1))
        except Exception:  # noqa: BLE001
            cov = None
        return res.x, cov, float(res.fun)

    @staticmethod
    def _failed(
        model: BreakthroughModel, t: np.ndarray, y: np.ndarray, msg: str
    ) -> FitResult:
        stats = FitStats(
            n=int(np.size(y)),
            p=model.p,
            rss=np.inf,
            tss=np.inf,
            r2=np.nan,
            adj_r2=np.nan,
            rmse=np.inf,
            chi2_red=np.inf,
            aic=np.inf,
            aicc=np.inf,
            aad=np.inf,
        )
        return FitResult(
            code=model.code,
            name=model.name,
            params=np.array([np.nan] * model.p),
            param_names=model.param_names,
            cov=None,
            stderr=np.array([np.nan] * model.p),
            stats=stats,
            converged=False,
            message=msg,
            y_pred=np.full_like(y, np.nan, dtype=float),
            t=t,
            y_obs=y,
        )


# ---------------------------------------------------------------------------
# Convenience F-test grid
# ---------------------------------------------------------------------------
NESTED_PAIRS: tuple[tuple[str, str], ...] = (
    ("M01", "M02"),   # logistic vs Clark (adds n)
    ("M01", "M04"),   # logistic vs dose-response asymmetry
    ("M01", "M23"),   # logistic vs fractal YN (adds h)
    ("M02", "M03"),   # Clark vs fractal Clark (adds h)
    ("M07", "M11"),   # erf vs fractal erf (adds h)
    ("M06", "M10"),   # gudermannian vs fractal gudermannian (adds h)
)


def nested_ftests(results: dict[str, FitResult], n: int) -> pd.DataFrame:
    rows: list[dict] = []
    for simple, complex_ in NESTED_PAIRS:
        if simple not in results or complex_ not in results:
            continue
        r1, r2 = results[simple], results[complex_]
        if not (r1.converged and r2.converged):
            continue
        df1 = max(n - r1.stats.p, 1)
        df2 = max(n - r2.stats.p, 1)
        p = f_test(r1.stats.rss, r2.stats.rss, df1, df2)
        rows.append({
            "simple": simple,
            "complex": complex_,
            "rss_simple": r1.stats.rss,
            "rss_complex": r2.stats.rss,
            "df_simple": df1,
            "df_complex": df2,
            "p_value": p,
        })
    return pd.DataFrame(rows)

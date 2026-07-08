"""Closed-form breakthrough models M01–M24.

Each model is exposed both as a plain callable ``model_XXX(t, *params)`` that
returns ``C/C0`` and as a :class:`BreakthroughModel` instance carrying its
parameter names, bounds, and initial-guess strategy.  The package fitter
(``fit.py``) consumes the :class:`BreakthroughModel` registry directly.

Conventions
-----------
* ``t``  — time in seconds (numpy array).
* All models return values in [0, 1] (saturating sigmoids) except where noted.
* Parameter names use ASCII identifiers without subscripts so they survive
  CSV round-trips (e.g. ``k_YN``, ``tau``, ``alpha_G``).

References cited inline correspond to the manifest in the project brief.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Optional, Sequence

import numpy as np
from scipy.optimize import brentq
from scipy.special import erf


# ---------------------------------------------------------------------------
# Numeric helpers
# ---------------------------------------------------------------------------
_EPS = 1e-300
_LOG_CLIP = 700.0  # ``exp`` overflow guard for double-precision floats.


def _sigmoid(x: np.ndarray) -> np.ndarray:
    """Numerically stable logistic ``1 / (1 + exp(x))``."""
    x = np.clip(x, -_LOG_CLIP, _LOG_CLIP)
    return np.where(x >= 0, np.exp(-x) / (1.0 + np.exp(-x)), 1.0 / (1.0 + np.exp(x)))


def _safe_pow(a: np.ndarray | float, b: float) -> np.ndarray | float:
    """Power with non-negative base, returning 0 for negative bases."""
    a = np.asarray(a, dtype=float)
    out = np.zeros_like(a, dtype=float)
    pos = a > 0
    out[pos] = np.power(a[pos], b)
    return out


# ---------------------------------------------------------------------------
# Group I — Logistic family (Yoon–Nelson / Bohart–Adams / Thomas)
# ---------------------------------------------------------------------------
def model_M01(t: np.ndarray, k_YN: float, tau: float) -> np.ndarray:
    """Yoon–Nelson / unified logistic.

    ``C/C0 = 1 / (1 + exp[k_YN (tau - t)])``.
    """
    return _sigmoid(k_YN * (tau - t))


# ---------------------------------------------------------------------------
# Group II — Clark
# ---------------------------------------------------------------------------
def model_M02(t: np.ndarray, r: float, A: float, n: float) -> np.ndarray:
    """Clark model with generalised-Freundlich isotherm exponent ``n``."""
    expo = np.clip(-r * t, -_LOG_CLIP, _LOG_CLIP)
    inner = 1.0 / (1.0 + A * np.exp(expo))
    inner = np.clip(inner, _EPS, 1.0)
    return _safe_pow(inner, 1.0 / (n - 1.0))


def model_M03(
    t: np.ndarray, r: float, A0: float, n: float, h: float
) -> np.ndarray:
    """Fractal-like Clark (Hu 2024).

    Uses the regularised time variable ``t^{1-h}`` to capture sub-diffusive
    front spreading.  ``h = 0`` collapses to :func:`model_M02`.
    """
    t = np.maximum(t, 1.0)  # avoid t=0 singularity in t^{1-h}
    exponent = -r / (1.0 - h) * np.power(t, 1.0 - h)
    exponent = np.clip(exponent, -_LOG_CLIP, _LOG_CLIP)
    inner = 1.0 / (1.0 + A0 * np.exp(exponent))
    inner = np.clip(inner, _EPS, 1.0)
    return _safe_pow(inner, 1.0 / (n - 1.0))


# ---------------------------------------------------------------------------
# Group III — Modified Dose–Response (Yan et al.)
# ---------------------------------------------------------------------------
def model_M04(t: np.ndarray, a: float, t50: float) -> np.ndarray:
    """Modified dose–response form parameterised on the half-time ``t50``."""
    t = np.maximum(t, _EPS)
    ratio = _safe_pow(t / t50, a)
    return 1.0 - 1.0 / (1.0 + ratio)


# ---------------------------------------------------------------------------
# Group IV — Wolborska (linearised, only fitted on C/C0 ≤ 0.15)
# ---------------------------------------------------------------------------
def model_M05(t: np.ndarray, slope: float, intercept: float) -> np.ndarray:
    """Wolborska in linearised form.

    Returns ``C/C0`` from ``ln(C/C0) = slope*t + intercept`` so the same model
    interface (returning ``C/C0``) is preserved for plotting.  The fitter
    restricts ``t`` to the early-breakthrough window.
    """
    val = slope * t + intercept
    val = np.clip(val, -_LOG_CLIP, 0.0)  # cap at C/C0 = 1
    return np.exp(val)


# ---------------------------------------------------------------------------
# Group V — Gudermannian / Error-Function / Tanh / Log-Normal
# ---------------------------------------------------------------------------
def model_M06(t: np.ndarray, k: float, tau: float) -> np.ndarray:
    arg = k * (t - tau)
    return 0.5 * (1.0 + (2.0 / np.pi) * np.arctan(np.sinh(arg)))


def model_M07(t: np.ndarray, k: float, tau: float) -> np.ndarray:
    return 0.5 * (1.0 + erf(k * (t - tau)))


def model_M08(t: np.ndarray, k: float, tau: float) -> np.ndarray:
    return 0.5 * (1.0 + np.tanh(k * (t - tau)))


def model_M09(t: np.ndarray, a: float, b: float) -> np.ndarray:
    """Chu–Hashim log-normal breakthrough."""
    t = np.maximum(t, _EPS)
    z = (np.log(t) - b) / (np.sqrt(2.0) * a)
    return 0.5 * (1.0 + erf(z))


def model_M10(
    t: np.ndarray, k0: float, tau0: float, h: float
) -> np.ndarray:
    """Fractal-like Gudermannian (Hu 2024)."""
    t = np.maximum(t, 1.0)
    arg = k0 * np.power(t, -h) * (t - tau0)
    return 0.5 * (1.0 + (2.0 / np.pi) * np.arctan(np.sinh(arg)))


def model_M11(
    t: np.ndarray, k0: float, tau0: float, h: float
) -> np.ndarray:
    """Fractal-like error-function (Hu 2024)."""
    t = np.maximum(t, 1.0)
    arg = k0 * np.power(t, -h) * (t - tau0)
    return 0.5 * (1.0 + erf(arg))


# ---------------------------------------------------------------------------
# Group VI — Gompertz family
# ---------------------------------------------------------------------------
def model_M12(t: np.ndarray, alpha_G: float, beta_G: float) -> np.ndarray:
    inner = np.clip(alpha_G - beta_G * t, -_LOG_CLIP, _LOG_CLIP)
    return np.exp(-np.exp(inner))


def model_M13(t: np.ndarray, alpha_G: float, beta_G: float) -> np.ndarray:
    t = np.maximum(t, _EPS)
    inner = np.clip(alpha_G - beta_G * np.log(t), -_LOG_CLIP, _LOG_CLIP)
    return np.exp(-np.exp(inner))


# ---------------------------------------------------------------------------
# Group VII — Weibull & Avrami
# ---------------------------------------------------------------------------
def model_M14(t: np.ndarray, tau: float, k: float) -> np.ndarray:
    t = np.maximum(t, 0.0)
    val = np.clip(_safe_pow(t / tau, k), 0.0, _LOG_CLIP)
    return 1.0 - np.exp(-val)


def weibull_derivative(t: np.ndarray, tau: float, k: float) -> np.ndarray:
    """First derivative ``d(C/C0)/dt`` of the Weibull curve."""
    t = np.maximum(t, _EPS)
    a = k / tau * _safe_pow(t / tau, k - 1.0)
    b = np.exp(-_safe_pow(t / tau, k))
    return a * b


def model_M15(t: np.ndarray, k: float, n: float) -> np.ndarray:
    t = np.maximum(t, 0.0)
    val = np.clip(k * _safe_pow(t, n), 0.0, _LOG_CLIP)
    return 1.0 - np.exp(-val)


# ---------------------------------------------------------------------------
# Group VIII — Klinkenberg / Dima
# ---------------------------------------------------------------------------
def model_M16(
    t: np.ndarray,
    K_fa: float,
    K: float,
    eps_b: float = 0.37,
    u_over_x: float = 1.0,
) -> np.ndarray:
    """Klinkenberg solution.

    Reduces to the canonical error-function form using the dimensionless time
    ``tau_K = K_fa / (K (1 - eps_b)) * (t - eps_b / u_over_x)`` and bed
    Stanton number ``zeta = K_fa / u_over_x``.  When ``u`` or ``x`` are
    unknown, the fitter passes ``u_over_x = 1`` and ``K_fa`` absorbs the
    geometric factor.
    """
    zeta = K_fa / max(u_over_x, _EPS)
    t_corr = np.maximum(t - eps_b / max(u_over_x, _EPS), _EPS)
    tau_K = np.maximum(K_fa / max(K * (1.0 - eps_b), _EPS) * t_corr, _EPS)
    arg = (
        np.sqrt(tau_K)
        - np.sqrt(zeta)
        + 1.0 / (8.0 * np.sqrt(tau_K))
        + 1.0 / (8.0 * np.sqrt(zeta))
    )
    return 0.5 * (1.0 + erf(arg))


def model_M17(
    t: np.ndarray, v_d: float, sigma_a: float, x: float = 1.0
) -> np.ndarray:
    """Dima travelling-wave error-function."""
    arg = (v_d * t - x) / max(np.sqrt(2.0) * sigma_a, _EPS)
    return 0.5 * (1.0 + erf(arg))


# ---------------------------------------------------------------------------
# Group IX — Chern–Chien (implicit, isotherm-embedded)
# ---------------------------------------------------------------------------
def _chern_chien_langmuir_t_of_x(
    x: float, K_fa: float, K_L: float, q0: float, t12: float,
    eps: float = 0.37, rho_b: float = 700.0, C0: float = 1.0,
) -> float:
    """Forward map t(x) for Chern–Chien Langmuir."""
    x = float(min(max(x, 1e-6), 1.0 - 1e-6))
    coeff = eps / max(K_fa * rho_b * q0 * C0, _EPS)
    term1 = np.log(2.0 * x / (1.0 - x))
    term2 = (1.0 / max(K_L * C0, _EPS)) * np.log(1.0 / (2.0 * (1.0 - x)))
    return t12 + coeff * (term1 + term2)


def model_M18(
    t: np.ndarray,
    K_fa: float,
    K_L: float,
    q0: float,
    t12: float,
    eps: float = 0.37,
    rho_b: float = 700.0,
    C0: float = 1.0,
) -> np.ndarray:
    """Chern–Chien Langmuir solved implicitly at each ``t``."""
    out = np.empty_like(t, dtype=float)

    def residual(x: float, t_target: float) -> float:
        return (
            _chern_chien_langmuir_t_of_x(x, K_fa, K_L, q0, t12, eps, rho_b, C0)
            - t_target
        )

    for i, ti in enumerate(t):
        try:
            out[i] = brentq(residual, 1e-6, 1.0 - 1e-6, args=(float(ti),))
        except (ValueError, RuntimeError):
            out[i] = np.nan
    return out


def _chern_chien_freundlich_t_of_x(
    x: float,
    K_fa: float,
    n: float,
    q0: float,
    t12: float,
    eps: float = 0.37,
    rho_b: float = 700.0,
    C0: float = 1.0,
) -> float:
    x = float(min(max(x, 1e-6), 1.0 - 1e-6))
    coeff = eps / max(K_fa * rho_b * q0 * C0, _EPS)
    term1 = np.log(2.0 * x / (1.0 - x))
    # ``(1 - x^{n-1}) / 2^{1-n}`` — guard against negative argument near x≈1.
    inner = (1.0 - x ** (n - 1.0)) / max(2.0 ** (1.0 - n), _EPS)
    term2 = -(1.0 / max(n - 1.0, _EPS)) * np.log(max(inner, _EPS))
    return t12 + coeff * (term1 + term2)


def model_M19(
    t: np.ndarray,
    K_fa: float,
    n: float,
    q0: float,
    t12: float,
    eps: float = 0.37,
    rho_b: float = 700.0,
    C0: float = 1.0,
) -> np.ndarray:
    out = np.empty_like(t, dtype=float)

    def residual(x: float, t_target: float) -> float:
        return (
            _chern_chien_freundlich_t_of_x(
                x, K_fa, n, q0, t12, eps, rho_b, C0
            )
            - t_target
        )

    for i, ti in enumerate(t):
        try:
            out[i] = brentq(residual, 1e-6, 1.0 - 1e-6, args=(float(ti),))
        except (ValueError, RuntimeError):
            out[i] = np.nan
    return out


# ---------------------------------------------------------------------------
# Group X — Log-modified logistic variants
# ---------------------------------------------------------------------------
def model_M20(
    t: np.ndarray, k_BA: float, log_a0_over_C0: float
) -> np.ndarray:
    """Log-modified Bohart–Adams (Apiratikul & Chu).

    The combined geometric/inlet term ``log(a0 x / (u C0))`` is fitted as a
    single intercept ``log_a0_over_C0`` so the model stays linear in the
    logarithm of time.
    """
    t = np.maximum(t, _EPS)
    arg = k_BA * (log_a0_over_C0 - np.log(t))
    return _sigmoid(arg)


def model_M21(
    t: np.ndarray, k_YN: float, tau: float
) -> np.ndarray:
    """Log-modified Yoon–Nelson (Apiratikul & Chu)."""
    t = np.maximum(t, _EPS)
    tau = max(tau, _EPS)
    arg = k_YN * (np.log(tau) - np.log(t))
    return _sigmoid(arg)


# ---------------------------------------------------------------------------
# Group XI — n-Order Bohart–Adams (Hu 2021)
# ---------------------------------------------------------------------------
def model_M22(
    t: np.ndarray,
    k_n: float,
    a0: float,
    n: float,
    x_over_u: float = 1.0,
    C0: float = 1.0,
) -> np.ndarray:
    """Generalised n-order Bohart–Adams.

    For numerical robustness we evaluate the ratio inside the bracket on a
    log scale.  ``n = 1`` recovers the standard BA logistic.
    """
    n1 = n - 1.0
    if abs(n1) < 1e-3:
        # Fall back to BA logistic in the n→1 limit.
        return model_M01(t, k_n, x_over_u / max(k_n, _EPS))
    num = 1.0 + n1 * k_n * (a0 ** n1) * (C0 ** n1) * x_over_u
    den = 1.0 + n1 * k_n * (a0 ** n1) * (C0 ** n) * np.maximum(t, _EPS)
    ratio = np.where(den > 0, num / den, _EPS)
    bracket = (
        n * (a0 ** (1.0 - n)) * (C0 ** n1) * _safe_pow(ratio, 1.0 / n1)
        - n * (a0 ** (1.0 - n)) * (C0 ** n1)
    )
    bracket = np.where(bracket > 0, bracket, _EPS)
    return np.clip(_safe_pow(bracket, -1.0 / n), 0.0, 1.0)


# ---------------------------------------------------------------------------
# Group XII — Fractal-like Yoon–Nelson
# ---------------------------------------------------------------------------
def model_M23(
    t: np.ndarray, k_YN0: float, tau: float, h: float
) -> np.ndarray:
    """Fractal-like YN.  Recovers M01 when ``h = 0``."""
    t = np.maximum(t, 1.0)
    tau = max(tau, 1.0)
    one_minus_h = max(1.0 - h, 1e-3)
    arg = (k_YN0 / one_minus_h) * (tau ** one_minus_h - np.power(t, one_minus_h))
    return _sigmoid(arg)


# ---------------------------------------------------------------------------
# Group XIII — Parallel sigmoidal (Blagojev et al.)
# ---------------------------------------------------------------------------
def model_M24(
    t: np.ndarray,
    p: float,
    tau1: float,
    k1: float,
    tau2: float,
    k2: float,
) -> np.ndarray:
    t = np.maximum(t, _EPS)
    p = float(np.clip(p, 0.0, 1.0))
    comp1 = 1.0 - 1.0 / (1.0 + _safe_pow(t / max(tau1, _EPS), k1))
    comp2 = 1.0 - 1.0 / (1.0 + _safe_pow(t / max(tau2, _EPS), k2))
    return p * comp1 + (1.0 - p) * comp2


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------
@dataclass
class BreakthroughModel:
    """Static descriptor for one breakthrough model."""

    code: str
    name: str
    func: Callable[..., np.ndarray]
    param_names: tuple[str, ...]
    bounds: tuple[tuple[float, float], ...]
    init_strategy: Callable[[np.ndarray, np.ndarray], tuple[float, ...]]
    group: str
    notes: str = ""
    early_only: bool = False  # restrict fit to C/C0 ≤ 0.15
    needs_implicit: bool = False
    extra_kwargs: dict = field(default_factory=dict)

    @property
    def p(self) -> int:
        return len(self.param_names)


def _t50_estimate(t: np.ndarray, y: np.ndarray) -> float:
    """Return the time at which ``C/C0`` first crosses 0.5 (else t.max()/2)."""
    if y.size == 0:
        return 1.0
    target = 0.5
    mask = y >= target
    if mask.any():
        idx = int(np.argmax(mask))
        if idx == 0:
            return float(max(t.min() + 1.0, 1.0))
        # Linear interpolation between idx-1 and idx.
        y0, y1 = float(y[idx - 1]), float(y[idx])
        t0, t1 = float(t[idx - 1]), float(t[idx])
        if y1 == y0:
            return t1
        return float(t0 + (target - y0) * (t1 - t0) / (y1 - y0))
    return float(max(t.max() / 2.0, 1.0))


def _t_at(t: np.ndarray, y: np.ndarray, level: float) -> float:
    mask = y >= level
    if not mask.any():
        return float(t.max())
    return float(t[int(np.argmax(mask))])


# ---------------------------------------------------------------------------
# Initial-guess strategies (each maps (t, y) → tuple of guesses).
# ---------------------------------------------------------------------------
def _init_M01(t, y):
    t50 = _t50_estimate(t, y)
    t05 = _t_at(t, y, 0.05)
    t95 = _t_at(t, y, 0.95)
    width = max(t95 - t05, 1.0)
    k = 4.0 / width
    return (k, t50)


def _init_M02(t, y):
    t50 = _t50_estimate(t, y)
    return (4.0 / max(t50, 1.0), 1.0, 2.0)


def _init_M03(t, y):
    t50 = _t50_estimate(t, y)
    return (4.0 / max(t50, 1.0), 1.0, 2.0, 0.1)


def _init_M04(t, y):
    return (2.0, _t50_estimate(t, y))


def _init_M05(t, y):
    # Linear regression on early-breakthrough log slope.
    mask = (y > 0.005) & (y <= 0.15)
    if mask.sum() < 2:
        return (1e-3, -5.0)
    slope, intercept = np.polyfit(t[mask], np.log(y[mask]), 1)
    return (float(slope), float(intercept))


def _init_M06(t, y):
    return _init_M01(t, y)


def _init_M07(t, y):
    t50 = _t50_estimate(t, y)
    t05 = _t_at(t, y, 0.05)
    t95 = _t_at(t, y, 0.95)
    width = max(t95 - t05, 1.0)
    return (2.0 / width, t50)


def _init_M08(t, y):
    return _init_M01(t, y)


def _init_M09(t, y):
    t50 = max(_t50_estimate(t, y), 1.0)
    return (0.3, float(np.log(t50)))


def _init_M10(t, y):
    return (_init_M06(t, y)[0], _init_M06(t, y)[1], 0.1)


def _init_M11(t, y):
    return (_init_M07(t, y)[0], _init_M07(t, y)[1], 0.1)


def _init_M12(t, y):
    t50 = _t50_estimate(t, y)
    return (5.0, 5.0 / max(t50, 1.0))


def _init_M13(t, y):
    t50 = _t50_estimate(t, y)
    return (5.0, 5.0 / max(np.log(max(t50, 2.0)), 1.0))


def _init_M14(t, y):
    return (_t50_estimate(t, y) / (np.log(2.0) ** (1.0 / 1.5)), 1.5)


def _init_M15(t, y):
    t50 = _t50_estimate(t, y)
    n = 1.5
    return (np.log(2.0) / max(t50 ** n, _EPS), n)


def _init_M16(t, y):
    t50 = _t50_estimate(t, y)
    return (4.0 / max(t50, 1.0), 1.0)


def _init_M17(t, y):
    t50 = _t50_estimate(t, y)
    return (1.0 / max(t50, 1.0), max(t50 / 4.0, 1.0))


def _init_M18(t, y):
    t50 = _t50_estimate(t, y)
    return (4.0 / max(t50, 1.0), 1.0, 1.0, t50)


def _init_M19(t, y):
    t50 = _t50_estimate(t, y)
    return (4.0 / max(t50, 1.0), 2.0, 1.0, t50)


def _init_M20(t, y):
    t50 = max(_t50_estimate(t, y), 1.0)
    return (4.0, float(np.log(t50)))


def _init_M21(t, y):
    return (4.0, _t50_estimate(t, y))


def _init_M22(t, y):
    return (1e-3, 1.0, 1.5)


def _init_M23(t, y):
    return (4.0 / max(_t50_estimate(t, y), 1.0), _t50_estimate(t, y), 0.1)


def _init_M24(t, y):
    t50 = _t50_estimate(t, y)
    return (0.5, max(t50 * 0.7, 1.0), 2.0, max(t50 * 1.3, 1.0), 2.0)


REGISTRY: tuple[BreakthroughModel, ...] = (
    BreakthroughModel(
        code="M01",
        name="Yoon-Nelson / Thomas / BA (logistic)",
        func=model_M01,
        param_names=("k_YN", "tau"),
        bounds=((1e-6, 1.0), (1.0, 1e6)),
        init_strategy=_init_M01,
        group="Logistic",
    ),
    BreakthroughModel(
        code="M02",
        name="Clark",
        func=model_M02,
        param_names=("r", "A", "n"),
        bounds=((1e-6, 1.0), (1e-6, 1e6), (1.01, 10.0)),
        init_strategy=_init_M02,
        group="Clark",
    ),
    BreakthroughModel(
        code="M03",
        name="Fractal Clark",
        func=model_M03,
        param_names=("r", "A0", "n", "h"),
        bounds=((1e-6, 1.0), (1e-6, 1e6), (1.01, 10.0), (0.0, 0.99)),
        init_strategy=_init_M03,
        group="Clark",
    ),
    BreakthroughModel(
        code="M04",
        name="Modified Dose-Response (Yan)",
        func=model_M04,
        param_names=("a", "t50"),
        bounds=((0.01, 20.0), (1.0, 1e6)),
        init_strategy=_init_M04,
        group="Dose-Response",
    ),
    BreakthroughModel(
        code="M05",
        name="Wolborska (linearised, early)",
        func=model_M05,
        param_names=("slope", "intercept"),
        bounds=((1e-6, 1.0), (-50.0, 0.0)),
        init_strategy=_init_M05,
        group="Wolborska",
        early_only=True,
    ),
    BreakthroughModel(
        code="M06",
        name="Gudermannian (Hu 2021)",
        func=model_M06,
        param_names=("k", "tau"),
        bounds=((1e-6, 1.0), (1.0, 1e6)),
        init_strategy=_init_M06,
        group="ErfFamily",
    ),
    BreakthroughModel(
        code="M07",
        name="Error-Function (Hu 2021)",
        func=model_M07,
        param_names=("k", "tau"),
        bounds=((1e-6, 1.0), (1.0, 1e6)),
        init_strategy=_init_M07,
        group="ErfFamily",
    ),
    BreakthroughModel(
        code="M08",
        name="Tanh (Hu 2019)",
        func=model_M08,
        param_names=("k", "tau"),
        bounds=((1e-6, 1.0), (1.0, 1e6)),
        init_strategy=_init_M08,
        group="ErfFamily",
    ),
    BreakthroughModel(
        code="M09",
        name="Log-Normal (Chu-Hashim)",
        func=model_M09,
        param_names=("a", "b"),
        bounds=((1e-3, 5.0), (-5.0, 20.0)),
        init_strategy=_init_M09,
        group="ErfFamily",
    ),
    BreakthroughModel(
        code="M10",
        name="Fractal Gudermannian (Hu 2024)",
        func=model_M10,
        param_names=("k0", "tau0", "h"),
        bounds=((1e-6, 1.0), (1.0, 1e6), (0.0, 0.99)),
        init_strategy=_init_M10,
        group="ErfFamily",
    ),
    BreakthroughModel(
        code="M11",
        name="Fractal Error-Function (Hu 2024)",
        func=model_M11,
        param_names=("k0", "tau0", "h"),
        bounds=((1e-6, 1.0), (1.0, 1e6), (0.0, 0.99)),
        init_strategy=_init_M11,
        group="ErfFamily",
    ),
    BreakthroughModel(
        code="M12",
        name="Gompertz (Chu 2020)",
        func=model_M12,
        param_names=("alpha_G", "beta_G"),
        bounds=((-20.0, 20.0), (1e-6, 1.0)),
        init_strategy=_init_M12,
        group="Gompertz",
    ),
    BreakthroughModel(
        code="M13",
        name="Log-Gompertz (Chu 2020)",
        func=model_M13,
        param_names=("alpha_G", "beta_G"),
        bounds=((-50.0, 50.0), (1e-3, 50.0)),
        init_strategy=_init_M13,
        group="Gompertz",
    ),
    BreakthroughModel(
        code="M14",
        name="Weibull (Chu 2021)",
        func=model_M14,
        param_names=("tau", "k"),
        bounds=((1.0, 1e6), (0.1, 10.0)),
        init_strategy=_init_M14,
        group="Weibull",
    ),
    BreakthroughModel(
        code="M15",
        name="Avrami (Singh)",
        func=model_M15,
        param_names=("k", "n"),
        bounds=((1e-12, 10.0), (0.1, 10.0)),
        init_strategy=_init_M15,
        group="Weibull",
    ),
    BreakthroughModel(
        code="M16",
        name="Klinkenberg",
        func=model_M16,
        param_names=("K_fa", "K"),
        bounds=((1e-6, 1.0), (1e-3, 1e4)),
        init_strategy=_init_M16,
        group="Physics",
    ),
    BreakthroughModel(
        code="M17",
        name="Dima (wave erf)",
        func=model_M17,
        param_names=("v_d", "sigma_a"),
        bounds=((1e-6, 1.0), (1e-3, 1e4)),
        init_strategy=_init_M17,
        group="Physics",
    ),
    BreakthroughModel(
        code="M18",
        name="Chern-Chien Langmuir",
        func=model_M18,
        param_names=("K_fa", "K_L", "q0", "t12"),
        bounds=((1e-6, 1.0), (1e-6, 1e4), (1e-3, 50.0), (1.0, 1e6)),
        init_strategy=_init_M18,
        group="ChernChien",
        needs_implicit=True,
    ),
    BreakthroughModel(
        code="M19",
        name="Chern-Chien Freundlich",
        func=model_M19,
        param_names=("K_fa", "n", "q0", "t12"),
        bounds=((1e-6, 1.0), (1.05, 10.0), (1e-3, 50.0), (1.0, 1e6)),
        init_strategy=_init_M19,
        group="ChernChien",
        needs_implicit=True,
    ),
    BreakthroughModel(
        code="M20",
        name="Log-modified Bohart-Adams",
        func=model_M20,
        param_names=("k_BA", "log_a0_C0"),
        bounds=((0.1, 50.0), (-5.0, 20.0)),
        init_strategy=_init_M20,
        group="LogLogistic",
    ),
    BreakthroughModel(
        code="M21",
        name="Log-modified Yoon-Nelson",
        func=model_M21,
        param_names=("k_YN", "tau"),
        bounds=((0.1, 50.0), (1.0, 1e6)),
        init_strategy=_init_M21,
        group="LogLogistic",
    ),
    BreakthroughModel(
        code="M22",
        name="n-Order Bohart-Adams",
        func=model_M22,
        param_names=("k_n", "a0", "n"),
        bounds=((1e-8, 1.0), (1e-3, 1e4), (1.01, 5.0)),
        init_strategy=_init_M22,
        group="LogLogistic",
    ),
    BreakthroughModel(
        code="M23",
        name="Fractal Yoon-Nelson (Hu 2024)",
        func=model_M23,
        param_names=("k_YN0", "tau", "h"),
        bounds=((1e-6, 50.0), (1.0, 1e6), (0.0, 0.95)),
        init_strategy=_init_M23,
        group="Fractal",
    ),
    BreakthroughModel(
        code="M24",
        name="Parallel two-component sigmoidal (Blagojev)",
        func=model_M24,
        param_names=("p", "tau1", "k1", "tau2", "k2"),
        bounds=((0.0, 1.0), (1.0, 1e6), (0.1, 20.0), (1.0, 1e6), (0.1, 20.0)),
        init_strategy=_init_M24,
        group="Parallel",
    ),
)


def get_model(code: str) -> BreakthroughModel:
    for m in REGISTRY:
        if m.code == code:
            return m
    raise KeyError(f"Unknown model code: {code}")

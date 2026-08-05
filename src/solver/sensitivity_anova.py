"""Sensitivity analysis of empirical breakthrough-model parameters by
ANOVA of clusters in scatterplots.

Method
------
Model-independent (distribution-free w.r.t. the input-output map) one-variate
sensitivity analysis after Kleijnen & Helton (1999a) and Saltelli et al.
(2000, ch. 2):

  1. Scatterplot the output ``y`` against each input ``x_i``.
  2. Partition the ``x_i`` axis into ``k`` equal-count clusters.
  3. Test the null "all clusters share a common mean of ``y``" (the CMNs test)
     with a one-way F.  Rejection => the scatterplot carries a non-random
     pattern => ``x_i`` is influential.  No linearity is assumed anywhere.
  4. Kruskal-Wallis (the CLs / common-locations test) is reported alongside as
     the rank-based backup, because normality is untestable at n = 9.
  5. Standardised regression coefficients (SRC) are reported for contrast.
     SRCs are only interpretable when the regression R^2 is high; where the
     cluster F is significant but the SRC is not, the dependence is non-linear
     and the regression has missed it.  That disagreement is the point of the
     method.

Two tiers of analysis:

  Tier 1 (experimental, model-free) - the nine "newest runs" form a balanced
     3x3 factorial in flow (0.05/0.10/0.15 lpm) x inlet CO2 (5/10/15 %).  The
     clusters are the design levels themselves, so the partition is not
     arbitrary.  Responses: t_b, t_E, t50, q_dyn, L_MTZ, psi.
     A pooled n = 14 layer adds runs 3/4/5/6/8 for the regression/scatterplot.

  Tier 2 (parametric, Monte Carlo) - the fitted parameters of the top-3 models
     by pooled AICc rank define ranges; N samples are drawn by Latin hypercube
     and propagated through each closed-form model to t_b/t50/t_E/q_dyn at a
     fixed reference operating point.  Independent-uniform sampling is the
     primary (textbook) case; Iman-Conover rank-correlated sampling is the
     robustness check, because k0 and h are near-perfectly rank-correlated
     (rho = 1.000) and independent sampling walks off the identifiable ridge.

  Tier 3 - regression of the fitted parameters themselves on (flow, C0), which
     closes the loop: operating condition -> empirical parameter -> breakthrough
     time and capacity.

Every number printed by this script traces to a committed run artefact under
``src/solver/breakthrough_out/`` or to the documented measurements block; no
parameter value is hand-typed except the run 3/4/5/6/8 metadata, which is
flagged inline with its provenance.

Run from the repository root:

    python src/solver/sensitivity_anova.py
"""

from __future__ import annotations

import glob
import os
import sys
import warnings
from dataclasses import dataclass
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
from scipy.optimize import brentq
from scipy.stats.qmc import LatinHypercube

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))

from breakthrough_fit.models import REGISTRY  # noqa: E402

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
SEED = 42
N_MC = 2000               # Monte Carlo / LHS sample size for Tier 2
K_CLUSTERS_MC = 5         # equal-count clusters for the MC scatterplots
K_CLUSTERS_EXP = 3        # experimental clusters == the 3 design levels
ALPHA = 0.05

REPO = _HERE.parent.parent
OUT_DIR = REPO / "src" / "solver" / "breakthrough_out"
FIG_DIR = REPO / "src" / "img" / "generated" / "sensitivity"
DOC_DIR = REPO / "src" / "docs"
CACHE = OUT_DIR / "_sa_cache.pkl"

R_GAS = 8.314             # J/(mol K)

RESPONSES = {
    "t_b_s": "t_b [s]",
    "t_E_s": "t_E [s]",
    "t50_s": "t50 [s]",
    "q_dyn_mol_per_kg": "q_dyn [mol/kg]",
    "L_MTZ_m": "L_MTZ [m]",
    "efficiency": "psi [-]",
}

# ---------------------------------------------------------------------------
# Run metadata
#
# The nine "newest runs" carry their own metadata in the CSV header (parser
# Format D) and are read from the file, never hand-typed.  Runs 3/4/5/6/8 have
# no in-file metadata; their values below are the documented measurements block
# (CLAUDE.md "Experimental design - as executed"), which is the authoritative
# record for those five runs.  Mass 8.00 g and column i.d. 8.5 mm are the fixed
# rig values recorded there.
# ---------------------------------------------------------------------------
OLD_RUN_META = {
    #  run_id : (flow_lpm, C0_ppm, bed_L_cm, mass_g, d_col_mm)
    "run 3": (0.15, 47_400.0, 21.0, 8.00, 8.5),
    "run 4": (0.05, 97_800.0, 21.3, 8.00, 8.5),
    "run 5": (0.10, 95_420.0, 21.2, 8.00, 8.5),
    "run 6": (0.15, 102_140.0, 21.5, 8.00, 8.5),
    "run 8": (0.10, 150_630.0, 21.5, 8.00, 8.5),
}

# Fallbacks used only when a Format-D header omits the field (mirrors
# new_runs_pipeline.py so the two scripts cannot drift).
T_K_DEFAULT = 298.0
P_PA_DEFAULT = 101_325.0


# ===========================================================================
# 1.  Data assembly
# ===========================================================================
def _split_params(s: str) -> dict[str, float]:
    """``"k0=0.23;tau0=2987.45"`` -> ``{"k0": 0.23, "tau0": 2987.45}``."""
    out: dict[str, float] = {}
    for item in str(s).split(";"):
        if "=" not in item:
            continue
        key, val = item.split("=", 1)
        try:
            out[key.strip()] = float(val)
        except ValueError:
            out[key.strip()] = np.nan
    return out


def _newest_run_meta(run_id: str) -> tuple[float, float, float, float, float, float, float]:
    """Read (flow_lpm, C0_ppm, bed_L_cm, mass_g, d_mm, T_K, P_Pa) from the
    Format-D header of a ``newest runs`` CSV."""
    path = REPO / "src" / "solver" / "data" / "newest runs" / f"{run_id}.csv"
    raw = path.read_text(encoding="utf-8", errors="replace")
    import re

    def grab(pat: str, default: float | None = None) -> float:
        m = re.search(pat, raw, re.IGNORECASE)
        return float(m.group(1)) if m else (np.nan if default is None else default)

    mass = grab(r"Mass:\s*([\d.]+)\s*g")
    bed_mm = grab(r"Bed height:\s*([\d.]+)\s*mm")
    flow = grab(r"Flow rate:\s*([\d.]+)\s*ml/min")
    c0 = grab(r"CO2:\s*[\d.]+\s*%\s*\(([\d.]+)\s*ppm\)")
    dia = grab(r"Tube diameter:\s*([\d.]+)\s*mm")
    # Operating T/P come from the data block, not the prose header.
    p_pa = grab(r"^P,(\d+),Pa", P_PA_DEFAULT)
    # Column 6 of the data block is the thermocouple; take its first reading.
    tmatch = re.search(r"\n[\d:.]+,0\.00,[^,]*,[^,]*,[^,]*,([\d.]+),", raw)
    t_k = (float(tmatch.group(1)) + 273.15) if tmatch else T_K_DEFAULT
    return flow / 1000.0, c0, bed_mm / 10.0, mass, dia, t_k, p_pa


def load_matrix() -> pd.DataFrame:
    """Assemble the 14-run x 24-model parameter and response matrix."""
    frames = []
    for d in sorted(glob.glob(str(OUT_DIR / "2026-*"))):
        f = glob.glob(os.path.join(d, "results_*.csv"))
        if f:
            frames.append(pd.read_csv(f[0]))
    for n in (3, 4, 5, 6, 8):
        f = OUT_DIR / f"run {n}" / f"results_run {n}.csv"
        if f.exists():
            frames.append(pd.read_csv(f))
    df = pd.concat(frames, ignore_index=True)

    meta_rows = []
    for rid in df.run_id.unique():
        if str(rid).startswith("2026"):
            q, c0, L, m, d, tk, ppa = _newest_run_meta(rid)
            dataset = "newest"
        else:
            q, c0, L, m, d = OLD_RUN_META[rid]
            tk, ppa = T_K_DEFAULT, P_PA_DEFAULT
            dataset = "new"
        meta_rows.append(
            dict(run_id=rid, dataset=dataset, flow_lpm=q, C0_ppm=c0,
                 bed_L_cm=L, mass_g=m, d_col_mm=d, T_K=tk, P_Pa=ppa)
        )
    meta = pd.DataFrame(meta_rows)
    # Derived operating variables.
    meta["C0_mol_m3"] = meta.C0_ppm * 1e-6 * meta.P_Pa / (R_GAS * meta.T_K)
    area = np.pi * (meta.d_col_mm * 1e-3 / 2.0) ** 2
    meta["u_sup_mm_s"] = (meta.flow_lpm / 60_000.0) / area * 1000.0
    meta["N_dot_mol_s"] = meta.flow_lpm / 60_000.0 * meta.C0_mol_m3  # CO2 molar feed

    df = df.merge(meta, on="run_id", how="left")
    return df


def param_table(df: pd.DataFrame, code: str) -> pd.DataFrame:
    """Wide table of fitted parameters for one model code, one row per run."""
    sub = df[df.code == code].copy()
    pv = pd.DataFrame([_split_params(s) for s in sub.params])
    pv.index = sub.index
    keep = ["run_id", "dataset", "flow_lpm", "C0_ppm", "bed_L_cm", "mass_g",
            "C0_mol_m3", "u_sup_mm_s", "AdjR2", "AICc", *RESPONSES]
    out = pd.concat([sub[keep].reset_index(drop=True), pv.reset_index(drop=True)], axis=1)
    return out


def canonicalise_M24(pt: pd.DataFrame) -> pd.DataFrame:
    """Fix label switching in the two-component mixture.

    ``p*S(t;tau1,k1) + (1-p)*S(t;tau2,k2)`` is invariant under
    ``(p,tau1,k1) <-> (1-p,tau2,k2)``.  Without a canonical ordering the
    marginal range of ``tau1`` mixes the fast and slow components and is
    meaningless.  Convention adopted: component 1 is the *fast* one
    (tau1 <= tau2).
    """
    pt = pt.copy()
    swap = pt.tau1 > pt.tau2
    if swap.any():
        for a, b in (("tau1", "tau2"), ("k1", "k2")):
            pt.loc[swap, [a, b]] = pt.loc[swap, [b, a]].values
        pt.loc[swap, "p"] = 1.0 - pt.loc[swap, "p"]
    pt.attrs["n_swapped"] = int(swap.sum())
    pt.attrs["swapped_runs"] = list(pt.run_id[swap])
    return pt


# ===========================================================================
# 2.  Statistical engine
# ===========================================================================
@dataclass
class ClusterANOVA:
    n: int
    k: int
    F: float
    p: float
    df1: int
    df2: int
    eta2: float
    H: float          # Kruskal-Wallis statistic (CLs test)
    p_kw: float
    edges: np.ndarray
    means: np.ndarray


def cluster_anova(x, y, k: int) -> ClusterANOVA:
    """Kleijnen-Helton CMNs test: partition ``x`` into ``k`` equal-count
    clusters and test equality of the cluster means of ``y``.

    Ties in ``x`` are kept together (so a 3-level design gives exactly 3
    clusters), which is why the partition uses ``rank(method='dense')`` when
    the number of distinct ``x`` values is <= k.
    """
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    ok = np.isfinite(x) & np.isfinite(y)
    x, y = x[ok], y[ok]
    n = x.size
    uniq = np.unique(x)
    if uniq.size <= k:
        labels = np.searchsorted(uniq, x)
        kk = uniq.size
        edges = uniq
    else:
        qs = np.quantile(x, np.linspace(0, 1, k + 1)[1:-1])
        labels = np.searchsorted(qs, x, side="right")
        kk = k
        edges = qs
    groups = [y[labels == j] for j in range(kk)]
    groups = [g for g in groups if g.size > 0]
    kk = len(groups)
    if kk < 2 or any(g.size < 1 for g in groups) or n - kk < 1:
        return ClusterANOVA(n, kk, np.nan, np.nan, kk - 1, n - kk,
                            np.nan, np.nan, np.nan, edges, np.array([]))

    grand = y.mean()
    ss_between = sum(g.size * (g.mean() - grand) ** 2 for g in groups)
    ss_within = sum(((g - g.mean()) ** 2).sum() for g in groups)
    ss_total = ss_between + ss_within
    df1, df2 = kk - 1, n - kk
    if ss_within <= 0 or df2 <= 0:
        F, p = np.inf, 0.0
    else:
        F = (ss_between / df1) / (ss_within / df2)
        p = float(stats.f.sf(F, df1, df2))
    eta2 = ss_between / ss_total if ss_total > 0 else np.nan
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        try:
            H, p_kw = stats.kruskal(*groups)
        except ValueError:
            H, p_kw = np.nan, np.nan
    return ClusterANOVA(n, kk, float(F), float(p), df1, df2, float(eta2),
                        float(H), float(p_kw), edges,
                        np.array([g.mean() for g in groups]))


def ols_src(X: pd.DataFrame, y: np.ndarray) -> tuple[pd.DataFrame, dict]:
    """OLS with standardised regression coefficients.

    Returns (per-regressor table, model-summary dict).
    ``std_coef`` is the SRC = beta_i * s_{x_i} / s_y, the classical SA measure
    (Saltelli et al. 2000, sec. 2.6); it is only interpretable when the model
    R^2 is high, which is why R^2 is reported alongside.
    """
    names = list(X.columns)
    Xv = X.to_numpy(float)
    y = np.asarray(y, float)
    ok = np.isfinite(y) & np.isfinite(Xv).all(axis=1)
    Xv, y = Xv[ok], y[ok]
    n, k = Xv.shape
    A = np.column_stack([np.ones(n), Xv])
    beta, *_ = np.linalg.lstsq(A, y, rcond=None)
    resid = y - A @ beta
    dof = n - k - 1
    if dof <= 0:
        raise ValueError(f"n={n} too small for {k} regressors")
    sigma2 = float(resid @ resid) / dof
    XtX_inv = np.linalg.pinv(A.T @ A)
    se = np.sqrt(np.diag(XtX_inv) * sigma2)
    tvals = beta / se
    pvals = 2.0 * stats.t.sf(np.abs(tvals), dof)
    sy = y.std(ddof=1)
    src = np.array([beta[i + 1] * Xv[:, i].std(ddof=1) / sy if sy > 0 else np.nan
                    for i in range(k)])

    ss_res = float(resid @ resid)
    ss_tot = float(((y - y.mean()) ** 2).sum())
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else np.nan
    adj = 1.0 - (1.0 - r2) * (n - 1) / dof
    see = float(np.sqrt(sigma2))
    f_model = ((ss_tot - ss_res) / k) / (ss_res / dof) if ss_res > 0 else np.inf
    p_model = float(stats.f.sf(f_model, k, dof)) if np.isfinite(f_model) else 0.0

    tbl = pd.DataFrame({
        "term": ["(Intercept)"] + names,
        "beta": beta,
        "std_error": se,
        "std_coef": [np.nan] + list(src),
        "t": tvals,
        "sig": pvals,
    })
    summary = dict(n=n, k=k, R2=r2, AdjR2=adj, SEE=see,
                   F_model=float(f_model), sig_model=p_model)
    return tbl, summary


def bh_fdr(p: np.ndarray) -> np.ndarray:
    """Benjamini-Hochberg adjusted p-values (many tests are run here)."""
    p = np.asarray(p, float)
    ok = np.isfinite(p)
    q = np.full_like(p, np.nan)
    pv = p[ok]
    m = pv.size
    if m == 0:
        return q
    order = np.argsort(pv)
    ranked = pv[order] * m / (np.arange(m) + 1)
    ranked = np.minimum.accumulate(ranked[::-1])[::-1]
    out = np.empty(m)
    out[order] = np.clip(ranked, 0, 1)
    q[ok] = out
    return q


def stars(p: float) -> str:
    if not np.isfinite(p):
        return "n/a"
    return "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else \
        "." if p < 0.10 else "n.s."


# ===========================================================================
# 3.  Sampling
# ===========================================================================
def lhs_uniform(lo: np.ndarray, hi: np.ndarray, n: int, rng) -> np.ndarray:
    """Latin hypercube sample on the box [lo, hi]."""
    eng = LatinHypercube(d=len(lo), seed=int(rng.integers(2**31 - 1)))
    u = eng.random(n)
    return lo + u * (hi - lo)


def iman_conover(X: np.ndarray, target: np.ndarray, rng) -> np.ndarray:
    """Iman-Conover restricted pairing: reorder the columns of ``X`` so their
    rank correlation approximates ``target``, leaving each marginal untouched.

    Used as the robustness check for correlated inputs (Saltelli et al. 2000,
    sec. 6.4) because independent sampling of (k0, h) is off-ridge.
    """
    n, k = X.shape
    try:
        P = np.linalg.cholesky(target)
    except np.linalg.LinAlgError:  # nudge to positive definite
        w, V = np.linalg.eigh(target)
        w = np.clip(w, 1e-8, None)
        P = np.linalg.cholesky(V @ np.diag(w) @ V.T)
    # van der Waerden scores, decorrelated then recorrelated.
    scores = stats.norm.ppf((np.arange(1, n + 1)) / (n + 1))
    M = np.column_stack([rng.permutation(scores) for _ in range(k)])
    M = M @ np.linalg.inv(np.linalg.cholesky(np.corrcoef(M, rowvar=False))).T
    T = M @ P.T
    out = np.empty_like(X)
    for j in range(k):
        ranks = np.argsort(np.argsort(T[:, j]))
        out[:, j] = np.sort(X[:, j])[ranks]
    return out


# ===========================================================================
# 4.  Forward propagation of a closed-form model
# ===========================================================================
def _crossing(f, level: float, t_hi: float) -> float:
    """First time at which ``f(t) = level``, by bracketed root-find."""
    lo, hi = 1.0, t_hi
    try:
        if f(lo) >= level:
            return lo
        if f(hi) < level:
            return np.nan
        return float(brentq(lambda t: f(t) - level, lo, hi, xtol=1e-3, rtol=1e-10))
    except (ValueError, RuntimeError, OverflowError):
        return np.nan


def propagate(func, theta, ref) -> dict[str, float]:
    """Map one parameter vector to the six breakthrough responses.

    ``ref`` holds the fixed reference operating point (flow, C0, mass, bed L),
    so the Monte Carlo varies only the empirical parameters.
    """
    def f(t):
        return float(np.atleast_1d(func(np.atleast_1d(float(t)), *theta))[0])

    # M10 evaluates arctan(sinh(arg)); for extreme MC draws sinh overflows to
    # inf, but arctan(inf) = pi/2 so the model still saturates at exactly 1.0.
    # The warning is benign - silence it rather than patch the fitted model.
    warnings.filterwarnings("ignore", category=RuntimeWarning)

    t_hi = ref["t_hi"]
    t_b = _crossing(f, 0.05, t_hi)
    t50 = _crossing(f, 0.50, t_hi)
    t_E = _crossing(f, 0.95, t_hi)
    if not np.isfinite(t_E) or not np.isfinite(t_b) or t_E <= t_b:
        return {k: np.nan for k in RESPONSES}

    grid = np.linspace(0.0, t_E, 4000)
    y = np.clip(np.asarray(func(np.maximum(grid, 1e-9), *theta), float), 0.0, 1.0)
    q_dyn = ref["flow_m3_s"] * ref["C0_mol_m3"] * float(np.trapezoid(1.0 - y, grid)) / ref["mass_kg"]

    grid_inf = np.linspace(0.0, 5.0 * t_E, 3000)
    y_inf = np.clip(np.asarray(func(np.maximum(grid_inf, 1e-9), *theta), float), 0.0, 1.0)
    t_star = float(np.trapezoid(1.0 - y_inf, grid_inf))

    return {
        "t_b_s": t_b,
        "t_E_s": t_E,
        "t50_s": t50,
        "q_dyn_mol_per_kg": q_dyn,
        "L_MTZ_m": (1.0 - (t_E - t_b) / (2.0 * t_E)) * ref["bed_L_m"],
        "efficiency": t_b / t_star if t_star > 0 else np.nan,
    }


# ===========================================================================
# 5.  Tier 1 - experimental sensitivity (model-free)
# ===========================================================================
FACTORS = {"flow_lpm": "Flow rate Q [lpm]", "C0_ppm": "Inlet CO2 C0 [ppm]"}


def _rss(X: np.ndarray, y: np.ndarray) -> float:
    """Residual sum of squares of the OLS fit of ``y`` on ``X``."""
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    r = y - X @ beta
    return float(r @ r)


def _dummies(labels: np.ndarray) -> np.ndarray:
    """Reference-coded dummies (k-1 columns) for a categorical vector."""
    lev = np.unique(labels)
    return np.column_stack([(labels == l).astype(float) for l in lev[1:]])


def two_way_anova(d: pd.DataFrame, resp: str) -> dict:
    """Unbalanced two-way ANOVA with replication, Type II sums of squares.

    The 18-file basis gives 1-2 observations per cell, so the flow x
    concentration interaction is estimable for the first time (it was wholly
    confounded with error under the earlier one-observation-per-cell design).
    Cells are unbalanced, so main effects use Type II SS - each adjusted for the
    other main effect but not for the interaction - which is the appropriate
    choice when the interaction is not assumed present a priori.

    Pure error (replicate variation within a cell) is separated from lack of
    fit where cells have more than one observation; ``F_pure`` compares the
    interaction against pure error only.
    """
    d = d[["flow_lpm", "C0_level", resp]].dropna()
    y = d[resp].to_numpy(float)
    n = y.size
    fl = d.flow_lpm.to_numpy()
    cl = d.C0_level.astype(str).to_numpy()
    one = np.ones((n, 1))
    A, B = _dummies(fl), _dummies(cl)
    AB = np.column_stack([a * b for a in A.T for b in B.T]) if A.size and B.size else np.empty((n, 0))

    X0 = one
    Xa = np.column_stack([one, A])
    Xb = np.column_stack([one, B])
    Xab = np.column_stack([one, A, B])
    Xfull = np.column_stack([one, A, B, AB])
    # Drop aliased interaction columns (cells with no observation).
    keep = np.linalg.matrix_rank(Xfull)
    if keep < Xfull.shape[1]:
        cols, cur = [], np.column_stack([one, A, B])
        for j in range(AB.shape[1]):
            trial = np.column_stack([cur, AB[:, j]])
            if np.linalg.matrix_rank(trial) > np.linalg.matrix_rank(cur):
                cur, _ = trial, cols.append(j)
        Xfull = np.column_stack([one, A, B, AB[:, cols]]) if cols else Xab

    rss_0, rss_a, rss_b = _rss(X0, y), _rss(Xa, y), _rss(Xb, y)
    rss_ab, rss_full = _rss(Xab, y), _rss(Xfull, y)
    ss_tot = rss_0

    df_a, df_b = A.shape[1], B.shape[1]
    df_ab = Xfull.shape[1] - Xab.shape[1]
    df_e = n - Xfull.shape[1]
    if df_e <= 0:
        return dict(response=resp, n=n, df_err=df_e, note="saturated - no error df")
    ms_e = rss_full / df_e

    ss_a = rss_b - rss_ab            # flow | conc
    ss_b = rss_a - rss_ab            # conc | flow
    ss_i = rss_ab - rss_full         # interaction | both

    f_a = (ss_a / df_a) / ms_e
    f_b = (ss_b / df_b) / ms_e
    f_i = (ss_i / df_ab) / ms_e if df_ab > 0 else np.nan

    return dict(
        response=resp, n=n,
        F_flow=f_a, sig_flow=float(stats.f.sf(f_a, df_a, df_e)),
        F_conc=f_b, sig_conc=float(stats.f.sf(f_b, df_b, df_e)),
        F_int=f_i,
        sig_int=float(stats.f.sf(f_i, df_ab, df_e)) if df_ab > 0 else np.nan,
        eta2_flow=ss_a / ss_tot, eta2_conc=ss_b / ss_tot,
        eta2_int=ss_i / ss_tot if df_ab > 0 else np.nan,
        eta2_resid=rss_full / ss_tot,
        df_flow=df_a, df_conc=df_b, df_int=df_ab, df_err=df_e,
    )


def replicate_reproducibility(d: pd.DataFrame) -> pd.DataFrame:
    """Within-cell spread of every response - the pure-error estimate.

    Replication is what the expanded run set buys; this quantifies how much of
    the observed variation is measurement repeatability rather than a real
    effect of the operating conditions.
    """
    rows = []
    for resp, lab in RESPONSES.items():
        g = d.dropna(subset=[resp]).groupby(["flow_lpm", "C0_level"], observed=True)[resp]
        reps = g.agg(["count", "mean", "std", "min", "max"])
        reps = reps[reps["count"] > 1]
        if reps.empty:
            rows.append(dict(response=lab, n_cells_replicated=0))
            continue
        cv = (reps["std"] / reps["mean"]).abs()
        pooled_var = ((reps["count"] - 1) * reps["std"] ** 2).sum() / (reps["count"] - 1).sum()
        total_sd = d[resp].std(ddof=1)
        rows.append(dict(
            response=lab,
            n_cells_replicated=int(len(reps)),
            pure_error_sd=float(np.sqrt(pooled_var)),
            total_sd=float(total_sd),
            pure_error_frac_of_total_var=float(pooled_var / total_sd ** 2),
            median_within_cell_CV=float(cv.median()),
            max_within_cell_CV=float(cv.max()),
            worst_cell_ratio=float((reps["max"] / reps["min"]).max()),
        ))
    return pd.DataFrame(rows)


def tier1(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    """Experimental SA: cluster ANOVA + factorial ANOVA + pooled regression."""
    runs = (df[df.code == "M01"]
            .drop_duplicates("run_id")
            .reset_index(drop=True))
    grid = runs[runs.dataset == "newest"].copy()
    grid["C0_level"] = pd.cut(grid.C0_ppm, [0, 7e4, 1.2e5, 2e5],
                              labels=["5%", "10%", "15%"])

    # --- 5a. cluster ANOVA, clusters = design levels -----------------------
    rows = []
    for scope, d in ((f"grid n={len(grid)}", grid), (f"pooled n={len(runs)}", runs)):
        for fac, flab in FACTORS.items():
            for resp, rlab in RESPONSES.items():
                ca = cluster_anova(d[fac], d[resp], K_CLUSTERS_EXP)
                rows.append(dict(scope=scope, factor=flab, response=rlab,
                                 n=ca.n, k=ca.k, df1=ca.df1, df2=ca.df2,
                                 F=ca.F, sig=ca.p, eta2=ca.eta2,
                                 H_KW=ca.H, sig_KW=ca.p_kw))
    clus = pd.DataFrame(rows)
    clus["q_BH"] = bh_fdr(clus.sig.to_numpy())
    clus["verdict"] = [stars(p) for p in clus.sig]

    # --- 5b. factorial with replication -----------------------------------
    fact = pd.DataFrame([two_way_anova(grid, r) for r in RESPONSES])
    fact["response"] = list(RESPONSES.values())
    repro = replicate_reproducibility(grid)

    # --- 5c. pooled regression on the operating conditions -----------------
    reg_rows, sum_rows = [], []
    for scope, d in ((f"grid n={len(grid)}", grid), (f"pooled n={len(runs)}", runs)):
        X = d[["flow_lpm", "C0_ppm"]].rename(
            columns={"flow_lpm": "Q [lpm]", "C0_ppm": "C0 [ppm]"})
        for resp, rlab in RESPONSES.items():
            tbl, summ = ols_src(X, d[resp].to_numpy())
            tbl.insert(0, "response", rlab)
            tbl.insert(0, "scope", scope)
            reg_rows.append(tbl)
            sum_rows.append(dict(scope=scope, response=rlab, **summ))
    reg = pd.concat(reg_rows, ignore_index=True)
    reg["verdict"] = [stars(p) for p in reg.sig]
    return dict(cluster=clus, factorial=fact, regression=reg, repro=repro,
                reg_summary=pd.DataFrame(sum_rows), runs=runs, grid=grid)


# ===========================================================================
# 6.  Tier 2 - Monte Carlo parameter sensitivity
# ===========================================================================
def bound_pinning(df: pd.DataFrame, tol: float = 1e-3) -> pd.DataFrame:
    """Fraction of runs in which each parameter is fitted at its own bound.

    A parameter pinned at a bound has not been estimated - the fitter ran out
    of room.  Its across-run range is then an artefact of the bound, so it must
    not be used to define a Monte Carlo prior.  Screening for this is what keeps
    a model like M03 (which pins n at 1.01 and A0 at 1e6) out of the parameter
    dissection on its AICc rank alone.
    """
    rows = []
    for m in REGISTRY:
        sub = df[df.code == m.code]
        if sub.empty:
            continue
        pv = pd.DataFrame([_split_params(s) for s in sub.params])
        for name, (lo, hi) in zip(m.param_names, m.bounds):
            v = pv[name].to_numpy(float)
            # Tolerance is relative to each bound, not to the bound span: with
            # bounds like (1, 1e6) a span-relative test would call any value
            # under 1001 "pinned at 1".
            pinned = (np.abs(v - lo) <= tol * max(abs(lo), 1e-12)) | \
                     (np.abs(v - hi) <= tol * max(abs(hi), 1e-12))
            rows.append(dict(code=m.code, name=m.name, parameter=name,
                             lower=lo, upper=hi, n_runs=len(v),
                             n_pinned=int(pinned.sum()),
                             frac_pinned=float(pinned.mean())))
    return pd.DataFrame(rows)


def top_models(df: pd.DataFrame, n: int = 3,
               max_pinned: float = 0.25) -> tuple[list[str], pd.DataFrame]:
    """Best models by mean AICc rank, after screening out non-identifiable ones.

    A model is disqualified if any of its parameters sits at a bound in more
    than ``max_pinned`` of runs: its AICc is then bought with a parameter that
    was never estimated.
    """
    d = df.copy()
    d["rank"] = d.groupby("run_id").AICc.rank()
    order = d.groupby(["code", "name"])["rank"].mean().sort_values().reset_index()
    pin = bound_pinning(df)
    worst = pin.groupby("code").frac_pinned.max()
    order["max_frac_pinned"] = order.code.map(worst)
    order["excluded"] = order.max_frac_pinned > max_pinned
    order["reason"] = [
        "" if not e else "; ".join(
            f"{r.parameter} pinned in {r.n_pinned}/{r.n_runs} runs"
            for _, r in pin[(pin.code == c) & (pin.frac_pinned > max_pinned)].iterrows())
        for c, e in zip(order.code, order.excluded)
    ]
    return list(order[~order.excluded].code[:n]), order


def reference_point(df: pd.DataFrame) -> dict:
    """Fixed operating point for the MC: the geometric centre of the 3x3 grid
    (0.10 lpm, 10 % CO2), taken from that run's own measured metadata."""
    r = df[df.run_id == "2026-07-08-conc10-flow0.10"].iloc[0]
    return dict(
        run_id=r.run_id,
        flow_m3_s=r.flow_lpm / 60_000.0,
        C0_mol_m3=r.C0_mol_m3,
        C0_ppm=r.C0_ppm,
        mass_kg=r.mass_g / 1000.0,
        bed_L_m=r.bed_L_cm / 100.0,
        t_hi=2.0e5,
    )


def distribution_table(pt: pd.DataFrame, names: list[str], code: str) -> pd.DataFrame:
    """Table 1: actual value per run, plus min/max and the assumed sampling
    distribution.

    The distribution column records the *assumed* Monte Carlo prior, not a
    fitted one: with n = 14 draws no distributional form can be identified.
    Uniform[min, max] is the standard non-informative choice when only a range
    is credible (Saltelli et al. 2000).  Shapiro-Wilk on the raw and log scale
    is reported as a diagnostic of which scale is less skewed.
    """
    rows = []
    for p in names:
        v = pt[p].to_numpy(float)
        v = v[np.isfinite(v)]
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            sw_raw = stats.shapiro(v).pvalue if v.size >= 3 else np.nan
            pos = v[v > 0]
            sw_log = stats.shapiro(np.log(pos)).pvalue if pos.size >= 3 else np.nan
        cv = v.std(ddof=1) / abs(v.mean()) if v.mean() != 0 else np.nan
        rows.append(dict(
            model=code, parameter=p,
            min=v.min(), max=v.max(), median=float(np.median(v)),
            mean=v.mean(), sd=v.std(ddof=1), CV=cv,
            span_decades=np.log10(v.max() / v.min()) if v.min() > 0 else np.nan,
            shapiro_p_raw=sw_raw, shapiro_p_log=sw_log,
            assumed_distribution=f"Uniform[{v.min():.4g}, {v.max():.4g}]",
        ))
    return pd.DataFrame(rows)


def tier2(df: pd.DataFrame, codes: list[str], ref: dict, rng) -> dict:
    """Monte Carlo SA for each selected model."""
    reg_model = {m.code: m for m in REGISTRY}
    out = {"dist": [], "cluster": [], "reg": [], "summary": [],
           "samples": {}, "notes": []}

    for code in codes:
        mdl = reg_model[code]
        names = list(mdl.param_names)
        pt = param_table(df, code)
        if code == "M24":
            pt = canonicalise_M24(pt)
            out["notes"].append(
                f"{code}: label switching corrected in {pt.attrs['n_swapped']} of "
                f"{len(pt)} runs ({', '.join(pt.attrs['swapped_runs'])}); "
                "convention tau1 <= tau2."
            )
        lo = pt[names].min().to_numpy(float)
        hi = pt[names].max().to_numpy(float)

        dist = distribution_table(pt, names, code)
        out["dist"].append(dist)

        # Empirical rank correlation of the fitted parameters (drives the
        # Iman-Conover robustness case and flags non-identifiability).
        rho = pt[names].corr(method="spearman").to_numpy()
        worst = np.abs(rho - np.eye(len(names))).max()
        if worst > 0.9:
            i, j = np.unravel_index(np.abs(rho - np.eye(len(names))).argmax(), rho.shape)
            out["notes"].append(
                f"{code}: |rho_S({names[i]}, {names[j]})| = {abs(rho[i, j]):.3f} - these "
                "parameters are not independently identifiable; independent-uniform "
                "sampling leaves the fitted ridge."
            )

        for scheme in ("independent", "rank-correlated"):
            X = lhs_uniform(lo, hi, N_MC, rng)
            if scheme == "rank-correlated":
                X = iman_conover(X, rho, rng)
            res = pd.DataFrame([propagate(mdl.func, th, ref) for th in X])
            samp = pd.concat([pd.DataFrame(X, columns=names), res], axis=1)
            samp["scheme"] = scheme
            samp["model"] = code
            out["samples"][(code, scheme)] = samp
            n_ok = int(res.t_b_s.notna().sum())
            out["notes"].append(
                f"{code}/{scheme}: {n_ok}/{N_MC} samples produced a complete "
                f"breakthrough curve ({100*n_ok/N_MC:.1f} %)."
            )

            valid = samp[samp.t_b_s.notna()]
            for resp, rlab in RESPONSES.items():
                # Cluster ANOVA, one input at a time (the model-free test).
                for p in names:
                    ca = cluster_anova(valid[p], valid[resp], K_CLUSTERS_MC)
                    out["cluster"].append(dict(
                        model=code, scheme=scheme, parameter=p, response=rlab,
                        n=ca.n, k=ca.k, df1=ca.df1, df2=ca.df2,
                        F=ca.F, sig=ca.p, eta2=ca.eta2,
                        H_KW=ca.H, sig_KW=ca.p_kw))
                # SRC regression, all inputs together (the linear contrast).
                tbl, summ = ols_src(valid[names], valid[resp].to_numpy())
                tbl.insert(0, "response", rlab)
                tbl.insert(0, "scheme", scheme)
                tbl.insert(0, "model", code)
                out["reg"].append(tbl)
                out["summary"].append(dict(model=code, scheme=scheme,
                                           response=rlab, **summ))

    out["dist"] = pd.concat(out["dist"], ignore_index=True)
    out["cluster"] = pd.DataFrame(out["cluster"])
    out["cluster"]["q_BH"] = bh_fdr(out["cluster"].sig.to_numpy())
    out["cluster"]["verdict"] = [stars(p) for p in out["cluster"].sig]
    out["reg"] = pd.concat(out["reg"], ignore_index=True)
    out["reg"]["verdict"] = [stars(p) for p in out["reg"].sig]
    out["summary"] = pd.DataFrame(out["summary"])
    return out


# ===========================================================================
# 7.  Tier 3 - operating condition -> empirical parameter
# ===========================================================================
def tier3(df: pd.DataFrame, codes: list[str]) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Regress each fitted parameter on (Q, C0): the link that explains *why*
    breakthrough time moves when the operating point moves."""
    reg_model = {m.code: m for m in REGISTRY}
    reg_rows, sum_rows, clus_rows = [], [], []
    for code in codes:
        pt = param_table(df, code)
        if code == "M24":
            pt = canonicalise_M24(pt)
        grid = pt[pt.dataset == "newest"]
        names = list(reg_model[code].param_names)
        X = grid[["flow_lpm", "C0_ppm"]].rename(
            columns={"flow_lpm": "Q [lpm]", "C0_ppm": "C0 [ppm]"})
        for p in names:
            y = grid[p].to_numpy(float)
            use_log = np.all(y > 0) and (y.max() / y.min() > 10)
            yy = np.log(y) if use_log else y
            tbl, summ = ols_src(X, yy)
            tbl.insert(0, "parameter", f"ln({p})" if use_log else p)
            tbl.insert(0, "model", code)
            reg_rows.append(tbl)
            sum_rows.append(dict(model=code,
                                 parameter=f"ln({p})" if use_log else p, **summ))
            for fac, flab in FACTORS.items():
                ca = cluster_anova(grid[fac], yy, K_CLUSTERS_EXP)
                clus_rows.append(dict(
                    model=code, parameter=f"ln({p})" if use_log else p,
                    factor=flab, n=ca.n, k=ca.k, df1=ca.df1, df2=ca.df2,
                    F=ca.F, sig=ca.p, eta2=ca.eta2, H_KW=ca.H, sig_KW=ca.p_kw))
    reg = pd.concat(reg_rows, ignore_index=True)
    reg["verdict"] = [stars(p) for p in reg.sig]
    clus = pd.DataFrame(clus_rows)
    clus["verdict"] = [stars(p) for p in clus.sig]
    return reg, pd.DataFrame(sum_rows), clus


# ===========================================================================
# 8.  Figures - scatterplots with the cluster partition drawn on
# ===========================================================================
def _scatter_panel(ax, x, y, k, xlabel, ylabel, logx=False, max_pts=900):
    ca = cluster_anova(x, y, k)   # statistics always use every sample
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    ok = np.isfinite(x) & np.isfinite(y)
    x, y = x[ok], y[ok]
    big = x.size > 100
    if x.size > max_pts:  # thin only what is *drawn*, never what is tested
        sel = np.random.default_rng(SEED).choice(x.size, max_pts, replace=False)
        xd, yd = x[sel], y[sel]
    else:
        xd, yd = x, y
    ax.scatter(xd, yd, s=8 if big else 46, alpha=0.35 if big else 0.95,
               c="#2b6cb0", edgecolors="none" if big else "k", linewidths=0.5,
               zorder=2, rasterized=True)
    uniq = np.unique(x)
    if uniq.size <= k:
        centres, edges = uniq, []
        labels = np.searchsorted(uniq, x)
    else:
        edges = np.quantile(x, np.linspace(0, 1, k + 1)[1:-1])
        labels = np.searchsorted(edges, x, side="right")
        bounds = np.concatenate([[x.min()], edges, [x.max()]])
        centres = 0.5 * (bounds[:-1] + bounds[1:])
    for e in np.atleast_1d(edges):
        ax.axvline(e, color="0.55", ls="--", lw=0.8, zorder=1)
    means = [y[labels == j].mean() for j in range(len(centres))]
    ax.plot(centres, means, "o-", color="#c53030", ms=6, lw=1.8, zorder=3,
            label="cluster mean")
    if logx:
        ax.set_xscale("log")
    ax.set_xlabel(xlabel, fontsize=8)
    ax.set_ylabel(ylabel, fontsize=8)
    ax.tick_params(labelsize=7)
    ax.set_title(f"F({ca.df1},{ca.df2}) = {ca.F:.3g}, p = {ca.p:.3g} {stars(ca.p)}"
                 f"   $\\eta^2$ = {ca.eta2:.3f}", fontsize=8)
    ax.grid(alpha=0.25, lw=0.5)
    return ca


def fig_tier1(t1: dict):
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    for key in ("grid", "runs"):
        d = t1[key]
        scope = f"{'3x3 grid' if key == 'grid' else 'pooled'} n={len(d)}"
        fig, axes = plt.subplots(len(FACTORS), len(RESPONSES),
                                 figsize=(3.0 * len(RESPONSES), 3.0 * len(FACTORS)))
        for i, (fac, flab) in enumerate(FACTORS.items()):
            for j, (resp, rlab) in enumerate(RESPONSES.items()):
                _scatter_panel(axes[i, j], d[fac], d[resp], K_CLUSTERS_EXP, flab, rlab)
        fig.suptitle(f"Tier 1 - cluster ANOVA of experimental scatterplots ({scope}); "
                     f"dashed lines = cluster boundaries", fontsize=11)
        fig.tight_layout(rect=(0, 0, 1, 0.96))
        name = f"S1_experimental_clusters_{key}.png"
        fig.savefig(FIG_DIR / name, dpi=300)
        plt.close(fig)
        print(f"  wrote {name}")


def fig_tier2(t2: dict, codes: list[str]):
    reg_model = {m.code: m for m in REGISTRY}
    for code in codes:
        names = list(reg_model[code].param_names)
        for scheme in ("independent", "rank-correlated"):
            samp = t2["samples"][(code, scheme)]
            valid = samp[samp.t_b_s.notna()]
            fig, axes = plt.subplots(len(names), len(RESPONSES),
                                     figsize=(3.0 * len(RESPONSES), 2.8 * len(names)),
                                     squeeze=False)
            for i, p in enumerate(names):
                logx = valid[p].min() > 0 and valid[p].max() / valid[p].min() > 50
                for j, (resp, rlab) in enumerate(RESPONSES.items()):
                    _scatter_panel(axes[i, j], valid[p], valid[resp],
                                   K_CLUSTERS_MC, p, rlab, logx=logx)
            fig.suptitle(f"Tier 2 - {code} {reg_model[code].name}; "
                         f"{scheme} LHS, N = {N_MC}, k = {K_CLUSTERS_MC} clusters",
                         fontsize=11)
            fig.tight_layout(rect=(0, 0, 1, 0.97))
            name = f"S2_{code}_{scheme}.png"
            fig.savefig(FIG_DIR / name, dpi=200)
            plt.close(fig)
            print(f"  wrote {name}")


def fig_identifiability(df: pd.DataFrame, codes: list[str]):
    """The k0-h ridge: why independent sampling is the wrong prior."""
    fig, axes = plt.subplots(1, len(codes), figsize=(4.4 * len(codes), 4.0),
                             squeeze=False)
    reg_model = {m.code: m for m in REGISTRY}
    for ax, code in zip(axes[0], codes):
        pt = param_table(df, code)
        if code == "M24":
            pt = canonicalise_M24(pt)
        names = list(reg_model[code].param_names)
        a, b = names[0], names[2] if len(names) > 2 else names[1]
        for ds, mk, col in (("newest", "o", "#2b6cb0"), ("new", "s", "#c53030")):
            s = pt[pt.dataset == ds]
            ax.scatter(s[a], s[b], marker=mk, s=60, c=col, edgecolors="k",
                       linewidths=0.6, label=f"{ds} runs (n={len(s)})")
        rho = stats.spearmanr(pt[a], pt[b]).statistic
        ax.set_xscale("log")
        ax.set_xlabel(a)
        ax.set_ylabel(b)
        ax.set_title(f"{code}: $\\rho_S$({a}, {b}) = {rho:.3f}", fontsize=10)
        ax.grid(alpha=0.25, lw=0.5)
        ax.legend(fontsize=7)
    fig.suptitle("Parameter identifiability: fitted values lie on a 1-D ridge",
                 fontsize=11)
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    fig.savefig(FIG_DIR / "S3_identifiability_ridge.png", dpi=300)
    plt.close(fig)
    print("  wrote S3_identifiability_ridge.png")


# ===========================================================================
# 9.  Self-checks
# ===========================================================================
def self_check(df: pd.DataFrame, ref: dict):
    """Assert-based checks. Fails loudly rather than reporting a wrong number."""
    rng = np.random.default_rng(0)

    # (a) our one-way F must equal scipy's f_oneway on the same partition
    x = rng.normal(size=300)
    y = 2.0 * x**2 + rng.normal(scale=0.3, size=300)
    ca = cluster_anova(x, y, 5)
    qs = np.quantile(x, np.linspace(0, 1, 6)[1:-1])
    lab = np.searchsorted(qs, x, side="right")
    F_ref, p_ref = stats.f_oneway(*[y[lab == j] for j in range(5)])
    assert abs(ca.F - F_ref) < 1e-9 * max(1.0, F_ref), (ca.F, F_ref)
    assert abs(ca.p - p_ref) < 1e-12, (ca.p, p_ref)

    # (b) purely quadratic y = x^2 on symmetric x: SRC ~ 0 but cluster F huge.
    #     This is the exact case the method exists for.
    tbl, summ = ols_src(pd.DataFrame({"x": x}), y)
    assert abs(tbl.loc[1, "std_coef"]) < 0.2, tbl
    assert ca.F > 50 and ca.p < 1e-10, (ca.F, ca.p)

    # (c) single-regressor SRC must equal Pearson r
    y_lin = 3.0 * x + rng.normal(scale=0.5, size=300)
    tbl2, _ = ols_src(pd.DataFrame({"x": x}), y_lin)
    assert abs(tbl2.loc[1, "std_coef"] - np.corrcoef(x, y_lin)[0, 1]) < 1e-10

    # (d) forward propagation: for M01 the logistic is exactly symmetric, so
    #     t50 == tau and t_b/t_E sit at +-ln(19)/k_YN about tau.  Parameters
    #     chosen so both crossings are interior to t > 0.
    by_code = {m.code: m for m in REGISTRY}
    k_yn, tau = 0.01, 1000.0
    r = propagate(by_code["M01"].func, (k_yn, tau), ref)
    half = np.log(19.0) / k_yn
    assert abs(r["t50_s"] - tau) < 1e-2, r["t50_s"]
    assert abs(r["t_b_s"] - (tau - half)) < 1e-2, r["t_b_s"]
    assert abs(r["t_E_s"] - (tau + half)) < 1e-2, r["t_E_s"]

    # (e) propagating the reference run's own fitted M11 parameters must
    #     reproduce that run's measured t_b, t50 and q_dyn.  They are not
    #     identical - one integrates the fitted curve, the other the raw data -
    #     so the tolerance is generous but the check would catch a unit slip.
    meas = df[(df.run_id == ref["run_id"]) & (df.code == "M11")].iloc[0]
    theta = tuple(_split_params(meas.params)[p] for p in by_code["M11"].param_names)
    rm = propagate(by_code["M11"].func, theta, ref)
    for key in ("t_b_s", "t50_s", "q_dyn_mol_per_kg"):
        rel = abs(rm[key] - meas[key]) / abs(meas[key])
        assert rel < 0.30, (key, rm[key], meas[key], rel)

    # (f) Iman-Conover must preserve marginals exactly and move rank corr.
    X = lhs_uniform(np.array([0.0, 0.0]), np.array([1.0, 1.0]), 500,
                    np.random.default_rng(1))
    tgt = np.array([[1.0, 0.9], [0.9, 1.0]])
    Xc = iman_conover(X, tgt, np.random.default_rng(2))
    for j in range(2):
        assert np.allclose(np.sort(X[:, j]), np.sort(Xc[:, j]))
    got = stats.spearmanr(Xc[:, 0], Xc[:, 1]).statistic
    assert got > 0.8, got

    # (g) two-way ANOVA: on a BALANCED synthetic design the Type II SS must
    #     reduce to the classical orthogonal decomposition and sum to the total,
    #     and a planted interaction must be recovered.
    lv_f = np.repeat([0.05, 0.10, 0.15], 6)
    lv_c = np.tile(np.repeat(["5%", "10%", "15%"], 2), 3)
    eff_f = {0.05: 0.0, 0.10: -5.0, 0.15: -8.0}
    eff_c = {"5%": 0.0, "10%": 2.0, "15%": 3.0}
    yy = np.array([eff_f[f] + eff_c[c] + (4.0 if (f == 0.15 and c == "15%") else 0.0)
                   for f, c in zip(lv_f, lv_c)]) + rng.normal(scale=0.05, size=18)
    syn = pd.DataFrame({"flow_lpm": lv_f, "C0_level": lv_c, "y": yy})
    a = two_way_anova(syn, "y")
    assert a["df_flow"] == 2 and a["df_conc"] == 2 and a["df_int"] == 4, a
    assert a["df_err"] == 9, a["df_err"]
    total = a["eta2_flow"] + a["eta2_conc"] + a["eta2_int"] + a["eta2_resid"]
    assert abs(total - 1.0) < 1e-9, total          # orthogonal when balanced
    assert a["sig_flow"] < 1e-6 and a["sig_int"] < 1e-6, a   # planted effects found

    # (h) with the interaction removed, the same design must report it absent
    syn["y"] = [eff_f[f] + eff_c[c] for f, c in zip(lv_f, lv_c)] + rng.normal(scale=0.05, size=18)
    b = two_way_anova(syn, "y")
    assert b["sig_int"] > 0.05, b["sig_int"]

    print("  self-check: 9/9 assertions passed "
          "(F vs scipy, quadratic SRC blindness, SRC==r, M01 closed form, "
          "q_dyn vs measured, Iman-Conover marginals, Type II SS decomposition, "
          "interaction recovered, interaction correctly absent)")


# ===========================================================================
# 10.  Output
# ===========================================================================
def write_workbook(path: Path, sheets: dict[str, pd.DataFrame]):
    path.parent.mkdir(parents=True, exist_ok=True)
    with pd.ExcelWriter(path, engine="openpyxl") as xl:
        for name, d in sheets.items():
            d.to_excel(xl, sheet_name=name[:31], index=False)
    print(f"  wrote {path.name} ({len(sheets)} sheets)")


def main(make_figs: bool = True):
    rng = np.random.default_rng(SEED)
    np.set_printoptions(suppress=True)
    pd.set_option("display.width", 200)
    pd.set_option("display.max_columns", 50)

    print("=" * 78)
    print("SENSITIVITY ANALYSIS BY ANOVA OF CLUSTERS IN SCATTERPLOTS")
    print("Kleijnen & Helton (1999a) CMNs/CLs tests; Saltelli et al. (2000) SRC")
    print("=" * 78)

    df = load_matrix()
    runs = df.drop_duplicates("run_id")
    print(f"\n[0] Data basis: {runs.run_id.nunique()} real runs "
          f"({(runs.dataset == 'newest').sum()} newest + {(runs.dataset == 'new').sum()} old), "
          f"{df.code.nunique()} models, {len(df)} fits.")
    print(runs[["run_id", "dataset", "flow_lpm", "C0_ppm", "bed_L_cm", "mass_g",
                "d_col_mm", "u_sup_mm_s"]].to_string(index=False))

    ref = reference_point(df)
    print(f"\n[0b] Self-checks")
    self_check(df, ref)

    codes, board = top_models(df, 3)
    n_all = runs.run_id.nunique()
    print(f"\n[0c] Model selection (pooled n={n_all} mean AICc rank, "
          "after bound-pinning screen):")
    print(board.head(8)[["code", "name", "rank", "max_frac_pinned",
                         "excluded", "reason"]]
          .to_string(index=False, float_format=lambda v: f"{v:.3f}"))
    print(f"     top-3 selected for parameter dissection: {codes}")

    # ---------------- Tier 1 ----------------
    print("\n" + "=" * 78)
    print("[1] TIER 1 - EXPERIMENTAL SENSITIVITY (model-free)")
    print("=" * 78)
    t1 = tier1(df)
    print("\n1a. Cluster ANOVA of scatterplots (clusters = design levels):")
    print(t1["cluster"][["scope", "factor", "response", "n", "k", "df1", "df2",
                         "F", "sig", "eta2", "sig_KW", "verdict"]]
          .to_string(index=False, float_format=lambda v: f"{v:.4g}"))
    print("\n1b. Two-way factorial ANOVA with replication, Type II SS:")
    print(t1["factorial"][["response", "n", "df_err", "F_flow", "sig_flow",
                           "F_conc", "sig_conc", "F_int", "sig_int",
                           "eta2_flow", "eta2_conc", "eta2_int", "eta2_resid"]]
          .to_string(index=False, float_format=lambda v: f"{v:.4g}"))
    print("\n1b-ii. Replicate reproducibility (pure error within cells):")
    print(t1["repro"].to_string(index=False, float_format=lambda v: f"{v:.4g}"))
    print("\n1c. Regression on operating conditions - coefficients:")
    print(t1["regression"].to_string(index=False, float_format=lambda v: f"{v:.4g}"))
    print("\n1d. Regression summary:")
    print(t1["reg_summary"].to_string(index=False, float_format=lambda v: f"{v:.4g}"))

    # ---------------- Tier 2 ----------------
    print("\n" + "=" * 78)
    print(f"[2] TIER 2 - MONTE CARLO PARAMETER SENSITIVITY (N = {N_MC}, seed {SEED})")
    print("=" * 78)
    print(f"    reference operating point: {ref['run_id']} "
          f"(Q = {ref['flow_m3_s']*60000:.2f} lpm, C0 = {ref['C0_ppm']:.0f} ppm, "
          f"m = {ref['mass_kg']*1000:.2f} g, L = {ref['bed_L_m']*100:.1f} cm)")
    t2 = tier2(df, codes, ref, rng)
    print("\n2-notes:")
    for n in t2["notes"]:
        print("  -", n)
    print("\n2a. Parameter distribution table (Table 1):")
    print(t2["dist"].to_string(index=False, float_format=lambda v: f"{v:.4g}"))
    print("\n2b. Cluster-ANOVA results (Table 4):")
    print(t2["cluster"][["model", "scheme", "parameter", "response", "n", "k",
                         "df1", "df2", "F", "sig", "eta2", "verdict"]]
          .to_string(index=False, float_format=lambda v: f"{v:.4g}"))
    print("\n2c. Regression results (Table 2):")
    print(t2["reg"].to_string(index=False, float_format=lambda v: f"{v:.4g}"))
    print("\n2d. Regression model summary (Table 3):")
    print(t2["summary"].to_string(index=False, float_format=lambda v: f"{v:.4g}"))

    # ---------------- Tier 3 ----------------
    print("\n" + "=" * 78)
    print("[3] TIER 3 - OPERATING CONDITION -> EMPIRICAL PARAMETER")
    print("=" * 78)
    t3_reg, t3_sum, t3_clus = tier3(df, codes)
    print("\n3a. Parameter ~ Q + C0, coefficients:")
    print(t3_reg.to_string(index=False, float_format=lambda v: f"{v:.4g}"))
    print("\n3b. Summary:")
    print(t3_sum.to_string(index=False, float_format=lambda v: f"{v:.4g}"))
    print("\n3c. Cluster ANOVA on the parameters themselves:")
    print(t3_clus.to_string(index=False, float_format=lambda v: f"{v:.4g}"))

    # ---------------- Figures + workbook ----------------
    if make_figs:
        print("\n" + "=" * 78)
        print("[4] FIGURES")
        print("=" * 78)
        fig_tier1(t1)
        fig_tier2(t2, codes)
        fig_identifiability(df, codes)
    else:
        import pickle
        CACHE.parent.mkdir(parents=True, exist_ok=True)
        with CACHE.open("wb") as fh:
            pickle.dump(dict(t1=t1, t2=t2, codes=codes), fh)
        print(f"\n[4] figures skipped; state cached to {CACHE.name}")

    print("\n[5] WORKBOOK")
    per_run = []
    for code in codes:
        pt = param_table(df, code)
        if code == "M24":
            pt = canonicalise_M24(pt)
        pt.insert(0, "model", code)
        per_run.append(pt)
    write_workbook(
        REPO / "src" / "docs" / "sensitivity_anova_tables.xlsx",
        {
            "T0_run_matrix": runs[["run_id", "dataset", "flow_lpm", "C0_ppm",
                                   "bed_L_cm", "mass_g", "d_col_mm", "T_K", "P_Pa",
                                   "C0_mol_m3", "u_sup_mm_s", *RESPONSES]],
            "T1_param_distribution": t2["dist"],
            "T1b_param_per_run": pd.concat(per_run, ignore_index=True),
            "T2_regression_MC": t2["reg"],
            "T3_regression_summary_MC": t2["summary"],
            "T4_cluster_anova_MC": t2["cluster"],
            "E1_cluster_anova_exp": t1["cluster"],
            "E2_factorial_anova": t1["factorial"],
            "E2b_replicate_reproducibility": t1["repro"],
            "E3_regression_exp": t1["regression"],
            "E4_regression_summary_exp": t1["reg_summary"],
            "P1_param_vs_conditions": t3_reg,
            "P2_param_vs_cond_summary": t3_sum,
            "P3_param_cluster_anova": t3_clus,
            "M0_model_selection": board,
            "M1_bound_pinning": bound_pinning(df),
            "notes": pd.DataFrame({"note": t2["notes"]}),
        },
    )
    print("\nDone.")
    return dict(df=df, t1=t1, t2=t2, t3=(t3_reg, t3_sum, t3_clus), codes=codes, ref=ref)


if __name__ == "__main__":
    # ponytail: two flags instead of an arg parser. --no-figs runs the analysis
    # and caches state; --figs-only redraws from that cache (figure rendering is
    # the slow half and is often the only thing being iterated on).
    if "--figs-only" in sys.argv:
        import pickle
        with CACHE.open("rb") as fh:
            st = pickle.load(fh)
        df = load_matrix()
        fig_tier1(st["t1"])
        fig_tier2(st["t2"], st["codes"])
        fig_identifiability(df, st["codes"])
    else:
        main(make_figs="--no-figs" not in sys.argv)

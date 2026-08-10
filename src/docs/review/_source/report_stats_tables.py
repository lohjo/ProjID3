"""Fit-statistics tables for the Final Report, rendered from committed artefacts.

Nothing here refits anything. Every number is read back out of
``src/solver/breakthrough_out/<run_id>/results_<run_id>.csv`` (the clean tree --
see the module note below) or out of ``src/docs/sensitivity_anova_tables.xlsx``.
The only arithmetic performed is:

* ΔAICc = AICc(model) − AICc(best in that run), a difference of two committed
  numbers;
* the nested F-test, computed with ``breakthrough_fit.stats.f_test`` -- the same
  function the pipeline itself calls -- over committed RSS and df.

Why ``src/solver/breakthrough_out/`` and not ``breakthrough_out/``: nine of the
sixteen results CSVs in the repo-root tree carry unresolved git merge-conflict
markers (``<<<<<<< HEAD`` / ``=======`` / ``>>>>>>>``), so they parse as 51 rows
instead of 24. Both conflict sides agree to ~1e-14 relative and side A is
byte-identical to the copy under ``src/solver/``. The root tree needs a real git
resolution; this module deliberately does not read it.

Every builder returns ``list[list[str]]`` with the header row first, which is the
shape ``insert_experiments_section.build_table`` consumes.
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
BT = REPO / "src/solver/breakthrough_out"
ANOVA_XLSX = REPO / "src/docs/sensitivity_anova_tables.xlsx"

sys.path.insert(0, str(REPO / "src" / "solver"))
from breakthrough_fit.fit import NESTED_PAIRS  # noqa: E402
from breakthrough_fit.stats import f_test  # noqa: E402

# --------------------------------------------------------------------------- #
# The measured basis: 21 real runs, two campaigns, never pooled.
# --------------------------------------------------------------------------- #
RUNS_OLD = ["run 3", "run 4", "run 5", "run 6", "run 8"]

RUNS_GRID = [
    "2026-06-26-conc5-flow0.05",
    "2026-07-03-conc5-flow0.10",
    "2026-07-08-conc5-flow0.15",
    "2026-07-08-conc10-flow0.05",
    "2026-07-08-conc10-flow0.10",
    "2026-07-08-conc10-flow0.15",
    "2026-07-10-conc15-flow0.05",
    "2026-07-10-conc15-flow0.10",
    "2026-07-15-conc15-flow0.15",
    "2026-07-17-conc15-flow0.10",
    "2026-07-22-conc10-flow0.05",
    "2026-07-22-conc10-flow0.10",
    "2026-07-29-conc5-flow0.05",
    "2026-07-29-conc5-flow0.10",
    "2026-07-31-conc5-flow0.15",
    "2026-07-31-conc10-flow0.10",
]

ALL_RUNS = RUNS_OLD + RUNS_GRID

# Short labels used in table cells so 504 rows stay readable.
SHORT = {r: r.replace("2026-", "").replace("-conc", " c").replace("-flow", " f")
         for r in RUNS_GRID}
SHORT.update({r: r for r in RUNS_OLD})

# Runs whose two stated flow rates disagree (prose header vs numeric cell `v`).
# parse.py reads the numeric cell, so these were fitted at that value; the prose
# value is the physical one on the t_b evidence. Owner: lab.
FLOW_CONFLICT = {
    "2026-07-22-conc10-flow0.05": (50, 100),
    "2026-07-22-conc10-flow0.10": (150, 100),
    "2026-07-31-conc10-flow0.10": (100, 50),
    "2026-07-31-conc5-flow0.15": (150, 100),
}
TRUNCATED = {"2026-07-29-conc5-flow0.05"}  # never reaches C/C0 = 0.95


# --------------------------------------------------------------------------- #
# Loading
# --------------------------------------------------------------------------- #
_CACHE: dict[str, pd.DataFrame] = {}


def load_results(run_id: str) -> pd.DataFrame:
    """One run's 24-model results table, with ΔAICc added."""
    if run_id in _CACHE:
        return _CACHE[run_id]
    path = BT / run_id / f"results_{run_id}.csv"
    df = pd.read_csv(path)
    if len(df) != 24 or df["run_id"].nunique() != 1:
        raise SystemExit(
            f"{path} is not a clean 24-row single-run table "
            f"({len(df)} rows, {df['run_id'].nunique()} run_ids) -- refusing to use it"
        )
    finite = df.loc[df["AICc"].apply(lambda v: math.isfinite(v)), "AICc"]
    best = finite.min() if len(finite) else float("nan")
    df["dAICc"] = df["AICc"] - best
    _CACHE[run_id] = df
    return df


def best_row(run_id: str) -> pd.Series:
    df = load_results(run_id)
    ok = df[df["converged"] & df["AICc"].apply(math.isfinite)]
    return ok.loc[ok["AICc"].idxmin()]


def _anova(sheet: str) -> pd.DataFrame:
    return pd.read_excel(ANOVA_XLSX, sheet_name=sheet)


# --------------------------------------------------------------------------- #
# Formatting
# --------------------------------------------------------------------------- #
def g(v, digits=4) -> str:
    """Compact fixed/scientific rendering that never loses a significant digit."""
    if v is None or (isinstance(v, float) and not math.isfinite(v)):
        return "n/a"
    try:
        f = float(v)
    except (TypeError, ValueError):
        return str(v)
    if f == 0:
        return "0"
    if f == int(f) and abs(f) < 1e6:
        return str(int(f))
    a = abs(f)
    if a >= 1e5 or a < 1e-3:
        return f"{f:.{digits}e}"
    return f"{f:.{max(0, digits - int(math.floor(math.log10(a))) - 1)}f}"


def r6(v) -> str:
    return g(v, 6)


def flag_suffix(run_id: str) -> str:
    marks = ""
    if run_id in FLOW_CONFLICT:
        marks += "*"
    if run_id in TRUNCATED:
        marks += "†"
    return marks


def run_label(run_id: str) -> str:
    return SHORT[run_id] + flag_suffix(run_id)


# --------------------------------------------------------------------------- #
# Body tables
# --------------------------------------------------------------------------- #
def tbl_fit_quality(runs: list[str]) -> list[list[str]]:
    """Best model by AICc against the M01 logistic baseline, one row per run."""
    head = ["Run", "n", "Best model (AICc)", "p", "R²", "Adj R²", "RMSE",
            "AICc", "ΔAICc vs M01", "M01 Adj R²", "M01 RMSE"]
    rows = [head]
    for r in runs:
        df = load_results(r)
        b = best_row(r)
        m01 = df[df["code"] == "M01"].iloc[0]
        rows.append([
            run_label(r), f"{int(b['n'])}", f"{b['code']} {b['name']}", f"{int(b['p'])}",
            r6(b["R2"]), r6(b["AdjR2"]), g(b["RMSE"], 4), g(b["AICc"], 6),
            g(m01["AICc"] - b["AICc"], 5), r6(m01["AdjR2"]), g(m01["RMSE"], 4),
        ])
    return rows


def tbl_model_ranking(runs: list[str]) -> list[list[str]]:
    """All 24 models ranked by mean Adj R2 over the campaign."""
    recs: dict[str, dict] = {}
    for r in runs:
        for _, row in load_results(r).iterrows():
            d = recs.setdefault(row["code"], {"name": row["name"], "adj": [],
                                              "rmse": [], "daicc": [], "wins": 0,
                                              "conv": 0, "n": 0})
            d["n"] += 1
            if row["converged"]:
                d["conv"] += 1
            if math.isfinite(row["AdjR2"]):
                d["adj"].append(float(row["AdjR2"]))
            if math.isfinite(row["RMSE"]):
                d["rmse"].append(float(row["RMSE"]))
            if math.isfinite(row["dAICc"]):
                d["daicc"].append(float(row["dAICc"]))
        recs[best_row(r)["code"]]["wins"] += 1

    def mean(xs):
        return sum(xs) / len(xs) if xs else float("nan")

    def median(xs):
        if not xs:
            return float("nan")
        s = sorted(xs)
        m = len(s) // 2
        return s[m] if len(s) % 2 else 0.5 * (s[m - 1] + s[m])

    order = sorted(recs.items(),
                   key=lambda kv: (-mean(kv[1]["adj"]) if kv[1]["adj"] else 1e9))
    head = ["Rank", "Code", "Model", "Mean Adj R²", "Median Adj R²",
            "Mean RMSE", "Mean ΔAICc", "Runs won", "Converged / n"]
    rows = [head]
    for i, (code, d) in enumerate(order, start=1):
        rows.append([
            str(i), code, d["name"], r6(mean(d["adj"])), r6(median(d["adj"])),
            g(mean(d["rmse"]), 4), g(mean(d["daicc"]), 5), str(d["wins"]),
            f"{d['conv']} / {d['n']}",
        ])
    return rows


def tbl_ftest(runs: list[str], pairs=(("M01", "M23"),)) -> list[list[str]]:
    """Nested F-test rows, computed with the pipeline's own f_test()."""
    head = ["Run", "Simple", "Complex", "RSS simple", "RSS complex", "df simple",
            "df complex", "F", "p", "Extra term warranted"]
    rows = [head]
    for r in runs:
        df = load_results(r).set_index("code")
        for simple, complex_ in pairs:
            if simple not in df.index or complex_ not in df.index:
                continue
            a, b = df.loc[simple], df.loc[complex_]
            if not (bool(a["converged"]) and bool(b["converged"])):
                continue
            n = int(a["n"])
            df1, df2 = max(n - int(a["p"]), 1), max(n - int(b["p"]), 1)
            p = f_test(float(a["RSS"]), float(b["RSS"]), df1, df2)
            ddf = df1 - df2
            F = (((float(a["RSS"]) - float(b["RSS"])) / ddf) / (float(b["RSS"]) / df2)
                 if ddf > 0 and float(b["RSS"]) > 0 else float("nan"))
            rows.append([
                run_label(r), simple, complex_, g(a["RSS"], 6), g(b["RSS"], 6),
                str(df1), str(df2), g(F, 6),
                ("< 1e-300" if p == 0 else g(p, 3)),
                "yes" if (math.isfinite(p) and p < 0.05) else "no",
            ])
    return rows


# --------------------------------------------------------------------------- #
# Sensitivity / ANOVA tables (straight out of the generated workbook)
# --------------------------------------------------------------------------- #
def _sheet_rows(sheet: str, cols: list[str], headers: list[str],
                digits: int = 4) -> list[list[str]]:
    df = _anova(sheet)
    missing = [c for c in cols if c not in df.columns]
    if missing:
        raise SystemExit(f"{sheet}: missing columns {missing}")
    rows = [headers]
    for _, r in df[cols].iterrows():
        rows.append([r[c] if isinstance(r[c], str) else g(r[c], digits) for c in cols])
    return rows


def tbl_e1_cluster_anova() -> list[list[str]]:
    return _sheet_rows(
        "E1_cluster_anova_exp",
        ["scope", "factor", "response", "n", "k", "df1", "df2", "F", "sig",
         "eta2", "q_BH", "verdict"],
        ["Scope", "Factor", "Response", "n", "k", "df1", "df2", "F", "p",
         "η²", "q (BH)", "Verdict"],
    )


def tbl_e2_factorial() -> list[list[str]]:
    return _sheet_rows(
        "E2_factorial_anova",
        ["response", "n", "F_flow", "sig_flow", "F_conc", "sig_conc", "F_int",
         "sig_int", "eta2_flow", "eta2_conc", "eta2_int", "eta2_resid"],
        ["Response", "n", "F flow", "p flow", "F conc", "p conc", "F flow×conc",
         "p int", "η² flow", "η² conc", "η² int", "η² resid"],
    )


def tbl_e2b_reproducibility() -> list[list[str]]:
    return _sheet_rows(
        "E2b_replicate_reproducibility",
        ["response", "n_cells_replicated", "pure_error_sd", "total_sd",
         "pure_error_frac_of_total_var", "median_within_cell_CV",
         "max_within_cell_CV", "worst_cell_ratio"],
        ["Response", "Replicated cells", "Pure-error SD", "Total SD",
         "Pure error / total var.", "Median within-cell CV", "Max within-cell CV",
         "Worst cell ratio"],
    )


def tbl_bound_pinning() -> list[list[str]]:
    df = _anova("M1_bound_pinning")
    df = df[df["n_pinned"] > 0]
    rows = [["Code", "Model", "Parameter", "Lower", "Upper", "Runs", "Pinned",
             "Fraction pinned"]]
    for _, r in df.iterrows():
        rows.append([r["code"], r["name"], r["parameter"], g(r["lower"], 4),
                     g(r["upper"], 4), str(int(r["n_runs"])), str(int(r["n_pinned"])),
                     g(r["frac_pinned"], 3)])
    return rows


def tbl_model_screen() -> list[list[str]]:
    return _sheet_rows(
        "M0_model_selection",
        ["code", "name", "rank", "max_frac_pinned", "excluded", "reason"],
        ["Code", "Model", "Rank", "Max fraction pinned", "Excluded", "Reason"],
        digits=3,
    )


# --------------------------------------------------------------------------- #
# Appendix B
# --------------------------------------------------------------------------- #
B1_HEAD = ["Run", "Code", "Model", "Conv.", "n", "p", "RSS", "R²", "Adj R²",
           "RMSE", "χ²_red", "AICc", "ΔAICc", "AAD"]


def tbl_b1_master(runs: list[str] = None) -> list[list[str]]:
    """Every model of every run: 24 x 21 = 504 rows."""
    runs = runs or ALL_RUNS
    rows = [B1_HEAD]
    for r in runs:
        for _, m in load_results(r).iterrows():
            rows.append([
                run_label(r), m["code"], m["name"], "yes" if m["converged"] else "no",
                str(int(m["n"])), str(int(m["p"])), g(m["RSS"], 6), r6(m["R2"]),
                r6(m["AdjR2"]), g(m["RMSE"], 4), g(m["chi2_red"], 4),
                g(m["AICc"], 6), g(m["dAICc"], 5), g(m["AAD"], 4),
            ])
    return rows


def tbl_b2_parameters(runs: list[str] = None) -> list[list[str]]:
    """Fitted parameter values with curve_fit's asymptotic standard errors."""
    runs = runs or ALL_RUNS
    rows = [["Run", "Code", "Model", "Fitted parameters ± SE"]]
    for r in runs:
        for _, m in load_results(r).iterrows():
            vals = str(m["params"]) if isinstance(m["params"], str) else ""
            errs = str(m["stderr"]) if isinstance(m["stderr"], str) else ""
            vmap = dict(kv.split("=", 1) for kv in vals.split(";") if "=" in kv)
            emap = dict(kv.split("=", 1) for kv in errs.split(";") if "=" in kv)
            parts = []
            for k, v in vmap.items():
                e = emap.get(k)
                parts.append(f"{k} = {v} ± {e}" if e else f"{k} = {v}")
            rows.append([run_label(r), m["code"], m["name"],
                         "; ".join(parts) if parts else "not estimated"])
    return rows


def tbl_b3_ftests(runs: list[str] = None) -> list[list[str]]:
    """All six nested pairs the pipeline tests, for every run."""
    return tbl_ftest(runs or ALL_RUNS, pairs=NESTED_PAIRS)


def tbl_b4_degenerate(runs: list[str] = None) -> list[list[str]]:
    """Models that did not converge, or converged to a non-finite / negative fit."""
    runs = runs or ALL_RUNS
    rows = [["Run", "Code", "Model", "Converged", "Adj R²", "AICc", "Message"]]
    for r in runs:
        for _, m in load_results(r).iterrows():
            bad = (not bool(m["converged"])
                   or not math.isfinite(float(m["AdjR2"]))
                   or float(m["AdjR2"]) < 0
                   or not math.isfinite(float(m["AICc"])))
            if bad:
                rows.append([run_label(r), m["code"], m["name"],
                             "yes" if m["converged"] else "no",
                             r6(m["AdjR2"]), g(m["AICc"], 6),
                             str(m["message"])[:60]])
    return rows


def tbl_a1_index(fig_start: dict[str, int]) -> list[list[str]]:
    """Appendix A contents: one row per run, with its figure range."""
    import json
    passport = json.loads((REPO / "src/docs/experiments_passport.json")
                          .read_text(encoding="utf8"))
    meta = {e["run_id"]: e for e in passport["experiments_provenance"]}
    old = pd.read_csv(REPO / "src/img/generated/may_prompt/table1_physical.csv") \
        .set_index("run_id")
    rows = [["Run", "Campaign", "Q (mL/min)", "C₀ (ppm)", "m (g)",
             "L_bed (cm)", "d_col (mm)", "n points", "Best model", "Figures"]]
    for r in ALL_RUNS:
        s = fig_start[r]
        figs = f"A{s}–A{s + 6}"
        if r in RUNS_OLD:
            o = old.loc[r]
            df = load_results(r)
            rows.append([r, "new runs (5-run)", f"{o['Q_lpm'] * 1000:.0f}",
                         "see Table 7", f"{o['m_g']:.4g}", f"{o['L_bed_cm']:.1f}",
                         "8.5", str(int(df['n'].max())),
                         best_row(r)["code"], figs])
        else:
            e = meta[r]
            m, d = e["measured"], e["derived"]
            rows.append([
                run_label(r), "newest runs (3×3 grid)",
                f"{e['flow_ml_min']['used_by_pipeline']:.0f}",
                f"{m['C0_ppm']:.0f}", f"{m['mass_g']:.2f}", f"{m['L_bed_cm']:.2f}",
                f"{m['d_col_mm']:.1f}", str(m["n_points"]),
                d["best_model_code"], figs,
            ])
    return rows


if __name__ == "__main__":  # smoke test
    for name, t in [
        ("fit quality grid", tbl_fit_quality(RUNS_GRID)),
        ("fit quality old", tbl_fit_quality(RUNS_OLD)),
        ("ranking grid", tbl_model_ranking(RUNS_GRID)),
        ("ranking old", tbl_model_ranking(RUNS_OLD)),
        ("ftest M01-M23", tbl_ftest(ALL_RUNS)),
        ("E1", tbl_e1_cluster_anova()),
        ("E2", tbl_e2_factorial()),
        ("E2b", tbl_e2b_reproducibility()),
        ("pinning", tbl_bound_pinning()),
        ("screen", tbl_model_screen()),
        ("B1", tbl_b1_master()),
        ("B2", tbl_b2_parameters()),
        ("B3", tbl_b3_ftests()),
        ("B4", tbl_b4_degenerate()),
    ]:
        print(f"{name:20s} {len(t) - 1:4d} data rows x {len(t[0])} cols")

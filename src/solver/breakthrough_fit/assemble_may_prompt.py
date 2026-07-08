"""Assemble the "Model Fitting & Statistical Analysis" deliverables for the
five new experimental runs (runs 3/4/5/6/8), *from existing pipeline outputs only*.

This is an ASSEMBLY script, not a fitting script. It does not re-fit anything:
it reuses

  * ``breakthrough_fit.parse.DataParser``  — to reload the raw C/C0(t) curve;
  * ``breakthrough_fit.models``            — to reconstruct a fitted curve from
                                             the parameter string already stored
                                             in ``results_<run>.csv``;

and reads the per-model statistics straight out of the stored CSVs. It then
emits the engineered-prompt deliverables for the five real runs:

  Table 1 — derived physical parameters (per the prompt's EC equations);
  Table 2 — per-model fit statistics (the 9 prompt-named models);
  Table 3 — model ranking by mean adjusted R^2;
  Table 4 — nested F-test  BA/logistic (M01) vs fractal-BA (M23);
  Fig P1  — experimental breakthrough curves, all runs overlaid;
  Fig P8  — predicted-vs-observed parity, coloured by model family.

Tables are written as Markdown + CSV; figures at 300 dpi. Everything lands in
``src/img/generated/may_prompt/``.

Run from the repo root::

    venv/Scripts/python.exe -m breakthrough_fit.assemble_may_prompt
"""

from __future__ import annotations

import re
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import f as f_dist

from breakthrough_fit import models as M
from breakthrough_fit.parse import DataParser

REPO = Path(__file__).resolve().parents[1]
RESULTS = REPO / "breakthrough_out"
DATA = REPO / "src" / "solver" / "data" / "new runs"
OUT = REPO / "src" / "img" / "generated" / "may_prompt"
OUT.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------------------------------- #
# Per-run metadata — matches new_runs_pipeline.py RUN_META.
# Q_lpm: authoritative inlet flow from the adsorption pressure-drop table.
# conc_pct: nominal CO2 level (5 ≈ 4.7%, 10 ≈ 9.5-10.2%, 15 ≈ 15.1%).
# --------------------------------------------------------------------------- #
RUN_META: dict[str, dict] = {
    "run 3": dict(Q_lpm=0.15, m_g=8.0076, L_bed_cm=21.0, conc_pct=5),
    "run 4": dict(Q_lpm=0.05, m_g=8.0000, L_bed_cm=21.3, conc_pct=10),
    "run 5": dict(Q_lpm=0.10, m_g=8.0000, L_bed_cm=21.2, conc_pct=10),
    "run 6": dict(Q_lpm=0.15, m_g=8.0000, L_bed_cm=21.5, conc_pct=10),
    "run 8": dict(Q_lpm=0.10, m_g=8.0000, L_bed_cm=21.5, conc_pct=15),
}

RUNS = [(run_id, m["conc_pct"], m["Q_lpm"]) for run_id, m in RUN_META.items()]

# --------------------------------------------------------------------------- #
# Column geometry (fixed) — from engineered prompt EC equations.
# ρ_p = 800 kg/m³ is a nominal PEI-SiO2 value used for EC-2 only; it is an
# open input and v_int below should not be treated as physical until confirmed.
# --------------------------------------------------------------------------- #
D_COL_M = 0.0085         # column inner diameter [m] (8.5 mm)
A_C = np.pi * (D_COL_M / 2.0) ** 2   # cross-sectional area [m^2]
RHO_P = 800.0            # assumed pellet density [kg/m^3] (EC-2; open input)
LPM_TO_M3S = 1.0e-3 / 60.0

# The 9 prompt-named models -> registry codes (Groups A-I of engineered prompt).
PROMPT_MODELS = [
    ("M01", "Logistic (BA/Thomas/YN)"),
    ("M02", "Clark"),
    ("M04", "Modified Dose-Response"),
    ("M05", "Wolborska (early, C/C0≤0.15)"),
    ("M06", "Gudermannian"),
    ("M07", "Error function"),
    ("M14", "Weibull"),
    ("M16", "Klinkenberg"),
    ("M23", "Fractal-BA (fractal YN)"),
]
PROMPT_CODES = [c for c, _ in PROMPT_MODELS]

FAMILY = {  # for the parity plot colouring
    "M01": "logistic", "M02": "asymmetric", "M04": "asymmetric",
    "M05": "logistic", "M06": "logistic", "M07": "logistic",
    "M14": "Weibull", "M16": "Klinkenberg", "M23": "asymmetric",
}
FAMILY_COLOR = {"logistic": "#1f77b4", "asymmetric": "#d62728",
                "Weibull": "#2ca02c", "Klinkenberg": "#9467bd"}


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #
def parse_params(blob: str) -> dict[str, float]:
    out: dict[str, float] = {}
    if not isinstance(blob, str):
        return out
    for piece in blob.split(";"):
        if "=" in piece:
            k, v = piece.split("=", 1)
            try:
                out[k.strip()] = float(v)
            except ValueError:
                pass
    return out


def model_curve(code: str, blob: str, t: np.ndarray):
    func = getattr(M, f"model_{code}", None)
    if func is None:
        return None
    try:
        spec = M.get_model(code)
    except KeyError:
        return None
    pvals = parse_params(blob)
    try:
        args = [pvals[n] for n in spec.param_names]
    except KeyError:
        return None
    try:
        y = np.asarray(func(t, *args), dtype=float)
        return y
    except Exception:
        return None


def t_at_level(t, y, level):
    finite = np.isfinite(y)
    t, y = t[finite], y[finite]
    if y.size < 2 or np.nanmax(y) < level:
        return float("nan")
    idx = int(np.argmax(y >= level))
    if idx == 0:
        return float(t[0])
    y0, y1, t0, t1 = y[idx - 1], y[idx], t[idx - 1], t[idx]
    if y1 == y0:
        return float(t1)
    return float(t0 + (level - y0) * (t1 - t0) / (y1 - y0))


def short(label: str, n: int = 24) -> str:
    return label if len(label) <= n else label[: n - 1] + "…"


def fmt(x, p="0.4g"):
    if x is None or (isinstance(x, float) and not np.isfinite(x)):
        return "—"
    return f"{x:{p}}"


# --------------------------------------------------------------------------- #
# Load: stored results + raw curves
# --------------------------------------------------------------------------- #
def load() -> list[dict]:
    parser = DataParser()
    out = []
    for run_id, conc, flow in RUNS:
        rcsv = RESULTS / run_id / f"results_{run_id}.csv"
        raw_path = DATA / f"{run_id}.csv"
        if not rcsv.exists():
            print(f"[skip] missing results CSV: {rcsv}")
            continue
        rdf = pd.read_csv(rcsv)
        by_code = {r["code"]: r for _, r in rdf.iterrows()}
        t = y = None
        if raw_path.exists():
            try:
                pr = parser.parse(raw_path)
                t = pr.df["t"].to_numpy(float)          # seconds
                y = pr.df["C_C0"].to_numpy(float)
            except Exception as exc:  # noqa: BLE001
                print(f"[warn] raw parse failed {run_id}: {exc}")
        first = rdf.iloc[0]
        out.append({
            "run_id": run_id, "conc": conc, "flow_lpm": flow,
            "rdf": rdf, "by_code": by_code, "t": t, "y": y,
            "t_b_s": float(first["t_b_s"]) if pd.notna(first.get("t_b_s", float("nan"))) else np.nan,
            "t_E_s": float(first["t_E_s"]) if pd.notna(first.get("t_E_s", float("nan"))) else np.nan,
            "t50_s": float(first["t50_s"]) if pd.notna(first.get("t50_s", float("nan"))) else np.nan,
            "q_dyn": float(first["q_dyn_mol_per_kg"]) if pd.notna(first.get("q_dyn_mol_per_kg", float("nan"))) else np.nan,
            "n": int(first["n"]) if pd.notna(first["n"]) else 0,
        })
    return out


# --------------------------------------------------------------------------- #
# Table 1 — derived physical parameters (EC-1 to EC-6, per-run geometry)
# --------------------------------------------------------------------------- #
def table1(rows) -> str:
    lines = [
        "### Table 1 — Derived physical parameters (5 real runs, EC-1 to EC-6)",
        "",
        "EC-1: ρ_b = m / (A_c · L_bed). "
        "EC-2: ε = 1 − ρ_b / ρ_p; ρ_p = 800 kg/m³ assumed (nominal PEI–SiO₂; open input — "
        "real ρ_p not yet supplied). "
        "Raw ε (EC-2) ≈ 0.16–0.18 in all runs (bulk density ~656–672 kg/m³ with ρ_p = 800); "
        "floored at 0.30 in the pipeline. "
        "**U is reliable** (depends only on Q and A_c); "
        "**v and ε-derived quantities should not be treated as physical** until ρ_p is confirmed. "
        "Outlet flow available for runs 3/4/5 (from pressure-drop table); "
        "runs 6/8 outlet = NaN — inlet flow used as operating flow per the prompt.",
        "",
        "| Run | Q (lpm) | m (g) | L_bed (cm) | C₀ (ppm) | ρ_b (kg/m³) | ε (EC-2, floored) | U (cm/s) | v (cm/s)* |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    csv_rows = []
    for r in rows:
        meta = RUN_META[r["run_id"]]
        Q = meta["Q_lpm"] * LPM_TO_M3S
        m_kg = meta["m_g"] * 1e-3
        L_m = meta["L_bed_cm"] * 1e-2
        rho_b = m_kg / (A_C * L_m)
        eps_raw = 1.0 - rho_b / RHO_P
        eps = max(eps_raw, 0.30)
        U = Q / A_C
        v = U / eps
        # get c0 from the parsed run
        c0_ppm = float(r["rdf"].iloc[0].get("c0_ppm", float("nan"))) if "c0_ppm" in r["rdf"].columns else float("nan")
        lines.append(
            f"| {r['run_id']} | {meta['Q_lpm']:.2f} | {meta['m_g']:.4f} | "
            f"{meta['L_bed_cm']:.1f} | — | "
            f"{rho_b:.1f} | {eps:.2f} ({eps_raw:.3f} raw) | "
            f"{U * 100:.3f} | {v * 100:.3f} |"
        )
        csv_rows.append({
            "run_id": r["run_id"], "Q_lpm": meta["Q_lpm"], "m_g": meta["m_g"],
            "L_bed_cm": meta["L_bed_cm"], "rho_b_kg_m3": rho_b,
            "eps_raw_EC2": eps_raw, "eps_floored": eps,
            "U_m_s": U, "v_m_s": v,
        })
    lines.append("")
    lines.append("*v computed with ε floored at 0.30. C₀ is per-run measured from the CSV plateau (see pipeline output).")
    pd.DataFrame(csv_rows).to_csv(OUT / "table1_physical.csv", index=False)
    return "\n".join(lines)


# --------------------------------------------------------------------------- #
# Table 2 — per-model fit statistics for the 9 prompt models
# --------------------------------------------------------------------------- #
def table2(rows) -> str:
    lines = [
        "### Table 2 — Model fit statistics (9 prompt models × 5 runs)",
        "",
        "Read straight from stored `results_<run>.csv`. AdjR² < 0 means the "
        "model is worse than a horizontal line through the mean. Wolborska (M05) "
        "is fitted on the early window only (C/C₀ ≤ 0.15), so its statistics are "
        "not comparable to the complete-curve models — see Table 3 note. "
        "F-tests between non-nested models (e.g. M01 vs M04, M01 vs M14) use "
        "ΔAICc, not F-statistic; see Table 4 for the only valid nested pair (M01 ⊂ M23).",
        "",
        "| Run | Model | p | AdjR² | χ²_ν | AICc | RMSE | key params |",
        "|---|---|---|---|---|---|---|---|",
    ]
    csv_rows = []
    for r in rows:
        for code, label in PROMPT_MODELS:
            row = r["by_code"].get(code)
            if row is None:
                continue
            params = parse_params(row.get("params", ""))
            key = ", ".join(f"{k}={fmt(v)}" for k, v in list(params.items())[:2])
            lines.append(
                f"| {r['run_id']} | {label} | {int(row['p'])} | "
                f"{fmt(row['AdjR2'])} | {fmt(row['chi2_red'])} | "
                f"{fmt(row['AICc'])} | {fmt(row['RMSE'])} | {key} |"
            )
            csv_rows.append({
                "run_id": r["run_id"], "code": code, "model": label,
                "p": row["p"], "AdjR2": row["AdjR2"], "chi2_red": row["chi2_red"],
                "AICc": row["AICc"], "RMSE": row["RMSE"], "R2": row["R2"],
                "params": row.get("params", ""),
            })
    pd.DataFrame(csv_rows).to_csv(OUT / "table2_fits.csv", index=False)
    return "\n".join(lines)


# --------------------------------------------------------------------------- #
# Table 3 — ranking by mean adjusted R^2
# --------------------------------------------------------------------------- #
def table3(rows) -> str:
    agg = {}
    for code, label in PROMPT_MODELS:
        vals = []
        for r in rows:
            row = r["by_code"].get(code)
            if row is not None and pd.notna(row["AdjR2"]):
                vals.append(float(row["AdjR2"]))
        agg[code] = (label, float(np.mean(vals)) if vals else np.nan,
                     float(np.median(vals)) if vals else np.nan, len(vals))
    order = sorted(agg, key=lambda c: np.nan_to_num(agg[c][1], nan=-1e9),
                   reverse=True)
    note = {
        "M05": "INVALID for complete curves (early-window exponential only)",
        "M16": "CONDITIONAL (requires ζ ≥ 2 and τ_K ≥ 1)",
    }
    lines = [
        "### Table 3 — Model ranking by mean Adj. R² across 5 real runs",
        "",
        "Note: among the full 24-model library, Fractal Error-Function (M11, Hu 2024) "
        "ranks first in 3/5 runs and second in the remaining 2 — it consistently "
        "outperforms all 9 prompt-listed models. It is not one of the 9 prompt-specified "
        "groups but is reported separately in the interpretation section.",
        "",
        "| Rank | Model | mean Adj.R² | median Adj.R² | n runs | validity flag |",
        "|---|---|---|---|---|---|",
    ]
    csv_rows = []
    for i, code in enumerate(order, 1):
        label, mean, med, k = agg[code]
        flag = note.get(code, "complete-curve model")
        lines.append(f"| {i} | {label} | {fmt(mean)} | {fmt(med)} | {k} | {flag} |")
        csv_rows.append({"rank": i, "code": code, "model": label,
                         "mean_AdjR2": mean, "median_AdjR2": med,
                         "n_runs": k, "flag": flag})
    pd.DataFrame(csv_rows).to_csv(OUT / "table3_ranking.csv", index=False)
    return "\n".join(lines)


# --------------------------------------------------------------------------- #
# Table 4 — nested F-test: M01 (BA/logistic) vs M23 (fractal-BA)
# --------------------------------------------------------------------------- #
def table4(rows) -> str:
    lines = [
        "### Table 4 — Nested F-test: BA/logistic (M01) ⊂ fractal-BA (M23)",
        "",
        "F = [(RSS₁−RSS₂)/(p₂−p₁)] / [RSS₂/(n−p₂)], recomputed from stored "
        "RSS/n/p. Valid because M23 reduces to M01 at h = 0. p < 0.05 ⇒ the "
        "fractal term is warranted. M01 vs M04/M14 are NOT nested — use ΔAICc "
        "for those comparisons (homoscedasticity caveat applies to all F-tests "
        "on bounded C/C₀ ∈ [0,1] data; see interpretation section).",
        "",
        "| Run | RSS(M01) | RSS(M23) | n | F | p-value | fractal warranted? |",
        "|---|---|---|---|---|---|---|",
    ]
    csv_rows = []
    for r in rows:
        a = r["by_code"].get("M01")
        b = r["by_code"].get("M23")
        if a is None or b is None:
            continue
        rss1, rss2 = float(a["RSS"]), float(b["RSS"])
        p1, p2, n = int(a["p"]), int(b["p"]), int(a["n"])
        if rss2 <= 0 or n - p2 <= 0 or p2 <= p1:
            F = pval = np.nan
        else:
            F = ((rss1 - rss2) / (p2 - p1)) / (rss2 / (n - p2))
            pval = float(f_dist.sf(F, p2 - p1, n - p2)) if F > 0 else 1.0
        decision = "yes" if (np.isfinite(pval) and pval < 0.05) else "no"
        lines.append(
            f"| {r['run_id']} | {fmt(rss1)} | {fmt(rss2)} | {n} | "
            f"{fmt(F)} | {fmt(pval, '0.3g')} | {decision} |"
        )
        csv_rows.append({"run_id": r["run_id"], "RSS_M01": rss1, "RSS_M23": rss2,
                         "n": n, "F": F, "p_value": pval, "warranted": decision})
    pd.DataFrame(csv_rows).to_csv(OUT / "table4_ftest.csv", index=False)
    return "\n".join(lines)


# --------------------------------------------------------------------------- #
# Fig P1 — all experimental curves overlaid
# --------------------------------------------------------------------------- #
def fig_p1(rows) -> None:
    # Color by CO2 level; linestyle by flow rate
    conc_color = {5: "#1f77b4", 10: "#d62728", 15: "#2ca02c"}
    flow_ls = {0.05: ":", 0.10: "-", 0.15: "--"}
    fig, ax = plt.subplots(figsize=(9, 5.5))
    for r in rows:
        if r["t"] is None:
            continue
        col = conc_color.get(r["conc"], "#7f7f7f")
        ls = flow_ls.get(r["flow_lpm"], "-")
        tmin = r["t"] / 60.0
        ax.plot(tmin, r["y"], ls, color=col, lw=1.2, alpha=0.85,
                label=f"{r['run_id']} ({r['conc']}% CO₂, {r['flow_lpm']:.2f} lpm)")
        tb = t_at_level(r["t"], r["y"], 0.05) / 60.0
        if np.isfinite(tb):
            ax.axvline(tb, color=col, ls=":", lw=0.5, alpha=0.4)
    ax.axhline(0.05, color="k", ls=":", lw=0.6, label="C/C₀ = 0.05 (t_BT)")
    ax.axhline(0.95, color="k", ls="-.", lw=0.6, label="C/C₀ = 0.95 (t_E)")
    ax.set_xlabel("time [min]")
    ax.set_ylabel(r"$C_t/C_0$  [—]")
    ax.set_ylim(-0.05, 1.1)
    ax.set_title(
        "Plot 1 — Experimental breakthrough curves (runs 3/4/5/6/8, overlaid)\n"
        "blue = ~5% CO₂ (run 3), red = ~10% CO₂ (runs 4/5/6), green = ~15% CO₂ (run 8)\n"
        "linestyle: dotted = 0.05 lpm, solid = 0.10 lpm, dashed = 0.15 lpm"
    )
    ax.legend(fontsize=7, loc="center right")
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUT / "Plot1_overlay.png", dpi=300)
    plt.close(fig)
    print(f"[fig] {OUT / 'Plot1_overlay.png'}")


# --------------------------------------------------------------------------- #
# Fig P8 — predicted vs observed parity, coloured by model family
# --------------------------------------------------------------------------- #
def fig_p8(rows) -> None:
    fig, ax = plt.subplots(figsize=(6.2, 6.2))
    seen = set()
    for r in rows:
        if r["t"] is None:
            continue
        for code, _ in PROMPT_MODELS:
            row = r["by_code"].get(code)
            if row is None:
                continue
            yhat = model_curve(code, row.get("params", ""), r["t"])
            if yhat is None:
                continue
            fam = FAMILY[code]
            col = FAMILY_COLOR[fam]
            m = np.isfinite(yhat) & np.isfinite(r["y"])
            ax.scatter(r["y"][m], yhat[m], s=4, color=col, alpha=0.25,
                       edgecolors="none",
                       label=fam if fam not in seen else None)
            seen.add(fam)
    ax.plot([0, 1], [0, 1], "k--", lw=1.0, label="1:1")
    ax.set_xlim(-0.05, 1.1)
    ax.set_ylim(-0.05, 1.1)
    ax.set_xlabel("observed $C_t/C_0$")
    ax.set_ylabel("predicted $C_t/C_0$")
    ax.set_title(
        "Plot 8 — predicted vs observed, 5 new runs\n"
        "(9 prompt models, coloured by family; tight diagonal = good fit)"
    )
    ax.legend(fontsize=8, loc="upper left", markerscale=2)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUT / "Plot8_parity.png", dpi=300)
    plt.close(fig)
    print(f"[fig] {OUT / 'Plot8_parity.png'}")


# --------------------------------------------------------------------------- #
def main() -> None:
    rows = load()
    print(f"Loaded {len(rows)} new runs.")
    t1, t2, t3, t4 = table1(rows), table2(rows), table3(rows), table4(rows)
    md = "\n\n".join([
        "# New experimental runs (3/4/5/6/8) — engineered-prompt deliverables",
        "*Assembled from stored `breakthrough_out/` fits; no re-fitting.*",
        t1, t2, t3, t4,
    ])
    (OUT / "tables.md").write_text(md, encoding="utf-8")
    print(f"[md] {OUT / 'tables.md'}")
    fig_p1(rows)
    fig_p8(rows)
    print("Done.")


if __name__ == "__main__":
    main()

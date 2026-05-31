"""Assemble the "Model Fitting & Statistical Analysis" deliverables for the
seven dated May-2026 diagnostic runs, *from existing pipeline outputs only*.

This is an ASSEMBLY script, not a fitting script. It does not re-fit anything:
it reuses

  * ``breakthrough_fit.parse.DataParser``  — to reload the raw C/C0(t) curve;
  * ``breakthrough_fit.models``            — to reconstruct a fitted curve from
                                             the parameter string already stored
                                             in ``results_<run>.csv``;

and reads the per-model statistics straight out of the stored CSVs. It then
emits the engineered-prompt deliverables for the May runs:

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
DATA = REPO / "src" / "solver" / "data"
OUT = REPO / "src" / "img" / "generated" / "may_prompt"
OUT.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------------------------------- #
# Run inventory — the seven dated May-2026 diagnostic runs.
# flow_lpm is parsed from the file name and treated as litres/min per the
# engineered prompt's "Inlet flow (lpm)" column. conc_pct is the nominal CO2
# set-point encoded in the name (conc5 ~ 4-6 %, conc10 ~ 10-11 %).
# --------------------------------------------------------------------------- #
RUNS = [
    ("May-20-2026Run2conc5_flow0.1", 5, 0.10),
    ("May-20-2026conc5_flow1.5", 5, 1.50),
    ("May-20-2026conc5_flow1.5(2)", 5, 1.50),
    ("May-20-2026conc5_flow1.5(3)", 5, 1.50),
    ("May-22-2026-conc10-flow0.05", 10, 0.05),
    ("May-22-2026-conc10-flow0.1", 10, 0.10),
    ("May-22-2026-conc10_flow-0.1(2)", 10, 0.10),
]

# --------------------------------------------------------------------------- #
# Geometry / physical assumptions — taken from the engineered prompt's
# "Column Geometry" + "Per-Run Measurements" tables, because Format-A logs
# carry no flow/mass/geometry. FLAGGED in Table 1: these values are
# internally inconsistent (8 g cannot pack a 21 cm x 85 mm bed).
# --------------------------------------------------------------------------- #
D_COL_M = 0.085          # column inner diameter, 85 mm
A_C = np.pi * (D_COL_M / 2.0) ** 2   # cross-sectional area [m^2]
L_BED_M = 0.210          # per-run bed length ~21 cm (prompt runs 1-9, assumed)
MASS_KG = 8.00e-3        # sorbent mass ~8.00 g (prompt, assumed)
RHO_P = 800.0            # PEI-SiO2 pellet density [kg/m^3] (EC-2 nominal)
EPS_TYPICAL = 0.40       # physical fallback void fraction for v (flagged)
LPM_TO_M3S = 1.0e-3 / 60.0

# The 9 prompt-named models -> registry codes.
PROMPT_MODELS = [
    ("M01", "Logistic (BA/Thomas/YN)"),
    ("M02", "Clark"),
    ("M04", "Modified Dose-Response"),
    ("M05", "Wolborska (early, C/C0<=0.15)"),
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
            "t_b_s": float(first["t_b"]) if pd.notna(first["t_b"]) else np.nan,
            "t_E_s": float(first["t_E"]) if pd.notna(first["t_E"]) else np.nan,
            "t50_s": float(first["t50"]) if pd.notna(first["t50"]) else np.nan,
            "n": int(first["n"]) if pd.notna(first["n"]) else 0,
        })
    return out


# --------------------------------------------------------------------------- #
# Table 1 — derived physical parameters
# --------------------------------------------------------------------------- #
def table1(rows) -> str:
    rho_b = MASS_KG / (A_C * L_BED_M)           # EC-1
    eps_ec2 = 1.0 - rho_b / RHO_P               # EC-2
    lines = [
        "### Table 1 — Derived physical parameters (May-2026 runs)",
        "",
        "**FLAG — geometrically inconsistent inputs.** Format-A sensor logs carry "
        "no flow/mass/geometry, so every value below uses the engineered prompt's "
        f"assumptions: d = 85 mm, bed L = {L_BED_M*100:.0f} cm, m = "
        f"{MASS_KG*1000:.2f} g, ρ_p = {RHO_P:.0f} kg/m³. With these, EC-1 gives "
        f"ρ_b = **{rho_b:.1f} kg/m³** and EC-2 gives ε = **{eps_ec2:.3f}** — an "
        "essentially empty column. 8 g cannot pack a 21 cm × 85 mm bed (that "
        f"volume ≈ {A_C*L_BED_M*RHO_P*1000:.0f} g at ρ_p = 800). ρ_b, ε(EC-2) and "
        "the ε-based interstitial velocity below are therefore unphysical; the "
        "real packed-bed geometry of these runs is the missing input "
        "(owner: Prof. Birgersson / SUTD rig). The U column (EC-5) depends only "
        "on flow + column area and is reliable; v is also reported against a "
        f"typical packed-bed ε = {EPS_TYPICAL:.2f} as a usable fallback.",
        "",
        "| Run | conc (%) | flow (lpm) | ρ_b [kg/m³] | ε (EC-2) | U [m/s] (EC-5) | "
        "v [m/s] @ε(EC-2) | v [m/s] @ε=0.40 |",
        "|---|---|---|---|---|---|---|---|",
    ]
    csv_rows = []
    for r in rows:
        Q = r["flow_lpm"] * LPM_TO_M3S          # m^3/s
        U = Q / A_C                             # EC-5
        v_ec2 = U / max(eps_ec2, 1e-9)          # EC-6 with EC-2 eps
        v_typ = U / EPS_TYPICAL
        lines.append(
            f"| {r['run_id']} | {r['conc']} | {r['flow_lpm']:.2f} | "
            f"{rho_b:.1f} | {eps_ec2:.3f} | {U:.3e} | {v_ec2:.3e} | {v_typ:.3e} |"
        )
        csv_rows.append({
            "run_id": r["run_id"], "conc_pct": r["conc"], "flow_lpm": r["flow_lpm"],
            "rho_b_kg_m3": rho_b, "eps_EC2": eps_ec2, "U_m_s": U,
            "v_eps_EC2_m_s": v_ec2, "v_eps0p40_m_s": v_typ,
        })
    pd.DataFrame(csv_rows).to_csv(OUT / "table1_physical.csv", index=False)
    return "\n".join(lines)


# --------------------------------------------------------------------------- #
# Table 2 — per-model fit statistics for the 9 prompt models
# --------------------------------------------------------------------------- #
def table2(rows) -> str:
    lines = [
        "### Table 2 — Model fit statistics (9 prompt models × 7 runs)",
        "",
        "Read straight from the stored `results_<run>.csv`. AdjR² < 0 means the "
        "model is worse than a horizontal line through the mean. Wolborska (M05) "
        "is fitted on the early window only (C/C0 ≤ 0.15), so its statistics are "
        "not comparable to the complete-curve models — see Table 3 note.",
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
        "M05": "INVALID for complete curves (early-window exponential)",
        "M16": "CONDITIONAL (ζ≥2 & τ_K≥1 only)",
    }
    lines = [
        "### Table 3 — Model ranking by mean Adj. R² across the 7 May runs",
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
        "fractal term is warranted.",
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
    fig, ax = plt.subplots(figsize=(9, 5.5))
    for r in rows:
        if r["t"] is None:
            continue
        col = "#d62728" if r["conc"] == 10 else "#1f77b4"
        ls = {0.05: ":", 0.10: "-", 1.50: "--"}.get(r["flow_lpm"], "-")
        tmin = r["t"] / 60.0
        ax.plot(tmin, r["y"], ls, color=col, lw=1.0, alpha=0.8,
                label=f"{short(r['run_id'],30)}")
        tb = t_at_level(r["t"], r["y"], 0.05) / 60.0
        te = t_at_level(r["t"], r["y"], 0.95) / 60.0
        if np.isfinite(tb):
            ax.axvline(tb, color=col, ls=":", lw=0.4, alpha=0.4)
    ax.axhline(0.05, color="k", ls=":", lw=0.6)
    ax.axhline(0.95, color="k", ls=":", lw=0.6)
    ax.set_xlabel("time [min]")
    ax.set_ylabel(r"$C_t/C_0$  [—]")
    ax.set_ylim(-0.05, 1.1)
    ax.set_title("Plot 1 — May-2026 experimental breakthrough curves (overlaid)\n"
                 "blue = ~4–6 % CO₂ (conc5), red = ~10 % CO₂ (conc10); "
                 "t_BT at C/C₀=0.05, t_E at 0.95")
    ax.legend(fontsize=7, loc="center right")
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUT / "Plot1_overlay.png", dpi=300)
    plt.close(fig)
    print(f"[fig] {OUT/'Plot1_overlay.png'}")


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
    ax.set_title("Plot 8 — predicted vs observed, all 7 May runs\n"
                 "(coloured by model family; tight diagonal = good fit)")
    ax.legend(fontsize=8, loc="upper left", markerscale=2)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUT / "Plot8_parity.png", dpi=300)
    plt.close(fig)
    print(f"[fig] {OUT/'Plot8_parity.png'}")


# --------------------------------------------------------------------------- #
def main() -> None:
    rows = load()
    print(f"Loaded {len(rows)} May runs.")
    t1, t2, t3, t4 = table1(rows), table2(rows), table3(rows), table4(rows)
    md = "\n\n".join([
        "# May-2026 diagnostic runs — engineered-prompt deliverables",
        "*Assembled from stored `breakthrough_out/` fits; no re-fitting.*",
        t1, t2, t3, t4,
    ])
    (OUT / "tables.md").write_text(md, encoding="utf-8")
    print(f"[md] {OUT/'tables.md'}")
    fig_p1(rows)
    fig_p8(rows)
    print("Done.")


if __name__ == "__main__":
    main()

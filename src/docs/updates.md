30/4/2026 (Week 2, Day 5)
study_plan.md (v1.0 → v2.0): Complete rewrite.
  - Title: "Regeneration" → "Adsorption Breakthrough"
  - Controllable parameters: T_regen/Q_purge/L/m → u/C_in/L/T_ads
  - Metrics: SER/v_th/τ_90 → τ_BT/η/W_MTZ/q_dyn
  - H1–H5: regeneration effects → velocity/concentration/bed-length/temperature/R-H shock
  - Gates B & C: thermal front/Elfving → R-H adsorption shock ±10% / Stampi-Bombelli 2024 τ_BT ±20%
  - Isotherm: Langmuir → Toth (ns0=1.23, b0=4839 kPa⁻¹, t0=0.25, ΔH0=70 kJ/mol — fully in hand)
  - IC/BC: saturated bed + purge inlet → clean bed + step C_in
  - Q_wall: non-zero → zero (adiabatic)
  - Literature map: 7 old regeneration sources → 7 papers from papers/md/
  - Solver scaffold, math track, report chapters, journal anchors all updated accordingly
  - Changelog appended

  CLAUDE.md: Updated repo purpose, gates, solver notes, Toth parameter table. papers/md/ named as source of truth.

  Two files still carry old-scope content and need separate updates: derivation.md and research.md. The .xlsx tracker
  sweep matrix also needs updating.

  17/05/2026: biweekly-journal-18may.md: New file created with content on SOP, DOE, and literature review. This journal reflects the shift in project scope from regeneration to adsorption breakthrough, detailing the new experimental design and key learnings from recent literature.

  26.05.2025
    Package layout

  breakthrough_fit/
  ├── __init__.py        — package exports
  ├── parse.py           — DataParser: auto-detect Format A/B, despike, metadata
  ├── models.py          — M01–M24 + BreakthroughModel registry, bounds, init strategies
  ├── stats.py           — R², AdjR², RMSE, χ²_red, AIC/AICc, Akaike weight, AAD, F-test
  ├── fit.py             — ModelFitter (curve_fit + L-BFGS-B fallback, 10 random starts, seed=42)
  ├── isotherm.py        — q₀ back-calc (YN/Thomas/BA), Langmuir/Freundlich linearised fits
  ├── performance.py     — t_b, t_E, t₅₀, q_dyn, L_MTZ, ψ (eqs. 72–76)
  ├── plots.py           — P1…P7 at 300 dpi (Agg backend, headless)
  ├── mtz_fem.py         — 1-D linear FEM mesh + travelling-wave projection
  └── main.py            — CLI: `python -m breakthrough_fit.main --data ... --c0 ... --flow ...`

  Smoke test

  Format B 50ml_2g.csv (475 rows, C₀=41000 ppm): all 24 models attempted, 22 converged. Top by AICc: M24 parallel
  sigmoidal (R²=0.998), M10 fractal gudermannian, M13 log-Gompertz. F-tests confirm fractal/asymmetric variants
  significantly outperform M01 (p < 1e-22). Performance: t_b=1271 s, q_dyn=0.0015 mol/kg, ψ=0.598. Seven PNGs +
  results_50ml_2g.csv written to breakthrough_out/50ml_2g/.

  Format A May-22-2026-conc10-flow0.1.csv parses after adaptive column-count detection (files vary 5–8 sensor channels).

  Notable design choices

  - Numerically stable sigmoid (_sigmoid) to avoid exp overflow at large arguments.
  - M22 n-order BA output clipped to [0,1]; M05 Wolborska evaluated only over its valid early-breakthrough mask (C/C₀ ≤
  0.15) for stats.
  - M18/M19 Chern–Chien use brentq per-point inside an L-BFGS-B outer loop; failed points → NaN, skipped by stats.
  - All deferred to the registry — adding a model means appending one entry.

  Run any file with:
  python -m breakthrough_fit.main --data "src/solver/data/*.csv" --c0 39900 --flow 50 --mass 4

  31.05.26

   ---
  Results: 5 new runs fitted against 24 models

  Output files: breakthrough_out/run {3,4,5,6,8}/ — 7 plots + 1 CSV per run.

  ---
  Model ranking (consistent across all runs)

  ┌────────┬─────────────────────────────┬─────────────────────────────────────────────┐
  │  Rank  │            Model            │                    Notes                    │
  ├────────┼─────────────────────────────┼─────────────────────────────────────────────┤
  │ 1      │ M10 Fractal Gudermannian    │ Best AICc on runs 6, 8; AdjR² > 0.9994      │
  ├────────┼─────────────────────────────┼─────────────────────────────────────────────┤
  │ 1      │ M11 Fractal ERF             │ Best on runs 3, 5; AdjR² > 0.9984           │
  ├────────┼─────────────────────────────┼─────────────────────────────────────────────┤
  │ 2      │ M14/M15 Weibull/Avrami      │ Best on run 4; near-identical to each other │
  ├────────┼─────────────────────────────┼─────────────────────────────────────────────┤
  │ 3      │ M03 Fractal Clark           │ Top 4 on all runs                           │
  ├────────┼─────────────────────────────┼─────────────────────────────────────────────┤
  │ 5–6    │ M23 Fractal YN              │ Consistently strong                         │
  ├────────┼─────────────────────────────┼─────────────────────────────────────────────┤
  │ Mid    │ M01 Logistic (YN/Thomas/BA) │ AdjR² 0.91–0.96, RMSE 0.065 — mediocre      │
  ├────────┼─────────────────────────────┼─────────────────────────────────────────────┤
  │ Bottom │ M16 Klinkenberg             │ AdjR² 0.32–0.37 — fails                     │
  ├────────┼─────────────────────────────┼─────────────────────────────────────────────┤
  │ Failed │ M18/M19 Chern-Chien         │ Did not converge on any run                 │
  └────────┴─────────────────────────────┴─────────────────────────────────────────────┘

  Main finding: all 5 curves are strongly asymmetric (right-skewed). Fractal models beat the standard logistic by ΔRMSE ≈ 6× (0.065 → 0.008). The standard YN/Thomas/BA misrepresents these curves.

  ---
  Per-run performance

  ┌─────┬───────────────┬─────────┬───────────┬───────────────┬────────────────┐
  │ Run │   C₀ (ppm)    │ Q (lpm) │ t₅₀ (min) │ t_E 95% (min) │ q₀_YN (mol/kg) │
  ├─────┼───────────────┼─────────┼───────────┼───────────────┼────────────────┤
  │ 3   │ 47,400 (5%)   │ 0.15    │ 5.5       │ 58.4          │ 0.307          │
  ├─────┼───────────────┼─────────┼───────────┼───────────────┼────────────────┤
  │ 4   │ 97,800 (10%)  │ 0.05    │ 12.6      │ 77.7          │ 0.418          │
  ├─────┼───────────────┼─────────┼───────────┼───────────────┼────────────────┤
  │ 5   │ 95,420 (10%)  │ 0.10    │ 3.8       │ 31.7          │ 0.279          │
  ├─────┼───────────────┼─────────┼───────────┼───────────────┼────────────────┤
  │ 6   │ 102,140 (10%) │ 0.05    │ 4.0       │ 39.3          │ 0.152          │
  ├─────┼───────────────┼─────────┼───────────┼───────────────┼────────────────┤
  │ 8   │ 150,630 (15%) │ 0.125   │ 4.1       │ 34.5          │ 0.558          │
  └─────┴───────────────┴─────────┴───────────┴───────────────┴────────────────┘

  Flag: runs 4 and 6 are nominally identical (10% CO₂, Q=0.05 lpm) but q₀_YN differs by 2.8× (0.418 vs 0.152 mol/kg). May 22 → May 29 — possible sorbent capacity degradation or different packing between days.

  ---
  Caveats

  - q_dyn in the results CSV has a ×1000 unit error in the existing performance.py formula (divides by mass_kg × 1000, giving mol/1000 kg not mol/kg). Multiply reported values by 1000 for true mol/kg. q₀_YN is correct.
  - t₀ detection is auto-derived (first sustained rise > 2% of plateau) — verify against lab notebook.
  - C₀ detection uses 92nd percentile of sensor readings — close but ~2–5% below nominal (47.4 vs 50k ppm for run 3, etc.).

✻ Churned for 13m 49s

※ recap: Fitted all 24 breakthrough models to the 5 new experimental runs (runs 3, 4, 5, 6, 8) using the existing breakthrough_fit pipeline extended with a Format C parser. Next step is reviewing the generated plots in
  breakthrough_out/ to verify fit quality. (disable recaps in /config)
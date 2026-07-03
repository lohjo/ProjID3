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

  I've searched the repo and traced all three topics to their source artefacts. Here's what's there — with the honest
  gaps flagged at the end.

  Where each topic lives

  Topic: (i) Parameter estimation
  Code: breakthrough_fit/performance.py, breakthrough_fit/stats.py, new_runs_pipeline.py, ModelFitter
  Equations: equation_compendium.md §16 (eqs 72–78)
  Prose: experimental-results.md §1.2, §2; CO2-adsorption-model.md §6
  ────────────────────────────────────────
  Topic: (ii) Fitting quality
  Code: breakthrough_fit/stats.py
  Equations: equation_compendium.md §23 (eqs 140–148)
  Prose: prompts/prompt01.md (stats table); experimental-results.md §4–5
  ────────────────────────────────────────
  Topic: (iii) Limitations
  Code: —
  Equations: —
  Prose: experimental-results.md §7.4–7.5, §9; TRAVELLING-WAVE…tex §"Scope and limitations"; derivation.md §F.6;
    CO2-adsorption-model.md §2, §3.4

  ---
  1) Extracting model parameters from the curves

  There are two distinct senses of "parameter," and the repo does both:

  (a) Model-free integral descriptors — yes, numerical integration of the curve. This is what you mean by integrating
  the curve. breakthrough_fit/performance.py computes them directly from the measured C/C₀(t) trace, no model assumed:

  - q_dyn (dynamic capacity), the key integral — q_dyn_trapz (performance.py:56) evaluates  q_dyn = (Q·C₀/m)·∫₀^{t_E}(1
  − C/C₀) dt  by np.trapezoid, truncated at the saturation time t_E. This is EC eq. 72 (equation_compendium.md:343).
  - t_BT / t₅₀ / t_E (performance.py:32, _interp_time) — crossing times at C/C₀ = 0.05 / 0.50 / 0.95 by linear
  interpolation between samples.
  - L_MTZ (performance.py:89) = [1 − (t_E − t_BT)/(2 t_E)]·L_bed — EC eq. 75.
  - ψ and t* (performance.py:98) — stoichiometric efficiency ψ = t_BT/t*, where t* = ∫₀^∞(1 − C/C₀) dt is the full
  integral — EC eq. 76.

  Note in experimental-results.md:54: because all five runs crossed C/C₀ = 0.95, t_E and q_dyn are measured integrals
  over real data, not model extrapolations.

  (b) Regression parameters via nonlinear least-squares. The 24 candidate models are fitted with
  scipy.optimize.curve_fit, method trf, 12 multi-starts, physically bounded (experimental-results.md:136). This yields
  the rate/shape constants — k_YN, τ, fractal exponent h (M23/M11), MDR asymmetry a, Clark n, Weibull k, etc. — stored
  per (run, model) in breakthrough_out/<run>/results_<run>.csv.

  (c) Cross-check between the two. new_runs_pipeline.py:152 back-calculates q₀ from the fitted Yoon–Nelson τ and
  compares it to the integral q_dyn — an independent sanity check (they agree to order of magnitude,
  experimental-results.md:104).

  (d) Mechanistic calibration target. For the physical model, CO2-adsorption-model.md §6 prescribes the two-step
  strategy from Stampi-Bombelli 2024: fit k₁ and D_L to the initial slope (≤ 70 % uptake), then η and k₂ to the tail,
  and verify t_b against the stoichiometric prediction t_b = η(1−ε)ρ_p q₀* L /(u₀ C₀).

  ---
  2) Evaluating fitting quality

  All error statistics are in breakthrough_fit/stats.py (compute_stats, stats.py:34), matching equation_compendium.md
  §23 (eqs 140–148) and the spec table in prompts/prompt01.md:193:

  ┌────────────────────────────────────────┬─────────────────┬─────┐
  │               Statistic                │ Code (stats.py) │ Eq. │
  ├────────────────────────────────────────┼─────────────────┼─────┤
  │ R²                                     │ :68             │ 140 │
  ├────────────────────────────────────────┼─────────────────┼─────┤
  │ Adj. R² = 1 − (1−R²)(n−1)/(n−p)        │ :70             │ 141 │
  ├────────────────────────────────────────┼─────────────────┼─────┤
  │ RMSE = √(RSS/(n−2))                    │ :74             │ 142 │
  ├────────────────────────────────────────┼─────────────────┼─────┤
  │ χ²_ν (weighted if σ supplied)          │ :81             │ 143 │
  ├────────────────────────────────────────┼─────────────────┼─────┤
  │ AAD (mean abs. relative dev.)          │ :92             │ 144 │
  ├────────────────────────────────────────┼─────────────────┼─────┤
  │ AIC = n·ln(RSS/n) + 2p                 │ :84             │ 147 │
  ├────────────────────────────────────────┼─────────────────┼─────┤
  │ AICc = AIC + 2p(p+1)/(n−p−1)           │ :86             │ 147 │
  ├────────────────────────────────────────┼─────────────────┼─────┤
  │ Akaike weight Wₐ = 1/(1+e^{0.5·ΔAICc}) │ rank_aicc, :113 │ 148 │
  ├────────────────────────────────────────┼─────────────────┼─────┤
  │ Nested F-test                          │ f_test, :98     │ 146 │
  └────────────────────────────────────────┴─────────────────┴─────┘

  Model discrimination workflow (experimental-results.md §4.3–5):
  - Rank by mean/median Adj. R² across runs (Table 3) and by AICc / Akaike weight within each run.
  - F-test only for genuinely nested pairs — here only M01 (logistic) ⊂ M23 (Fractal-BA), testing whether the fractal
  exponent h is warranted. It was decisive in all 5 runs (F > 10⁴, p ≪ 0.001; Table 4).
  - Important caveat the docs already flag (experimental-results.md:208, prompt01.md:202): since C/C₀ ∈ [0,1],
  measurement variance is structurally bounded (~μ(1−μ)) and vanishes at the endpoints, violating the homoscedasticity
  assumption behind OLS F-tests and standard AIC. A beta-regression / logit transform would be more rigorous; the
  F-stats here are large enough that the conclusion survives.

  Two minor inconsistencies worth knowing about: stats.py and EC-142 use RMSE = √(RSS/(n−2)), whereas prompt01.md:198
  says √(RSS/n); and Adj. R² uses n−p (stats.py:69, EC-141) while prompt01.md:194 writes n−p−1. The code is internally
  consistent — just don't quote the prompt's formula and the CSV value as identical.

  ---
  3) Limitations of the current models

  Here the three items you listed split into two that are well-covered and one that is genuinely absent from the live
  repo:

  ✅ "Accessible amine fraction" — covered (as η). CO2-adsorption-model.md:36 defines η = fraction of surface (fast)
  amine sites ≈ 0.60–0.85; the dual-kinetic model splits total loading q̄ = q₁ + q₂ into fast surface sites (fraction η)
  and slow bulk PEI-layer sites (fraction 1−η) with κ = k₂/k₁ ≪ 1 (§3.4, lines 78–114). The capacity-utilisation
  limitation is quantified empirically: ψ ≈ 0.02–0.04 and L_MTZ ≈ 50 % of bed (experimental-results.md §3.2, §6.1) —
  i.e. most of the bed's amine capacity is unused at breakthrough. §7.5 also states the empirical lumped parameters
  (k_YN, h, a) cannot be extrapolated outside the fitted range and that q_dyn can't be compared to the Toth equilibrium
  loading until ρ_p/ε are confirmed (§9).

  ✅ "R-H valid only as a local approximation near the front" — covered. This is the cleanest match:
  - derivation.md §F.6 (:481): "Pe → ∞, NTU → ∞: ideal hyperbolic system. Fronts are shocks. R-H gives exact wave speed.
  Useful zeroth-order check." The R-H thermal-front speed is derived as a hyperbolic jump condition in §1.6/§2.6
  (:332–354), explicitly valid only at thermal equilibrium (NTU_h ≫ 1).
  - The travelling-wave paper (TRAVELLING-WAVE…tex, Theorem, :350) makes the front-locality precise: the analytical
  solution is a leading-order constant-pattern result (δ₁ = 0, 1/Pe = 0); v_{f,1} = v_f/η is the R-H speed for the
  ├────────────────────────────────────────┼─────────────────┼─────┤
  │ Akaike weight Wₐ = 1/(1+e^{0.5·ΔAICc}) │ rank_aicc, :113 │ 148 │
  ├────────────────────────────────────────┼─────────────────┼─────┤
  │ Nested F-test                          │ f_test, :98     │ 146 │
  └────────────────────────────────────────┴─────────────────┴─────┘

  Model discrimination workflow (experimental-results.md §4.3–5):
  - Rank by mean/median Adj. R² across runs (Table 3) and by AICc / Akaike weight within each run.
  - F-test only for genuinely nested pairs — here only M01 (logistic) ⊂ M23 (Fractal-BA), testing whether the fractal exponent h is warranted. It was decisive in all 5 runs (F > 10⁴, p ≪ 0.001; Table 4).
  - Important caveat the docs already flag (experimental-results.md:208, prompt01.md:202): since C/C₀ ∈ [0,1], measurement variance is structurally bounded (~μ(1−μ)) and vanishes at the endpoints, violating
  the homoscedasticity assumption behind OLS F-tests and standard AIC. A beta-regression / logit transform would be more rigorous; the F-stats here are large enough that the conclusion survives.

  Two minor inconsistencies worth knowing about: stats.py and EC-142 use RMSE = √(RSS/(n−2)), whereas prompt01.md:198 says √(RSS/n); and Adj. R² uses n−p (stats.py:69, EC-141) while prompt01.md:194 writes
  n−p−1. The code is internally consistent — just don't quote the prompt's formula and the CSV value as identical.

  ---
  3) Limitations of the current models

  Here the three items you listed split into two that are well-covered and one that is genuinely absent from the live repo:

  ✅ "Accessible amine fraction" — covered (as η). CO2-adsorption-model.md:36 defines η = fraction of surface (fast) amine sites ≈ 0.60–0.85; the dual-kinetic model splits total loading q̄ = q₁ + q₂ into fast
  surface sites (fraction η) and slow bulk PEI-layer sites (fraction 1−η) with κ = k₂/k₁ ≪ 1 (§3.4, lines 78–114). The capacity-utilisation limitation is quantified empirically: ψ ≈ 0.02–0.04 and L_MTZ ≈ 50 %
  of bed (experimental-results.md §3.2, §6.1) — i.e. most of the bed's amine capacity is unused at breakthrough. §7.5 also states the empirical lumped parameters (k_YN, h, a) cannot be extrapolated outside the
  fitted range and that q_dyn can't be compared to the Toth equilibrium loading until ρ_p/ε are confirmed (§9).

  ✅ "R-H valid only as a local approximation near the front" — covered. This is the cleanest match:
  - derivation.md §F.6 (:481): "Pe → ∞, NTU → ∞: ideal hyperbolic system. Fronts are shocks. R-H gives exact wave speed. Useful zeroth-order check." The R-H thermal-front speed is derived as a hyperbolic jump
  condition in §1.6/§2.6 (:332–354), explicitly valid only at thermal equilibrium (NTU_h ≫ 1).
  - The travelling-wave paper (TRAVELLING-WAVE…tex, Theorem, :350) makes the front-locality precise: the analytical solution is a leading-order constant-pattern result (δ₁ = 0, 1/Pe = 0); v_{f,1} = v_f/η is
  the R-H speed for the equilibrated system, valid for the fast front only, with the dispersive smoothing (1/Pe) and the slow-site tail entering as O(κ) corrections that require numerics (§5 of
  ├────────────────────────────────────────┼─────────────────┼─────┤
  │ Akaike weight Wₐ = 1/(1+e^{0.5·ΔAICc}) │ rank_aicc, :113 │ 148 │
  ├────────────────────────────────────────┼─────────────────┼─────┤
  │ Nested F-test                          │ f_test, :98     │ 146 │
  └────────────────────────────────────────┴─────────────────┴─────┘

  Model discrimination workflow (experimental-results.md §4.3–5):
  - Rank by mean/median Adj. R² across runs (Table 3) and by AICc / Akaike weight within each run.
  - F-test only for genuinely nested pairs — here only M01 (logistic) ⊂ M23 (Fractal-BA), testing whether the fractal
  exponent h is warranted. It was decisive in all 5 runs (F > 10⁴, p ≪ 0.001; Table 4).
  - Important caveat the docs already flag (experimental-results.md:208, prompt01.md:202): since C/C₀ ∈ [0,1],
  measurement variance is structurally bounded (~μ(1−μ)) and vanishes at the endpoints, violating the homoscedasticity
  assumption behind OLS F-tests and standard AIC. A beta-regression / logit transform would be more rigorous; the
  F-stats here are large enough that the conclusion survives.

  Two minor inconsistencies worth knowing about: stats.py and EC-142 use RMSE = √(RSS/(n−2)), whereas prompt01.md:198
  says √(RSS/n); and Adj. R² uses n−p (stats.py:69, EC-141) while prompt01.md:194 writes n−p−1. The code is internally
  consistent — just don't quote the prompt's formula and the CSV value as identical.

  ---
  3) Limitations of the current models

  Here the three items you listed split into two that are well-covered and one that is genuinely absent from the live
  repo:

  ✅ "Accessible amine fraction" — covered (as η). CO2-adsorption-model.md:36 defines η = fraction of surface (fast)
  amine sites ≈ 0.60–0.85; the dual-kinetic model splits total loading q̄ = q₁ + q₂ into fast surface sites (fraction η)
  and slow bulk PEI-layer sites (fraction 1−η) with κ = k₂/k₁ ≪ 1 (§3.4, lines 78–114). The capacity-utilisation
  limitation is quantified empirically: ψ ≈ 0.02–0.04 and L_MTZ ≈ 50 % of bed (experimental-results.md §3.2, §6.1) —
  i.e. most of the bed's amine capacity is unused at breakthrough. §7.5 also states the empirical lumped parameters
  (k_YN, h, a) cannot be extrapolated outside the fitted range and that q_dyn can't be compared to the Toth equilibrium
  loading until ρ_p/ε are confirmed (§9).

  ✅ "R-H valid only as a local approximation near the front" — covered. This is the cleanest match:
  - derivation.md §F.6 (:481): "Pe → ∞, NTU → ∞: ideal hyperbolic system. Fronts are shocks. R-H gives exact wave speed.
  Useful zeroth-order check." The R-H thermal-front speed is derived as a hyperbolic jump condition in §1.6/§2.6
  (:332–354), explicitly valid only at thermal equilibrium (NTU_h ≫ 1).
  - The travelling-wave paper (TRAVELLING-WAVE…tex, Theorem, :350) makes the front-locality precise: the analytical
  solution is a leading-order constant-pattern result (δ₁ = 0, 1/Pe = 0); v_{f,1} = v_f/η is the R-H speed for the
  equilibrated system, valid for the fast front only, with the dispersive smoothing (1/Pe) and the slow-site tail
  entering as O(κ) corrections that require numerics (§5 of CO2-adsorption-model.md). Gate B tests this front velocity
  to ±10–15 % (CLAUDE.md Gate B; .tex:518).

  ❌ "Plasticisation" — NOT in the repo. A repo-wide search (excluding the archive) for plasticis*, accessible amine
  density, and degrad* returns zero matches. The nearest physical content is the bulk PEI-layer diffusion resistance —
  k_{s,amine} ~ 10⁻⁴–10⁻³ s⁻¹, "diffusion through the viscous polyethylenimine" (CO2-adsorption-model.md:108–114, :321).
  That models slow diffusion through the polymer, not CO₂-induced plasticisation/swelling that changes the polymer's
  transport properties or capacity over cycles. Oxidative degradation is cited only as a bibliography entry (Bollini
  2012) in the .tex, never discussed; the .tex scope section (:593) explicitly excludes humidity and treats only
  single-component dry CO₂/N₂.

  So if your report's Limitations section needs plasticisation and an accessible-amine-density (sites per kg, vs. just
  the fraction η) discussion, those would be new additions — the repo currently has only the η fraction and the static
  k_{s,amine} resistance, neither of which captures a load-/cycle-dependent change in the polymer. Want me to draft a
  limitations subsection covering those two gaps, anchored to the existing dual-kinetic notation? I'd put it in
  experimental-results.md §7.5 or as a new bullet in §9, but I'll hold until you confirm where you want it.

✻ Churned for 3m 25s

※ recap: Searched the repo on parameter estimation, fit-quality stats, and model limitations for the breakthrough work,
  and reported findings. Plasticisation and accessible amine density aren't covered in the repo. Next: draft a
  limitations subsection on those gaps if you want it. (disable recaps in /config)

  Both deliverables complete. Here's what was done:

  ---
  Task 1 — assemble_may_prompt.py refactor (done):
  - D_COL_M 0.085 → 0.0085 (8.5 mm)
  - RUNS list replaced with RUN_META dict (runs 3/4/5/6/8, per-run Q/m/L/conc_pct)
  - DATA path updated to src/solver/data/new runs/
  - load() fixed to use t_b_s / t_E_s / t50_s column names (old May-run CSVs used t_b/t_E/t50)
  - table1() rewritten: per-run ρ_b/ε/U/v from RUN_META; "geometrically inconsistent" FLAG removed; replaced with correct ρ_p=800 caveat + ε floor explanation
  - Table 2/3 headers corrected ("7 May runs" → "5 new runs"); Table 3 adds note that M11 outperforms all 9 prompt models
  - Fig P1 title/colors corrected (blue=~5% CO₂, red=~10%, green=~15%)
  - Script runs clean; src/img/generated/may_prompt/ regenerated

  Task 2 — experimental-results.md rewrite (done):
  - Built entirely on the 5 real runs; follows engineered-prompt structure (Tables 0→4, §1–9)
  - Reports all key findings: fractal family dominates (M23 best among 9 prompt models; M11 best from 24-model library in runs 3/5), decisive F-test (F > 10,000 in all
  runs), Clark n→1 + MDR a=1.2–1.4 confirm asymmetry, q_dyn = 0.55–0.89 mol/kg physically plausible
  - Flags the run5/run6 t₅₀ anomaly (19s vs 14s at 150 vs 100 mL/min) honestly
  - Flags ρ_p/ε open input throughout
  - Synthetic placeholder appendix (12 *ml_*g) clearly labeled as NOT measured, with old q_dyn values preserved but flagged as pre-fix

  Also corrected: CLAUDE.md "best model M11 every run" → per-run actual winners (M11 runs 3/5, M14 run 4, M10 runs 6/8). Memory updated to match.
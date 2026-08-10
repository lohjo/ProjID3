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

---
10/07/2026

Gap analysis of the Danilov-pairing comment vs. the three sessions it seeded (Mechanistic adsorption model → mechanistic-model.md; Danilov dispersion model implementation → psi_quadrature_verify.py; Ψ-Quadrature consistency proof → psi-quadrature-consistency-proof.md). Findings:

- **A.4's pseudo-homogeneous assumption cites a dead reference.** The comment's suggested route (derive single-T from Danilov's actual two-T balances, sum-cancel the α_v term, get a general criterion ΔT=(1-ε)ρ_p(-ΔH)kψ/α_v ≪ ΔT_ad) was not what got built. A.4 instead asserts pseudo-homogeneity from RGC75 directly (assumption A6) and justifies it with two rig-specific order-of-magnitude checks (τ_w/t_st≈0.08, isotherm sensitivity ≈30%/K) — reasonable, but not the general closed-form bound promised, and A6's own stated criterion cites `derivation.md` §1.3–1.4, a file that does not exist in the repo (only `derivation.tex`, and only inside the archived, do-not-open folder). The single load-bearing assumption behind the whole single-T formulation currently rests on an uncitable reference. Owner: next session on mechanistic-model.md — either re-derive A6's bound from danilov2019.txt's own two-T balance (still in `src/docs/papers/`, not archived) or strike the derivation.md citation.
- **CLAUDE.md's "Architecture of the solver work" table is stale.** It still lists a 4-field state vector [C,q,T_g,T_s] and flags the two-T/one-T split as an open reconciliation. mechanistic-model.md A.6 has since settled on a single-T model (3 fields). Needs a CLAUDE.md/AGENTS.md sync per the twin-file rule.
- **Comment's proposed nondimensional group ω (thermal/mass front-speed ratio) was never named in Part C.** psi-quadrature-consistency-proof.md ends up needing exactly this ratio (v_th/v_RH~0.2–0.5) to prove the part-(c) two-front obstruction, but computes it ad hoc rather than citing a Part-C definition. Cosmetic; tie back to Λ, γ_h, ε when Part C is next touched.
- **The comment's central premise did not survive rigorous checking — this is the real finding, not a nitpick.** The comment treated "both routes share the bc_f→0 logistic limit, so γ≈1 is safe" as a clean sanity check. psi-quadrature-consistency-proof.md Theorem 4.2/4.3 show Route B (as the comment specified: β frozen at 1) does not converge to the logistic at all (sup-distance→1/2), and even the charitable reading (β re-derived at the Henry point) leaves a universal, non-vanishing 3/2−√2≈8.6% sup-norm residual. "Λ~500 so sub-1% error" is true only for the one tail rate the comment checked, not the wave shape as a whole.
- **Severity miscalibration, already fixed:** comment flagged Eq. 5/6 forward-march ill-conditioning as a Pe≳50 issue; it actually breaks at Pe=10 once non-isothermal T-feedback is present (~5× more conservative than estimated). Fixed via backward march (repo erratum, `psi_quadrature_verify.py`).
- **Sweep status unchanged.** Gates A/B are genuinely, numerically passed against their exact defined tolerances (V.1: 0.69% L² at N=1000 < 1% Gate-A budget; V.2: 0.020% RH-speed error < 10% Gate-B budget) — but only at the single illustrative operating point of §C.4, via the T1–T5 verification suite, which tests solver correctness, not the planned sweep. The 39-run/(11 OAT + 9 u×C_in) matrix CLAUDE.md flags as planned-not-executed remains exactly that — none of the three sessions ran it. What's new: §6.3 of psi-quadrature-consistency-proof.md now supplies the regime-check formula (c_f−c_I)tanh(aT_sep/2) ≤ tolerance needed to decide, per sweep point, whether the cheap ψ-quadrature surrogate is admissible or the full FV-MOL solve is required — the tool for running the sweep cheaply now exists; the sweep itself does not.
- **Research-direction novelty gap:** psi-quadrature-consistency-proof.md's Theorem 7.1 (general Ansatz-Consistency principle for seeded marching schemes) and Theorem 5.2 (closed-form error floor in bc_f) are genuinely original results in the sense the "is this publishable" assessment asked for — but they come from a single unverified pass. Per prompt00.md's own closing-note protocol (run twice, diff before trusting), this has not yet happened for the ψ-quadrature problem. `src/docs/prompts/prompt02.md` created to run it: same problem, two independently-dispatched rerun modes (creative-disproof / rigor-check), explicit instruction not to read the existing proof first, and a diff procedure before anything gets promoted into mechanistic-model.md or the report.

**Audit addendum (same day):** cross-checked prompt02.md against mechanistic-model.md and the actual `danilov2019.txt` (OCR'd, `src/docs/literature/modelling/danilov2019.txt` — not `src/docs/papers/`, which does not exist; CLAUDE.md's own citation rule points at a dead path, fixed in prompt02.md's notes). Route A equations (v_RH, t_st, D.8, tail rates) verified verbatim against MM. Route B mechanics verified against the paper directly: Eq. (1)'s corrected-time formula θ=(t-z/u_f)-t_s matches the paper's printed form exactly (line 459); Appendix A Eq. A.8 defines γ_q as an explicit function of the local isotherm slope ∂q_eq/∂y, and Appendix B Eq. B.5 defines β=1-(γ_q-1)/(ε_b·mol_G·y) in terms of it — i.e. the paper's own machinery already makes β state-dependent, and "γ_q≈1, β≈1" (line 1478, 1915-1917) is stated as a numerical evaluation result for the Table-2 system specifically, not a structural assumption. This corroborates rather than undermines psi-quadrature-consistency-proof.md's Lemma 2.4 (independently derived via Route A's concentration-basis ODE) — added as expected-failure-mode #6 in prompt02.md so a rerun that doesn't notice this from the paper itself is flagged as having missed available information.
  05/08/2026
    sensitivity-analysis.md + sensitivity_anova.py: NEW — sensitivity analysis by ANOVA of clusters in
    scatterplots (Kleijnen & Helton 1999a CMNs/CLs tests; Saltelli et al. 2000 SRC + Iman-Conover).
    Three tiers: (1) experimental, model-free, on the balanced 3x3 grid (flow x C0); (2) Monte-Carlo/LHS
    over the fitted-parameter ranges of the top-3 models by pooled AICc rank (M11, M24, M10), N=2000,
    propagated to t_b/t_E/t50/q_dyn/L_MTZ/psi at a fixed reference operating point; (3) regression of the
    fitted parameters themselves on (Q, C0).

    Headline: flow rate sets WHEN breakthrough happens (t_b F(2,6)=30.9, p=0.0007, eta2=0.911; C0 n.s.);
    concentration sets HOW MUCH is adsorbed (q_dyn F=5.29, p=0.047, eta2=0.638; flow n.s.). Mechanism —
    flow compresses every time constant (tau0/tau1/tau2 std. coef. -0.86/-0.89/-0.87 on Q) and also lowers
    the fractal exponent h (b ~ -0.72 to -0.75, p ~ 0.026); concentration reaches the kinetics only weakly
    and the shape parameters not at all.

    Findings that constrain future work:
      - M10/M11 k0 and h are NOT independently identifiable: rho_Spearman = 1.000 (M11) / 0.982 (M10)
        across all 14 runs. Independent-uniform sampling leaves the ridge — 11.3% (M11) / 8.3% (M10) of
        LHS draws failed to produce a breakthrough curve at all, vs 0% under Iman-Conover rank-correlated
        sampling. Re-parameterise on kappa = k0*tau0^(-h). Do not report k0 as an independent sensitivity.
      - M24 label switching: 2 of 14 runs returned tau1 > tau2. Canonical ordering tau1 <= tau2 now imposed;
        without it the tau1 range was wrong by ~4x.
      - M03 (Fractal Clark) excluded from the dissection despite 4th rank: pins n = 1.01 (lower bound) in
        all 14 runs and A0 = 1e6 (upper bound) in 6 of 9 newest runs. M10 k0 hits its upper bound (1.000)
        in 2026-07-10-conc15-flow0.05.
      - DO NOT POOL the 5 old runs with the 9-run grid for inference: bed L is 21.0-21.5 cm vs 23.0-24.5 cm
        and i.d. 8.5 vs 8.2 mm, so pooling adds a confounded factor. Every eta2 falls; t_b R2 0.879 -> 0.496;
        pooled L_MTZ adj. R2 goes negative.
      - L_MTZ = [1 - (t_E-t_b)/(2 t_E)]*L_bed has a hard floor of 0.5*L_bed. Measured span is 0.519-0.569
        of L_bed, CV 3.8% vs 79% for t_b. Its universal non-significance is a formula artefact, not physics.
      - The uniform MC prior is an ASSUMPTION, flagged as such. k0/tau0/tau1/tau2 are log-normal-shaped
        (Shapiro p >= 0.26 on logs, <= 0.013 raw); log-uniform would be the more defensible prior.
      - Blocking matters: C0 is n.s. for t_b in the one-way cluster test (p=0.80) but significant in the
        two-way factorial once flow's variance is removed (p=0.041). Report the factorial.

    Validation: 7 assertion-based self-checks run before any result prints (cluster F vs scipy f_oneway;
    SRC blindness to a pure quadratic; single-regressor SRC == Pearson r; M01 closed-form t50 = tau and
    t_b/t_E = tau -/+ ln(19)/k; propagated M11 t_b/t50/q_dyn vs measured for the reference run; Iman-Conover
    marginal preservation; two-way SS decomposition). Separately, all 141 numeric claims in the markdown
    were re-read from the workbook and reconciled to 3 s.f.

    CLAUDE.md / AGENTS.md: document-layout section updated with the new live doc and its three standing flags.

  05/08/2026 (later) — RERUN ON THE EXPANDED BASIS (18 files / 16 usable runs)
    new_runs_pipeline.py re-run over all 18 files in `newest runs/`. 16 fitted (24 models x 12 starts,
    seed 42, + plots P1-P7); 2 skipped by the pipeline's own metadata guard. sensitivity-analysis.md
    and sensitivity_anova_tables.xlsx regenerated. Basis for Tier 1 is now n=16 (grid) / n=21 (pooled).

    Reproducibility check: refitting the 9 previously-committed runs reproduced them to
    max |dAdjR2| = 9.9e-12 with identical t_b/t_E/t50/q_dyn. The git diff on those CSVs is last-digit
    formatting only. The pipeline is reproducible end to end.

    *** CONCLUSION WITHDRAWN ***
    The 14-run claim that "concentration sets capacity" does NOT survive replication. At n=9 the C0
    effect on q_dyn was F=5.29, p=0.047, eta2=0.638. At n=16 it is F=3.75, p=0.052 (cluster) and
    p=0.220 (factorial). Cause: 78.4% of q_dyn's total variance is PURE MEASUREMENT ERROR — replicate
    cells differ by up to 3.04x (e.g. 1.133 vs 0.373 mol/kg at 0.10 lpm / 10% CO2), median within-cell
    CV 36.7%. q_dyn is not currently measurable at the precision needed to detect anything.
    By contrast t_b and t50 carry only 4.4% / 4.0% pure error and are trustworthy.
    ACTION: run every experiment to a fixed C/C0 = 0.98 rather than stopping by wall-clock; q_dyn is an
    integral to t_E and inherits all tail noise.

    New results the replication bought (interaction was previously confounded with error, df_err 0 -> 7):
      - t50 shows a significant flow x concentration INTERACTION, F(4,7)=4.36, p=0.044. First time testable.
      - L_MTZ became significant for both factors (flow p=0.015, C0 p=0.028) — but see the standing
        dynamic-range flag; L_MTZ/L spans only 0.519-0.589 against a hard floor of 0.5.
      - Flow -> t_b strengthened to F(2,13)=46.2, p=1.2e-6, eta2=0.877 (was F=30.9, p=7e-4).
      - Flow -> h (fractal exponent) is now the strongest parameter-level effect in the study:
        M10 F(2,13)=52.0, p=6.3e-7, eta2=0.889.

    Data problems found and how they were handled:
      - 2026-07-22-conc10-flow0.10.csv IS MIS-NAMED: its header says 150 ml/min, not 100. Metadata is
        authoritative, and this was confirmed physically — its t_b=185 s sits with the 0.15 lpm runs
        (213 s), not the 0.10 lpm runs (326, 249 s). Treated as 0.15 lpm. ACTION: rename at source.
      - 2026-07-17-conc15-flow0.1.csv (no metadata) is the SAME EXPERIMENT as
        2026-07-17-conc15-flow0.10.csv (has metadata): the raw log has an ~80-min idle head; after
        aligning the trim they agree (132700 vs 134400 ppm at the 30-min mark). Excluding the raw one
        loses nothing and avoids double-counting.
      - 2026-07-17-conc15-flow0.15.csv still has no metadata AND is not a clean breakthrough — CO2 reads
        144590 ppm at 98 min, 0 ppm at 139 min, 142040 ppm at 179 min (sensor dropout / multi-segment).
        Genuinely lost. ACTION: supply bed geometry and re-record.
      - 2026-07-29-conc5-flow0.05 never reaches C/C0=0.95, so t_E is undefined. Handled pairwise (n=15
        for t_E/L_MTZ/psi); never imputed.
      - M24 label switching is OPTIMISER-ORDER-DEPENDENT: 2026-07-08-conc5-flow0.15 was swapped in the
        previous fit and is not in this one — same optimum, same RSS, components returned in the other
        order. Confirms canonicalisation (tau1 <= tau2) must be applied, not trusted to the fitter.

    Code changes to sensitivity_anova.py:
      - two_way_anova_no_rep() -> two_way_anova(): unbalanced two-way with replication, Type II SS,
        estimable interaction, aliased-column dropping. The old function silently AVERAGED replicate
        cells via pivot_table and would have been wrong on this basis.
      - replicate_reproducibility(): pure-error vs total-variance decomposition per response.
      - bound_pinning() + top_models() screen: a model is disqualified from the parameter dissection if
        any parameter sits at its own bound in >25% of runs. This is what now excludes M03 (n pinned
        21/21, A0 10/21) automatically — previously a hand-written exclusion. Tolerance is relative to
        each BOUND, not the bound span (a span-relative test called any tau0 < 1001 "pinned at 1").
      - Self-checks 7 -> 9: added Type II SS reducing to the orthogonal decomposition on a balanced
        synthetic design, a planted interaction recovered, and an absent interaction reported absent.
      - Scope labels are now derived from the data (n=16 / n=21), not hardcoded.

    Verification: 9/9 assertions pass. src/docs/verify_sensitivity_doc.py re-reads all 341 numeric
    claims in the markdown from the workbook and reconciles them (0 mismatches).

    Standing flags unchanged: k0/h non-identifiable (rho_S = 0.984 M11 / 0.971 M10; 11.3% / 8.3% of
    independent-uniform draws produce no breakthrough curve vs 0% rank-correlated); do not pool the
    5 old runs (every eta2 still falls); L_MTZ dynamic range is a formula artefact; rho_p still unknown.

  09/08/2026 — Final Report §5 "Experiments" inserted; document renumbered

    src/T32_PI05_Final_Report.docx, edited in place (backup:
    src/T32_PI05_Final_Report.backup-2026-08-09.docx). The report recorded the SOP (§4) and the
    outcomes (§5) but never recorded the experiments themselves: no run inventory, no source file
    per number, no exclusion list. The replicate tables identified runs only by grid position
    "No. 1-9", the ambiguity flagged as review item 3.11.

    New §5 Experiments, between the SOP and Experimental Results:
      5.1 Design as executed        — Table 3, cell counts for the 3x3 grid (16 runs, 7 cells replicated)
      5.2 Run inventory/provenance  — Table 4, 16 rows: run, both stated flows, C0, m, L_bed, d_col,
                                      n points, best model, and where each run appears later
      5.3 Excluded/flagged records  — Table 5, 9 rows, each with an owner
      5.4 Data lineage              — pipeline chain, passport, and the t_b/t_E definition note

    Scoped to the `newest runs/` campaign only; runs 3/4/5/6/8 stay where they are and are explicitly
    not pooled (different rig geometry).

    Renumbering, forced by the insertion and applied by script:
      H1  5-10 -> 6-11.  H2/H3 7.x -> 8.x, 8.x -> 9.x, 9.x -> 10.x, 5.x -> 6.x.
      Tables 3-9 -> 6-13; new tables take 3-5. This resolved a pre-existing collision (two different
      tables were both captioned "Table 7)") and a prose reference that pointed at the wrong one.
      12 report-internal section cross-references retargeted; refs to `experimental-results.md` §N
      and all §3.x/§4.x refs left alone.
      "7Fitting performance and analysis" and §6.1-6.3 were body-styled, so they never reached the
      table of contents; promoted to Heading1/Heading2. <w:updateFields> set, so Word offers to
      refresh the TOC (and its page numbers) on open.

    New: src/solver/build_experiments_passport.py -> src/docs/experiments_passport.{json,md}.
    experiments_provenance[] carries, per record: source path, SHA-256, size, date, the metadata the
    file states about itself (prose block AND numeric cell, kept separate), what the pipeline actually
    used, the derived metrics read back from the committed results CSV, and status. Nothing is refitted;
    the three docx tables are rendered from it, so no value in §5 is hand-typed. The generator asserts
    each run's derived t_b matches the value already printed in the report to within 0.05 min -- all 16
    pass, which is what establishes that the report's replicate tables are these runs.

    Two data findings, reported in §5.3 and not silently fixed:
      - Four files state flow twice and disagree with themselves (prose block vs numeric cell `v`).
        parse.py reads `v`, so those four were fitted at the numeric value; comparing t_b against the
        same-concentration runs shows the prose value is the physical one in every case. q_dyn, L_MTZ
        and psi for those four are provisional. Owner: lab. Note this contradicts sensitivity-analysis.md
        §1.2(a), which states 2026-07-22-conc10-flow0.10 was "treated as 0.15 lpm throughout" -- the
        artefacts show 0.10. That doc needs reconciling against the artefacts.
      - Rows 7 and 9 of the replicate-II table (15% at 50 and 150 ml/min, t_b = 17.967 and 2.843 min)
        are not reproducible from any committed CSV. Retained as recorded, flagged as untraceable.
        Owner: author/lab.

    Verification, all run: 1518 paragraphs / 24 tables (was 1241 / 21); H1 sequence 1-11 with no gaps;
    body table captions 3-13 unique; no stale report-internal section reference remains; all 59 zip
    parts parse; the 20 embedded images are byte-identical to the backup; all 252 cells of the three
    new tables found verbatim in experiments_passport.md.

    Still open: experimental-results.md §10 documents only the first 9 of the 16 grid runs; the TOC
    needs one field refresh in Word; the "7.?.4" heading still carries a literal "?".

  09/08/2026 (later the same day) — every generated figure and every fit statistic
  embedded in the Final Report

    src/T32_PI05_Final_Report.docx, edited in place (backup:
    src/T32_PI05_Final_Report.backup-2026-08-09-prefigures.docx, which is Word's own
    re-save of the post-§5 document, i.e. the exact pre-edit state).

    The report held 20 images, of which 3 were results plots, and exactly one error-
    statistics table (Table 11, five rows). Meanwhile the repo held 147 per-run fit
    plots, 21 x 24 = 504 rows of fit statistics, 9 sensitivity figures, a 17-sheet
    ANOVA workbook and 17 model-verification figures, none of it in the manuscript.
    06-change-list.md named this as the outstanding gap (items 2.16/2.17 and its
    "deliberately not in this list" note).

    Now in the document:
      §6.4  new   The measured breakthrough curves themselves (Fig. 9-11): the 3x3
                  design as small multiples, the sixteen grid runs overlaid, and the
                  five earlier runs overlaid separately
      §7          The four charts that were embedded without captions are now
                  Fig. 12-15; the three existing results figures became Fig. 16-18
                  (no prose referenced them by number, checked by grep)
      §7.1  new   Cross-run trends and model ranking (Fig. 19-21)
      §7.2        The five stale "6.???"/"7.?.4" pseudo-headings renumbered to
                  7.2/7.2.1-7.2.4 and promoted to Heading2/Heading3, so they reach
                  the table of contents for the first time
      §8.2        Error-statistics definitions and the nonlinear-vs-linearised
                  estimation-strategy justification (Hu et al. 2024 §4, §5.2, §5.5),
                  then Tables 14-17: fit quality for the 16 grid runs, both
                  campaigns' 24-model rankings, and the nested F-test on all 21 runs
      §8.5  new   Sensitivity analysis (Tables 18-21, Fig. 22-30), carrying the three
                  standing flags verbatim: q_dyn is not currently measurable (78.4 %
                  pure replicate error), k0 and h are not independently identifiable
                  (report kappa = k0*tau0^-h), L_MTZ's dynamic range is a formula
                  artefact; the pooled scope is shown but not used for inference
      §9.4  new   Numerical verification (Fig. 31-41: V1-V4, F5/F6, psi-quadrature
                  F1-F3, minimal kinetic x2), with the four limitations stated -
                  placeholder thermal parameters, floored epsilon, the unreconciled
                  two-temperature/pseudo-homogeneous split, and no fit against §6-§8
      App. A new  Per-run fit diagnostics: 7 plots x 21 real runs = 147 figures
                  (Fig. A1-A147), indexed by Table A.1. Nothing selected - every run
                  the pipeline fitted is there, flags carried into the index
      App. B new  Complete fit statistics: B.1 the 504-row master table (n, p, RSS,
                  R2, AdjR2, RMSE, chi2_red, AICc, dAICc, AAD), B.2 all fitted
                  parameters with curve_fit's asymptotic standard errors, B.3 all six
                  nested F-tests per run (126 rows), B.4 the 60 degenerate fits
      Also        Fig. 16's caption completed ("isother" -> "isotherm"); "Table 7)" and
                  "Table 11)" given the space they were missing after the bracket;
                  List of Figures gained 34 figure and 16 table entries and lost 2
                  superseded ones.

    Scripts (all new, all one-shot, all reading committed artefacts only):
      src/docs/review/_source/report_stats_tables.py      table builders
      src/docs/review/_source/insert_figures_and_stats.py the docx pass
      src/docs/review/_source/verify_figures_and_stats.py the checks below
      src/docs/review/_source/regen_truncated_p7.py       the one damaged figure

    Nothing was refitted. The only arithmetic is dAICc (a difference of two committed
    numbers) and the nested F-test, computed with breakthrough_fit.stats.f_test, the
    same function the pipeline calls - it reproduces table4_ftest.csv exactly.

    Verification, all executed: 35/35 checks pass. All 39 XML parts parse; 189 image
    references resolve to 189 distinct media parts with no double reference and no
    orphan; the 20 pre-existing images are byte-identical to the backup; body figures
    are 1-41 (8 reserved, see below) and appendix figures A1-A147, each caption
    directly following its picture; table captions 1-21, A.1 and B.1-B.4 each appear
    once; and all 12,148 cells of the fifteen generated tables were re-read out of the
    saved .docx and compared against freshly rendered tables from the source CSVs and
    the ANOVA workbook, with zero mismatches. Word opens the result in under 5 s:
    193 pages, 187 inline shapes, 37 tables, 44,697 words. Every picture paragraph
    and every table caption carries <w:keepNext>, so a page break cannot land between
    a figure and its caption or between a caption and its table.

    A figure-basis correction caught by rendering the draft and looking at it.
    fig9-fig12 from breakthrough_fit/cross_run_figs.py were drafted into §6.4 and
    §7.1, then pulled: that script's "clean runs" selector is ^(\d+)ml_(\d+)g$, i.e.
    the twelve SYNTHETIC parametric CSVs, and fig11/fig12 plot the May-* records.
    CLAUDE.md rule 1 forbids presenting either as measured, and the first PDF proof
    showed "50ml_2g" and "May-22-2026-conc10-flow0.05" printed inside figures
    captioned "Measured breakthrough curves". Replaced by src/solver/
    report_figs_measured.py, new, which builds four figures on the real 21-run basis:
    R1 the 3x3 design as small multiples with replicates overlaid and the flagged
    runs marked, R2 the sixteen grid runs on one axis, R3 the 24-model ranking with
    the two campaigns as separate series, R4 all six performance metrics against
    flow with the four provisional runs drawn as open markers. Curves come from the
    raw CSVs through the pipeline's own DataParser; every statistic is read back from
    the committed results CSVs. fig9-fig12 are left on disk, unused by the report.

    Two repository defects found while scoping, one fixed and one deliberately not:
      - P7_2026-07-03-conc5-flow0.10.png was truncated (852,244 bytes, ends mid-
        stream) in both breakthrough_out trees. Regenerated; the refit reproduces the
        committed optimum to 8.6e-7 max relative difference over 24 models x 10
        columns, which is what licensed using it. Only the PNG was replaced.
      - Nine of the sixteen results CSVs under the repo-root breakthrough_out/ carry
        unresolved git merge-conflict markers (<<<<<<< HEAD / ======= / >>>>>>>
        ed48a6a) and parse as 51 rows instead of 24. Both conflict sides agree to
        ~1e-14 relative and side A is byte-identical to the clean copy under
        src/solver/breakthrough_out/. NOT silently rewritten: the report build reads
        the clean tree and refuses any file that is not a 24-row single-run table.
        The root tree needs a real git resolution. Owner: author.

    Still open, flagged not fixed:
      - Fig. 8 ("Labelled process flow diagram") is in the List of Figures but has no
        caption and no image, and no such diagram exists anywhere in the repo. The
        number is left reserved rather than closing the gap by renumbering; the author
        must supply the diagram or delete the entry.
      - The abstract still carries the literal placeholder "[Insert 1-2 sentences
        summarising your key experimental findings/trends here...]".
      - `mechanistic_selfcontained.py`'s RUNS dict now lists "run 1".."run 9", but
        `new runs/` contains only run 3/4/5/6/8, so parse_run("run 1") raises and the
        script can no longer reproduce its own committed F5/F6. Those two figures are
        from the real five runs (their titles and annotations prove it) and are used
        as-is; the script needs its RUNS dict restored. Owner: author.
      - The document is 43.7 MB (42.1 MB before Word's own re-save). Rebuild the
        atlas with --max-width 1100 for roughly 26 MB if a
        submission portal objects; P7 and the 9-panel sensitivity figures lose
        legibility at that width.
      - The table of contents was refreshed and saved through Word after the build,
        so it already lists 6.4, 7.1, 7.2.x, 8.5, 9.4, Appendix A (all 21 run
        subsections) and Appendix B.1-B.4 with page numbers. That save renumbered
        and re-encoded the media parts, which is why the verifier compares
        pre-existing images by decoded pixels rather than by part name; all 20 are
        present unaltered.
      - requirements.txt gained openpyxl and pillow; the interpreter is .venv/, not
        the venv/ that CLAUDE.md still names.

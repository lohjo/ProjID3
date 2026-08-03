# Scientific Figure Audit + Reproducibility Review — T32_PI05 Interim Report

**Document audited:** `src/docs/T32_PI05_Interim_Report.docx` ("CO2 Adsorption in Packed-Bed Column using Polymer-based Sorbent: Parametric Study and Model Prediction", Interim Report, dated 18 May 2026)
**Auditor basis:** report text + all 17 embedded images (extracted from the docx), rendered PDF pages, repo pipeline outputs (`src/solver/breakthrough_out/`), raw data (`src/solver/data/new runs/`), `src/docs/hu2024.pdf`. All numeric checks below were executed (scripts run in-session); nothing is asserted from memory.
**Standard:** every claim treated as unverified until traced to evidence. Facts reported by the paper, my inferences, and my criticisms are labelled throughout.

---

## Phase 1 — Paper Model

**Research question.** How do inlet CO₂ concentration and flow rate affect breakthrough dynamics of a PEI@SiO₂ (C³) packed bed, and which breakthrough model best describes the measured curves?

**Hypotheses (implicit — never stated as testable hypotheses).**
- H-a: breakthrough time decreases with flow rate and inlet concentration (§6).
- H-b: fractal-like / asymmetric models (fractal-BA, fractal-Gudermannian, fractal-erf, Clark, Weibull) outperform classical logistic models on tailed curves (§3.5.2–3.5.3, §7).
- H-c: BA, Thomas, and YN are one logistic function in three notations (§3.4.4).

**Methodology.** Fixed-bed rig (§4 SOP: two gas cylinders, 3 MFCs, CO₂ analyser/TI/PI/FI train); breakthrough runs; nonlinear least-squares fitting in Python (`scipy`, per Fig. 9 caption).

**Datasets/materials.** PEI@SiO₂ C³ granules, ~8 g, bed 21.0–21.5 cm in an 8.5 mm i.d. × 38.6 cm column. Claimed design: 3×3 (5/10/15 % CO₂ × 50/100/150 mL/min), Table 4.

**Variables.** Independent: inlet CO₂ % , total flow. Dependent: t_B (C/C₀ = 0.05), t_E (C/C₀ ≥ 0.95, stable ≥ 5 min), t₅₀. Controls: none reported (no blank-column run, no replicate runs, ambient uncontrolled T).

**Statistics.** Report shows only R² on figure legends; no error bars, CIs, replicate counts, or test statistics in the text. (The repo pipeline computes AdjR², RMSE, AICc, F-tests — almost none of this reaches the report.)

**Conclusions and where they appear:**

| # | Conclusion | Location | Claimed support |
|---|---|---|---|
| C1 | "Models are validated against breakthrough data … across a 3×3 design of experiment" | Abstract; §2.1 | Table 4 |
| C2 | Higher flow and concentration accelerate breakthrough | §5 ¶2, §6 ¶1 | Table 4 |
| C3 | Equilibrium time has "a good in-between value … at peak optimisation" | §5 ¶2 | Table 4 (rows 4–6) |
| C4 | BA/Thomas/YN are mathematically equivalent logistics | §3.4.4 | Theorem + proof |
| C5 | Slope-matched logistic/erf/Gudermannian differ by sup-norm < 0.04 | §3.4.4 Remark | Stated bound |
| C6 | Fractal-like kinetics give superior fits for asymmetric curves | §3.5.2, §7 | Fig. 11; cited lit. |
| C7 | SOP resolves data-reliability problems | Abstract, §4 | §4 itself |

**Flag — conclusions with no supporting evidence in the report:** C3 (a two-point "optimum" claim from non-replicated single runs); C7 (no before/after comparison demonstrating the SOP improved reliability). C1 is contradicted by the underlying data (Phase 3/4).

---

## Phase 2 — Figure Audit

The docx contains 11 figure objects (some vector drawings, some bitmaps) plus a logo and three signature images. Figure numbering in the List of Figures does not match the body: the List stops at "Fig. 10" while the body contains a Fig. 11; the List includes "Table 1" and a "Fig. 5 & 6" entry containing a full OneDrive sharing URL that should not appear in a report.

### Fig. 1 — Singapore GHG emissions by sector (OWID chart, p. 6)
- **Purpose:** motivate CO₂ capture relevance for Singapore. Variables: sector (categorical) vs Mt CO₂eq.
- **Integrity:** axes/units fine (source chart). Caption typo "by section". Adapted-from credit given in List of Figures but not under the figure itself.
- **Criticism (inference):** the dominant bar, "Aviation and shipping, 184 Mt", reflects OWID/Climate Watch attribution of *international bunker fuels* to Singapore as a refuelling hub — roughly 4× all domestic sectors combined. Using it unqualified to argue Singapore's domestic abatement need is potentially misleading; a footnote on bunker attribution is needed.
- **Support for claim:** moderate (context only). **Confidence: 70/100.**

### Fig. 2 — Research methodology flowchart (p. 16)
- **Integrity:** legend defines yellow = "Decision nodes", green = "Input nodes", but "Experimental data" and "Breakthrough curve" are yellow (they are inputs, not decisions) — the colour semantics are internally inconsistent. §3.1 consists solely of this figure; there is no prose "Overview".
- **Support:** weak (decorative). **Confidence: 55/100.**

### Fig. 3 / Fig. 4 — Packed-bed schematic; granule diagram (p. 18)
- **Integrity:** clean vector drawings. Notation drift: the List of Figures caption promises y_in, u_s, T_in; the figure and §3.3 text use c_in, u_in, and no temperature. §3.3 also switches between "internal radius R" and diameter conventions used later (0.85 cm i.d.).
- **Support:** adequate for setup description. **Confidence: 70/100.**

### Fig. 5 — MTZ schematic; Fig. 6 — breakthrough curve diagram (pp. 19–20; sourced from SUTD pptx)
- **Integrity:** legible; v₀ = Q₀/A_c and v = Q₀/(εA_c) defined. Cross-referencing is wrong in the text: §3.3 says "In Fig. 4) the inlet CO₂ concentration … flows at v₀" (that is Fig. 5) and "in Fig. 5) the bed divides into three zones" while announcing "three zones: saturation zone, mass-transfer zone, and adsorption zone" — the saturation and adsorption zones are also conflated in the description ("the adsorbent contaminant reaches dynamic equilibrium" is garbled). Fig. 6's red shading labelled "breakthrough sorption capacity" shades a rectangle left of t_B rather than the area between the curve and C/C₀ = 1, which is the actual capacity integral — pedagogically misleading.
- **Attribution:** figures are third-party (SUTD); source credited only via a OneDrive link in the List of Figures.
- **Support:** background only. **Confidence: 65/100.**

### Fig. 7 — rig photo; Fig. 8 — process flow diagram (pp. ~29–30)
- **Integrity:** photo shows numbered valves ①–⑤ consistent with SOP; PFD shows N₂/CO₂ cylinders, 3 MFCs, purge line, column with TC, outlet train CO₂→TI→PI→FI matching §4.1.3. These are the strongest figures in the report.
- **Note (fact):** the PFD bitmap is embedded twice in the docx (media/image10.png and image11.png are pixel-identical duplicates); harmless but indicates draft hygiene.
- **Contradiction (criticism):** §4.1.2 states the column is "inside diameter of 8.2 mm and length of 32 cm", while §4.1.3's equipment list and §5 state 0.85 cm i.d. × 38.6 ± 0.1 cm. Two different columns are described within the same SOP. One must be corrected.
- **Support:** strong for apparatus description. **Confidence: 85/100 (photo), 85/100 (PFD).**

### Fig. 9 — "Predicted vs. observed values in breakthrough models fit using scipy.optimise_curve.fit()" (4 panels, §6)
- **What it is (fact):** the pipeline's P1 parity plots for **runs 3, 4, 5, 6** (panel titles say so). Legends list 8 models each with R² ≈ 0.996–0.9996.
- **Integrity problems:**
  1. **Run 8 is silently omitted** — the report elsewhere implies 9 runs; even the 5 measured runs are not all shown. No explanation given. Selective presentation.
  2. Panel titles ("P1 — predicted vs observed (run N)") expose internal run IDs that are never defined in the report; a reader cannot map "run 3" to a row of Table 4.
  3. Legends are illegibly small at print size; colours for 8 models are not distinguishable.
  4. **Parity plots cannot discriminate models.** When all models achieve R² > 0.99, predicted-vs-observed scatter compresses onto the diagonal; the informative differences (tail behaviour, residual structure) are invisible. The figure demonstrates only that sigmoids fit sigmoids.
  5. No error bars, no replicate structure, n per panel not stated (pipeline n = 285 for run 6).
  6. Caption cites a nonexistent API, "scipy.optimise_curve.fit()" (the function is `scipy.optimize.curve_fit`).
- **Support for "models fit well":** weak-to-moderate; support for model *selection*: none. **Confidence: 50/100.**

### Fig. 10 — captioned "Breakthrough curve fitting with linear adsorption isotherm" (§6)
- **What it actually shows (fact):** the pipeline's P2 plot for **run 6**, titled "P2 — breakthrough curves (run 6)" with two panels: "Langmuir-isotherm fits" (M01 YN/Thomas/BA, M02 Clark, M16, M17) and "Freundlich-isotherm fits" (M04, M19).
- **Integrity problems:**
  1. **Caption does not match content.** No "linear adsorption isotherm" fit is shown; the panels are labelled Langmuir- and Freundlich-class models.
  2. **A failed fit is displayed:** legend shows "M19 R² = nan" — a non-converged model plotted as if informative. M16 (R² = 0.327) is also plotted and visibly wrong, and the green M16 curve exhibits a solver artifact spiking down to C/C₀ ≈ 0.4 near t = 0.
  3. Only 1 of 5 runs shown; no criterion given for choosing run 6.
  4. **Internal contradiction with Table 4:** the dotted t_E (C/C₀ = 0.95) marker sits at ≈ 39 min, consistent with the pipeline value for run 6 (t_E = 2357 s = 39.3 min, from `breakthrough_out/run 6/results_run 6.csv`), but Table 4 row 6 reports equilibrium time = 58 min. The figure and the table disagree about the same run within the same report. Likewise the plotted t_b marker (~0.3 min; pipeline 19.0 s) contradicts Table 4's 3 min.
- **Support for any stated claim:** does not support the caption's claim (linear isotherm); weakly supports "several models fit run 6". **Confidence: 35/100.**

### Fig. 11 — "Validation of fractal-like kinetics on logistic breakthrough model curve" (§6)
- **What it shows (fact):** pipeline P6 for run 6: standard YN (M01, R² = 0.942, structured residuals ±0.1–0.2) vs fractal YN (M23, R² = 0.999, h = 0.865, "F-test p = 1.84e-248"), with residual panels.
- **Strengths:** this is the right *kind* of figure — side-by-side fit + residuals genuinely demonstrates that the symmetric logistic underfits the tail and the fractal modification removes most structure. Residual y-scales differ appropriately (±0.2 vs ±0.02) and are labelled.
- **Integrity problems:**
  1. **The F-test p-value is not credible as stated.** p = 1.84×10⁻²⁴⁸ presumes i.i.d. residuals; breakthrough data sampled every 5 s are strongly serially correlated (visible in both residual panels: smooth low-frequency structure, growing tail oscillation in the fractal panel). The effective sample size is far below n = 285, and the p-value is inflated by many orders of magnitude. The qualitative conclusion survives; the number should not be printed.
  2. Missing from the List of Figures; only run 6 shown; h = 0.865 is a large heterogeneity exponent whose physical plausibility is never discussed (h → 1 makes k(t) = k₀t⁻ʰ nearly non-integrable at t → 0).
  3. Residual autocorrelation, sensor noise growth at the tail (right panel, t > 80 min) unexplained.
- **Support for C6 (fractal superiority):** moderate — convincing for run 6, unquantified for the rest. **Confidence: 65/100.**

---

## Phase 3 — Cross-Figure / Cross-Table Consistency

1. **Table 4 vs pipeline outputs (the central inconsistency).** I recomputed nothing by hand; values below are read directly from `breakthrough_out/run N/results_run N.csv` (t_b: C/C₀ = 0.05; t_E: 0.95):

   | Run (Table 4 row) | Table 4 t_B / t_E (min) | Pipeline t_b / t_E (min) | Ratio t_B | Ratio t_E |
   |---|---|---|---|---|
   | run 3 (row 3: 5 %, 0.15) | 2 / 110 | 0.30 / 58.4 | 6.6× | 1.9× |
   | run 4 (row 4: 10 %, 0.05) | 11 / 146 | 0.57 / 77.7 | 19× | 1.9× |
   | run 5 (row 5: 10 %, 0.10) | 3 / 64 | 0.23 / 31.7 | 13× | 2.0× |
   | run 6 (row 6: 10 %, 0.15) | 3 / 58 | 0.32 / 39.3 | 9× | 1.5× |
   | run 8 (row 8: 15 %, 0.10) | 2 / 81 | 0.44 / 34.5 | 4.5× | 2.3× |

   No definition of breakthrough/equilibrium reconciles both columns (the SOP §4.2.4 and §4.4 use exactly the 5 % / 95 % thresholds the pipeline uses). The systematic ~2× on t_E and 4–20× on t_B indicates Table 4 was **not produced by the stated analysis pipeline** — plausibly hand-read from raw sensor logs under different conventions, but the report gives no such provenance. Until traced, Table 4 is unverified.

2. **Rows 1, 2, 7, 9 of Table 4 have no traceable measured basis.** The measured dataset in this repo comprises five bench runs (run 3/4/5/6/8, `src/solver/data/new runs/`). Files matching rows 2/4/5 nominal conditions exist only as `May-*.csv`, which are synthetic/placeholder per the repo's own data policy, and their processed metrics (e.g. May-20 conc5_flow0.1: t_E = 26.2 min) match Table 4 nowhere. For rows 1 (5 %, 0.05), 7 (15 %, 0.05) and 9 (15 %, 0.15) no data file predating the 18 May report exists at all (15 %/50 mL and 15 %/100 mL files are dated July 10, 2026). **The abstract's "validated … across a 3×3 design of experiment" is therefore unsupported: at most 5 of 9 cells were measured when the report was written.**

3. **Trend claims vs measured metrics.** §6 asserts monotonic acceleration of breakthrough with flow at 10 % CO₂. Pipeline values are non-monotonic: t₅₀ = 12.6 min (run 4, 50 mL) → 3.8 min (run 5, 100 mL) → 4.0 min (run 6, 150 mL); t_E = 77.7 → 31.7 → 39.3 min. The 100→150 mL step *increases* t₅₀ and t_E slightly (runs 5 vs 6 also differ in C₀: 9.5 % vs 10.2 %, and bed length 21.2 vs 21.5 cm — confounded). The clean monotonic story in §6 rests on the unverified Table 4 numbers.

4. **Geometry contradiction:** 8.2 mm/32 cm (§4.1.2) vs 8.5 mm/38.6 cm (§4.1.3, §5, Table 2). Fig. 10's t_E marker vs Table 4 (item 1 above). Notation contradictions: c_in vs y_in vs C₀ for inlet composition; u_s vs u_in vs v₀.

5. **Units errors in Table 2 (verified arithmetically):**
   - "Volume flow rate 3.0–9.0 cm³·h⁻¹" — the correct values are 3.0–9.0 **L·h⁻¹** (50–150 mL/min); as printed the flows are 1000× too small and inconsistent with "Inlet velocity 1.47–4.41 cm/s" two rows above (which is correct: Q/A with A = 0.5675 cm²).
   - "Volume of packing 11.92 cm³" corresponds to exactly 21.0 cm bed; bed heights vary 21.0–21.5 cm per run, so the single volume is over-precise.
6. **Table 3 "Interstitial Velocity" (verified arithmetically):** the listed 0.049/0.098/0.147 m/s equal superficial velocity ÷ 0.30 exactly. ε = 0.30 is a code floor applied because pellet density ρ_p is unknown (the raw estimate ε ≈ 0.16 from assumed ρ_p = 800 kg/m³ is unphysical). The table presents a placeholder-derived quantity as measured, with no mention of ε or its provenance. Also: the column header "Hgt. of Carbon Bed" refers to a **carbon** bed — the sorbent is PEI@SiO₂ — evidence of an uncorrected template import; §5's opening sentence "equilibrium adsorption data was carried out in an experimental batch adsorber" likewise describes a batch system that appears nowhere else and contradicts the fixed-bed method.
7. **Sample-size opacity:** nowhere does the report state points per run, run durations, or that zero replicate runs exist.

---

## Phase 4 — Claim-to-Evidence Audit

| Paper Claim | Supporting Figures | Supporting Tables | Supporting Equations | Evidence Strength | Confidence |
|---|---|---|---|---|---|
| C1: 3×3 DOE executed & models validated (Abstract, §2.1) | — | Table 4 | — | **Does not support** — 4 of 9 cells untraceable; remaining 5 disagree with pipeline metrics | 15/100 |
| C2: ↑flow, ↑conc ⇒ faster breakthrough (§6) | (Fig. 10, indirectly) | Table 4 | — | Weak — direction plausible and lit-consistent, but the specific numbers are unverified and measured metrics are non-monotonic at 10 % | 40/100 |
| C3: equilibrium-time "peak optimisation" (§5) | — | Table 4 rows 4–6 | — | Does not support — single unreplicated runs; no uncertainty; likely noise | 10/100 |
| C4: BA≡Thomas≡YN logistic (§3.4.4) | — | — | Theorem + proof | Strong — algebra correct up to a sign typo (below); consistent with Hu et al. 2024 | 85/100 |
| C5: sup-norm < 0.04 for slope-matched sigmoids (§3.4.4) | — | — | Remark ineq. | **Verified independently**: computed sup-differences 0.018 (σ vs erf), 0.013 (σ vs gd), 0.031 (erf vs gd) — all < 0.04 | 90/100 |
| C6: fractal kinetics superior for asymmetric curves (§3.5.2, §7) | Fig. 11 | — | k(t)=k₀t⁻ʰ | Moderate — demonstrated on one run; F-test p-value invalid; consistent with pipeline rankings across runs | 65/100 |
| C7: SOP solves data-reliability issues (Abstract) | Figs. 7–8 | — | — | Not tested — no before/after evidence | 20/100 |

**Equation-level errors found (all in §3.4):**
- **Sign error in the Theorem:** it defines σ(k_YN(t−τ)) := 1/(1+exp(k_YN(t−τ))), which *decreases* in t (c/c₀ → 0 as t → ∞ — desorption, not breakthrough). The Remark's σ(x) = (1+e⁻ˣ)⁻¹ and the proof are correct; the Theorem's ":=" line contradicts both.
- **Yoon-Nelson (§3.4.3):** c/c₀ = 1/(1+exp(a+bt)) with b = k_YN > 0 is likewise decreasing; the standard form is 1/(1+exp(k_YN(τ−t))).
- **Danckwerts BC (§3.3):** written as D_L ∂c/∂t|₍z=0₎ = …; the flux condition requires **∂c/∂z**. As printed it is dimensionally wrong.
- **Bohart-Adams limit (§3.4.1):** the linearised form is claimed "as k_BA becomes very large"; the actual condition is exp(k_BA N₀L/u) ≫ 1, which holds at large *bed capacity term*, not merely large k_BA — and a large k_BA also shrinks the transition width, degrading the c/c₀ range where the linearisation applies.
- **Clark model (§3.4.5):** stated n ≥ 1 but the exponent 1/(n−1) is singular at n = 1; also reduces to logistic at n = 2 (correct) — the reference "Eq. (??)" is an unresolved cross-reference, and "Eq. ()" appears empty twice in §3.4.2. Notation switches silently: a = k_T q₀M/Q uses M, Q where m, v were defined.

---

## Phase 5 — Hidden Assumptions

**Explicit (stated):** plug flow, negligible radial dispersion, LDF kinetics, spherical particles, constant velocity/void fraction (§3.3, attributed to Hu et al. 2024).

**Implicit / unstated — each materially affects conclusions:**
1. **Constant interstitial velocity at up to 15 % CO₂.** Adsorbing 10–15 % of the molar flow reduces gas velocity along the bed by a comparable fraction. The constant-u assumption is borrowed from trace-aqueous systems (Hu et al. 2024 is a *Journal of Water Process Engineering* review); at these concentrations velocity variation distorts fitted k and τ. Never acknowledged.
2. **Isothermality.** CO₂ chemisorption on PEI is strongly exothermic (~85–90 kJ/mol scale for amine sorbents); the SOP even records outlet temperature "to detect thermal wave front" (§4.4), yet no temperature data are reported and all fitted models are isothermal. A thermal wave co-propagating with the MTZ changes local equilibrium and curve shape — an alternative explanation for the "fractal" tail (Phase 8).
3. **Aqueous-literature transferability.** The entire model family (norfloxacin/GAC, bisphenol-A/polyaniline benchmarks in §3.5) is liquid-phase. Gas-phase differences (compressibility, thermal effects, velocity change) are never discussed.
4. **ε = 0.30** underlying Table 3's interstitial velocities is a placeholder floor, not a measurement (needs ρ_p; owner: lab / Stampi-Bombelli). Any quantity derived from interstitial velocity inherits this.
5. **Ideal step input at t = 0.** Valve-switching (§4.2.4) plus dead volume between valve 3 and the bed produces a smeared inlet step; at t_b of order 20–30 s (pipeline values), dead-volume lag is a first-order confounder of the "breakthrough time" itself.
6. **Sensor fidelity:** the Gaslab CO₂ sensor's range, accuracy, and response time at 5–15 vol% are never stated; §5 admits "sudden sensor jumps" and curves "never reaching initial concentration" — the latter also consistent with sensor calibration drift rather than incomplete saturation.
7. **Statistical:** i.i.d. Gaussian residuals assumed by least squares and the F-test; violated by 5 s autocorrelated sampling (see Fig. 11 critique).
8. **Measurement:** inlet C₀ assumed equal to nominal (5/10/15 %); measured values are 4.74/9.78/9.54/10.21/15.06 % — the 4.74 % run misses the SOP's own ±2 % acceptance criterion (§4.3.1) if read as relative deviation (−5.2 %); the criterion's ambiguity (relative vs absolute) is itself a flaw.

---

## Phase 6 — Reproducibility Audit

**Reconstructed pipeline (inference from report + repo):**
raw 5 s CO₂ ppm logs → (unstated despiking) → normalize to C/C₀ → fit ~24 sigmoid models via `scipy.optimize.curve_fit` → report R², extract t_B/t_E/t₅₀ → compare models.

**Pseudocode (as reconstructible from the report alone):**
```
for each run in DOE(conc ∈ {5,10,15}%, Q ∈ {50,100,150} mL/min):
    log ppm(t) every 5 s until C/C0 ≈ 1          # SOP §4.2.4
    C/C0 = ppm / C0                               # C0 provenance unstated
    for model in {BA/Thomas/YN, Clark, gd, erf, Weibull, fractal-*…}:
        params = curve_fit(model, t, C/C0)        # bounds, starts, loss: unstated
    t_B = t(C/C0=0.05); t_E = t(C/C0≥0.95 stable 5 min)
```

**Missing information that blocks independent reproduction from the report alone:**
- sorbent: granule size d_p, PEI loading, pellet density ρ_p, bed void fraction ε, per-run sorbent mass (only "~8 g" pre-run);
- environment: temperature (ambient, unlogged in report), humidity (PEI capacity is strongly humidity-sensitive), pressure;
- instruments: CO₂ sensor model/range/accuracy/response time, MFC models/calibration;
- data processing: despiking rule, baseline correction, how C₀ was fixed (nominal vs measured plateau), points per run;
- fitting: model list and functional forms actually fitted (report describes ~10 forms, figures reference codes M01–M24 that are never defined), parameter bounds, initial values, multi-start policy, random seed, convergence criteria;
- statistics: how R² was computed, any model-selection criterion (AICc exists in the pipeline but is absent from the report);
- raw data availability: no data or code availability statement at all.

The repo itself contains most of this (`breakthrough_fit/` package: 10 starts, seed 42, L-BFGS-B fallback, AICc, F-tests) — but the report neither cites the repo nor describes these settings, so an external reader cannot reproduce it.

**Score: Partially reproducible.** The SOP (§4) is genuinely detailed enough to re-run the *experiment*; the *analysis* is not reproducible from the report, and Table 4 is not reproducible even *with* the repo (Phase 3, item 1).

---

## Phase 7 — Independent Reimplementation Plan

1. **Software:** Python 3.11, numpy/scipy/matplotlib. Reimplement the ~10 stated model forms (logistic, Clark, normalized gd/erf, Weibull, fractal-BA/gd/erf) directly from §3.4 equations — feasible except one must *correct the YN/Theorem sign errors* first.
2. **Hardware/materials:** 8.5 mm i.d. × 38.6 cm column; ~8 g PEI@SiO₂ granules (source: SUTD; composition unavailable → substitute commercial PEI-silica and expect different capacity); 2 MFC-blended N₂/CO₂ feed at 50–150 mL/min, 5–15 vol%; NDIR CO₂ analyser rated ≥ 20 vol% with ≤ 5 s response.
3. **Experiments:** replicate the 3×3 grid **in triplicate**, logging inlet C₀ via bypass before each run (SOP §4.2.3 supports this), bed T at two axial positions, ambient T/RH.
4. **Validation:** recompute t_B/t_E/t₅₀ with the 5 %/95 % definitions; fit models with multi-start NLS; select by AICc; compare fractal vs standard by F-test *with autocorrelation-robust inference* (e.g. block bootstrap).
5. **Difficulty:** moderate (2–3 weeks bench + 1 week analysis). **Expected failure points:** sorbent equivalence (largest risk); dead-volume correction at short t_B; sensor saturation/nonlinearity at 15 %; ambient T/RH drift across runs; reproducing Table 4 (expected to fail — see Phase 3).

---

## Phase 8 — Robustness Analysis

- **Confounder — thermal effects:** the "asymmetric tail" attributed to fractal surface heterogeneity is equally consistent with an exotherm-driven equilibrium shift; no temperature trace is shown to exclude it. h = 0.865 may be soaking up thermodynamics, not fractality.
- **Confounder — velocity change and dead volume** (Phase 5, items 1 & 5): both distort early-time shape, where t_B (order 20 s, per pipeline) lives entirely.
- **Confounded design:** runs 5 vs 6 differ in flow *and* C₀ *and* bed height; single-factor conclusions in §6 are not cleanly identified.
- **Selection bias:** only run 6 shown in Figs. 10–11; run 8 dropped from Fig. 9; the best-fitting model family is showcased against the *worst* symmetric baseline (M01) rather than against Clark/Weibull, which are closer competitors.
- **Overfitting risk:** 24 models × small run count, ranked by R² alone in the report; R² differences of 0.001 among 8 models (Fig. 9 legends) are meaningless without information criteria (the pipeline's AICc/W_AICc never appear in the report).
- **Data-provenance risk (the dominant one):** Table 4's 9-cell matrix cannot currently be traced to raw data (4 cells) or reconciled with the pipeline (5 cells). Until resolved, every downstream claim (C1–C3) is unsupported.
- **Overclaiming:** Abstract "Models are validated" — nothing is validated in the report's own sense (no hold-out, no prediction test, no gate criteria); "SOP is proposed to solve these issues" — untested; intro states atmospheric CO₂ "rose from 280 ppm to over 440 ppm above pre-industrial levels" — the phrasing is garbled ("above pre-industrial levels" cannot modify 440 ppm) and the 440 figure is unsourced and likely overstated for 2026; verify against the cited Xu et al. (2024).
- **Correlation vs causation:** acceptable here (manipulated variables), but the "peak optimisation" claim (C3) is a two-point artefact.

---

## Phase 9 — Reviewer Critique (as for a journal/conference)

**Major strengths.** (1) The mathematical unification section (§3.4.4) is the report's best contribution: the BA/Thomas/YN equivalence is proved cleanly and the sup-norm ≤ 0.04 claim survives independent numerical verification. (2) The SOP (§4) is unusually complete for a student report — valve-by-valve, with acceptance criteria and a data-recording checklist. (3) Fig. 11 uses the correct visual grammar (fit + residuals) and the underlying analysis pipeline (multi-start NLS, AICc, F-tests) is more sophisticated than the report reveals. (4) Literature coverage of asymmetric breakthrough models is current and relevant.

**Major weaknesses.** (1) **Evidence–claim gap on the central experimental result:** the 3×3 "validated" matrix (Abstract, Table 4) is irreproducible from the project's own pipeline, four of its nine cells have no traceable data, and its numbers contradict the report's own Fig. 10 markers for run 6. This alone would trigger major revisions at any venue. (2) Equation errors: sign errors in the YN model and the equivalence Theorem, a wrong derivative in the Danckwerts BC, unresolved "Eq. ()"/"Eq. (??)" references. (3) Figure integrity: mismatched caption (Fig. 10), displayed failed fits (R² = nan), omitted run 8, undefined model codes M01–M24, illegible legends. (4) No statistics: no replicates, no uncertainty on any number, an invalid p-value as the only test statistic shown. (5) Internal contradictions: two column geometries, batch-adsorber sentence, "Carbon bed" header, duplicated section numbers (two §2.2, two §3.3), SOP subsections ordered 4.2.1→4.2.3→4.2.2→4.2.4. (6) **Reference list is broken:** ~25+ in-text citations are missing from the list — including Hu et al. (2024), the paper the whole modelling framework rests on (repo copy: *J. Water Process Eng.* 59 (2024) 105065) — while ~14 listed entries (e.g. Langlo & Espedal 1994, two-phase flow in porous media) are never cited in the text.

**Novelty:** low-to-moderate (review + application; the equivalence theorem is known — cf. Hu et al. 2024, Chu 2020 — though the sup-norm quantification is a nice touch). **Technical correctness:** mixed (Phase 4). **Experimental rigor:** weak (no replicates, uncontrolled T/RH, confounded factors). **Statistical rigor:** weak. **Presentation:** below standard (contradictions, broken cross-references, OneDrive URL in List of Figures). **Reproducibility:** partial.

**Recommendation: Major revision.** For an interim student report the trajectory is credible, but Table 4 must be regenerated from the pipeline with stated definitions, the unmeasured DOE cells relabelled "planned", and the abstract's "validated" claim withdrawn or scoped to what exists. **Reviewer confidence: high** (audit performed against the raw data and analysis code, not just the manuscript).

---

## Phase 10 — Future Work / Required Fixes

**Must-fix before the final report (ordered by severity):**
1. Rebuild Table 4 from `new_runs_pipeline.py` outputs; state the t_B/t_E definitions in the caption; mark cells 1, 2, 7, 9 as *planned/not yet executed* (or attach their raw logs with dates); reconcile with Fig. 10's markers.
2. Replace "validated against … a 3×3 design" (Abstract) with "fitted against five completed runs of a planned 3×3 design".
3. Correct the YN and Theorem signs, the Danckwerts BC derivative, the §4.1.2 geometry, Table 2's flow-rate units (L/h), and resolve all "Eq. ()" references.
4. Repair the reference list (add Hu 2024, Hu 2019/2025, Kimani 2023, Khim 2019, Chen 2020, Ruthven, etc.; delete or cite the orphans).
5. Disclose ε = 0.30 as an assumption pending ρ_p (owner: lab / Stampi-Bombelli) wherever interstitial velocity appears.

**Missing experiments:** triplicates of at least the 10 % flow sweep (runs 4/5/6 conditions); a blank-column (no sorbent) run to quantify dead-volume lag; simultaneous bed-temperature logging to separate thermal from fractal tailing; a humidity-controlled pair of runs.

**Stronger analysis:** report AICc/weights instead of bare R²; residual-autocorrelation-aware model comparison (block bootstrap); fit fractal vs Clark vs Weibull head-to-head across all five runs (the pipeline already ranks them — surface it); propagate C₀ and flow uncertainty into q_dyn.

**Better visualization:** replace Fig. 9's parity panels with overlaid breakthrough curves + residuals per run (the pipeline's P2/P6 style) for all five runs; define M-codes in a table; drop non-converged models from plots; add run-condition annotations (C₀, Q, bed L) to every panel.

**New directions:** connect the fitted logistic/fractal parameters to the mechanistic 4-PDE model (Gate A–C path already planned); use the equivalence theorem to reduce the fitted-model family; test the travelling-wave/constant-pattern prediction k_YN ∝ u/L against the flow sweep.

---

### Sources
- Report: `src/docs/T32_PI05_Interim_Report.docx` (all section/figure/table references above)
- Pipeline metrics: `src/solver/breakthrough_out/run {3,4,5,6,8}/results_run N.csv`; synthetic/May outputs under `src/solver/breakthrough_out/`
- Raw data inventory: `src/solver/data/new runs/` (run 3/4/5/6/8 + July-10-2026 files), `src/solver/data/May-*.csv`
- Central reference identity: `src/docs/hu2024.pdf` (Q. Hu et al., *J. Water Process Eng.* 59 (2024) 105065)
- Numeric verifications (sup-norm, velocities, bed volume, unit checks) executed in-session; scripts reproducible from the commands quoted in this audit's history.

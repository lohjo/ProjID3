# Results and Discussion: Goodness of Fit and Parameter Estimation

*CO₂ Adsorption Breakthrough in a Packed-Bed Column Charged with PEI–SiO₂ Granules*

---

## 4. Parameter Estimation Strategy

### 4.1 Model Set

Nine empirical breakthrough models, spanning two to three free parameters each, were selected to characterise the outlet concentration–time profiles (Table 1). The set encompasses symmetric logistic-family models (Yoon–Nelson / Thomas / Bohart–Adams, Gudermannian, error function), asymmetric extensions (Clark, Modified Dose-Response), a stretched-exponential form (Weibull), the Klinkenberg linear-driving-force approximation, and the fractal Bohart–Adams model of Hu et al. (2024). The Wolborska model was retained solely for comparison in the initial rising region (C/C₀ ≤ 0.15); its statistics are not directly comparable to complete-curve models and are excluded from the primary ranking.

**Table 1 — Candidate models and parameter count.**

| Code | Model | Free params *p* | Functional form |
|------|-------|:---:|---|
| M01 | Logistic (Yoon–Nelson / Thomas / Bohart–Adams) | 2 | $C/C_0 = [1 + \exp(k_\text{YN}(\tau - t))]^{-1}$ |
| M02 | Clark | 3 | $C/C_0 = C_\infty [1 + A \exp(-rt)]^{-1/(n-1)}$ |
| M04 | Modified Dose-Response (MDR) | 2 | $C/C_0 = 1 - [1 + (t/t_{50})^a]^{-1}$ |
| M05 | Wolborska (early window only, C/C₀ ≤ 0.15) | 2 | $\ln(C/C_0) \approx \beta_w/N_0 \cdot C_0 t - \text{const.}$ |
| M06 | Gudermannian | 2 | $C/C_0 = \tfrac{1}{\pi}\operatorname{gd}(k(t-\tau)) + \tfrac{1}{2}$ |
| M07 | Error function | 2 | $C/C_0 = \tfrac{1}{2}[1 + \operatorname{erf}(k(t - \tau))]$ |
| M14 | Weibull | 2 | $C/C_0 = 1 - \exp[-(t/\tau)^k]$ |
| M16 | Klinkenberg | 2 | $C/C_0 \approx \tfrac{1}{2}[1 + \operatorname{erf}(\sqrt{\tau_K} - \sqrt{\zeta})]$ |
| M23 | Fractal-BA (Fractal Yoon–Nelson, Hu 2024) | 3 | $C/C_0 = [1 + k_{\text{YN}0}\,t^{1-h}/(1-h) \cdot \exp(-k_{\text{YN}0}\tau_0)]^{-1}$ |

### 4.2 Nonlinear Least-Squares Fitting

All models were fitted by nonlinear least squares using `scipy.optimize.curve_fit` with the Trust Region Reflective (TRF) algorithm, which handles bounded parameter spaces reliably. For each model, a battery of twelve starting-point initialisations was employed: one data-driven seed (derived from moment estimates or characteristic time interpolation specific to each model) and eleven additional starts sampled uniformly at random within the physical parameter bounds, using a fixed random seed (42) for reproducibility. The optimiser converged to the best-RSS solution across all starts.

Parameter bounds were enforced throughout to exclude non-physical solutions: rate constants were constrained to be strictly positive; characteristic times were bounded between a small positive floor and four times the maximum observed time; the Weibull shape exponent and fractal exponent *h* were bounded to (0, 1). For models with implicit or NaN-prone evaluation kernels (Chern–Chien types), a fall-back L-BFGS-B minimisation of the residual sum of squares was employed, with the approximate covariance matrix estimated via finite-difference Hessian.

The Wolborska model was fitted exclusively on the early-breakthrough sub-window (0.005 < C/C₀ ≤ 0.15) as required by its derivation as an initial-slope approximation; its goodness-of-fit statistics are computed on that restricted window and are not comparable to complete-curve statistics.

### 4.3 Goodness-of-Fit Statistics

Eight scalar statistics were computed per (model, run) pair from the vector of *n* observations and *p* free parameters. The formulas, following the notation in Hu et al. (2024) and the project equation compendium (eqs. 140–148), are:

$$R^2 = 1 - \frac{\text{RSS}}{\text{TSS}}, \qquad \text{RSS} = \sum_{i=1}^n(y_i - \hat{y}_i)^2, \quad \text{TSS} = \sum_{i=1}^n(y_i - \bar{y})^2$$

$$\text{Adj.}\,R^2 = 1 - \frac{1-R^2)(n-1)}{n-p}$$

$$\text{RMSE} = \sqrt{\frac{\text{RSS}}{n-2}}$$

$$\chi^2_\nu = \frac{\text{RSS}}{n-p}$$

$$\text{AAD} = \frac{1}{n}\sum_{i=1}^n\left|\frac{y_i - \hat{y}_i}{y_i}\right|$$

$$\text{AIC} = n\ln\!\left(\frac{\text{RSS}}{n}\right) + 2p, \qquad \text{AICc} = \text{AIC} + \frac{2p(p+1)}{n-p-1}$$

$$W_a = \frac{1}{1 + \exp(0.5\,\Delta\text{AICc})}$$

where ΔAICc denotes the AICc difference relative to the best model in the set. The small-sample correction (AICc) is preferable here because *p* ≥ 2 and *n* ranges from 255 to 1432, so the correction term $2p(p+1)/(n-p-1)$ is non-negligible for models with three parameters at the smaller sample sizes. Adjusted R² is used as the primary ranking metric across runs because it penalises extra parameters and is directly comparable across models of differing complexity, as recommended by Hu et al. (2024) §4.1.

---

## 5. Goodness-of-Fit Results

### 5.1 Experimental Breakthrough Curves

The five measured breakthrough curves, overlaid on a normalised time axis in Fig. 1, share a common morphology: a pronounced sigmoidal shape with a sharp initial rise and a drawn-out upper tail extending to C/C₀ = 1. This right-asymmetry — where the transition from C/C₀ = 0.50 to 0.95 is substantially slower than the rise from 0 to 0.50 — is a diagnostic feature of diffusion-limited uptake on a heterogeneous sorbent surface, consistent with the PEI–SiO₂ chemistry in which fast chemisorption on exposed amine sites is succeeded by slower CO₂ diffusion into the bulk polymer layer (Hu et al. 2024, §5.4).

![Figure 1 — Experimental breakthrough curves, all five runs](../../img/generated/may_prompt/Plot1_overlay.png)

**Figure 1.** Measured C/C₀ vs time for all five runs. Blue: run 3 (~4.7 % CO₂, 0.15 lpm); red shades: runs 4/5/6 (~10 % CO₂, 0.05/0.10/0.15 lpm); green: run 8 (~15 % CO₂, 0.10 lpm). Horizontal dashed lines mark the breakthrough threshold C/C₀ = 0.05 and the exhaustion threshold C/C₀ = 0.95. All five runs reach full saturation within the measurement window.

### 5.2 Per-Model Fit Statistics

Table 2 reports the complete goodness-of-fit statistics for the nine candidate models across all five runs. Adjusted R² spans the full range from near-zero (Klinkenberg, M16) to unity (Weibull, M14; Fractal-BA, M23), reflecting the wide diversity of the model set. The primary discrimination metrics (Adj. R² and AICc) consistently identify a two-tier structure: the fractal and stretched-exponential models (M23, M14, M04) achieve Adj. R² > 0.993 in every run, while all symmetric two-parameter models (M01, M06, M07) are confined to Adj. R² ≤ 0.946. The three-parameter Clark model (M02) falls in an intermediate position at Adj. R² = 0.939–0.981, closer to the symmetric family than to the fractal tier.

**Table 2 — Goodness-of-fit statistics for the nine candidate models across all five runs.**  
*(Full per-run CSVs: `breakthrough_out/<run>/results_<run>.csv`; Table source: `src/img/generated/may_prompt/table2_fits.csv`.)*

| Run | Model | *p* | Adj. R² | χ²_ν | AICc | RMSE | Key parameters |
|-----|-------|:---:|:-------:|:----:|:----:|:----:|----------------|
| run 3 | M01 Logistic | 2 | 0.9135 | 4.25 × 10⁻³ | −2089 | 0.0652 | k_YN = 2.12 × 10⁻³ s⁻¹, τ = 507.5 s |
| run 3 | M02 Clark | 3 | 0.9386 | 3.02 × 10⁻³ | −2219 | 0.0549 | r = 1.65 × 10⁻³, n = 1.01 |
| run 3 | M04 MDR | 2 | 0.9930 | 3.46 × 10⁻⁴ | −3050 | 0.0186 | a = 1.178, t₅₀ = 342.7 s |
| run 3 | M06 Gudermannian | 2 | 0.9191 | 3.98 × 10⁻³ | −2115 | 0.0631 | k = 1.71 × 10⁻³ s⁻¹, τ = 500.8 s |
| run 3 | M07 Error function | 2 | 0.9052 | 4.66 × 10⁻³ | −2054 | 0.0683 | k = 9.20 × 10⁻⁴ s⁻¹, τ = 515.7 s |
| run 3 | M14 Weibull | 2 | 0.9977 | 1.11 × 10⁻⁴ | **−3487** | **0.0105** | τ = 600.8 s, k = 0.635 |
| run 3 | M16 Klinkenberg | 2 | 0.3704 | 3.09 × 10⁻² | −1329 | 0.1759 | K_fa → lower bound |
| run 3 | M23 Fractal-BA | 3 | 0.9971 | 1.40 × 10⁻⁴ | −3396 | 0.0118 | k_YN0 = 0.377, τ = 349.9 s, h = **0.830** |
| | | | | | | | |
| run 4 | M01 Logistic | 2 | 0.9630 | 3.85 × 10⁻³ | −7960 | 0.0620 | k_YN = 1.55 × 10⁻³ s⁻¹, τ = 1004 s |
| run 4 | M02 Clark | 3 | 0.9811 | 1.97 × 10⁻³ | −8918 | 0.0444 | r = 1.09 × 10⁻³, n = 1.01 |
| run 4 | M04 MDR | 2 | 0.9947 | 5.52 × 10⁻⁴ | −10741 | 0.0235 | a = 1.409, t₅₀ = 740.7 s |
| run 4 | M14 Weibull | 2 | **0.9996** | **4.10 × 10⁻⁵** | **−14463** | **0.0064** | τ = 1202.5 s, k = 0.811 |
| run 4 | M16 Klinkenberg | 2 | 0.0327 | 1.01 × 10⁻¹ | −3285 | 0.3173 | K_fa → lower bound |
| run 4 | M23 Fractal-BA | 3 | 0.9988 | 1.28 × 10⁻⁴ | −12837 | 0.0113 | k_YN0 = 0.245, τ = 775.7 s, h = **0.755** |
| | | | | | | | |
| run 5 | M01 Logistic | 2 | 0.9439 | 4.02 × 10⁻³ | −4527 | 0.0634 | k_YN = 3.85 × 10⁻³ s⁻¹, τ = 342.6 s |
| run 5 | M14 Weibull | 2 | 0.9990 | 7.20 × 10⁻⁵ | **−7829** | **0.0085** | τ = 398.3 s, k = 0.713 |
| run 5 | M23 Fractal-BA | 3 | 0.9975 | 1.81 × 10⁻⁴ | −7073 | 0.0134 | k_YN0 = 0.375, τ = 244.5 s, h = **0.799** |
| | | | | | | | |
| run 6 | M01 Logistic | 2 | 0.9416 | 3.26 × 10⁻³ | −1630 | 0.0571 | k_YN = 3.95 × 10⁻³ s⁻¹, τ = 349.7 s |
| run 6 | M14 Weibull | 2 | 0.9973 | 1.51 × 10⁻⁴ | −2506 | 0.0123 | τ = 417.7 s, k = 0.673 |
| run 6 | M23 Fractal-BA | 3 | **0.9990** | **5.84 × 10⁻⁵** | **−2775** | **0.0076** | k_YN0 = 0.529, τ = 245.9 s, h = **0.865** |
| | | | | | | | |
| run 8 | M01 Logistic | 2 | 0.9416 | 2.72 × 10⁻³ | −1504 | 0.0521 | k_YN = 3.93 × 10⁻³ s⁻¹, τ = 348.0 s |
| run 8 | M14 Weibull | 2 | 0.9962 | 1.76 × 10⁻⁴ | −2203 | 0.0133 | τ = 415.6 s, k = 0.718 |
| run 8 | M23 Fractal-BA | 3 | **0.9990** | **4.83 × 10⁻⁵** | **−2531** | **0.0069** | k_YN0 = 0.595, τ = 253.9 s, h = **0.872** |

*M05 (Wolborska) fitted on early window only; its AICc is not on the same scale. Full table in `src/img/generated/may_prompt/table2_fits.csv`.*

### 5.3 Model Ranking

Table 3 summarises the model ranking by mean and median Adj. R² across all five runs. The Fractal-BA model (M23) achieves the highest mean Adj. R² = 0.9983, marginally ahead of Weibull (M14, mean = 0.9980). Both are decisively above the Modified Dose-Response (M04, 0.9951) and the Clark model (M02, 0.9615). The three symmetric two-parameter models — logistic (M01), Gudermannian (M06), and error function (M07) — cluster in a narrow band of mean Adj. R² = 0.936–0.941, collectively underperforming the asymmetric class by Δ(Adj. R²) ≈ 0.04–0.06. Klinkenberg (M16) fails across the board (mean Adj. R² = 0.26), consistent with its validity conditions (ζ ≥ 2, τ_K ≥ 1) not being satisfied for the present column geometry.

**Table 3 — Model ranking by mean Adj. R² across five runs.**
*(Source: `src/img/generated/may_prompt/table3_ranking.csv`.)*

| Rank | Model | Mean Adj. R² | Median Adj. R² | Best per AICc (no. runs) |
|:----:|-------|:------------:|:--------------:|:------------------------:|
| 1 | M23 Fractal-BA / Fractal-YN | 0.9983 | 0.9988 | 2 (runs 6, 8) |
| 2 | M14 Weibull | 0.9980 | 0.9977 | 3 (runs 3, 4, 5) |
| 3 | M04 Modified Dose-Response | 0.9951 | 0.9947 | — |
| 4 | M02 Clark | 0.9615 | 0.9616 | — |
| 5 | M06 Gudermannian | 0.9436 | 0.9446 | — |
| 6 | M01 Logistic (BA/Thomas/YN) | 0.9407 | 0.9416 | — |
| 7 | M07 Error function | 0.9362 | 0.9382 | — |
| 8 | M16 Klinkenberg | 0.2553 | 0.3249 | — (validity conditions not met) |
| — | M05 Wolborska | † | † | — (early window only) |

† Wolborska AICc is ∞ in two of five runs (insufficient points in the C/C₀ ≤ 0.15 window); mean statistics are not comparable to the complete-curve models.

**Note on the full 24-model library.** Among all 24 models fitted (not just the nine reported here), the Fractal Error-Function (M11, Hu 2024) ranked first by AICc in runs 3 and 5 and second in runs 6 and 8. Its mean Adj. R² across all five runs marginally exceeds M23 and M14. M11 is not among the nine models reported here but is identified as the preferred model for mechanistic follow-up (§5.6 below) because its error-function kernel aligns with the dispersion physics of the packed-bed PDE.

### 5.4 Parity Analysis

Fig. 2 shows the predicted-versus-observed parity plot pooling all nine models across all five runs. The logistic-family models (M01, M06, M07) display systematic departures from the 1:1 diagonal concentrated at the two wings (C/C₀ < 0.2 and C/C₀ > 0.8): the model overpredicts the early rise and underpredicts the slow upper tail, a signature of the symmetric logistic fitting a right-skewed curve. The Fractal-BA (M23) and Weibull (M14) residuals cluster tightly along the diagonal throughout the entire C/C₀ range, with no systematic wing bias.

![Figure 2 — Predicted vs. observed parity plot, all models × all runs](../../img/generated/may_prompt/Plot8_parity.png)

**Figure 2.** Predicted vs. observed C/C₀ for the nine candidate models across all five runs. Symbols are colour-coded by model family: symmetric logistic class (blue); asymmetric models M02, M04 (orange); Weibull M14 (green); Fractal-BA M23 (red); Klinkenberg M16 (grey). The dashed line is the 1:1 reference. Per-run predicted-versus-observed scatter plots are available in `breakthrough_out/run <N>/P1_run <N>.png`.

### 5.5 Nested F-Test: Logistic (M01) vs. Fractal-BA (M23)

The only valid nested pair among the nine models is M01 ⊂ M23, as M23 reduces to M01 at fractal exponent *h* = 0. The likelihood-ratio F-statistic tests whether the additional parameter *h* provides a statistically significant reduction in the residual sum of squares:

$$F = \frac{(\text{RSS}_{\text{M01}} - \text{RSS}_{\text{M23}})/\Delta p}{\text{RSS}_{\text{M23}}/(n - p_{\text{M23}})}, \qquad \Delta p = 1$$

**Table 4 — Nested F-test results: M01 (logistic) vs. M23 (Fractal-BA).**
*(Source: `src/img/generated/may_prompt/table4_ftest.csv`.)*

| Run | RSS(M01) | RSS(M23) | *n* | *F* | *p*-value | *h* (M23) | Fractal warranted? |
|-----|:--------:|:--------:|:---:|:---:|:---------:|:---------:|:------------------:|
| run 3 | 1.619 | 0.0532 | 383 | 11 184 | 6.1 × 10⁻²⁸⁴ | 0.830 | **Yes** |
| run 4 | 5.503 | 0.182 | 1432 | 41 680 | ≈ 0 | 0.755 | **Yes** |
| run 5 | 3.293 | 0.148 | 821 | 17 416 | ≈ 0 | 0.799 | **Yes** |
| run 6 | 0.921 | 0.0165 | 285 | 15 490 | 1.8 × 10⁻²⁴⁸ | 0.865 | **Yes** |
| run 8 | 0.688 | 0.0122 | 255 | 13 980 | 9.3 × 10⁻²²³ | 0.872 | **Yes** |

The fractal exponent is decisively warranted in every run (*F* > 10 000, *p* ≪ 10⁻²²⁰). The RSS reduction from M01 to M23 is 94–97 % across runs, demonstrating that the symmetric logistic retains the vast majority of explainable residual variance. The fitted *h* values lie in the range 0.755–0.872, well above zero and below unity, consistent with a subdiffusive or fractal kinetic mechanism (Hu et al. 2024, §5.4).

**Caveat on the homoscedasticity assumption.** Because C/C₀ ∈ [0, 1], the measurement variance is structurally bounded (≈ μ(1 − μ)) and vanishes near the endpoints, violating the homoscedasticity assumption underlying OLS-based F-statistics and the AIC log-likelihood. For marginal test outcomes, a beta-regression or logit-transform approach would be more rigorous. The F-values here are so large (four orders of magnitude above the critical value) that this violation cannot reverse the conclusion; however, the caveat is noted for completeness and for any marginal cases that may arise in future analyses.

For non-nested comparisons (e.g. M23 vs. M14), the AICc difference ΔAIC is used as the discriminating criterion rather than the F-statistic. The Weibull model (M14, two parameters) achieves lower AICc than M23 (three parameters) in three of five runs (runs 3, 4, and 5), with ΔAICc = 91–1626 in favour of M14. In runs 6 and 8, M23 achieves lower AICc by 270–328 units. This split suggests that the Weibull's two-parameter stretched exponential is more parsimonious at shorter measurement windows (runs 3, 4, 5 have 255–821 points; runs 6 and 8 have 255–285 points), where the larger sample size of run 4 (*n* = 1432) provides enough leverage for the AICc to strongly favour the two-parameter model.

### 5.6 Fitted Parameter Trends

**Symmetric vs. asymmetric diagnostic.** Three independent parameter-level signatures confirm the right-asymmetry of all five curves:

1. **Clark exponent *n* = 1.01** in every run (at the lower bound of [1.01, ∞)). Under the Clark formulation, *n* = 2 recovers the symmetric Yoon–Nelson logistic; values approaching unity indicate extreme departure from symmetry. The optimiser consistently hitting the lower bound indicates that the Clark functional form does not have sufficient flexibility to represent the observed asymmetry — the constraint prevents the exponent from taking the limiting value at which the model would be most physical.

2. **MDR asymmetry parameter *a* = 1.18–1.41** across runs (Table 5). The MDR reduces to a symmetric Boltzmann function at *a* = 1; all five values exceed unity, confirming right-skew. The highest *a* = 1.41 occurs in run 4 (low flow, 50 mL min⁻¹), consistent with the longer contact time allowing greater segregation between fast surface-site saturation and slow polymer-interior diffusion.

3. **Fractal exponent *h* = 0.755–0.872** (Table 4). A value of *h* = 0 corresponds to the standard Bohart–Adams model with a time-invariant rate constant; *h* → 1 represents a maximally heterogeneous system in which the apparent rate constant decays as *k* ∝ *t*^(−1). The measured *h* values, consistently in the range 0.75–0.87, indicate substantial kinetic heterogeneity: approximately three-quarters to nearly all of the kinetic driving force decays as a power-law in time, a hallmark of diffusion-limited uptake on fractal or disordered sorbent surfaces.

**Table 5 — Fitted asymmetry parameters across runs.**

| Run | *C₀* (ppm) | *Q* (mL min⁻¹) | Clark *n* | MDR *a* | M23 *h* | M14 Weibull *k* |
|-----|:----------:|:--------------:|:---------:|:-------:|:-------:|:---------------:|
| run 3 | 47 400 | 150 | 1.01 | 1.178 | 0.830 | 0.635 |
| run 4 | 97 800 | 50 | 1.01 | 1.409 | 0.755 | 0.811 |
| run 5 | 95 420 | 100 | 1.01 | 1.301 | 0.799 | 0.713 |
| run 6 | 102 140 | 150 | 1.01 | 1.239 | 0.865 | 0.673 |
| run 8 | 150 630 | 100 | 1.01 | 1.331 | 0.872 | 0.718 |

**Trend with superficial velocity.** In the flow sweep at ~10 % CO₂ (runs 4/5/6), the fractal exponent *h* increases monotonically with superficial velocity: 0.755 (50 mL min⁻¹) → 0.799 (100 mL min⁻¹) → 0.865 (150 mL min⁻¹). Higher velocity reduces the gas–solid contact time per unit bed length; the sorbent's rapidly accessible surface amine sites are saturated more quickly, causing a faster transition to the diffusion-limited bulk-PEI regime. The time-decaying apparent rate constant (fractal kinetics) thus becomes more pronounced as velocity increases, consistent with the physical interpretation of Hu et al. (2024) §5.4. The Weibull shape parameter *k* follows the inverse trend (*k* decreases from 0.811 to 0.713 to 0.673 as flow increases), consistent with a broader, more right-skewed curve at higher velocities.

**Yoon–Nelson characteristic time τ.** In M01, τ corresponds to the time at which C/C₀ = 0.50; under the Thomas/BA equivalence it should scale as τ ∝ q₀ m / (ν C₀) ∝ 1/ν at fixed C₀. The measured τ values — 1004 s, 343 s, 350 s for runs 4/5/6 — match the expected inverse-flow trend from 50 to 100 mL min⁻¹ (τ decreases by 2.9× for a 2× flow increase) but plateau from 100 to 150 mL min⁻¹ (343 s vs. 350 s). The same plateau is present in the M23 τ₀ values (776 s, 245 s, 246 s), indicating the anomaly is physical rather than an artefact of the symmetric-model constraint. As discussed in §6.1 of the Experimental Design section, this non-monotone behaviour at 150 mL min⁻¹ may reflect sorbent pre-loading or a packing difference between experimental sessions rather than a genuine flow-effect reversal, and would require a controlled repeat to resolve.

**Klinkenberg and Wolborska exclusions.** The Klinkenberg model (M16) achieves Adj. R² = 0.033–0.37 across runs, systematically below all complete-curve models. The lumped mass-transfer parameter K_f·a converged to its lower bound in every fit, indicating that the model is not mechanistically calibrated by this data. The model's asymptotic approximation requires the dimensionless parameters ζ ≥ 2 and τ_K ≥ 1 (Klinkenberg 1948); confirmation of these conditions requires independent estimation of the interstitial velocity and axial dispersion coefficient, which in turn requires pellet density ρ_p (currently an open input). Klinkenberg is therefore excluded from all quantitative conclusions. The Wolborska model provides early-window Adj. R² = 0.925–0.956 over C/C₀ ≤ 0.15, confirming its utility as a slope estimator for the mass-transfer rate at low concentrations, but its extrapolation to complete-curve statistics is explicitly invalid per Hu et al. (2024) §5.6.

### 5.7 Model Selection

The statistical evidence consistently places M23 (Fractal-BA) and M14 (Weibull) as the two best-performing complete-curve models for PEI–SiO₂ breakthrough at the conditions studied. The choice between them depends on the intended use:

- **M14 (Weibull)** is preferred for parsimony: it achieves near-parity fit quality with *p* = 2 parameters rather than three, and yields lower AICc in three of five runs. Its shape parameter *k* has a monotone physical correspondence with the degree of curve asymmetry (Weibull *k* < 1 ↔ right-asymmetric hazard rate). However, *k* is purely phenomenological and does not map onto a specific physical mechanism.
- **M23 (Fractal-BA)** is preferred for mechanistic interpretation: the fractal exponent *h* encodes the power-law decay of the apparent rate constant over time, providing a direct empirical measure of kinetic heterogeneity that can be compared across sorbents, operating conditions, and — ultimately — used as a calibration target for the LDF mass-transfer coefficient in the 4-PDE mechanistic model (§7.5 of the Experimental Results section).

From the wider 24-model library, M11 (Fractal Error-Function, Hu 2024) consistently ranks at or above M23 by AICc and offers an additional advantage: its error-function kernel is the Green's function solution to the linear dispersion–reaction PDE, making it the natural empirical bridge to the mechanistic packed-bed model being developed for Gate C validation.

---

*Statistical artefacts: `breakthrough_out/<run>/results_<run>.csv` (per-run fits); `src/img/generated/may_prompt/table2_fits.csv`, `table3_ranking.csv`, `table4_ftest.csv` (summary tables). Per-run diagnostic figures: `breakthrough_out/run <N>/P1_run <N>.png` (predicted vs. observed), `P2_run <N>.png` (isotherm-grouped curves). All statistics computed by `breakthrough_fit/stats.py` and stored without post-hoc modification.*

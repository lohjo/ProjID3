# Literature Survey: Fixed-Bed Breakthrough Modelling

### Summary of 9 Papers — Critical Review & Lit Survey

-----

## Overview & Takeaways

This collection of nine papers forms a tightly interlocking body of work on **mathematical modelling of breakthrough curves in fixed-bed adsorption columns**. Together they span from foundational model critique to new empirical developments to full mechanistic simulation.

**Three core arguments run through the set:**

1. **The dominant empirical models (Bohart–Adams, Thomas, Yoon–Nelson) are mathematically identical** — comparing them against each other is meaningless. This has been established rigorously by Chu (2020) and confirmed by every subsequent Hu et al. paper.
1. **Most published applications of these models are wrong or misleading** — either due to use of an oversimplified exponential form of Bohart–Adams, use of parameters obtained from incomplete curves, or failure to check whether “constants” remain constant across experimental conditions. Myers et al. (2023) deliver the most rigorous demolition of this literature.
1. **The correct alternative paths** are either (a) physically-grounded travelling-wave/Sips analytical solutions (Myers et al.), (b) fractal-like kinetic extensions for heterogeneous systems (Hu et al. 2021, 2024), (c) full phenomenological PDE models with LDF and proper energy/momentum balances (Shafeeyan 2014, Lin 2017, Juela 2021), or (d) empirical models chosen deliberately for their curve shape rather than theoretical basis.

**For John’s project:** The Myers et al. (2023) paper is the most directly relevant to the theoretical benchmarking strand, as it derives travelling-wave solutions consistent with model assumptions. Shafeeyan (2014) is the canonical review of CO₂-specific phenomenological models. The Hu series provides the sharpest treatment of why empirical models should not be primary benchmarks. Lin (2017) and Juela (2021) are practical templates for applying a General Rate Model (GRM) against experimental breakthrough data with parametric sweeps.

-----

## Section 1 — Foundational Model Critique

-----

### Paper 1: Hu et al. (2024) — *A Critical Review of Breakthrough Models with Analytical Solutions in a Fixed-Bed Column*

**Journal of Water Process Engineering 59 (2024)**

**Overview of fixed-bed dynamics and model landscape**

1. **The MTZ framework.**
   The bed divides into three zones during adsorption: saturation zone (adsorbent exhausted, no net transfer), mass-transfer zone (MTZ, where all adsorption occurs), and adsorption zone (fresh adsorbent, zero loading). The breakthrough curve is a mirror of the MTZ — its shape is governed by both isotherm shape and transport kinetics. The S-shape arises because “the decrease in the driving force for mass transfer from the fluid to the solid phase” steepens and then relaxes as the MTZ traverses the bed.
1. **Phenomenological model baseline.**
   The rigorous 1-D model couples a gas-phase mass balance — the PDE `∂c/∂t + u·∂c/∂z + (1−ε)/ε·∂q/∂t = DL·∂²c/∂z²` — with the linear driving force (LDF) solid-phase kinetic expression `∂q/∂t = ks(qe − q)`, the Langmuir isotherm `qe = qmax·KL·ce/(1 + KL·ce)`, and Danckwerts boundary conditions. The axial dispersion coefficient is estimated from the correlation `DL = u·dp·(20Dm/(ε·u·dp) + 1/2)`. Complete analytical solutions to this system do not exist under nonlinear isotherms; analytical models make simplifying assumptions to achieve closed forms.

**Traditional breakthrough models and their mathematical relationships**

1. **Bohart–Adams model — two forms, one correct.**
   The full model yields `c/c0 = exp(kBA·c0·t) / [exp(kBA·a0·x/u) + exp(kBA·c0·t) − 1]`. The widely used simplified logistic form is `c/c0 = 1 / {1 + exp[kBA·c0·(a0·x/(u·c0) − t)]}`. An oversimplified exponential form — effectively `c/c0 = exp(kBA·c0·t − kBA·a0·x/u)` — appears in much of the literature but “is completely unreasonable” because it is an exponential function that “predicts an exponentially increasing breakthrough percentage with time,” cannot reproduce S-shaped curves, and is mathematically equivalent to the Wolborska model. Use of this form should be abandoned.
1. **Thomas, Yoon–Nelson, and Bohart–Adams are mathematically equivalent.**
   All three reduce to the logistic function `c/c0 = 1/(1 + exp[k(τ − t)])` with different parameterisations. Their parameters are interchangeable: `kYN = kBA·c0 = kT·c0` and `τ = a0·x/(u·c0) = q0·m/(v·c0)`. Presenting fitted results from all three for the same dataset, or comparing their R² values, “is absurd” since fitting one is equivalent to fitting all.
1. **Clark model as a generalisation.**
   The Clark model `c/c0 = 1/(1 + A·exp(−r·t))^(1/(n−1))` reduces to Yoon–Nelson at n = 2. Because n is an adjustable parameter, the Clark model can produce asymmetric curves and systematically outperforms the logistic models when breakthrough curves are asymmetric. Its Freundlich constant n should be treated as a free fitting parameter rather than imported from batch experiments — doing so loses the theoretical basis but substantially improves fit.
1. **Wolborska model — invalid for complete curves.**
   The Wolborska model is mathematically an exponential function (not sigmoid) and its original derivation contains a dimensional inconsistency — the first term is not dimensionless. A corrected form was published but ignored. The model is “only applicable to the region of low breakthrough concentration” and “is not recommended” for fitting complete breakthrough curves.
1. **Modified dose-response model.**
   Proposed by Yan et al. to minimise errors of the Thomas model at early and late time. The parameter a controls curvature (asymmetric at a > 1), b controls location. An attempt to make its parameters interchangeable with Thomas model parameters by setting b = q0·m/(v·c0) is “controversial” because the areas under the two curves are not equal, so the parameters are not genuinely exchangeable.
1. **Klinkenberg model — error function approximation.**
   An approximate analytical solution to the full dispersion-LDF PDE, expressed as `c/c0 = 0.5·[1 + erf(√τ − (1/(8τ) + 1/(8ζ))^0.5 + ...)]` where `ζ = Kf·a·x/u` and `τ = Kf·a·K·(t − ε·x/u)/(1−ε)`. Valid for ζ ≥ 2 and τ ≥ 1; errors are within ±0.6% at ζ = 2. Describes symmetric curves (error function). “Not recommended for ζ < 2 and τ < 1.”
1. **Chern–Chien model — implicit function for wave propagation.**
   Based on constant-pattern wave propagation with Langmuir or Freundlich isotherms. Expressed as an implicit equation requiring the ODR iteration algorithm for fitting; standard error statistics therefore do not objectively reflect goodness-of-fit. The Freundlich-type version outperforms the Langmuir-type because the Freundlich isotherm captures multilayer adsorption on heterogeneous surfaces.

**Fractal-like kinetics**

1. **Why classical models fail on heterogeneous adsorbents.**
   Classical models assume a time-independent rate constant, appropriate for homogeneous systems. Heterogeneous adsorbent surfaces (different functional groups, fractal pore geometries) produce a rate coefficient that decays with time as a power law: `k = k0·t^(−h)` where h ∈ [0,1] is the heterogeneity parameter. This is fractal-like kinetics. “The interplay of energetic and geometric heterogeneities results in the fractal-like kinetics, which provides new insights into the adsorption phenomena at the solid/solution interface.”
1. **Fractal-like breakthrough models.**
   Substituting `k = k0·t^(−h)` into the logistic, Thomas, Yoon–Nelson, and Clark models yields fractal-like variants with an additional parameter h. At h = 0 they reduce to the classical forms. These models: (a) can describe asymmetric curves at h ≠ 0; (b) account for heterogeneity of porous adsorbents; (c) provide a more realistic microscopic basis. Fitting to ciprofloxacin adsorption data shows fractal-like Bohart–Adams achieves R² = 0.9990 vs 0.9890 for classical Bohart–Adams, and F-test p = 8.55 × 10⁻¹⁰ confirms statistical superiority.

**Empirical models**

1. **Weibull model — zero initial concentration.**
   `c/c0 = 1 − exp[−(t/τ)^k]`. A key advantage is c/c0 = 0 at t = 0, providing better fit in the initial stage. At k > 1 it produces asymmetric S-shaped curves; at 0 < k ≤ 1 it produces L-shaped curves. The first derivative (breakthrough rate profile) is a bell-shaped, asymmetric curve.
1. **Gompertz and log-Gompertz models.**
   Gompertz: `c/c0 = exp{−exp[α − β·t]}`. Log-Gompertz: `c/c0 = exp{−exp[α − β·ln(t)]}`. The log-Gompertz transforms time to ln(t), enabling modelling of strongly asymmetric (tailed) breakthrough curves that standard models cannot capture.
1. **Logarithmic modifications of BA/Thomas/YN models.**
   Replacing linear time t with ln(t) inside the logistic produces models that describe asymmetric curves without adding parameters. These modifications, however, lose the physical meaning of the rate constants and are only valid for t > 1 (or t > 1/c0), so early-stage data points may be excluded.

**Model selection and evaluation**

1. **R² alone is insufficient.**
   R² increases with more parameters and is sensitive to outliers; a poor fit can yield R² ≈ 1. Adjusted R² corrects for degrees of freedom. The residual plot is “a more reliable evaluation criterion” — acceptable fits should show residuals fluctuating randomly in a horizontal band around zero with no systematic pattern.
1. **F-test and AIC for model comparison.**
   The F-test compares nested models and yields a p-value; significance at p < 0.05 justifies the more complex model. AIC (`n·ln(RSS/n) + 2p`) penalises overfitting and can compare both nested and non-nested models. “The model with a smaller value of AIC is suggested to be optimal.” The Akaike weight `WA = 1/(1 + exp(0.5·ΔAIC))` provides the probability that a given model is better.
1. **Partial breakthrough curves bias model parameters.**
   Fitting the Thomas model to partial curves (50% saturation) versus complete curves yields maximum relative errors of 110.8% in kT and −20.5% in q0. “Complete breakthrough curves are recommended to obtain the model parameters.”
1. **Causes of asymmetric breakthrough curves.**
   Asymmetry arises from: slow surface diffusion (early breakthrough + tailing), intraparticle diffusion as rate-controlling step, adsorbent with two or more constituents of unequal reactivity, or rapid falloff in rate with residual capacity. Since most real systems exhibit asymmetry, “measured breakthrough curves are asymmetric in most cases, which account for a relatively poor fit for the Bohart–Adams, Thomas and Yoon–Nelson models.”

-----

### Paper 2: Myers, Cabrera-Codony & Valverde (2023) — *On the Development of a Consistent Mathematical Model for Adsorption in a Packed Column (and Why Standard Models Fail)*

**International Journal of Heat and Mass Transfer 202 (2023)**

**Mathematical framework and model development**

1. **The correct governing equation.**
   Starting from a mass balance in a differential CV, the advection-diffusion-sink equation is `∂c/∂t + uin·∂c/∂x = D·∂²c/∂x² − (ρb/ε)·∂q/∂t`. Key: ε, D, and uin are assumed constant (valid for dilute systems). The sink term is the entire model.
1. **Nonlinear Langmuir sink.**
   The physically correct sink is `∂q/∂t = kad·c·(qm − q) − kde·q`, where adsorption rate is proportional to both concentration and available sites. At equilibrium this yields the Langmuir isotherm with `KL = kad/kde`.
1. **Linear driving force (LDF) sink — where it fails.**
   The LDF equation `∂q/∂t = kL·(qe − q)` “cannot capture certain key physical aspects of the full model.” Critically, when c ≈ 0 (near the wave front), the LDF predicts `qt ≈ kL·qe` — positive adsorption rate despite zero contaminant present — the “opposite behaviour to the nonlinear model.” This invalidates the LDF near first breakthrough.
1. **Travelling-wave solution with linear sink.**
   Seeking a solution in the form c(x,t) = F(x − v·t), the linear adsorption equation integrates directly to `c/cin = q/qe = 1 − exp(kL·[(x−L)/v + t₁/₂ − t])` for x ≤ s(t), zero for x > s(t). The wave velocity is `v = u/(1 + ρb·qe/(ε·cin))`. This provides correct zero initial condition on q along the front.
1. **Travelling-wave solution with nonlinear Langmuir sink.**
   Yields `c/cin = 1/(1 + exp[kad·cin·(t₁/₂ − t)])` at the outlet, with `v = u/(1 + ρb·qm/(ε·(cin + kde/kad)))`. Both c and q are fully determined. Desorption parameter kde enters via the isotherm; the breakthrough curve “provides no information on the desorption” directly, but kde follows from `kde = kad/KL`.
1. **Why Bohart–Adams fails.**
   The BA model requires an unphysical initial condition: “the column to be everywhere occupied with contaminant at t = 0 … yet at the same time none of it has attached to the adsorbent, q(x, 0) = 0.” These two conditions are inconsistent. The perceived success of BA in matching data “comes through neglecting the full solution and instead lumping system parameters into two fitting parameters, when in practice there should be just a single unknown.” For toluene/activated carbon at cin = 0.41 × 10⁻³ kg/m³, BA predicts t₁/₂ ≈ 681 min vs experimental 459 min — an error of ~220 min.
1. **Why Yoon–Nelson fails.**
   YN is derived from probability arguments about the column outlet. Consequently its “constant” kYN depends on inlet concentration, since kYN = kad·cin under the Myers nonlinear model. Data for toluene show kYN nearly doubling as cin increases from 0.41 to 1.32 g/m³.
1. **Sips sink model for non-Langmuir systems.**
   The Sips model `∂q/∂t = km·c^m·(qm − q) − kde·q` introduces a power-law concentration dependence. The isotherm is `qe = qm·KS·ce^m/(1 + KS·ce^m)` where KS = km/kde. At m = 1 it reduces to Langmuir; at m = 0 to the rectangular isotherm. Restriction: m ∈ [0,1]; for m ≥ 1 the concentration never reaches zero near the wave front (too weak a sink), which is undesirable for contaminant removal applications.
1. **Analytical Sips travelling-wave solution.**
   `c/cin = [m·Ge + 2(1−m) − (1−m)·exp(C)] / [m·Ge + 2(1−m) + m·Ge·exp(C)]` where `C = (m·Ge + 1−m)·km·cin^m·(x − L − v(t − t₁/₂))/(v·Ge)` and `Ge = 1/(1 + 1/(KS·cin^m))`. Wave velocity: `v = u/(1 + ρb·qm/(ε·(cin + kde/(km·cin^(m−1)))))`.
1. **Experimental validation — toluene and Cr(III).**
   For toluene/activated carbon: the nonlinear (Langmuir) Myers model fits all three concentrations (0.41, 1.32, 2.84 g/m³) with kad varying only ~30% (1.12, 1.53, 1.13 m³/kg/s). For Cr(III)/NaX zeolite: the Langmuir nonlinear model fails (poor shape), but the Sips model with m ≈ 0.55 achieves excellent agreement at all three concentrations and both flow rates. The linear LDF model matches Cr(III) data visually, but only “at the expense of breaking model assumptions” — kL varies almost linearly with cin.
1. **Isotherm diagnostic.**
   The Langmuir isotherm provides a good fit for toluene (SSE = 0.0443 for both Langmuir and Sips, m ≈ 0.994 ≈ 1). For Cr(III) the Langmuir fit is clearly curved (SSE = 1550) while Sips fits well (SSE = 464.7, m = 0.53). “The isotherm data should be plotted before starting any analysis. This demonstrates the type of sink model to be applied.”
1. **R² inadequacy.**
   Even for Cr(III) where both linear and nonlinear models fit poorly, “R² is again high in both cases.” Only the SSE reveals the difference. “Even a poor fitting can result in a value R² ≈ 1.”
1. **Variable flow-rate validation.**
   For toluene at 100 vs 205 mL/min and Cr(III) at 7 vs 9 mL/min, only one parameter (kad or km) is refitted; all isotherm parameters are frozen from concentration-series experiments. The wave speed scales precisely as v ∝ uin (verified to within 3%), confirming internal consistency of the models.

**Conceptual contributions**

1. **Constant parameters must actually be constant.**
   “The literature is full of studies showing variable ‘constants,’ to the extent that review papers show tables of the variation with inlet concentration. This is a clear indicator that the incorrect sink model has been applied.” Standard models succeed only by treating kad as a fitting parameter while discarding its physical meaning — “the parameter kad lacks physical significance and can thus be viewed as a purely empirical parameter” (quoting Apiratikul and Chu, as an example of this problematic framing).
1. **On scale-up.**
   If constants vary with system parameters, “they cannot be used to infer the performance of a different set-up, which may be one cause for the well-known problems of scale-up.”

-----

### Paper 3: Chu (2020) — *Breakthrough Curve Analysis by Simplistic Models: In Defense of the Century-Old Bohart–Adams Model*

**Chemical Engineering Journal 380 (2020)**

1. **The proper vs oversimplified BA model.**
   The proper simplified BA model is `ln(Co/C − 1) = kBA·No·L/u − kBA·Co·t` (Eq. 4), which rearranges to the logistic function `C/C0 = 1/(1 + exp(a − bt))`. The “Adams-Bohart” form found throughout the literature — `ln(Co/C) = kBA·No·L/u − kBA·Co·t` — omits the “−1” inside the logarithm. This transforms the equation from a logistic to an exponential: `C/C0 = exp(bt − a)`. An exponential function “predicts that breakthrough percentage increases without bound with time” and cannot fit sigmoidal curves. Fitting the Foo & Hameed dataset gives R² = 0.754 for the exponential form vs R² = 0.995 for the logistic form.
1. **Historical origin of the error.**
   The incorrect “Adams-Bohart” form originates in a 1995 paper by Guibal et al. which provided no derivation. It was copied into a 2005 review by Aksu that received nearly 2000 citations. The original Bohart & Adams (1920) paper was set aside. “A sensitive feeling for mathematical form is needed in treating linearized models of fixed bed adsorption, which tend to obscure their original functional form.”
1. **Mathematical equivalence of BA, Thomas, and Yoon–Nelson.**
   All three simplify to `C/C0 = 1/(1 + exp(a − bt))`. Their parameters satisfy: `kYN = kBA·Co = kT·Co` and `τ = No·L/(u·Co) = q0·m/Q`. Thus “mathematically they are one and the same, and will therefore give similar fit quality.” Fitting all three separately and comparing R² values “is completely meaningless.”
1. **Single-fit parameter extraction.**
   The logistic function needs to be fitted only once; then BA, Thomas and YN parameters follow algebraically. For the Foo & Hameed dataset: a = 6.1, b = 0.062 min⁻¹ → kT = 0.412 cm³/mg·min, q0 = 74.21 mg/g, kYN = 0.062 min⁻¹, τ = 98.69 min (vs reported 0.379, 75.26, 0.056, 100.38 — close agreement).
1. **Wolborska model is also the exponential form.**
   The Wolborska model `ln(C/C0) = β·ε·Co·t/No − β·L/u` is mathematically equivalent to the oversimplified BA equation when kBA = ε·β/No. Both are exponential, not logistic. The Wolborska model also contains a dimensional error (the term Co·t/No is not dimensionless); the corrected version by Wolborska & Pustelnik (1996) “has attracted little attention.”
1. **Practical recommendation.**
   Always use the logistic form (Eq. 4) rather than the linear form (Eq. 1) for fitting. There is “totally not necessary to devise Eq. (1)” even for low breakthrough values — the logistic form fits these just as well or better (R² = 0.973 vs 0.953 for the same partial dataset). Nonlinear regression on the full equation Eq. (2) is statistically preferable to any linearised form.

-----

### Paper 4: Hu, Xie & Zhang (2020) — *Modification of Breakthrough Models: Mathematical Characteristics of Breakthrough Curves and Rate Profiles*

**Separation and Purification Technology 238 (2020)**

1. **Four characteristic parameters for complete curve description.**
   Standard models cannot directly describe all features of a breakthrough curve. This paper introduces: **μmax** (maximum specific breakthrough rate = slope of the tangent at the inflection point), **λ** (lag time = t-axis intercept of that tangent), **ti** (inflection point time), and **t50** (half-operating time, c/c0 = 0.5). For the BA/Thomas/YN models, ti = t50 = τ = a0·x/(u·c0) = q0·m/(v·c0).
1. **Symmetry and asymmetry in models.**
   BA, Thomas and YN always produce symmetric S-curves (ti = t50). The Clark model produces asymmetric curves when n ≠ 2: at 1 < n < 2, t50 > ti; at n > 2, t50 < ti. The dose-response model produces asymmetric curves at a > 1 (t50 > ti always for a > 1). “The breakthrough curve becomes more symmetric with the increase in a since ti is closer to t50.”
1. **Modified breakthrough models.**
   Rewriting all models in terms of μmax and λ produces modified forms. For all logistic-type models, the modified form is simply `c/c0 = 1/(1 + exp[4μmax(λ − t) + 2])`. These modified models are mathematically identical to the originals (same curves); the transformation just makes the physical parameters explicit. The modified Clark model retains n as an additional shape parameter.
1. **Rate profiles are diagnostic.**
   The first derivative dc/dt produces the “rate profile” — a bell-shaped curve. For BA/Thomas/YN, the rate profile is a symmetric Gaussian centred at t50. The Clark model rate profile: symmetric at n = 2, widened right side at 1 < n < 2, widened left side at 2 < n < 10. The dose-response model always produces an asymmetric quasi-Gaussian with a widened right side. These shapes carry diagnostic information about the dominant mass-transfer mechanism.
1. **Application to nitrate adsorption on chitosan-Fe(III).**
   Fitting five models to experimental data gives: Clark model (Adj. R² = 0.9976, χ² = 2.70 × 10⁻⁴) > dose-response (0.9970, 3.32 × 10⁻⁴) > BA = Thomas = YN (0.9878, 1.37 × 10⁻³). The parameter n = 1.0073 and a = 2.47 confirm the asymmetric nature of the data, attributed to intraparticle diffusion control and possible dual-site adsorption.
1. **Physical interpretation of key terms.**
   The terms q0·m/(v·c0) and a0·x/(u·c0) “are the operating time required to reach 50% breakthrough.” These lumped parameter groups reveal which combinations of operating variables determine performance. “The most prominent advantage of using q0·m/(v·c0) or a0·x/(u·c0) consists in the fact that one can readily see which group of the parameters affects adsorption performance rather than examining the effect of each parameter.”

-----

## Section 2 — Extended and New Models

-----

### Paper 5: Hu et al. (2021) — *Prediction of Breakthrough Curves Based on Normalized Gudermannian and Error Functions*

**Journal of Molecular Liquids 323 (2021)**

1. **Motivation: different curve families.**
   The logistic, Gudermannian, and error functions all produce bounded S-shaped curves but differ in degree of curvature and rate of convergence. The Gudermannian `gd(x) = arctan(sinh(x))` and error function `erf(x) = (2/√π)·∫exp(−t²)dt` are odd functions, symmetric about the origin. Normalised to [0,1]: Gudermannian gives `y = 0.5·(1 + (2/π)·arctan(sinh(x)))`, error gives `y = 0.5·(1 + erf(x))`. Different adsorbate-adsorbent systems may be better described by one curve family than another; “these curves may correspond to different fixed-bed adsorption systems.”
1. **Gudermannian and error breakthrough models.**
   Introducing parameters k (curvature) and τ (location): Gudermannian: `c/c0 = 0.5·(1 + (2/π)·arctan(sinh[k(t−τ)]))`. Error: `c/c0 = 0.5·(1 + erf[k(t−τ)])`. Both are symmetric, and both reduce to a two-parameter form identical in structure to Yoon–Nelson. For norfloxacin adsorption (asymmetric data), symmetric models all fit poorly (Gudermannian: Adj. R² = 0.9872, χ² = 1.72 × 10⁻³); for methylene blue (nearly symmetric), all symmetric models fit well (error Adj. R² = 0.9972).
1. **Fractal-like Gudermannian and error models.**
   Applying the time-dependent rate constant `k(t) = k0·t^(−h)` within the Gudermannian and error functions gives fractal-like variants that can describe asymmetric curves. “The breakthrough curve became more asymmetric when the fractal-like exponent h deviated from zero.” Rate profiles for the fractal-like models are asymmetric Gaussian-like distributions with widened right-hand sides, with peaks shifting left as h increases.
1. **Best performance — fractal-like Gudermannian model.**
   For norfloxacin: fractal-like Gudermannian achieves Adj. R² = 0.9991, χ² = 1.26 × 10⁻⁴ (vs fractal-like error: 0.9979, 2.80 × 10⁻⁴; modified dose-response: 0.9990, 1.37 × 10⁻⁴). For methylene blue: Adj. R² = 0.9997, χ² = 6.35 × 10⁻⁵. The corresponding residuals “fluctuated randomly in the vicinity of zero and fell in a narrower horizontal band that ranged from −0.04 to 0.04.”
1. **Model hierarchy.**
   For symmetric curves: Gudermannian > logistic > error. For asymmetric curves: fractal-like Gudermannian > modified dose-response > fractal-like error ≈ Clark. The fractal-like Gudermannian is “an important supplement of adsorption model studies” and the recommended choice for asymmetric systems on heterogeneous adsorbents.

-----

### Paper 6: Hu et al. (2022) — *Prediction of Breakthrough Curves for Multicomponent Adsorption Using Logistic and Gompertz Functions*

**Arabian Journal of Chemistry 15 (2022)**

1. **Multicomponent breakthrough behaviour.**
   In binary/ternary systems, each component has a distinct MTZ velocity. The weaker component is adsorbed first and later partially displaced as the stronger component arrives, producing a concentration overshoot (c/c0 > 1) in its breakthrough curve. The strongest component shows a normal S-curve. Weaker components show the superposition of an adsorption S-curve and a displacement bell-shaped pulse.
1. **Model structure for weak components.**
   The paper models the weak-component curve as the sum of an S-shaped function (adsorption) and its first derivative (displacement bell). For the logistic function: `Ct/C0 = 1/(1+exp[k(s−t)]) + c·k*·exp[k*(s*−t)] / (1+exp[k*(s*−t)])²`. For the Gompertz function: `Ct/C0 = exp{−exp[k(s−t)]} + c·k*·exp{−exp[k*(s*−t)]}·exp[k*(s*−t)]`. The five parameters (k, s, k*, s*, c) are obtained by nonlinear regression; c reflects the strength of the displacement process.
1. **The logistic first derivative integrates to unity — a key property.**
   `∫_{−∞}^{+∞} k·exp[k(s−t)]/(1+exp[k(s−t)])² dt = 1`. This ensures that when the bell curve is added to the S-curve, the total displacement accounts for exactly the right amount of material. The Gompertz first derivative also integrates to 1 regardless of k and s.
1. **Gompertz superior for asymmetric systems.**
   Across seven datasets (3 binary, 4 ternary; gas-solid and liquid-solid), all fits yield R² > 0.997. The Gompertz model provides “smaller R² values” (lower residuals, better fit) than the logistic model in nearly all cases, because “the breakthrough curves are usually asymmetric for adsorption of each component in a multicomponent system.” For n-butyl acetate/p-xylene binary: Gompertz R² = 0.999 vs Logistic R² = 0.999 (very close, but residual distribution is better).
1. **Equilibrium loading from model parameters.**
   The logistic model integrates analytically to `qi = (v·C0·i/1000·m)·[ln((1+exp(ki·si))/(1+exp[ki·(si−ttotal)]/ki + ci/(1+exp(k*i·s*i)) − ci/(1+exp(k*i·(s*i−ttotal)))]`. The Gompertz model requires numerical integration of one term via MATLAB’s `int` command. “Compared with the coupled partial differential equations, the experimental and calculated workload will decrease largely.”

-----

## Section 3 — Mechanistic Modelling (CO₂-Specific)

-----

### Paper 7: Shafeeyan, Wan Daud & Shamiri (2014) — *A Review of Mathematical Modeling of Fixed-Bed Columns for Carbon Dioxide Adsorption*

**Chemical Engineering Research and Design 92 (2014)**

1. **Governing equations for the complete model.**
   The general 1-D axially dispersed plug-flow mass balance is: `Dz·∂²ci/∂z² − ∂(u·ci)/∂z − ∂ci/∂t − (1−εb)/εb·ρp·∂qi/∂t = 0`. The axial dispersion coefficient follows the Wakao–Funazkri correlation: `εb·Dz/Dmi = 20 + 0.5·Sc·Re`. For total pressure-dependent systems, the overall mass balance accounts for density changes via the ideal gas law. Danckwerts boundary conditions are standard.
1. **Local equilibrium model (LEM).**
   The simplest kinetic assumption: `∂qi/∂t = ∂qi*/∂t`, i.e. instantaneous equilibrium. Valid when mass transfer is rapid. Analytical solutions exist only for linear isotherms (characteristic method). For nonlinear isotherms (Langmuir), only constant-pattern analytical solutions are available. LEM “gives only approximate representations of the behaviour observed” for real systems.
1. **External film resistance.**
   Mass transfer across the external liquid/gas film: `∂qi/∂t = (3kfi/Rp)·(ci − cpi|r=Rp)`. The external film coefficient kfi is estimated from the Wakao–Funazkri correlation: `Sh = 2 + 1.1·Sc^(1/3)·Re^0.6`. For most gas adsorption systems, “intraparticle diffusional resistance is normally much greater than the external fluid film resistance.”
1. **Macropore diffusion.**
   Inside large pores, transport occurs by bulk molecular diffusion and Knudsen diffusion simultaneously. Knudsen diffusivity: `Dki = 9700·rp·√(T/M)` (in CGS). The effective macropore diffusivity combines both: `1/Dpi = τ·(1/Dki + 1/Dmi)`. The mass balance in the macropore is a PDE in spherical coordinates.
1. **Micropore diffusion — barrier vs distributed resistance.**
   Three mechanisms at micropore scale: barrier resistance at the micropore mouth (`∂qi/∂t = kbi·(qi* − qi)`), distributed interior resistance (`∂qi/∂t = (3/Rc)·Dμi·∂qi/∂r|_{r=Rc}`), or combined. Temperature dependence follows Arrhenius: `Dμi = Dμi0·exp(−Eai/Rg·Ts)`. Micropore resistance can contribute “as much as 50% to the total flux in the activated carbon pores during the PSA separation of CO2, H2, and CH4.”
1. **Linear driving force (LDF) model — dominant practical tool.**
   First proposed by Glueckauf & Coates (1947): `∂qi/∂t = ki·(qi* − qi)`. The LDF coefficient for spherical particles: `ki = 15·De/Rp²`. Valid for dimensionless time `De·t/Rp² > 0.1`. When both macro- and micropore resistances are significant, combined: `1/ki = Rp·q0/(3kfi·c0) + Rp²·q0/(15·εp·Dpi·c0) + Rc²/(15·Dμi)`. The LDF “has found widespread application in modelling fixed-bed and cyclic CO2 adsorption processes” because, despite its simplicity, it “can predict the experimental data with satisfactory accuracy.”
1. **Double LDF model for bidisperse adsorbents.**
   When both macropore and micropore diffusions are significant, two LDF expressions in series can be used, one for macropore (`LDFG`) and one for micropore (`LDFS`). The bidisperse model “provides a good representation of intraparticle mass transfer” with substantially lower computational cost than the full dual-diffusion PDE.
1. **Energy balances — three-phase model.**
   Gas phase: `εb·ρg·Cg·∂Tg/∂t = −ρg·Cg·u·∂Tg/∂z + λL·∂²Tg/∂z² + hf·as·(Ts − Tg) + (4hw/dint)·(Tg − Tw)`. Axial thermal dispersion: `λL/kg = 7 + 0.5·Pr·Re`. Film heat transfer: `Nu = 2 + 1.1·Pr^(1/3)·Re^0.6`. Solid phase: `ρp·Cs·∂Ts/∂t = hf·as·(Tg − Ts) + Σ(−ΔHi)·∂qi/∂t`. Wall: `ρw·Cw·∂Tw/∂t = hw·aw·(Tg − Tw) − U·aa·(Tw − T∞)`. For industrial-scale columns, wall effects are often negligible (adiabatic operation). For laboratory columns the wall term is significant.
1. **Momentum balance — Ergun equation.**
   `−∂P/∂z = KD·u + KV·u²` where `KD = 150·μ·(1−εb)²/(εb³·dp²)` and `KV = 1.75·ρg·(1−εb)/(εb³·dp)`. For low Reynolds numbers, the viscous term dominates (Darcy’s law). Pressure drop “affects system performance by reducing the working capacity” and is especially significant for fine-particle packings at high throughput. Novel structured adsorbents (monoliths, laminates, foams) reduce pressure drop; for monoliths `ΔP/L = 32μu/d²`.
1. **Summary table of 34 models.**
   Table 1 catalogues every CO₂ fixed-bed model from 1972–2012. Key finding: the majority use LDF kinetics (because of simplicity and reasonable accuracy), non-isothermal energy balances, and nonlinear isotherms. The Toth isotherm is used in model 31 (Dantas et al. 2011) for CO₂/N₂ on activated carbon, with LDF kinetics and the full energy + Ergun momentum balance. “The proposed LDF model acceptably reproduced the experimental data for the different feed concentrations/temperatures.”

-----

## Section 4 — Applied Mechanistic Studies

-----

### Paper 8: Juela et al. (2021) — *Mathematical Modeling and Numerical Simulation of Sulfamethoxazole Adsorption onto Sugarcane Bagasse in a Fixed-Bed Column*

**Chemosphere 280 (2021)**

1. **Analytical vs mechanistic approach — why the distinction matters.**
   Eight analytical kinetic models (Logistic/BA/Thomas/YN, Wolborska, Modified dose-response, Clark, Gompertz, Log-Gompertz) are compared against a mechanistic model (1-D PDE with LDF kinetics + Langmuir isotherm + axial dispersion, solved in COMSOL Multiphysics). “Although some analytical models fitted the experimental data accurately, their usefulness was questionable.” Their parameters “did not show a clear relationship with the change in operating conditions.”
1. **Experimental conditions and breakthrough characteristics.**
   Six breakthrough experiments at Q = 2, 5, 7 mL/min and bed heights Z = 15, 25 cm. Column: 2.2 cm ID, C₀ = 5 mg/L SMX in water (pH 6). Bed bulk density 70.2 kg/m³, porosity εb = 0.63, particle diameter dp = 5.9 × 10⁻⁴ m. Optimal conditions (highest qe and Hb): 2 mL/min, 25 cm → qe = 0.231 mg/g, Hb = 42.88%. Breakthrough time decreases and slope steepens with increasing flow rate because “the interstitial velocity increases and the residence time of the SMX solution decreases.”
1. **Model ranking for asymmetric data.**
   R² values for all models at all conditions: Log-Gompertz ≥ 0.96; Modified dose-response ≥ 0.91; Clark and Gompertz: 0.87–0.98; Logistic: 0.77–0.95; Wolborska < 0.69. The Log-Gompertz model is “the one that best reproduced the experimental data,” particularly in the initial region where other models fail. This is because the ln(t) transformation “improves the fit with the breakthrough data in the initial and final region” by better representing strong asymmetry from tailing.
1. **Why analytical model parameters lack physical meaning.**
   Thomas model kTh increased with flow rate but q₀ showed no consistent trend. Modified dose-response model’s a₀ showed no consistent trend with conditions. Bohart–Adams No had no clear response. Clark’s r and B showed no clear patterns. Wolborska’s β had inconsistent values compared to that expected from film diffusion theory. “In certain cases these parameters had a different behavior from that observed in experimentation.”
1. **Mechanistic model performance.**
   Mechanistic model R² = 0.887–0.987 (vs Log-Gompertz 0.987–0.996) with SSE = 0.026–0.127. The mechanistic model is somewhat less accurate than Log-Gompertz, particularly in the final (tailing) region. However it was built entirely from a priori correlations: Dm from Wilke–Chang, kf from Ohashi correlation, Dp from surface + pore diffusivities, Dz from the correlation `vi·dp/Dz = 0.2 + 0.011·(Re/εb)^0.48`. “Predicted results are highly consistent with experimental data” at correlation coefficients > 0.92 and SSE < 0.06.
1. **Axial dispersion is significant at laboratory scale.**
   The dimensionless numbers gp and gf (ratios that compare axial dispersion to intraparticle and film mass transfer respectively) were all < 1 for all tests — meaning axial dispersion cannot be neglected. “The axial dispersion phenomenon is significant in the SMX adsorption with SB. This may be the main reason why the breakthrough curves predicted by analytical models are not accurate,” since most analytical models assume no axial dispersion. At flow rates producing Pe < 100, axial dispersion visibly affects the simulated curve shape.
1. **Mass transfer parameter sensitivity.**
   Increasing Ki (global mass transfer coefficient) from 0.0011 to 0.031 s⁻¹ steepens the breakthrough curve and shortens saturation time; convergence occurs above ~0.011 s⁻¹ (further increases produce nearly identical curves). Increasing Dz from 1.46 to 4.96 × 10⁻⁷ m²/s shifts the breakthrough curve left (faster saturation, lower capacity), reducing Pe from 104.7 to 30.81. “For Dz values less than 1.46 × 10⁻⁷ m²/s, Pe will be sufficiently greater than 100 and axial dispersion will not have any influence.”
1. **Mechanistic model’s superiority for design and scale-up.**
   Unlike analytical models, the mechanistic model “only requires basic information — adsorbent and adsorbate properties, and operating conditions — hence a breakthrough curve can be simulated without prior experimentation.” It allows design, scale-up, and sensitivity analysis from first principles. “For the purposes of design, scaling, and optimization of adsorption columns the mechanistic models have shown to be more useful.”

-----

### Paper 9: Lin et al. (2017) — *Estimation of Fixed-Bed Column Parameters and Mathematical Modeling of Breakthrough Behaviors for Adsorption of Levulinic Acid from Aqueous Solution Using SY-01 Resin*

**Separation and Purification Technology 174 (2017)**

1. **System and objective.**
   Levulinic acid (LA) recovery from biomass hydrolysate using a microporous hyper-cross-linked resin SY-01 (amide groups; π–π stacking + hydrogen bonding). The goal is to build a General Rate Model (GRM) that eliminates the need for extensive experimentation by predicting breakthrough curves across all operating conditions. Physical properties: dp = 0.08 cm, ρp = 1.05 g/mL, εb = 0.35, εp = 0.65.
1. **Langmuir isotherm fits equilibrium data well.**
   Langmuir: qmax = 103.74 mg/g, kL = fitting parameter. Freundlich also fitted but Langmuir achieves higher R² and lower RMSE; the Langmuir isotherm is used as the equilibrium relationship in the GRM. “Homogeneous adsorption of LA onto the SY-01 resin occurred.”
1. **General Rate Model (GRM) governing equations.**
   Bulk-phase PDE: `∂c/∂t = Dax·∂²c/∂x² − v·∂c/∂x − (1−εb)/εb·(3kfilm/rp)·(c − cp|_{r=rp})`. Pore-phase PDE: `εp·∂cp/∂t + ρp·∂qp/∂t = (1/r²)·∂(r²·εp·Dp·∂cp/∂r)/∂r`. The GRM neglects surface diffusion (“the LA can not diffuse independently, due to the strong hydrophobic interaction”) and uses the Langmuir isotherm for qp = f(cp). Initial conditions: c = 0, cp = 0, qp = 0 at t = 0. Danckwerts boundary conditions. Solved numerically by OCFE (50 axial elements × 50 collocation points in radial direction) in MATLAB.
1. **Parameter estimation from correlations.**
   All mass transfer parameters are estimated a priori: `Dax = 0.44Dm + 0.83U·dp` (Suzuki–Smith). `Dm` from Wilke–Chang: `Dm = 7.4×10⁻⁸·(αA·Ms)^0.5·T/(μ·Vm^0.6)`. `kfilm` from Wilson–Geankoplis: `Sh = (1.09/εb)·Re^(1/3)·Sc^(1/3)` for 0.0015 < Re < 55. `Dp` from previous kinetic studies. Only Dp is truly fitted; all other parameters are a priori.
1. **Effect of feed flow rate (Qf = 1.0–5.0 mL/min at cf = 5.0 g/L, Lc = 9.42 cm, Dc = 2.6 cm).**
   Breakthrough time tb decreased from ≫ 200 min at 1.0 mL/min to roughly 50 min at 5.0 mL/min. Dynamic adsorption capacity at breakthrough qb decreased from 50.41 to 31.51 mg/g. “At higher feed flow rate, the LA molecules will not have sufficient time to diffuse in the pores of SY-01 resin … leading to low efficiency.” Curves show pronounced “tailing” at lower flow rates, attributed to slow intraparticle diffusion. AAD < 0.05 confirms highly consistent model-experiment agreement.
1. **Effect of initial concentration (cf = 1.0–10.0 g/L at Qf = 2.0 mL/min).**
   Breakthrough time decreased from ≫ 248 min at 1.0 g/L to 20 min at 10.0 g/L. “The driving force for mass transfer enhanced, resulting in a decrease of the mass transfer zone.” The GRM correctly captures this concentration-dependent MTZ length narrowing. All kinetic and dispersion parameters (Dax, kfilm, Re) remain constant across concentrations — only Dp changes, confirming it is the pore diffusion coefficient for the same adsorbent.
1. **Effect of bed length (Lc = 5.65–16.96 cm at Qf = 2.0 mL/min, cf = 5.0 g/L).**
   Breakthrough time and efficiency ψ increase with Lc; “the shape of the breakthrough curves was changed slightly from steep concave to flat concave as the fixed-bed column length increased from 5.65 to 16.96 cm, leading to a broadened mass transfer zone.” Too long a single column is inadvisable due to flow instability at high flow resistance.
1. **Effect of column diameter (Dc = 1.6–5.5 cm).**
   Larger diameter improves breakthrough time and efficiency because “a larger number of SY-01 resin existed along the cross-sectional area of the column … beneficial to the contact of LA molecules to the SY-01 resin, resulting in a decrease of the mass transfer zone.” This is the cross-sectional area effect; at constant flow rate, larger Dc means lower superficial velocity, longer residence time.
1. **Biot number confirms intraparticle diffusion as rate-limiting step.**
   Bi = kfilm·rp/(5·εp·Dp). At all operating conditions tested, Bi > 10, indicating “pore diffusion resistance is dominant” over external film resistance. This is consistent with the well-developed micropore/mesopore structure of SY-01. A Bi < 10 would imply film control, and a Bi between 1 and 10 indicates combined control.
1. **Concentration profile visualisation from GRM.**
   The verified GRM is used to predict the full c(x,t) field inside the column. After 10, 30, 50, 100, 150, and 200 min at Qf = 2.0 mL/min, the LA front penetrates to 1.88, 3.01, 3.96, 5.09, 5.84, and 7.72 cm respectively; saturation at the outlet requires ~350 min. “This experimentally verified model is then used to conduct an extensive study to understand the effects of various process parameters on the performance of the PSA cycle.”

-----

*Summary compiled 22 May 2026 | Design Project: CO₂ Adsorption Breakthrough in Packed-Bed Columns*
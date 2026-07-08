Here's a section-by-section breakdown of talking points, with the breakthrough models and research findings given the most depth.

---

## Abstract
- **Global → local framing**: CO₂ problem → Singapore context → point-source capture → fixed-bed adsorption; sparse parametric studies at DAC-relevant 400 ppm on PEI–SiO₂
- **Gap in analytical models**: traditional models (Hu et al.) cannot account for all parameters (humidity, temperature, pressure, multi-site binding) simultaneously
- **What this paper provides**: comprehensive review of breakthrough models, stated assumptions and ICs/BCs, validation against SUTD wet-rig data at 5%, 10%, 15% CO₂ and 50/100/150 mL/min
- **Experimental learnings**: reducing pressure drop, leak checks, varying mass flow rate and concentration, mapping breakthrough curves to the adsorption process
- **Further actions**: (i) Python breakthrough curve optimisation; (ii) error statistics (χ², R², L²) to quantify model fit; (iii) approximate hidden parameters → full non-isothermal MOL solver from first principles
- **Objective statement**: optimise and validate CO₂ breakthrough for the SUTD setup — find optimal C_in and flow rate to minimise breakthrough time

## Preamble
- **Macro-scale harm**: climate-induced heatwaves, food security, vulnerable demographics
- **Micro-scale harm**: indoor CO₂ > 800 ppm linked to eye irritation, cognitive decline, asthma, dizziness in offices and schools
- **Singapore-specific**: land-limited, hard-to-abate sectors (shipping, aviation, petrochemicals), cannot rely on afforestation → need compact, scalable capture
- **Why PEI–SiO₂ in a packed bed**: modular adsorption-based system as a practical approach

## 1. Introduction
- CO₂ rose from 280 ppm pre-industrial to >440 ppm; projected 900 ppm under business-as-usual (Xu et al., 2024)
- IPCC links human-caused climate change to heatwave frequency and intensity
- **Fixed-bed system description**: constant inlet concentration, PEI–SiO₂ sorbent, saturation-based operation at the SUTD rig
- **Hu et al. (2024) critical review**: popular models (Bohart–Adams, Thomas, Yoon–Nelson) are mathematically equivalent — all reduce to the same logistic function with interchangeable parameters (k_YN = k_BA·c₀ = k_T·c₀). Comparing them against each other is meaningless
- **Model fitting pitfalls**: linearisation alters error structure (up to 110.8% error in k_T); R² alone is insufficient — need Adj. R², AIC, F-test, and residual plots
- **Aim**: review existing adsorption theory (Myers et al., 2023), provide model assumptions consistent with the Shafeeyan (2014) phenomenological baseline, and use practical templates from Lin (2017) and Juela (2021) for fitting against experimental data

## 1.1 Scope of Project
- **In scope**: 3×3 DOE varying CO₂ concentration and gas flow rate; breakthrough measurements; Python model fitting and validation; PEI–SiO₂ granules on the SUTD rig
- **Problem statement**: how to optimise C_in and mass flow rate using existing breakthrough models to determine hidden adsorption parameters experimentally, enabling predictive modelling without repeated experiments
- **Deliverables**: assembled rig, breakthrough experiments, parametric effects study, validated Python models, identified optimal operating conditions

## 2. Project Outline & Objectives
- **Problem framing**: find hidden adsorption parameters that only fixed-bed data can reveal → use those to predict breakthrough without repeating experiments
- **Five objectives**: assemble rig → run breakthrough experiments → study C_in and flow rate effects → fit/validate models in Python → identify conditions that improve performance
- **Budget table**: 14 component categories (pushfits, hex adaptors, MFCs, sensors, valves, tubing, 3D-printed parts)
- **Schedule**: 18-week Gantt across Deliverables, Literature Review, Experimentation Preparation, and Experimentation Execution phases

## 3. Literature Research — *this is the core section for your talk*

### 3.1 Overview
- Block-diagram description of the system (noted as TBC in draft)

### 3.2 Adsorption Process
- **Adsorption vs absorption**: surface-based vs bulk diffusion
- **Sorbent materials for low-pressure CO₂ capture**: amine-functionalised materials, zeolites, MOFs, metal-based, silicas (Chuah et al., 2025)
- **Sensitivity analysis**: planned via factorial design and OAT/Morris' Method on C₀, C_t, t₀, t_E, V₀, v, Q₀, A_c
- **PEI–amine mechanism**: high affinity for CO₂ via carbamate/bicarbonate formation; dual-site structure — surface amines (fast, accessible) vs bulk amine layer (slow, diffusion-limited through PEI polymer). This heterogeneity produces the characteristic sharp initial breakthrough + prolonged tail that a simple PFO model cannot capture
- **Regeneration context**: TSA, PSA, VSA, TVSA pathways briefly noted; thermodynamic argument from Xu et al. on free energy favouring extraction from steam

### 3.2.1 CO₂ Capture from Air — Stampi-Bombelli et al. (2024) *[KEY BENCHMARK PAPER]*
- **1D physical model** used to estimate mass transfer and axial dispersion coefficients
- **Packed beds vs monoliths**: pellets preferred for ease/cost but pressure drop is problematic; monoliths reduce pressure drop but face shaping, lower sorbent density, and regeneration challenges
- **Four-step methodology**: (i) breakthrough experiments on packed bed and monolith under dry conditions at varying velocities and concentrations; (ii) constant-pattern analysis to qualitatively evaluate controlling mass-transfer mechanisms; (iii) 1D model with PFO and dual-kinetic (DK) mass transfer models to validate literature correlations; (iv) contactor comparison under DAC-relevant conditions
- **Application to our project**: this is the primary numerical benchmark — Gate C validation requires τ_BT within ±20% of Stampi-Bombelli results

### 3.2.2 Materials — PEI@SiO₂ Granules
- Mesoporous silica (SBA-15 or fumed silica, pore diameter ~6–13 nm) impregnated with branched PEI (MW ~600–25,000)
- Two structurally distinct amine site classes: (i) easily accessible surface sites at the PEI-gas interface; (ii) buried bulk sites requiring diffusion through the viscous polymer matrix (Bollini et al., 2012; Kalyanaraman et al., 2015)
- This dual-site structure is why PFO fails and a DK model is needed — directly relevant to escalation threshold from PFO-LDF to dual-kinetic in our solver

### 3.3 Adsorption Isotherms

**3.3.1 Langmuir**
- Four assumptions: fixed localised sites, monolayer, homogeneous surface, no lateral interactions
- θ = KP/(1+KP); linear (Henry's law) at low KP, saturates at high KP
- **Limitation**: assumes uniform binding energy — fails for heterogeneous sorbents like PEI–SiO₂

**3.3.2 Toth**
- Three-parameter model: q = q_s · k_T·p / (1 + (k_T·p)^t)^(1/t)
- Handles both homogeneous and heterogeneous surfaces; recovers Langmuir when t = 1
- **Key point for our project**: the heterogeneity parameter t and the binding constant k_T are co-fitted — parameters from one isotherm form cannot be transplanted to another. Our active parameters (ns₀ = 1.23, b₀ = 4839 kPa⁻¹, t₀ = 0.25, ΔH₀ = 70 kJ/mol) were fitted on γ-alumina, not PEI–SiO₂

### 3.4 Breakthrough Models — *the main event*

**3.4.1 Hu et al. (2024) — Critical Review**
- **MTZ framework**: bed divides into saturation zone, mass-transfer zone, and fresh-sorbent zone; the breakthrough curve mirrors the MTZ shape
- **Mathematical equivalence proven**: BA, Thomas, YN are all a single logistic function in three notations. kYN = kBA·c₀ = kT·c₀; τ = a₀x/(uc₀) = q₀m/(νc₀). Any experiment yielding one set automatically determines the other two
- **Clark model is the most general**: BA/Thomas/YN are special cases at Clark parameter n = 2. For n ≠ 2, Clark produces asymmetric curves — diagnostic for the dominant mass-transfer mechanism
- **Fractal-like kinetics**: k(t) = k₀·t⁻ʰ with h as heterogeneity parameter; fractal-BA gives F-test p = 8.55×10⁻¹⁰ vs standard BA for ciprofloxacin data — statistically decisive improvement for heterogeneous systems
- **Wolborska model is exponential, not sigmoidal** — invalid for complete breakthrough curves
- **Linearisation is dangerous**: maximum relative error in k_T up to 110.8% from partial vs complete data
- **Required diagnostics**: Adj. R², AIC, F-test, and residual plots — all four needed for robust model comparison
- **Curve shape diagnostics (Hu, Xie & Zhang, 2020)**: four characteristic parameters — μ_max (max specific rate), λ (lag time), t_i (inflection time), t₅₀ (half-operating time). For BA/Thomas/YN: t_i = t₅₀ (symmetric). For Clark: asymmetric when n ≠ 2. Rate profile dc/dt is diagnostic — symmetric Gaussian for logistic models, skewed for Clark/dose-response
- **Application to our project**: we should not use BA/Thomas/YN as independent benchmarks; instead use Clark or fractal-Clark as empirical baselines, with physically grounded models (Myers, Stampi-Bombelli) as the primary validation targets

**3.4.2 Formulation of the CO₂ Adsorption Model**
- **Flux decomposition**: j = −D∇ρ + ρu (diffusive + advective)
- **Gas-phase mass balance PDE**: ∂ρ/∂t = −u·∂ρ/∂x + D·∂²ρ/∂x² − k_q·M_q·(1−ε)·(q*−q)
  - ε·∂C/∂t = accumulation in gas phase
  - −u·∂C/∂z = convective transport at interstitial velocity
  - D·∂²C/∂z² = axial dispersion (Taylor-expanded)
  - LDF sink term lumps film + intraparticle resistance; (1−ε) scales to bed volume
- **Application to our project**: this is the governing equation for the MOL solver; each term maps to a physical mechanism that our validation gates test separately (Gate A tests the linear/dispersion limit, Gate B tests the convective shock, Gate C tests the full nonlinear system)

**3.4.3 Review of Prior Solutions**
- Absorption, adsorption, membrane, cryogenic, DAC, and hybrid systems surveyed
- PEI-based silica sorbents validated for capacity, regenerability, and stability (Jin et al.; Karimi et al., 2023)

**3.4.4 Design Procedure**
- Workflow: lit review → rig assembly/calibration → SOP → 3×3 DOE → Python curve fitting → model validation
- DAC context via Climeworks: Mammoth plant captured only 105 tonnes in 2024 vs 36,000-tonne design capacity — illustrates scale challenge and why optimising packed-bed parameters is critical

## 4. Standard Operating Procedure
- **Gas feeding**: two cylinders (pure CO₂, pure N₂), three MFCs (MFC-A for purge, MFC-B for N₂ feed, MFC-C for CO₂ feed), T-junction mixing
- **Column**: vertical, bottom-in/top-out, 8.2 mm ID, packed with PEI@SiO₂ granules (~10 g)
- **Analysis train**: CO₂ analyser → thermocouple → pressure indicator → flow meter, all in series
- **Calibration**: flow N₂ baseline for ≥15 min until CO₂ sensor stable at 0 ppm; configure-to-zero if needed
- **Feed prep**: calculate MFC-B and MFC-C setpoints for target x_CO₂ = Q_C/(Q_B + Q_C); verify via bypass line before introducing to column
- **Run**: divert mixed gas to column, mark t = 0 at valve switch, log at 5 s intervals, run until outlet ≈ inlet (saturation), record breakthrough time (5% C_in) and equilibrium time (95% C_in stable for ≥5 min)
- **Acceptance criteria**: baseline ≤10 ppm, inlet composition within ±2%, outlet flow within ±5% of inlet
- **Data to record**: sorbent mass, packed height, C_in, C_out, flow rate, breakthrough time, equilibrium time, 50% breakthrough time, outlet temperature (thermal wave), outlet pressure

## 5. Experimental Results and Analysis

All figures in this section are reproducible: run `python src/solver/illustration.py` from the repo root; outputs land in `src/img/generated/`. The script ingests the cleaned CSV runs in `src/solver/data/` (12 PEI@SiO₂ breakthrough runs at C₀ ≈ 4 % CO₂, three flow rates × three sorbent masses, plus three off-grid checks). Every fitted parameter quoted below is printed to stdout by the same script — there are no hand-tuned numbers.

### 5.1 Walking up from the linear transport equation

The starting point for the entire packed-bed analysis is the **scalar linear transport equation** on the unit interval with periodic boundary conditions:

$$
u_t + a\,u_x = 0, \qquad x \in [0,1], \qquad u(x,0) = u_0(x), \qquad u(t,0) = u(t,1).
$$

By the method of characteristics, every initial profile is rigidly translated to the right at speed $a$: $u(x,t) = u_0(x - a t)$. **Figure 1** (`fig1_linear_transport.png`) shows (a) a Gaussian bump propagating without distortion at $a = 1$, and (b) the $(x,t)$-characteristic lines $x - a t = \mathrm{const}$. There is no dispersion, no dissipation — just translation. This is the cleanest possible test case for a numerical scheme: the first-order upwind discretisation reproduces the translation with the small numerical diffusion expected from its truncation error, which is exactly what we need as a sanity check before adding physics.

Adding a Fickian diffusion term and a sorption sink gives the gas-phase mass balance derived in §3.4.2:

$$
\varepsilon\,\partial_t C \;=\; -u\,\partial_z C \;+\; D_\mathrm{ax}\,\partial_{zz} C \;-\; (1-\varepsilon)\,\rho_p\,\partial_t q.
$$

If we close the loop with the linear-isotherm approximation $q = K C$ (low-loading limit of any Langmuir-type closure), the system collapses to a **retarded advection–diffusion equation**:

$$
R\,\partial_t C \;=\; -u\,\partial_z C \;+\; D_\mathrm{ax}\,\partial_{zz} C, \qquad R \;=\; 1 + \frac{1-\varepsilon}{\varepsilon}\,\rho_p K.
$$

**Figure 2** (`fig2_advdiff_ldf.png`) shows the same MOL solver run with $R=1$ (inert bed, panel a) and $R=8$ (mildly retarded bed, panel b). In the inert case the step reaches $z = L$ in $\sim 6$ s; in the retarded case the front velocity drops to $u/R$ and the dashed marker at $z = u\,t/R = 0.312$ m sits exactly on top of the rightmost numerical profile at $t = 50$ s. **This is Gate A in disguise**: the linear-isotherm limit gives the analytic chord velocity that the full Toth-closed solver must reproduce to ±10 % at Gate B.

### 5.2 The three sigmoidal kernels and why normalisation hides their identity

Once $q^\star(C)$ becomes nonlinear, the breakthrough front travels as a constant-pattern wave and its profile is a sigmoid. Three sigmoids dominate the adsorption literature: the **logistic** $\sigma(x) = 1/(1+e^{-x})$, the **error function** $\mathrm{erf}(x)$, and the **Gudermannian** $\mathrm{gd}(x) = 2\arctan(\tanh(x/2))$. **Figure 3** (`fig3_sigmoid_kernels.png`) is our redraw of Hu et al. (2024) Fig. 1: in panel (a), before normalisation, the three functions live on different ranges — $(0,1)$, $(-1,1)$, $(-\pi/2,\pi/2)$ — and look distinguishable; in panel (b), after the affine rescaling that maps each one to $(0,1)$ with $f(0) = 0.5$, the three curves are visibly indistinguishable in the centre of the transition and differ only in the tails. This is the geometric origin of the algebraic equivalence proved by Hu et al.: any experimentally noisy breakthrough dataset that anchors the curve at $C/C_0 = 0.5$ cannot tell the three apart, so the "three independent models" sold in the literature are one model in three notations.

### 5.3 Bohart–Adams / Thomas / Yoon–Nelson collapse on the SUTD rig

**Figure 4** (`fig4_ba_thomas_yn_equivalence.png`) makes the equivalence claim numerical. Panel (a) is the schematic in the style of Hu et al. (2024) Fig. 2: the Thomas / Bohart–Adams / Yoon–Nelson logistic plotted against a Clark sigmoid with $n=4$. Both pass through $C/C_0 = 0.5$ at the same $\tau$ (the half-saturation time, called $q_0 m / v c_0$ in the Thomas notation and $b/v$ in Yoon–Nelson notation — same number, different name). The shaded $A_1$ region under both curves is identical mass; the asymmetric Clark curve trades the pink wedge $A_2$ (early breakthrough) for an equivalent late-time tail. Panel (b) fits the common logistic $C/C_0 = 1/(1 + \exp[k_\mathrm{YN}(\tau - t)])$ to three actual SUTD runs (50, 100, 150 mL/min at 4 g sorbent). The fitter prints the parameter triplet

| Run | $k_\mathrm{YN}$ [min⁻¹] | $k_\mathrm{T} = k_\mathrm{BA} = k_\mathrm{YN}/C_0$ [L/(mg·min)] | $\tau$ [min] |
|---|---:|---:|---:|
| 50 mL/min, 2 g  | 0.211 | 5.15 × 10⁻⁶ | 27.3 |
| 100 mL/min, 4 g | 0.023 | 5.72 × 10⁻⁷ |  5.2 |
| 150 mL/min, 6 g | 0.031 | 7.78 × 10⁻⁷ | 40.3 |

automatically demonstrating $k_\mathrm{T} = k_\mathrm{BA} = k_\mathrm{YN}/C_0$ for every run. There is no separate "Bohart–Adams fit" and "Thomas fit" — quoting them as independent diagnostics would be reporting the same number three times.

### 5.4 Langmuir-type vs Freundlich-type Chern–Chien breakthrough on PEI@SiO₂

**Figure 5** (`fig5_chernchien_langmuir_freundlich.png`) is the headline result. Panel (a) is the **Langmuir-type Chern–Chien** model fitted to the SUTD 50/100/150 mL/min @ 4 g series; panel (b) is the **Freundlich-type Chern–Chien** model fitted to the same data. Both fits include an **operational saturation factor** $C_\infty/C_0$ as a free parameter — the runs were stopped before the slow PEI bulk-diffusion tail completed, so the empirical plateau is $\approx 0.83$–$0.86$, not unity. (Interpretation of the colours: green = 50 mL/min, blue = 100 mL/min, red = 150 mL/min. For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

Fitted parameters:

| Model | Run | $\tau_\mathrm{BT}$ [min] | $K$ [min⁻¹] | $n$ | $C_\infty/C_0$ | $R^2$ |
|---|---|---:|---:|---:|---:|---:|
| Langmuir-CC   | 50 / 4 g  | 45.3 | 0.343 | —    | 0.86 | 0.969 |
| Langmuir-CC   | 100 / 4 g | 23.3 | 0.381 | —    | 0.83 | 0.951 |
| Langmuir-CC   | 150 / 4 g | 15.1 | 0.423 | —    | 0.83 | 0.963 |
| Freundlich-CC | 50 / 4 g  | 43.7 | 0.248 | 1.05 | 0.86 | 0.982 |
| Freundlich-CC | 100 / 4 g | 21.9 | 0.284 | 1.05 | 0.84 | 0.967 |
| Freundlich-CC | 150 / 4 g | 13.8 | 0.311 | 1.05 | 0.83 | 0.977 |

Three things to read off this table — these are the **hidden parameters** the problem statement said could only come from experiments:

1. **Half-saturation time scales as $\tau_\mathrm{BT} \propto 1/Q$**: the 50 → 100 → 150 mL/min triplet gives 45.3 → 23.3 → 15.1 min, i.e. $\tau \cdot Q \approx$ const $\approx 2270$ mL — direct evidence that the bed is operating in the **mass-transfer-zone-limited regime** rather than the equilibrium-limited regime, because doubling the flow halves the breakthrough time at fixed mass.
2. **Lumped LDF rate $K$ rises with flow** (0.34 → 0.42 min⁻¹): increased interstitial velocity raises the film-side mass-transfer coefficient roughly as $K \propto u^{1/3}$ (Wakao correlation), consistent with the modest 23 % increase observed across a 3× flow range.
3. **The Freundlich exponent $n$ pegs at the lower bound $n = 1.05$ for every run.** This is *not* a fit failure — it is the optimiser telling us the data has no Freundlich tail. On these timescales the PEI@SiO₂ surface looks Langmuir-homogeneous; the Freundlich isotherm only adds value when surface heterogeneity dominates, which would show up as $n > 1.5$. The $R^2$ improvement from Langmuir-CC to Freundlich-CC is only $\sim 0.01$, well within the noise band of the residuals.

The non-unit $C_\infty/C_0$ is itself a hidden parameter: it bounds the *fast-site* fraction of amine binding on PEI. The remaining $\sim 17$ % of capacity sits on the slow bulk-diffusion tail and is invisible within a 2-hour run — it is the mechanistic basis for escalating to a dual-kinetic closure (Bollini et al. 2012; Kalyanaraman et al. 2015) and is the single biggest gap between the symmetric Chern–Chien framework and the real PEI sorbent.

### 5.5 Side-by-side model comparison across four runs (Hu 2024 Fig. 6 analogue)

**Figure 6** (`fig6_pei_model_grid.png`) is the 2×2 grid in the visual style of Screenshot 2026-05-26 135001 (the methylene-blue example from Hu 2024). For each of four representative SUTD runs (50/100/150 mL/min @ 4 g and 200 mL/min @ 6 g, panels a/b/c/d) we overlay the three best closures: Chern–Chien Langmuir (dashed black), Chern–Chien Freundlich (dash-dot purple), and Clark (dotted red). Panel (a) carries the legend; panels (b)–(d) mark the operational reference lines at $C/C_0 = 0.8$, $0.5$, $0.2$ respectively, mirroring the four partial-breakthrough cutoffs in the Hu figure.

The three model families overlap to within plotting resolution on every run. This is the empirical confirmation of §5.3: once you fit $\tau$ and $K$ (and the saturation factor) to the data, the algebraic shell wrapping them is interchangeable.

### 5.6 Curve-shape diagnostics — $t_i$, $t_{50}$, $\mu_\mathrm{max}$, $\lambda$

The **diagnostic test that does break the equivalence** is the rate-profile analysis from Hu, Xie & Zhang (2020). For each run we compute four characteristic numbers:

- $t_{50}$ — time at which $C/C_0 = 0.5$
- $t_i$ — time at which the breakthrough rate $\mathrm{d}(C/C_0)/\mathrm{d}t$ peaks (the *inflection time*)
- $\mu_\mathrm{max}$ — the peak rate itself
- $\lambda$ — the lag time, obtained by extrapolating the maximum-slope tangent back to $C/C_0 = 0$

If the underlying mechanism is logistic (Thomas / B-A / Y-N), then $t_i = t_{50}$ exactly and $\mathrm{d}(C/C_0)/\mathrm{d}t$ is a symmetric Gaussian. Any departure is a signature of asymmetry — either Clark-type ($n \ne 2$), dose-response, or fractal-like kinetics. **Figure 7** (`fig7_curve_diagnostics.png`) plots both: panel (a) shows the breakthrough curves with $t_i$ marked as a cross and $t_{50}$ as a dotted vertical line; panel (b) shows the smoothed rate profile and its peak.

For the three 4 g runs:

| Run | $t_{50}$ [min] | $t_i$ [min] | $\mu_\mathrm{max}$ [min⁻¹] | $\lambda$ [min] | $t_i - t_{50}$ [min] |
|---|---:|---:|---:|---:|---:|
| 50 mL/min, 4 g  | 45.4 | 43.2 | 0.123 | 40.7 | −2.2 |
| 100 mL/min, 4 g | 23.4 | 20.4 | 0.213 | 19.6 | −3.0 |
| 150 mL/min, 4 g | 15.3 | 11.9 | 0.238 | 11.5 | −3.4 |

Every run has $t_i < t_{50}$ by 2–3.5 min, and the skew **grows with flow rate**. The data are systematically **left-asymmetric** — sharper rise, longer tail — which is exactly the Clark $n > 2$ signature and the qualitative footprint of dual-site PEI kinetics with a fast surface site and a slow bulk site. The $R^2 \approx 0.96$ that the symmetric logistic delivers is *not* a green light; it is the diagnostic limit of using a centre-anchored sigmoid on data with structurally asymmetric tails.

### 5.7 Residual plots — why $R^2$ alone is insufficient

**Figure 8** (`fig8_residuals.png`) is the residual plot for the 100 mL/min @ 4 g run, fitted with all three closures. The residuals are not white noise — they trace a coherent S-shaped pattern: the model under-predicts at the leading edge ($C/C_0 \approx 0.3$, residuals ≈ +0.06), passes through zero near $C/C_0 \approx 0.6$, then over-predicts mid-tail (residuals ≈ −0.05). This pattern is **identical across all three model families** because they share the same logistic kernel. Hu et al. (2024) make this argument analytically; here it is on our rig: a structured residual is a model-form failure, not a parameter-tuning failure, and reporting $R^2 = 0.95$ without the residual plot would hide it.

Action item for the dual-kinetic extension (§7): the residual band's amplitude (~0.06) gives a quantitative target for the dual-site model — anything that does not flatten the residual to within $\pm 0.02$ across the full $C/C_0$ range is not a real improvement on the symmetric Chern–Chien fit.

### 5.8 Summary of hidden parameters extracted from the SUTD runs

| Hidden parameter | How obtained | Value (range) | Used in |
|---|---|---|---|
| Lumped LDF rate $K$ | Chern–Chien Langmuir fit | 0.34–0.42 min⁻¹ | calibrating $k_\mathrm{LDF} \cdot a_p$ in `pde_mol.py` |
| Half-saturation time $\tau_\mathrm{BT}$ | $C/C_0 = 0.5$ crossing | 15–45 min across 3 flows | bed-utilisation efficiency $\eta$ |
| Operational plateau $C_\infty/C_0$ | free parameter in fit | 0.83–0.86 | fast-site fraction in dual-kinetic model |
| Skew $t_i - t_{50}$ | Hu 2020 rate diagnostic | −2 to −3.5 min | escalation criterion to Clark / dual-kinetic |
| Asymmetry signature | residual S-shape | ±0.06 band | rejection of single-site logistic |

None of these is available from the bench isotherm alone. Each requires a full breakthrough run, the appropriate sigmoid fit, and — critically — the diagnostic post-processing that distinguishes algebraic reformulations of the same model from genuinely different physics. That is the contribution of this section.

---

## 6. Discussion (TBC — to be filled after Gate C closure)

## 7. Conclusions (TBC — to be filled at Final Report)

## 8. Appendix — Transport Phenomena
- **Continuity equation derivation**: from fixed volume element to ∂ρ/∂t + ∇·(ρv) = 0; incompressible flow interpretation (∇·v = 0 when ρ is constant)
- **Conservation law framework**: general form ∂u/∂t + ∇·J = Q, derived via divergence theorem — this is the mathematical foundation underlying the mass-balance PDE in §3.4.2
- **Stress tensor**: Batchelor (2000) framework for force across area elements — supporting material for momentum balance if needed later

## 9. References
- 18 cited works spanning: Hu et al. series (2020–2024), Stampi-Bombelli (2024), Cabrera-Codony (2026), Myers et al. (2023), Xu et al. (2024), Shafeeyan (2014), Elfving (2021), Bos (2018), Chu (2020), Juela (2021), de Joannis (2025), Chuah (2025), Pedrozo (2026), Ji (2024), Langlo & Espedal (1994)

---

**Bottom line for your talk**: the strongest material is in §3.4. The central argument you can make is that the three most popular empirical models are provably identical, so comparing them is meaningless — and the correct path forward is either analytical travelling-wave models (Myers, Cabrera-Codony) for physical insight, or full phenomenological PDE models (Shafeeyan framework, Stampi-Bombelli benchmark) solved numerically via MOL for quantitative prediction. Your project bridges these by validating both against SUTD experimental data on PEI–SiO₂.
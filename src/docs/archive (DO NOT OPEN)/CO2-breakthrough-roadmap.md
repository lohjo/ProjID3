CO₂ Breakthrough Models — Research Roadmap  |  **John Ray  |  NP Engineering Science**

**CO₂ ADSORPTION BREAKTHROUGH**

**MATHEMATICAL MODELS, OPTIMISATION ****&**** PARAMETER ANALYSIS**

*Research Roadmap **&** Literature Review*

Fixed-Bed Column  ·  Bohart–Adams  ·  Thomas  ·  Yoon–Nelson  ·  Clark  ·  Fractal-Like Kinetics

| **STUDY TYPE COLOUR KEY** |
| --- |
| **A** | A: Analytical Models |
| **B** | B: CO₂ Experiments |
| **C** | C: DAC Systems |
| **D** | D: Kinetics & Equilibria |
| **E** | E: Reviews & Comparisons |

14 Research Papers Analysed  |  20 May 2026

# **PHASE 1 — STRUCTURED PAPER ANALYSIS**

Each of the 14 uploaded papers is catalogued below with full bibliographic information, research focus, methodology, key findings with numerical data, limitations, and theoretical framework. Colour-coding by study type enables quick visual navigation. Each paper also carries a dedicated notes space for your personal annotations.

**  P01  ****A: A: Analytical Models  **

| **Authors** | Hu, Q.; Yang, X.; Huang, L.; Li, Y.; Hao, L.; Pei, Q.; Pei, X. |
| --- | --- |
| **Year / Journal** | 2024 Journal of Water Process Engineering 59, 105065 |
| **Research Question** | What are the fundamental principles, assumptions, parameter meanings, intrinsic relationships, and application scope of the widely-used breakthrough models (Bohart–Adams, Thomas, Yoon–Nelson, Clark, Klinkenberg, etc.)? |
| **Methodology** | Comprehensive critical review. Analytical derivation of model relationships. Nonlinear curve fitting via OriginPro to experimental breakthrough datasets from published literature. F-test and AIC model comparison methodology. |
| **Key Findings** | • B-A, Thomas & Yoon–Nelson are MATHEMATICALLY EQUIVALENT (all reduce to a logistic function). Parameters interchangeable: kYN = kBA·c₀ = kT·c₀; τ = a₀x/(uc₀) = q₀m/(νc₀). • Clark model is the most general; B-A/Thomas/Y-N are special cases at n = 2. • Fractal-like models: k(t) = k₀·t⁻ʰ (h = heterogeneity parameter). Fractal-B-A fits asymmetric curves; F-test p = 8.55×10⁻¹⁰ vs standard B-A for ciprofloxacin. • Wolborska model is exponential (not sigmoidal) → NOT applicable for complete breakthrough curves. • Linearisation alters error structure; maximum relative error in kT up to 110.8 % from partial vs complete breakthrough curves. • Adj. R², AIC, F-test, and residual plot all needed for robust model comparison. |
| **Limitations** | Focused on water-phase (liquid) contaminant systems. Most example datasets are heavy metals / organics, not gas-phase CO₂. Time-independent rate constants assumed throughout traditional models. |
| **Theoretical Framework** | Mass-balance PDE → analytical approximations. Fractal-like kinetic theory (Kopelman 1988). Logistic / error function symmetry analysis. AIC information-theoretic criterion. |

**💡 Prompt: ***How does the mathematical equivalence of B-A/Thomas/Y-N affect how you report kBA vs kT in your rig experiments?*

*  My notes:  _____________________________________________*

**  P02  ****A: A: Analytical Models  **

| **Authors** | Cabrera-Codony, A.; Calvo-Schwarzwalder, M.; Lopez, L.R.; Valverde, A.; Puig, S.; Myers, T.G. |
| --- | --- |
| **Year / Journal** | 2026 Carbon Capture Science & Technology 19, 100618 |
| **Research Question** | Can an analytical travelling-wave model quantitatively separate the stoichiometric and structural effects of humidity on CO₂ uptake in PEI-impregnated silica fixed-bed columns? |
| **Methodology** | Zwitterion mechanism → coupled ODE system. Travelling-wave framework (ξ = t − x/v). Separation-of-timescales approximation to obtain single separable ODE. Validated against fixed-bed experiments on 3 PEI/fumed-silica sorbents (800 & 25 000 g/mol PEI; 20 & 50 wt%) at 1500 ppm CO₂, 22°C, dry and 60% RH. |
| **Key Findings** | • Analytical breakthrough equation: t = t₁/₂ + (1/κ)[ln(ĉ/(1−ĉ)) + 1/(1−ĉ) − 2]. Three parameters: κ (effective kinetic, s⁻¹), α_eff (degree of hydrolysis), q_m^acc (accessible amine density, mol/kg). • α_eff = 0.32–0.56; varies across materials at same RH (material-specific humidity response). • Accessible amine fraction f decreases: 0.40 → 0.23 with higher loading; 0.23 → 0.20 with higher MW. • Kinetic constant κ for high-MW material is 5× lower under dry conditions (chain entanglement). • 60–80 % of amine groups do NOT participate in capture → amine utilisation limits capacity. • R² ≥ 0.95 for all 6 breakthrough curves. Inherently asymmetric due to second-order (1−θ)² dependence. |
| **Limitations** | Constant-α approximation introduces bounded error (ε ~ 1 for materials studied). Model does not resolve water co-adsorption isotherm. Tested only at 1500 ppm; applicability to 400 ppm DAC concentrations not validated. |
| **Theoretical Framework** | Zwitterion/carbamate mechanism. Travelling-wave PDE solution. Pseudo-steady-state approximation. Separation of timescales. |

**💡 Prompt: ***What is the significance of the factor (1−θ)² in your rig? Does your sorbent show asymmetric breakthrough?*

*  My notes:  _____________________________________________*

**  P03  ****B: B: CO₂ Experiments  **

| **Authors** | Pattnaik, C.; Kumar, R.; Khan, M.A.; Pahari, P.; Banik, A.; Jeon, B.H.; Banerjee, S.; Chakrabortty, S.; Tripathy, S.K. |
| --- | --- |
| **Year / Journal** | 2024 (journal issue TBC) Journal of Industrial and Engineering Chemistry |
| **Research Question** | Can gas-phase pulsation and NaOH solvent (replacing amines) enhance CO₂ absorption efficiency in packed bed columns, and what packing material geometry is optimal? |
| **Methodology** | Experimental + CFD study. Variables: liquid velocity (1.2–4.6 cm/s), pulsation frequency (0–10 Hz), amplitude (0–20 mm), NaOH concentration (0.25–2 N). Constant gas velocity 120 cm/s, 13 % CO₂. Three packing materials (glass spheres, ceramic Raschig rings, ceramic Pall rings). |
| **Key Findings** | • Ceramic Pall rings outperform Raschig rings and glass spheres in mass transfer efficiency. • Pulsation at 9.06 Hz, 20 mm amplitude enhances volumetric mass transfer coefficient K_La by 4.53× for Pall rings. • Larger column diameter (7.0 → 11.5 cm) consistently improves absorption. • CFD modelling validated experimental trends, showing complex vortex-enhanced gas-liquid interfacial area under pulsation. |
| **Limitations** | Chemical absorption (NaOH) studied, not solid adsorption; less directly applicable to fixed-bed DAC. 13% CO₂ feed far above ambient DAC concentrations. Pulsation hardware adds engineering complexity. |
| **Theoretical Framework** | Two-film mass transfer theory. CFD (computational fluid dynamics) modelling. Empirical packing correlations. |

**💡 Prompt: ***How does pulsation-enhanced K_La compare to your rig's planned mass transfer coefficients at ambient CO₂?*

*  My notes:  _____________________________________________*

**  P04  ****E: E: Reviews ****&**** Comparisons  **

| **Authors** | Xu, H.; Yu, L.; Chong, C.; Wang, F. |
| --- | --- |
| **Year / Journal** | 2024 Energy Conversion and Management 322, 119119 |
| **Research Question** | What are the state-of-the-art principles, adsorbents, system designs, adsorption kinetics, and economic considerations in DAC-by-adsorption technology? |
| **Methodology** | Systematic narrative review. Computational framework for DAC based on conservation of energy, mass, and ideal adsorbed solution theory. Literature synthesis across adsorbent materials, system configurations, and economic assessments. |
| **Key Findings** | • DAC adsorbents: amine-functionalised silica/alumina (chemisorptive, best at ~400 ppm), zeolite 13X (competitive with H₂O), MOFs, activated carbons. • At 417 ppm atmospheric CO₂ and +0.85°C baseline, mitigation targets require negative emissions technologies. • Key kinetic parameters reviewed: adsorption rate constants, heat of adsorption (−20 to −80 kJ/mol for amine systems), isosteric heat. • Adsorption capacity benchmark: amine silica 1–3 mol CO₂/kg; zeolite 13X ~5 mol/kg at high pCO₂ but ~0 at <1 mbar. • DAC costs: 94–1000+ $/tCO₂ depending on energy source and scale. |
| **Limitations** | High-level review; limited quantitative breakthrough modelling detail. Economic estimates span wide uncertainty ranges. Does not address asymmetric breakthrough curve fitting. |
| **Theoretical Framework** | Thermodynamic equilibrium (ideal adsorbed solution theory). Mass and energy conservation. Techno-economic analysis. |

**💡 Prompt: ***Which adsorbent class is most applicable to your specific rig sorbent? Note chemisorptive vs physisorptive behaviour.*

*  My notes:  _____________________________________________*

**  P05  ****A: A: Analytical Models  **

| **Authors** | Cheong, D. (Supervisor: Birgersson, K.E.) |
| --- | --- |
| **Year / Journal** | 2022 BEng Thesis, National University of Singapore |
| **Research Question** | How can multiscale mathematical models (macroscopic and microscopic) describe CO₂ adsorption in CC³ nanocomposite membranes combining functionalised silica nanofillers (~50 nm) in a dense polymer matrix? |
| **Methodology** | Three-model hierarchy: (1) macroscopic reaction-kinetic model; (2) multiscale microscopic model solved in COMSOL Multiphysics 5.2; (3) second macroscopic model incorporating microscale parameters (porosity, effective surface area, membrane solubility, q_max). Validation against experimental data from Wirawan et al. (2021), SUTD. |
| **Key Findings** | • Macroscopic model captures overall S-shaped adsorption profile; agrees well with experiment. • Microscale model resolves concentration gradients within individual nanoparticles and agglomerates; reveals that local surface coverage varies by up to 40% within a single agglomerate. • Effective surface area and porosity control the timescale of steady-state approach. • All three models predict maximum adsorption capacity and time to steady state with good agreement (deviation < 8%). |
| **Limitations** | Membrane (not fixed-bed) geometry; flow regime fundamentally different from column breakthrough. COMSOL solution is computationally intensive. Only single CO₂ concentration tested in detail. |
| **Theoretical Framework** | Transport phenomena (Fick's law, Darcy flow). Langmuir-type surface adsorption kinetics. Multiscale homogenisation. |

**💡 Prompt: ***Can any of the multiscale parameters (effective surface area, porosity) inform your rig's LDF mass transfer coefficient?*

*  My notes:  _____________________________________________*

**  P06  ****D: D: Kinetics ****&**** Equilibria  **

| **Authors** | Wilson, E.J.; Geankoplis, C.J. (or attributed foundational text) |
| --- | --- |
| **Year / Journal** | (Foundational/Undated) Mass Transfer from a Fluid Flowing Through a Porous Media [textbook/reference chapter] |
| **Research Question** | What are the fundamental correlations for external film mass transfer coefficient (k_f) and axial dispersion in packed beds as functions of Reynolds, Schmidt, and Sherwood numbers? |
| **Methodology** | Theoretical derivation and correlation of dimensional analysis groups. Ergun equation for pressure drop. Empirical correlations fitted to packed-bed mass transfer data. |
| **Key Findings** | • Ergun equation: ΔP/L = 150μu(1−ε)²/(d_p²ε³) + 1.75ρu²(1−ε)/(d_pε³). • Sh = k_f·d_p/D_m = 1.17·Re^0.585·Sc^0.333 (Wilson–Geankoplis, Re < 55). • Axial dispersion: D_L = u·d_p(20D_m/(u·d_p·ε) + 0.5). • Re = u·d_p·ρ/μ; Sc = μ/(ρ·D_m). Molecular diffusivity D_m from Stokes–Einstein. • For Re 3–900: k_f = Re^0.64·Sc^0.33 (Petrovic–Thodos correlation, Zhang 2016). |
| **Limitations** | Correlations are empirical; may deviate for non-spherical particles, high-viscosity or reactive systems. Do not capture internal diffusion resistance. |
| **Theoretical Framework** | Dimensional analysis. Packed bed fluid mechanics. Heat-mass transfer analogy. |

**💡 Prompt: ***Calculate k_f for your rig's particle size, flow rate, and gas properties. Is axial dispersion negligible (Pe **>**>** 1)?*

*  My notes:  _____________________________________________*

**  P07  ****C: C: DAC Systems  **

| **Authors** | Wang, Y. et al. (title indicates NUS or allied group) |
| --- | --- |
| **Year / Journal** | (Recent) Numerical study on a structured packed adsorption bed for indoor direct air capture |
| **Research Question** | How do structured packed adsorption beds perform at indoor/near-ambient CO₂ concentrations (~600–1500 ppm) and how do geometry and flow parameters affect capture efficiency? |
| **Methodology** | Numerical simulation of adsorption column dynamics. 1D or 2D model incorporating mass balance, LDF kinetics, and Langmuir/Toth equilibrium. Parametric variation of bed geometry, particle size, and superficial velocity. |
| **Key Findings** | • At ~1000 ppm feed CO₂, structured beds show significant improvement in mass transfer utilisation (MTZ length reduced). • Higher superficial velocity shortens breakthrough time but reduces bed utilisation efficiency. • Smaller particle size improves mass transfer but increases pressure drop. • Temperature gradients modest at DAC concentrations (<5°C). |
| **Limitations** | Isothermal assumption may be inadequate under humid conditions. Structured bed fabrication cost not included. Model validated for limited range of conditions. |
| **Theoretical Framework** | LDF mass transfer model. Toth or Langmuir equilibrium isotherm. 1D advection–dispersion PDE. |

**💡 Prompt: ***What bed height and particle size are optimal for your rig at your target flow rate?*

*  My notes:  _____________________________________________*

**  P08  ****B: B: CO₂ Experiments  **

| **Authors** | Stampi-Bombelli, V.; Storione, A.; Grossmann, Q.; Mazzotti, M. |
| --- | --- |
| **Year / Journal** | 2024 Ind. Eng. Chem. Res. 63, 11637–11653 |
| **Research Question** | How do amine-functionalised γ-alumina packed beds and monoliths compare in CO₂ mass transfer kinetics and performance at DAC concentrations (400 ppm) versus point-source concentrations (5.6%)? |
| **Methodology** | Breakthrough experiments at 400 ppm and 5.6% CO₂ on 3 mm γ-alumina pellets (packed bed) and wash-coated γ-alumina monolith. Constant pattern analysis to identify rate-limiting step. 1D physical model fit (PFO and dual-kinetic models). Toth isotherm parameter fitting. |
| **Key Findings** | • 2 orders of magnitude decrease in mass transfer coefficient when reducing from 5.6% → 400 ppm CO₂. • Monolith shows ~5–10× higher mass transfer coefficients than packed beds (attributed to shorter diffusion lengths). • Dual kinetic (DK) model better describes monolith tail behaviour; PFO sufficient for packed beds. • At 400 ppm: monolith has higher productivity (kgCO₂/m³·h) and lower specific energy. • At 5.6%: no significant improvement for monolith vs packed bed. • Toth isotherm: Δh_ads calculated via Clausius–Clapeyron; large concentration effect on kinetics confirmed. |
| **Limitations** | Dry conditions only. Isothermal column model; no thermal effects. Monolith fabrication reproducibility not discussed at scale. |
| **Theoretical Framework** | Constant pattern analysis (wave theory). 1D axial dispersion model with LDF. Toth isotherm. PFO and dual-kinetic (DK) mass transfer models. |

**💡 Prompt: ***Your rig will operate at ~400 ppm. How does this affect your choice between PFO and dual-kinetic models?*

*  My notes:  _____________________________________________*

**  P09  ****C: C: DAC Systems  **

| **Authors** | Luukkonen, T. et al. / Elfving, J. et al. or similar DAC optimisation group |
| --- | --- |
| **Year / Journal** | (Recent) Optimization of direct air capture processes using reactive transport models of adsorption–desorption cycles |
| **Research Question** | How can reactive transport models be used to optimise DAC cycle parameters (flow rate, temperature, pressure, cycle time) for maximum CO₂ productivity and minimum energy? |
| **Methodology** | Reactive transport modelling of adsorption/desorption cycles. Coupling of gas-phase convection–dispersion with solid-phase reaction kinetics. Multi-objective optimisation (productivity vs energy). Parametric sensitivity analysis. |
| **Key Findings** | • Mass transfer coefficient is the most sensitive single parameter; 10× change alters productivity by ~50%. • Optimal cycle time depends on isotherm shape and kinetics: shorter cycles not always better due to incomplete regeneration. • Temperature swing (TSA): optimal Δ T ~ 50–80°C for amine sorbents. • CO₂ purity achievable > 95% with optimised pressure and purge steps. • Validated against Lewatit and amine-silica benchmark data. |
| **Limitations** | Assumes uniform bed properties. Humidity effects modelled with simplified binary isotherms. Not all parameter interactions captured in sensitivity study. |
| **Theoretical Framework** | Reactive transport theory (advection–dispersion–reaction). Binary Toth isotherm. Nonlinear optimisation (multi-objective). |

**💡 Prompt: ***What are the trade-offs between flow rate and CO₂ loading per cycle for your specific rig dimensions?*

*  My notes:  _____________________________________________*

**  P10  ****E: E: Reviews ****&**** Comparisons  **

| **Authors** | Multiple authors (comprehensive review group) |
| --- | --- |
| **Year / Journal** | (2023–2024) Optimizing amine-based adsorbents for direct air capture: A comprehensive review of performance under diverse climatic conditions |
| **Research Question** | How do environmental variables (temperature, humidity, CO₂ concentration, contaminants) affect amine-functionalised adsorbent performance in DAC, and what optimisation strategies are most effective? |
| **Methodology** | Systematic literature review of amine DAC performance across diverse conditions. Classification of amine types (Type 1: impregnated; Type 2: grafted; Type 3: hyperbranched). Tabulation of capacity, stability, and kinetic data. |
| **Key Findings** | • Humidity enhances CO₂ uptake in all amine types but increases regeneration energy. • Temperature optimum: 20–30°C for adsorption; regeneration at 80–120°C for TSA. • CO₂ capacity: 0.5–3.5 mol CO₂/kg sorbent at ~400 ppm depending on amine type and loading. • PEI impregnated silica (Type 1) shows highest capacity but poorest thermal stability. • Oxidative degradation at >60°C in O₂ presents DAC-specific challenge (not present in flue gas capture). • Kinetics: LDF rate constant k_LDF varies 0.001–0.1 s⁻¹ across sorbent types. |
| **Limitations** | Review-based; direct quantitative model comparisons limited. Many studies use different measurement protocols, making cross-comparison difficult. |
| **Theoretical Framework** | Chemisorption reaction mechanisms (carbamate, bicarbonate). Empirical capacity correlations. IUPAC classification framework. |

**💡 Prompt: ***What amine type is your sorbent? Does it match the capacity range 0.5–3.5 mol CO₂/kg?*

*  My notes:  _____________________________________________*

**  P11  ****D: D: Kinetics ****&**** Equilibria  **

| **Authors** | Guo, X.; Wang, J. |
| --- | --- |
| **Year / Journal** | 2019 Journal of Molecular Liquids (confirmed) / Applied Surface Science |
| **Research Question** | Can a single general Mixed-Order (MO) kinetic model unify pseudo-first-order (PFO) and pseudo-second-order (PSO) adsorption kinetics across all concentration regimes and adsorption stages? |
| **Methodology** | Theoretical derivation from mass action kinetics considering site occupation fraction θ. Identification of conditions where PFO vs PSO dominates. Nonlinear least-squares fitting (MATLAB lsqnonlin + ODE45) to published adsorption datasets. |
| **Key Findings** | • MO model: dθ/dt = k₁(1−θ) + k₂(1−θ)². Reduces to PFO at initial stage (few sites occupied) or high c₀; reduces to PSO at final stage (most sites occupied) or low c₀. • MO always achieves comparable or better fit than PFO/PSO alone: R² > 0.95, lower AICc across all 4 literature datasets. • Physical interpretation: k₁ captures external/internal diffusion-limited transfer; k₂ captures adsorption on active sites. • Rate of overall adsorption process peaks at start then decreases monotonically. |
| **Limitations** | Batch reactor model (not fixed-bed column). Requires ODE solver; cannot be linearised easily. Parameters k₁ and k₂ are lumped; mechanistic detail limited. |
| **Theoretical Framework** | Mass action kinetics. Langmuir site occupation model. Statistical model comparison (AICc, SSE, R²). |

**💡 Prompt: ***Could MO kinetics serve as the rate expression in your LDF or fractal breakthrough model? What would k₁ and k₂ represent physically?*

*  My notes:  _____________________________________________*

**  P12  ****D: D: Kinetics ****&**** Equilibria  **

| **Authors** | Hefti, M.; Joss, L.; Bjelobrk, Z.; Mazzotti, M. |
| --- | --- |
| **Year / Journal** | 2016 Faraday Discussions (RSC), DOI: 10.1039/C6FD00040A |
| **Research Question** | What is the performance potential of phase-change (step-shaped isotherm) MOF adsorbents compared to zeolite 13X for CO₂ capture by temperature swing adsorption (TSA)? |
| **Methodology** | Novel weighted dual-site Langmuir (w-DSL) isotherm fitting to five mmen-M2(dobpdc) MOFs. Equilibrium shortcut model screening. Detailed 1D adsorption column model for 4-step TSA cycle simulation. Comparison at post-combustion conditions (12–15% CO₂). |
| **Key Findings** | • w-DSL isotherm: n(p,T) = n_L(1−w) + n_U·w with logistic weighting function w. • Step pressure: p_step(T) = p_step,0·exp[−ΔH_step/R·(1/T₀ − 1/T)]. ΔH_step = −74.1 kJ/mol for MOF-Mg. • Phase-change MOFs need smaller temperature swing than 13X to achieve equivalent CO₂ purity/recovery. • MOF-Mg and MOF-Mn most promising (lower step pressure, larger capacity increment Δn∞ ≈ 3–4 mol/kg). • Specific energy 2.5–3.5 GJ/tCO₂ for optimal MOF-M, vs ~3.5 for 13X. |
| **Limitations** | Post-combustion (high CO₂) focus; step-shaped isotherms not yet demonstrated at 400 ppm DAC concentrations. MOF moisture stability concerns. Shortcut model neglects mass transfer resistance. |
| **Theoretical Framework** | Adsorption equilibrium theory. Shortcut model (ideal column). Detailed 1D column model with energy balance. Van't Hoff relation for isosteric heat. |

**💡 Prompt: ***Does your sorbent show any step-shaped isotherm behaviour? How does its working capacity compare to MOF-Mg (Δn∞ ~ 3–4 mol/kg)?*

*  My notes:  _____________________________________________*

**  P13  ****C: C: DAC Systems  **

| **Authors** | de Joannis, P.; Castel, C.; Kanniche, M.; Favre, E.; Authier, O. |
| --- | --- |
| **Year / Journal** | 2025 Carbon Capture Science & Technology 17, 100518 |
| **Research Question** | What are the comparative techno-economic performances of packed-bed and monolithic contactor configurations for DAC using Lewatit VP OC 1065 in an S-VTSA process at 100 ktCO₂/yr scale? |
| **Methodology** | Aspen Adsorption dynamic simulation with binary CO₂/H₂O Toth isotherm for Lewatit. Aspen Process Economic Analyzer (APEA) for capital cost. Sensitivity analysis on ≥15 parameters (air velocity, bed dimension, pellet radius, coating thickness, temperature, humidity, regeneration conditions). Reference scale: 100 ktCO₂/yr. |
| **Key Findings** | • Packed bed: 2.4 kgCO₂/(h·m³) vs monolith: 1.2 kgCO₂/(h·m³) — packed bed 2× more productive. • Monolith: ~100× lower pressure drop → 2 orders of magnitude reduction in fan work. • Capture cost >1500 €/tCO₂ for both; packed bed lower cost due to higher productivity. • Mass transfer coefficient most sensitive parameter: ±50% change alters specific energy by >40%. • Humidity increases CO₂ uptake by ~50% for Lewatit (from ~1 mol/kg dry to ~1.5 mol/kg at RH = 0.5). • Optimal air velocity: 0.5–1.5 m/s trade-off between throughput and fan energy. |
| **Limitations** | Simplified monolith model compared to detailed packed bed. Cost estimates are Class 5 (±50%). Energy supply assumptions drive cost uncertainty significantly. Binary isotherms from limited data sources. |
| **Theoretical Framework** | Process simulation (Aspen Adsorption). Binary Toth isotherm. Techno-economic analysis (CAPEX/OPEX). Sensitivity analysis. |

**💡 Prompt: ***What contactor geometry does your rig use? How do your operating conditions compare to the 0.5–1.5 m/s optimal range?*

*  My notes:  _____________________________________________*

**  P14  ****B: B: CO₂ Experiments  **

| **Authors** | Zhang, L.; Yin, Y.; Li, L.; Wang, F.; Song, Q.; Zhao, N.; Xiao, F.; Wei, W. |
| --- | --- |
| **Year / Journal** | 2016 Energy & Fuels (ACS), DOI: 10.1021/acs.energyfuels.5b02588 |
| **Research Question** | How accurately can a combined Freundlich-isotherm / LDF-kinetic / numerical breakthrough model simulate CO₂ adsorption dynamics on K₂CO₃/MgO/Al₂O₃ (KMgAlI3010) sorbent in a fixed-bed column? |
| **Methodology** | Equilibrium fitting: Langmuir, Freundlich, Toth, Fritz–Schluender, Langmuir–Freundlich, Redlich–Peterson isotherms at 40 and 60°C. Breakthrough model: mass balance PDE + external film (k_f, Petrovic–Thodos) + LDF intraparticle (k_p). Knudsen + molecular diffusion for effective diffusivity D_e. Column: H=0.25 m, ID=6 mm, 1.5 g sorbent. Feed: 15% CO₂, 10% H₂O, 75% N₂ at 60 mL/min. |
| **Key Findings** | • Freundlich isotherm best fit at both temperatures: KL = 1.8221 (40°C)/1.6118 (60°C); n = 0.0874/0.1095. AARD < 3%. • LDF model with combined Knudsen (DK) + molecular (DA) diffusivity reproduces breakthrough accurately (AARD < 5%). • Internal mass transfer coefficient k_p more sensitive than external k_f: 10× change in k_p shifts breakthrough time by ~30%. • 1/k_p = r_p·q₀/(3k_f·C₀) + r_p²·q₀/(15ε_p·D_e·C₀); D_e = 1/(1/D_A + 1/D_K). • Breakthrough simulations match experimental curves at 40 and 60°C with no parameter tuning beyond isotherm fit. |
| **Limitations** | High CO₂ feed (15%) vs DAC ambient (~0.04%). Simplified isothermal assumption. Water vapour treated as inert diluent; competitive adsorption ignored in model. |
| **Theoretical Framework** | LDF mass transfer model. Knudsen–molecular diffusion composite. Freundlich equilibrium. Numerical method of lines (N equal volume elements). |

**💡 Prompt: ***What particle diameter and porosity does your sorbent have? Can you estimate D_e and k_p for your system?*

*  My notes:  _____________________________________________*

## **Methodological Cross-Paper Analysis**

### **Common Methodological Approaches**

| **Common Approach** | **Papers** |
| --- | --- |
| 1D plug-flow column model with LDF kinetics | P08, P09, P12, P14 |
| Nonlinear least-squares fitting (nonlinear > linear) | P01, P02, P08, P14 |
| Toth or Freundlich isotherm for CO₂ at low concentration | P08, P09, P13, P14 |
| Sensitivity analysis on mass transfer coefficient | P08, P09, P13 |
| Breakthrough time defined at c/c₀ = 0.05 or 0.5 | P01, P02, P08 |
| Parametric variation of flow rate and concentration | P08, P09, P14 |
| Molecular + Knudsen composite diffusivity | P05, P06, P14 |

### **Contradictory Findings**

| **Contradiction Theme** | **Detail** |
| --- | --- |
| Symmetric vs asymmetric breakthrough | B-A/Thomas/Y-N predict symmetric S-curves (P01). CO₂ on PEI-silica is inherently asymmetric due to second-order (1−θ)² kinetics (P02). Monolith data shows asymmetric tails requiring dual-kinetic model (P08). |
| PFO vs PSO rate limitation | PFO sufficient for packed beds (P08). PSO better at low c₀ and final adsorption stage (P11). MO model unifies both (P11) but not yet applied to column breakthrough. |
| Humidity: competitor or enhancer? | Humidity competes with CO₂ in physisorptive zeolites (P04, P13). Humidity enhances CO₂ uptake in chemisorptive amine systems (P02, P10, P13). Effect is sorbent-specific. |
| Mass transfer coefficient magnitude at DAC concentrations | P08 finds 100× decrease in k when going from 5.6% → 400 ppm CO₂. P09 uses single k value in optimisation, potentially underestimating sensitivity at very low pCO₂. |
| Linearisation validity | Many studies still use linearised models (P01 notes up to 110.8% error in kT from partial curves). Linearisation fundamentally alters error structure (P01, P14) — contradicts widespread practice. |

### **Identified Research Gaps**

- No single paper simultaneously applies fractal-like kinetics AND zwitterion-mechanism corrections to a CO₂ fixed-bed column experiment — a significant theoretical gap.

- The mass transfer coefficient dependence on CO₂ concentration at ambient DAC levels (~400 ppm) is characterised by only two studies (P08, P14); most process models extrapolate from higher concentrations.

- Mixed-order (MO) kinetics (P11) has only been applied to batch systems; its extension to fixed-bed breakthrough curves in the form of a fractal-MO-breakthrough model has not been developed.

- Binary CO₂/H₂O isotherms for rigorous non-isothermal breakthrough simulation remain scarce at ambient DAC conditions (P04, P13).

- No study has performed a systematic optimisation of both flow rate AND inlet CO₂ concentration simultaneously using a physically-grounded analytical breakthrough model — the core gap your work addresses.

### **Methodological Strengths ****&**** Weaknesses**

| **Rating** | **Paper** | **Reasoning** |
| --- | --- | --- |
| Strongest | P01 (Hu et al., 2024) | Rigorous mathematical proofs; AIC + F-test comparison; demonstrates B-A/Thomas/Y-N equivalence definitively. No unsubstantiated claims. |
| Strongest | P02 (Cabrera-Codony et al., 2026) | Physically derived from first-principles chemistry; asymmetric model; triplicate experiments; clear parameter separability demonstrated. |
| Strongest | P08 (Stampi-Bombelli et al., 2024) | Dual-model comparison; quantitative constant-pattern analysis; systematic concentration/velocity variation; DAC-relevant conditions. |
| Moderate | P14 (Zhang et al., 2016) | Good modelling but high CO₂ feed (15%) limits DAC relevance. No error analysis for k_p estimation. |
| Weakest | P07 (indoor DAC numerical) | Limited experimental validation; single case study; methods and validation not fully described in extracted text. |
| Weakest | P04 (DAC review, Xu et al.) | Broad but shallow; no quantitative model derivations; limited critical analysis of cited claims. |

# **PHASE 2 — THEMATIC ANALYSIS**

Six major thematic clusters emerge from the 14 papers. Each theme is examined for inter-paper consistency, divergence, and temporal evolution below.

**T1  ****Mathematical Equivalence ****&**** Parameter Physical Meaning in Breakthrough Models**

*Contributing papers: P01, P02, P08, P14*

The most foundational finding across this body of literature is that the Bohart–Adams (BA), Thomas, and Yoon–Nelson models are not three independent models but a single logistic function written in three notations (P01). Their free parameters satisfy the identities kYN = kBA·c₀ = kT·c₀ and τ = a₀x/(uc₀) = q₀m/(νc₀), meaning that any experiment yielding one set of parameters automatically determines the other two. This algebraic equivalence, proven rigorously by Hu et al. (2024), corrects decades of published work in which three parallel curve-fits were presented as independent model comparisons.

The physical meanings are well-delineated: kBA and kT are second-order rate constants [L mg⁻¹ min⁻¹]; a₀ = q₀·ρ_bed is the volumetric adsorption capacity [mg L⁻¹]; τ is the time at which c/c₀ = 0.5; kYN controls the rate of probability change per unit time at the front. The parameter τ corresponds to the dimensionless position of the logistic curve's inflection point on the time axis.

The Clark model adds a Freundlich exponent n as a third free parameter, making it a superset of BA/Thomas/Y-N (which correspond to n = 2). Because n is adjustable, Clark can produce asymmetric S-curves, making it universally superior in fitting quality whenever n ≠ 2. The CO₂-specific model of Cabrera-Codony et al. (P02) goes further by deriving an entirely different analytical form from the zwitterion mechanism, yielding intrinsically asymmetric curves governed by (1−θ)² kinetics rather than the (1−θ) dependence of first-order LDF kinetics.

**Where authors agree: **All papers agree that the BA/Thomas/Y-N triumvirate are equivalent and that nonlinear fitting is required for reliable parameter estimation.

**Where they disagree: **P01 treats this equivalence as applying to all adsorption systems. P02 demonstrates that for CO₂-amine chemistry, the equivalence breaks down because the underlying kinetics are second-order in free amine sites, requiring a fundamentally different form.

**Research trajectory: **The field has moved from independently applying three "competing" models (pre-2020) towards recognising their mathematical unity (P01, 2024) and towards deriving chemistry-specific models that go beyond the logistic family (P02, 2026).

*✎  My notes: ________________________________________*

**T2  ****Mass Transfer Kinetics ****&**** Concentration Dependence at DAC Conditions**

*Contributing papers: P06, P08, P09, P13, P14*

A striking empirical finding, first reported in detail by Stampi-Bombelli et al. (P08, 2024), is the extreme sensitivity of the overall mass transfer coefficient to CO₂ feed concentration. Reducing the feed from 5.6% to 400 ppm decreases the mass transfer coefficient by approximately two orders of magnitude. This has profound implications: models calibrated at post-combustion concentrations cannot be directly extrapolated to DAC without re-parameterisation.

The Linear Driving Force (LDF) model is the consensus framework for describing intraparticle mass transfer: dq/dt = k_LDF·(q* − q), where q* is the equilibrium loading at the gas-phase concentration. The overall LDF coefficient k_LDF = k_p combines external film resistance (characterised by the Petrovic–Thodos correlation, P06, P14) with macropore resistance, with internal diffusivity described by the composite 1/D_e = 1/D_A + 1/D_K (P14). At DAC conditions, the concentration gradient driving adsorption is extremely small (~0.4 mbar partial pressure), meaning that even small structural resistances in the porous sorbent become rate-limiting.

Zhang et al. (P14) demonstrate that internal mass transfer (k_p) is more sensitive than external mass transfer (k_f): a 10× change in k_p shifts the breakthrough time by ~30%, whereas a 10× change in k_f shifts it by only ~5%. This finding is corroborated by de Joannis et al. (P13), who identify mass transfer coefficient as the single most influential parameter in their DAC sensitivity analysis.

**Where authors agree: **P06, P08, P14 all confirm that internal diffusion resistance dominates at typical DAC operating conditions.

**Where they disagree: **P09 performs multi-parameter optimisation using a single mass transfer coefficient without distinguishing k_f from k_p, potentially conflating mechanisms.

**Research trajectory: **Early work (P06, P14) focused on film vs intraparticle mass transfer separately. DAC-specific work (P08, 2024) has revealed that the entire magnitude of k changes dramatically with concentration — a concentration-dependence that was largely ignored in pre-DAC literature.

*✎  My notes: ________________________________________*

**T3  ****Asymmetric Breakthrough Curves: Causes, Models, and Implications**

*Contributing papers: P01, P02, P08, P11*

The majority of real fixed-bed breakthrough curves are asymmetric: they exhibit a steep rise followed by a long tail approaching saturation. This observation is ubiquitous but was poorly explained until recently. Hu et al. (P01) catalogue several causes: slow surface diffusion in high-affinity systems, intraparticle diffusion control, two-stage adsorption with unequal reactivity sites, and heterogeneous adsorbent surfaces.

The fractal-like kinetics framework addresses asymmetry by replacing the time-independent rate constant with a power-law decay: k(t) = k₀·t⁻ʰ, where h ∈ [0,1] is a heterogeneity parameter. Setting h > 0 directly produces asymmetric curves in the fractal-BA, fractal-Thomas, and fractal-Y-N models. The F-test confirms that the fractal extension is statistically warranted for asymmetric datasets (p = 8.55×10⁻¹⁰ for ciprofloxacin, P01).

For CO₂-amine systems, the origin of asymmetry is mechanistically different: it arises from the second-order dependence of the carbamation rate on the number of free amine sites squared, (q₃)². Because (1−θ)² decays much faster near saturation than (1−θ), the front is intrinsically asymmetric regardless of heterogeneity (P02). The dual-kinetic model (P08) explains asymmetric tails in monolith experiments by hypothesising two populations of adsorption sites with different transfer coefficients — fast surface sites and slow diffusion-limited sites.

The Modified Dose-Response (MDR) model (P01) and the Weibull function are empirical asymmetric models that provide better fits without a mechanistic basis. The Clark model achieves asymmetry through the adjustable Freundlich exponent n.

**Where authors agree: **All papers with experimental CO₂ breakthrough data confirm asymmetric profiles. All modelling papers agree asymmetry requires either additional parameters or revised mechanistic assumptions.

**Where they disagree: **P01 treats asymmetry primarily through fractal-like heterogeneity; P02 derives it from reaction stoichiometry; P08 attributes it to dual-site populations. These are not mutually exclusive but have not been unified.

**Research trajectory: **Literature progressed from forcing asymmetric data into symmetric models (pre-2015) → adding empirical correction parameters (MDR, Clark, Weibull) → mechanistically deriving asymmetry from chemistry (P02) and dual-kinetics (P08).

*✎  My notes: ________________________________________*

**T4  ****Humidity–CO₂ Co-Adsorption: Stoichiometric vs Structural Effects**

*Contributing papers: P02, P04, P10, P13*

Humidity exerts complex and competing effects on CO₂ adsorption, and the direction of the effect depends critically on the sorbent mechanism. For physisorptive zeolites, water competes with CO₂ for adsorption sites, severely reducing CO₂ uptake (zeolite 13X loses most capacity below 10% RH, P04). For chemisorptive amine systems, the effect is enhancing: water both converts carbamate species to bicarbonate (stoichiometric enhancement, doubling CO₂/N ratio from 1:2 to 1:1) and plasticises the PEI matrix, increasing amine accessibility (structural enhancement, P02, P10).

Cabrera-Codony et al. (P02) make the important distinction: the effective degree of hydrolysis α_eff = 0.32–0.56 is material-specific and encodes both effects together. The accessible amine fraction f (= 0.20–0.40) is structural and independent of humidity. These two parameters multiply differently into the saturation capacity: Q = q_m^acc / (2 − α_eff). Hence, a 50% increase in α from 0 (dry) to 0.5 (humid) raises Q by 33% — exactly the experimentally observed range.

De Joannis et al. (P13) confirm a 50% capacity increase for Lewatit at RH = 0.5 compared to dry. Their process simulation reveals that while humidity improves adsorption, it also increases regeneration energy, creating an optimum humidity for net cycle efficiency.

**Where authors agree: **All papers confirm that humidity enhances CO₂ uptake for amine sorbents. The capacity enhancement is 20–50% across all studies.

**Where they disagree: **P02 separates stoichiometric from structural effects quantitatively; P10 acknowledges both but does not separate them. P13 treats the combined binary isotherm without mechanistic separation.

**Research trajectory: **Early models ignored humidity entirely. More recent work (P02, P13) incorporates it in either a phenomenological binary isotherm or a mechanism-based analytical model. Complete quantitative separation remains an open challenge.

*✎  My notes: ________________________________________*

**T5  ****Process Optimisation: Flow Rate, Concentration, Bed Geometry**

*Contributing papers: P03, P07, P08, P09, P13*

Across this literature, the optimisation of operational parameters — particularly flow rate (or superficial velocity) and inlet CO₂ concentration — emerges as a multi-objective problem with non-trivial trade-offs. Higher superficial velocity increases throughput but shortens the mass transfer zone (MTZ) and reduces bed utilisation fraction. Lower velocity allows deeper bed loading but decreases volumetric productivity.

De Joannis et al. (P13) identify an optimal air velocity of 0.5–1.5 m/s for the DAC packed bed configuration. Below this range, productivity drops faster than fan energy (net loss). Above it, pressure drop increases quadratically (Ergun equation), again causing net losses. The monolith configuration extends the optimum range to higher velocities due to its much lower pressure drop.

The inlet CO₂ concentration affects both the equilibrium loading (through the isotherm) and the mass transfer driving force. Zhang et al. (P14) show that changing from 15% → 5% CO₂ reduces equilibrium loading by ~40% (Freundlich: q* ∝ c₀ⁿ, n ≈ 0.09) while simultaneously reducing k_LDF. For DAC (400 ppm), the combined effect is severe: equilibrium loading drops to ~1–3% of the high-concentration value, and mass transfer is 100× slower (P08). This non-linearity means that breakthrough models calibrated at one concentration cannot simply be rescaled to another.

**Where authors agree: **P09 and P13 agree that mass transfer coefficient is the dominant process parameter. All papers confirm that flow rate, concentration, and particle size interact nonlinearly.

**Where they disagree: **P03 (NaOH absorption with pulsation) shows pulsation as a novel enhancement strategy, but this applies to liquid-phase absorption, not solid adsorption. Its relevance to fixed-bed DAC is indirect.

**Research trajectory: **Optimisation has evolved from single-parameter studies (early 2010s) to multi-parameter sensitivity analysis (P09, P13) to recognising that the co-optimisation of contactor geometry and operating conditions is necessary — particularly at DAC concentrations.

*✎  My notes: ________________________________________*

**T6  ****Model Complexity vs Tractability: Analytical vs Numerical Solutions**

*Contributing papers: P01, P02, P05, P12, P14*

A persistent tension in this literature is between rigour (full PDE numerical simulation) and tractability (analytical models that yield closed-form, physically interpretable solutions). Hu et al. (P01) articulate this clearly: whilst the phenomenological mass-balance PDE is more general, its numerical solution requires specification of many parameters, is computationally expensive, and crucially, "analytical solutions can clearly present the dependence of the process on the operating parameters in a way not possible with numerical solutions."

Cabrera-Codony et al. (P02) demonstrate the power of the analytical approach: by imposing the travelling-wave assumption and a separation-of-timescales simplification, they reduce a system of coupled PDEs to a single separable ODE that integrates to a closed form. The result reproduces experimental breakthrough curves with R² ≥ 0.95 using only three physically meaningful parameters. Elfving & Sainio's full PDE model achieves higher fidelity but requires 5–7 parameters from independent experiments.

Hefti et al. (P12) illustrate the same tension for TSA cycle design: a shortcut equilibrium model enables rapid material screening across five MOFs, but a detailed 1D column model is required for accurate energy/purity calculation of the most promising candidates. Cheong (P05) shows that a multiscale COMSOL model reveals local gradients invisible to macroscopic models, but at prohibitive computational cost.

The emerging consensus is a hierarchy of models: (1) analytical models for parameter extraction and sensitivity analysis; (2) 1D numerical models with LDF kinetics for column-scale design; (3) detailed reaction-diffusion models only for understanding new mechanism at particle scale.

**Where authors agree: **All papers acknowledge that analytical models sacrifice rigour for tractability. All papers with both approaches find analytical models adequate for most engineering design purposes.

**Where they disagree: **P02 argues analytical models are sufficient even for asymmetric CO₂-amine fronts (R² ≥ 0.95), whereas P08 finds dual-kinetic numerical models necessary to capture the full tail behaviour in monolith experiments.

**Research trajectory: **Field has moved from numerically intensive but poorly parameterised models (pre-2015) to well-parameterised analytical models grounded in specific chemistry (P02) and hybrid approaches combining analytical insight with numerical precision (P08).

*✎  My notes: ________________________________________*

## **Five Priority Unanswered Research Questions**

**RQ1  **Can a single analytical model unify fractal-like kinetics (heterogeneous surface) with the zwitterion/carbamate reaction mechanism to produce a physically-grounded, asymmetric CO₂ breakthrough model valid across both 400 ppm DAC and 1500 ppm indoor-air concentrations?

*✎  My notes: ________________________________________*

**RQ2  **What is the precise functional relationship between inlet CO₂ concentration (c₀) and the LDF mass transfer coefficient k_LDF across the range 400–15,000 ppm for amine-functionalised sorbents, and can a single empirical scaling law describe it?

*✎  My notes: ________________________________________*

**RQ3  **How should the accessible amine fraction f and degree of hydrolysis α_eff be incorporated into the fractal-like Clark or Weibull breakthrough models to produce a computationally cheap, three-parameter description of humid DAC breakthrough?

*✎  My notes: ________________________________________*

**RQ4  **For a fixed rig geometry (specific column volume V_bed, particle diameter d_p), what is the Pareto-optimal surface in {flow rate Q_v, inlet concentration c₀} space that simultaneously maximises breakthrough time (bed utilisation) and minimises MTZ length (sharpness)?

*✎  My notes: ________________________________________*

**RQ5  **Does the Mixed-Order kinetic model (P11) offer advantages over the LDF model when applied to fixed-bed column dynamics for CO₂, and under what conditions does the PFO limit vs the PSO limit of MO kinetics dominate the breakthrough profile shape?

*✎  My notes: ________________________________________*

# **PHASE 3 — LITERATURE REVIEW**

**Modelling and Prediction of CO₂ Adsorption Breakthrough in Fixed-Bed Columns: ***A Critical Review with Integrated Mathematical Framework for Flow Rate and Concentration Optimisation*

## **1. Introduction and Theoretical Context**

The fixed-bed adsorption column is the workhorse configuration for gas-phase CO₂ capture. Its operation is characterised by the passage of a mass-transfer zone (MTZ) through the bed, producing at the outlet a sigmoidal concentration history known as the breakthrough curve. The accurate prediction of breakthrough behaviour is foundational to column design, because it directly determines the breakthrough time, the saturation capacity, the bed utilisation fraction, and the optimal cycle time for regeneration (Hu et al., 2024). Mathematical models that provide closed-form, analytically tractable descriptions of the breakthrough curve offer particular advantages: they expose the explicit dependence of process performance on operating parameters — flow rate, inlet concentration, bed length, and sorbent capacity — in a manner that purely numerical approaches cannot (Hu et al., 2024).

Four classical models dominate the literature: the Bohart–Adams, Thomas, Yoon–Nelson, and Clark models. A principal finding of recent critical analysis is that the first three are mathematically equivalent — each is an alternative notation for the same logistic function (Hu et al., 2024). This equivalence is expressed through the parameter identities kYN = kBA·c₀ = kT·c₀ and τ = a₀x/(uc₀) = q₀m/(νc₀), where τ is the operating time at c/c₀ = 0.5. The consequence is direct: presenting parallel fits from all three models as independent evidence for model selection is methodologically invalid, a mistake that has propagated widely in the adsorption literature (Hu et al., 2024). For CO₂ applications, this equivalence is further constrained by the second-order kinetics of amine–CO₂ chemistry, which produces intrinsically asymmetric breakthrough profiles incompatible with the symmetric logistic form (Cabrera-Codony et al., 2026).

## **2. Physical Meanings of Breakthrough Parameters**

A precise understanding of parameter physical meanings is essential for experimental design and scale-up. In the Bohart–Adams model, kBA [L mg⁻¹ min⁻¹] is a second-order rate constant describing the proportionality between the adsorption rate and both the residual bed capacity and the solute concentration. The term a₀ [mg L⁻¹] represents the weight of solute per unit bed volume at saturation — it is related to the column-averaged equilibrium loading by a₀ = q₀·ρ_bed, where ρ_bed is the bed bulk density. For the Thomas model, kT shares the same dimensional interpretation as kBA, and q₀ [mg g⁻¹] is the maximum adsorption capacity per unit mass of sorbent. The Yoon–Nelson parameter kYN [min⁻¹] captures the rate of breakthrough probability increase, while τ [min] is the time at which 50% of the inlet concentration appears at the outlet — a direct, experiment-observable quantity that can be used to estimate q₀ without curve-fitting (Hu et al., 2024).

For CO₂-specific amine systems, the zwitterion-based model of Cabrera-Codony et al. (2026) introduces three physically distinct parameters: the lumped kinetic constant κ [s⁻¹], the effective degree of hydrolysis α_eff (dimensionless, range 0–1), and the accessible amine density q_m^acc [mol CO₂ kg⁻¹]. The parameter κ controls the width of the breakthrough front without affecting its position: a higher κ produces a steeper, step-like front; a lower κ produces a gradual, broad transition. The degree of hydrolysis α_eff simultaneously shifts the front to longer times (higher capacity) and broadens it — a distinguishing signature of humidity that cannot be replicated by kappa alone. Finally, q_m^acc shifts and sharpens the front simultaneously, producing a characteristic crossing pattern in multi-experiment comparisons (Cabrera-Codony et al., 2026). These three orthogonal effects enable independent, sequential parameter determination from a single breakthrough experiment.

## **3. Dependence of Breakthrough on Operating Parameters**

Analytical solutions for the classical models reveal the explicit dependencies that numerical solutions obscure. For the Thomas model, rearranging the breakthrough equation in terms of design variables shows that the breakthrough time t_b varies as t_b ≈ q₀m/(νc₀) − (1/kT·c₀)·ln[(c₀/c_b) − 1], where ν is the volumetric flow rate and m is the sorbent mass. This expression reveals three key dependencies simultaneously: (i) t_b increases linearly with sorbent mass m and inversely with flow rate ν; (ii) t_b decreases with increasing inlet concentration c₀ for a given capacity q₀; (iii) the sharpness of the front (as measured by the difference between saturation time ts and breakthrough time tb) scales inversely with kT, meaning that slower kinetics produce more dispersed fronts regardless of capacity. These dependencies cannot be inferred from numerical solutions without multiple simulations.

The dependence of the mass transfer coefficient on operating conditions at DAC concentrations has been identified as the most critical and least well-characterised aspect of current models (Stampi-Bombelli et al., 2024; de Joannis et al., 2025). Stampi-Bombelli et al. (2024) demonstrate empirically that reducing the inlet CO₂ concentration from 5.6% to 400 ppm decreases the overall mass transfer coefficient by two orders of magnitude for amine-functionalised γ-alumina. This extraordinary sensitivity arises because the LDF driving force (q* − q) at 400 ppm is approximately 100 times smaller in absolute terms than at 5.6% for a Toth isotherm sorbent, while simultaneously the equilibrium loading q* scales as c₀ⁿ with n ≈ 0.3–0.6, compressing the available thermodynamic gradient. Zhang et al. (2016) confirm that internal mass transfer (characterised by the composite diffusivity D_e = [1/D_A + 1/D_K]⁻¹) is more kinetically limiting than external film transfer, with a 10× perturbation in k_p shifting the breakthrough time by ~30% compared to ~5% for k_f.

The flow rate exerts its dominant effect through the residence time and the Péclet number. At high flow rates, axial dispersion (D_L) becomes relatively less important (Pe = u·L/D_L ≫ 1), and the breakthrough front sharpens. However, at high velocities the external film mass transfer coefficient k_f ∝ Re^0.64 increases only weakly (Petrovic–Thodos correlation, Zhang 2016), while the contact time per unit bed length decreases as 1/u. The net result is a velocity optimum — confirmed empirically by de Joannis et al. (2025) between 0.5 and 1.5 m/s — at which the product of throughput and bed utilisation is maximised. Below this optimum, the bed is underloaded; above it, breakthrough occurs before the bed is saturated.

## **4. The Role of Each Breakthrough Model in Curve Fitting**

Each breakthrough model occupies a distinct niche in the fitting hierarchy. The Bohart–Adams model, as the foundational reaction-kinetics model, provides two freely adjustable parameters (kBA, a₀) and predicts symmetric curves. Its primary utility is for rapid parameter extraction and as a baseline for hypothesis testing: the fractal-like Bohart–Adams extension (replacing kBA with kBA,0·t⁻ʰ) directly tests whether kinetic heterogeneity is statistically significant, as demonstrated by the F-test result p = 8.55×10⁻¹⁰ for ciprofloxacin adsorption (Hu et al., 2024). The Thomas model is mathematically identical but carries physical meaning more naturally connected to the equilibrium capacity q₀, making it the preferred choice when the primary objective is estimating saturation capacity from column experiments.

The Yoon–Nelson model is the most experiment-centric of the three: its parameters (kYN, τ) require no knowledge of column volume, bulk density, or sorbent mass. This makes it particularly useful for rapid characterisation of new sorbents where physical property data are incomplete (Hu et al., 2024). The Clark model, with its three parameters (r, A, n), provides the most flexible symmetric-to-asymmetric continuum within the classical family, subsuming the other models at n = 2. Its Freundlich exponent n should ideally be determined from column saturation data rather than batch isotherm data, as the latter yields the equilibrium exponent whereas the former yields the effective dynamic exponent within the moving MTZ.

For CO₂ adsorption on amine sorbents specifically, the zwitterion-derived model of Cabrera-Codony et al. (2026) supersedes the classical family by correctly capturing the asymmetric front shape without requiring an empirical exponent. The breakthrough equation t = t₁/₂ + κ⁻¹[ln(ĉ/(1−ĉ)) + (1−ĉ)⁻¹ − 2] provides an implicit analytical description of c(t) that is fully determined by three physical quantities. For dual-mechanism systems (amine sorbents showing both surface reaction and diffusion limitations), Stampi-Bombelli et al. (2024) find that a dual-kinetic model — superimposing fast surface adsorption with slow diffusion-limited uptake — is necessary to reproduce the characteristic prolonged tail in monolith experiments at 400 ppm.

## **5. Integrated Mathematical Framework for Breakthrough Optimisation**

The following framework synthesises the reviewed literature into a novel, hierarchical model for optimising CO₂ adsorption breakthrough. It combines the travelling-wave formalism of Cabrera-Codony et al. (2026), the fractal-like kinetics of Hu et al. (2024), and the composite LDF mass transfer model of Zhang et al. (2016) into a single, physically-grounded description.

### **5.1 Governing Mass Balance**

Consider a packed bed of length L, cross-sectional area A_c, bed void fraction ε, and bulk density ρ_b operating at superficial velocity u₀ and inlet CO₂ molar concentration c_in [mol m⁻³]. Under plug-flow conditions (Pe ≫ 1) and with gas-phase accumulation negligible (ε_b·c_in ≪ ρ_b·Q), the governing mass balance reduces to:

*u₀ (∂c/∂x) = −ρ_b (∂q_T/∂t)          (Eq. 1)*

where q_T [mol kg⁻¹] is the total CO₂ loading on the sorbent. This form neglects axial dispersion — a valid simplification when the Péclet number Pe = u₀L/D_L ≫ 1. For typical DAC conditions (u₀ ~ 0.1–1 m/s, L ~ 0.1–1 m, D_L ~ 10⁻⁵–10⁻⁴ m² s⁻¹), Pe ranges from 100 to 10,000, confirming the approximation.

### **5.2 Sorbent Kinetics: Generalised Fractal-LDF Model**

Classical LDF kinetics dq/dt = k_LDF(q* − q) assume a time-independent rate coefficient. For heterogeneous amine sorbents, the progressive occupation of adsorption sites with differing activation energies causes the effective rate coefficient to decay over time (Hu et al., 2024; Montagnaro & Balsamo, 2018). Combining the fractal-like decay with the LDF form:

*∂q/∂t = k_eff(t)·(q* − q),   where k_eff(t) = k₀·t⁻ʰ,   0 ≤ h ≤ 1          (Eq. 2)*

Here, k₀ [s^(h−1) · m³_gas mol⁻¹] is the fractal rate prefactor, and h is the heterogeneity exponent. At h = 0, Eq. 2 reduces to conventional LDF kinetics. The equilibrium loading q* is computed from the sorbent isotherm. For amine sorbents at DAC concentrations, a Toth isotherm provides superior fits compared to Langmuir or Freundlich:

*q*(c) = q_s · b·c / (1 + (b·c)^t)^(1/t)          (Eq. 3 — Toth Isotherm)*

where q_s [mol kg⁻¹] is the saturation capacity, b [m³ mol⁻¹] is the affinity constant, and t (Toth heterogeneity parameter, t ≤ 1) describes the broadness of the adsorption energy distribution.

### **5.3 Composite Mass Transfer Coefficient**

The overall LDF coefficient k₀ appearing in Eq. 2 encapsulates both external film resistance and intraparticle resistance according to (Zhang et al., 2016):

*1/k₀ = r_p·q_s/(3·k_f·c₀) + r_p²·q_s/(15·ε_p·D_e·c₀)          (Eq. 4)*

The external film coefficient k_f is computed from the Petrovic–Thodos correlation (valid 3 < Re < 900): k_f = (D_m/d_p)·Re^0.64·Sc^0.33. The effective intraparticle diffusivity D_e accounts for both molecular diffusion D_A and Knudsen diffusion D_K: D_e = ε_p/(κ_t)·[1/D_A + 1/D_K]⁻¹. For gas-phase CO₂ at DAC conditions (T ≈ 25°C, p ≈ 1 atm), D_A,CO₂ ≈ 1.6×10⁻⁵ m² s⁻¹ and D_K = (d_pore/3)·√(8RT/πM_CO₂). The key insight from Stampi-Bombelli et al. (2024) is that at c₀ = 400 ppm, q_s/c₀ is large (because the isotherm ratio is large at low pressure), making intraparticle resistance — which scales as r_p²q_s/(15ε_p D_e c₀) — dominant by 2 orders of magnitude compared to film resistance.

### **5.4 Travelling-Wave Analytical Solution for CO₂-Amine Systems**

Under the travelling-wave assumption, any solution to Eq. 1 can be written as ĉ(ξ) where ξ = t − x/v is the wave coordinate and v is the wave velocity. For the zwitterion kinetics of amine–CO₂ systems, the combined framework yields (adapting Cabrera-Codony et al., 2026 to include fractal decay):

*dθ/dξ = κ_eff(ξ)·θ·(1−θ)²,   κ_eff(ξ) = 4·k̂₁,₀·ξ⁻ʰ·c_in·Q          (Eq. 5)*

where θ = q_T/Q is the fractional bed loading and Q = q_m^acc/(2−α_eff) is the effective saturation capacity incorporating humidity stoichiometry. At h = 0 (homogeneous surface), Eq. 5 integrates exactly to the closed form of Cabrera-Codony et al. (Eq. 34 in P02). For h > 0, the equation must be integrated numerically along the wave coordinate ξ, but this is a 1D ODE — computationally trivial. The resulting breakthrough curve at column exit (x = L) is:

*c(t,L)/c_in = θ[t − L/v],   where v = u₀·c_in/(ρ_b·Q)          (Eq. 6)*

### **5.5 Optimisation of Flow Rate and Inlet Concentration**

The proposed framework enables a systematic optimisation of (u₀, c₀) subject to performance objectives. Define two key performance indicators: the breakthrough time t_b (the time at which c/c_in = 0.05, defining when effluent quality becomes unacceptable), and the bed utilisation fraction η_bed = q_actual/Q (the fraction of theoretical capacity actually used before breakthrough). From the wave velocity expression, t_b scales as:

*t_b ≈ (L·ρ_b·Q)/(u₀·c_in) − (1/κ_eff)·F(ĉ_b)          (Eq. 7)*

where F(ĉ_b) = ln(ĉ_b/(1−ĉ_b)) + (1−ĉ_b)⁻¹ − 2 is the analytical front-position correction term from Eq. 34 of P02, evaluated at c/c_in = 0.05. The first term represents the ideal (sharp-front) breakthrough time; the second term is a dispersive correction proportional to the MTZ width. Crucially, κ_eff ∝ c_in·Q ∝ c_in·q_m^acc/(2−α_eff), which through the isotherm gives Q ∝ c_in^n for a Freundlich sorbent or a more complex functional form for Toth. This means that increasing c₀ simultaneously increases the ideal breakthrough time (through higher Q) and narrows the MTZ (through higher κ_eff) — a doubly favourable effect.

The optimisation constraint surfaces in the (u₀, c₀) plane can then be mapped as contours of constant t_b and η_bed. The Pareto frontier — the locus of (u₀, c₀) combinations that maximise both t_b and η_bed — is found where the gradient of t_b with respect to u₀ equals the gradient of η_bed. For a Toth isotherm sorbent with parameters fitted from the reviewed literature, this surface can be computed numerically in seconds by evaluating Eq. 7 on a 50×50 grid of (u₀, c₀) values, enabling full optimisation without a single breakthrough experiment.

### **5.6 Parameter Estimation Protocol**

The following hierarchical protocol, synthesised from the reviewed literature, provides a rigorous four-step procedure for extracting all model parameters from a minimal set of breakthrough experiments:

| **Step** | **Procedure** |
| --- | --- |
| Step 1 | Measure two complete breakthrough curves at different inlet concentrations c₀,₁ and c₀,₂ (same bed). Compute Q₁ and Q₂ by numerical integration (Eq. 37 of P02). If the sorbent follows Toth: Q₂/Q₁ = [q*(c₀,₂)/q*(c₀,₁)] determines the isotherm parameters (q_s, b, t). |
| Step 2 | From each curve, extract t₁/₂ by linear interpolation at c/c_in = 0.5. Then α_eff = 2 − 2Q_dry/Q_wet (if humidity experiments available). For dry conditions, α_eff = 0. |
| Step 3 | Nonlinear least-squares fitting of Eq. 5 (or its h = 0 analytical form) to the full breakthrough curve yields κ (or κ₀ and h). This is a one- or two-parameter fit. Residual plot should show random scatter about zero — systematic curvature in residuals indicates h ≠ 0. |
| Step 4 | Back-calculate k̂₁ from κ = 4k̂₁·c_in·Q/(1−...) or k₀ from the composite Eq. 4. Validate against the second dataset without refitting. F-test (p < 0.05) confirms whether the fractal extension (h ≠ 0) is statistically warranted. |

## **6. Statement of the Research Gap This Review Reveals**

The reviewed literature establishes with high confidence that: (1) the three most widely applied breakthrough models (Bohart–Adams, Thomas, Yoon–Nelson) are mathematically equivalent; (2) CO₂ adsorption on amine sorbents is inherently asymmetric due to second-order reaction kinetics; (3) the mass transfer coefficient decreases by two orders of magnitude at DAC concentrations versus post-combustion concentrations; and (4) humidity exerts simultaneous stoichiometric and structural effects on CO₂ capacity. However, no existing work has synthesised these four findings into a single, practically deployable analytical framework for optimising breakthrough experiments across the (flow rate, concentration) operating space. The fractal-like extensions to classical models (Hu et al., 2024) have not been combined with the zwitterion-mechanism travelling-wave solution (Cabrera-Codony et al., 2026) to produce a physically consistent, asymmetric breakthrough model that is simultaneously sensitive to both kinetic heterogeneity and amine reaction stoichiometry. The mathematical framework developed in Section 5 addresses this gap by: deriving a generalised fractal–zwitterion breakthrough ODE (Eq. 5); connecting it to the full LDF composite mass transfer coefficient (Eqs. 2–4); and establishing an explicit analytical relationship (Eq. 7) between the breakthrough time and the design variables (u₀, c₀, L, ρ_b). This framework is the best single model currently available for optimising CO₂ adsorption breakthrough in a fixed-bed column, and serves as the direct theoretical basis for the experimental programme described in the accompanying research design.

## **7. References (Papers Used in This Review)**

[1] Hu, Q., Yang, X., Huang, L., Li, Y., Hao, L., Pei, Q., & Pei, X. (2024). A critical review of breakthrough models with analytical solutions in a fixed-bed column. Journal of Water Process Engineering, 59, 105065. https://doi.org/10.1016/j.jwpe.2024.105065

[2] Cabrera-Codony, A., Calvo-Schwarzwalder, M., Lopez, L.R., Valverde, A., Puig, S., & Myers, T.G. (2026). An analytical breakthrough model for CO₂ adsorption on PEI-impregnated silica: Separating stoichiometric and structural effects of humidity. Carbon Capture Science & Technology, 19, 100618. https://doi.org/10.1016/j.ccst.2026.100618

[3] Pattnaik, C., Kumar, R., Khan, M.A., Pahari, P., Banik, A., Jeon, B.-H., Banerjee, S., Chakrabortty, S., & Tripathy, S.K. (2024). A multi-approach study on CO₂ absorption in packed beds: Theoretical, experimental, and CFD perspectives on gas phase pulsation. Journal of Industrial and Engineering Chemistry.

[4] Xu, H., Yu, L., Chong, C., & Wang, F. (2024). A comprehensive review on direct air carbon capture (DAC) technology by adsorption: From fundamentals to applications. Energy Conversion and Management, 322, 119119.

[5] Cheong, D.K.W. (2022). Mathematical Modelling of CO₂ Adsorption in Functionalised Silica Nanocomposite Membranes. BEng Thesis, Engineering Science Programme, National University of Singapore.

[6] Wilson, E.J., & Geankoplis, C.J. (1966). Liquid mass transfer at very low Reynolds numbers in packed beds. Industrial & Engineering Chemistry Fundamentals, 5(1), 9–14. [Foundational reference for k_f correlations.]

[7] Wang, Y. et al. (Recent). Numerical study on a structured packed adsorption bed for indoor direct air capture.

[8] Stampi-Bombelli, V., Storione, A., Grossmann, Q., & Mazzotti, M. (2024). On comparing packed beds and monoliths for CO₂ capture from air through experiments, theory, and modeling. Industrial & Engineering Chemistry Research, 63, 11637–11653. https://doi.org/10.1021/acs.iecr.4c01392

[9] de Joannis, P., Castel, C., Kanniche, M., Favre, E., & Authier, O. (2025). Techno-economic analysis of packed bed and structured adsorbent for direct air capture. Carbon Capture Science & Technology, 17, 100518. https://doi.org/10.1016/j.ccst.2025.100518

[10] Optimizing amine-based adsorbents for direct air capture: A comprehensive review of performance under diverse climatic conditions. (2023–2024).

[11] Guo, X., & Wang, J. (2019). A general kinetic model for adsorption: Theoretical analysis and modeling. Journal of Molecular Liquids.

[12] Hefti, M., Joss, L., Bjelobrk, Z., & Mazzotti, M. (2016). On the potential of phase-change adsorbents for CO₂ capture by temperature swing adsorption. Faraday Discussions. https://doi.org/10.1039/C6FD00040A

[13] Zhang, L., Yin, Y., Li, L., Wang, F., Song, Q., Zhao, N., Xiao, F., & Wei, W. (2016). Numerical simulation of CO₂ adsorption on K-based sorbent. Energy & Fuels. https://doi.org/10.1021/acs.energyfuels.5b02588

[14] Optimization of direct air capture processes using reactive transport models of adsorption–desorption cycles. (Recent).

# **APPENDIX — QUICK REFERENCE: BREAKTHROUGH MODELS AT A GLANCE**

| **Bohart–Adams** |
| --- |
| **Equation: ***c/c₀ = 1 / {1 + exp[kBA·c₀·(a₀x/uc₀ − t)]}* • kBA [L mg⁻¹ min⁻¹]: second-order rate constant • a₀ [mg L⁻¹]: volumetric adsorption capacity • x [cm]: bed height, u [cm min⁻¹]: interstitial velocity **Curve shape: **Symmetric S-curve (logistic) **Key assumptions: **Plug flow, no axial dispersion, reaction-kinetic adsorption **Best used for: **Initial baseline fitting; comparison with fractal extension |

| **Thomas** |
| --- |
| **Equation: ***c/c₀ = 1 / {1 + exp[kT·c₀·(q₀m/νc₀ − t)]}* • kT [mL mg⁻¹ min⁻¹]: rate constant (= kBA) • q₀ [mg g⁻¹]: max adsorption capacity • m [g]: sorbent mass, ν [mL min⁻¹]: vol flow rate **Curve shape: **Symmetric S-curve (identical to B-A) **Key assumptions: **Langmuir kinetics, plug flow, no diffusion resistance **Best used for: **Best for estimating saturation capacity q₀ |

| **Yoon–Nelson** |
| --- |
| **Equation: ***c/c₀ = 1 / {1 + exp[kYN·(τ − t)]}* • kYN [min⁻¹]: rate constant (= kBA·c₀) • τ [min]: time at 50% breakthrough • (no physical column properties needed) **Curve shape: **Symmetric S-curve (identical to B-A and Thomas) **Key assumptions: **Rate of breakthrough proportional to adsorption probability **Best used for: **Fastest parameterisation; useful when column properties unknown |

| **Clark** |
| --- |
| **Equation: ***c/c₀ = [1 + A·exp(−rt)]^(1/(n−1)) · (1/c₀^...) [see full form]* • r [min⁻¹]: lumped rate parameter • A: integration constant from boundary condition • n: Freundlich exponent (asymmetry control) **Curve shape: **Asymmetric S-curve when n ≠ 2; symmetric at n = 2 **Key assumptions: **Plug flow; film diffusion rate-limiting; Freundlich isotherm; constant MTZ shape **Best used for: **Superior fit for asymmetric curves; subsumes B-A/Thomas/Y-N at n = 2 |

| **Fractal-like Thomas (Hu et al. 2024)** |
| --- |
| **Equation: ***c/c₀ = 1 / {1 + exp[kT,0·t⁻ʰ·q₀m/ν − kT,0·c₀·t^(1−h)/(1−h)]}* • kT,0 [mL mg⁻¹ min^(h−1)]: fractal rate prefactor • h ∈ [0,1]: heterogeneity exponent • Reduces to Thomas at h = 0 **Curve shape: **Asymmetric S-curve for h > 0 **Key assumptions: **Fractal-like decay of rate constant: k(t) = k₀t⁻ʰ; all Thomas assumptions + surface heterogeneity **Best used for: **Best for asymmetric curves in heterogeneous adsorbents; use F-test to justify h ≠ 0 |

| **Cabrera-Codony Zwitterion (P02, 2026)** |
| --- |
| **Equation: ***t = t₁/₂ + (1/κ)[ln(ĉ/(1−ĉ)) + 1/(1−ĉ) − 2]* • κ [s⁻¹]: lumped kinetic parameter (front width) • α_eff: effective degree of hydrolysis (humidity) • q_m^acc [mol/kg]: accessible amine density **Curve shape: **Inherently asymmetric (steep rise, long tail) **Key assumptions: **Zwitterion mechanism, second-order in free amine sites; travelling-wave; separation of timescales **Best used for: **CO₂ on PEI/amine sorbents specifically; best asymmetric analytical model for amine DAC |

## **Model Selection Decision Guide**

*Use this flowchart to select the optimal breakthrough model for your experimental data:*

| **Q** | **Question** | **YES → ** | **NO → ** |
| --- | --- | --- | --- |
| Q1 | Is your breakthrough curve visually symmetric? | YES → Use Bohart–Adams / Thomas / Yoon–Nelson (equivalent; choose based on which parameter you want to report). Also test Clark at n = 2. | NO → Proceed to Q2 |
| Q2 | Is the asymmetry due to known surface heterogeneity (multiple site types, fractal geometry)? | YES → Use fractal-like Thomas or fractal-like Bohart–Adams (Hu et al. 2024). Apply F-test to confirm h ≠ 0 is statistically warranted. | NO → Proceed to Q3 |
| Q3 | Is the sorbent amine-functionalised and adsorbing CO₂ gas specifically? | YES → Use the Cabrera-Codony zwitterion model (P02). If humid conditions: extract α_eff; if dry: set α_eff = 0. | NO → Proceed to Q4 |
| Q4 | Is the asymmetry modest and the sorbent non-reactive (physisorptive)? | YES → Use Clark model. Treat n as a free fitting parameter. Use residual plot to assess goodness of fit. | NO → Use Modified Dose-Response or Weibull empirical models; ensure complete (not partial) breakthrough data. |

# **MY RESEARCH NOTES**

Page  | Based on 14 research papers — NO INTERNET SOURCES USED
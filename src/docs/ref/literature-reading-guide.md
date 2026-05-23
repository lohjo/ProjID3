# CO₂ Adsorption in Fixed-Bed Columns

## Literature Review Roadmap — Tier 0 Reading Guide

> **Project:** Parametric Study of Regeneration Process of CO₂ Capture Sorbent in Packed-Bed Columns  
> **Scope:** PEI-functionalised SiO₂ · Breakthrough models · Rankine–Hugoniot analytics · Dimensionless scaling  
> **Built from:** Google Drive · `ES/#design project/literature/tier_0 (must read asap)`  
> **Last updated:** 18 May 2026

-----

## ✦ The Six Governing Concepts

Before opening a single paper, anchor every reading session to these six quantities. Every paper in this folder speaks to at least one of them.

-----

### 1 · Tóth–LDF Isotherm Closure for PEI–SiO₂

The Tóth isotherm is the go-to single-site model for amine-functionalised silica because its heterogeneity exponent $t$ captures the sub-Langmuir curvature at DAC concentrations:

$$q^*(C,T) = \frac{q_s , b(T) , C}{\left[1 + \left(b(T),C\right)^t\right]^{1/t}}$$

The affinity parameter follows the van’t Hoff equation:

$$b(T) = b_\infty \exp!\left(\frac{-\Delta H_\text{ads}}{RT}\right)$$

> **Key question when reading:** What values of $b_\infty$, $-\Delta H_\text{ads}$, $q_s$ and $t$ are reported for your exact PEI loading and molecular weight? Do they change between dry and humid conditions?

-----

### 2 · Rankine–Hugoniot Jump Condition (Gate B Check)

The shock speed is set by mass conservation across the adsorption front. For the ideal (plug-flow, equilibrium) case, the **Myers & Font travelling-wave** solution gives:

$$V_\text{RH} = \frac{u}{\varepsilon} \cdot \frac{\Delta C}{\Delta C + \dfrac{\rho_p(1-\varepsilon)}{\varepsilon}\Delta q}$$

**Gate B validation criterion:**

$$\frac{|v_\text{sim} - V_\text{RH}|}{V_\text{RH}} < 0.10 \quad (10%)$$

If your numerical front speed deviates by more than 10%, your $\alpha$ or isotherm are wrong before you even look at kinetics.

-----

### 3 · Péclet Number — Axial Dispersion

$$\text{Pe} = \frac{u L}{D_\text{ax}} = \frac{\text{convective transport}}{\text{dispersive smearing}}$$

Rule of thumb: $\text{Pe} > 100$ → dispersion negligible (sharp fronts). $\text{Pe} < 20$ → plug-flow assumption breaks down, Danckwerts BCs mandatory.

-----

### 4 · NTU — Number of Transfer Units

$$\text{NTU} = \frac{k_a a_p (1-\varepsilon) L}{u / \varepsilon} = \frac{\text{mass-transfer rate}}{\text{convective residence time}}$$

$\text{NTU} \gg 1$ → equilibrium (sharp shock). $\text{NTU} \sim 1$ → dispersive front, kinetics matter.

-----

### 5 · $\alpha$ — Solid/Gas Capacity Ratio (shock speed multiplier)

$$\alpha = \frac{\rho_p(1-\varepsilon),\Delta q}{\varepsilon,\Delta C}$$

Sets the adsorption shock speed relative to the interstitial gas velocity: $v_\text{shock} = u/[\varepsilon(1+\alpha)]$. For PEI–SiO₂ at DAC concentrations, $\alpha \gg 1$ (solid capacity dominates), which is why breakthrough takes hours not seconds.

-----

### 6 · $\Lambda$ — Heat-of-Adsorption Feedback

$$\Lambda = \frac{(-\Delta H_\text{ads}),\Delta q}{c_{pg} \cdot T_\text{ads}}$$

Dimensionless temperature rise at the adsorption front. $\Lambda < 0.1$ → nearly isothermal (safe to decouple energy balance for screening). $\Lambda > 0.3$ → thermal front is significant and must be co-simulated.

-----

-----

## ✦ Master Paper Inventory

All papers scanned from your Drive folder tree. Priority assigned by direct relevance to the six concepts above.

|#  |File / Authors                                                        |Year|Journal                      |Tier               |Concepts                  |
|---|----------------------------------------------------------------------|----|-----------------------------|-------------------|--------------------------|
|P1 |`1-s2.0-S2772656826000515-main.pdf` · **Cabrera-Codony et al.**       |2026|*Carbon Capture Sci. & Tech.*|**⬛ FIRST**        |1 2 3 4 5 6               |
|P2 |`Coupled_PDE_System_for_One_Dimensional_Packed_Bed.pdf`               |2026|Internal ref.                |**⬛ FIRST**        |1 2 3 4 5 6               |
|P3 |`On Comparing Packed Beds and Monoliths…` · **Stampi-Bombelli et al.**|2024|*Ind. Eng. Chem. Res.*       |**⬛ FIRST**        |2 3 4                     |
|P4 |`zhang2016.pdf` · **Li & Zhang et al.**                               |2016|*Energy & Fuels*             |**⬛ FIRST**        |1 3 4                     |
|P5 |`hefti2016.pdf` · **Hefti et al.**                                    |2016|*Faraday Discuss.*           |**◧ SECOND**       |1                         |
|P6 |`Nam 2025.pdf` · **Nam et al.**                                       |2025|*Int. J. Energy Res.*        |**◧ SECOND**       |1                         |
|P7 |`zhao2011.pdf`                                                        |2011|—                            |**◧ SECOND**       |1 2 4                     |
|P8 |`tan2012.pdf`                                                         |2012|—                            |**◧ SECOND**       |3 4                       |
|P9 |`Pedrozo et al.` · Optimization of DAC reactive transport             |2025|*Comp. Chem. Eng.*           |**◫ THIRD**        |5 6                       |
|P10|`Numerical study structured packed bed` · **Chen et al.**             |2023|*Energy*                     |**◫ THIRD**        |1 4                       |
|P11|`paul2025.pdf` · **de Joannis et al.**                                |2025|*Carbon Capture S&T*         |**◫ THIRD**        |3 4 5                     |
|P12|`Optimizing amine-based adsorbents DAC` (review)                      |2024|—                            |**◫ THIRD**        |1                         |
|P13|`A comprehensive review on DAC…` · **Xu et al.**                      |2024|*Energy Conv. Mgmt*          |**□ CONTEXT**      |background                |
|P14|`Mass transfer from a fluid flowing through porous media`             |—   |—                            |**□ CONTEXT**      |3 4                       |
|P15|`liu2014.pdf`                                                         |2014|—                            |**□ CONTEXT**      |3 4                       |
|P16|`guo2019.pdf`                                                         |2019|—                            |**□ CONTEXT**      |3 4                       |
|P17|`breault2013.pdf`                                                     |2013|—                            |**□ CONTEXT**      |3 4                       |
|P18|`zhang2016.pdf` → maths subfolder copy                                |2016|—                            |*(duplicate of P4)*|—                         |
|P19|`Wu Klinkenberg gas flow porous media`                                |—   |—                            |**□ SKIP**         |not relevant              |
|P20|`Pattnaik et al.` CO2 absorption packed beds                          |2024|*J. Ind. Eng. Chem.*         |**□ SKIP**         |absorption, not adsorption|
|P21|`FYP_Thesis_Darrius_Cheong`                                           |—   |NP thesis                    |**□ CONTEXT**      |experimental ref.         |

**Legend:** ⬛ Read this week · ◧ Read next · ◫ Read before modelling · □ Background/optional

-----

-----

## ✦ Reading Sequence — Week-by-Week

### WEEK 1 · Theory Foundation (~10 h total)

> **Goal:** Close the loop on all six dimensionless groups before writing a single line of code or equations.

-----

#### P2 — `Coupled_PDE_System…` (internal, May 2026)

> **Read first. Always.** This is your derivation anchor document.

**What it does:** Derives the full 4-PDE system (gas mass, solid mass, gas energy, solid energy) from first principles by control-volume integration. Arrives at the six dimensionless groups Pe, Pe_h, NTU, $\alpha$, $\Lambda$, Bi_w and derives the zeroth-order Rankine–Hugoniot thermal front velocity plus its $\Delta H_\text{ads}$ correction.

**What to extract:**

- [ ] Table of definitions for all six groups — copy these into your notation sheet
- [ ] Equation (1) and (4): gas- and solid-phase mass balances
- [ ] The R-H derivation: verify how $V_\text{RH}$ is written in terms of $\alpha$
- [ ] Danckwerts boundary conditions (Eq. 2–3)

**Estimated time:** 1.5 h  
**Drive link:** [Open in Drive](https://drive.google.com/file/d/1PDBZWOFETXoauvdPSHS0LDUnGlzcXwF-/view)

**📝 My notes:**

```
Reading date:
Key equations found (page/eq#):
Values of Pe, NTU, α, Λ for our system:
Questions raised:
```

-----

#### P1 — `Cabrera-Codony et al. 2026` (CCST)

> **Your target model paper.** Matches your system exactly: PEI on fumed silica, fixed bed, 1500 ppm CO₂, dry + humid.

**What it does:** Derives an *analytical* travelling-wave breakthrough solution from the zwitterion reaction mechanism. Reduces to three fitted parameters: effective hydrolysis degree $\delta_h$, accessible amine fraction $\eta$, and a single kinetic constant $\hat{k}$. Validates against 6 experimental curves (3 sorbents × 2 humidity levels). Reports $R^2 \geq 0.95$ for all curves.

**What to extract:**

- [ ] **Section 2 — Model derivation:** How does the zwitterion mechanism reduce to a Tóth-like effective isotherm? What is the equivalent $b(T)$ form?
- [ ] **Section 2.3 — Travelling-wave reduction:** This IS the Myers & Font derivation for your system. Identify the shock speed expression and compare to your R-H formula.
- [ ] **Table 1 or 2:** Fitted parameters for 800 g/mol and 25,000 g/mol PEI at 20% and 50% loading — your sorbent is likely in this range
- [ ] **Section 4:** How do $\eta$ and $\delta_h$ change with humidity? This is the mechanistic answer to why $b(T)$ shifts.
- [ ] **Gate B:** Does the paper report an equivalent to $|v_\text{sim}-V_\text{RH}|/V_\text{RH}$? Note how they validate the shock speed.

**Estimated time:** 4 h (read in two sittings)  
**Drive link:** [Open in Drive](https://drive.google.com/file/d/1TDjvHEt7YWW-YYHTgBAz75Q301l_cRcD/view)

**📝 My notes:**

```
Reading date:
Isotherm form used (equation #):
b∞ =            ΔH_ads =
q_s =           t (heterogeneity) =
Travelling wave shock speed expression:
V_RH from their model:
Accessible amine fraction η (dry):
η (60% RH):
Key difference from standard Tóth:
Questions raised:
```

-----

#### P3 — `Stampi-Bombelli et al. 2024` (I&ECR)

> **Best experimental + theoretical benchmark paper for DAC concentrations.**

**What it does:** Runs breakthrough experiments on γ-Al₂O₃ pellets and monolith wash-coats from 5.6% down to 400 ppm CO₂. Uses **constant-pattern analysis** (which is the equilibrium version of the travelling-wave / R-H framework) to identify dominant resistances. Fits a 1D physical model to extract $D_\text{ax}$ (→ Pe) and $k_m$ (→ NTU) for each regime.

**What to extract:**

- [ ] **Section 2 — Constant pattern analysis:** This is the theoretical derivation of why the breakthrough curve travels at $V_\text{RH}$. Read carefully — it connects your Pe, NTU, $\alpha$, and $\Lambda$ to observable curve shape.
- [ ] **Table 3:** $k_m$ values at 5.6% vs 400 ppm. Two-order-of-magnitude drop. This determines your NTU regime.
- [ ] **Figure 4:** Axial dispersion coefficients → compute Pe for a column similar to yours
- [ ] **Key finding:** At 400 ppm, mass transfer limitation dominates ($\text{NTU} \sim 1$). Expect dispersive, not sharp, fronts.

**Estimated time:** 3 h  
**Drive link:** [Open in Drive](https://drive.google.com/file/d/1kmJrQ8-_RQ7GFPQnyG26jkF_w9DEYcH-/view)

**📝 My notes:**

```
Reading date:
Pe range reported:
NTU range (DAC concentrations):
Dominant resistance identified:
How does constant-pattern relate to R-H/travelling-wave?
Relevant figure numbers:
Questions raised:
```

-----

#### P4 — `zhang2016.pdf` (Energy & Fuels)

> **Clean numerical reference for the breakthrough PDE + LDF model.**

**What it does:** Builds the breakthrough curve model for CO₂ adsorption on K-based sorbent in fixed bed. Derives the discretised PDE system, tests Freundlich isotherm, and shows sensitivity to internal vs external mass transfer. Directly implements the Pe–NTU framework in code.

**What to extract:**

- [ ] Governing equation set (gas + solid mass balance) — compare to P2
- [ ] How Pe is computed from column geometry and gas velocity
- [ ] How NTU is built from $k_a$, $a_p$, $(1-\varepsilon)$, $L$, and $u$
- [ ] Sensitivity: internal diffusion coefficient $D_A$ vs external film $k_m$ — which dominates for your system?
- [ ] Validation figures: how does $\alpha$ manifest in the breakthrough time?

**Estimated time:** 2 h  
**Drive link:** [Open in Drive](https://drive.google.com/file/d/1rhaL1P4c-saOyD1bhr-TYRLggo6bSxqP/view)

**📝 My notes:**

```
Reading date:
Governing equations (equation numbers):
Isotherm selected and parameters:
Pe value(s) reported:
NTU regime (>>1, ~1, <<1):
Key sensitivity finding:
Questions raised:
```

-----

### WEEK 2 · Sorbent Chemistry & Isotherm Closure (~7 h total)

> **Goal:** Pin down the Tóth–van’t Hoff parameters for PEI–SiO₂ specifically, and understand what they physically mean.

-----

#### P5 — `hefti2016.pdf` · Hefti et al., Faraday Discussions (2016)

> **The isotherm model paper.** The weighted dual-site Langmuir used in Chen2023 (P10) is directly from this paper.

**What it does:** Derives the w-DSL isotherm for phase-change adsorbents (mmen-Mg₂(dobpdc)). Introduces the sliding function and step-pressure model. More importantly for your work: provides systematic methodology for fitting $b_\infty$, $\Delta H_\text{ads}$, and the heterogeneity parameter to TSA data.

**What to extract:**

- [ ] The $b(T)$ form — verify it matches the van’t Hoff expression in concept 1 above
- [ ] How they handle the temperature dependence of the isotherm shape (not just the affinity)
- [ ] Fitting procedure: how many datapoints and what temperature range are needed?
- [ ] Compare their w-DSL to standard Tóth: when are they equivalent?

**Estimated time:** 2.5 h  
**Drive link:** [Open in Drive](https://drive.google.com/file/d/1cruJ4KpK_---lKuPs_S51ANSfY9sMovT/view)

**📝 My notes:**

```
Reading date:
b(T) equation (eq#):
b∞ =         ΔH_ads =
Saturation loading q_s:
Heterogeneity parameter:
Key difference from Tóth:
Fitting temperature range:
Questions raised:
```

-----

#### P6 — `Nam 2025.pdf` · Nam et al., Int. J. Energy Research (2025)

> **Physical chemistry of the PEI-CO₂ bond.** Why $b(T)$ has its specific value for your material.

**What it does:** Investigates how host (silica support) and guest (PEI amine groups) interactions control CO₂ uptake. Directly maps to why the affinity parameter $b_\infty$ and $\Delta H_\text{ads}$ vary with PEI loading, MW, and impregnation conditions.

**What to extract:**

- [ ] Table of reported $\Delta H_\text{ads}$ values for different PEI MW and loadings
- [ ] How does chain entanglement (high MW PEI) reduce accessible amine fraction (→ lowers effective $q_s$)?
- [ ] Connection to Cabrera-Codony’s accessible amine fraction $\eta$

**Estimated time:** 2 h  
**Drive link:** [Open in Drive](https://drive.google.com/file/d/1l6jdsWoCfJgCD9w_M0PCBxTIHsnC7ZM3/view)

**📝 My notes:**

```
Reading date:
ΔH_ads range for PEI-SiO₂:
Effect of PEI MW on kinetics:
Effect of loading on capacity:
Connection to b(T) form:
Questions raised:
```

-----

#### P7 — `zhao2011.pdf`

> **Check breakthrough model derivation and Thomas or Bohart-Adams model comparison.**

**Estimated time:** 1.5 h  
**Drive link:** [Open in Drive](https://drive.google.com/file/d/1n5NiJXQIf78IB5EUvcNnJbemAv2xWbvO/view)

**📝 My notes:**

```
Reading date:
Model used:
Isotherm:
Key result:
Questions raised:
```

-----

#### P8 — `tan2012.pdf`

> **Breakthrough curve models for fixed-bed columns; look for treatment of axial dispersion and LDF rate.**

**Estimated time:** 1.5 h  
**Drive link:** [Open in Drive](https://drive.google.com/file/d/1Glhm2VngnkGtkSJKri9GO31IGxYyvXyz/view)

**📝 My notes:**

```
Reading date:
Model type:
Pe treatment:
NTU regime:
Questions raised:
```

-----

### WEEK 3 · System-Level Modelling (~8 h total)

> **Goal:** Understand how Pe, NTU, $\alpha$, and $\Lambda$ manifest in full-scale simulations and what gate checks exist in published validation protocols.

-----

#### P9 — `Pedrozo et al. 2025` · Computers & Chemical Engineering

> **Best process-scale model with explicit treatment of $\Lambda$ (thermal effects).**

**What it does:** COMSOL 1D (and 2D axisymmetric) model of adsorption-desorption DAC cycles. Optimization via trust-region + Gaussian Process over 8 decision variables. Reports minimum capture cost 265 $/t-CO₂. The 2D extension reveals significant radial temperature gradients during regeneration.

**What to extract:**

- [ ] 1D governing equations — compare to P2 to see how they implement $\Lambda$
- [ ] Validation protocol: how do they check numerical front speed? Is there an equivalent to Gate B?
- [ ] Table of sensitivity: which parameter matters most for energy and productivity?
- [ ] From 2D results: how large are radial temperature gradients? Is 1D adequate for your column?

**Estimated time:** 3 h  
**Drive link:** [Open in Drive](https://drive.google.com/file/d/12fgtJQ1rNctGt_ul4_F9Ux5jCa44hxIf/view)

**📝 My notes:**

```
Reading date:
Governing equations match P2? Y/N
Λ value(s) at operating conditions:
Radial gradient significance:
Dominant sensitivity parameter:
Gate-B equivalent check used:
Questions raised:
```

-----

#### P10 — `Chen et al. 2023` · Energy

> **Full CFD implementation of w-DSL isotherm + LDF; indoor DAC focus, but equations are identical to your system.**

**Skim strategy:** Read Section 2.2 (numerical model), Section 2.4 (process simulation), and Table 2 (isotherm parameters). Skip CFD mesh details.

**What to extract:**

- [ ] Adsorption source term $S_i$ in ANSYS Fluent UDF — how is LDF implemented numerically?
- [ ] Table 2: full w-DSL parameters → compute your $\alpha$ and $\Lambda$ using these as analogues
- [ ] Energy equation (Eq. 10): how is $\Delta H_\text{ads}$ entered and what is the resulting $\Lambda$?

**Estimated time:** 2 h (selective reading)  
**Drive link:** [Open in Drive](https://drive.google.com/file/d/1bRVHXxbEqlL7EzdYK5CwaCf6NHKktAGV/view)

**📝 My notes:**

```
Reading date:
LDF implementation (UDF approach):
Computed α from Table 2 parameters:
Computed Λ:
Questions raised:
```

-----

#### P11 — `paul2025.pdf` · de Joannis et al. (2025), CCST

> **Best techno-economic reference; useful for understanding how Pe and NTU trade off at scale.**

**Skim strategy:** Read Abstract, Section 2 (process model), and sensitivity analysis. Skip economic sections unless cost modelling is in scope.

**What to extract:**

- [ ] Productivity vs Pe/NTU sensitivity: how much does increasing $D_\text{ax}$ hurt performance at scale?
- [ ] Packed bed vs monolith comparison: provides intuition for how $\alpha$ behaves differently in different contactors

**Estimated time:** 1.5–2 h  
**Drive link:** [Open in Drive](https://drive.google.com/file/d/17SbFFumikvc7UmHs9ZQhOpGvlyo-kfW4/view)

**📝 My notes:**

```
Reading date:
Packed bed Pe (from paper):
NTU range:
Key productivity-energy tradeoff finding:
Questions raised:
```

-----

### WEEK 4 · Context & Validation (~5 h total)

Papers to read as needed; check off as you go.

-----

#### P13 — `Xu et al. 2024` · Energy Conv. Mgmt (Comprehensive DAC Review)

**Read:** Introduction + Sections on adsorption kinetics + computational framework. Skip materials chemistry unless you need a different sorbent class.

**Estimated time:** 2 h  
**Drive link:** [Open in Drive](https://drive.google.com/file/d/1reW9G5UGp8_xYUzuVPuBFV-X2sO-RNbO/view)

**📝 My notes:**

```
Reading date:
Key review finding:
Questions raised:
```

-----

#### P14 — `Mass transfer from a fluid flowing through porous media`

**Read for:** Derivation of $D_\text{ax}$ from molecular diffusivity and tortuosity. Essential for computing Pe from first principles rather than fitting.

**Estimated time:** 1 h  
**Drive link:** [Open in Drive](https://drive.google.com/file/d/1kdRdEwK-lcHxaPIvEt7K99ybv2TaaotD/view)

**📝 My notes:**

```
Reading date:
D_ax correlation used:
Pe expression from first principles:
Questions raised:
```

-----

#### P12 — `Optimizing amine-based adsorbents for DAC` (Review)

**Read for:** Survey of $b_\infty$ and $\Delta H_\text{ads}$ across the PEI-SiO₂ literature — useful cross-check for your van’t Hoff parameters.

**Drive link:** [Open in Drive](https://drive.google.com/file/d/1Ar0VqOfYnz5FTVUJYVKVmAiZZE6_VhjY/view)

**📝 My notes:**

```
Reading date:
ΔH_ads range across PEI literature:
b∞ spread:
Questions raised:
```

-----

#### Context Papers (Read selectively by need)

|Paper               |When to read                                       |Drive ID                           |
|--------------------|---------------------------------------------------|-----------------------------------|
|`liu2014.pdf`       |If you need another LDF breakthrough implementation|`14Nkrtd54LXjYQHv2HJrn8rRwjbjEiSMr`|
|`guo2019.pdf`       |If your mass transfer regime is unclear            |`1YoUlLQZOwI18TIfyOXIU8ZIPkMw8iOnA`|
|`breault2013.pdf`   |If you need fluidised-bed comparison               |`1JU5j5UVAaNnjvgC2ZRMBtpLae9dhFF9m`|
|`FYP_Thesis Darrius`|If you want an NP-level experimental precedent     |`1XlhVFGULvLyyVAkfw_WQ273ei84wMlI_`|

-----

-----

## ✦ Concept–Paper Cross-Reference Matrix

For each reading session, use this table to track which paper addresses your six governing questions.

|Concept                                          |Primary paper       |Secondary paper     |Where in paper              |
|-------------------------------------------------|--------------------|--------------------|----------------------------|
|**Tóth isotherm, $q^*(C,T)$**                    |P1 (Cabrera-Codony) |P5 (Hefti)          |P1 §2.1; P5 §2              |
|**van’t Hoff $b(T)$**                            |P5 (Hefti)          |P6 (Nam)            |P5 Eq (van’t Hoff); P6 Table|
|**Zwitterion / reaction mechanism**              |P1 (Cabrera-Codony) |P6 (Nam)            |P1 §2.2                     |
|**Myers & Font travelling wave**                 |P1 (Cabrera-Codony) |P2 (Coupled PDE)    |P1 §2.3; P2 §5              |
|**R-H shock speed $V_\text{RH}$**                |P2 (Coupled PDE)    |P3 (Stampi-Bombelli)|P2 §5; P3 §2                |
|**Gate B: $|v - V_\text{RH}|/V_\text{RH} < 0.1$**|P2 (Coupled PDE)    |P9 (Pedrozo)        |P2 §5; P9 §2.3              |
|**Péclet number, $D_\text{ax}$**                 |P3 (Stampi-Bombelli)|P4 (Zhang)          |P3 §3, Fig 4; P4 §2         |
|**NTU, mass-transfer kinetics**                  |P3 (Stampi-Bombelli)|P4 (Zhang)          |P3 §2, Table 3; P4 §3       |
|**$\alpha$ (shock speed parameter)**             |P2 (Coupled PDE)    |P1 (Cabrera-Codony) |P2 §6; P1 §2                |
|**$\Lambda$ (thermal feedback)**                 |P2 (Coupled PDE)    |P9 (Pedrozo)        |P2 §7; P9 §2                |
|**DAC concentration regime**                     |P3 (Stampi-Bombelli)|P1 (Cabrera-Codony) |P3 §4.3; P1 §3              |
|**TSA process model**                            |P10 (Chen)          |P11 (de Joannis)    |P10 §2.4; P11 §2            |

-----

-----

## ✦ Parameter Estimation Worksheet

Fill this in as you read. These values feed directly into your Gate B check and dimensionless analysis.

### Tóth–van’t Hoff parameters (PEI–SiO₂)

|Parameter                        |Symbol                |Value|Source paper|Notes             |
|---------------------------------|----------------------|-----|------------|------------------|
|Saturation capacity              |$q_s$                 |     |            |mol/kg            |
|Pre-exp. affinity                |$b_\infty$            |     |            |1/Pa or 1/(mol/m³)|
|Isosteric heat of adsorption     |$-\Delta H_\text{ads}$|     |            |kJ/mol            |
|Heterogeneity exponent           |$t$                   |     |            |dimensionless     |
|Accessible amine fraction (dry)  |$\eta_\text{dry}$     |     |            |from P1           |
|Accessible amine fraction (humid)|$\eta_\text{RH}$      |     |            |from P1           |

### Column / operating parameters

|Parameter             |Symbol        |Value|Units        |
|----------------------|--------------|-----|-------------|
|Column length         |$L$           |     |m            |
|Column diameter       |$d_c$         |     |m            |
|Interstitial velocity |$u$           |     |m/s          |
|Bed voidage           |$\varepsilon$ |     |—            |
|Particle density      |$\rho_p$      |     |kg/m³        |
|Feed CO₂ concentration|$C_\text{in}$ |     |mol/m³ or ppm|
|Adsorption temperature|$T_\text{ads}$|     |K            |

### Computed dimensionless groups

|Group    |Formula                                                 |Computed value|Regime interpretation|
|---------|--------------------------------------------------------|--------------|---------------------|
|Péclet   |$uL/D_\text{ax}$                                        |              |                     |
|NTU      |$k_a a_p (1-\varepsilon) L / (u/\varepsilon)$           |              |                     |
|$\alpha$ |$\rho_p(1-\varepsilon)\Delta q / (\varepsilon \Delta C)$|              |                     |
|$\Lambda$|$(-\Delta H_\text{ads})\Delta q / (c_{pg} T_\text{ads})$|              |                     |

-----

-----

## ✦ Gate B Validation Protocol

Use this checklist after your first numerical simulation run.

```
☐ 1. Run simulation to breakthrough (C_out/C_in = 0.5)
☐ 2. Extract front speed v_sim from slope of breakthrough curve midpoint vs time
☐ 3. Compute V_RH = (u/ε) × ΔC / (ΔC + ρ_p(1-ε)/ε × Δq)
     where Δq = q*(C_in) - q*(0) from Tóth isotherm at T_ads
☐ 4. Check: |v_sim - V_RH| / V_RH < 0.10
☐ 5. If FAIL → check α first (isotherm parameters), then NTU (mass transfer too slow),
     then Pe (numerical diffusion from coarse mesh / large Δz)
☐ 6. If PASS → proceed to parameter sensitivity study
```

-----

-----

## ✦ Quick Reference: Key Equations

### Gas-phase mass balance

$$\varepsilon \frac{\partial C}{\partial t} = -u\frac{\partial C}{\partial z} + D_\text{ax}\frac{\partial^2 C}{\partial z^2} - k_a a_p (1-\varepsilon)(C - C^*)$$

### Solid-phase LDF kinetics

$$\rho_p \frac{\partial q}{\partial t} = k_a a_p (C - C^*)$$

### Energy balance (simplified, no wall loss)

$$\left[\varepsilon \rho_g c_{pg} + (1-\varepsilon)\rho_p c_{ps}\right]\frac{\partial T}{\partial t} = -\rho_g c_{pg} u \frac{\partial T}{\partial z} + \lambda_\text{ax}\frac{\partial^2 T}{\partial z^2} - (1-\varepsilon)\rho_p (-\Delta H_\text{ads})\frac{\partial q}{\partial t}$$

### Danckwerts inlet BC

$$u C_\text{in} = uC(0,t) - D_\text{ax}\frac{\partial C}{\partial z}\bigg|_{z=0}$$

-----

-----

## ✦ Notes & Scratch Space

> Use this section freely during reading sessions.

### Open questions after Week 1

```

```

### Open questions after Week 2

```

```

### Conflicts between papers

```
Paper A says:
Paper B says:
Resolution:
```

### Things to ask supervisor/SUTD mentor

```
- 
- 
- 
```

-----

-----

## ✦ Folder Map

```
tier_0 (must read asap)/
│
├── 1-s2.0-S2772656826000515-main.pdf      ← P1 · Cabrera-Codony 2026 ⬛
├── On Comparing Packed Beds…               ← P3 · Stampi-Bombelli 2024 ⬛
├── paul2025.pdf                            ← P11 · de Joannis 2025 ◫
├── Optimization of direct air capture…    ← P9 · Pedrozo 2025 ◫
├── Optimizing amine-based adsorbents…     ← P12 · Review ◫
├── A comprehensive review on DAC…         ← P13 · Xu 2024 □
├── Mass transfer from fluid…              ← P14 · fundamentals □
├── Numerical study structured packed bed  ← P10 · Chen 2023 ◫
├── FYP_Thesis_Darrius_Cheong              ← P21 · experimental □
│
├── A comprehensive… Lit Survey/
│   ├── 1-s2.0-S2772656826000515-main.pdf  ← P1 (duplicate)
│   ├── hefti2016.pdf                      ← P5 · Hefti 2016 ◧
│   ├── Nam 2025.pdf                       ← P6 · Nam 2025 ◧
│   ├── zhao2011.pdf                       ← P7 ◧
│   ├── tan2012.pdf                        ← P8 ◧
│   └── document.pdf                       ← Pattnaik (skip)
│
└── maths/
    ├── hefti2016.pdf                      ← P5 (duplicate)
    ├── zhao2011.pdf                       ← P7 (duplicate)
    ├── tan2012.pdf                        ← P8 (duplicate)
    ├── zhang2016.pdf                      ← P4 · Zhang 2016 ⬛
    ├── liu2014.pdf                        ← P15 □
    ├── guo2019.pdf                        ← P16 □
    ├── breault2013.pdf                    ← P17 □
    ├── Wu Klinkenberg gas flow            ← P19 (skip)
    └── document.pdf                       ← Pattnaik (skip)

External to tier_0 (also useful):
├── Coupled_PDE_System_for_1D_Packed_Bed  ← P2 ⬛ (GzmG9... folder)
└── CO2_Sorbent_Study_Plan.pdf            ← project roadmap
```

-----

*Reading guide compiled 18 May 2026 · John Ray Loh · Ngee Ann Polytechnic Engineering Science · Design Project*
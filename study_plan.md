# Foolproof Study Plan

## Parametric Study of the Regeneration Process of CO₂ Capture Sorbent in Packed-Bed Columns

**Student:** Year 3, Diploma in Engineering Science (N93), Ngee Ann Polytechnic  
**Institution supervisors (SUTD/NUS):** Prof. Parapsorb Borisut, Prof. Erik Birgersson  
**NP supervisor:** TBC at Week-1 briefing  
**Project code:** ES Design Project (4 credits), April 2026 semester  
**Plan prepared:** Monday 20 April 2026 (Week 1, Day 1)  
**Submission deadlines:** Interim Report Mon 1 Jun 2026 (Wk 7); Final Report Mon 10 Aug 2026 (Wk 17); Final Presentation 17–19 Aug 2026 (Wk 18)

---

## 0. How to use this document

This plan is deliberately redundant in two directions: the **project management spine** (Parts I, III, VI, VII, IX) is what keeps the degree assessment foolproof, and the **scientific spine** (Parts II, IV, V, VIII + Appendices) is what keeps the mathematics honest. Treat Part III as the weekly checklist you actually run your life by, and treat Parts II and IV as the intellectual commitments you've made to yourself about what you will understand, not just what you will submit.

Three ground rules:

1. **Every Sunday evening, read Part III for the upcoming week.** Write the Monday journal entry first thing, not last thing.
2. **Bi-weekly journals are free marks.** They are 10% of the grade for essentially zero intellectual cost beyond doing the work you were doing anyway. Missing one is the single most common way polytechnic design projects lose a grade band.
3. **The Interim Report at Week 7 is a gate, not a preview.** Everything upstream of Week 7 is designed so that on 1 June you submit a 2,500–3,500 word document that already contains: the full derivation of the governing PDE system, a validated numerical solver, and baseline simulation results matched against a literature benchmark (Elfving et al. 2021). The second half of the semester is then parametric sweeps and writing up. If you arrive at Week 7 without a working solver, the rest cascades.

---

## Part I — Project Charter

### 1.1 Problem statement

CO₂ capture by solid sorbents in packed-bed columns is viable at scale only if the thermal-swing regeneration cycle is both fast and energetically cheap. The regeneration performance depends on four directly controllable parameters — regeneration temperature T_regen, purge gas flow rate Q_purge, bed length L, and sorbent mass m — and on the internal physics of coupled heat and mass transfer with a nonlinear adsorption isotherm. Published parametric studies isolate one or two of these factors; a focused, mathematically rigorous study that simultaneously (i) derives the governing PDE system from first principles, (ii) implements a validated 1-D solver, (iii) performs systematic sensitivity sweeps across all four parameters, and (iv) interprets results through dimensionless groups and the Rankine–Hugoniot front-velocity prediction, is the scope of this Design Project.

### 1.2 Objectives and success criteria

| # | Objective | Success criterion | Evidence |
|---|---|---|---|
| O1 | Derive the coupled mass-energy PDE system for a 1-D packed-bed regeneration with a Langmuir isotherm and LDF kinetics, starting from first-principles conservation laws | Full derivation, with every term physically justified and every dimensionless group identified, appears as Ch. 3 of the Final Report | Final Report §3; oral defence Wk 18 |
| O2 | Implement the PDE solver in Python (method of lines + implicit time integration) and validate it against (a) an analytical linear case, (b) the Rankine–Hugoniot thermal front velocity, (c) the Elfving 2021 benchmark SER value of ~4.2 MJ/kg CO₂ at 60 °C TSA | Error < 5% vs analytical; front velocity within ±15% of R–H prediction; SER within ±20% of Elfving | Validation figures in Final Report §5 |
| O3 | Complete a full one-at-a-time (OAT) sensitivity sweep across T_regen (60–150 °C, 5 levels), Q_purge (3 levels), L (3 levels), m (3 levels), plus one 2-parameter interaction grid (T × Q) | 5+3+3+3+25 = 39 simulations with standardised outputs | Results Ch. of Final Report |
| O4 | Recast sensitivity results in dimensionless form and interpret via Pe, NTU, Λ, α, Bi_w | Response surface plotted in (Pe, NTU) space; ranked Pareto of the four physical parameters | Discussion Ch. |
| O5 | Submit assessment deliverables on time | Four bi-weekly journals, Interim Report (1 Jun), Final Report (10 Aug), Final Presentation (Wk 18) all submitted by deadline | NP LMS timestamps |

### 1.3 Scope — in and out

**In scope** (6-month Design Project):

- 1-D axial, non-isothermal packed-bed model (radial effects treated as a wall heat input term).
- Single-component CO₂ / purge gas mixture; Langmuir isotherm; linear driving force (LDF) kinetics.
- Numerical solution in Python (or MATLAB if Prof. Birgersson's group uses it) via method of lines + `scipy.integrate.solve_ivp` with a stiff integrator (BDF or LSODA).
- OAT sensitivity + one two-parameter interaction. Full central-composite DOE is deferred to FYP.
- Energy consumption computed as post-processing from the temperature solution (sensible heat + heat of desorption + ideal gas enthalpy) per Drechsler & Agar (2020) framework.
- Literature benchmarking against Elfving et al. (2021), Bos et al. (2018), and Serna-Guerrero et al. (2010).

**Out of scope** (for this Design Project; belongs to the 30-credit FYP):

- Wet-lab experiments on the SUTD rig. *However*, if Prof. Birgersson can provide one or two existing breakthrough/regeneration runs from the group archive, those will be used as a model-vs-experiment check in the Discussion chapter. This is a stretch goal, not a commitment.
- 2-D axi-symmetric model with explicit radial temperature gradients.
- Pressure drop via Ergun equation (included as a Future Work note only).
- Multi-component isotherms (Toth, Sips), water co-adsorption, or amine degradation.
- Bayesian inverse problem for parameter estimation (Future Work).
- Optimal transport / Wasserstein analysis — interesting, but an enrichment reading, not a deliverable.

### 1.4 Stakeholders and RACI

| Stakeholder | Role | R / A / C / I |
|---|---|---|
| You (student) | Deriver, coder, experimentalist, writer | **R** for everything; **A** for timeline |
| Prof. Parapsorb Borisut | Institution supervisor (sorbent chemistry, benchmark data) | **A** for scientific correctness; **C** on isotherm parameters |
| Prof. Erik Birgersson | Institution supervisor (transport modelling, numerical methods) | **A** for mathematical/numerical correctness; **C** on solver design |
| NP supervisor (TBC Wk 1) | Academic oversight, assessment, panel | **A** for assessment file; **I** on weekly progress |
| Panel (Wk 18) | Final presentation assessors | **I** |

### 1.5 Deliverables map against assessment (total 100%)

| Wk | Deliverable | Due date | Weight | Owner of assessment |
|---|---|---|---|---|
| 3 | Bi-weekly Journal #1 | Mon 4 May 2026 | 2.5% | NP |
| 5 | Bi-weekly Journal #2 | Mon 18 May 2026 | 2.5% | NP |
| 7 | **Interim Report** | Mon 1 Jun 2026 | 10% | NP / Institution |
| 7–8 | Interim Review & Assessment | 1–5 Jun 2026 | 20% + 10% | Institution (20%) + NP (10%) |
| 13 | Bi-weekly Journal #3 | Mon 13 Jul 2026 | 2.5% | NP |
| 15 | Bi-weekly Journal #4 | Mon 27 Jul 2026 | 2.5% | NP |
| 17 | **Final Report** | Mon 10 Aug 2026 | 10% | NP / Institution |
| 18 | Final Assessment | 17–19 Aug 2026 | 20% + 10% | Institution (20%) + NP (10%) |
| 18 | Final Presentation (panel) | 17–19 Aug 2026 | 10% | Panel |
|   | **Total** |   | **100%** |   |

Observation: 60% of the grade sits in the two Assessment Files filled by your institution and NP supervisors (Wk 7–8 and Wk 18). Those files are filled against *the quality of your journals, reports and demonstrated understanding in meetings*. Therefore the journal entries (10% line item) are leveraged at ~6× that weight through their influence on the supervisors' impression during assessment. Write them seriously.

---

## Part II — Experimental Design Framework (Experiment-Tracker layer)

### 2.1 Master research question

> *How do regeneration temperature, purge gas flow rate, bed length, and sorbent mass individually and jointly shape the axial temperature profile and energy consumption of a thermal-swing regeneration cycle in a 1-D packed-bed CO₂ adsorption column — and to what extent is this behaviour predicted from first principles by the Rankine–Hugoniot thermal-front condition and the governing dimensionless groups (Pe, NTU, Λ, α, Bi_w)?*

### 2.2 Sub-hypotheses

Each maps onto one of the five sub-topics identified in the literature review (`research.md`) and to one of the seven anchor sources. A sub-hypothesis is accepted/rejected/refined based on the sweep results + benchmark agreement.

| H# | Sub-topic | Hypothesis | Primary anchor source | Accept / refine threshold |
|---|---|---|---|---|
| **H1** | Regeneration temperature | Raising T_regen from 60 → 120 °C more than doubles the initial desorption rate while raising working capacity by ≥ 20%. Above ~120 °C, returns diminish as equilibrium asymptote is approached. | Bos et al. 2018; Serna-Guerrero et al. 2010 | Rate ratio > 2.0; Δcapacity > 20% |
| **H2** | Purge gas flow rate | SER (MJ/kg CO₂) versus Q_purge exhibits a **minimum** between 100–500 mL/min (at fixed T); below the minimum, equilibrium pinches recovery; above, parasitic purge-heating cost dominates. | Elfving et al. 2021 | A local minimum exists in the SER(Q_purge) curve |
| **H3** | Bed height / sorbent mass (length) | Front velocity is independent of L; breakthrough time scales linearly in L; MTZ width grows as ~L^(1/2) / Pe. | Hanh et al. 2024; Zanco et al. 2022 | v_front vs L slope < 5% of mean; t_BT slope within 10% of linear fit |
| **H4** | Bed height / sorbent mass (mass) | Sensible heat demand Q_sens scales linearly with m_sorbent; total SER has an **optimum** m because working capacity saturates while sensible heat keeps growing. | Zanco et al. 2022; Drechsler & Agar 2020 | Linear Q_sens fit R² > 0.98; an interior minimum of SER(m) is observed |
| **H5** | Axial temperature profile | The measured thermal-front velocity in the simulation matches the Rankine–Hugoniot prediction v_th = u / (1 + (1−ε)ρ_p c_ps / (ε ρ_g c_pg)) — adjusted for heat of adsorption feedback — within ±15%. | Marx et al. 2016; Zanco et al. 2022 | |v_sim − v_RH| / v_RH < 0.15 |

Each of H1–H5 will receive its own subsection in the Results chapter and a one-line verdict (**accept / refine / reject**) in the Conclusions.

### 2.3 Metrics

| Tier | Metric | Symbol | Units | Source |
|---|---|---|---|---|
| Primary | Thermal front velocity | v_th | m/s | From T(z,t) simulation: slope of the 50%-front isotherm in (z,t) plane |
| Primary | Time to complete regeneration (T_out reaches 95% of T_regen) | τ_90 | s | T_out(t) trace |
| Primary | Peak bed temperature | T_peak | °C | max over (z, t) |
| Secondary | Working capacity | Δq | mol/kg | q_initial − q_final |
| Secondary | Specific energy requirement | SER | MJ/kg CO₂ | ∫Q_wall dt / (Δq · m_sorbent · M_CO₂) |
| Secondary | CO₂ recovery fraction | η_rec | — | n_CO₂,out / n_CO₂,initially-loaded |
| Guardrail | CFL stability (explicit parts) | CFL | < 1 | u·Δt/Δz |
| Guardrail | Mass balance drift over a cycle | ε_m | < 1% | |Σ in − Σ out − ΔInventory| / Σ in |
| Guardrail | Energy balance drift over a cycle | ε_E | < 2% | same for energy |

### 2.4 Parametric sweep matrix (pre-committed before running anything)

**Baseline** (mirrors Elfving et al. 2021 for benchmarking):

| Parameter | Baseline value | Rationale |
|---|---|---|
| T_regen | 100 °C | midpoint between Elfving's 60 and ~140 °C |
| Q_purge | 100 mL/min (N₂) | Elfving mid-range |
| L | 15 cm | Typical lab-scale column |
| d_c | 2.0 cm | TBC from SUTD rig |
| m_sorbent | 20 g | Sets ε, bed voidage |
| T_in | 25 °C | Ambient inlet before heat-up |
| q_initial | saturated at 400 ppm, 25 °C | Simulates DAC loading |

**OAT sweep levels:**

| Parameter | Level 1 (low) | Level 2 | Level 3 (base) | Level 4 | Level 5 (high) |
|---|---|---|---|---|---|
| T_regen (°C) | 60 | 80 | **100** | 120 | 150 |
| Q_purge (mL/min) | 40 | **100** | 500 | — | — |
| L (cm) | 7.5 | **15** | 30 | — | — |
| m_sorbent (g) | 10 | **20** | 50 | — | — |

→ **14 OAT simulations** (5 T + 3 Q + 3 L + 3 m, with the baseline shared).

**Two-parameter interaction (T × Q):** 5 × 3 = 15 simulations → covers full factorial in the two most sensitive parameters (H1, H2).

**Total simulation budget:** 14 OAT + 15 interaction + ~10 validation/diagnostic = **~39 runs**. At ~2–5 min per simulation on a laptop (1-D, 200 grid points, LSODA), this fits comfortably in Weeks 8–14 with margin for reruns.

### 2.5 Benchmark datasets

| Benchmark | Source | What we match | Tolerance |
|---|---|---|---|
| Analytical advection-diffusion step response | Carslaw & Jaeger; Evans PDE | T(z,t) under zero adsorption | error < 1% |
| SER at 60 °C TSA, no purge | Elfving 2021, Table / Fig. | 4.2 MJ/kg CO₂ | ±20% |
| Working capacity lift from 0.47 → 0.51 mmol/g when mild vacuum is added | Elfving 2021 | Directional | direction only |
| Desorption rate doubling between 80 → 150 °C | Bos 2018 | k_des(T) Arrhenius | ±30% |
| Thermal front velocity from Rankine–Hugoniot | Marx 2016, Zanco 2022 | v_th | ±15% |

### 2.6 Validation protocol (mandatory before any production sweep)

Three gates, each must pass before moving on:

1. **Gate A — Linear validation (Wk 4):** solve ∂T/∂t + u ∂T/∂z = α ∂²T/∂z² with a step inlet; compare to the analytical Gaussian-broadening solution. Pass: L² error < 1% on a 200-node grid.
2. **Gate B — Nonlinear front validation (Wk 5–6):** solve isothermal Langmuir + LDF; verify the breakthrough-front velocity matches the Rankine–Hugoniot chord formula. Pass: |v_sim − v_RH| / v_RH < 10%.
3. **Gate C — Elfving benchmark (Wk 6):** reproduce SER ≈ 4.2 MJ/kg at the TSA-60 condition. Pass: |SER_sim − 4.2| / 4.2 < 20%.

**No parametric sweeps start until Gates A–C pass.** This is the single most important rule in the schedule; skipping it is how simulation projects produce prolific plots of garbage.

---

## Part III — 18-Week Master Plan (aligned exactly to the NP timeline)

Legend:  **DELIV** = hard deliverable; **GATE** = technical gate; **M** = math-learning anchor; **T** = technical/coding work; **W** = writing.

| Wk | Dates | Phase | M (math/theory) | T (technical) | W (writing) | DELIV / GATE |
|---|---|---|---|---|---|---|
| **1** | 20–24 Apr | P0 Kickoff | First-order quasilinear PDE (Evans Ch 3.1–3.2); method of characteristics | Install Python / `numpy` `scipy` `matplotlib`; clone a 1-D heat equation solver as starter template; read all 7 sources in `research.md` | Set up LaTeX report skeleton; compile parameter tables from Elfving + Bos; draft project charter (Part I above) | **Wk-1 briefing + 1st supervisor meeting** |
| **2** | 27 Apr–1 May | P1 Model derivation | Nonlinear conservation laws, Rankine–Hugoniot, entropy condition (Evans Ch 3.4; LeVeque Ch 3) | Derive the 4-PDE coupled system from a CV mass/energy balance — write every line; identify every parameter with units | Write "derivation from first principles" subsection (goes into Interim §3) | — |
| **3** | 4–8 May | P1 Non-dim | Buckingham Π; scaling analysis | Non-dimensionalise; identify Pe, NTU, Λ, α, Bi_w; tabulate expected order of magnitude for SUTD geometry | Write "dimensionless analysis" subsection | **DELIV: Journal #1 — Mon 4 May** |
| **4** | 11–15 May | P2 Linear solver | Method of lines; stiff ODE integration (BDF2, LSODA) | Python 1-D heat eqn MOL solver; validate vs analytical Gaussian kernel | Validation figure #1 (draft) | **GATE A: linear solver < 1% err** |
| **5** | 18–22 May | P2 Nonlinear coupled solver | LDF kinetics; upwind differencing; why upwind ≡ entropy condition numerically | Add Langmuir + LDF; full 4-PDE coupled system; sanity check: zero-heat-input should recover isothermal breakthrough | Draft "numerical methods" chapter | **DELIV: Journal #2 — Mon 18 May** |
| **6** | 25–29 May | P2 Benchmark + Interim draft | Heat-of-adsorption feedback in the thermal front velocity formula | Baseline simulation at Elfving conditions; compute v_th, SER, Δq; first benchmark comparison; fix bugs | **Draft the entire Interim Report** (target 2,500–3,500 words) | **GATE B + C: R-H within 15%; SER within 20%** |
| **7** | 1–5 Jun | Interim gate | — | Address any validation gaps found during Interim Review | Polish and submit Interim; prepare 10-min slide deck | **DELIV: Interim Report — Mon 1 Jun; Interim Review Wk 7–8** |
| **8** | 8–12 Jun | P3 Sensitivity Part 1 | Sensitivity equations: differentiate the PDE wrt a parameter → linear PDE for ∂T/∂θ | OAT sweep on T_regen (5 levels) and Q_purge (3 levels); save all profiles to `.npz` | Running "Results" log in the report | — |
| 9–10 | 15–28 Jun | **Term Break** | Optional: read 1 ch. of LeVeque or Villani for pleasure; don't burn out | — | — | — |
| **11** | 29 Jun–3 Jul | P3 Sensitivity Part 2 | Local equilibrium limit → hyperbolic reduction; how the full parabolic system tends to it as NTU → ∞ | OAT on L (3 levels) and m (3 levels); extract v_th, τ_90, T_peak, Δq, SER for each | Add to Results log | — |
| **12** | 6–10 Jul | P4 Energy analysis | Drechsler & Agar (2020) energy decomposition: Q_sens + Q_des + Q_parasitic | Post-process all runs for SER; break into components; plot SER vs each parameter | Draft "Energy analysis" subsection | — |
| **13** | 13–17 Jul | P4 Interaction study | Response-surface fitting (quadratic); sensitivity ranking via dimensionless groups | T × Q 5×3 grid (15 runs); fit quadratic response surface; plot contour | Revise Methods + add Interaction Results | **DELIV: Journal #3 — Mon 13 Jul** |
| **14** | 20–24 Jul | P5 Dimensionless recast | Recast each OAT result in (Pe, NTU, Λ) coordinates; universal plots | Generate dimensionless response plots; rank parameters by ∂(output)/∂(log Π_i) | Discussion draft: physical interpretation via dimensionless groups | — |
| **15** | 27–31 Jul | P6 Writing Sprint 1 | — | Clean code, reproducibility check, figure finalisation (all figures ≥ 300 dpi, consistent style) | **Draft full Final Report v0.5**; share with both supervisors for feedback | **DELIV: Journal #4 — Mon 27 Jul** |
| **16** | 3–7 Aug | P6 Writing Sprint 2 | — | Rerun any sensitivity cell requested by supervisors | Final Report v1.0 — incorporate feedback, final proofread, format-check | — |
| **17** | 10–14 Aug | P7 Submit + prep | — | — | **Submit Final Report Mon 10 Aug**; build slide deck; 2 rehearsals | **DELIV: Final Report — Mon 10 Aug** |
| **18** | 17–19 Aug | P7 Defence | — | — | Slide revision after dry-run | **DELIV: Final Presentation + panel Q&A** |

### Critical path

The critical path runs: **Wk 1 read → Wk 2–3 derive + non-dim → Wk 4 Gate A → Wk 5 Gate B → Wk 6 Gate C + interim draft → Wk 7 submit**. If any Gate slips by more than 3 days, re-baseline immediately: the term break (Wk 9–10) contains zero schedule slack, and Wk 15–16 are already writing-constrained. Do not attempt to buy back slipped Gates by working during term break — empirically that backfires as burnout. Buy it back by descoping sweep levels (drop L and m to 2 levels each).

---

## Part IV — Mathematical Learning Track

Paired weekly with the technical work. The goal is that by Week 17, the Final Report can stand on its mathematical chapter alone as a coherent exposition — not a parts catalog.

| Wk | Math topic | Why it matters here | Canonical reading | Exercise (min. 3 worked problems) |
|---|---|---|---|---|
| 1 | Method of characteristics for linear first-order PDE | Warm-up; prerequisite for nonlinear case | Evans §3.1; Strauss §14.1 | Solve u_t + c(x) u_x = 0 for three c(x); draw characteristics |
| 2 | Quasilinear first-order; shock formation; Rankine–Hugoniot; Lax entropy condition | The nonlinear wave theory that makes your breakthrough / thermal front predictable | Evans §3.4; LeVeque Ch 3 | Inviscid Burgers with two initial profiles; compute breaking time; derive R–H |
| 3 | Dimensional analysis & Π theorem | Universalises the parametric study — your results become portable | Bird/Stewart/Lightfoot Ch 6; Barenblatt — Scaling | Non-dim the 4-PDE system yourself, by hand, on paper |
| 4 | Method of lines + stiff ODE theory | Underpins the entire solver | Ascher & Petzold, *CompDE*; `scipy` docs for `solve_ivp` | Code the heat eqn MOL + compare RK4 vs LSODA step counts |
| 5 | Upwind schemes; numerical diffusion; CFL | Why an inappropriate scheme will fake shocks or smear them | LeVeque Ch 6–7 | Solve linear advection at CFL = 0.5, 1.0, 1.1; observe |
| 6 | Heat of adsorption coupling; modified wave speed; Clausius–Clapeyron | Closes the loop between thermodynamics and PDE | Ruthven Ch 8; Do Ch 3 | Derive v_th formula with heat feedback term |
| 7 | — (buffer for report) | — | — | — |
| 8 | Sensitivity equations; forward sensitivity analysis | Lets you say "∂τ_90 / ∂T_regen = X" with a number, not an eyeball | Cacuci, *Sensitivity and Uncertainty*, Ch 1 | Hand-derive the sensitivity PDE for one parameter |
| 11 | Local equilibrium limit; singular perturbation in NTU | Explains the sharp-front vs spread-front transition | Ruthven Ch 8; Kevorkian & Cole | Show that NTU → ∞ collapses the parabolic system to a hyperbolic one |
| 12 | Energy decomposition and exergy | Separates "thermodynamically unavoidable" from "engineering waste" | Drechsler & Agar 2020; Kotas, *Exergy Method* Ch 3 | Compute ΔG of desorption vs SER — the ratio is second-law efficiency |
| 13 | Response surface methodology; quadratic polynomial fits | Lets you summarise 15 simulations as an analytical function | Montgomery, *DOE* Ch 11 | Fit y = β₀ + Σβᵢxᵢ + Σβᵢⱼxᵢxⱼ + Σβᵢᵢxᵢ² to synthetic data |
| 14 | Rescaling results into (Pe, NTU, Λ, α, Bi_w) space; sensitivity ranking via logarithmic derivatives | Final universalisation step | Kuzmin, *A Guide to Numerical Methods*; any advanced transport text | Rank sensitivity ∂(log y)/∂(log Π) for each dimensionless group |
| 15–18 | — | — | — | — |

**Enrichment (optional, if time permits — do *not* let these crowd out deliverables):**

- Villani, *Topics in Optimal Transport*, Ch 1 — connects to the multi-marginal transport paper in your library.
- LeVeque, *Numerical Methods for Conservation Laws* Ch 14 — Riemann problems if you want a clean view of where the front-propagation theory sits.
- Evans Ch 5 — Sobolev spaces; only if you truly love this and the core project is on track.

---

## Part V — Literature anchor map

How the seven sources from `research.md` plug into the project:

| Source | Sub-topic served | Used for | Week first referenced |
|---|---|---|---|
| **Bos et al. 2018** (I&EC Res) | H1 (T_regen), H2 (Q_purge) | Justification for T_regen 60–150 °C sweep range; comparison for desorption-rate-vs-T trend | 2 (parameter ranges) |
| **Elfving et al. 2021** (Chem Eng J) | H1, H2, energy (Part of Ch 3, 5) | **Primary benchmark** — apparatus geometry, 60 °C SER = 4.2 MJ/kg, 40 / 1000 mL/min purge comparison | 6 (Gate C) |
| **Serna-Guerrero et al. 2010** (CES) | H1, H2 | Statistical-significance framing: "temperature dominant on rate; all three on capacity" — sets the expected *directions* of H1, H2 | 8 (sensitivity interpretation) |
| **Zanco et al. 2022** (Chem Eng J) | H3, H4, H5 | Template for axial/radial T-profile interpretation; packed foams comparison as a future-work sidebar | 11 (L, m sweep) |
| **Marx et al. 2016** (I&EC Res) | H5 | **Primary benchmark** for 1-D non-isothermal model calibration; supplies heat-transfer coefficient reference values | 6 (Gate B); 14 (discussion) |
| **Hanh et al. 2024** (J Taiwan IChE) | H3 | MTZ / ABU / AER breakdown for the L sweep discussion | 11, 14 |
| **Drechsler & Agar 2020** (I&EC Res) | Energy | **Framework** for decomposing SER into Q_sens + Q_des + Q_parasitic | 12 (energy ch.) |

Your existing library (from `sources_csv.xlsx`) supplies the provided papers — *Fixed-bed column adsorption of CO₂*, *Enhancing CO₂ Adsorption via Amine Impregnated AC*, plus the math papers (*Reducing Nonlinear Transport Equations to Laplacians*, *Nonlinear Systems Coupled through Multi-Marginal Transport*, etc.). These cover: (a) your primary sorbent characterisation for isotherm parameters, and (b) the mathematical context. The seven new sources listed in `research.md` are the engineering anchors; the provided papers are the chemistry and mathematics anchors.

**Gap analysis / what's still missing and must be obtained at Wk 1:**

1. Sorbent-specific Langmuir parameters (q_m0, b_0, ΔH_ads) — must come from SUTD / Prof. Borisut or Prof. Birgersson. Placeholder literature value for now: q_m0 ≈ 2–3 mol/kg, ΔH_ads ≈ 70–90 kJ/mol for amine-functionalised silica.
2. Column geometry (d_c, L, heating element wattage, thermocouple positions) — **ask in Wk-1 meeting**.
3. Sorbent particle density ρ_p, bed voidage ε, particle diameter d_p — **ask in Wk-1 meeting**.

---

## Part VI — Risk Register

High-impact risks are listed first. Every risk has a *trigger* (a specific signal that tells you the risk is materialising) and a *response* (the concrete action to take).

| # | Risk | Likelihood | Impact | Trigger | Response |
|---|---|---|---|---|---|
| R1 | Numerical solver fails Gate A (linear validation) by end of Wk 4 | Medium | High | `scipy.solve_ivp` outputs diverge or L² error > 1% | Drop to Crank–Nicolson finite difference in hand-coded form; consult Birgersson in office hours; 3-day buffer built in |
| R2 | SUTD does not provide sorbent / geometry parameters by end of Wk 2 | Medium | High | No email reply by end of Wk 2 | Proceed with Elfving 2021 literature defaults as placeholders; document this clearly in Interim; escalate to NP supervisor |
| R3 | Time overrun on derivation chapter → Interim Report late | Medium | Critical (−10% + supervisor confidence) | Wk 6 Friday and interim draft < 1500 words | Submit a tighter scope: cover only H1 and H2 in the Interim; finish others by Wk 13 |
| R4 | Ill-posed Langmuir parameter fit — solver blows up near pinch points | Low | Medium | Solver rejects steps; stiff integrator goes to zero step size | Regularise isotherm: cap b(T) at a lower bound; use `atol`/`rtol` tuning |
| R5 | Scope creep into 2-D / Bayesian / experimental work | High | Medium | You find yourself reading Villani on a Wednesday morning | Part I §1.3 "Out of scope" is the answer; bookmark for FYP |
| R6 | Burnout in Wk 11–13 after the term break | Medium | Medium | Journal #3 is late or thin; weekend work exceeds 12 h | Cut one interaction-grid point (go 4×3 not 5×3); call NP supervisor |
| R7 | Laptop / code-loss catastrophe | Low | Catastrophic | — | **Push every commit to GitHub nightly**; weekly Google Drive backup of `.ipynb` + `.npz` results |
| R8 | Panel presentation overruns / Q&A fumble | Medium | Medium | Dry-run clocks > 22 min | Two full rehearsals minimum; record yourself once; the first slide is a *physical* picture of the column, not equations |
| R9 | Misaligned supervisor expectations (SUTD vs NP) | Low | High | A supervisor is surprised by project direction in Wk 7 | Monthly 30-min joint update email to both SUTD supervisors + NP supervisor with one-page status (use Part IX template) |

---

## Part VII — Bi-weekly Journal template

Each journal is ~400–600 words, Markdown, 4 sections. Submit by Monday 23:59.

```markdown
# Journal #N — Week X (dd Mmm 2026)

## 1. What I did this period
- [bullet, concrete, verb-first — "Derived the dimensionless form of the gas-phase mass balance, identifying five governing groups."]
- [include code commit links where relevant]

## 2. What I learned
- [mathematical/physical insight — this is where your mathematics-first philosophy shows up]
- [brief derivation or diagram if the insight is visual]

## 3. Blockers and questions
- [be honest; supervisors value this more than smoothed narratives]
- [name the person whose answer would unblock each item]

## 4. Plan for next period
- [3–5 concrete items matching Part III of the master plan for the upcoming week]
- [any scope-change flag]
```

### Topic anchors per journal

| Journal | Target content |
|---|---|
| #1 (4 May, Wk 3) | Mathematical foundation: method of characteristics worked; PDE system derived; Π-groups identified; first solver skeleton coded. |
| #2 (18 May, Wk 5) | Linear solver passes Gate A; nonlinear LDF + Langmuir coupled; first breakthrough curve plotted; Rankine–Hugoniot prediction for v_th computed by hand. |
| #3 (13 Jul, Wk 13) | Mid-sweep status: OAT complete for T_regen and Q_purge; sensitivity directions confirm H1 and H2; interaction grid design finalised. |
| #4 (27 Jul, Wk 15) | Dimensionless recast of all results; response surface fitted; Final Report v0.5 circulated to supervisors. |

---

## Part VIII — Report Scaffolds

### Interim Report (Mon 1 June, Wk 7) — target 2,500–3,500 words

1. **Introduction & motivation** (~300 w) — global CO₂ context; specific scope; sub-hypotheses H1–H5 stated.
2. **Governing equations — derived** (~800 w) — four-PDE system derived from CV; Langmuir; LDF; **write every line**.
3. **Dimensional analysis** (~400 w) — full non-dim; five Π groups with typical values for SUTD rig.
4. **Numerical methods & validation** (~700 w) — MOL; stiff integrator; Gates A, B, C passed with figures.
5. **Baseline simulation & benchmark** (~600 w) — Elfving comparison; SER, Δq, v_th reported; numbers tabulated.
6. **Work plan for weeks 8–17** (~300 w) — sensitivity + interaction + energy + write-up, with dates.

### Final Report (Mon 10 Aug, Wk 17) — target 6,000–8,000 words

1. Abstract (200 w)
2. Introduction (500 w) — including a section titled *Why the mathematics of this system is the engineering of this system*, which is the Poincaré-inspired subsection your study plan (Ch 7) already sketched.
3. Literature Review (800 w) — structured by sub-topic (H1–H5), each closing with "What is known / what the present work adds".
4. Governing equations — derived (1,000 w) — expanded from Interim; include dimensional analysis.
5. Numerical methods (700 w) — include MOL, upwind, stability, verification plots.
6. Parametric sensitivity study (1,800 w) — H1 → H2 → H3 → H4 subsections; each figure captioned with the accept/refine verdict.
7. Axial temperature profile & Rankine–Hugoniot comparison (700 w) — this is where the "mathematical insight" shines; H5 result.
8. Energy analysis (500 w) — Q_sens / Q_des / Q_parasitic breakdown; optimal m discussion.
9. Discussion — dimensionless recast (600 w) — universal plots in (Pe, NTU) space; parameter ranking.
10. Conclusions (400 w) — verdict on H1–H5; what it means for scale-up; limitations.
11. Future work — one page — 2-D model, experimental campaign, Bayesian inverse problem, Wasserstein lower bound on regeneration energy.
12. References (30–50 entries) + appendices (code listings, full result tables).

---

## Part IX — Weekly Operating Rhythm

### Daily

- **09:00** — read one page of the week's math anchor reading. Non-negotiable; 15 minutes.
- **End of day** — commit code to GitHub with a meaningful message ("Closed Gate A: linear heat eqn MOL validated against Gaussian kernel, L² = 0.4%"), even on non-coding days.

### Weekly

| Day | Block |
|---|---|
| Mon | 09:00–10:30 Math theory (Evans / LeVeque) |
| Tue | 14:00–15:00 Physical-chemistry reading (Ruthven / one journal paper) |
| Wed | 10:00–12:00 Coding sprint (one feature or one validation gate per session) |
| Thu | 14:00–15:00 Literature: read one `research.md` source end-to-end; add 3 lines to running annotated bibliography |
| Fri | 14:00–15:00 Integration note — 400–600 words connecting the week's math to the week's code. Feeds directly into the next journal. |
| Sat | 2–3 h extended coding/analysis (optional; skip without guilt during term break) |
| Sun | 30 min — read Part III for next week; write Monday's journal (or draft its opening) |

### Monthly

- Last Friday of each month — one-page status email to Prof. Borisut + Prof. Birgersson + NP supervisor. Template below.

```markdown
Subject: [CO2 Sorbent Regen — Month M status] <headline, 1 line>

Status colour: 🟢 on-track / 🟡 at-risk / 🔴 blocked

Done this month:
- …

Upcoming next month:
- …

Risks and decisions needed:
- …

Deliverables in the next 4 weeks:
- …
```

A single consistent monthly message, received on the same day each month, is the cheapest piece of project-management infrastructure you will ever buy.

---

## Appendix A — Governing equations (quick reference)

Gas-phase CO₂ mass balance:

    ε ∂C/∂t = −u ∂C/∂z + D_ax ∂²C/∂z² − k_a a_p (1−ε)(C − C*)

Solid-phase mass balance (LDF):

    (1−ε) ρ_p ∂q/∂t = k_a a_p (1−ε)(C − C*)

Gas energy balance:

    ε ρ_g c_pg ∂T_g/∂t = −ρ_g c_pg u ∂T_g/∂z + λ_ax ∂²T_g/∂z² + h_f a_p (T_s − T_g) + Q_wall

Solid energy balance:

    (1−ε) ρ_p c_ps ∂T_s/∂t = h_f a_p (T_g − T_s) + (−ΔH_ads) ρ_p (1−ε) ∂q/∂t

Closure — Langmuir isotherm with T-dependent constants:

    q* = q_m(T) · b(T) · C / [1 + b(T) C]
    q_m(T) = q_m0 · exp(χ/T),   b(T) = b_0 · exp(ΔH_ads / (RT))

Rankine–Hugoniot thermal-front velocity (ignoring heat of adsorption feedback for the first estimate):

    v_th = u · ρ_g c_pg / [ρ_g c_pg + (1−ε)/ε · ρ_p c_ps]

---

## Appendix B — Dimensionless groups

| Group | Definition | Typical | Meaning |
|---|---|---|---|
| Pe | u L / D_ax | 10–500 | convective vs dispersive transport |
| NTU | k_a a_p L (1−ε) / (ε u) | 1–20 | mass-transfer rate vs convective residence time |
| Pe_h | ρ_g c_pg u L / λ_ax | 10–200 | thermal convective vs conductive |
| Λ | (−ΔH) q_m / (c_pg T_ref) | 0.1–1 | heat-of-adsorption feedback strength |
| α | ρ_p (1−ε) q_m / (ε C_0) | 1–100 | solid-phase vs gas-phase capacity |
| Bi_w | h_w · (4/d_c) / (ρ_g c_pg u) | 0.01–0.5 | wall heating vs convective sweep |

---

## Appendix C — Python solver scaffold (Week 4–5)

```python
# Repo: github.com/<you>/co2-regen-design-proj
# File: solver/pde_mol.py

import numpy as np
from scipy.integrate import solve_ivp

# ---- Parameters (load from yaml / supervisor inputs) ----
eps, rho_p, rho_g = 0.4, 1200.0, 1.2
c_pg, c_ps = 1040.0, 900.0
u, L, d_c = 0.05, 0.15, 0.02
D_ax, lam_ax = 1e-4, 0.2
k_a, a_p = 0.1, 1.5e4
h_f, h_w = 50.0, 30.0
dH_ads = 75e3                # J/mol
q_m0, b0 = 2.5, 1e-5
chi, T_ref = 0.0, 298.15

N = 200
z = np.linspace(0, L, N)
dz = z[1] - z[0]

def langmuir(C, T):
    b = b0 * np.exp(dH_ads / (8.314 * T))
    q_m = q_m0 * np.exp(chi / T)
    return q_m * b * C / (1 + b * C)

def rhs(t, y):
    C, q, Tg, Ts = np.split(y, 4)
    # First-order upwind for convection; central for diffusion
    dCdz = np.zeros_like(C); dTdz = np.zeros_like(Tg)
    dCdz[1:]  = (C[1:] - C[:-1]) / dz
    dTdz[1:]  = (Tg[1:] - Tg[:-1]) / dz
    d2Cdz2 = np.zeros_like(C);  d2Tdz2 = np.zeros_like(Tg)
    d2Cdz2[1:-1] = (C[2:] - 2*C[1:-1] + C[:-2]) / dz**2
    d2Tdz2[1:-1] = (Tg[2:] - 2*Tg[1:-1] + Tg[:-2]) / dz**2

    C_star = inverse_langmuir(q, Ts)   # implemented separately
    rate   = k_a * a_p * (C - C_star)

    dCdt = (-u*dCdz + D_ax*d2Cdz2 - rate*(1-eps)) / eps
    dqdt = rate / rho_p
    dTgdt = (-rho_g*c_pg*u*dTdz + lam_ax*d2Tdz2
             + h_f*a_p*(Ts - Tg) + Q_wall(z, t)) / (eps*rho_g*c_pg)
    dTsdt = (h_f*a_p*(Tg - Ts) + dH_ads*rho_p*(1-eps)*dqdt) / ((1-eps)*rho_p*c_ps)

    # Inlet BC (Dirichlet via strong form on i=0)
    dCdt[0] = 0.0;  dTgdt[0] = 0.0
    return np.concatenate([dCdt, dqdt, dTgdt, dTsdt])

# Initial condition: saturated at 400 ppm, ambient; purge starts at t=0
y0 = np.concatenate([np.full(N, 0.0),         # gas-phase C at inlet-purge = 0
                     np.full(N, q_sat_400ppm),
                     np.full(N, 298.15),
                     np.full(N, 298.15)])

sol = solve_ivp(rhs, (0, 1200), y0, method='LSODA',
                rtol=1e-6, atol=1e-9, t_eval=np.linspace(0, 1200, 241))
```

The snippet above is a scaffold, not working production code. Expect to spend Weeks 4–5 turning this into a Gate-A-passing implementation.

---

## Appendix D — Prioritised reading list

**Tier 1 — read in Week 1, referred to throughout:**
- Evans, *PDE* — Ch 3 (first-order equations) in full.
- LeVeque, *Numerical Methods for Conservation Laws* — Ch 3 (scalar laws), Ch 6–7 (upwind).
- Ruthven, *Principles of Adsorption and Adsorption Processes* — Ch 6, 8.
- Elfving et al. 2021 *Chem Eng J* 404, 126337 — **main benchmark**.
- Bos et al. 2018 *I&EC Res* 57, 11141 — regeneration options.

**Tier 2 — reference when topic arrives:**
- Serna-Guerrero et al. 2010 *CES* 65, 4166 — factorial DOE direction.
- Marx et al. 2016 *I&EC Res* 55, 1401 — 1-D non-isothermal calibration.
- Zanco et al. 2022 *Chem Eng J* 430, 131000 — axial T template.
- Hanh et al. 2024 *J Taiwan IChE* 164, 105681 — MTZ.
- Drechsler & Agar 2020 *I&EC Res* 59, 9207 — energy breakdown.
- Bird/Stewart/Lightfoot, *Transport Phenomena* Ch 6, 11, 14.

**Tier 3 — enrichment (only if on-track):**
- Villani, *Topics in Optimal Transport* — Ch 1.
- The three nonlinear-transport papers already in `sources_csv.xlsx` (*Laplacians*, *Multi-Marginal*, *Statistical Mechanics*).

---

*End of Foolproof Study Plan — version 1.0, 20 April 2026.*  
*Revision policy: update Part III and Part VI weekly, log every change in a changelog section appended to this file.*
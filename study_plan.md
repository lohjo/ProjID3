# Foolproof Study Plan

## Parametric Study of CO₂ Adsorption Breakthrough in Packed-Bed Columns

**Student:** Year 3, Diploma in Engineering Science (N93), Ngee Ann Polytechnic  
**Institution supervisors (SUTD/NUS):** Prof. Parapsorb Borisut, Prof. Erik Birgersson  
**NP supervisor:** TBC at Week-1 briefing  
**Project code:** ES Design Project (4 credits), April 2026 semester  
**Plan prepared:** Monday 20 April 2026 (Week 1, Day 1); **revised 30 April 2026 — scope change: regeneration → adsorption breakthrough**  
**Submission deadlines:** Interim Report Mon 1 Jun 2026 (Wk 7); Final Report Mon 10 Aug 2026 (Wk 17); Final Presentation 17–19 Aug 2026 (Wk 18)

---

## 0. How to use this document

This plan is deliberately redundant in two directions: the **project management spine** (Parts I, III, VI, VII, IX) is what keeps the degree assessment foolproof, and the **scientific spine** (Parts II, IV, V, VIII + Appendices) is what keeps the mathematics honest. Treat Part III as the weekly checklist you actually run your life by, and treat Parts II and IV as the intellectual commitments you've made to yourself about what you will understand, not just what you will submit.

Three ground rules:

1. **Every Sunday evening, read Part III for the upcoming week.** Write the Monday journal entry first thing, not last thing.
2. **Bi-weekly journals are free marks.** They are 10% of the grade for essentially zero intellectual cost beyond doing the work you were doing anyway. Missing one is the single most common way polytechnic design projects lose a grade band.
3. **The Interim Report at Week 7 is a gate, not a preview.** Everything upstream of Week 7 is designed so that on 1 June you submit a 2,500–3,500 word document that already contains: the full derivation of the governing PDE system, a validated numerical solver, and baseline simulation results matched against the Stampi-Bombelli 2024 breakthrough benchmark. The second half of the semester is then parametric sweeps and writing up. If you arrive at Week 7 without a working solver, the rest cascades.

---

## Part I — Project Charter

### 1.1 Problem statement

CO₂ capture by solid sorbents in packed-bed columns depends critically on the adsorption breakthrough dynamics: how the mass-transfer zone (MTZ) propagates through the bed, when the outlet concentration exceeds an acceptable threshold, and how operating conditions — superficial gas velocity u, inlet CO₂ concentration C_in, bed length L, and adsorption temperature T_ads — jointly determine the breakthrough time τ_BT and the fraction of sorbent capacity actually utilised η. Published parametric studies at DAC-relevant concentrations (400 ppm) are sparse; Stampi-Bombelli et al. (2024) is the first rigorous experimental dataset at this regime, using amine-functionalised γ-alumina in a packed-bed column with a fully characterised Toth isotherm. A mathematically grounded parametric study that (i) derives the coupled 1-D breakthrough PDE system from first-principles conservation laws, (ii) implements and validates a Method-of-Lines solver against analytical traveling-wave theory (Myers & Font 2020) and the Stampi-Bombelli benchmark, (iii) performs systematic OAT and interaction sweeps across all four controllable parameters, and (iv) recasts sensitivity results in (Pe, NTU) space is the scope of this Design Project.

### 1.2 Objectives and success criteria

| # | Objective | Success criterion | Evidence |
|---|---|---|---|
| O1 | Derive the coupled mass-energy PDE system for 1-D adsorption breakthrough with a Toth isotherm and LDF kinetics, starting from first-principles conservation laws | Full derivation, with every term physically justified and every dimensionless group identified, appears as Ch. 3 of the Final Report | Final Report §3; oral defence Wk 18 |
| O2 | Implement the PDE solver in Python (method of lines + implicit time integration) and validate against (a) analytical linear step response, (b) R-H adsorption shock chord velocity, (c) Stampi-Bombelli 2024 breakthrough curve at 400 ppm | Gate A: L² error < 1%; Gate B: \|v_sim − v_RH\|/v_RH < 10%; Gate C: τ_BT within ±20% of Stampi-Bombelli | Validation figures in Final Report §5 |
| O3 | Complete a full one-at-a-time (OAT) sensitivity sweep across u (3 levels), C_in (3 levels), L (3 levels), T_ads (3 levels), plus one 2-parameter interaction grid (u × C_in) | 11 OAT + 9 interaction + ~19 validation/diagnostic = ~39 simulations | Results chapter of Final Report |
| O4 | Recast sensitivity results in dimensionless form and interpret via Pe, NTU, α | Response surface plotted in (Pe, NTU) space; ranked Pareto of the four physical parameters | Discussion chapter |
| O5 | Submit all assessment deliverables on time | Four bi-weekly journals, Interim Report (1 Jun), Final Report (10 Aug), Final Presentation (Wk 18) all submitted by deadline | NP LMS timestamps |

### 1.3 Scope — in and out

**In scope** (6-month Design Project):

- 1-D axial, non-isothermal adsorption breakthrough model; radial effects neglected (adiabatic, Q_wall = 0).
- Single-component CO₂ / carrier gas (N₂ or air); Toth isotherm with temperature-dependent parameters from Stampi-Bombelli 2024; linear driving force (LDF) kinetics.
- Numerical solution in Python via Method of Lines + `scipy.integrate.solve_ivp` with stiff integrator (BDF or LSODA).
- Isothermal simplification (T_g = T_s = T_ads = const) used for Gate A and Gate B validation before the full non-isothermal run.
- Breakthrough metrics extracted as post-processing from C(z=L, t): τ_BT (C_out/C_in = 0.05), τ_sat (C_out/C_in = 0.95), MTZ width W_MTZ, stoichiometric utilisation η, dynamic capacity q_dyn.
- OAT sensitivity + one two-parameter interaction (u × C_in). Full central-composite DOE deferred to FYP.
- Literature benchmarking against Stampi-Bombelli et al. (2024) and Myers & Font (2020). Concentration-range checks against Chen et al. (2023).

**Out of scope** (belongs to the 30-credit FYP):

- Wet-lab experiments on the SUTD rig. If Prof. Birgersson's group can provide an existing breakthrough run, it will be used as a model-vs-experiment stretch check — not a commitment.
- Cyclic simulation (repeated adsorption + regeneration cycles). The focus here is the adsorption half-cycle only.
- 2-D axi-symmetric model with explicit radial temperature or concentration gradients.
- Pressure drop via Ergun equation (Future Work note only).
- Multi-component isotherms (humidity co-adsorption). Dry feed assumed throughout.
- Bayesian inverse problem for parameter estimation (Future Work).
- Wasserstein / optimal-transport analysis — enrichment reading, not a deliverable.

### 1.4 Stakeholders and RACI

| Stakeholder | Role | R / A / C / I |
|---|---|---|
| You (student) | Deriver, coder, analyst, writer | **R** for everything; **A** for timeline |
| Prof. Parapsorb Borisut | Institution supervisor (sorbent chemistry, column data) | **A** for scientific correctness; **C** on isotherm and geometry |
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

> *How do superficial gas velocity, inlet CO₂ concentration, bed length, and adsorption temperature individually and jointly shape the breakthrough time and stoichiometric capacity utilisation of an amine-functionalised packed bed at DAC-relevant concentrations — and to what extent is this behaviour predicted from first principles by the Rankine–Hugoniot adsorption-shock condition and the governing dimensionless groups (Pe, NTU, α)?*

### 2.2 Sub-hypotheses

Each maps onto one of the four controllable parameters plus the front-velocity theory. A sub-hypothesis is accepted/rejected/refined based on the sweep results + benchmark agreement.

| H# | Sub-topic | Hypothesis | Primary anchor source | Accept / refine threshold |
|---|---|---|---|---|
| **H1** | Feed velocity / Pe | Higher u → shorter τ_BT (less residence time per bed volume), but stoichiometric utilisation η drops as Pe increases because the fixed adsorption kinetics can no longer saturate the faster-moving gas before the outlet. At high NTU, τ_BT ∝ 1/u. | Stampi-Bombelli 2024 (u = 0.5–2.5 m/s); Myers & Font 2020 | τ_BT ∝ u^(−0.9 to −1.1) verified across 3 velocity levels |
| **H2** | Inlet CO₂ concentration | Higher C_in → shorter τ_BT (larger driving force speeds the front). Dynamic capacity q_dyn (mol CO₂/kg per cycle) stays roughly constant across the DAC-to-moderate-indoor range (400–2000 ppm) because the Toth isotherm is concave (compressive wave) — actual test is whether the adsorption shock speed matches the R-H chord for each C_in step. | Chen et al. 2023 (500–2000 ppm); Stampi-Bombelli 2024 (400 ppm) | R-H chord velocity within ±15% of v_front for each C_in level |
| **H3** | Bed length L | τ_BT scales linearly with L at fixed u, C_in, and T_ads (same front propagation speed; only the distance to travel changes). MTZ width in metres grows with L due to axial dispersion: W_MTZ ∝ sqrt(L / Pe). Stoichiometric utilisation η is independent of L when NTU per unit length is held fixed. | Myers & Font 2020 (traveling-wave result); Stampi-Bombelli column geometry | τ_BT ∝ L fit R² > 0.97; MTZ scaling within 20% of sqrt prediction |
| **H4** | Adsorption temperature T_ads | Higher T_ads reduces equilibrium loading q* via the Toth b(T) temperature dependence → earlier breakthrough. Quantitative prediction: τ_BT(T) / τ_BT(25 °C) tracks q*(T) / q*(25 °C) within ±20%. At 90 °C (directly tested in Stampi-Bombelli), the capacity drop is significant and measurable. | Stampi-Bombelli 2024 (25, 50, 90 °C tests); Jin et al. 2025 | \|τ_BT(T)/τ_BT(25 °C) − q*(T)/q*(25 °C)\| < 20% |
| **H5** | Adsorption-front velocity | The adsorption shock velocity measured in simulation matches the Rankine–Hugoniot chord formula: v_shock = u · ΔC / (ε · ΔC + (1−ε) · ρ_p · Δq), where Δq = q*(C_in) − q*(0) from the Toth isotherm at T_ads. | Myers & Font 2020; LeVeque Ch 3 | \|v_sim − v_RH\| / v_RH < 15% |

Each of H1–H5 will receive its own subsection in the Results chapter and a one-line verdict (**accept / refine / reject**) in the Conclusions.

### 2.3 Metrics

| Tier | Metric | Symbol | Units | Source |
|---|---|---|---|---|
| Primary | Breakthrough time (C_out/C_in = 0.05) | τ_BT | s | C(z=L, t) trace |
| Primary | Saturation time (C_out/C_in = 0.95) | τ_sat | s | C(z=L, t) trace |
| Primary | Stoichiometric bed utilisation | η | — | τ_st / τ_sat, where τ_st = stoichiometric breakthrough time (area method) |
| Primary | MTZ width at τ_BT | W_MTZ | m | axial distance between 10%–90% C/C_in contours |
| Secondary | Dynamic adsorption capacity per cycle | q_dyn | mol/kg | ∫₀^τ_BT u·(C_in − C_out) dt / (ρ_p · (1−ε) · L) |
| Secondary | Adsorption front velocity | v_front | m/s | slope of 50%-concentration isoline in (z, t) plane |
| Secondary | Bed utilisation at breakthrough | BU | — | q_avg(τ_BT) / q*(C_in) |
| Guardrail | CFL stability | CFL | < 1 | u · Δt / Δz |
| Guardrail | Mass balance drift over full adsorption run | ε_m | < 1% | \|Σ in − Σ out − ΔInventory\| / Σ in |

### 2.4 Parametric sweep matrix (pre-committed before running anything)

**Baseline** (mirrors Stampi-Bombelli 2024 packed-bed column for Gate C benchmarking):

| Parameter | Baseline value | Rationale |
|---|---|---|
| u | 1.5 m/s | Stampi-Bombelli mid-range (0.5–2.5 m/s tested) |
| C_in | 400 ppm CO₂ | DAC-relevant; primary benchmark condition |
| L | 32.5 cm | Stampi-Bombelli packed-bed column length |
| d_c | 3.37 cm | Stampi-Bombelli packed-bed column diameter |
| T_ads | 25 °C | Ambient adsorption temperature |
| Sorbent | Amine-functionalised γ-alumina, 3 mm ring pellets | Stampi-Bombelli 2024 |
| Toth isotherm | ns0 = 1.23 mol/kg; b0 = 4839 kPa⁻¹; t0 = 0.25; ΔH0 = 70 kJ/mol; T0 = 298 K; χ = 0 | Stampi-Bombelli 2024, Table 2 |
| Bed void fraction ε | ~0.40 (packed rings, literature estimate) | Stampi-Bombelli / standard |
| Pellet porosity εp | 0.71 | Stampi-Bombelli 2024 |
| Pellet density ρ_p | 1044 kg/m³ | Stampi-Bombelli 2024 |
| IC | Clean bed: C = 0, q = 0, T_g = T_s = T_ads | Adsorption starts from fresh sorbent |

**OAT sweep levels:**

| Parameter | Level 1 (low) | Level 2 (base) | Level 3 (high) |
|---|---|---|---|
| u (m/s) | 0.5 | **1.5** | 2.5 |
| C_in (ppm) | 400 | **1000** | 2000 |
| L (cm) | 15 | **32.5** | 65 |
| T_ads (°C) | 25 | **50** | 90 |

→ **11 OAT** simulations (3 + 3 + 3 + 3, sharing the baseline).

**Two-parameter interaction (u × C_in):** 3 × 3 = **9 runs** — covers the two most physically coupled parameters (Pe and driving-force simultaneously).

**Total simulation budget:** 11 OAT + 9 interaction + ~19 validation/diagnostic = **~39 runs**. At ~2–5 min per simulation on a laptop (1-D, 200 grid points, LSODA), this fits comfortably in Weeks 8–14 with margin for reruns.

Output per run: τ_BT, τ_sat, η, W_MTZ, q_dyn, v_front.

### 2.5 Benchmark datasets

| Benchmark | Source | What we match | Tolerance |
|---|---|---|---|
| Analytical step response (advection-diffusion only, no adsorption) | Myers & Font 2020; Carslaw & Jaeger | C(z, t) profile — Gaussian broadening | L² error < 1% |
| Adsorption shock velocity from R-H chord | Myers & Font 2020; LeVeque Ch 3 | v_front at baseline conditions (400 ppm, u=1.5 m/s, 25 °C) | ±10% |
| Breakthrough curve shape and τ_BT at 400 ppm | Stampi-Bombelli 2024 | τ_BT and approximate C_out(t) shape | τ_BT ±20% |
| Capacity drop with T_ads at 25, 50, 90 °C | Stampi-Bombelli 2024 | τ_BT(T) trend and magnitude | directional + ±20% |
| Concentration effect on front dynamics at 500–2000 ppm | Chen et al. 2023 | τ_BT vs C_in direction and approximate scaling | directional |

### 2.6 Validation protocol (mandatory before any production sweep)

Three gates, each must pass before moving on:

1. **Gate A — Linear solver validation (Wk 4):** solve ∂C/∂t + u ∂C/∂z = D_ax ∂²C/∂z² with a step inlet, zero adsorption; compare to the analytical Gaussian-broadening solution. Pass: L² error < 1% on a 200-node grid.
2. **Gate B — Nonlinear front validation (Wk 5–6):** solve isothermal (T = T_ads = const) Toth + LDF; verify the adsorption breakthrough-front velocity matches the Rankine–Hugoniot chord formula v_RH = u · ΔC / (ε · ΔC + (1−ε) · ρ_p · Δq_Toth). Pass: \|v_sim − v_RH\| / v_RH < 10%.
3. **Gate C — Stampi-Bombelli benchmark (Wk 6):** full non-isothermal solver; reproduce the Stampi-Bombelli 2024 breakthrough curve at 400 ppm DAC conditions (baseline column geometry and Toth parameters above). Pass: τ_BT within ±20%.

**No parametric sweeps start until Gates A–C pass.** This is the single most important rule in the schedule.

---

## Part III — 18-Week Master Plan (aligned exactly to the NP timeline)

Legend: **DELIV** = hard deliverable; **GATE** = technical gate; **M** = math-learning anchor; **T** = technical/coding work; **W** = writing.

| Wk | Dates | Phase | M (math/theory) | T (technical) | W (writing) | DELIV / GATE |
|---|---|---|---|---|---|---|
| **1** | 20–24 Apr | P0 Kickoff | First-order quasilinear PDE (Evans Ch 3.1–3.2); method of characteristics; read Myers & Font 2020 §2–3 for traveling-wave context | Install Python / `numpy` `scipy` `matplotlib`; read all 7 papers in `papers/md/`; extract Toth isotherm parameters from Stampi-Bombelli Table 2; clone 1-D heat-equation solver as starter template | Set up LaTeX report skeleton; update project charter with breakthrough scope | **Wk-1 briefing + 1st supervisor meeting** |
| **2** | 27 Apr–1 May | P1 Model derivation | Adsorption R-H shock: v_shock chord formula; traveling wave substitution ξ = z − v·t (Myers & Font framework); self-sharpening condition for concave (Toth) isotherm; dispersive vs compressive wave behaviour | Derive the 4-PDE coupled system from a CV mass/energy balance for adsorption; identify every parameter with units; set ICs (C = 0, q = 0, T_g = T_s = T_ads) and inlet BCs (step C_in at z = 0) | Write "derivation from first principles" subsection (goes into Interim §3) | — |
| **3** | 4–8 May | P1 Non-dim | Buckingham Π; scaling analysis | Non-dimensionalise; identify Pe, NTU, α; tabulate expected order of magnitude for Stampi-Bombelli geometry | Write "dimensionless analysis" subsection | **DELIV: Journal #1 — Mon 4 May** |
| **4** | 11–15 May | P2 Linear solver | Method of lines; stiff ODE integration (BDF2, LSODA) | Python 1-D MOL solver for pure advection-diffusion (no adsorption); validate against analytical Gaussian-broadening step response | Validation figure #1 (draft) | **GATE A: linear solver L² < 1%** |
| **5** | 18–22 May | P2 Nonlinear coupled solver | LDF kinetics; Toth isotherm; upwind differencing; why upwind ≡ entropy condition numerically | Add Toth isotherm + LDF to MOL solver; full 4-PDE coupled system; sanity check: zero-NTU case should recover plug-flow concentration step | Draft "numerical methods" chapter | **DELIV: Journal #2 — Mon 18 May** |
| **6** | 25–29 May | P2 Benchmark + Interim draft | Constant-pattern analysis; LUB/UB method; why LDF + Toth → self-sharpening (constant-pattern) front at large NTU; MTZ width scaling | Baseline simulation at Stampi-Bombelli conditions; compute τ_BT, η, v_front, W_MTZ; benchmark τ_BT vs Paper 3 data; fix bugs | **Draft the entire Interim Report** (target 2,500–3,500 words) | **GATE B + C: R-H shock < 10%; τ_BT within ±20%** |
| **7** | 1–5 Jun | Interim gate | — | Address any validation gaps found during Interim Review | Polish and submit Interim; prepare 10-min slide deck | **DELIV: Interim Report — Mon 1 Jun; Interim Review Wk 7–8** |
| **8** | 8–12 Jun | P3 Sensitivity Part 1 | Sensitivity equations: ∂τ_BT/∂u and ∂τ_BT/∂C_in — differentiate the breakthrough condition wrt each parameter | OAT sweep on u (3 levels) and C_in (3 levels); save all C(z, t) profiles to `.npz`; extract τ_BT, η, W_MTZ, v_front | Running "Results" log in the report | — |
| 9–10 | 15–28 Jun | **Term Break** | Optional: read 1 ch. of LeVeque or Myers & Font supplementary material for pleasure; don't burn out | — | — | — |
| **11** | 29 Jun–3 Jul | P3 Sensitivity Part 2 | Local equilibrium limit as NTU → ∞; how the dispersive MTZ collapses to a shock; Pe–NTU regime map | OAT on L (3 levels) and T_ads (3 levels); extract τ_BT, η, W_MTZ, q_dyn for each | Add to Results log | — |
| **12** | 6–10 Jul | P4 Column efficiency analysis | Breakthrough curve integration: stoichiometric front time τ_st; η = τ_st / τ_sat; q_dyn vs q_eq; productivity (kg CO₂ / h / m³ bed) — framework from Stampi-Bombelli §3 | Post-process all runs for η and q_dyn; plot efficiency vs each parameter | Draft "Column efficiency and sorbent utilisation" subsection | — |
| **13** | 13–17 Jul | P4 Interaction study | Response-surface fitting (quadratic polynomial); sensitivity ranking via dimensionless groups | u × C_in 3×3 grid (9 runs); fit quadratic response surface; plot contour in (u, C_in) space | Revise Methods + add Interaction Results | **DELIV: Journal #3 — Mon 13 Jul** |
| **14** | 20–24 Jul | P5 Dimensionless recast | Recast each OAT result in (Pe, NTU, α) coordinates; universal plots; rank parameters by ∂(log output) / ∂(log Π_i) | Generate dimensionless response plots; rank parameters | Discussion draft: physical interpretation via dimensionless groups | — |
| **15** | 27–31 Jul | P6 Writing Sprint 1 | — | Clean code, reproducibility check, figure finalisation (all figures ≥ 300 dpi, consistent style) | **Draft full Final Report v0.5**; share with both supervisors for feedback | **DELIV: Journal #4 — Mon 27 Jul** |
| **16** | 3–7 Aug | P6 Writing Sprint 2 | — | Rerun any sensitivity cell requested by supervisors | Final Report v1.0 — incorporate feedback, final proofread, format-check | — |
| **17** | 10–14 Aug | P7 Submit + prep | — | — | **Submit Final Report Mon 10 Aug**; build slide deck; 2 rehearsals | **DELIV: Final Report — Mon 10 Aug** |
| **18** | 17–19 Aug | P7 Defence | — | — | Slide revision after dry-run | **DELIV: Final Presentation + panel Q&A** |

### Critical path

The critical path runs: **Wk 1 read → Wk 2–3 derive + non-dim → Wk 4 Gate A → Wk 5 Gate B → Wk 6 Gate C + interim draft → Wk 7 submit**. If any Gate slips by more than 3 days, re-baseline immediately: the term break (Wk 9–10) contains zero schedule slack, and Wk 15–16 are already writing-constrained. Do not attempt to buy back slipped Gates by working during term break — empirically that backfires as burnout. Buy it back by descoping sweep levels (drop L and T_ads to 2 levels each; cut the u × C_in interaction grid from 3×3 to 2×3).

---

## Part IV — Mathematical Learning Track

Paired weekly with the technical work. The goal is that by Week 17, the Final Report can stand on its mathematical chapter alone as a coherent exposition — not a parts catalog.

| Wk | Math topic | Why it matters here | Canonical reading | Exercise (min. 3 worked problems) |
|---|---|---|---|---|
| 1 | Method of characteristics for linear first-order PDE | Warm-up; prerequisite for adsorption wave theory | Evans §3.1; Strauss §14.1 | Solve u_t + c(x) u_x = 0 for three c(x); draw characteristics |
| 2 | Adsorption R-H shock: v_shock chord formula; traveling wave substitution ξ = z − vt; self-sharpening condition for concave isotherm; dispersive vs compressive waves | Directly predicts τ_BT and v_front; foundation for H5 and the Gate B test | Myers & Font 2020 §2–3; LeVeque Ch 3 | Derive v_shock from Rankine–Hugoniot for a Langmuir isotherm; repeat for Toth; draw the chord on q* vs C |
| 3 | Dimensional analysis & Π theorem | Universalises the parametric study — results become portable across scales and sorbents | Bird/Stewart/Lightfoot Ch 6; Barenblatt — Scaling | Non-dim the 4-PDE system yourself, by hand, on paper |
| 4 | Method of lines + stiff ODE theory | Underpins the entire solver | Ascher & Petzold, *CompDE*; `scipy` docs for `solve_ivp` | Code the heat eqn MOL + compare RK4 vs LSODA step counts |
| 5 | Upwind schemes; numerical diffusion; CFL | Why an inappropriate scheme will fake shocks or smear them | LeVeque Ch 6–7 | Solve linear advection at CFL = 0.5, 1.0, 1.1; observe |
| 6 | Constant-pattern analysis: LUB/UB method; why LDF + concave isotherm → constant-pattern at large NTU; MTZ width scaling with Pe and NTU | Explains the self-sharpening front observed in simulation; needed for Discussion interpretation of W_MTZ results | Ruthven Ch 8; Do Ch 3 | Derive the constant-pattern condition; show analytically that W_MTZ ∝ sqrt(L / Pe) for dispersive case |
| 7 | — (buffer for report) | — | — | — |
| 8 | Sensitivity equations; forward sensitivity analysis | Lets you say "∂τ_BT / ∂u = X" with a number, not an eyeball | Cacuci, *Sensitivity and Uncertainty*, Ch 1 | Hand-derive the sensitivity PDE for one parameter (u); interpret sign |
| 11 | Local equilibrium limit; singular perturbation in NTU | Explains the sharp-front vs spread-front transition; maps directly to H1/H3 results | Ruthven Ch 8; Kevorkian & Cole | Show that NTU → ∞ collapses the parabolic system to a hyperbolic one; verify in simulation |
| 12 | Breakthrough curve integration: stoichiometric front time τ_st; η = τ_st / τ_sat; q_dyn vs q_eq; productivity per cycle | Translates simulation output into engineering figures of merit directly comparable to Stampi-Bombelli Table 3 | Stampi-Bombelli 2024 §3; Ruthven Ch 5 | Compute η and q_dyn from a synthetic C_out(t) trace; check mass balance |
| 13 | Response surface methodology; quadratic polynomial fits | Lets you summarise 9 u × C_in simulations as an analytical function | Montgomery, *DOE* Ch 11 | Fit y = β₀ + Σβᵢxᵢ + Σβᵢⱼxᵢxⱼ to synthetic data |
| 14 | Rescaling results into (Pe, NTU, α) space; sensitivity ranking via logarithmic derivatives | Final universalisation step | Kuzmin, *A Guide to Numerical Methods*; any advanced transport text | Rank sensitivity ∂(log τ_BT)/∂(log Π) for each dimensionless group |
| 15–18 | — | — | — | — |

**Enrichment (optional, if time permits — do *not* let these crowd out deliverables):**

- Villani, *Topics in Optimal Transport*, Ch 1 — connects to the multi-marginal transport paper in your library.
- LeVeque, *Numerical Methods for Conservation Laws* Ch 14 — Riemann problems for full wave-propagation context.
- Evans Ch 5 — Sobolev spaces; only if you truly love this and the core project is on track.

---

## Part V — Literature anchor map

How the seven papers in `papers/md/` plug into the project:

| Source | Sub-topic served | Used for | Wk first referenced |
|---|---|---|---|
| **Myers & Font 2020** (Int J Heat Mass Transf 163) | H3, H5 | Analytical traveling-wave solution; R-H adsorption shock formula; theoretical foundation for all front-velocity predictions and Gate B | 2 (wave theory) |
| **Stampi-Bombelli et al. 2024** (I&EC Res) | H1, H2, H4, Gate C | **Primary benchmark** — breakthrough experiments at 400 ppm; Toth isotherm parameters (Table 2); PFO and dual-kinetic models; packed-bed column geometry; capacity vs temperature data | 6 (Gate C) |
| **Chen et al. 2023** (Energy 282) | H1, H2 | Breakthrough simulations at 500–2000 ppm; concentration effect on front dynamics and capture rate; LDF kinetics with mmen-Mg2(dobpdc) MOF; validates concentration-range sweep directions | 8 (sensitivity) |
| **Pedrozo et al. 2026** (Comput Chem Eng 204) | H1, H3, H4 | 1-D reactive transport model; TVSA cycle optimization; computational efficiency comparison (1-D vs 2-D ~40× cost); template for cyclic future-work discussion | 11 (L, T_ads sweep) |
| **de Joannis et al. 2025** (Carbon Capture Sci Tech 17) | H2, H4 | Breakthrough under humid conditions; Lewatit sorbent; packed-bed vs monolith comparison at process scale; humidity as Future Work driver | 13 (interaction + discussion) |
| **Jin et al. 2025** (Renew Sustain Energy Rev 217) | H4 | Comprehensive review of T and RH effects on amine sorbents across −20 to 40 °C and 0–100% RH; validates direction of T_ads effect for H4; sorbent classification context | 1 (literature survey) |
| **Xu et al. 2024** (Energy Convers Manage 322) | H2, fundamentals | DAC fundamentals review; adsorption kinetics and thermodynamics; system-design context; supports Introduction and Literature Review chapters | 1 (literature survey) |

**Data in hand — no supervisor data needed for Gate C:**

All primary sorbent and column parameters are available from Stampi-Bombelli 2024 (Table 2). Remaining open items for supervisor meetings:

1. If SUTD rig geometry is available (d_c, L, sorbent type, thermocouple positions), add as a model-vs-experiment stretch check in the Discussion chapter. Not blocking.
2. If Prof. Borisut's group uses a different sorbent, update isotherm parameters from the group's characterisation data and re-run Gate C.

---

## Part VI — Risk Register

High-impact risks first. Every risk has a *trigger* and a *response*.

| # | Risk | Likelihood | Impact | Trigger | Response |
|---|---|---|---|---|---|
| R1 | Numerical solver fails Gate A (linear validation) by end of Wk 4 | Medium | High | `scipy.solve_ivp` diverges or L² error > 1% | Drop to Crank–Nicolson finite difference in hand-coded form; consult Birgersson; 3-day buffer built in |
| R2 | SUTD does not provide rig-specific sorbent / geometry parameters | Low | Low | No reply by end of Wk 2 | **Not blocking** — baseline uses Stampi-Bombelli 2024 literature parameters (fully available). Document clearly in Interim. |
| R3 | Time overrun on derivation chapter → Interim Report late | Medium | Critical | Wk 6 Friday and interim draft < 1,500 words | Submit tighter scope: cover only H1 and H2 in Interim; complete H3–H5 by Wk 13 |
| R4 | Toth isotherm closure causes numerical stiffness near low-concentration limit | Low | Medium | Solver rejects steps; LSODA goes to zero step size | Add small regularisation to Toth denominator (floor b·C at 1 × 10⁻¹²); tune `atol` / `rtol` |
| R5 | Scope creep into 2-D / humidity / cyclic simulation | High | Medium | You find yourself reading de Joannis humidity details on a Wednesday morning | Part I §1.3 "Out of scope" is the answer; bookmark for FYP |
| R6 | Burnout in Wk 11–13 after the term break | Medium | Medium | Journal #3 is late or thin; weekend work exceeds 12 h | Cut interaction grid to 2×3 (drop one u level); call NP supervisor |
| R7 | Laptop / code-loss catastrophe | Low | Catastrophic | — | **Push every commit to GitHub nightly**; weekly Google Drive backup of `.npz` results |
| R8 | Panel presentation overruns / Q&A fumble | Medium | Medium | Dry-run clocks > 22 min | Two full rehearsals minimum; record yourself once; first slide is a *physical picture* of a packed bed with a breakthrough curve, not equations |
| R9 | Misaligned supervisor expectations (SUTD vs NP) | Low | High | A supervisor is surprised by project direction in Wk 7 | Monthly 30-min joint update email to both SUTD + NP supervisors with one-page status (Part IX template) |

---

## Part VII — Bi-weekly Journal template

Each journal is ~400–600 words, Markdown, 4 sections. Submit by Monday 23:59.

```markdown
# Journal #N — Week X (dd Mmm 2026)

## 1. What I did this period
- [bullet, concrete, verb-first — "Derived the R-H chord formula for the adsorption shock; verified against Stampi-Bombelli Fig. 4 front velocity."]
- [include code commit links where relevant]

## 2. What I learned
- [mathematical/physical insight — this is where your mathematics-first philosophy shows up]
- [brief derivation or diagram if the insight is visual]

## 3. Blockers and questions
- [be honest; supervisors value this more than smoothed narratives]
- [name the person whose answer would unblock each item]

## 4. Plan for next period
- [3–5 concrete items matching Part III for the upcoming week]
- [any scope-change flag]
```

### Topic anchors per journal

| Journal | Target content |
|---|---|
| #1 (4 May, Wk 3) | Mathematical foundation: method of characteristics + traveling-wave substitution worked; 4-PDE breakthrough system derived; Toth isotherm parameters read in from Stampi-Bombelli; Π-groups identified; first solver skeleton coded |
| #2 (18 May, Wk 5) | Gate A passed (linear solver L² < 1%); Toth + LDF coupled; first breakthrough curve plotted; R-H chord prediction for v_front computed by hand and compared with simulation |
| #3 (13 Jul, Wk 13) | Mid-sweep status: OAT complete for u and C_in; velocity and concentration effects confirm H1 and H2; u × C_in interaction grid designed and running |
| #4 (27 Jul, Wk 15) | Results recast in (Pe, NTU) space; quadratic response surface fitted to interaction data; Final Report v0.5 circulated to supervisors |

---

## Part VIII — Report Scaffolds

### Interim Report (Mon 1 June, Wk 7) — target 2,500–3,500 words

1. **Introduction & motivation** (~300 w) — global CO₂ context; DAC concentration regime (400 ppm); specific scope (breakthrough parametrics); sub-hypotheses H1–H5 stated.
2. **Governing equations — derived** (~800 w) — four-PDE system derived from CV; Toth isotherm; LDF; ICs (clean bed) and BCs (step inlet); **write every line**; note Q_wall = 0 (adiabatic).
3. **Dimensional analysis** (~400 w) — full non-dim; Pe, NTU, α with typical values for Stampi-Bombelli geometry.
4. **Numerical methods & validation** (~700 w) — MOL; stiff integrator; Gates A, B, C passed with figures.
5. **Baseline simulation & benchmark** (~600 w) — Stampi-Bombelli column at 400 ppm; τ_BT, η, v_front, W_MTZ reported; comparison to Paper 3 data tabulated.
6. **Work plan for weeks 8–17** (~300 w) — sensitivity + interaction + efficiency analysis + write-up, with dates.

### Final Report (Mon 10 Aug, Wk 17) — target 6,000–8,000 words

1. Abstract (200 w)
2. Introduction (500 w) — including *Why the mathematics of this system is the engineering of this system*
3. Literature Review (800 w) — structured by sub-topic (H1–H5), each closing with "What is known / what the present work adds"; anchored to the 7 papers in Part V
4. Governing equations — derived (1,000 w) — expanded from Interim; include dimensional analysis; Q_wall = 0 stated explicitly
5. Numerical methods (700 w) — MOL, upwind, stability, Gate A/B/C verification plots
6. Parametric sensitivity study (1,800 w) — H1 (velocity) → H2 (concentration) → H3 (bed length) → H4 (temperature); each subsection ends with accept/refine verdict
7. Adsorption front velocity and Rankine–Hugoniot comparison (700 w) — H5 result; chord diagram; regime map in (Pe, NTU) space
8. Column efficiency and sorbent utilisation (500 w) — η and q_dyn breakdown; optimal operating window discussion
9. Discussion — dimensionless recast (600 w) — universal (Pe, NTU) plots; parameter ranking by ∂(log τ_BT)/∂(log Π)
10. Conclusions (400 w) — verdict on H1–H5; what it means for DAC column design; limitations
11. Future work (one page) — cyclic TSA simulation coupling breakthrough + regeneration half-cycles; 2-D model; humidity effects; Bayesian inverse problem for LDF k_a estimation
12. References (30–50 entries) + appendices (code listings, full result tables, Toth isotherm derivation)

---

## Part IX — Weekly Operating Rhythm

### Daily

- **09:00** — read one page of the week's math anchor reading. Non-negotiable; 15 minutes.
- **End of day** — commit code to GitHub with a meaningful message ("Closed Gate A: linear advection-diffusion MOL validated against Gaussian broadening, L² = 0.4%"), even on non-coding days.

### Weekly

| Day | Block |
|---|---|
| Mon | 09:00–10:30 Math theory (Evans / LeVeque / Myers & Font) |
| Tue | 14:00–15:00 Physical-chemistry reading (Ruthven / one paper from papers/md/) |
| Wed | 10:00–12:00 Coding sprint (one feature or one validation gate per session) |
| Thu | 14:00–15:00 Literature: read one source end-to-end; add 3 lines to running annotated bibliography |
| Fri | 14:00–15:00 Integration note — 400–600 words connecting the week's math to the week's code. Feeds directly into the next journal. |
| Sat | 2–3 h extended coding/analysis (optional; skip without guilt during term break) |
| Sun | 30 min — read Part III for next week; write Monday's journal (or draft its opening) |

### Monthly

- Last Friday of each month — one-page status email to Prof. Borisut + Prof. Birgersson + NP supervisor. Template below.

```markdown
Subject: [CO2 Adsorption Breakthrough — Month M status] <headline, 1 line>

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

---

## Appendix A — Governing equations (quick reference)

Gas-phase CO₂ mass balance:

    ε ∂C/∂t = −u ∂C/∂z + D_ax ∂²C/∂z² − k_LDF · a_p · (1−ε) · (C − C*)

Solid-phase mass balance (LDF kinetics):

    (1−ε) ρ_p ∂q/∂t = k_LDF · a_p · (1−ε) · (C − C*)

Gas energy balance (adiabatic adsorption; Q_wall = 0):

    ε ρ_g c_pg ∂T_g/∂t = −ρ_g c_pg u ∂T_g/∂z + λ_ax ∂²T_g/∂z² + h_f a_p (T_s − T_g)

Solid energy balance:

    (1−ε) ρ_p c_ps ∂T_s/∂t = h_f a_p (T_g − T_s) + (−ΔH_ads) ρ_p (1−ε) ∂q/∂t

Closure — Toth isotherm with temperature-dependent parameters (Stampi-Bombelli 2024, Table 2):

    q*(C, T) = ns(T) · b(T)·C / [1 + (b(T)·C)^t0]^(1/t0)

    ns(T) = ns0 · exp(χ / T),   χ = 0 for amine-γ-alumina
    b(T)  = b0  · exp[(ΔH0 / (R · T0)) · (T0/T − 1)]

    Parameters: ns0 = 1.23 mol/kg;  b0 = 4839 kPa⁻¹;  t0 = 0.25;  ΔH0 = 70 kJ/mol;  T0 = 298 K

Initial conditions (adsorption from a clean bed):

    C(z, 0) = 0;   q(z, 0) = 0;   T_g(z, 0) = T_s(z, 0) = T_ads

Boundary condition (inlet step at z = 0, enforced via Dirichlet zeroing of dY/dt[0]):

    C(0, t) = C_in;   T_g(0, t) = T_feed = T_ads

Rankine–Hugoniot adsorption shock velocity:

    v_shock = u · ΔC / (ε · ΔC + (1−ε) · ρ_p · Δq)

    where Δq = q*(C_in, T_ads) − q*(0, T_ads) = q*(C_in, T_ads)

---

## Appendix B — Dimensionless groups

| Group | Definition | Typical | Meaning |
|---|---|---|---|
| Pe | u L / D_ax | 10–500 | convective vs dispersive transport; governs MTZ width |
| NTU | k_LDF a_p L (1−ε) / (ε u) | 1–20 | mass-transfer rate vs convective residence time; governs how close to constant-pattern |
| Pe_h | ρ_g c_pg u L / λ_ax | 10–200 | thermal convective vs conductive |
| α | ρ_p (1−ε) Δq / (ε ΔC) | 1–100 | solid-phase vs gas-phase CO₂ capacity; sets v_shock / u ratio |
| Λ | (−ΔH_ads) Δq / (c_pg · T_ads) | 0.1–1 | heat-of-adsorption feedback strength on temperature rise |
| Bi_w | — | — | not relevant for adiabatic adsorption (Q_wall = 0); retained for reference if wall heating is added in FYP |

The three most important groups for this parametric study are **Pe** (governs MTZ dispersion), **NTU** (governs proximity to local equilibrium and constant-pattern), and **α** (sets the adsorption shock speed relative to u).

---

## Appendix C — Python solver scaffold (Week 4–5)

```python
# File: src/solver/pde_mol.py

import numpy as np
from scipy.integrate import solve_ivp

# ---- Parameters (from Stampi-Bombelli 2024) ----
eps    = 0.40        # bed void fraction
eps_p  = 0.71        # pellet porosity
rho_p  = 1044.0      # pellet bulk density, kg/m³
rho_g  = 1.2         # carrier gas density, kg/m³
c_pg   = 1040.0      # gas specific heat, J/(kg·K)
c_ps   = 900.0       # solid specific heat, J/(kg·K)  [placeholder — request from supervisor]
u      = 1.5         # superficial velocity, m/s
L      = 0.325       # bed length, m
D_ax   = 1e-4        # axial dispersion coefficient, m²/s  [placeholder]
lam_ax = 0.2         # effective axial thermal conductivity  [placeholder]
k_LDF  = 0.01        # LDF mass transfer coefficient, 1/s  [fitted at Gate B]
a_p    = 1.5e4       # specific interfacial area, 1/m  [estimate for 3 mm rings]
h_f    = 50.0        # gas-solid heat transfer coefficient  [placeholder]
dH_ads = 70e3        # heat of adsorption, J/mol
T_ads  = 298.15      # adsorption temperature, K

# Toth isotherm parameters — Stampi-Bombelli 2024 Table 2
ns0  = 1.23          # mol/kg
b0   = 4839.0        # kPa⁻¹
t0   = 0.25
T0   = 298.15        # K
R    = 8.314         # J/(mol·K)
chi  = 0.0

C_in_ppm = 400.0
C_in = C_in_ppm * 1e-6 * 101325.0 / (R * T_ads)  # mol/m³

N  = 200
z  = np.linspace(0, L, N)
dz = z[1] - z[0]

def toth(C, T):
    """Toth isotherm — Stampi-Bombelli 2024 amine-γ-alumina."""
    ns = ns0 * np.exp(chi / T)
    b  = b0  * np.exp((dH_ads / (R * T0)) * (T0 / T - 1.0))
    bC = np.maximum(b * C, 0.0)
    return ns * bC / (1.0 + bC**t0)**(1.0 / t0)

def rhs(t, y):
    C, q, Tg, Ts = np.split(y, 4)

    # First-order upwind for convection; central differences for diffusion
    dCdz  = np.zeros_like(C)
    dTdz  = np.zeros_like(Tg)
    dCdz[1:]  = (C[1:] - C[:-1]) / dz
    dTdz[1:]  = (Tg[1:] - Tg[:-1]) / dz
    d2Cdz2 = np.zeros_like(C)
    d2Tdz2 = np.zeros_like(Tg)
    d2Cdz2[1:-1] = (C[2:] - 2*C[1:-1] + C[:-2]) / dz**2
    d2Tdz2[1:-1] = (Tg[2:] - 2*Tg[1:-1] + Tg[:-2]) / dz**2

    C_star = toth(C, Ts)
    rate   = k_LDF * a_p * (C - C_star)

    dCdt  = (-u*dCdz + D_ax*d2Cdz2 - rate*(1-eps)) / eps
    dqdt  = rate / rho_p
    # Adiabatic: no Q_wall term
    dTgdt = (-rho_g*c_pg*u*dTdz + lam_ax*d2Tdz2
             + h_f*a_p*(Ts - Tg)) / (eps*rho_g*c_pg)
    dTsdt = (h_f*a_p*(Tg - Ts)
             + dH_ads*rho_p*(1-eps)*dqdt) / ((1-eps)*rho_p*c_ps)

    # Dirichlet inlet BC enforced by zeroing dY/dt at node 0
    dCdt[0]  = 0.0
    dTgdt[0] = 0.0

    return np.concatenate([dCdt, dqdt, dTgdt, dTsdt])

# Initial condition: clean bed at T_ads
y0 = np.concatenate([np.zeros(N),        # C = 0
                     np.zeros(N),        # q = 0
                     np.full(N, T_ads),  # T_g
                     np.full(N, T_ads)]) # T_s
# Fix inlet node
y0[0]   = C_in
y0[2*N] = T_ads

t_end = 3 * 3600  # 3 h; adjust per run
sol = solve_ivp(rhs, (0, t_end), y0, method='LSODA',
                rtol=1e-6, atol=1e-9,
                t_eval=np.linspace(0, t_end, 500))
```

The snippet is a scaffold, not working production code. Expect to spend Weeks 4–5 turning this into a Gate-A-passing implementation. `k_LDF`, `a_p`, `D_ax`, `h_f`, and `c_ps` are placeholders that must be either fitted to the Gate B/C benchmark or supplied by supervisors.

---

## Appendix D — Prioritised reading list

**Tier 1 — read in Week 1, referred to throughout:**
- Evans, *PDE* — Ch 3 (first-order equations) in full.
- Myers & Font 2020, *Int J Heat Mass Transf* 163, 120434 — **analytical foundation**.
- LeVeque, *Numerical Methods for Conservation Laws* — Ch 3 (scalar laws), Ch 6–7 (upwind).
- Ruthven, *Principles of Adsorption and Adsorption Processes* — Ch 5 (breakthrough), Ch 8 (thermal effects).
- Stampi-Bombelli et al. 2024, *I&EC Res* — **primary benchmark**.

**Tier 2 — reference when topic arrives:**
- Chen et al. 2023, *Energy* 282 — concentration-range sweep context.
- Pedrozo et al. 2026, *Comput Chem Eng* 204 — reactive transport model template.
- Jin et al. 2025, *Renew Sustain Energy Rev* 217 — sorbent temperature sensitivity.
- de Joannis et al. 2025, *Carbon Capture Sci Tech* 17 — packed bed vs monolith; humidity context.
- Xu et al. 2024, *Energy Convers Manage* 322 — DAC fundamentals.
- Bird/Stewart/Lightfoot, *Transport Phenomena* Ch 6, 11, 14.
- Ascher & Petzold, *Computer Methods for ODEs and DAEs*.

**Tier 3 — enrichment (only if on-track):**
- Villani, *Topics in Optimal Transport* — Ch 1.
- Evans Ch 5 — Sobolev spaces.

---

*End of Foolproof Study Plan — version 2.0, 30 April 2026 (scope revised: regeneration → adsorption breakthrough).*  
*Revision policy: update Part III and Part VI weekly, log every change in a changelog section appended to this file.*

---

## Changelog

| Date | Version | Change |
|---|---|---|
| 20 Apr 2026 | 1.0 | Initial plan — regeneration scope |
| 30 Apr 2026 | 2.0 | Full scope pivot: regeneration → adsorption breakthrough. New controllable parameters (u, C_in, L, T_ads). New benchmarks (Stampi-Bombelli 2024, Myers & Font 2020). New H1–H5, Gates B/C, metrics (τ_BT, η, MTZ, q_dyn), literature map, Toth isotherm closure, IC/BC. 18-week table, math track, risk register, report scaffolds all updated accordingly. |

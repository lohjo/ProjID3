# Bi-Weekly Journal #2 — Weeks 3–4 (5–16 May 2026)

**Project:** Parametric Study of CO₂ Adsorption Breakthrough in Packed-Bed Columns
**Students:** Loh John Ray, Saraswati Eloise Gunawan
**Institution supervisors:** Dr. Prapatsorn Borisut (SUTD), Prof. Erik Birgersson (NUS)
**NP supervisor:** Dr. Pham The Hanh
**Submission:** Mon 18 May 2026 (Week 5) · Word count: ~800

---

## 1. What I did this period

- **Second supervisor meeting (8 May, SUTD):** Clarified experimental scope with Dr. Borisut.
  Confirmed that wet-rig breakthrough experiments using PEI@SiO₂ granules are now **in scope**
  alongside the computational model. Key experimental parameters confirmed: 5% CO₂ inlet
  concentration, ~50 mL/min flow rate, ~6–10 g of sorbent packed to ≥50% column height. Rig
  uses MFCs (A: purge line, B: N₂ mixing, C: CO₂), with N₂ purge to baseline before each run.
  Confirmed that two kinetic models are in focus: **PFO (pseudo-first-order)** and
  **dual-kinetic (DK)**; Klinkenberg model and Thomas–Adam model are also to be surveyed
  alongside the Toth isotherm.

- **Conducted a trial CO₂ adsorption breakthrough experiment** at SUTD (5% CO₂, 50 mL/min,
  6 g PEI@SiO₂). Observed the characteristic S-shaped breakthrough curve; breakthrough
  threshold set at 5% of inlet concentration. Identified sensor and flowmeter as the two
  primary measurement sources (±20% sensor tolerance noted). Purge-to-zero was confirmed as
  mandatory prior to each run.

- **Polished the Gantt chart** for the interim report. Separated high-level deliverable
  milestones from detailed mathematical reading tasks; the latter now live in the Master
  Schedule rather than the chart submitted to supervisors.

- **Wrote Bill of Materials (BOM)** for the SUTD rig setup: push-fit connectors, hex
  adaptors, 3-way valves, T-shaped mixer, 8 mm clear tubing, CO₂ sensor, SFC/SFM electronics,
  and associated fittings.

- **Drafted the Standard Operating Procedure (SOP):** N₂ baseline calibration (~15 min),
  MFC concentration verification before introducing gas to column, data acquisition via GasLab
  (CO₂ sensor) and Sensirion (flow), recording breakthrough curve with inlet/outlet CO₂, flow
  rate, temperature, and pressure.

- **Literature review continued:** Completed second-pass readings of Xu et al. (2024) DAC
  review and Chen et al. (2023) structured packed-bed CFD paper. Began first pass of
  Stampi-Bombelli et al. (2024) as the primary benchmark. Surveyed Hefti et al. on
  non-standard isotherm shapes for MOF-vs-zeolite comparison; noted its relevance to
  understanding Toth isotherm behaviour at the DAC concentration range.

- **Learned the three-pass reading method** (first pass: skim title/abstract/figures for
  relevance; second pass: read all figures, tables, and section headers; third pass:
  focused read of methods and results relevant to current gate). Applied to all papers this
  fortnight.

---

## 2. What I learned

**Physical insight — breakthrough curve structure.** The trial experiment made concrete what
was previously only symbolic. The S-shaped C_out/C_in curve is not arbitrary: it reflects
the mass-transfer zone (MTZ) entering, traversing, and exiting the bed. The "breakthrough
hump" at ~5% of inlet is not a true hump but the threshold at which the bed is considered
saturated for practical purposes. Connecting this to the model: τ_BT is the time at which
C_out/C_in = 0.05, and the sharpness of the curve at breakthrough is directly set by the
NTU (mass-transfer rate relative to convective residence time). A low-NTU bed produces a
long, gradual approach to saturation; a high-NTU bed produces a sharper front — and the
Toth isotherm's concavity drives this toward a constant-pattern (self-sharpening) regime at
large NTU.

**Mathematical insight — why two kinetic models matter.** Dr. Borisut confirmed that both
PFO and DK models are used to fit breakthrough curves because neither fits perfectly across
the full concentration range. PFO (pseudo-first-order) uses a single lumped rate constant
k_f(C* − q), which linearises the isotherm; it fits well at low loading but fails at high
loading where site heterogeneity matters. The dual-kinetic model uses two parallel sites with
different rate constants — it handles the heterogeneity explicitly. The Toth isotherm is the
equilibrium closure that governs C*; the kinetic model governs how fast q approaches that
equilibrium. Understanding this distinction clarifies why we cannot decouple the isotherm
choice from the kinetic model choice when designing the experiment matrix.

**Experimental design insight — initial and boundary conditions.** From the rig familiarisation
and the meeting, the ICs and BCs of the physical system are now clear. The bed starts clean
(C = 0, q = 0, T_g = T_s = T_ads = room temperature after N₂ purge). The inlet BC is a
step in CO₂ concentration at t = 0; the outlet is open to atmosphere (zero-gradient pressure
BC). These match the mathematical ICs and BCs in `derivation.md` §2 (adsorption scope), which
gives confidence the model and experiment are aligned.

---

## 3. Blockers and questions

**B1 — Velocity units in the sweep matrix.** The planned sweep (u = 0.5 / 1.5 / 2.5 m/s) is
an order of magnitude higher than the experimental rig operates (~50 mL/min ≈ 0.001 m/s
superficial for an 8 mm column). Need to confirm with Prof. Birgersson whether the sweep is
in *interstitial* velocity (not superficial), or whether these values are intended as a
wider-than-experimental parametric study. The distinction matters for how we report
dimensionless Pe and compare with Stampi-Bombelli (their u ≈ 0.14 m/s).
*Owner: Prof. Birgersson — flag at next meeting.*

**B2 — Missing Toth α parameter.** Stampi-Bombelli Table 1 lists α = 0.11 (temperature
dependence of heterogeneity exponent via t(T) = t₀ + α(1 − T₀/T)) but this is absent from
the CLAUDE.md parameter table. At T_ads = 90 °C, omitting α shifts q* by an amount
comparable to the ±20% Gate C tolerance. Will add α = 0.11 to `derivation.md` §1.5 and
`pde_mol.py` before Gate C.
*Owner: technical — will flag to Dr. Borisut for confirmation.*

**B3 — Gate A solver status.** The linear MOL solver (pure advection-diffusion, no
adsorption) is scaffolded but not yet at the L² < 1% pass threshold. CFL stability at
numbers above 1.0 needs explicit testing. This is the week 4 priority.
*Owner: self — target pass by Fri 22 May.*

---

## 4. Plan for next fortnight (Wks 5–6, 19–29 May)

1. **Pass Gate A** (linear solver, L² < 1% vs analytical Gaussian broadening). Test at CFL =
   0.5, 0.9, 1.1 to confirm CFL > 1 breaks the scheme as theory predicts. Log timestep
   history to catch LSODA hiding CFL instability.
2. **Add Toth + LDF to solver** (Gate B preparation). Verify the zero-NTU case recovers
   plug-flow step; verify adsorption front appears at finite NTU.
3. **Compute R-H chord velocity by hand** for the Stampi-Bombelli baseline (400 ppm,
   T_ads = 25 °C) and compare with the front velocity extracted from the simulation.
   Target: |v_sim − v_RH| / v_RH < 10%.
4. **Begin Interim Report draft**: Introduction (~300 words), governing equations section
   (~800 words from derivation.md), and dimensional analysis section (~400 words). Write
   these in parallel with Gate work — not after.
5. **Prepare one experimental run** for the 3×3 OAT matrix (vary flow rate × concentration)
   at the SUTD rig following the confirmed SOP.

<Appendix>
Standard Operating Procedure (SOP) for SUTD adsorption breakthrough experiments
Source: https://connectnpedu.sharepoint.com/:w:/s/DPDACO2AdsorptioninPackedBedColumns/IQDsHK3c-Rs4QpLcMwq52tsmAY0Hx83Pef6cKa53lg0s8iM?e=3SwnHn 
Key elements from the source document:
	PEI@SiO₂ granules, ~10g, packed to at least 50% column height
	Software: GasLab for CO₂ sensor, Sensirion for flow
	Calibration: ~15 min N₂ baseline before loading granules
	MFC-controlled N₂/CO₂ mixing
	Secondary bypass line for concentration verification before introducing to column
	No regeneration step mentioned in the basic SOP (but the diagram shows a heating jacket)
	Sensors: CO₂ concentration, TI/TC, PI, FI
	Data: breakthrough curve, inlet/outlet CO₂, flow rate, temperature, pressure
From the rig diagram:
	MFC-A: top, purge line
	MFC-B: middle, N₂ for mixing
	MFC-C: lower, CO₂
	Purge outlet at top
	Heating jacket (red) around column
	TC on column wall
	Bottom outlet with CO₂, TI, PI, FI instruments
	PEI@SiO₂ granules bed
From project context:
	Breakthrough metrics: τ_BT, τ_sat, η, W_MTZ, q_dyn, v_front
	Parameters: u, C_in, L, T_ads
	Toth isotherm parameters from Stampi-Bombelli 2024
	The SOP needs to support the parametric study (Gate C validation)

Design of Experiment:

Literature Review
-- BIRD EYE VIEW --
A comprehensive review on direct air carbon capture (DAC) technology… (Huijin Xu et al.)
	abstract gave a comprehensive overview of understanding DAC technologies, analyses of underlying principles and theories
	introduction shows various co2 issues in real-world; linking to DAC technologies by use of point-source capture argument.
	conclusion reviews adsorption materials, seeks both sides for and against DAC technologies

Each figure is explicitly mentioned in its section—linking its visual context to analytical content (i.e. mass transfer effects in the adsorbent particle, illustrating several transport mechanisms such as mass transfer, micropore diffusion with/without external macropore resistances and surface resistance of micro-particles). Another notable figure is the CO2 uptake isotherms at 25degC in the pressure range [0,1] bar of activated carbon. While Fig. 9 provides a comparative analysis of different sorbent materials. A device for fixed-bed CO2 capture experiments shown in Fig. 13 provides further analyses into the design and setup of equipment for CO2 adsorption. To take note on rig familiarization: MFCs, N2 and CO2 routers, and output measurements.
The paper also mentions several adsorption swing methods (i.e. TVSA, PSA, VSA, MSA) with schematics on two-bed VSA and flow diagrams and graphs in Fig. 16 and 17 respectively. The graphs are helpful in understanding adsorption isotherms patterns by analyzing its derivatives and linking it to the governing equations as delimited in Myers & Font. TSA in particular was evaluated against multiple adsorption isotherms as in Fig 18. This could be helpful to understand how the different parameters affect adsorption as well as comparing experimental findings against qualitative analyses of different adsorption isotherms. A way that could bypass CO2-H20 adsorption selectivity issue illustrated in Fig. 19 and its isotherms in Fig. 20 can be developed to optimize the efficiency of adsorption process, specifically with physical adsorbents--with implications of cost and energy reductions.
Configuration references are provided in Table 4, enabling deeper analyses of models (i.e. optimization) [196], experimental design for several swing processes (i.e. temperature swing packed-bed foam => heat transfer [197]; CO2 capture efficiency through temperature management [201]; TVSA DAC setup [185]; energy savings with moving bed systems and low temp steam? [202]; amine loading and pore size on capture capacity (q*) in fluidized packed-bed reactor using silica-based sorbents [203,204]; This paper also analyzes business flow of DAC technology considering economic viability.

Numerical simulation structured packed adsorption bed for indoor DAC (Chen et al.)
	abstract & introduction laid out optimization of mass transfer and pressure drop; energy savings with HVAC-DAC systems and costs under different capture materials; CFD model for indoor adsorption showed that fan support rose energy consumption by significant amounts;
	conclusions stated that the 30% reduction in packed reduces pressure drop significantly, arguing that conventional packed-bed not suitable for indoor capture due to its high pressure drop and energy penalty; structured packed bed design offers a potential for indoor air purification while saving fan energy consumption.
Second pass: read all figures, ensure its verifiability, accuracy, relevance and reliability to this project. 
	Fig. 1. details the lifecycle of CO2 capture processes; adsorption removes CO2 from ambient air, while desorption transform captured CO2 for storage or utilization.
	Table. 1. shows basic parameters surrounding Co2 adsorption; particularly noting that for SUTD setup, the pressure of 1 bar is industry standard, fixed parameters include: volume of packing, height of reactor, temperature & density is assumed to be constant (but yet to determined/ need to approximate), angle of bed etc. Thus, the only varying parameters we are working with for now are: Co2 concentration and mass flow rate.
	Table. 2. shows the relevant parameters for the adsorption equilibrium breakthrough model (mathematical); following ref [41], Hefti et al. describes the adsorption equilibrium isotherm using step-phase non-standard isotherm shapes to compare MOF-Mn with 13X Zeolite—state-of-the-art standard for Co2 adsorption processes; Hefti et al. lays out material properties (i.e. heat of adsorption, selectivity, adsorption capacity etc) [41]; it argues that MOFs material improve separation in adsorbents, e.g. Mg-MOF-74 high uptake capacity at 0.2 bar Co2 partial pressure (% of pressure within gas); it also states performance criteria including purity, recovery, energy consumption and productivity; Hefti uses model-based process design to “elucidate the effect of non-standard isotherm shape on process performance”
	Table. 2. extends with parameters for CFD simulation
	Fig. 3. Provides a block diagram illustrating the workflow of UDF and CFD calculations
	
<\Appendix>
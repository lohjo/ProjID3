Bi-Weekly Journal #2: 14 May 2026
These two weeks gave a comprehensive overview of our design project. The first week, we polished our Gantt chart, sought feedback for our first biweekly journal and reviewed industry-standard models for the CO2 adsorption process. This bi-weekly journal outlines the standard of procedure (SOP), the design of experiment (DOE) and the literature review that has been conducted thus far.

Student: Loh John Ray, Saraswati Eloise Gunawan
Institution supervisors (SUTD/NUS): Dr. Prapatsorn Borisut, Prof. Erik Birgerhesson
NP Supervisor: Dr. Pham the Hanh
Project code: 3
Plan prepared: Monday 20 April 2026 (Week 1, Day 1); revised 30 April 2026 – scope change: regeneration → adsorption breakthrough;
Submission deadlines: Interim Report Mon 1 Jun 2026 (Wk 7); Final Report Mon 10 Aug 2026 (Wk 17); Final Presentation 17–19 Aug 2026 (Wk 18)

What I learnt
	Three-pass method for reading research papers;
	 Polished Gantt chart with literature review content, experimental preparation and execution;
	Wrote bill of materials (BOM) for rig equipment setup;
	Trial Co2 adsorption breakthrough experiment using 5% CO2 concentration, 50ml/min with 6g of PEI-SiO2 sorbent material.

 
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
	
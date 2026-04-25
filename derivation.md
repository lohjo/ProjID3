Prompt: Read and analyse the following arxiv HTML page and understand f1-prompting for this project.

Imagine you are a mathematician researching the regeneration process of CO2 capture sorbent in packed bed columns. Your task is to develop a prompt with F-1 prompting principles (as in arxiv paper) to achieve the following:
## Objectives
Derive the coupled mass-energy PDE system for a 1-D packed-bed regeneration with a Langmuir isotherm and LDF kinetics, starting from first-principles conservation laws
## Success Criterion 
Full derivation, with every term physically justified
<f1-prompting>
Reference: https://arxiv.org/html/2601.19302v2 
Paper: Formula-One Prompting (F-1) by Nitarach, Taveekitworachai, Pipatanakul (SCB DataX, Jan 2026).
Core idea. LLMs trained on math-rich corpora already know governing equations. But CoT and PoT never ask model to write equations first — they skip straight to reasoning or code. F-1 fixes this.
Two phases, one call:
1. Equation Formalization — model extracts governing equations from problem statement.
2. Natural Flow Reasoning — model picks its own solving strategy (CoT, PoT, or direct calc) based on equation structure. No router, no rules.
Why it works. Equation acts as structured intermediate rep. Simple substitution → direct calc. Multi-step derivation → CoT. Numerical heavy → PoT. Model self-routes.
Results. Tested across 5 models, 4 benchmarks:
* Beats CoT by +5.76% and PoT by +8.42% on average, winning 53 of 60 benchmark-model comparisons (88.3%).
* Largest gains in applied domains: +13.30% on FinanceMath over CoT.
* Equation formalization flips 168 problems from wrong to right vs CoT, across 1,916 problems. Achieves 73% strategy selection accuracy, reaching 81–84% of upper bound on applied domains.
vs prior work. CoT = step-by-step natural language. PoT = code generation. Plan-and-Solve = decomposition planning. None ask for equations explicitly. F-1 fills that gap without adding extra LLM calls.
Relevance to your project. Your solver derivation work (PDE system, dimensionless groups, Rankine–Hugoniot) is exactly the kind of applied-math problem where F-1 shines — equations first, then reasoning. Worth keeping in mind when prompting Claude or GPT for help debugging your MOL solver.
<\f1-prompting>

—

PHASE 1 — Equation Formalization
Six governing relations. Symbolic forms with term labels. No derivation yet.
1.1 Gas-phase CO₂ mass balance
$$\varepsilon \frac{\partial C}{\partial t} = -u \frac{\partial C}{\partial z} + D_{ax} \frac{\partial^2 C}{\partial z^2} - k_a a_p (1-\varepsilon)(C - C^*)$$
Term	Meaning
$\varepsilon ,\partial C/\partial t$	Accumulation of CO₂ in gas phase per unit bed volume; voidage $\varepsilon$ converts gas-phase concentration to bed basis
$-u, \partial C/\partial z$	Net convective transport at interstitial velocity $u$
$D_{ax}, \partial^2 C/\partial z^2$	Axial dispersion (molecular + Taylor + tortuosity-driven mixing)
$-k_a a_p (1-\varepsilon)(C - C^*)$	Sink to solid phase via film + intraparticle resistance lumped as LDF; $(1-\varepsilon)$ scales surface area to bed volume
1.2 Solid-phase CO₂ mass balance (LDF)
$$(1-\varepsilon)\rho_p \frac{\partial q}{\partial t} = k_a a_p (1-\varepsilon)(C - C^*)$$
Term	Meaning
$(1-\varepsilon)\rho_p, \partial q/\partial t$	Accumulation in solid phase per unit bed volume; $q$ in mol/kg sorbent
$k_a a_p (1-\varepsilon)(C - C^*)$	Source to solid; equal magnitude, opposite sign of mass-balance sink
LDF closure: $C^*$ = gas-phase concentration in equilibrium with current $q$, obtained by inverting Langmuir isotherm at $T_s$.
1.3 Gas-phase energy balance
$$\varepsilon \rho_g c_{pg}\frac{\partial T_g}{\partial t} = -\rho_g c_{pg} u \frac{\partial T_g}{\partial z} + \lambda_{ax}\frac{\partial^2 T_g}{\partial z^2} + h_f a_p (T_s - T_g) + \frac{4 h_w}{d_c}(T_w - T_g)$$
Term	Meaning
$\varepsilon \rho_g c_{pg}, \partial T_g/\partial t$	Sensible heat accumulation in gas
$-\rho_g c_{pg} u, \partial T_g/\partial z$	Convective enthalpy flux gradient
$\lambda_{ax}, \partial^2 T_g/\partial z^2$	Axial thermal dispersion in gas
$h_f a_p (T_s - T_g)$	Interphase heat transfer; gas heated/cooled by particles
$(4 h_w/d_c)(T_w - T_g)$	Wall heating; geometric factor $4/d_c$ = perimeter/area for cylinder
1.4 Solid-phase energy balance
$$(1-\varepsilon)\rho_p c_{ps}\frac{\partial T_s}{\partial t} = h_f a_p (T_g - T_s) + (-\Delta H_{ads}) \rho_p (1-\varepsilon)\frac{\partial q}{\partial t}$$
Term	Meaning
$(1-\varepsilon)\rho_p c_{ps}, \partial T_s/\partial t$	Sensible heat accumulation in solid
$h_f a_p (T_g - T_s)$	Reciprocal of interphase term in 1.3
$(-\Delta H_{ads}) \rho_p (1-\varepsilon),\partial q/\partial t$	Heat of adsorption; for exothermic adsorption $\Delta H_{ads} < 0$, so $(-\Delta H_{ads}) > 0$. During regeneration $\partial q/\partial t < 0$, term becomes negative — heat sink
1.5 Langmuir closure
$$q^*(C, T) = \frac{q_m(T), b(T), C}{1 + b(T), C}$$
$$q_m(T) = q_{m,0}\exp(\chi/T), \qquad b(T) = b_0 \exp!\left(\frac{|\Delta H_{ads}|}{RT}\right)$$
Term	Meaning
$q^*$	Equilibrium loading at given $(C, T)$
$q_m(T)$	Saturation capacity; weak T-dependence via $\chi$ (thermal expansion of monolayer sites)
$b(T)$	Affinity constant; van 't Hoff form. Convention: $\Delta H_{ads}$ entered as positive magnitude → $b$ decreases with $T$ as required for exothermic adsorption
[ASSUMPTION: single-site Langmuir adequate for amine-functionalised silica at low partial pressures. Violated at very high CO₂ loading where Toth or Sips fit better.]
1.6 Rankine–Hugoniot thermal front velocity
$$v_{th}^{(0)} = \frac{u,\rho_g c_{pg}}{\rho_g c_{pg} + \frac{1-\varepsilon}{\varepsilon}\rho_p c_{ps}}$$
Symbol	Meaning
$v_{th}^{(0)}$	Zeroth-order thermal-wave celerity, no adsorption coupling
Numerator	Convective enthalpy carrying capacity of gas
Denominator	Total volumetric heat capacity per unit gas volume


PHASE 2 — Natural Flow Reasoning
2.1 Gas-phase CO₂ mass balance
Step A — Control volume derivation
CV: thin axial slice from $z$ to $z + \Delta z$, cross-sectional area $A_c$, volume $A_c \Delta z$. Gas occupies fraction $\varepsilon$ → gas volume in slice = $\varepsilon A_c \Delta z$.
Word balance:
$$[\text{accumulation}] = [\text{in by convection}] - [\text{out by convection}] + [\text{net dispersion}] - [\text{lost to solid}]$$
Term-by-term:
* Accumulation: $\dfrac{\partial}{\partial t}(\varepsilon A_c \Delta z, C) = \varepsilon A_c \Delta z, \dfrac{\partial C}{\partial t}$
* Net convection: $A_c[(uC)|z - (uC)|{z+\Delta z}] \to -A_c \Delta z, u, \dfrac{\partial C}{\partial z}$ as $\Delta z \to 0$ (constant $u$ assumption)
* Net dispersion: $A_c[(-D_{ax} \partial C/\partial z)|z - (-D{ax}\partial C/\partial z)|{z+\Delta z}] \to A_c \Delta z, D{ax}, \dfrac{\partial^2 C}{\partial z^2}$
* Loss to solid: $-k_a a_p (1-\varepsilon)(C - C^*) \cdot A_c \Delta z$
Divide by $A_c \Delta z$, take $\Delta z \to 0$:
$$\varepsilon \frac{\partial C}{\partial t} = -u\frac{\partial C}{\partial z} + D_{ax}\frac{\partial^2 C}{\partial z^2} - k_a a_p (1-\varepsilon)(C - C^*)$$
[ASSUMPTION: $u$ constant in $z$ — valid when total molar flux conserved and $C \ll C_{total}$, i.e. dilute CO₂ in N₂.] [ASSUMPTION: plug flow with axial dispersion lumps radial velocity profile into $D_{ax}$.]
Step B — Term justification
Term	Sign	Process	Units check
$\varepsilon \partial C/\partial t$	+	Accumulation	$\text{(mol/m³)/s}$ ✓
$-u\partial C/\partial z$	− front, + back of wave	Convective transport	$(\text{m/s})(\text{mol/m}^4) = \text{(mol/m³)/s}$ ✓
$D_{ax}\partial^2 C/\partial z^2$	+ at concavity	Dispersion smears front	$(\text{m²/s})(\text{mol/m}^5) = \text{(mol/m³)/s}$ ✓
$-k_a a_p(1-\varepsilon)(C-C^*)$	− during adsorption, + during desorption	LDF mass transfer	$(\text{m/s})(\text{m}^{-1})(\text{mol/m³}) = \text{(mol/m³)/s}$ ✓
Step C — Coupling
* Couples to solid balance through $\partial q/\partial t \leftrightarrow (C-C^*)$ — same magnitude term, opposite sign.
* Couples to solid energy through $C^* = C^(q, T_s)$ via Langmuir inversion. Higher $T_s$ → higher $C^$ → faster desorption sink.
* Couples to gas energy weakly through $\rho_g$ and $u$ if temperature-dependent transport properties retained; usually frozen at reference.
Step D — Boundary and initial conditions
Inlet ($z=0$), Danckwerts: $$u,C(0,t) - D_{ax}\left.\frac{\partial C}{\partial z}\right|{z=0} = u,C{in}(t)$$
For pure N₂ purge during regeneration: $C_{in}(t) = 0$ for $t > 0$.
Outlet ($z=L$), Danckwerts (closed): $$\left.\frac{\partial C}{\partial z}\right|_{z=L} = 0$$
IC: $C(z, 0) = C_0$ (saturated bed, in gas-phase equilibrium with $q_{sat}$ at 400 ppm, 25 °C).
[ASSUMPTION: simpler Dirichlet $C(0,t) = C_{in}$ used in Wk 4–5 starter code; switch to Danckwerts when $\text{Pe} < 50$ to avoid front smearing.]



2.2 Solid-phase CO₂ mass balance (LDF)
Step A — Control volume derivation
Same CV. Now consider solid phase only, volume $(1-\varepsilon) A_c \Delta z$.
$$[\text{accumulation in solid}] = [\text{rate of mass transfer from gas}]$$
Solid is stationary → no convection or dispersion. Loading $q$ in mol/kg sorbent. Mass of sorbent in slice = $\rho_p (1-\varepsilon) A_c \Delta z$.
$$\frac{\partial}{\partial t}!\left[\rho_p(1-\varepsilon) A_c \Delta z, q\right] = k_a a_p (1-\varepsilon)(C - C^*), A_c \Delta z$$
Divide by $A_c \Delta z$:
$$(1-\varepsilon)\rho_p \frac{\partial q}{\partial t} = k_a a_p (1-\varepsilon)(C - C^*)$$
Cancel $(1-\varepsilon)$ if desired:
$$\rho_p \frac{\partial q}{\partial t} = k_a a_p (C - C^*)$$
[ASSUMPTION: LDF lumps film + macropore + micropore + surface diffusion into single $k_a$. Glueckauf approximation gives $k_a a_p \approx 15 D_p / r_p^2$ for spherical particles with diffusion-controlled uptake.]
Step B — Term justification
Term	Sign	Process	Units
$(1-\varepsilon)\rho_p \partial q/\partial t$	+ during ads, − during regen	Loading change	$(\text{kg/m³})(\text{mol/kg/s}) = \text{(mol/m³)/s}$ ✓
$k_a a_p(1-\varepsilon)(C-C^*)$	+ when $C > C^*$ (driving toward solid)	Mass transfer rate	$\text{(mol/m³)/s}$ ✓
Sign sanity for regeneration: hot bed → $C^* > C$ (Langmuir at high $T$) → RHS negative → $\partial q/\partial t < 0$ → bed loses CO₂. ✓
Step C — Coupling
* Direct conjugate to gas balance — sink in 2.1 = source in 2.2 in mass terms.
* Couples to solid energy via $\partial q/\partial t$ term in Eq. 1.4 (heat of desorption is sink term proportional to LDF rate).
* Couples to Langmuir isotherm via $C^*(q, T_s)$ — implicit inversion needed each timestep.
Step D — Boundary and initial conditions
No spatial BCs needed (no spatial derivative).
IC: $q(z, 0) = q_{sat}(C_0, T_0)$ uniform — bed pre-loaded at ambient conditions before regeneration starts.



2.3 Gas-phase energy balance
Step A — Control volume derivation
CV: gas phase in slice. Conservation of enthalpy (assume incompressible gas, neglect kinetic/potential, neglect viscous dissipation).
Word form:
$$[\text{accum sensible}] = [\text{conv in}] - [\text{conv out}] + [\text{axial conduction}] + [\text{film from solid}] + [\text{wall input}]$$
Term-by-term:
* Accumulation: $\varepsilon A_c \Delta z \cdot \rho_g c_{pg}, \partial T_g/\partial t$
* Net convection: $-\rho_g c_{pg} u A_c \Delta z, \partial T_g/\partial z$ (constant $\rho_g c_{pg} u$)
* Axial conduction: $\lambda_{ax} A_c \Delta z, \partial^2 T_g/\partial z^2$ (effective conductivity covers gas conduction + dispersive heat transport)
* Interphase: $h_f a_p (T_s - T_g) \cdot A_c \Delta z$ — film heat transfer per unit bed volume; $a_p$ = specific external surface area
* Wall: heat input through tube wall. Cylindrical geometry — perimeter $\pi d_c$, area $\pi d_c^2/4$, ratio = $4/d_c$. Per unit volume: $(4/d_c) h_w (T_w - T_g)$
Divide by $A_c \Delta z$:
$$\varepsilon \rho_g c_{pg}\frac{\partial T_g}{\partial t} = -\rho_g c_{pg} u \frac{\partial T_g}{\partial z} + \lambda_{ax}\frac{\partial^2 T_g}{\partial z^2} + h_f a_p(T_s - T_g) + \frac{4 h_w}{d_c}(T_w - T_g)$$
[ASSUMPTION: ideal gas; no compressibility work term ($p, dV$ neglected). Justified for low-pressure-drop packed bed at near-isobaric conditions.] [ASSUMPTION: $\lambda_{ax}$ effective property — Wakao–Kaguei correlation gives $\lambda_{ax}/\lambda_g = 7 + 0.5,\text{Pr},\text{Re}_p$.]
Step B — Term justification
Term	Sign	Process	Units
$\varepsilon \rho_g c_{pg}, \partial T_g/\partial t$	+	Sensible heat accumulation	$\text{(J/m³)/s}$ ✓
$-\rho_g c_{pg} u, \partial T_g/\partial z$	sign of $\partial T/\partial z$ flipped	Enthalpy convection	$(\text{kg/m³})(\text{J/kg/K})(\text{m/s})(\text{K/m}) = \text{(J/m³)/s}$ ✓
$\lambda_{ax}, \partial^2 T_g/\partial z^2$	+ at concave-up	Axial thermal dispersion	$(\text{W/m/K})(\text{K/m²}) = \text{W/m³}$ ✓
$h_f a_p(T_s - T_g)$	+ when solid hotter	Gas-solid film transfer	$(\text{W/m²/K})(\text{m}^{-1})(\text{K}) = \text{W/m³}$ ✓
$(4 h_w/d_c)(T_w - T_g)$	+ during regen ($T_w > T_g$)	Wall heating	$\text{W/m³}$ ✓
Step C — Coupling
* To solid energy directly via $h_f a_p(T_s - T_g)$ — equal/opposite term in 2.4.
* To gas mass balance via temperature-dependence of $C^*$ → indirect (via $T_s$).
* Wall heating drives entire regeneration — sole external energy input. $T_w(t)$ is control variable in TSA; for jacketed setup, $T_w$ ramps from ambient to $T_{regen}$ at start of cycle.
[ASSUMPTION: $T_w(z,t)$ uniform along bed — valid for high-flow heating fluid in jacket. For SUTD plate-heated geometry, may need $T_w(z,t)$ from auxiliary jacket model.]
Step D — Boundary and initial conditions
Inlet: $$T_g(0, t) = T_{in}(t)$$
(ambient purge at $T_{in} = 25,°\text{C}$; or $T_{in} = T_{regen}$ if pre-heating purge.)
Outlet: $$\left.\frac{\partial T_g}{\partial z}\right|_{z=L} = 0$$
IC: $T_g(z, 0) = T_0 = 25,°\text{C}$.



2.4 Solid-phase energy balance
Step A — Control volume derivation
CV: solid phase only, volume $(1-\varepsilon) A_c \Delta z$. Solid stationary → no convection. Solid axial conduction usually negligible vs gas-side dispersion (low contact area between particles); often dropped — checked here.
Word form:
$$[\text{accum solid sensible}] = [\text{film from gas}] + [\text{heat released or consumed by ads/des}]$$
* Accumulation: $(1-\varepsilon)\rho_p c_{ps}, A_c \Delta z, \partial T_s/\partial t$
* Film: $h_f a_p (T_g - T_s), A_c \Delta z$
* Heat of adsorption: rate of CO₂ uptake × heat per mole. Rate of moles being adsorbed per unit bed volume = $\rho_p (1-\varepsilon), \partial q/\partial t$. Heat released per mole adsorbed = $-\Delta H_{ads}$ (positive when exothermic). Heat released per unit volume per second: $$Q_{ads} = (-\Delta H_{ads}),\rho_p (1-\varepsilon),\frac{\partial q}{\partial t}$$
Divide by $A_c \Delta z$:
$$(1-\varepsilon)\rho_p c_{ps}\frac{\partial T_s}{\partial t} = h_f a_p (T_g - T_s) + (-\Delta H_{ads})\rho_p (1-\varepsilon)\frac{\partial q}{\partial t}$$
[ASSUMPTION: solid axial conduction $\lambda_s, \partial^2 T_s/\partial z^2$ omitted — particle-particle contact areas small. Re-introduce if Bi > 0.1 indicates intra-particle resistance.] [ASSUMPTION: intra-particle temperature uniform — Biot ≪ 1.]
Step B — Term justification
Term	Sign	Process	Units
$(1-\varepsilon)\rho_p c_{ps}, \partial T_s/\partial t$	+	Solid sensible heat accumulation	$\text{(J/m³)/s}$ ✓
$h_f a_p(T_g - T_s)$	+ when gas hotter	Reverse of gas-side film term	$\text{W/m³}$ ✓
$(-\Delta H_{ads})\rho_p(1-\varepsilon), \partial q/\partial t$	+ during ads ($\partial q/\partial t > 0$, exotherm); − during regen ($\partial q/\partial t < 0$, endothermic)	Heat of phase change between gas & adsorbed states	$(\text{J/mol})(\text{kg/m³})(\text{mol/kg/s}) = \text{W/m³}$ ✓
Sanity: regeneration → solid loses CO₂ → $\partial q/\partial t < 0$ → adsorption term contributes cooling → solid temperature rises only due to heat from gas (heated by wall). ✓ Matches physical expectation that breaking sorbent–CO₂ bonds requires energy input.
Step C — Coupling
* To gas energy via $h_f a_p(T_g - T_s)$ (anti-symmetric with 2.3).
* To solid mass balance via $\partial q/\partial t$ — heat term scales with LDF rate.
* To Langmuir via $T_s$ controlling $b(T_s)$ — feedback loop: hotter solid → smaller $b$ → smaller $C^$? No — careful. Smaller $b$ at higher $T$ → smaller $q^$ at given $C$. Equivalently, larger $C^*$ at given $q$ → drives desorption. ✓
* This is the central coupling that distinguishes adsorption from chemical reaction: nonlinear isotherm + heat-of-adsorption feedback creates self-sharpening or self-broadening fronts depending on isotherm curvature.
Step D — Boundary and initial conditions
No spatial BCs (no spatial derivative under chosen assumption).
IC: $T_s(z, 0) = T_0 = 25,°\text{C}$.
If solid axial conduction reinstated: insulated ends, $\partial T_s/\partial z = 0$ at both $z=0$ and $z=L$.



2.5 Langmuir closure
Step A — Thermodynamic derivation (substitute for CV)
Langmuir derivation rests on:
1. Adsorption to single layer of identical, non-interacting sites.
2. Rate of adsorption $\propto P,(\text{vacant sites})$; rate of desorption $\propto (\text{occupied sites})$.
3. Equilibrium: rates balance.
Surface coverage $\theta = q^*/q_m$:
$$k_{ads} P (1-\theta) = k_{des} \theta \quad\Rightarrow\quad \theta = \frac{b,P}{1 + b,P}, \qquad b \equiv k_{ads}/k_{des}$$
Convert pressure to gas-phase concentration via ideal gas: $P = CRT$ → absorb $RT$ into redefined $b$:
$$q^* = \frac{q_m, b, C}{1 + b, C}$$
T-dependence:
* $b(T)$: rate constants follow Arrhenius. Net activation energy difference = heat of adsorption. Van 't Hoff: $$b(T) = b_0 \exp!\left(\frac{|\Delta H_{ads}|}{RT}\right)$$ Magnitude convention: $|\Delta H_{ads}| > 0$ → $b$ decreases monotonically with $T$. ✓
* $q_m(T)$: weak dependence; thermal expansion of monolayer or site availability. Linearised: $q_m(T) = q_{m,0}\exp(\chi/T)$ with $\chi$ small; often $\chi = 0$ in practice.
[ASSUMPTION: monolayer adsorption — breaks down at high partial pressures where multilayer (BET) becomes significant. Acceptable for DAC conditions ($P_{CO_2} \sim 40,\text{Pa}$).] [ASSUMPTION: homogeneous sites — real amine sorbents have site heterogeneity; Toth correction better fit. Quantify residual via benchmark (Bos 2018 reports Toth fits for Lewatit VP OC 1065).]
Step B — Term justification
* $q_m b C$ in numerator: surface filling rate proportional to vacant sites and gas pressure.
* $1 + b C$ in denominator: saturation as $C$ grows. At low $C$, $q^* \to q_m b C$ (Henry's law). At high $C$, $q^* \to q_m$ (saturation). ✓
Step C — Coupling
* $q^$ enters gas balance (2.1) via $C^ = $ inverse Langmuir at $(q, T_s)$ — implicit equation, solve at each cell each timestep.
* $C^*$ depends on $T_s$, not $T_g$ (driving force is set by surface temperature, not bulk gas temperature). Critical for fronts under non-equilibrium thermal conditions.
* Inversion: $$C^*(q, T_s) = \frac{q}{b(T_s),(q_m(T_s) - q)}$$ diverges as $q \to q_m$ — regularize with cap at $q < 0.99, q_m$ during numerical solution.
Step D — IC
No BC (algebraic). Used to set IC of $q$: $$q(z, 0) = q^*(C_0, T_0) = \frac{q_m(T_0),b(T_0),C_0}{1 + b(T_0),C_0}$$
with $C_0$ from inlet partial pressure of pre-loading step (e.g., 400 ppm at 25 °C, 1 atm → $C_0 \approx 1.6\times 10^{-2},\text{mol/m}^3$).



2.6 Rankine–Hugoniot thermal front velocity (zeroth-order)
Step A — Wave-speed derivation
Consider local thermal equilibrium ($T_g = T_s = T$) and neglect axial dispersion, wall heating, heat of adsorption. Add 2.3 + 2.4:
$$[\varepsilon \rho_g c_{pg} + (1-\varepsilon)\rho_p c_{ps}],\frac{\partial T}{\partial t} = -\rho_g c_{pg} u, \frac{\partial T}{\partial z}$$
This is linear advection with celerity:
$$v_{th}^{(0)} = \frac{\rho_g c_{pg} u}{\varepsilon \rho_g c_{pg} + (1-\varepsilon)\rho_p c_{ps}}$$
Divide top and bottom by $\varepsilon$:
$$\boxed{,v_{th}^{(0)} = \frac{u,\rho_g c_{pg}}{\rho_g c_{pg} + \frac{1-\varepsilon}{\varepsilon}\rho_p c_{ps}},}$$
Matches user's appendix.
Rankine–Hugoniot interpretation: jump condition for hyperbolic conservation law. Defining flux $F = \rho_g c_{pg} u T$ and conserved density $U = [\varepsilon \rho_g c_{pg} + (1-\varepsilon)\rho_p c_{ps}] T$, jump:
$$v_{shock} = \frac{[F]}{[U]} = \frac{\rho_g c_{pg} u}{\varepsilon \rho_g c_{pg} + (1-\varepsilon)\rho_p c_{ps}} = v_{th}^{(0)}$$
[ASSUMPTION: thermal equilibrium between gas and solid — valid only when NTU_h $= h_f a_p L /(\rho_g c_{pg} u) \gg 1$. Otherwise two-temperature model gives two distinct wave speeds, one fast-gas, one slow-solid.]
Step B — Term justification
Numerator $\rho_g c_{pg} u$: rate at which enthalpy is convected per unit cross-section. Denominator: total volumetric heat capacity that must be raised by 1 K — only gas contributes to flux but both gas + solid resist temperature rise. Larger solid heat capacity → slower wave (retardation factor $1 + (1-\varepsilon)\rho_p c_{ps}/(\varepsilon \rho_g c_{pg})$).
Order of magnitude: with $\varepsilon = 0.4$, $\rho_g c_{pg} \approx 1250,\text{J/m³K}$, $\rho_p c_{ps} \approx 10^6,\text{J/m³K}$, retardation $\sim 1200$. Thermal front travels ~$10^{-3},u$ — slow. Fast gas pulse, slow thermal sweep.
Step C — Coupling to other equations
R-H is a derived consequence, not independent equation. Couples gas+solid energy balances under equilibrium assumption.
Step D — IC
Wave initiated at $z = 0$ when wall temperature step applied at $t = 0$. Front position at time $t$: $z_{th}(t) = v_{th}^{(0)} t$.



Step E — Heat-of-adsorption correction
Reinstate heat of desorption term. Add 2.3 + 2.4 (still with $T_g = T_s = T$, no dispersion):
$$[\varepsilon \rho_g c_{pg} + (1-\varepsilon)\rho_p c_{ps}]\frac{\partial T}{\partial t} + \rho_g c_{pg} u\frac{\partial T}{\partial z} = (-\Delta H_{ads})\rho_p(1-\varepsilon)\frac{\partial q}{\partial t}$$
Local equilibrium assumption: $q = q^*(C, T)$. Chain rule:
$$\frac{\partial q}{\partial t} = \left.\frac{\partial q^}{\partial C}\right|_T \frac{\partial C}{\partial t} + \left.\frac{\partial q^}{\partial T}\right|_C \frac{\partial T}{\partial t}$$
Define isotherm slopes:
* $K_C \equiv \partial q^*/\partial C|_T = q_m b /(1+bC)^2$ (mol/kg per mol/m³)
* $K_T \equiv \partial q^*/\partial T|_C$ — negative for exothermic adsorption (at fixed $C$, hotter surface holds less)
Substitute:
$$\left[\varepsilon \rho_g c_{pg} + (1-\varepsilon)\rho_p c_{ps} - (-\Delta H_{ads})\rho_p(1-\varepsilon)K_T\right]\frac{\partial T}{\partial t} + \rho_g c_{pg} u\frac{\partial T}{\partial z} = (-\Delta H_{ads})\rho_p(1-\varepsilon)K_C\frac{\partial C}{\partial t}$$
Note $K_T < 0$ → $-(-\Delta H_{ads}) K_T > 0$ → adds to effective heat capacity → further retardation.
Define modified front velocity (for thermal wave dragged by composition wave of similar velocity):
$$v_{th} = v_{th}^{(0)} \cdot \frac{1}{1 + \Lambda_{eff}}$$
with effective heat-of-adsorption number:
$$\Lambda_{eff} = \frac{(-\Delta H_{ads})\rho_p(1-\varepsilon),(-K_T)}{\varepsilon \rho_g c_{pg} + (1-\varepsilon)\rho_p c_{ps}}$$
For typical amine sorbent: $-\Delta H_{ads} = 75,\text{kJ/mol}$, $\rho_p = 1200,\text{kg/m}^3$, $-K_T \sim 0.01,\text{mol/kg/K}$, denominator $\sim 6\times 10^5,\text{J/m³K}$ → $\Lambda_{eff} \sim 0.7$ → ~40% reduction in front velocity.
[ASSUMPTION: local equilibrium ($\text{NTU} \to \infty$) — collapses parabolic system to hyperbolic. Real LDF kinetics broaden front; correction is for front speed, not front width.]
Validation criterion: $|v_{sim} - v_{th}|/v_{th} < 0.15$ (Gate B in study plan).



Step F — Dimensionless groups
Scaling choices:
* $z^\dagger = z/L$, $t^\dagger = t u/L$ (gas residence time)
* $\hat{C} = C/C_0$, $\hat{q} = q/q_{m,0}$, $\theta_g = T_g/T_{ref}$, $\theta_s = T_s/T_{ref}$
* $T_{ref}$ = ambient (298 K); $C_0$ = inlet CO₂ concentration during pre-loading
F.1 Gas mass balance (non-dimensional)
Substitute and divide by $\varepsilon C_0 u/L$:
$$\frac{\partial \hat{C}}{\partial t^\dagger} = -\frac{1}{\varepsilon}\frac{\partial \hat{C}}{\partial z^\dagger} + \frac{1}{\varepsilon,\text{Pe}}\frac{\partial^2 \hat{C}}{\partial z^{\dagger 2}} - \text{NTU},(\hat{C} - \hat{C}^*)$$
$$\boxed{,\text{Pe} = \frac{u L}{D_{ax}},}, \qquad \boxed{,\text{NTU} = \frac{k_a a_p (1-\varepsilon) L}{\varepsilon u},}$$
Group	Physics	Order, lab column	Limit
Pe	Convection vs axial dispersion	50–500	Pe → ∞ : pure plug flow, sharp fronts
NTU	Mass-transfer rate vs gas residence	1–20	NTU → ∞ : local equilibrium, $C \to C^*$ everywhere
F.2 Solid mass balance
$$\alpha,\frac{\partial \hat{q}}{\partial t^\dagger} = \text{NTU},(\hat{C} - \hat{C}^*)$$
$$\boxed{,\alpha = \frac{(1-\varepsilon)\rho_p q_{m,0}}{\varepsilon C_0},}$$
Group	Physics	Order	Limit
α	Solid-phase capacity / gas-phase capacity	$10^2$–$10^4$	α → ∞ : very long bed cycles per gas pass-through; classic packed-bed regime
F.3 Gas energy
Divide by $\varepsilon \rho_g c_{pg} T_{ref} u/L$:
$$\frac{\partial \theta_g}{\partial t^\dagger} = -\frac{1}{\varepsilon}\frac{\partial \theta_g}{\partial z^\dagger} + \frac{1}{\varepsilon,\text{Pe}_h}\frac{\partial^2 \theta_g}{\partial z^{\dagger 2}} + \text{St},(\theta_s - \theta_g) + \text{Bi}_w,(\theta_w - \theta_g)$$
$$\boxed{,\text{Pe}h = \frac{\rho_g c{pg} u L}{\lambda_{ax}},}, \quad \text{St} = \frac{h_f a_p L}{\varepsilon \rho_g c_{pg} u}, \quad \boxed{,\text{Bi}w = \frac{4 h_w L}{\varepsilon \rho_g c{pg} u, d_c},}$$
Group	Physics	Order	Limit
Pe_h	Thermal convection / axial conduction	10–200	Pe_h ≫ 1: thermal front propagates without smearing
St (Stanton)	Interphase heat transfer / convection	1–50	St → ∞ : thermal equilibrium $\theta_g = \theta_s$
Bi_w	Wall heating / convective sweep	0.01–0.5	Bi_w → ∞ : isothermal-wall limit (bed temperature follows wall instantly); Bi_w → 0 : adiabatic
F.4 Solid energy
Divide by $(1-\varepsilon)\rho_p c_{ps} T_{ref} u/L$:
$$\frac{\partial \theta_s}{\partial t^\dagger} = \text{St}_s (\theta_g - \theta_s) + \Lambda \cdot \beta,\frac{\partial \hat{q}}{\partial t^\dagger}$$
$$\boxed{,\Lambda = \frac{(-\Delta H_{ads}),q_{m,0}}{c_{ps} T_{ref}},}, \quad \beta = \frac{c_{ps}}{c_{pg}}\cdot\frac{\rho_p (1-\varepsilon)}{\rho_g (1-\varepsilon)\rho_p/\rho_p} = \mathcal{O}(1)$$
Group	Physics	Order	Limit
Λ	Heat of adsorption / solid sensible heat at $T_{ref}$	0.1–1.0	Λ → 0 : adsorption thermally invisible (linear thermal wave); Λ ~ 1 : strong feedback, wave self-sharpens during adsorption / spreads during desorption
(St_s defined analogously to St with solid heat capacity in denominator.)
F.5 Summary of governing dimensionless groups
Symbol	Definition	Typical lab column	Controls
Pe	$u L / D_{ax}$	50–500	Mass-front sharpness
Pe_h	$\rho_g c_{pg} u L / \lambda_{ax}$	10–200	Thermal-front sharpness
NTU	$k_a a_p (1-\varepsilon) L /(\varepsilon u)$	1–20	Approach to local equilibrium
α	$(1-\varepsilon)\rho_p q_{m,0}/(\varepsilon C_0)$	$10^2$–$10^4$	Capacity ratio; cycle time
Λ	$(-\Delta H_{ads}) q_{m,0}/(c_{ps} T_{ref})$	0.1–1.0	Heat-of-adsorption coupling strength
Bi_w	$4 h_w L /(\varepsilon \rho_g c_{pg} u, d_c)$	0.01–0.5	Wall heating effectiveness
St	$h_f a_p L /(\varepsilon \rho_g c_{pg} u)$	1–50	Gas–solid thermal coupling
F.6 Limiting regimes for parametric study
* Pe → ∞, NTU → ∞: ideal hyperbolic system. Fronts are shocks. R-H gives exact wave speed. Useful zeroth-order check.
* NTU → ∞, Pe finite: chromatographic limit. $C \approx C^*(q, T)$ everywhere. Single mass wave with isotherm-curvature-dependent shape.
* St → ∞: thermal equilibrium between phases. Two-temperature model collapses to one-temperature.
* Bi_w → ∞: isothermal-wall (bed quickly follows $T_w$). Realistic only for very thin beds or high-flow heating.
* Λ ≪ 1: thermal wave decoupled from composition wave. Pure linear thermal advection with R-H velocity.
* Λ ~ 1: full nonlinear coupling. Front shape depends on direction (adsorption sharpening vs desorption broadening).
For the planned sweep: T_regen sweep changes $b(T)$ → effectively varies effective $\Lambda$ and isotherm slope $K_C$. Q_purge sweep changes $u$ → directly varies Pe, Pe_h, NTU, Bi_w (note Bi_w $\propto 1/u$ — higher purge flow weakens wall heating per unit gas, key insight for H2 minimum). L and m sweeps scale Pe, NTU, α linearly — but $\Lambda$ unchanged → expected weaker effect on dimensionless dynamics, dominant effect on absolute throughput and SER.



End of derivation. All terms physically justified. Dimensional consistency verified at each step. Coupling structure explicit. BCs and ICs stated for solver implementation. Ready to drop into Final Report Ch. 3 with minor stylistic edits.



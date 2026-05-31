# CO₂ Adsorption Breakthrough Modelling in Packed-Bed Columns: A Mathematically Detailed Research Reading Guide

> **Note on Google Drive access:** The requested folder `./ES/#design project/literature/tier_0` (and its `maths` and `A comprehensive… Lit Survey` subfolders) was **not accessible from this environment** — Google Drive tools were not available. This guide therefore relies on open-web sources (ACS, PMC, arXiv, RSC, ScienceDirect) supplemented by a targeted full-text extraction from the Stampi-Bombelli et al. (2024) DK paper. Once you regain Drive access, cross-check this guide against the PDFs already filed in `tier_0` and add any missing in-house notes to the 📝 boxes provided.

-----

## EXECUTIVE SUMMARY (one page)

This guide is built for a Year-3 polytechnic Design Project on CO₂ breakthrough in packed-bed columns with a Python Method-of-Lines (MOL) deliverable. It synthesises five focus areas — (i) Toth isotherm + LDF, (ii) Dual Kinetic (DK) model + dual-site Langmuir, (iii) travelling-wave / constant-pattern theory + Rankine–Hugoniot, (iv) MOL for stiff PDE→ODE systems, (v) a curated 2020–2026 literature survey.

**Bottom line for model selection.** For an isothermal benchtop packed bed of amine-functionalised pellets fed with 400 ppm CO₂, the literature strongly supports a **Toth equilibrium + single-LDF (PFO)** model as the *baseline*: Stampi-Bombelli et al. (2024) explicitly show that for packed beds the DK model collapses to the PFO solution (k₂ → k₁ or η → 1), and Pang, Sholl & Realff (2024) demonstrate the PFO–LDF + Toth combination reproduces benchtop DAC breakthroughs across temperature, flow and humidity. Move to **DK** only if you observe an unmistakable long tail in the breakthrough — a signature of two distinct timescales (fast surface amines + slow bulk amine-layer diffusion) — which Stampi-Bombelli found in monoliths but *not* in packed beds. For **Lewatit VP OC 1065** at sub-ambient temperatures, Mohajeri et al. (Chem. Eng. J. 2025) show the **dual-site Langmuir + PFO** outperforms Toth — Lewatit is a special case. 

**Bottom line for the wave-speed sanity check.** Before any numerical solve, hand-compute the Rankine–Hugoniot shock speed v_s = u·ε·Δc / [ε·Δc + (1−ε)·ρ_p·Δq]. Under DAC conditions, ε·Δc ≪ (1−ε)·ρ_p·Δq, so v_s ≈ u·ε·c_in/[(1−ε)·ρ_p·Δq], typically 10³–10⁴ times slower than the gas velocity. This sets the *expected breakthrough time* t_b ≈ L/v_s and is the single most powerful debugging tool for your MOL solver.

**Bottom line for solver design.** The 1D PDE system after spatial discretisation produces an extremely stiff ODE system (large NTU = k·L·(1−ε)/(ε·u), often 10²–10⁴ for DAC). Use **SciPy `solve_ivp` with `method='BDF'` or `'LSODA'`** (multi-step implicit), 100–300 finite-volume cells with **upwind for advection** and **central differences for dispersion**. Avoid explicit RK4: the CFL limit Δt < Δz/u combined with the LDF stiffness makes explicit schemes impractical.

**Top 4 papers to read first (TIER 0, in order):**

1. **Stampi-Bombelli, Storione, Grossmann, Mazzotti (2024)** — DK vs PFO formulation, Toth parameters, constant-pattern analysis; contains the exact equations you will code.
1. **Pang, Sholl, Realff (2024)** — Minimal PFO–LDF + Toth model for DAC; explicit MOL-friendly form; published Toth parameters for PEI/SBA-15 and PEI silica fibre.
1. **Elfving & Sainio (2021)** — Chemistry-based kinetic model for CO₂ on Lewatit including humid air; non-isothermal fixed-bed dynamics.
1. **Myers & Font (2020) + Anglada-Lloveras, Aguareles, Barrabés (arXiv 2507.16404, 2025)** — Travelling-wave reduction of the PDE system to an ODE; analytical breakthrough form and rigorous existence proof.

-----

## SECTION A — CONCEPTUAL FOUNDATION

### A1. Hierarchy of Adsorption Isotherms

The isotherm is the *thermodynamic* closure that tells the solid how much CO₂ it wants to hold at equilibrium with a given gas-phase concentration. Choosing too simple an isotherm makes the model wrong; choosing too complex an isotherm makes parameters un-identifiable from limited data.

**(a) Henry’s Law** — linear, valid only in the dilute, low-coverage limit:
$$q^{*} = K_{H},c \qquad \text{or} \qquad q^{*} = K_{H},p$$
*When appropriate:* sanity checking and analytical solutions (Klinkenberg 1948). *What breaks it:* any curvature in measured q*(p) — i.e., any approach to saturation.

**(b) Langmuir** — monolayer on energetically identical sites:
$$q^{*}(p,T) ;=; \frac{q_{m},b(T),p}{1 + b(T),p}, \qquad b(T) = b_{0}\exp!\left[\frac{-\Delta H}{R}!\left(\frac{1}{T}-\frac{1}{T_{0}}\right)\right]$$
*Assumptions:* (i) finite number of identical sites; (ii) one molecule per site; (iii) no lateral interactions; (iv) reversible adsorption with constant ΔH.  *What breaks it:* heterogeneity of site energies — amine sorbents have a *distribution* of amine environments (primary, secondary, water-stabilised carbamates, etc.) which Langmuir cannot capture.

**(c) Toth** — Langmuir with an empirical heterogeneity exponent t ∈ (0, 1]:
$$\boxed{,q^{*}(p,T) ;=; \frac{n_{s}(T),b(T),p}{\bigl[,1+(b(T),p)^{t(T)},\bigr]^{1/t(T)}},}$$

When t = 1, Toth collapses exactly to Langmuir. As t → 0, the surface is increasingly heterogeneous and the isotherm becomes more rectangular (sharper “knee” at low pressure, saturating earlier). For amine sorbents, t is typically sub-unity: t₀ = 0.25 for amine-grafted γ-alumina pellets (Stampi-Bombelli et al., *Ind. Eng. Chem. Res.* 63, 11637, 2024, Table 1)  and t₀ = 0.40 for PEI-impregnated silica fibre (Pang, Sholl & Realff, *Ind. Eng. Chem. Res.*, DOI: 10.1021/acs.iecr.3c04535, 2024);  Low et al. (*J. Chem. Eng. Data* 68, 3499, 2023) apply the same temperature-dependent Toth form to Lewatit VP OC 1065 and Purolite A110  with fitted τ₀ in the same sub-unity range, consistent with the physically known mix of carbamate, carbamic-acid and bicarbonate species.

The **temperature-dependent Toth** model used by virtually every DAC modelling paper (Stampi-Bombelli 2024 eqs 1–4; identical in Pang 2024, Young et al. 2021, Elfving & Sainio 2021):
$$n_{s}(T) = n_{s0}\exp!\bigl[\chi(1-T/T_{0})\bigr]$$
$$b(T) = b_{0}\exp!\left[\frac{\Delta H_{0}}{R,T_{0}}!\left(\frac{T_{0}}{T}-1\right)\right]$$
$$t(T) = t_{0} + \alpha\bigl(1-T_{0}/T\bigr)$$

Five fitted parameters per gas: (n_{s0}, b_{0}, t_{0}, ΔH_{0}, χ, α)  with reference temperature T₀ fixed  (commonly 298 K). For γ-alumina amine pellets (Stampi-Bombelli 2024, Table 1): n_{s0} = 1.23 mol/kg, b₀ = 4839 kPa⁻¹, t₀ = 0.25, ΔH₀ = 70 kJ/mol, χ = 0, α = 0.11.  For PEI-impregnated silica fibre (Pang et al. 2024): T₀ = 308 K, n_{s0} = 0.81 mmol/g, b₀ = 6.2 × 10³ kPa⁻¹, t₀ = 0.40, ΔH₀ = 210 kJ/mol, χ = 6.6, α = 10.8.  

**(d) Dual-site Langmuir** — explicit two-site model:
$$q^{*} ;=; \frac{q_{m,1},b_{1},p}{1+b_{1},p} + \frac{q_{m,2},b_{2},p}{1+b_{2},p}$$
The two sites have distinct saturation capacities (q_{m,1}, q_{m,2}) and affinities (b_{1}, b_{2}); each b_{i}(T) carries its own van’t Hoff form with separate ΔH_{i}. Mohajeri et al. (*Chem. Eng. J.* 2025) report for Lewatit VP OC 1065 dual-site fits with ΔH = −69.8 kJ/mol (high-energy site) and −50.0 kJ/mol (low-energy site), total capacity 3.32 mmol/g  — and explicitly find dual-site Langmuir + PFO–LDF outperforms Toth + PFO  across 400–2000 ppm and −10 to 40 °C.

**(e) DK–Toth (this project’s most general model)** — combine the Toth equilibrium with the dual-kinetic LDF closure (see A2 and Section B6). The equilibrium is still the single Toth q*(p,T), but the *approach* to q* is split: a fraction η of q* belongs to the fast site, (1 − η) to the slow site.

### A2. The Linear Driving Force (LDF) Approximation

The exact solid-phase mass transport is intraparticle diffusion:
$$\frac{\partial c_{p}}{\partial t} = \frac{D_{p}}{r^{2}},\frac{\partial}{\partial r}!\left(r^{2}\frac{\partial c_{p}}{\partial r}\right)$$
This is a PDE inside *each* PDE — prohibitively expensive in a column model. **Glueckauf (1955)** showed that for a spherical particle of radius r_p subjected to a step change at the external surface, the volume-averaged solid concentration q̄(t) approximately satisfies: 
$$\boxed{\frac{d\bar{q}}{dt} = k_{\mathrm{LDF}},\bigl(q^{*}-\bar{q}\bigr), \qquad k_{\mathrm{LDF}} ;=; \frac{15,D_{p}}{r_{p}^{2}}}$$
The factor 15 comes from matching the first eigenmode of the spherical diffusion equation; for slab geometry the constant is 3,  for an infinite cylinder it is 8. The derivation (Glueckauf 1955; re-derived rigorously in Sircar & Hufton 2000) is exact at long times and produces excellent breakthrough predictions even at moderate times.

**Number of Transfer Units (NTU)** — the dimensionless group governing front sharpness:
$$\mathrm{NTU} ;=; \frac{k_{\mathrm{LDF}},(1-\varepsilon),L}{\varepsilon,u} \quad \text{or, with }a_{p}\text{-factored form:}\quad \mathrm{NTU} = \frac{k_{\mathrm{LDF}},a_{p}(1-\varepsilon),L}{\varepsilon,u}$$
*Physical meaning:* the ratio of residence time L/u to the mass-transfer time constant 1/k_{LDF}. NTU ≫ 1 → equilibrium-limited, sharp shock-like front. NTU ≲ 1 → kinetics-limited, broad dispersed front. For DAC at 400 ppm with k_{LDF} ≈ 10⁻⁴ s⁻¹ (Stampi-Bombelli 2024, packed bed), L = 0.2 m and u = 0.1 m/s, NTU ≈ 2 — *moderate* sharpness, exactly the regime where LDF is informative.

For amine sorbents the LDF coefficient should not naively use 15D_p/r_p²: at 400 ppm CO₂, Stampi-Bombelli (2024) report k_{LDF} ≈ 8.8 × 10⁻⁵ s⁻¹ for the γ-alumina packed bed and 0.037 s⁻¹ for the monolith — *more than two orders of magnitude difference* despite the Toth equilibrium being shared (the monolith uses a scaled isotherm q*_mono = 0.035 q*_pellet).  

### A3. The Coupled 1D PDE System

For a 1D, isothermal packed bed with axial dispersion, the gas-phase mass balance is:
$$\varepsilon,\frac{\partial c}{\partial t} ;=; \varepsilon,D_{L},\frac{\partial^{2}c}{\partial z^{2}} ;-; \frac{\partial(u,c)}{\partial z} ;-; (1-\varepsilon),\rho_{p},\frac{\partial \bar{q}}{\partial t}$$
where:

- c [mol/m³] = gas-phase CO₂ concentration
- D_L [m²/s] = axial dispersion coefficient (Stampi-Bombelli 2024 fit: D_L = 6.95u + 0.02 for the packed bed; D_L = 1.22u² + 4 × 10⁻⁴ for the monolith) 
- u [m/s] = superficial velocity
- ε = bed voidage; canonical poured-bed value is ε ≈ 0.40 (range 0.35–0.44 from very dense to very loose random packing); Stampi-Bombelli et al. (2024) report ε_p = 0.71 for particle porosity of the 3 mm γ-alumina pellets  and use bed voidage consistent with this range
- ρ_p = particle density (1044 kg/m³ for γ-alumina pellets, Stampi-Bombelli 2024) 
- q̄ [mol/kg] = averaged solid loading

The solid LDF closure couples back:
$$\frac{\partial \bar{q}}{\partial t} ;=; k_{\mathrm{LDF}}!\left[,q^{*}(c,T) - \bar{q},\right]$$
where q*(c,T) is given by the Toth isotherm at the local gas concentration. The conversion p = cRT (ideal gas) is used to plug c into the Toth p-formulation.

**Non-isothermal extension** (Elfving & Sainio 2021; Stampi-Bombelli 2024 references Casas et al., *Adsorption* 2012, 18: 143–161, eqs 1–6 for the explicit form): 
$$\bigl[,\varepsilon,\rho_{g}c_{p,g} + (1-\varepsilon)\rho_{p}c_{p,s},\bigr]\frac{\partial T}{\partial t} = \lambda_{L}\frac{\partial^{2}T}{\partial z^{2}} - \rho_{g}c_{p,g}u\frac{\partial T}{\partial z} + (1-\varepsilon)\rho_{p}(-\Delta H)\frac{\partial \bar{q}}{\partial t} - \frac{4 h_{W}}{d_{c}}(T-T_{w})$$
The four coupling pathways the student must track:

1. **c → q̄** via Toth(c,T) in the LDF source term.
1. **q̄ → c** via the (1−ε)ρ_p ∂q̄/∂t sink in the gas balance.
1. **q̄ → T** via heat-of-adsorption release (−ΔH)∂q̄/∂t.
1. **T → q̄** via temperature dependence of n_s, b, t in the Toth isotherm.

The fourth coupling makes the system nonlinearly self-amplifying: adsorption releases heat, heat reduces b(T), reducing q*, reducing adsorption rate — a built-in negative feedback that broadens the front in non-isothermal beds.

**Boundary conditions** (Danckwerts):

- At z = 0: $;u,c_{0} = u,c - \varepsilon D_{L},\partial c/\partial z$
- At z = L: $;\partial c/\partial z = 0$

-----

## SECTION B — TRAVELLING-WAVE THEORY

### B1. Constant-Pattern Assumption

After a transient (≈ the first NTU of bed length), the wavefront in a column with favourable (concave-up) isotherm “self-sharpens” into a shape that propagates without further change. Mathematically, both c and q̄ become functions of a single co-moving coordinate:
$$\xi ;=; z - v_{s},t$$
i.e. c(z, t) = C(ξ), q̄(z, t) = Q(ξ). This is the **constant-pattern hypothesis**, also called the **travelling-wave ansatz** (Myers & Font 2020;  Anglada-Lloveras, Aguareles & Barrabés arXiv:2507.16404, 2025). 

Under this ansatz:
$$\frac{\partial c}{\partial t} = -v_{s}\frac{dC}{d\xi}, \qquad \frac{\partial c}{\partial z} = \frac{dC}{d\xi}, \qquad \frac{\partial^{2}c}{\partial z^{2}} = \frac{d^{2}C}{d\xi^{2}}$$
and the same for q̄.

### B2. ODE Reduction (step by step)

Substituting the ansatz into the gas-phase PDE (assuming constant u and ε):
$$-\varepsilon v_{s} C’ ;=; \varepsilon D_{L} C’’ - u C’ + (1-\varepsilon)\rho_{p} v_{s} Q’$$
Integrating once from ξ = +∞ (clean: C = 0, Q = 0) to ξ:
$$\varepsilon D_{L} C’ ;=; (u - \varepsilon v_{s}) C - (1-\varepsilon)\rho_{p} v_{s} Q$$
This is a **first-order ODE** in ξ, coupled algebraically to the LDF closure. With LDF:
$$-v_{s}Q’ ;=; k_{\mathrm{LDF}}\bigl[q^{*}(C) - Q\bigr]$$
Combining gives a single second-order ODE in C(ξ) with Q expressed implicitly through Q’. In the Myers–Font (2020) treatment, non-dimensionalisation reveals an inverse Péclet number 1/Pe = D_L/(uL) that is typically small  (∼10⁻³ at DAC velocities), permitting a **singular perturbation** reduction to a first-order ODE plus boundary layers — rigorously analysed by Anglada-Lloveras et al. (arXiv:2507.16404),   who prove the existence of a heteroclinic connection  between the clean and saturated states for small 1/Pe.

### B3. Rankine–Hugoniot Shock Condition — Derivation

In the **dispersion-free limit (D_L → 0, Pe → ∞)** with favourable isotherm, the smooth ODE solution collapses to a true shock at which C jumps from C_in to 0 and Q jumps from q* to 0. Integral conservation across the shock (Stampi-Bombelli 2024 SI §S1; standard chromatography theory) reads:

Mass conservation in a control volume moving with the shock:
$$\text{(flux in)} - \text{(flux out)} = \text{(accumulation)}$$
$$u,\Delta c ;=; v_{s}!\left[\varepsilon,\Delta c + (1-\varepsilon),\rho_{p},\Delta q\right]$$
giving:
$$\boxed{,v_{s} ;=; \frac{u,\Delta c}{\varepsilon,\Delta c + (1-\varepsilon),\rho_{p},\Delta q},}$$

Some authors absorb ε into u (defining interstitial u_i = u/ε); always check the convention. For DAC where Δc ≈ c_in ≈ 1.6 × 10⁻² mol/m³ (400 ppm at 1 atm, 25 °C) and Δq · ρ_p ≈ 1 mol/kg × 1044 kg/m³ = 1044 mol/m³ ≫ Δc, the formula simplifies to:
$$v_{s} ;\approx; \frac{u,\varepsilon,c_{in}}{(1-\varepsilon),\rho_{p},\Delta q}$$
*(With u in m/s, v_s is typically 10⁻³–10⁻⁴ × u.)*

### B4. How Toth Modifies the Wave Speed vs Langmuir

Δq depends entirely on the isotherm shape. For Langmuir, Δq = q_m·b·c_in/(1 + b·c_in) ≈ q_m·b·c_in for small b·c_in. For Toth, Δq = n_s·b·p_in/(1 + (b·p_in)^t)^{1/t} — at small p_in this becomes ≈ n_s·b·p_in (same as Langmuir), but at intermediate p_in the Toth’s “earlier saturation” with t < 1 means **Δq is larger** than Langmuir would predict at the same b, *for the same fitted capacity n_s*. This makes v_s *slower* and the breakthrough time *longer*. Practically: at 400 ppm DAC conditions you are deep in the low-pressure regime where Toth and Langmuir nearly coincide, *but the fitted b values differ by orders of magnitude* because the fit is global — so a Langmuir-fitted-to-Toth-data column model will give the wrong v_s. **Always fit and use the same isotherm form.**

### B5. Heat-of-Adsorption Correction (Non-isothermal Wave Speed)

For an adiabatic non-isothermal bed, the energy balance must be carried along with mass. Define the *retardation factor* including temperature:
$$R(T,c) ;=; 1 + \frac{(1-\varepsilon)\rho_{p}}{\varepsilon}!\left[,\frac{\partial q^{*}}{\partial c}\bigg|_{T} + \frac{\partial q^{*}}{\partial T}\bigg|_{c}\frac{dT}{dc},\right]$$
The non-isothermal wave speed is u/R. The new term ∂q*/∂T < 0 for exothermic adsorption (b decreases with T) — i.e., heat *reduces* the retardation and *speeds up* the wave. There can in principle be two coupled waves (a mass wave and a heat wave) propagating at different speeds, producing a “plateau region” between them; this is well known in adiabatic PSA modelling (LeVan & Vermeulen).

### B6. When the Constant-Pattern Solution Breaks Down

The travelling-wave / constant-pattern picture *requires*:

1. **Favourable isotherm** (Langmuir / Toth with t > 0): otherwise the front spreads rather than sharpens (Anglada-Lloveras et al. 2025).
1. **Single timescale**: with **DK kinetics**, q₁ and q₂ each obey LDF with different time constants k₁, k₂. If k₁ ≫ k₂, the fast site reaches equilibrium quickly while the slow site is still loading — producing a *two-stage* front: a sharp main front (controlled by k₁) plus a long exponential **tail** (controlled by k₂). Stampi-Bombelli (2024) state explicitly: *“In contrast to the packed bed experiments, the kinetics within the aminopolymer layer significantly affected k₂ in the monoliths, owing to the considerably larger value of k₁ compared to k_{s,amine}. This resulted in a substantial change in mass transfer kinetics during adsorption, which was particularly evident at higher concentrations, where the tail was more pronounced.”* 
1. **Isothermal**: a non-isothermal column has at least two waves, breaking the single-pattern assumption.

In the DK case the system *can* admit travelling waves under restrictive conditions (van der Zee 1990 showed this for two-site Langmuir + Freundlich combinations),  but the resulting front is composite and rarely admits a closed-form. For your Design Project, treat DK as a **regime that breaks the constant-pattern shortcut** — and rely on the numerical MOL solver instead.

-----

## SECTION C — PAPER-BY-PAPER READING GUIDE

### TIER 0 — read first (foundational equations and parameters)

-----

**[MODELLING] [TIER 0] [~3 h]** **Stampi-Bombelli, V.; Storione, A.; Grossmann, Q.; Mazzotti, M. (2024)** *“On Comparing Packed Beds and Monoliths for CO₂ Capture from Air Through Experiments, Theory, and Modeling.”* *Ind. Eng. Chem. Res.* 63(26): 11637–11653. DOI: 10.1021/acs.iecr.4c01392. Open access (PMC PMC11228921).

*Core claim:* For amine-grafted γ-alumina (3 mm pellets vs honeycomb monolith) at 400 ppm CO₂, mass-transfer coefficients drop two orders of magnitude relative to 5.6 % CO₂.   A pseudo-first-order LDF model fits packed-bed breakthroughs sufficiently, but the monolith requires a dual-kinetic (DK) model to capture the long tail. 

*Mathematical contribution:* The single most important paper for your project. It provides verbatim:

- Toth isotherm in temperature-dependent form (their eqs 1–4) — see Section A1.
- **PFO–LDF model (their eq 7):** ∂q/∂t = k(q* − q), with k assembled from film + pore + solid resistances by their eq 11: 1/k = 1/k_f + (q**{p,in}/c_in)·(1/k_p) + (q**{p,in}/c_in)·(1/k_s). 
- **DK model (their eqs 8–10):** q = q₁ + q₂; ∂q₁/∂t = k₁(η·q* − q₁); ∂q₂/∂t = k₂((1 − η)·q* − q₂).  η = fraction of fast-site amines.
- **DK rate constants (their eqs 12–15):** 1/k₁ = 1/k_g + (q*/c)·(1/k_s); 1/k₂ = 1/k₁ + 1/k_{s,amine}. 
- Constant-pattern analysis (their §3.1 and SI §S1) used as a *diagnostic* — they read off the limiting mass-transfer mechanism from the shape and asymmetry of the breakthrough. 

*Key fitted parameters (γ-alumina amine pellets, T₀ = 298 K):* n_{s0} = 1.23 mol/kg, b₀ = 4839 kPa⁻¹, t₀ = 0.25, ΔH₀ = 70 kJ/mol, χ = 0, α = 0.11. 

*Mass-transfer coefficients (Table 8):*

|Quantity|Packed bed, 400 ppm|Packed bed, 5.6 %|Monolith, 400 ppm|Monolith, 5.6 %|
|--------|-------------------|-----------------|-----------------|---------------|
|k₁ (s⁻¹)|8.8 × 10⁻⁵         |6.3 × 10⁻³       |0.037            |2.7            |
|k₂ (s⁻¹)|8.2 × 10⁻⁵         |1.0 × 10⁻³       |0.0011           |0.0011         |

For the packed bed k₁ ≈ k₂ → PFO suffices (DK is un-identifiable).  For the monolith k₁/k₂ = 33–2 500 → DK is needed.

*Pellet/bed properties:* d_p = 3 mm, ρ_p = 1044 kg/m³, ε_p = 0.71.  Dispersion D_L = 6.95u + 0.02 (m²/s) packed bed; D_L = 1.22u² + 4 × 10⁻⁴ monolith. 

*Authors’ verbatim conclusion (§3.2.3):* *“The successful application of the PFO model in modeling the packed bed experiments suggests that employing a DK model may not be necessary for this contactor. Indeed, attempts to use the DK model in fitting the packed bed breakthrough profiles resulted in: k₂ = k₁, for any value of η; or η = 1 for any value of k₂, leading to the same solution as the PFO model.”* 

*Answers for the project:* “Should I use DK or PFO?” — PFO for packed bed; DK only if a tail appears. “What does Toth fit look like for an amine sorbent?” — exactly the parameters above. “How do I do constant-pattern analysis?” — follow their §3.1 step by step. The SI (ie4c01392_si_001.pdf) contains the closed-form v_s.

📝 **MY NOTES:** ______________________________________

-----

**[MODELLING] [TIER 0] [~2 h]** **Pang, S. H.; Sholl, D. S.; Realff, M. J. (2024)** *“Minimal Kinetic Model of Direct Air Capture of CO₂ by Supported Amine Sorbents in Dry and Humid Conditions.”* *Ind. Eng. Chem. Res.* DOI: 10.1021/acs.iecr.3c04535. Open access PMC PMC10995953.

*Core claim:* A reduced isothermal model (PFO–LDF + Toth + GAB for water) reproduces published breakthroughs for SBA-15-amine and PEI-silica-fibre across temperature (25–60 °C), flow rate, and humidity (0–80 % RH)  using only 5–7 fitted parameters. Provides the “minimal viable model” template the project can implement directly.

*Mathematical contribution:* Their equation set is precisely the MOL-ready form you should code:

- Gas balance: ε·∂c/∂t + ∂(u·c)/∂z + (1 − ε)·ρ_B·∂q/∂t = ε·D_L·∂²c/∂z² (their eq 1). 
- LDF: ∂q/∂t = k(q_e − q) (their eq 2). 
- Toth equilibrium (their eq 3).
- Simplified “minimal” form drops dispersion (their eq 10)  — useful as a debug step. 

*Key parameters reported (PEI silica fibre, T₀ = 308 K):* n_{s0} = 0.81 mmol/g, b₀ = 6.2 × 10³ kPa⁻¹, t₀ = 0.40, ΔH₀ = 210 kJ/mol, χ = 6.6, α = 10.8. Water GAB: c_m = 26 mmol/g, c_G = 0.22, K_ads = 0.84.  

*Answers:* “What does a clean MOL implementation look like?” — their methodology. “Can I get away with isothermal model at benchtop scale?” — yes, they validate explicitly.  

📝 **MY NOTES:** ______________________________________

-----

**[MODELLING] [TIER 0] [~2.5 h]** **Elfving, J.; Sainio, T. (2021)** *“Kinetic approach to modelling CO₂ adsorption from humid air using amine-functionalized resin: Equilibrium isotherms and column dynamics.”* *Chem. Eng. Sci.* 246: 116885. DOI: 10.1016/j.ces.2021.116885. Open access (CC-BY).

*Core claim:* Develops a chemistry-based kinetic model for CO₂ on Lewatit VP OC 1065 in humid air. Models carbamate formation as a 2nd-order reaction (2 amines + CO₂); enhancement of equilibrium capacity by humidity emerges naturally from the kinetic framework. Validated against own non-isothermal breakthrough experiments. 

*Mathematical contribution:* Reaction kinetic constant fitted from breakthrough data.  Non-isothermal 1D model with energy balance.  Provides the cleanest derivation in the literature of how reaction stoichiometry (1 CO₂ : 2 amines dry; 1 CO₂ : 1 amine humid via bicarbonate) maps onto an “effective Langmuir-like” isotherm.

*Key results:* Humid CO₂ adsorption capacity up to 2× dry value;  fitted rate constants temperature- and humidity-dependent.

*Answers:* “How do I handle humidity?” “How does Lewatit differ from γ-alumina-grafted?” “What does a non-isothermal column model with energy balance look like?”

📝 **MY NOTES:** ______________________________________

-----

**[THEORY] [TIER 0] [~2 h]** **Myers, T. G.; Font, F. (2020)** *“Mass transfer from a fluid flowing through a porous media.”* arXiv:2009.08902.

*Core claim:* Develops the rigorous travelling-wave reduction of the column-adsorption PDE system, including the case of significant mass loss (relevant when the contaminant is a *major* component — not directly DAC, but the small-loss limit *is* DAC). Demonstrates by non-dimensionalisation which terms can be neglected and gives the analytical wave solution. 

*Mathematical contribution:* The single best reference for **deriving the wave speed and front shape from first principles**. Provides the dimensionless groups (Péclet, dimensionless adsorption number) and the systematic reduction to ODE.

*Answers:* “Where does the v_s formula come from?” “When can I use a travelling wave instead of a full PDE solve?”

📝 **MY NOTES:** ______________________________________

-----

### TIER 1 — read second (cross-check and extensions)

-----

**[EXPERIMENTAL/MODELLING] [TIER 1] [~2 h]** **Mohajeri, M. et al. (2025)** *“Comparing thermodynamic equilibrium isotherms, mechanistic kinetic models and mass transfer resistances for fixed bed CO₂ direct air capture (DAC).”* *Chem. Eng. J.*, ScienceDirect ID S1385894725107389.

*Core claim:* On Lewatit VP OC 1065 across −10 to 40 °C and 400–2000 ppm,  the **dual-site Langmuir + PFO–LDF outperforms Toth + PFO**. Heats of adsorption fitted at −69.8 kJ/mol (high-energy) and −50.0 kJ/mol (low-energy); total capacity 3.32 mmol/g.  Activation energy for chemisorption ≈ 60 kJ/mol (consistent with DFT). 

*Why important:* This is the **counter-example** to Toth being universal. If the project sorbent is Lewatit specifically, this paper supersedes Stampi-Bombelli’s Toth fit. It is also the cleanest dual-site Langmuir reference.

📝 **MY NOTES:** ______________________________________

-----

**[MODELLING] [TIER 1] [~2 h]** **Young, J.; García-Díez, E.; Garcia, S.; van der Spek, M. (2021)** *“The impact of binary water-CO₂ isotherm models on the optimal performance of sorbent-based direct air capture processes.”* *Energy Environ. Sci.* 14: 5377–5394. DOI: 10.1039/D1EE01272J.

*Core claim:* Builds a “weighted average dual-site Toth” (WADST) model for co-adsorption  of CO₂ and H₂O on Lewatit. Demonstrates via TVSA process optimisation that the minimum work equivalent varies across co-adsorption models and that different isotherm descriptions produce substantially divergent Pareto fronts for specific work vs productivity; the benchmark mechanistic model gives a minimum work equivalent of 2.49 MJ kg⁻¹ CO₂. 

*Why important:* The benchmark for *humid* CO₂ on Lewatit.   Provides systematic parameter sets and a clear discussion of why pure-component Toth + simple mixing rules fail.

📝 **MY NOTES:** ______________________________________

-----

**[THEORY] [TIER 1] [~2.5 h]** **Anglada-Lloveras, J.; Aguareles, M.; Barrabés, E. (2025/2026)** *“Analysis of travelling wave equations in sorption processes.”* arXiv:2507.16404 (April 2026 version).

*Core claim:* Rigorous singular-perturbation analysis of the column-adsorption travelling-wave ODE in the small-1/Pe limit; proves existence of a heteroclinic connection between the clean and saturated states. 

*Why important:* Mathematical justification for everything in Section B. Sensitivity analysis showing the wave speed is robust to small Péclet variation. 

📝 **MY NOTES:** ______________________________________

-----

**[MODELLING] [TIER 1] [~1.5 h]** **Grossmann, Q.; Stampi-Bombelli, V.; Yakimov, A.; Docherty, S.; Copéret, C.; Mazzotti, M. (2023)** *“Developing Versatile Contactors for Direct Air Capture of CO₂ through Amine Grafting onto Alumina Pellets and Alumina Wash-Coated Monoliths.”* *Ind. Eng. Chem. Res.* 62: 13594–13611.  Open access PMC PMC10472440.

*Core claim:* Reports CO₂ uptake kinetics measured by batch volumetric uptake on the same materials used in Stampi-Bombelli 2024. Fitted LDF k_s·a_p = 1.5 × 10⁻⁴ s⁻¹ (pellets), 1.2 × 10⁻³ s⁻¹ (monolith). 

*Why important:* The companion paper providing the *intrinsic* sorbent kinetics, independent of column geometry. Critical for separating sorbent properties from contactor properties when fitting.

📝 **MY NOTES:** ______________________________________

-----

**[MODELLING] [TIER 1] [~2 h]** **Stampi-Bombelli, V.; Mazzotti, M. (2024)** *“Exploring Geometric Properties and Cycle Design in Packed Bed and Monolith Contactors Using Temperature-Vacuum Swing Adsorption Modeling for Direct Air Capture.”* *Ind. Eng. Chem. Res.* 63: 19728–19743. DOI: 10.1021/acs.iecr.4c02303.

*Core claim:* Full cycle simulation of TVSA-DAC processes, integrating the adsorption modelling of the 2024 paper above. Uses LDF + Toth in PDE form for the adsorption step; non-isothermal energy balance throughout.

*Why important:* Shows how the breakthrough model is embedded in a full process simulation — the natural next step after the breakthrough project.

📝 **MY NOTES:** ______________________________________

-----

**[EXPERIMENTAL] [TIER 1] [~1 h]** **Elfving, J.; Kauppinen, J.; Jegoroff, M.; Ruuskanen, V.; Järvinen, L.; Sainio, T. (2021)** *“Experimental comparison of regeneration methods for CO₂ concentration from air using amine-based adsorbent.”* *Chem. Eng. J.* 404: 126337. DOI: 10.1016/j.cej.2020.126337.

*Core claim:* Compares TSA, TVSA and TVSA-with-purge regeneration on Lewatit. Per Elfving et al. (Chem. Eng. J. 404, 126337, 2021): all regeneration modes except closed TVSA (without purge flow) achieved > 85 % regeneration already at 60 °C;  isobaric TSA at 60 °C delivered the lowest specific energy requirement (SER) of 4.2 MJ/kgCO₂, while TVSA with mild vacuum + purge raised working capacity from 0.47 to 0.51 mmolCO₂/g at 7.5 MJ/kgCO₂, versus closed TVSA at 8.6 MJ/kgCO₂ at 100 °C. 

*Why important:* Companion regeneration paper to Elfving & Sainio (2021). Provides desorption parameters and validates the kinetic model in reverse.

📝 **MY NOTES:** ______________________________________

-----

### TIER 2 — background and corroboration

-----

**[THEORY] [TIER 2] [~1 h]** **Glueckauf, E. (1955)** *“Theory of chromatography. Part 10. Formulae for diffusion into spheres and their application to chromatography.”* *Trans. Faraday Soc.* 51: 1540. The original LDF derivation; gives k_LDF = 15D_p/r_p². Read for completeness; modern textbook treatments (Ruthven 1984; Do 1998) are easier.

📝 **MY NOTES:** ______________________________________

-----

**[THEORY] [TIER 2] [~30 min]** **Klinkenberg, A. (1948)** *Ind. Eng. Chem.* 40: 1992. Analytical approximation to the Anzelius convection-mass-transfer problem with linear isotherm:
$$\frac{C}{C_{F}} \approx \frac{1}{2}!\left[,1+\mathrm{erf}!\left(\sqrt{\tau}-\sqrt{\xi}+\frac{1}{8\sqrt{\tau}}+\frac{1}{8\sqrt{\xi}}\right),\right]$$ 
with τ = K(t − z/u_i)·H/ε_b, ξ = K·z·H/(u_i·ε_b). Use as a **sanity-check analytical solution** for your MOL solver in the *linear-isotherm limit*. If your solver doesn’t match Klinkenberg in that limit, it has a bug.

📝 **MY NOTES:** ______________________________________

-----

**[THEORY] [TIER 2] [~45 min]** **Thomas (1948) / Bohart–Adams (1920)** models — analytical breakthrough formulas. Critical observation by Chu (*J. Hazard. Mater.* 2010, PMID 20096997): *the Bohart-Adams and Thomas models are mathematically identical with re-named parameters*.  The Thomas form:
$$\frac{C}{C_{0}} = \frac{1}{1+\exp!\bigl[k_{T}(q_{0}m - C_{0},V_{eff})/Q\bigr]}$$
is convenient for **fitting** experimental breakthrough data to extract empirical k_T and q₀, but does NOT predict from first principles. For design use the LDF + isotherm model. Worth knowing because nearly every experimental DAC paper fits these as a first pass.

📝 **MY NOTES:** ______________________________________

-----

**[REVIEW] [TIER 2] [~1.5 h]** **(2024 review)** *“A critical review of breakthrough models with analytical solutions in a fixed-bed column.”* *Sustainable Chemistry and Pharmacy*, ScienceDirect S2214714424002976. Surveys all analytical breakthrough models, clarifies common mistakes, discusses asymmetric breakthrough curves. 

📝 **MY NOTES:** ______________________________________

-----

**[EXPERIMENTAL] [TIER 2] [~1 h]** **Low, M.-Y. A.; Danaci, D.; Azzan, H.; Woodward, R. T.; Petit, C. (2023)** *“Measurement of Physicochemical Properties and CO₂, N₂, Ar, O₂, and H₂O Unary Adsorption Isotherms of Purolite A110 and Lewatit VP OC 1065 for Application in Direct Air Capture.”* *J. Chem. Eng. Data* 68: 3499–3511. DOI: 10.1021/acs.jced.3c00401. The benchmark physicochemical-properties paper for Lewatit (and a comparable resin, Purolite A110).  Open access PMC PMC10726313.

📝 **MY NOTES:** ______________________________________

-----

**[MODELLING] [TIER 2] [~1 h]** **Storione, A.; Stampi-Bombelli, V. et al. (2025)** *“Mass Transfer of CO₂ in Amine-Functionalized Structured Contactors in Ultra-Dilute Conditions.”* *Ind. Eng. Chem. Res.* DOI: 10.1021/acs.iecr.4c04099. Companion to Stampi-Bombelli 2024; quantifies separate film, macropore, and amine-layer diffusivities using a commercial volumetric device modified to remove instrument resistances. 

📝 **MY NOTES:** ______________________________________

-----

**[EXPERIMENTAL] [TIER 2] [~30 min]** **Wilkins et al. (2024)** *“Evaluation of CO₂/H₂O Co-Adsorption Models for the Anion Exchange Resin Lewatit VPOC 1065 under Direct Air Capture Conditions Using a Novel Lab Setup.”* *MDPI Separations* 11(6): 160. Compares Toth co-adsorption models against new experimental data; finds the weighted-average dual-site Toth (WADST) of Young et al. 2021 fits best. 

📝 **MY NOTES:** ______________________________________

-----

**[MODELLING] [TIER 2] [~1.5 h]** **Stampi-Bombelli, V.; van der Spek, M.; Mazzotti, M. (2020)** *“Analysis of direct capture of CO₂ from ambient air via steam-assisted temperature–vacuum swing adsorption.”* *Adsorption* 26: 1183–1197. DOI: 10.1007/s10450-020-00249-w.  The original “SB” co-adsorption model for amine sorbents in DAC processes;  widely used in subsequent literature despite later critique (Young 2021; RSC Energy Advances 2026 D5YA00336A) that the SB formulation cannot properly describe CO₂ desorption. 

📝 **MY NOTES:** ______________________________________

-----

**[REVIEW] [TIER 2] [~1 h]** **Sabatino, F.; Grimm, A.; Gallucci, F.; van Sint Annaland, M.; Kramer, G. J.; Gazzani, M. (2021)** *“A comparative energy and costs assessment and optimization for direct air capture technologies.”* *Joule* 5: 2047–2076. DOI: 10.1016/j.joule.2021.05.023. Process-level comparison of liquid scrubbing vs solid-sorbent DAC;  provides baseline cost benchmarks and a complete TVSA-DAC process model that includes the adsorption sub-model the project is building.

📝 **MY NOTES:** ______________________________________

-----

## SECTION D — SYNTHESIS

### D1. Model Selection Logic

|Scenario                                         |Isotherm                                       |Kinetics           |Justification                                      |
|-------------------------------------------------|-----------------------------------------------|-------------------|---------------------------------------------------|
|Linear-isotherm sanity check                     |Henry                                          |LDF                |Klinkenberg analytical = solver validation         |
|Generic packed-bed DAC (γ-alumina, PEI/silica)   |**Toth**                                       |**PFO–LDF**        |Stampi-Bombelli 2024 packed bed; Pang 2024 baseline|
|Lewatit specifically                             |**Dual-site Langmuir**                         |PFO–LDF            |Mohajeri 2025; Toth underperforms here             |
|Monolith with visible tail                       |Toth                                           |**DK (2-site LDF)**|Stampi-Bombelli 2024 §3.2.3                        |
|Humid air                                        |dual-site Toth WADST or Elfving-Sainio reaction|LDF                |Young 2021; Elfving & Sainio 2021                  |
|Non-isothermal (large columns or high feed conc.)|Toth                                           |LDF                |+ energy balance with −ΔH·∂q̄/∂t source             |

The dispositive question is **“do I see a tail in my breakthrough?”**. If yes → DK or dual-site Langmuir. If no → PFO + Toth (or PFO + Langmuir if a quick fit shows Langmuir is adequate). Always plot breakthrough on both linear and log axes; tails are often invisible linearly.

### D2. Parameter Estimation Workflow

1. **Equilibrium data first.** Run static isotherm measurements (TGA or volumetric) at ≥ 3 temperatures spanning the column operating range. Fit Toth (or dual-site Langmuir) — get (n_{s0}, b₀, t₀, ΔH₀, χ, α). Without good equilibrium data, no kinetic fit is meaningful.
1. **Mass transfer next, in two steps.**
- (a) *Intrinsic sorbent kinetics:* batch volumetric uptake (Grossmann 2023 method) at the operating partial pressure. Fit LDF k from the uptake curve. This gives k_intrinsic ≈ 15D_p/r_p² (Glueckauf).
- (b) *Column kinetics:* breakthrough experiment with full mass-transfer-zone development (use the constant-pattern diagnostic from Stampi-Bombelli 2024 §3.1). Fit the column k including external film/pore. If k_column ≈ k_intrinsic, internal diffusion dominates; if not, look for axial dispersion (Pe < 50) or wall channelling.
1. **Dispersion D_L** from a non-adsorbing tracer pulse (e.g., He pulse with TCD), or from velocity-dependence: D_L = αu + β with α from typical correlations (Edwards-Richardson or Wakao).
1. **Check for DK signature.** If breakthrough exhibits a fast rise to ∼0.8C₀ followed by a slow tail to 1.0, fit DK; otherwise PFO.
1. **Heat of adsorption ΔH₀** from Clausius-Clapeyron on the isotherm set at multiple T, OR from microcalorimetry — typically 60–90 kJ/mol for chemisorbing solid amine sorbents, per Robertson et al. (*ACS Appl. Polym. Mater.* 6, 14169, 2024): *“average chemisorption heats of sorption range between 60 and 90 kJ/mol”*;  consistent with Mohajeri et al. (2025) reporting −69.8 and −50.0 kJ/mol for the two Lewatit sites,  and Stampi-Bombelli (2024) reporting ΔH₀ = 70 kJ/mol for γ-alumina amine pellets. 

### D3. Validation Hierarchy

1. **Analytical:** Klinkenberg linear-isotherm solution — your MOL solver must match in the linear limit.
1. **Constant-pattern:** Rankine–Hugoniot v_s prediction of breakthrough time (within 10–20 % once tails are accounted for).
1. **Benchmark numerical:** reproduce Figure 7 of Stampi-Bombelli 2024 (their published k₁, k₂, and isotherm parameters) and Figure 4 of Pang 2024 (PEI silica fibre breakthrough). If your code reproduces both, it’s trustworthy.
1. **Own experiments:** then and only then fit to your own data — and validate at conditions *not used in fitting* (cross-validation).

### D4. MOL Solver Recommendations for Python

- **Spatial discretisation:** finite volume; upwind (first-order) for the convective term ∂(uc)/∂z, central for the dispersive term D_L·∂²c/∂z². 100–300 cells is sufficient for most DAC problems. Avoid second-order upwind unless you implement a flux limiter (Van Leer or Superbee) — without one you get spurious oscillations near the breakthrough front.
- **Time integration:** `scipy.integrate.solve_ivp(method='BDF', rtol=1e-6, atol=1e-9)` or `method='LSODA'`. LSODA auto-switches between Adams and BDF and is often most robust. For very stiff cases (high NTU) use `Radau`. *Never* use `RK45` for stiff column problems.
- **Jacobian:** providing the analytical Jacobian (or even a sparsity pattern) accelerates BDF by 10×. For a banded tridiagonal-like Jacobian (typical of MOL with upwind + central), pass `jac_sparsity` as a sparse matrix.
- **CFL warning:** even with implicit methods, accuracy degrades if Δt > Δz/u (the convective Courant condition). Let the solver choose Δt adaptively rather than forcing it.

### D5. Key Unresolved Questions Relevant to This Project

1. **Whether the DK model is unique** — Stampi-Bombelli (2024) acknowledge that for packed beds, η and k₂ become un-identifiable (any pair (η = 1, k₂) or (k₂ = k₁, η) gives the same fit).  For monoliths it is identifiable; for packed beds you cannot extract DK parameters from breakthrough alone.
1. **Whether Toth or dual-site Langmuir is more “physical”** for amine sorbents — Mohajeri (2025) prefers dual-site Langmuir with two distinct ΔH (chemically interpretable as two amine types); Stampi-Bombelli (2024) prefers Toth (mathematical simplicity, one fewer parameter). Both fit well; neither is mechanistically derived.
1. **The role of humidity in column dynamics** — Young (2021), Elfving & Sainio (2021), and the swelling-paper by Piscina & van der Spek (2024 SSRN) all give *different* mechanistic pictures. For a dry benchtop project, defer; if humidity is needed, start with Young’s WADST.
1. **The travelling-wave solution for DK systems** — open mathematically; Anglada-Lloveras et al. (2025) handle only single-LDF. If the project finds a clean two-stage wave numerically, that is a publishable contribution.

-----

## RECOMMENDATIONS — staged next steps

**Stage 1 (week 1): build the baseline.** Implement an isothermal PFO–LDF + Toth MOL solver in Python following Pang et al. (2024) exactly. Hard-code the γ-alumina parameters from Stampi-Bombelli 2024 Table 1 and the k_LDF = 8.8 × 10⁻⁵ s⁻¹ from Table 8. Run at 400 ppm, T = 25 °C, u = 0.1 m/s, L = 0.2 m. **Success criterion:** breakthrough time within 20 % of the Rankine–Hugoniot prediction t_b = L/v_s. **Trigger to escalate:** if the simulated breakthrough is < 50 % or > 200 % of v_s prediction, the implementation is wrong; debug before adding complexity.

**Stage 2 (week 2): validate.** Reproduce Figure 7 (packed bed) of Stampi-Bombelli 2024 by feeding their published parameters. **Success criterion:** the simulated curve must overlay their experimental curve to the eye on the log-time axis. **Trigger to escalate:** if not, check ε, ρ_p, the b₀ unit (kPa vs Pa), and the gas-phase concentration unit (mol/m³ vs mol/kg-gas).

**Stage 3 (week 3): add the DK option.** Extend the solver with the two-loading DK formulation (Stampi-Bombelli 2024 eqs 8–10), making it a runtime flag. Test on the monolith case (k₁ = 0.037, k₂ = 0.0011, η = 0.75 from their Table 7).  **Success criterion:** reproduce the long tail in their Figure 7b.

**Stage 4 (week 4): non-isothermal extension.** Add the energy balance (Section A3). **Success criterion:** at 5.6 % CO₂ feed (where ΔT ≈ 5–10 K), the simulated breakthrough should be visibly shifted earlier than the isothermal prediction.

**Stage 5 (week 5+): own experiments.** Conduct breakthrough experiments at one feed concentration and one temperature. Fit k_LDF (PFO) only; do not attempt DK unless an unambiguous tail is observed. Cross-validate at a different velocity.

**Benchmarks that would change these recommendations:**

- If the project sorbent is Lewatit specifically → swap Toth for dual-site Langmuir (Mohajeri 2025) at Stage 1.
- If humid feed is mandated → add water co-adsorption following Young 2021 WADST or Elfving-Sainio 2021 at Stage 4 (not earlier).
- If columns are short (L < 50 mm) → the constant-pattern assumption may fail; the wave-speed validation in Stage 1 will tell you immediately (poor agreement → use full PDE solve only).

-----

## CAVEATS

- This guide synthesises searched literature; the project student should obtain and verify every cited paper, especially the closed-form Rankine–Hugoniot expression which is in the Stampi-Bombelli 2024 Supporting Information (ie4c01392_si_001.pdf), not the main text.
- The 1D gas-phase PDE that Stampi-Bombelli (2024) actually uses is by reference to Casas et al. (*Adsorption* 2012, 18: 143–161, eqs 1–6);  for an exact verbatim form, retrieve Casas et al.
- Some fitted parameters in Stampi-Bombelli (2024) are weakly constrained — e.g. the packed-bed solid mass-transfer coefficient k_s ≈ 5.8 × 10⁵ s⁻¹ vs literature 1.9 × 10⁴  — because the solid resistance is not the limiting one and is therefore poorly identifiable from the fit. The authors flag this explicitly.
- The Anglada-Lloveras et al. arXiv paper is dated April 2026 in some metadata snapshots; treat as preprint until peer-reviewed.
- The Google Drive folder `./ES/#design project/literature/tier_0` was not accessible from this environment; any internal in-house literature notes already filed there should be merged with this guide manually.
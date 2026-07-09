# Dissection Prompt — Validate the Roadmap & Prove/Disprove the Model
*Target document: `Adsorption_Breakthrough_Research_Roadmap.docx` (13 papers + 1 technical reference, Pillars A–C, 1-D axial non-isothermal CO₂/N₂ fixed-bed breakthrough). This prompt is self-contained: everything the target model needs is reproduced below in "Information you may or may not need." Send as-is to a fresh model instance with no other context and no internet access.*

---

## PROMPT (send as-is)

Don't search the internet. Part of this is a test to see how well you can craft non-trivial, novel and creative proofs given a math problem — for that part, provide a full **unconditional** proof or disproof. REMEMBER: the unconditional argument in Part II may require non-trivial, creative and novel elements, not a recitation of a textbook theorem.

You are dissecting a literature-review roadmap for a 1-D axial, non-isothermal fixed-bed CO₂ (in inert N₂) adsorption model. Do two things, in order.

### Part I — Validate the roadmap itself

The roadmap's "Consolidated Governing-Equation Reference Sheet" claims to synthesize, in one consistent notation, the equations extracted from 13 sources across three pillars (A: isotherms & T-dependence, B: LDF kinetics evidence, C: numerical integration). Audit that synthesis. For each item below, give a verdict — **valid**, **invalid**, or **valid-with-qualification** — and justify it from the equations themselves, not from authority:

1. **Dimensional consistency.** Check every governing equation below (mass balance, LDF rate law, DSL isotherm + Arrhenius terms, energy balance) term-by-term for dimensional homogeneity. Report any term that cannot balance under the stated definitions of ε, u, D_L, ρ_p, c_p,g, c_p,s, λ_eff, h_w.

2. **Single-component reduction.** The isotherm sheet is written for a general species index *i* with sums Σ_j b_j c_j and Σ_j d_j c_j (multi-site, multi-species Dual-Site Langmuir, per Fabian Ramos et al. 2024). The roadmap's own framing treats N₂ as an inert, non-adsorbing carrier and CO₂ as the *only* adsorbable species. Prove whether Σ_j b_j c_j collapses cleanly to the single term b·c (and likewise for d_j) under that stated assumption, or identify a hidden condition (e.g. on how N₂ physisorption is being neglected) that this reduction silently requires.

3. **Stiffness argument.** The roadmap justifies BDF/LSODA over explicit RK45 by arguing k_LDF is "typically orders of magnitude faster than the convective residence time L/u," producing "a large spread of eigenvalues." Reconstruct this argument rigorously: state what the relevant eigenvalues of the semi-discretized Jacobian actually are (convective term, dispersive term, the LDF term, and the Arrhenius-coupled energy term), and determine whether the stated conclusion (stiffness ⇒ implicit integrator required) actually follows, or whether the roadmap has conflated "stiff" with merely "multi-timescale."

4. **Front-formation claim.** The roadmap asserts a favourable isotherm drives concentration *and* the coupled temperature profile toward a "constant-pattern, shock-like front," citing Ruthven Ch. 8 and the Lax entropy condition / genuine nonlinearity framework (LeVeque Ch. 6–7, Evans Ch. 3) as the formal backing. Those citations concern a *scalar* hyperbolic conservation law. Determine whether their conclusions transfer as stated to this *coupled two-field* (concentration + temperature) hyperbolic system without further argument, or whether the roadmap is overreaching by citing scalar shock theory for a system it does not, on its own, cover.

Produce a short verdict table for items 1–4, then proceed to Part II regardless of what Part I finds — Part II is a harder, independent claim that Part I's outcome does not resolve.

### Part II — Mathematical soundness: derivation and proof

**Step 1 (derivation, not optional).** Starting only from conservation of mass and energy on a differential control volume of the bed (do not just restate the sheet — derive it), reproduce:
(a) the fluid-phase mass balance,
(b) the energy balance,
(c) the isothermal (T fixed) constant-pattern wave speed θ_iso from a Rankine–Hugoniot jump condition on the mass balance alone, in closed form in terms of ε, u, ρ_p, and Δq/Δc across the front.
Show every step; state which terms are assumptions (e.g. plug flow, no radial gradients, pseudo-homogeneous solid) versus consequences of conservation.

**Step 2 (the claim to prove or disprove).** Consider the full coupled system in "Information you may or may not need" below: mass balance + LDF kinetics + temperature-dependent Dual-Site Langmuir isotherm (Arrhenius b(T), d(T)) + energy balance.

> **Claim (Non-Isothermal Constant-Pattern Uniqueness).** Suppose the isotherm is favourable at every temperature attained during breakthrough (∂²q*/∂c² ≤ 0 at fixed T, over the relevant concentration range) and the column is adiabatic (h_w = 0). Then:
> (a) the coupled PDE system admits a *unique* constant-pattern (travelling-wave) solution (c, q, T)(z − θt) connecting the initial bed state (c=0, q=0, T=T₀) to the feed state (c=c_feed, T=T_feed) as t → ∞, and
> (b) the wave speed θ is uniquely determined in closed form by simultaneous mass and energy Rankine–Hugoniot jump conditions across the front, independent of D_L and independent of k — even though b(T) and d(T) vary nonlinearly across the front.

Prove this claim in full generality for the system given, or disprove it by exhibiting the specific mechanism (nonlinearity, coupling term, or boundary behavior) that breaks uniqueness or breaks the closed-form wave-speed result. If false as stated, identify the minimal additional hypothesis that restores it, and prove the corrected statement instead.

Your answer must directly engage with:
- why the classical single-component **isothermal** constant-pattern theorem you derived in Step 1(c) does *not* automatically transfer once T is a coupled field;
- whether the Lax entropy condition / genuine nonlinearity framework for the hyperbolic (convective) part alone is sufficient to select the front, or whether the parabolic (D_L, λ_eff) regularization terms are doing essential work in selecting *which* weak solution survives;
- whether Arrhenius coupling through b(T), d(T) can produce non-monotonic loading or a two-wave (split concentration/temperature front) structure that the claim does not anticipate — construct an explicit parameter regime that tests this, don't just assert it abstractly.

Do not cite that such theorems "are known" — construct or refute the argument from the governing equations given. This is where the non-trivial, creative, novel element is required: a routine restatement of Ruthven's isothermal result, or of Danilov et al.'s semi-analytical treatment, does not settle the coupled uniqueness/closed-form question — neither source proves it, so recall alone cannot answer this.

---

## Information you may or may not need (self-contained — extracted from the roadmap)

**Notation.** c: gas-phase CO₂ concentration; q: adsorbed-phase loading; q*: equilibrium loading; T: pseudo-homogeneous gas/solid temperature; z: axial coordinate; t: time; ε: bed voidage; u: interstitial velocity; D_L: axial dispersion coefficient; ρ_p: particle density; ρ_g, c_p,g: carrier-gas density/heat capacity; c_p,s: solid heat capacity; λ_eff: effective axial thermal conductivity; h_w: wall heat-transfer coefficient; d_col: column diameter; T_wall: wall temperature; R: gas constant.

**1. Fluid-phase mass balance (single adsorbable species)**
ε ∂c/∂t + u ∂c/∂z = ε D_L ∂²c/∂z² − (1−ε) ρ_p ∂q/∂t
(Ruthven Eq. 8.1; Fabian Ramos et al. 2024, Eq. 4)

**2. LDF kinetics**
dq/dt = k(q* − q), k = 15 D_eff / r_p²
(Glueckauf 1955, via Ruthven §8.5; Fabian Ramos Eqs. 12–13)

**3. Equilibrium isotherm — Dual-Site Langmuir, general multi-species form as given in the roadmap sheet**
qᵢ* = q_{1,i} b_i c_i /(1 + Σ_j b_j c_j) + q_{2,i} d_i c_i /(1 + Σ_j d_j c_j)
b_i = b_{0,i}·exp(−ΔU_{b,i}/RT), d_i = d_{0,i}·exp(−ΔU_{d,i}/RT)
(Fabian Ramos Eqs. 14–16; single-adsorbable-species reduction is Part I, item 2, above)

**4. Energy balance (non-isothermal)**
[ε ρ_g c_p,g + (1−ε) ρ_p c_p,s] ∂T/∂t + u ρ_g c_p,g ∂T/∂z = λ_eff ∂²T/∂z² + (1−ε) ρ_p (−ΔH) ∂q/∂t − (4h_w/d_col)(T − T_wall)
Isosteric heat: −ΔH(T,q) = −ΔU + RT (+ empirical loading correction for CO₂)
(Fabian Ramos Eq. 7 & Eqs. 9–10; Danilov et al. 2019 §3)

**5. Boundary / initial conditions (standard for this problem class — not stated verbatim in the roadmap, flag as an assumption if you rely on a specific form)**
- Danckwerts-type inlet: u c_feed = u c(0,t) − ε D_L ∂c/∂z|_{z=0}, analogous form for T; zero-gradient at outlet.
- Initial bed: c(z,0) = 0, q(z,0) = 0, T(z,0) = T₀.
- Feed step: c(0,t) = c_feed, T(0,t) = T_feed for t > 0.

**6. Semi-discretised (Method of Lines) form**
State vector y(t) = [c, q, T]ᵀ per axial node; dy/dt = f(t,y) after replacing ∂/∂z, ∂²/∂z² with upwind/flux-limited stencils (LeVeque Ch. 6–7 justify upwind bias near shock-like fronts). Integrated via `solve_ivp(f, t_span, y0, method='BDF'|'LSODA', jac=..., rtol≤1e-6, atol≤1e-9)`.

**7. Background relevant to both parts (not required, but available)**
- Roadmap's stiffness argument: k typically ≫ u/L; a favourable isotherm (∂²q*/∂c² ≤ 0) drives the isothermal system toward a self-sharpening "constant pattern" front (Ruthven Ch. 8; Garg & Ruthven 1973 asymptotic solutions).
- Isothermal, dispersion-free wave speed (the special case Part II, Step 1(c) must reproduce and Part II, Step 2 must show does or doesn't generalise): θ = uε / [ε + (1−ε)ρ_p·Δq/Δc] (Rankine–Hugoniot form on the mass balance).
- Danilov et al. (2019) derive an analytical simplification for the driving force via ∂y/∂t = (∂y/∂q)(∂q/∂t) but close the remaining coupled non-isothermal system *numerically* — they do not themselves prove a closed-form non-isothermal wave speed. This is a genuine gap in the 13-source library, not a result the roadmap can be checked against.
- Kumar (1986): multicomponent constant-pattern theory shows competing fronts can separate into multiple waves — structurally relevant to whether concentration and temperature fronts can decouple under strong Arrhenius coupling (Part II's third engagement point).
- Ruthven (1984) §8.6 states the LDF/diffusion equivalence "breaks down when the isotherm is highly nonlinear" — a caveat on how much weight the LDF closure itself can bear inside any proof.

---

## Notes for the lead researcher (not part of the sent prompt)

- Part I is deliberately checkable against the roadmap text itself — a competent model should be able to find at least one place where the roadmap's citation-to-claim mapping is looser than it reads (most likely candidates: item 3's stiffness reasoning, which is physically right but stated qualitatively rather than derived; and item 4's citation of scalar shock theory for a two-field system).
- Part II's claim is unresolved in the 13-source library by construction (see background note above), so a correct response has to actually derive something, not recall it. Expected failure modes: (1) silently letting D_L → 0, h_w → 0 collapse the problem back to the isothermal case without checking that T still couples through b(T), d(T) at zero dispersion; (2) asserting uniqueness without checking whether the concentration and temperature characteristic speeds can generically split into two fronts.
- Suggest running this once and, separately, running Part II alone at a different sampling temperature as a consistency check before trusting the verdict — diff the two derivations for whether they commit to the same corrected statement (if the claim is disproved).

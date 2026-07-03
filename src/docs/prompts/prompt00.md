# Proof/Disproof Challenge Prompt — Non-Isothermal Fixed-Bed CO₂ Adsorption

*Source dissected: `Adsorption_Breakthrough_Research_Roadmap.docx` (13 papers + 1 technical reference, Pillars A–C). This prompt is self-contained — the target model receives no other context and must not search the internet.*

---

## PROMPT (send as-is)

Don't search the internet. This is a test to see how well you can craft non-trivial, novel and creative proofs given a "**Non-Isothermal Constant-Pattern Uniqueness**" math problem. Provide a full unconditional proof or disproof of the problem.

REMEMBER — this unconditional argument may require non-trivial, creative and novel elements.

### The problem

Consider a single adsorbable species (CO₂) in an inert carrier (N₂) flowing through a 1-D fixed bed, governed by the coupled system below (mass balance, LDF kinetics, temperature-dependent Dual-Site Langmuir isotherm, energy balance). The isotherm's affinity parameters depend on temperature through an Arrhenius law, so the mass and energy equations are nonlinearly coupled — this is what makes the system "non-isothermal."

**Claim.** Suppose the isotherm is favourable at every temperature attained during breakthrough (i.e. ∂²q*/∂c² ≤ 0 at fixed T, over the relevant concentration range) and the column is adiabatic (h_w = 0, no wall heat loss). Then:

(a) the coupled PDE system admits a unique constant-pattern (travelling-wave) solution (c, q, T)(z − θt) connecting the initial bed state (c=0, q=0, T=T₀) to the feed state (c=c_feed, T=T_feed) as t → ∞, and

(b) the wave speed θ is uniquely determined in closed form by simultaneous mass and energy conservation (Rankine–Hugoniot-type jump conditions across the front), independent of the axial-dispersion coefficient D_L and independent of the LDF rate constant k — even though b(T) and d(T) vary nonlinearly across the front.

Prove this claim in full generality for the system given, or disprove it by exhibiting the specific mechanism (nonlinearity, coupling term, or boundary behavior) that breaks uniqueness or breaks the closed-form wave-speed result. If the claim is false as stated, identify the minimal additional hypothesis (if any) that would restore it, and prove the corrected statement instead.

Your answer must directly engage with:
- why the classical single-component **isothermal** constant-pattern theorem (favourable isotherm ⇒ unique constant pattern, Rankine–Hugoniot wave speed from mass balance alone) does *not* immediately transfer once T is a coupled field;
- whether the Lax entropy condition / genuine nonlinearity framework for the hyperbolic (convective) part of the system is sufficient on its own, or whether the parabolic (dispersive/diffusive) regularization terms are doing essential work in selecting the unique front;
- whether coupling through an Arrhenius b(T), d(T) can produce non-monotonic or multi-wave (two-front) structures that the claim as stated does not anticipate.

Do not simply cite that such theorems "are known" — construct or refute the argument from the governing equations below.

---

## Information you may or may not need (mathematical skeleton extracted from the roadmap)

**Notation.** c: gas-phase CO₂ concentration; q: adsorbed-phase loading; q*: equilibrium loading; T: pseudo-homogeneous gas/solid temperature; z: axial coordinate; t: time; ε: bed voidage; u: interstitial velocity; D_L: axial dispersion coefficient; ρ_p: particle density; ρ_g, c_p,g: carrier gas density/heat capacity; c_p,s: solid heat capacity; λ_eff: effective axial thermal conductivity; h_w: wall heat-transfer coefficient; d_col: column diameter; T_wall: wall temperature; R: gas constant.

**1. Fluid-phase mass balance (single adsorbable species)**
ε ∂c/∂t + u ∂c/∂z = ε D_L ∂²c/∂z² − (1−ε) ρ_p ∂q/∂t
(Ruthven Eq. 8.1; Fabian Ramos et al. 2024, Eq. 4)

**2. LDF kinetics**
dq/dt = k(q* − q),  k = 15 D_eff / r_p²
(Glueckauf 1955, via Ruthven §8.5; Fabian Ramos Eqs. 12–13)

**3. Equilibrium isotherm — Dual-Site Langmuir, single component**
q* = q₁ b c /(1 + b c) + q₂ d c /(1 + d c)
b = b₀ · exp(−ΔU_b / RT),  d = d₀ · exp(−ΔU_d / RT)
(Fabian Ramos Eqs. 14–16, reduced to one adsorbable species)

**4. Energy balance (non-isothermal)**
[ε ρ_g c_p,g + (1−ε) ρ_p c_p,s] ∂T/∂t + u ρ_g c_p,g ∂T/∂z = λ_eff ∂²T/∂z² + (1−ε) ρ_p (−ΔH) ∂q/∂t − (4h_w/d_col)(T − T_wall)
Isosteric heat: −ΔH(T,q) = −ΔU + RT (+ empirical loading correction for CO₂)
(Fabian Ramos Eq. 7 & Eqs. 9–10; Danilov et al. 2019 §3)

**5. Boundary / initial conditions (standard for this problem class)**
- Danckwerts inlet: u c_feed = u c(0,t) − ε D_L ∂c/∂z|_{z=0}, analogous form for T at inlet; zero-gradient (∂c/∂z = ∂T/∂z = 0) at outlet.
- Initial bed: c(z,0) = 0, q(z,0) = 0, T(z,0) = T₀ (clean bed at feed-line temperature or ambient).
- Feed step: c(0,t) = c_feed, T(0,t) = T_feed for t > 0 (step breakthrough test).

**6. Semi-discretised (Method of Lines) form**
State vector y(t) = [c, q, T]^T (per axial node); dy/dt = f(t,y) after replacing ∂/∂z, ∂²/∂z² by upwind/flux-limited finite-difference or finite-volume stencils (LeVeque Ch. 6–7 justify upwind bias near shock-like fronts). Integrated with `solve_ivp(f, t_span, y0, method='BDF'|'LSODA', jac=..., rtol≤1e-6, atol≤1e-9)`.

**7. Why the problem is stiff / front-forming (relevant background, not required)**
- k is typically orders of magnitude larger than the convective rate u/L (stiffness).
- A favourable isotherm (∂²q*/∂c² ≤ 0) drives the isothermal system toward a self-sharpening, shock-like "constant pattern" front (Ruthven Ch. 8; Garg & Ruthven 1973 asymptotic solutions).
- The hyperbolic (first-order, convective) part of the system is governed by characteristics; crossing characteristics signal shock formation, formalised via the Lax entropy condition and genuine nonlinearity (LeVeque Ch. 6–7; Evans Ch. 3).
- Known **isothermal** analogue: for a single favourable Langmuir isotherm with no dispersion, the constant-pattern wave speed follows directly from the mass-balance jump condition θ = u ε / [ε + (1−ε)ρ_p Δq/Δc] (Rankine–Hugoniot form) — this is the special case the claim above must be shown to generalise (or fail to generalise).
- Known partial extensions in the literature bundle: Danilov et al. (2019) derive an analytical simplification for the driving force ψ via ∂y/∂t = (∂y/∂q)(∂q/∂t) but close the remaining coupled system *numerically*, i.e. they do not themselves prove a closed-form non-isothermal wave speed — this is a genuine gap the claim is probing, not a result already published in the source library.
- Multicomponent constant-pattern theory (Kumar 1986) shows that competing fronts can separate into multiple waves — structurally relevant to whether concentration and temperature fronts can decouple into two distinct waves under strong Arrhenius coupling.

---

## Notes on this prompt (for the lead researcher, not part of the sent prompt)

- **Topic choice rationale:** every other candidate claim drawn from the roadmap (e.g. LDF↔exact-diffusion equivalence, MOL stiffness-order bounds) is already answered qualitatively by a cited source. This one — closed-form, unique wave speed for the *coupled* non-isothermal front — is explicitly *not* resolved in the 13-source library (Danilov et al. stop at a semi-analytical/numerical hybrid), which is what makes it a genuine test of novel derivation rather than recall.
- **Expected failure modes to watch for in the response:** (1) silently assuming D_L → 0 and h_w → 0 collapse the problem back to the isothermal case without checking that the *temperature* field still couples through b(T), d(T) in the isotherm even at zero dispersion; (2) asserting uniqueness without addressing whether two coupled hyperbolic families (concentration char. speed vs. temperature char. speed) can generically split into two fronts, which would disprove part (a) as stated.
- Suggest running this once at high temperature (creative disproof search) and once at low temperature (rigor check on whatever proof/disproof it commits to), then diffing the two for consistency before trusting either.
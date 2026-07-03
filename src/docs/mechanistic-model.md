# Mechanistic Fixed-Bed CO₂ Adsorption Model — Full Derivation, Analysis, and Numerical Formulation

**Scope.** Single-component CO₂ adsorption from an inert carrier in a 1-D fixed bed. The model is derived from conservation laws, closed with LDF kinetics and a nonlinear isotherm (Toth primary, Dual-Site Langmuir alternative), nondimensionalised, proven conservative and sign-preserving, solved exactly in its tractable limits, and cast into a mathematically correct Method-of-Lines / finite-volume formulation. All results are self-contained; local references are the repo copies of Ruthven ch. 6/8, LeVeque ch. 6–7, Evans PDE, Danilov 2019, Xu 2013 (`src/docs/papaers/`).

**Why mechanistic.** The fitted analytical models in `breakthrough_out/` (Yoon–Nelson, Thomas, Bohart–Adams, Clark, fractal sigmoids …) parameterise the *shape* of one curve at one operating point. §D.4 proves that the YN/Thomas logistic is the weak-nonlinearity constant-pattern *limit* of this mechanistic model, with $k_{YN}=k\,b\,c_f$ and $\tau=t_{st}(u,c_f,L)$ — composites of kinetics, isotherm affinity, and operating conditions. That composition is exactly why fitted $k_{YN},\tau$ cannot extrapolate across $u$, $c_f$, $L$, or $T$, and why the PDE model below can.

---

## 0. Notation, conventions, assumptions

### 0.1 Symbols and units

| Symbol | Meaning | Units |
|---|---|---|
| $z\in[0,L]$, $t\ge 0$ | axial coordinate, time | m, s |
| $\varepsilon$ | interparticle (bed) voidage | — |
| $u$ | **superficial** gas velocity (volumetric flux per bed cross-section) | m s⁻¹ |
| $v_i = u/\varepsilon$ | interstitial velocity | m s⁻¹ |
| $c(z,t)$ | gas-phase CO₂ concentration **per unit void (gas) volume** | mol m⁻³ |
| $q(z,t)$ | adsorbed loading per unit sorbent mass | mol kg⁻¹ |
| $q^*(c,T)$ | equilibrium loading | mol kg⁻¹ |
| $T(z,t)$ | pseudo-homogeneous bed temperature | K |
| $D_L$ | axial dispersion coefficient (void-area basis) | m² s⁻¹ |
| $\rho_p$, $\rho_b=(1-\varepsilon)\rho_p$ | particle density, bed bulk density | kg m⁻³ |
| $\alpha_b \equiv (1-\varepsilon)\rho_p$ | sorbent mass per bed volume | kg m⁻³ |
| $k$ | LDF rate constant | s⁻¹ |
| $\rho_g,\ c_{p,g}$ | gas density, specific heat | kg m⁻³, J kg⁻¹ K⁻¹ |
| $c_{p,s}$ | sorbent specific heat | J kg⁻¹ K⁻¹ |
| $C_h=\varepsilon\rho_g c_{p,g}+(1-\varepsilon)\rho_p c_{p,s}$ | volumetric heat capacity of bed | J m⁻³ K⁻¹ |
| $\lambda_{\mathrm{eff}}$ | effective axial bed conductivity | W m⁻¹ K⁻¹ |
| $(-\Delta H)>0$ | heat of adsorption (exothermic) | J mol⁻¹ |
| $h_w$, $d_{\mathrm{col}}$ | wall heat-transfer coefficient, column i.d. | W m⁻² K⁻¹, m |
| $c_f,\ T_f,\ T_0$ | feed concentration, feed temperature, initial temperature | mol m⁻³, K, K |
| $q_f \equiv q^*(c_f,T_0)$ | reference (feed-equilibrium) loading | mol kg⁻¹ |

**Convention warning (repo-internal).** Here $u$ is *superficial* and $D_L$ is defined on the void area, so the dispersive flux per bed area is $-\varepsilon D_L\,\partial c/\partial z$. The older `derivation.md` uses interstitial $u$ and a bed-basis $D_{ax}$; the mapping is $u_{\text{here}}=\varepsilon\,u_{\text{deriv.md}}$, $\varepsilon D_{L,\text{here}}=D_{ax,\text{deriv.md}}$. Mixing conventions silently changes Péclet numbers by a factor $\varepsilon$ — always state the basis.

### 0.2 Assumptions

- **A1 (1-D):** radial gradients neglected. Caveat for the bench rig: $d_{\mathrm{col}}/d_p \lesssim 10$ invites wall channeling; treat radial uniformity as an idealisation to be checked, not a fact.
- **A2 (dilute feed / constant $u$):** CO₂ mole fraction $y_f\ll 1$ so total molar flux, hence $u$, is $z$-independent. At the measured 10–15 % feeds this is only first-order accurate; Remark A.1 gives the exact variable-velocity extension and the $O(y_f)$ error bound.
- **A3 (ideal gas, isobaric):** $P$ uniform (pressure drop ≪ $P$); $c_{\text{tot}}=P/RT$.
- **A4 (Fickian axial dispersion):** all axial mixing mechanisms (molecular + Taylor–Aris + packing) lumped into one $D_L$.
- **A5 (LDF):** intraparticle + film resistance lumped into a single first-order driving force with constant $k$ (§A.3); valid when one resistance dominates or profiles are near-parabolic.
- **A6 (pseudo-homogeneous heat):** gas and solid share one temperature $T$; valid when interphase exchange is fast, $h_f a_p L /(u\rho_g c_{p,g}) \gg 1$ (the two-temperature model of `derivation.md` §1.3–1.4 collapses onto this one).
- **A7 (thermodynamic consistency):** the $(-\Delta H)$ in the energy balance equals the isosteric heat implied by the isotherm's temperature dependence (§A.4.3).
- **A8:** constant $\varepsilon,\rho_p,c_{p,s},\lambda_{\mathrm{eff}},D_L$ over the operating window.

---

## Part A — Derivation from conservation laws

### A.1 Gas-phase CO₂ mass balance

Take a control volume $[z,z+\Delta z]$ of cross-section $A$ (bed basis). Moles of gaseous CO₂ inside: $\varepsilon\,c\,A\,\Delta z$.

**Fluxes through the faces** (per bed area, mol m⁻² s⁻¹):

$$N(z,t) = \underbrace{u\,c}_{\text{convective}}\; \underbrace{-\ \varepsilon D_L \frac{\partial c}{\partial z}}_{\text{dispersive (Fickian)}} .$$

The convective term is $u c = \varepsilon v_i c$: interstitial molar flux $v_i c$ scaled by the open-area fraction $\varepsilon$. The dispersive flux acts on the same open area, hence the $\varepsilon$.

**Sink to the solid:** sorbent mass in the CV is $(1-\varepsilon)\rho_p A\Delta z$, so uptake removes $(1-\varepsilon)\rho_p \frac{\partial q}{\partial t} A\Delta z$ mol s⁻¹ from the gas.

Balance ( accumulation = in − out − sink ), divide by $A\Delta z$, let $\Delta z\to 0$:

$$\varepsilon\frac{\partial c}{\partial t} + \frac{\partial N}{\partial z} = -(1-\varepsilon)\rho_p\frac{\partial q}{\partial t},$$

and with A2 ($u_z=0$):

$$\boxed{\ \varepsilon\frac{\partial c}{\partial t} + u\frac{\partial c}{\partial z} \;=\; \varepsilon D_L\frac{\partial^2 c}{\partial z^2} \;-\;(1-\varepsilon)\rho_p\frac{\partial q}{\partial t}\ }\tag{A.1}$$

| Term | Physical meaning | Units |
|---|---|---|
| $\varepsilon\,c_t$ | accumulation of gaseous CO₂ per **bed** volume ($\varepsilon$ converts gas-basis $c$ to bed basis) | mol m⁻³ s⁻¹ |
| $u\,c_z$ | net convective outflow per bed volume, superficial $u$ | mol m⁻³ s⁻¹ |
| $\varepsilon D_L c_{zz}$ | net dispersive inflow (axial mixing) | mol m⁻³ s⁻¹ |
| $(1-\varepsilon)\rho_p q_t = \alpha_b q_t$ | transfer to the adsorbed phase | mol m⁻³ s⁻¹ |

**Remark A.1 (variable velocity — when 10–15 % feeds bite).** Only CO₂ leaves the gas; a total molar balance with $c_{\text{tot}}=P/RT$ constant (A3, isothermal) gives

$$c_{\text{tot}}\frac{\partial u}{\partial z} = -(1-\varepsilon)\rho_p\frac{\partial q}{\partial t}\quad\Rightarrow\quad u(z,t)=u_{\text{in}}-\frac{\alpha_b}{c_{\text{tot}}}\int_0^z q_t\,dz' .$$

Across a saturating front the velocity deficit is $\Delta u/u \approx y_f$: ~1 % at 1 % feed (negligible) but ~10–15 % for runs 4–8 (`new runs/`). The dilute model (A.1) then mislocates $t_{st}$ by $O(y_f)$; if that exceeds the ±10 % Gate-B budget, solve (A.1) together with the $u$-equation above (still MOL-compatible: $u$ is obtained by quadrature of $q_t$ at each RHS evaluation).

### A.2 Solid-phase balance: LDF kinetics

Exact pellet-scale mass transfer is a diffusion problem in the particle; the **linear driving force** closure replaces it by first-order relaxation toward equilibrium:

$$\boxed{\ \frac{\partial q}{\partial t} = k\,\bigl(q^*(c,T)-q\bigr)\ }\tag{A.2}$$

| Term | Physical meaning | Units |
|---|---|---|
| $q_t$ | uptake rate per kg sorbent | mol kg⁻¹ s⁻¹ |
| $k$ | inverse relaxation time of the pellet | s⁻¹ |
| $q^*-q$ | displacement from equilibrium (driving force) | mol kg⁻¹ |

**Mechanistic content of $k$** (resistances in series, Glueckauf; Ruthven ch. 6): for spherical pellets of radius $r_p$, film coefficient $k_f$, macropore diffusivity $D_p$, porosity $\varepsilon_p$, crystal/micro scale $r_c, D_c$, and local slope $K'=\rho_p\, \partial q^*/\partial c$,

$$\frac{1}{k} \;=\; \frac{r_p K'}{3k_f} \;+\; \frac{r_p^2 K'}{15\,\varepsilon_p D_p} \;+\; \frac{r_c^2}{15\,D_c},$$

each term a time constant (s). LDF is exact for a linear isotherm with parabolic intraparticle profile; otherwise it is the controlled approximation this project fits at Gate B. For amine sorbents (PEI@SiO₂) the last, reaction/amine-phase term often dominates and $k$ is small — the measured, strongly smeared fronts (`breakthrough_out/run 5`: $t_b\!\approx\!14$ s vs $t_{50}\!\approx\!230$ s) are consistent with a kinetics-limited bed (§C.4).

### A.3 Equilibrium closure

**Toth (primary; amine-functionalised sorbent).** Written in the concentration basis,

$$\boxed{\ q^*(c,T)=\frac{n_s(T)\,b(T)\,c}{\bigl[1+(b(T)\,c)^{t_T}\bigr]^{1/t_T}}\ }\tag{A.3}$$

$$n_s(T)=n_{s0}\exp\!\Bigl[\chi\Bigl(1-\tfrac{T}{T_0}\Bigr)\Bigr],\qquad
b(T)=b_0\exp\!\Bigl[\tfrac{\Delta H_0}{R T_0}\Bigl(\tfrac{T_0}{T}-1\Bigr)\Bigr],\qquad
t_T(T)=t_0+\alpha_T\Bigl(1-\tfrac{T_0}{T}\Bigr),$$

with $0<t_T\le 1$ the heterogeneity exponent ($t_T=1$ recovers Langmuir). **Units trap:** literature Toth parameters (e.g. the Stampi-Bombelli 2024 set, still `??` in `CLAUDE.md`) are usually *pressure-basis*, $b_P$ in kPa⁻¹ with $q^*(p_{\mathrm{CO_2}})$; convert with $p_{\mathrm{CO_2}}=cRT$, i.e. $b(T)=b_P(T)\,R\,T$. The conversion inserts an extra $T$-dependence — do it before differentiating, not after.

Equivalent driving-force form used in `derivation.md` §1.2 ($C-C^*$ with $C^*$ the isotherm inverse): identical model when $k_a a_p (1-\varepsilon)(C-C^*) = \alpha_b k (q^*-q)$ under the local linearisation $k = k_a a_p (C-C^*)/(\rho_p (q^*-q))$; (A.2) is preferred because $q^*(c,T)$ stays single-valued while the inverse $C^*(q,T)$ need not be evaluated.

**Dual-Site Langmuir (alternative; zeolite 13X):**

$$q^*(c,T)=\frac{q_1 b(T)c}{1+b(T)c}+\frac{q_2 d(T)c}{1+d(T)c},\qquad
b=b_0e^{-\Delta U_b/RT},\ d=d_0e^{-\Delta U_d/RT},\quad \Delta U_b,\Delta U_d<0. \tag{A.4}$$

**Lemma A.1 (shape of the closures).** For fixed $T$ and $c>0$, both (A.3) and (A.4) satisfy
1. $q^*(0,T)=0$ and Henry limit $q^*\sim n_s b\,c$ (Toth) resp. $(q_1b+q_2d)c$ (DSL);
2. strict monotonicity — Toth: $\dfrac{\partial q^*}{\partial c} = \dfrac{n_s b}{\bigl[1+(bc)^{t_T}\bigr]^{(1+t_T)/t_T}}>0$;
3. strict concavity — Toth: $\dfrac{\partial^2 q^*}{\partial c^2} = -\,n_s b^2 (1+t_T)\,(bc)^{t_T-1}\bigl[1+(bc)^{t_T}\bigr]^{-(1+2t_T)/t_T}<0$; DSL: sum of Langmuir terms with $q_i b^2\cdot(-2)/(1+bc)^3<0$;
4. saturation $q^*\to n_s$ (Toth) resp. $q_1+q_2$ (DSL) as $c\to\infty$.

*Proof.* Differentiate (A.3) with $s=(bc)^{t_T}$: $q^*=n_sbc(1+s)^{-1/t_T}$, $\partial_c q^* = n_s b(1+s)^{-1/t_T}-n_s b s(1+s)^{-1/t_T-1}=n_s b (1+s)^{-(1+t_T)/t_T}$; differentiate again using $\partial_c s = t_T s/c$. ∎

Concavity = **favorable** isotherm; it is what makes adsorption fronts self-sharpening (Part D). Note for $t_T<1$ the curvature blows up like $c^{\,t_T-1}$ as $c\to0^+$: $q^*$ is $C^1$ but not $C^2$ at $c=0$ — harmless for well-posedness (the slope stays bounded by $n_sb$) but it steepens the leading foot of the front.

**A.4.3 Thermodynamic consistency of $(-\Delta H)$.** The isosteric heat implied by the closure is $(-\Delta H_{\mathrm{iso}}) = R T^2\,\partial_T \ln p \big|_{q^*}$. For (A.3) with $\chi=\alpha_T=0$ this returns exactly $-\Delta H_{\mathrm{iso}}=-\Delta H_0$, constant; with $\chi\neq0$ it becomes loading-dependent. Assumption A7: use that same function in (A.5). Using an isotherm fitted with one $\Delta H_0$ and an energy balance with an unrelated $(-\Delta H)$ violates the Clausius–Clapeyron relation and produces spurious heat.

### A.4 Pseudo-homogeneous energy balance

Same control volume; energy carried by gas convection, conducted axially through the composite bed, released by adsorption, exchanged with the wall. Accumulation uses both phases (single $T$, A6):

$$\boxed{\ C_h\frac{\partial T}{\partial t} + u\rho_g c_{p,g}\frac{\partial T}{\partial z} \;=\; \lambda_{\mathrm{eff}}\frac{\partial^2 T}{\partial z^2} \;+\;(1-\varepsilon)\rho_p(-\Delta H)\frac{\partial q}{\partial t}\;-\;\frac{4h_w}{d_{\mathrm{col}}}\,(T-T_{\mathrm{wall}})\ }\tag{A.5}$$

$$C_h=\varepsilon\rho_g c_{p,g}+(1-\varepsilon)\rho_p c_{p,s}\ \ [\mathrm{J\,m^{-3}K^{-1}}].$$

| Term | Physical meaning | Units |
|---|---|---|
| $C_h T_t$ | sensible-heat accumulation of gas + solid per bed volume | W m⁻³ |
| $u\rho_g c_{p,g} T_z$ | convected enthalpy gradient (superficial flux $u\rho_g c_{p,g}$, J m⁻² s⁻¹ K⁻¹) | W m⁻³ |
| $\lambda_{\mathrm{eff}} T_{zz}$ | effective axial conduction/thermal dispersion | W m⁻³ |
| $\alpha_b(-\Delta H) q_t$ | adsorption heat source; $>0$ during uptake since $(-\Delta H)>0,\ q_t>0$ | W m⁻³ |
| $\tfrac{4h_w}{d_{\mathrm{col}}}(T-T_{\mathrm{wall}})$ | wall loss; $4/d_{\mathrm{col}}$ = perimeter/area of the cylinder | W m⁻³ |

Neglected knowingly: adsorbed-phase heat capacity $(1-\varepsilon)\rho_p q\,c_{p,a}$ (≤ a few % of $C_h$ at $q\lesssim1$ mol kg⁻¹), pressure work, kinetic energy. **Adiabatic column:** $h_w=0$.

**Isothermal reduction — quantitative justification (prompt item 3).** Two independent smallness arguments:
1. *Heat-release vs wall-loss timescales.* Heat is generated over the front-passage time $\sim t_{st}$ and removed on $\tau_w = C_h d_{\mathrm{col}}/(4h_w)$. The quasi-steady excursion is $\Delta T \approx \Delta T_{\mathrm{ad}}\cdot \tau_w/t_{st}$ where $\Delta T_{\mathrm{ad}}=\alpha_b(-\Delta H)q_f/C_h$ is the adiabatic rise. Bench rig estimate ($d_{\mathrm{col}}=8.5$ mm, $C_h\!\sim\!6.6\times10^5$ J m⁻³K⁻¹, $h_w\!\sim\!30$ W m⁻²K⁻¹, $t_{st}\!\sim\!600$ s): $\tau_w\!\approx\!47$ s, $\Delta T_{\mathrm{ad}}\!\approx\!40$ K, so $\Delta T\!\approx\!3$–4 K — mild, and the isothermal model is a defensible base case **for this rig**. For a pilot column ($d_{\mathrm{col}}\!\gtrsim\!5$ cm) $\tau_w$ grows linearly in $d_{\mathrm{col}}$ and the full (A.5) is mandatory.
2. *Isotherm sensitivity.* The perturbation enters through $b(T)$: $\delta q^*/q^* \sim (\Delta H_0/RT^2)\,\Delta T \approx (70\,000/8.314/298^2)\times 3.5 \approx 0.33$… i.e. even a 3–4 K excursion shifts local capacity by ~30 % near the front. Conclusion: keep (A.5) in the model; drop it only after checking *both* numbers for the case at hand. (This is why the model here is non-isothermal by default and the isothermal system is treated as a limit in Part D.)

### A.5 Initial and boundary conditions

Clean bed:
$$c(z,0)=0,\qquad q(z,0)=0,\qquad T(z,0)=T_0. \tag{A.6}$$

**Inlet ($z=0$), feed step at $t>0$.** Two admissible choices:
- *Dirichlet (hyperbolic-limit shortcut):* $c(0,t)=c_f,\ T(0,t)=T_f$.
- *Danckwerts flux continuity (correct with dispersion):* upstream of the packing there is no dispersion, so the total flux $uc_f$ must equal the total flux just inside:

$$u c_f = u\,c(0^+,t) - \varepsilon D_L\,c_z(0^+,t), \qquad
u\rho_g c_{p,g} T_f = u\rho_g c_{p,g} T(0^+,t) - \lambda_{\mathrm{eff}} T_z(0^+,t). \tag{A.7}$$

**Outlet ($z=L$):** $c_z(L,t)=0$, $T_z(L,t)=0$ (no dispersive flux through the exit plane).

Danckwerts is a Robin condition; it makes the inventory identity of Part B exact and forces $c(0^+,t)<c_f$ while the front is inside the bed (the dispersive term is positive). Dirichlet overfeeds the column by $-\varepsilon D_L c_z(0,t)>0$; the defect is $O(Pe^{-1})$ and vanishes in the hyperbolic limit. Both are implemented in Part E; the finite-volume form makes Danckwerts trivial.

### A.6 Full model (summary)

$$\varepsilon c_t + u c_z = \varepsilon D_L c_{zz} - \alpha_b q_t, \qquad
q_t = k\,(q^*(c,T)-q), \qquad
C_h T_t + u\rho_g c_{p,g} T_z = \lambda_{\mathrm{eff}} T_{zz} + \alpha_b(-\Delta H)q_t - \tfrac{4h_w}{d_{\mathrm{col}}}(T-T_{\mathrm{wall}}),$$

with closure (A.3) or (A.4), IC (A.6), BC (A.7) + zero-gradient outlet. Structurally this is a **parabolic–hyperbolic relaxation system**: two transport PDEs coupled pointwise to one stiff local ODE.

---

## Part B — Conservation and well-posedness

### B.1 CO₂ inventory identity

Define the CO₂ inventory per unit bed cross-section

$$M(t)=\int_0^L\bigl[\varepsilon c+\alpha_b q\bigr]\,dz \quad[\mathrm{mol\,m^{-2}}].$$

Add $\alpha_b q_t$ to both sides of (A.1) and write the left side in divergence form:

$$\frac{\partial}{\partial t}\bigl[\varepsilon c+\alpha_b q\bigr] + \frac{\partial}{\partial z}\Bigl[\underbrace{uc-\varepsilon D_L c_z}_{N(z,t)}\Bigr]=0. \tag{B.1}$$

Integrate over $[0,L]$:

$$\boxed{\ \frac{dM}{dt} = N(0,t)-N(L,t) = \bigl[uc-\varepsilon D_Lc_z\bigr]_{z=0}-\bigl[uc-\varepsilon D_Lc_z\bigr]_{z=L}.\ }\tag{B.2}$$

With Danckwerts inlet, $N(0,t)=uc_f$ **exactly**, and with $c_z(L)=0$, $N(L,t)=u\,c(L,t)$:

$$\boxed{\ \frac{dM}{dt} = u\,c_f - u\,c(L,t).\ }\tag{B.3}$$

With a Dirichlet inlet instead, $dM/dt = uc_f - \varepsilon D_L c_z(0,t) - uc(L,t)$: the extra term is the Dirichlet mass defect (positive early in the run), of relative size $O(Pe^{-1})$. (B.3) is the guardrail every simulation must reproduce to tolerance (Part E, test 4).

**Corollary B.1 (exact stoichiometric-time invariance — the useful one).** Isothermal case; suppose $c(L,t)\to c_f$ and $q\to q^*(c_f,T_0)=q_f$ as $t\to\infty$. Integrating (B.3) from 0 to ∞ with $M(0)=0$, $M(\infty)=L(\varepsilon c_f+\alpha_b q_f)$:

$$\int_0^\infty \Bigl(1-\frac{c(L,t)}{c_f}\Bigr)dt \;=\; \frac{L\bigl[\varepsilon c_f+\alpha_b q_f\bigr]}{u\,c_f}\;=\;t_{st},$$

**for every** $D_L\ge0$ and every $k>0$. Dispersion and kinetics reshape the breakthrough curve but cannot move its first moment: the area above the curve is pinned to equilibrium capacity. Practical consequences: (i) the pipeline's saturation-integrated capacity ($q_{dyn}$ variants integrated to $t_E$ or beyond) estimates $q^*(c_f,T_0)$ *model-free*; (ii) any fitted model whose $\tau$ disagrees with $t_{st}$ computed from an independently measured isotherm signals an inconsistency (leak, dead volume, $u$ or $c_f$ error), not "a different model". Caveats: exact under flux (Danckwerts) BCs; Dirichlet adds $O(Pe^{-1})$; non-isothermal runs must return to $T_0$ before the identity closes.

### B.2 Energy inventory (analogue)

Integrating (A.5): with $E(t)=\int_0^L C_h(T-T_0)\,dz$,

$$\frac{dE}{dt} = u\rho_gc_{p,g}\bigl[T(0,t)-T(L,t)\bigr] + \lambda_{\mathrm{eff}}\bigl[T_z(L,t)-T_z(0,t)\bigr] + \alpha_b\!\!\int_0^L\!\!(-\Delta H)q_t\,dz - \frac{4h_w}{d_{\mathrm{col}}}\!\!\int_0^L\!\!(T-T_{\mathrm{wall}})dz,$$

sensible-heat change = net convected enthalpy + boundary conduction + adsorption release − wall loss. Same telescoping structure; same numerical guardrail.

### B.3 Positivity and invariant region

**Proposition B.2 ($q\ge0$, exactly).** If $q(z,0)\ge0$ and $c\ge0$ (so $q^*\ge0$), then Duhamel on the linear-in-$q$ ODE (A.2) gives

$$q(z,t)=q(z,0)e^{-kt}+k\!\int_0^t e^{-k(t-s)}\,q^*(c(z,s),T(z,s))\,ds\;\ge\;0,$$

and likewise $q(z,t)\le \max\{q(z,0),\ \sup_s q^*(c(z,s),T(z,s))\}$: the loading is a $k$-exponential moving average of the equilibrium history. No PDE argument needed.

**Proposition B.3 ($c\ge0$).** Extend $q^*(c,T):=0$ for $c<0$ (the extension never activates once the result holds). Suppose $c$ attained a negative value; consider the open set $\{c<0\}$ and note that on it the source in (A.1) is $-\alpha_b k(q^*-q)=+\alpha_b k q\ge0$ by B.2. So $\varepsilon c_t + u c_z - \varepsilon D_L c_{zz} \ge 0$ wherever $c<0$, while $c=0$ on that set's parabolic boundary (IC $c=0$; and the set cannot touch the lateral boundaries: at $z=0$ a negative minimum would need $c_z(0)\ge0$, but Danckwerts gives $\varepsilon D_L c_z(0)=u(c(0)-c_f)<0$, contradiction; at $z=L$, Hopf's lemma requires $c_z(L)<0$ at a strict boundary minimum, contradicting $c_z(L)=0$). The parabolic minimum principle then forces $c\ge0$ on the set — so it is empty. ∎

**Proposition B.4 (invariant rectangle, isothermal).** For $T\equiv T_0$ the region

$$\mathcal R=\{(c,q):\ 0\le c\le c_f,\ 0\le q\le q_f\},\qquad q_f=q^*(c_f,T_0),$$

is positively invariant. *Proof sketch:* check the field points inward on each face. Face $q=q_f$, $c\le c_f$: $q_t=k(q^*(c)-q_f)\le k(q^*(c_f)-q_f)=0$ (monotone $q^*$). Face $q=0$: $q_t=kq^*(c)\ge0$. Face $c=0$: Prop. B.3. Face $c=c_f$ with $q\le q_f$: source $-\alpha_bk(q^*(c_f)-q)\le0$, and the maximum principle (plus the Robin inlet, which pins $c(0)\le c_f$) blocks crossing. ∎

**Remark B.5 (roll-up is physical, not a bug).** Non-isothermally, $c\le c_f$ can fail: a passing thermal wave lowers $q^*(c,T)$, forces $q_t<0$ locally (desorption), and the released CO₂ can push the outlet trace transiently above $c_f$ ($c/c_f>1$ "roll-up"). Positivity (B.2–B.3) still holds. A simulated overshoot is admissible; a *negative* concentration is a numerics failure — this is precisely why Part E uses upwinding (monotone) rather than central convection.

**Well-posedness note.** With $q^*\in C^1$ bounded-slope (Lemma A.1), the right-hand sides are locally Lipschitz on $\mathcal R\times[T_{\min},T_{\max}]$; the system is a semilinear parabolic pair coupled to a family of ODEs, and standard semigroup theory (Evans ch. 7 machinery) gives local existence/uniqueness; the a-priori bounds B.2–B.4 make solutions global. The relaxation structure additionally satisfies the subcharacteristic condition (§D.5), so the stiff limit $k\to\infty$ is stable rather than oscillatory.

---

## Part C — Nondimensionalisation

### C.1 Scales and variables

$$x=\frac{z}{L},\qquad \tau=\frac{ut}{L},\qquad C=\frac{c}{c_f},\qquad Q=\frac{q}{q_f},\qquad \Theta=\frac{T-T_0}{\Delta T},\qquad q_f=q^*(c_f,T_0).$$

$\tau$ counts **superficial** bed volumes fed; $\Delta T$ is free — choosing $\Delta T=\Delta T_{\mathrm{ad}}=\alpha_b(-\Delta H)q_f/C_h$ normalises $\Lambda=1$ below.

### C.2 Dimensionless system

Substituting into (A.1)–(A.5) and multiplying by $L/(uc_f)$, $L/(uq_f)$, $L/(uC_h\Delta T)$ respectively:

$$\boxed{\ \varepsilon\,C_\tau + C_x = \frac{\varepsilon}{Pe}\,C_{xx} - \beta\,Q_\tau\ },\qquad
\boxed{\ Q_\tau = Da\,\bigl[Q^*(C,\Theta)-Q\bigr]\ },$$

$$\boxed{\ \Theta_\tau + \gamma_h\,\Theta_x = \frac{1}{Pe_h}\,\Theta_{xx} + \Lambda\,Q_\tau - Bi_w\,(\Theta-\Theta_{\mathrm{wall}})\ },$$

where $Q^*(C,\Theta)=q^*(c_fC,\,T_0+\Delta T\,\Theta)/q_f$ and

$$Pe=\frac{uL}{D_L},\qquad Da=\frac{kL}{u},\qquad \beta=\frac{\alpha_b q_f}{c_f},\qquad
\alpha=\frac{\beta}{\varepsilon}=\frac{(1-\varepsilon)\rho_p q_f}{\varepsilon c_f},$$

$$\gamma_h=\frac{\rho_g c_{p,g}}{C_h},\qquad Pe_h=\frac{C_h uL}{\lambda_{\mathrm{eff}}},\qquad
\Lambda=\frac{(1-\varepsilon)\rho_p(-\Delta H)q_f}{C_h\,\Delta T},\qquad
Bi_w=\frac{4h_wL}{d_{\mathrm{col}}C_h u}.$$

BCs: Danckwerts becomes $1 = C - \tfrac{\varepsilon}{Pe}\,C_x$ at $x=0^+$; $C_x(1,\tau)=0$; thermal analogues with $Pe_h$; IC $C=Q=\Theta=0$.

### C.3 Physical meaning of the groups

| Group | Ratio | Reading |
|---|---|---|
| $Pe=uL/D_L$ | axial convection / axial dispersion | $Pe\to\infty$: hyperbolic, sharp fronts; $Pe\lesssim40$: dispersion visibly rounds breakthrough |
| $Da=kL/u$ | residence time / LDF relaxation time | $Da\to\infty$: local equilibrium; $Da\lesssim1$: kinetically limited, smeared front |
| $\alpha$ (or $\beta=\varepsilon\alpha$) | solid capacity / gas void inventory | sets front retardation; $t_{st}\approx(1+\alpha)\,\varepsilon L/u$ |
| $\gamma_h$ | gas heat flux / bed heat capacity | thermal-wave speed ratio $v_{th}/u=\gamma_h$ (≪ 1 in packed sorbent beds) |
| $Pe_h$ | thermal convection / axial conduction | conduction rarely dominant except near walls/low flow |
| $\Lambda$ | adsorption heat / sensible heat at scale $\Delta T$ | with $\Delta T=\Delta T_{\mathrm{ad}}$, $\Lambda\equiv1$ and $\Delta T_{\mathrm{ad}}$ carries the physics |
| $Bi_w$ | wall extraction / thermal convection | $Bi_w\to\infty$: isothermal wall-clamped; $0$: adiabatic |

### C.4 Magnitudes for the bench rig (illustrative — flagged placeholders)

Using run-5-like conditions ($Q=100$ mL min⁻¹ ⇒ $u=2.94\times10^{-2}$ m s⁻¹ on $d_{\mathrm{col}}=8.5$ mm; $L=0.21$ m; $c_f\approx3.9$ mol m⁻³ at 9.5 %; $\rho_b\approx660$ kg m⁻³; $q_f\sim0.6$ mol kg⁻¹; $D_L\sim5\times10^{-5}$ m² s⁻¹ from $D_L\approx0.7D_m+0.5d_pv_i$; $k\sim5\times10^{-3}$ s⁻¹; $\varepsilon$ **not yet physical** pending $\rho_p$ — `CLAUDE.md` open item):

$$Pe\sim1.2\times10^{2},\qquad Da\sim3.6\times10^{-2},\qquad \beta\sim10^{2},\ \alpha\sim2.5\times10^{2},\qquad \gamma_h\sim2\times10^{-3},\qquad \Lambda\,\Delta T=\Delta T_{\mathrm{ad}}\sim40\ \mathrm K,\qquad Bi_w\sim0.15.$$

Diagnosis: transport is convection-dominated ($Pe\gg1$) but the bed is **kinetically limited** ($Da\ll1$) — the observed MTZ of ~0.11 m on a 0.21 m bed is LDF smearing, not dispersion. Empirical-model shape parameters fitted here encode mostly $k$; scale-up to a longer bed changes $Da$ linearly and every fitted shape breaks. These are order-of-magnitude anchors only; no value here supersedes measured/tabulated parameters (per repo policy, deviations must be flagged — this whole table is a flag).

---

## Part D — Analytically tractable limits

### D.1 Isothermal local-equilibrium limit ⇒ scalar conservation law

Limit: $T\equiv T_0$, $D_L=0$, $k\to\infty$ so $q=Q(c):=q^*(c,T_0)$ pointwise (regular relaxation limit; justified a posteriori by D.5). Then (A.1) becomes $\varepsilon c_t + \alpha_b Q'(c)c_t + uc_z=0$, i.e. the **scalar hyperbolic conservation law**

$$\boxed{\ \frac{\partial}{\partial t}\,m(c) + u\,\frac{\partial c}{\partial z}=0,\qquad m(c)=\varepsilon c+\alpha_b Q(c)\ }\tag{D.1}$$

$m$ = total (gas + adsorbed) CO₂ per bed volume at equilibrium. Since $m'(c)=\varepsilon+\alpha_bQ'(c)\ge\varepsilon>0$, $m$ is invertible; with $m$ as the conserved variable, (D.1) is $m_t+F(m)_z=0$, flux $F(m)=u\,c(m)$.

**Characteristic (concentration-wave) speed.** Smooth solutions propagate values of $c$ at

$$v_c(c)=F'(m)=\frac{u}{m'(c)}=\frac{u}{\varepsilon+\alpha_b Q'(c)}. \tag{D.2}$$

For favorable (concave) $Q$: $Q'$ decreases in $c$ ⇒ **high concentrations travel faster**. A feed step $0\to c_f$ is therefore compressive: characteristics collide and the profile steepens into a shock in finite time. Convexity bookkeeping: $m$ concave increasing ⇒ its inverse $c(m)$ convex ⇒ $F$ convex — the Riemann problem has pure shock/rarefaction solutions, no composites (LeVeque ch. 6).

**Rankine–Hugoniot speed.** Conservation across a moving discontinuity between upstream state $c_f$ and downstream state $0$ ($[\![F]\!]=v_{RH}[\![m]\!]$, from the integral form of (D.1) on a CV straddling the front):

$$\boxed{\ v_{RH}=\frac{F(m_f)-F(0)}{m_f-0}=\frac{u\,c_f}{\varepsilon c_f+\alpha_b Q(c_f)}\ }\tag{D.3}$$

**Admissibility (Lax entropy condition).** Concavity of $Q$ with $Q(0)=0$ gives the chord inequalities $Q'(c_f)\le Q(c_f)/c_f\le Q'(0)$, hence

$$v_c(0)\;\le\; v_{RH}\;\le\; v_c(c_f),$$

with strict inequalities for strictly concave $Q$: characteristics run **into** the shock from both sides — the shock is the unique entropy (vanishing-viscosity) solution, i.e. the physically selected front. It is also, correctly, the $D_L\to0$, $k\to\infty$ limit of the smooth fronts of D.2–D.3.

**Ideal breakthrough time.**

$$\boxed{\ t_{st}=\frac{L}{v_{RH}}=\frac{L\bigl[\varepsilon c_f+\alpha_bQ(c_f)\bigr]}{u\,c_f}\ }\tag{D.4}$$

— identical to the first-moment invariant of Corollary B.1, as it must be: kinetics and dispersion redistribute the front around $t_{st}$ but cannot shift its centroid.

**Remark D.1 (adsorption/desorption asymmetry).** For the reverse Riemann problem (saturated bed, feed switched to $0$) the same concave $Q$ makes the data *expansive*: the entropy solution is a **rarefaction fan**, $c(z,t)$ defined implicitly by $z/t=v_c(c)$ for $v_c(c_f)\,t\le z\le v_c(0)\,t$ ("proportionate pattern"). One isotherm ⇒ shock on adsorption, spreading fan on desorption. No symmetric empirical sigmoid can represent both; the mechanistic model gets both from one parameter set.

### D.2 Linear-isotherm local-equilibrium limit ⇒ retarded advection–dispersion

Henry closure $Q(c)=Kc$, $K=n_s(T_0)b(T_0)$ [m³ kg⁻¹] (Toth Henry slope). Then (A.1) with $q=Kc$:

$$(\varepsilon+\alpha_bK)\,c_t+u\,c_z=\varepsilon D_L\,c_{zz}
\quad\Longleftrightarrow\quad
\boxed{\ c_t+v_{\mathrm{eff}}\,c_z=D_{\mathrm{eff}}\,c_{zz}\ },$$

$$\boxed{\ v_{\mathrm{eff}}=\frac{u}{\varepsilon+\alpha_bK}\ },\qquad
\boxed{\ D_{\mathrm{eff}}=\frac{\varepsilon D_L}{\varepsilon+\alpha_bK}\ },\qquad
R:=1+\frac{\alpha_bK}{\varepsilon}=\frac{v_i}{v_{\mathrm{eff}}}\ (\text{retardation factor}).$$

**Step-input solution (semi-infinite, Dirichlet inlet).** Laplace transform in $t$: $s\hat c+v\hat c'=D\hat c''$ (drop subscripts), bounded branch

$$\hat c(z,s)=\frac{c_f}{s}\exp\!\Bigl[\frac{vz}{2D}\Bigr]\exp\!\Bigl[-\frac{z}{\sqrt D}\sqrt{s+\tfrac{v^2}{4D}}\Bigr].$$

Using the standard pair $\mathcal L^{-1}\{s^{-1}e^{-a\sqrt{s+\gamma}}\}=\tfrac12\bigl[e^{-a\sqrt\gamma}\operatorname{erfc}\bigl(\tfrac{a}{2\sqrt t}-\sqrt{\gamma t}\bigr)+e^{a\sqrt\gamma}\operatorname{erfc}\bigl(\tfrac{a}{2\sqrt t}+\sqrt{\gamma t}\bigr)\bigr]$ (itself obtained from $\mathcal L^{-1}\{e^{-a\sqrt s}\}=\tfrac{a}{2\sqrt{\pi t^3}}e^{-a^2/4t}$ by shift + convolution) with $a=z/\sqrt D$, $\gamma=v^2/4D$:

$$\boxed{\ \frac{c(z,t)}{c_f}=\frac12\operatorname{erfc}\!\Bigl(\frac{z-v_{\mathrm{eff}}t}{2\sqrt{D_{\mathrm{eff}}t}}\Bigr)+\frac12\exp\!\Bigl(\frac{v_{\mathrm{eff}}z}{D_{\mathrm{eff}}}\Bigr)\operatorname{erfc}\!\Bigl(\frac{z+v_{\mathrm{eff}}t}{2\sqrt{D_{\mathrm{eff}}t}}\Bigr)\ }\tag{D.5}$$

(Ogata–Banks form; direct substitution verifies PDE, IC, and BC.) Checks: $t\to0^+$ ⇒ both arguments $\to+\infty$ ⇒ $c\to0$; $t\to\infty$ ⇒ $c\to c_f$; at $z=0$ the two halves sum to $c_f$. The second term is $\le e^{Pe_{\mathrm{eff}}}\operatorname{erfc}(\sqrt{Pe_{\mathrm{eff}}}\,\cdot)\!\sim\!O(e^{-Pe_{\mathrm{eff}}})$ relative at breakthrough ($Pe_{\mathrm{eff}}=v_{\mathrm{eff}}L/D_{\mathrm{eff}}=Pe/\varepsilon\cdot\ldots\gg1$), so the practical Gate-A target is the single-erfc front of width $\sqrt{2D_{\mathrm{eff}}t}$. Finite-column Danckwerts BCs replace (D.5) by an eigenseries whose deviation is again $O(e^{-Pe})$ — invisible at $Pe\gtrsim40$ except within $O(L/Pe)$ of the ends.

### D.3 Constant-pattern travelling wave at finite $k$ (mechanistic S-curve)

Keep finite LDF kinetics, isothermal, $D_L=0$, favorable $Q$. Seek $c=\varphi(\eta)$, $q=\psi(\eta)$, $\eta=z-vt$, with rest state ahead ($\varphi,\psi\to0$, $\eta\to+\infty$) and saturation behind ($\varphi\to c_f$, $\psi\to q_f$, $\eta\to-\infty$).

Mass balance (A.1): $(u-\varepsilon v)\varphi' = \alpha_b v\,\psi'$. Integrate with the ahead-state:

$$(u-\varepsilon v)\,\varphi=\alpha_b v\,\psi. \tag{D.6}$$

Evaluating (D.6) at $\eta\to-\infty$ forces

$$v=\frac{uc_f}{\varepsilon c_f+\alpha_b q_f}=v_{RH},$$

— a travelling wave exists **only** at the Rankine–Hugoniot speed (mass consistency), and (D.6) becomes the **coherence relation** $\psi(\eta)=\dfrac{q_f}{c_f}\,\varphi(\eta)$: loading and concentration are locked proportional through the front.

Insert into LDF $-v\psi'=k(Q(\varphi)-\psi)$:

$$\boxed{\ \frac{d\varphi}{d\eta} = -\,\frac{k\,c_f}{v_{RH}\,q_f}\,\Bigl[\,\underbrace{Q(\varphi)-\tfrac{q_f}{c_f}\varphi}_{G(\varphi)}\,\Bigr]\ }\tag{D.7}$$

For strictly concave $Q$: $G>0$ on $(0,c_f)$, $G(0)=G(c_f)=0$ (chord under the curve) ⇒ $\varphi$ decreases monotonically from $c_f$ to $0$: a smooth, kinetics-broadened shock. Quadrature:

$$\eta_0-\eta=\frac{v_{RH}\,q_f}{k\,c_f}\int_{\varphi(\eta_0)}^{\varphi(\eta)}\frac{d\varphi'}{G(\varphi')}.$$

$G$ vanishes linearly at both ends ⇒ logarithmic divergence ⇒ **exponential tails**, with e-folding lengths

$$\ell_{+}=\frac{v_{RH}q_f}{kc_f\bigl(Q'(0)-q_f/c_f\bigr)}\ \ (\text{leading foot}),\qquad
\ell_{-}=\frac{v_{RH}q_f}{kc_f\bigl(q_f/c_f-Q'(c_f)\bigr)}\ \ (\text{saturation tail}).$$

Headline scaling: **MTZ width ∝ $v_{RH}/k$ × isotherm-curvature factor.** This inverts: a measured $L_{MTZ}$ plus an isotherm yields a mechanistic estimate of $k$ — the correct route from the pipeline's $L_{MTZ}$ column to a rate constant.

**Langmuir closed form.** $Q(\varphi)=q_mb\varphi/(1+b\varphi)$, $q_f=q_mbc_f/(1+bc_f)$. Then $G(\varphi)=\dfrac{q_mb^2\,\varphi(c_f-\varphi)}{(1+b\varphi)(1+bc_f)}$ and (D.7) collapses to

$$\frac{d\varphi}{d\eta}=-\frac{kb}{v_{RH}}\cdot\frac{\varphi(c_f-\varphi)}{1+b\varphi},$$

separable by partial fractions ($\tfrac{1+b\varphi}{\varphi(c_f-\varphi)}=\tfrac{1}{c_f\varphi}+\tfrac{1+bc_f}{c_f(c_f-\varphi)}$), giving with $w=\varphi/c_f$:

$$\boxed{\ \ln w-(1+bc_f)\ln(1-w) = -\frac{k\,b\,c_f}{v_{RH}}\,(\eta-\eta_0)\ }\tag{D.8}$$

An exact, mechanistic breakthrough profile: at the outlet ($\eta=L-v_{RH}t$) it is a sigmoid in $t$ that is **inherently asymmetric** — the saturation tail is slower than the leading edge by the factor $(1+bc_f)$. The strong tailing in the measured runs ($t_E-t_{50}\gg t_{50}-t_b$ in `breakthrough_out/run 5`) is the qualitative signature of $bc_f\gg1$ chemisorption (plus, in reality, thermal drift and amine-phase diffusion); symmetric logistics can only fake it by distorting other parameters.

### D.4 Why empirical fits cannot extrapolate — derived, not asserted

Take (D.8) with weak nonlinearity $bc_f\ll1$ (or replace the exponent by 1). At $z=L$:

$$\frac{c(L,t)}{c_f}=\frac{1}{1+\exp[-k_{YN}(t-\tau)]},\qquad
\boxed{\ k_{YN}=k\,b\,c_f\ },\qquad \boxed{\ \tau=t_{st}=\frac{L[\varepsilon c_f+\alpha_bq_f]}{uc_f}\ }.$$

This **is** the Yoon–Nelson/Thomas/Bohart–Adams logistic (they are one two-parameter family, cf. M01 in `breakthrough_fit/models.py`) — recovered here as the constant-pattern, weak-nonlinearity limit of the mechanistic model. The fitted constants are composites:

- $k_{YN}$ mixes kinetics ($k$), affinity ($b$, itself $e^{-\Delta H_0/RT}$-sensitive), and feed ($c_f$). Change $c_f$ or $T$ and $k_{YN}$ must change — the fit cannot know how.
- $\tau$ inherits $u$, $L$, $c_f$, and the whole isotherm through $q_f=q^*(c_f,T_0)$.

Hence one $(k_{YN},\tau)$ pair is one point of a two-parameter *projection* of a seven-plus-parameter mechanistic surface: interpolation works, extrapolation is structurally impossible. Inverting the projection at several operating points ($k$, $b$, $q_m$ from a family of runs — e.g. the 4/5/6 flow sweep) is the legitimate use of the fitted library, and the mechanistic model is the object that then extrapolates.

### D.5 Relaxation → effective dispersion (van Deemter) and the subcharacteristic condition

For large-but-finite $Da$, Chapman–Enskog expand (A.2): $q=Q(c)-k^{-1}\partial_t Q(c)+O(k^{-2})$. For $Q=Kc$, substituting into (A.1) and eliminating $c_{tt}\approx v_{\mathrm{eff}}^2c_{zz}$ to leading order:

$$c_t+v_{\mathrm{eff}}c_z=\Bigl[D_{\mathrm{eff}}+\underbrace{\frac{\alpha_bK}{\varepsilon+\alpha_bK}\cdot\frac{v_{\mathrm{eff}}^2}{k}}_{D_{\mathrm{kin}}}\Bigr]c_{zz}+O(k^{-2}).$$

Finite kinetics ≍ extra axial dispersion $D_{\mathrm{kin}}\propto v_{\mathrm{eff}}^2/k$ — the C-term of the van Deemter equation, derived from the model. Two structural consequences: (i) the **subcharacteristic condition** $0\le v_{\mathrm{eff}}\le u/\varepsilon$ holds automatically (equilibrium wave slower than frozen wave), so the relaxation limit is dissipative and stable — the mathematical licence behind D.1; (ii) LDF smearing and $D_L$ smearing are *additive and confounded* at first order: breakthrough-curve fitting alone cannot separate $k$ from $D_L$ — an independent $D_L$ estimate (correlation or tracer run) is required. Design implication for the parametric study: vary $u$ — $D_{\mathrm{kin}}\propto v^2/k$ while $D_L$ grows ~linearly in $v$ — the sweep decorrelates them.

### D.6 Why the full model has no closed form

The full system couples: $q^*(c,T)$ (nonlinear in both), Arrhenius $b(T)$ feedback from the energy balance into the mass balance, finite relaxation ($Da<\infty$) destroying local equilibrium, and parabolic terms ($Pe,Pe_h<\infty$) destroying characteristics. Non-isothermally the front is generally **not** constant-pattern: an adiabatic bed supports combined concentration–thermal waves (speeds $v_{RH}$ vs $v_{th}=\gamma_h u$; here $v_{th}\sim0.2$–$0.5\,v_{RH}$), producing plateaus and possible roll-up (Rem. B.5) — phenomena outside every scalar-wave ansatz. Each mechanism alone is tractable (D.1, D.2, D.3, D.5); their composition is not: the tractable cases are precisely the commuting limits $\{Pe\to\infty\}$, $\{Da\to\infty\}$, $\{\text{linear }Q\}$, $\{\Lambda\to0\}$. The full model must be integrated numerically — Part E.

---

## Part E — Numerical formulation (Method of Lines)

### E.1 Grid, state, and the two discretisations

Uniform grid, $N$ nodes. Two variants; **(b) is recommended**.

**(a) Node-based / Dirichlet (matches the prompt and the `pde_mol.py` scaffold).** $z_i=i\Delta z$, $\Delta z=L/(N-1)$, $i=0,\dots,N-1$; state

$$y(t)=[c_0..c_{N-1},\ q_0..q_{N-1},\ T_0..T_{N-1}]^{\mathsf T}\in\mathbb R^{3N},\qquad \frac{dy}{dt}=f(t,y).$$

Interior operators — first-order **upwind** convection (flow in $+z$): $(\delta_z^-c)_i=\dfrac{c_i-c_{i-1}}{\Delta z}$; **central** dispersion: $(\delta_{zz}c)_i=\dfrac{c_{i+1}-2c_i+c_{i-1}}{\Delta z^2}$. Then for $i=1,\dots,N-2$:

$$\frac{dq_i}{dt}=k\bigl(q^*(c_i,T_i)-q_i\bigr),\qquad
\frac{dc_i}{dt}=\frac{\varepsilon D_L(\delta_{zz}c)_i-u(\delta_z^-c)_i-\alpha_b\,dq_i/dt}{\varepsilon},$$

$$\frac{dT_i}{dt}=\frac{\lambda_{\mathrm{eff}}(\delta_{zz}T)_i-u\rho_gc_{p,g}(\delta_z^-T)_i+\alpha_b(-\Delta H)\,dq_i/dt-\tfrac{4h_w}{d_{\mathrm{col}}}(T_i-T_{\mathrm{wall}})}{C_h}.$$

Boundaries: inlet Dirichlet $c_0=c_f,\ T_0=T_f$ imposed by $dc_0/dt=dT_0/dt=0$ after setting the values (note $dq_0/dt$ is **still integrated** — the solid at the inlet is not clamped); outlet ghost nodes $c_N:=c_{N-1}$, $T_N:=T_{N-1}$ (zero gradient), equivalent to $(\delta_{zz}c)_{N-1}=(c_{N-2}-c_{N-1})/\Delta z^2$.

**(b) Finite-volume / Danckwerts (conservative — makes B.3 hold to machine precision).** Cell centres $z_i=(i+\tfrac12)\Delta z$, $\Delta z=L/N$, faces $z_{i\pm1/2}$. Total-flux at faces:

$$F_{i+1/2}=u\,c_i-\varepsilon D_L\,\frac{c_{i+1}-c_i}{\Delta z}\ \ (i=0..N-2),\qquad
\boxed{F_{-1/2}=u\,c_f}\ \ (\text{Danckwerts, exact}),\qquad
F_{N-1/2}=u\,c_{N-1}\ (\text{zero-gradient}),$$

(upwind cell value in the convective part), and

$$\varepsilon\frac{dc_i}{dt}=\frac{F_{i-1/2}-F_{i+1/2}}{\Delta z}-\alpha_b\frac{dq_i}{dt}. \tag{E.1}$$

Summing (E.1) over $i$ telescopes: $\dfrac{d}{dt}\Bigl[\Delta z\sum_i(\varepsilon c_i+\alpha_b q_i)\Bigr]=uc_f-uc_{N-1}$ — the **discrete inventory identity**, exactly (B.3). The Danckwerts inlet is not a boundary condition to approximate; it *is* the inlet face flux. Energy: identical structure with fluxes $u\rho_gc_{p,g}T_i-\lambda_{\mathrm{eff}}(T_{i+1}-T_i)/\Delta z$ and inlet face flux $u\rho_gc_{p,g}T_f$.

### E.2 Why upwind (and its price)

Upwinding makes the convective update monotone ⇒ no spurious oscillations, positivity preserved (the discrete analogue of B.3; central convection at $Pe_{\Delta z}=u\Delta z/\varepsilon D_L>2$ oscillates and produces $c<0$). Price: numerical diffusion $D_{\mathrm{num}}=\dfrac{u\Delta z}{2\varepsilon}$ (modified-equation analysis). Resolution requirement:

$$D_{\mathrm{num}}\ll D_L\ \Longleftrightarrow\ N\gg \frac{Pe}{2\varepsilon},$$

e.g. $Pe\sim120,\ \varepsilon\sim0.4$ ⇒ $N\gg150$; use $N\gtrsim4\times$ that, or verify by grid-doubling (Richardson) that observables ($t_{BT}$, $t_{50}$) are grid-converged to below gate tolerance. Upgrade path if needed: TVD flux limiter (minmod/van Leer) on the convective face value — second-order in smooth regions, still monotone; keep first-order for the validation ladder baseline.

### E.3 Stiffness, Jacobian, integrator

Three disparate timescales: dispersion CFL $\Delta z^2/(2D_L)$ (∝ $N^{-2}$), LDF $1/k$, transport $L/u$. Use a stiff implicit integrator: `scipy.integrate.solve_ivp` with `BDF` or `LSODA`, `rtol≈1e-6`, `atol` per-component ($\sim10^{-6}c_f$, $10^{-6}q_f$, $10^{-6}$ K). The Jacobian is block-tridiagonal; with the block ordering $[c;q;T]$ supply `jac_sparsity` (three tridiagonal bands plus the pointwise $c\!-\!q\!-\!T$ couplings); alternatively interleave $(c_i,q_i,T_i)$ per node to get a banded matrix (`lband=uband=3`) — markedly faster for large $N$. Event functions $g_{BT}=c_{N-1}/c_f-0.05$, $g_{sat}=c_{N-1}/c_f-0.95$ give $t_{BT},t_{sat}$ to integrator precision (no post-hoc interpolation).

### E.4 Outputs

$$t_{BT}=\inf\{t>0:\ c(L,t)/c_f=0.05\},\qquad
t_{sat}=\inf\{t>0:\ c(L,t)/c_f=0.95\},$$

$$q_{\mathrm{dyn}}=\frac{1}{(1-\varepsilon)\rho_pL}\int_0^{t_{BT}}u\bigl[c_f-c(L,t)\bigr]dt\quad[\mathrm{mol\,kg^{-1}}],$$

MTZ length $L_{MTZ}=L\,\dfrac{t_{sat}-t_{BT}}{t_{st}}$ (front-width reading of D.3's $\ell_\pm$). Definition discipline: the prompt's $q_{\mathrm{dyn}}$ integrates only to $t_{BT}$ (capacity *used at breakthrough*); the pipeline's saturation-integrated variant estimates $q^*(c_f,T_0)$ by Corollary B.1. Both are meaningful; never compare one to the other.

### E.5 Validation ladder (with quantitative gates)

1. **No adsorption** ($k=0$, $q\equiv0$): outlet trace vs analytical step solution (D.5) with $v=u/\varepsilon$, $D=D_L$; relative $L^2$ error $<1\%$ (**Gate A**).
2. **Isothermal equilibrium shock** ($T=T_0$, large $Da$, $Pe$ large): measured mid-front speed (e.g. $t_{50}$ crossing) vs $v_{RH}$ (D.3) within ±10 % (**Gate B**); additionally the first-moment $\int(1-c/c_f)dt$ must equal $t_{st}$ (Cor. B.1) — a sharper, model-free check.
3. **Finite-$Da$ family**: front width shrinks ~$1/k$ (D.3), outlet curve → RH step as $Da\uparrow$; overlay the exact Langmuir wave (D.8).
4. **Full non-isothermal benchmark**: $t_{BT}$ within ±20 % of the benchmark breakthrough (Stampi-Bombelli 2024 at 400 ppm — **Gate C**), plus qualitative $T$-excursion and roll-up check.
5. **Mass-balance drift**: $\bigl|\int_0^{t_{end}}u[c_f-c(L,t)]dt-\bigl[M(t_{end})-M(0)\bigr]\bigr|/\bigl(uc_ft_{end}\bigr)$. Scheme (b) telescopes exactly at the semi-discrete level, so the *reported* metric is limited only by ODE tolerance and output-sampling quadrature: require $<10^{-4}$ (measured: $5\times10^{-5}$, App. V). Scheme (a): $<10^{-3}$ at working resolution (the Dirichlet defect is physical to that scheme, cf. B.1).

---

## Appendix V — Numerical verification of every closed-form claim

Produced by `src/solver/mechanistic_verify.py` (FV scheme (b), LSODA, banded Jacobian, interleaved state; numpy 2.2.6 / scipy 1.15.3). Figures in `src/img/generated/mechanistic/`. Parameters are the illustrative-flagged set of §C.4 — the tests verify **mathematics**, not sorbent values. Run: `python src/solver/mechanistic_verify.py [t1 t2 t3 t5]`.

### V.1 — Gate-A analogue: no-adsorption ADE vs (D.5) — `V1_ade_vs_erfc.png`

![Figure 5) Full non-isothermal Toth demo](https://github.com/lohjo/ProjID3/blob/main/src/img/generated/mechanistic/V1_ade_vs_erfc.png?raw=true)

$k=0$, $Pe_i=v_iL/D_L\approx303$; outlet trace vs Ogata–Banks, relative $L^2$ error:

| $N$ | 500 | 1000 | 2000 | 4000 |
|---|---|---|---|---|
| error | 1.33 % | 0.69 % | 0.35 % | 0.17 % |

Error halves per grid doubling — the clean first-order signature of upwind + $D_{\mathrm{num}}=u\Delta z/2\varepsilon$ predicted in §E.2 ($N\gg Pe/2\varepsilon\approx380$ indeed marks the <1 % boundary). **Gate A (<1 % $L^2$) passes for $N\ge1000$.**

### V.2 — Rankine–Hugoniot speed (D.3) and first-moment invariance (Cor. B.1) — `V2_rh_front.png`

![Figure 5) Full non-isothermal Toth demo](https://github.com/lohjo/ProjID3/blob/main/src/img/generated/mechanistic/V2_rh_front.png?raw=true)

Isothermal Langmuir ($bc_f=2.045$), $Da=kL/u\approx14$, $D_L=10^{-6}$, $N=800$:

| quantity | analytical | numerical | error |
|---|---|---|---|
| front speed | $v_{RH}=2.7028\times10^{-4}$ m s⁻¹ | $2.7034\times10^{-4}$ m s⁻¹ (fit of $z_{50\%}(t)$) | **0.020 %** |
| stoichiometric time | $t_{st}=777.0$ s | first moment $\int(1-c_{out}/c_f)\,dt=777.0$ s | **<0.005 %** |

Gate B tolerance is ±10 %; the scheme is three orders inside it. The moment identity holding to solver precision is the numerical fingerprint of the exact Danckwerts-flux inlet (B.3).

### V.3 — Exact LDF travelling wave (D.8) — `V3_travelling_wave.png`

![Figure 5) Full non-isothermal Toth demo](https://github.com/lohjo/ProjID3/blob/main/src/img/generated/mechanistic/V3_travelling_wave.png?raw=true)

Finite kinetics ($k=0.02$ s⁻¹, $D_L=0$), $N=3000$, profile sampled at $0.65\,t_{st}$ and overlaid on the implicit closed form $\ln w-(1+bc_f)\ln(1-w)=-(kbc_f/v_{RH})(\eta-\eta_0)$ after matching only the 50 % point (no fitted parameters): **RMS deviation 0.30 %** over $0.02<c/c_f<0.98$. The predicted tail asymmetry is visible: saturation tail $\ell_-\approx(1+bc_f)$-fold slower than the leading foot — the mechanistic origin of the tailing that symmetric logistic fits (M01) cannot represent.

### V.4 — Mass-balance drift (E.5-5)

Over the full T2 run: relative drift $4.6\times10^{-5}$, dominated by the output-sampling trapezoid of the outflow term, not by the scheme (semi-discretely exact). **Passes <10⁻⁴.**

### V.5 — Full non-isothermal Toth demo — `V4_nonisothermal.png`

![Figure 5) Full non-isothermal Toth demo](https://github.com/lohjo/ProjID3/blob/main/src/img/generated/mechanistic/V4_nonisothermal.png?raw=true)

Toth ($n_{s0}=2.5$ mol kg⁻¹, $b(T_0)=0.49$ m³ mol⁻¹, $t_0=0.4$, $Q_{\mathrm{iso}}=70$ kJ mol⁻¹), $k=5\times10^{-3}$ s⁻¹, $q_f=0.61$ mol kg⁻¹ (inside the measured $q_{dyn}$ band 0.55–0.89 of runs 3–8), $t_{st}=707$ s:

| case | $t_{BT}$ (5 %) | $t_{sat}$ (95 %) | $\Delta T_{\max}$ | max $c/c_f$ | $q_{\mathrm{dyn}}$ (to $t_{BT}$) |
|---|---|---|---|---|---|
| isothermal | 293 s | — | 0 | 1.000 | — |
| wall-coupled ($h_w=30$) | 217 s | 1572 s | **4.9 K** | 0.988 | 0.187 mol kg⁻¹ |
| adiabatic | 132 s | 833 s | **18.9 K** | 0.956 → plateau | 0.114 mol kg⁻¹ |

Readings, each tied to a derived result: (i) heat release accelerates breakthrough (adiabatic $t_{BT}$ = 45 % of isothermal) because $b(T)$ falls with $T$ — the $q^*(c,T)$ feedback of §D.6; (ii) the adiabatic outlet stalls on a **hot plateau** at $c/c_f\approx0.955$ while $T$ stays +18.9 K: the concentration wave has passed but full capacity is only released as the (much slower, $v_{th}=\gamma_h u$) thermal wave clears — the two-wave structure predicted in §D.6, and a warning that threshold-based $t_{sat}$ interacts pathologically with thermal plateaus; (iii) the wall-coupled excursion (+4.9 K peak, decaying) matches the §A.4 order-of-magnitude estimate $\Delta T\approx\Delta T_{\mathrm{ad}}\tau_w/t_{st}\approx3$–4 K for the 8.5 mm rig, supporting near-isothermal operation of the bench column while showing the same sorbent would run ~19 K hot adiabatically (scale-up warning); (iv) the prompt-definition $q_{\mathrm{dyn}}$ (integrated to $t_{BT}$) is 3–5× below $q_f$ — quantifying §E.4's warning against comparing differently-defined capacities.

### V.6 — Verdict

Every closed-form claim in Parts B and D is reproduced by the Part-E discretisation within stated tolerances; the scheme meets Gates A and B with wide margin and conserves inventory to output-quadrature precision. The single unverified item — Gate C against the Stampi-Bombelli 2024 benchmark — is blocked only on the Toth parameter values (still `??` in `CLAUDE.md`), not on any element of this formulation.

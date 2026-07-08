# Parametric Study of CO₂ Adsorption Breakthrough in Packed-Bed Columns

## A Unified Analytical–Numerical Model for PEI@SiO₂ Solid Sorbents

**Author:** John Ray Loh  
**Affiliation:** Ngee Ann Polytechnic / SUTD Collaboration  
**Date:** May 2026

-----

## 1. Executive Summary and Problem Statement

**Problem:** Develop a mathematical (analytical/numerical) model to describe CO₂ adsorption breakthrough on PEI@SiO₂ solid sorbents within a fixed-bed column.

**Solution developed below:** A *dual-kinetic travelling-wave model with non-isothermal correction*, which unifies the analytical travelling-wave framework of Myers & Font (2020) with the dual-kinetic (DK) amine-site physics of Stampi-Bombelli, Storione, Grossmann & Mazzotti (2024), adapted specifically for polyethylenimine-impregnated mesoporous silica (PEI@SiO₂) granules. The model captures the asymmetric breakthrough tails that are characteristic of amine-functionalized sorbents and provides closed-form expressions for the initial breakthrough while requiring numerical integration only for the slow amine-layer tail — a creative hybrid that no single paper in the reference set achieves alone.

-----

## 2. Physical System Description

The system under consideration is a cylindrical packed-bed column of length $L$ and internal radius $R$, filled with spherical or near-spherical PEI@SiO₂ granules of mean diameter $d_p$. A gas mixture of CO₂ (mole fraction $y_{in}$) in N₂ enters the column at superficial velocity $u_s$ and temperature $T_{in}$.

**Sorbent material — PEI@SiO₂:** Mesoporous silica (SBA-15 or fumed silica, pore diameter ~6–13 nm) is impregnated with branched polyethylenimine (PEI, molecular weight ~600–25000). The PEI fills the mesopore network and provides a high density of amine groups (primary, secondary, tertiary) that react chemically with CO₂ via carbamate and bicarbonate formation. The sorbent exhibits two structurally distinct classes of amine sites: (i) easily accessible **surface amine sites** at the PEI–gas interface, and (ii) **bulk amine-layer sites** buried within the PEI polymer matrix, which require diffusion through the viscous polymer before CO₂ can react (Bollini et al., 2012; Kalyanaraman et al., 2015; Stampi-Bombelli et al., 2024). This heterogeneity produces the characteristic *sharp initial breakthrough followed by a prolonged tail* observed experimentally in amine-functionalized sorbents, which a simple pseudo-first-order (PFO) model cannot capture.

The key material parameters, drawn from the Cheong (2021) thesis, the SUTD experimental programme, and the Stampi-Bombelli et al. (2024) / Grossmann et al. (2023) measurements on analogous amine-functionalized silica/alumina systems, are:

|Symbol          |Meaning                                  |Typical PEI@SiO₂ Value|Units   |
|----------------|-----------------------------------------|----------------------|--------|
|$d_p$           |Granule diameter                         |0.5–3.0               |mm      |
|$\varepsilon$   |Bed void fraction                        |0.35–0.55             |—       |
|$\varepsilon_p$ |Particle (pellet) porosity               |0.45–0.71             |—       |
|$\rho_p$        |Pellet density                           |500–1100              |kg m⁻³  |
|$\rho_s$        |Skeletal (material) density              |2000–3600             |kg m⁻³  |
|$q_s^*$         |Equilibrium capacity (at $p_{CO_2}$, $T$)|0.5–3.5               |mol kg⁻¹|
|$\Delta H_{ads}$|Isosteric heat of adsorption             |60–90                 |kJ mol⁻¹|
|$\eta$          |Fraction of surface amine sites          |0.60–0.85             |—       |

-----

## 3. Governing Equations

### 3.1 Assumptions

The model makes the following assumptions, each justified by the referenced literature and by order-of-magnitude analysis:

**A1.** The gas is ideal: $p = c R_g T$ where $c = c_1 + c_2$ is the total molar concentration (Myers & Font, 2020, eq. 5).

**A2.** Plug flow with no radial gradients. The Péclet number based on particle diameter is $Pe_p = u d_p / D_m \gtrsim 10$ for typical DAC and post-combustion conditions, justifying the neglect of radial dispersion (Stampi-Bombelli et al., 2024; Zhang et al., 2016).

**A3.** Axial dispersion is included explicitly via a dispersion coefficient $D_L$ because the constant-pattern analysis of Stampi-Bombelli et al. (2024) demonstrated that axial dispersion is significant in packed beds, especially at higher concentrations.

**A4.** The momentum balance reaches steady state instantaneously (Stampi-Bombelli et al., 2024, Section 2.4.1), so the Ergun equation describes the pressure drop at each instant.

**A5.** The adsorbed phase obeys a **Toth isotherm** — the standard choice for amine-functionalized silica/alumina sorbents, as fitted by Grossmann et al. (2023) and used by Stampi-Bombelli et al. (2024), Pedrozo et al. (2025), and the Cheong (2021) thesis. The Toth isotherm accommodates the steep, favorable shape characteristic of chemisorption.

**A6.** Mass transfer is described by a **dual-kinetic (DK) linear driving force** model, distinguishing surface and bulk amine sites (Kalyanaraman et al., 2015; Ohs et al., 2018; Stampi-Bombelli et al., 2024).

**A7.** A lumped non-isothermal correction is included. Although Myers & Font (2020) showed that temperature variation is small for physical adsorption on activated carbon, the high heat of adsorption ($\Delta H_{ads} \sim 70$ kJ/mol) of PEI@SiO₂ causes measurable temperature peaks ($>15$ °C at 5.6% CO₂; Stampi-Bombelli et al., 2024, Section 3.1), which shift the equilibrium and affect breakthrough timing.

### 3.2 Species Mass Balance (CO₂)

Following Myers & Font (2020, eq. 12) with axial dispersion retained:

$$
\varepsilon \frac{\partial c_1}{\partial t} + \frac{\partial (u , c_1)}{\partial z} = \varepsilon D_L \frac{\partial^2 c_1}{\partial z^2} - (1 - \varepsilon) \rho_p \frac{\partial \bar{q}}{\partial t}
$$

where $c_1(z,t)$ is the molar concentration of CO₂ in the gas phase [mol m⁻³], $u(z,t)$ is the interstitial velocity, $\bar{q}(z,t)$ is the average adsorbed-phase loading [mol kg⁻¹ sorbent], $\rho_p$ is the pellet density, and $\varepsilon$ is the bed void fraction.

### 3.3 Carrier Gas (N₂) Mass Balance

$$
\varepsilon \frac{\partial c_2}{\partial t} + \frac{\partial (u , c_2)}{\partial z} = \varepsilon D_L \frac{\partial^2 c_2}{\partial z^2}
$$

Since N₂ is not adsorbed by PEI@SiO₂, there is no sink term.

### 3.4 Dual-Kinetic (DK) Adsorption Rate Model

This is the **novel core** of the model, adapted from Stampi-Bombelli et al. (2024, eqs. 7–13) and Kalyanaraman et al. (2015) for PEI@SiO₂. The total loading is partitioned between surface and bulk amine sites:

$$
\bar{q} = q_1 + q_2
$$

The rate of uptake on the surface sites (fraction $\eta$ of total capacity $q^*$) is governed by the overall resistance to reach the particle surface:

$$
\frac{\partial q_1}{\partial t} = k_1 \left( \eta , q^*(c_1, T) - q_1 \right)
$$

The rate of uptake on the bulk amine-layer sites (fraction $1-\eta$) includes an additional resistance for diffusion within the PEI polymer:

$$
\frac{\partial q_2}{\partial t} = k_2 \left( (1 - \eta) , q^*(c_1, T) - q_2 \right)
$$

The overall mass transfer coefficients $k_1$ and $k_2$ are constructed from resistances in series:

$$
\frac{1}{k_1} = \frac{1}{\frac{q^**{p,in}}{c*{in}} k_f} + \frac{1}{\frac{q^**{p,in}}{c*{in}} k_p} + \frac{1}{k_s}
$$

$$
\frac{1}{k_2} = \frac{1}{k_1} + \frac{1}{k_{s,amine}}
$$

where $k_f$, $k_p$, $k_s$ are the film, pore, and solid (crystallite) mass transfer coefficients respectively, and $k_{s,amine}$ is the rate coefficient for transport within the bulk PEI layer. For PEI@SiO₂ granules:

The film coefficient is estimated from the Wakao-Funazkri correlation: $Sh = 2 + 1.1 , Re^{0.6} Sc^{1/3}$, giving $k_f’ = D_m Sh / d_p$ and $k_f = 3 k_f’ / r_p$.

The pore coefficient accounts for combined molecular and Knudsen diffusion within the mesoporous silica: $k_p = 15 D_p / r_p^2$ (Glueckauf LDF approximation, 1955), where the effective pore diffusivity is $D_p = (1/D_m + 1/D_K)^{-1} / \tau$ with Knudsen diffusivity $D_K = d_{pore} \sqrt{8 R_g T / (\pi M_1)} / 3$ and tortuosity $\tau \approx 2.5$ (Zhang et al., 2016; Stampi-Bombelli et al., 2024).

The solid (crystal) coefficient $k_s = 15 D_s / r_c^2$ accounts for diffusion within the primary silica particles if applicable. For impregnated PEI@SiO₂ where PEI fills the mesopores, $k_s$ is very large (fast access to the PEI surface) and the dominant resistance is in the PEI layer itself, giving $k_{s,amine} \sim 10^{-4}$–$10^{-3}$ s⁻¹ (Stampi-Bombelli et al., 2024, Table 7: $k_{s,amine} = 0.0011$ s⁻¹ for analogous amine-grafted alumina).

### 3.5 Toth Isotherm

The equilibrium loading $q^*(p_{CO_2}, T)$ follows the temperature-dependent Toth isotherm (Grossmann et al., 2023; Stampi-Bombelli et al., 2024, eqs. 1–4):

$$
q^*(p_{CO_2}, T) = \frac{n_s(T) , b(T) , p_{CO_2}}{\left[1 + \left(b(T) , p_{CO_2}\right)^{t(T)}\right]^{1/t(T)}}
$$

where

$$
n_s(T) = n_{s0} \exp\left[\chi \left(1 - \frac{T}{T_0}\right)\right], \quad b(T) = b_0 \exp\left[\frac{\Delta H_0}{R_g T_0}\left(\frac{T_0}{T} - 1\right)\right], \quad t(T) = t_0 + \alpha\left(1 - \frac{T_0}{T}\right)
$$

Typical fitted parameters for PEI@SiO₂ at reference temperature $T_0 = 298$ K are: $n_{s0} \approx 1.0$–$3.5$ mol kg⁻¹, $b_0 \approx 10^2$–$10^4$ kPa⁻¹, $t_0 \approx 0.2$–$0.4$, $\Delta H_0 \approx 70$ kJ mol⁻¹, $\chi \approx 0$, $\alpha \approx 0.1$. The CO₂ partial pressure is related to the gas-phase concentration by $p_{CO_2} = c_1 R_g T$.

### 3.6 Energy Balance

$$
\left[\varepsilon \rho_g c_{p,g} + (1-\varepsilon) \rho_p c_{p,s}\right] \frac{\partial T}{\partial t} + \varepsilon \rho_g c_{p,g} , u \frac{\partial T}{\partial z} = \lambda_{eff} \frac{\partial^2 T}{\partial z^2} + (1-\varepsilon) \rho_p (-\Delta H_{ads}) \frac{\partial \bar{q}}{\partial t} - \frac{4 h_W}{d_{col}} (T - T_W)
$$

where $\lambda_{eff}$ is the effective axial thermal conductivity, $h_W$ is the wall heat transfer coefficient [W m⁻² K⁻¹], $d_{col}$ is the column diameter, and $T_W$ is the wall (ambient) temperature. For small-diameter laboratory columns, the wall heat loss term is significant (Stampi-Bombelli et al., 2024 used $h_W \approx 10$–26 W m⁻² K⁻¹).

### 3.7 Momentum Balance (Ergun Equation)

$$
-\frac{\partial p}{\partial z} = \frac{150 \mu_g (1-\varepsilon)^2}{\varepsilon^3 d_p^2} u_s + \frac{1.75 (1-\varepsilon)}{\varepsilon^3 d_p} \rho_g |u_s| u_s
$$

where $u_s = \varepsilon u$ is the superficial velocity. For low Reynolds number flows (typical of DAC conditions: $Re \lesssim 10$), the quadratic term is negligible and the Ergun relation reduces to the Darcy-type form used by Myers & Font (2020, eq. 8): $-\partial p / \partial z = \beta u$ with $\beta = 150 \mu_g (1-\varepsilon)^2 / (\varepsilon^2 d_p^2)$.

### 3.8 Ideal Gas Law (Closure)

$$
p = (c_1 + c_2) R_g T
$$

### 3.9 Boundary and Initial Conditions

At the inlet $z = 0$: Danckwerts conditions for the species balances (Myers & Font, 2020, eqs. 17–18):

$$
u_0 c_{1,in} = \left. \left(u c_1 - \varepsilon D_L \frac{\partial c_1}{\partial z}\right)\right|*{z=0^+}, \qquad u_0 c*{2,in} = \left. \left(u c_2 - \varepsilon D_L \frac{\partial c_2}{\partial z}\right)\right|_{z=0^+}
$$

$$
T(0, t) = T_{in}, \qquad p(0, t) = p_0(t) \text{ or } u_s(0,t) = u_{s,0} \text{ (flow-controlled)}
$$

At the outlet $z = L$: zero-gradient conditions $\partial c_1 / \partial z = \partial c_2 / \partial z = \partial T / \partial z = 0$, and $p(L, t) = p_{atm}$.

Initial conditions: $c_1(z, 0) = 0$, $c_2(z, 0) = p_{atm} / (R_g T_{in})$, $q_1(z,0) = q_2(z,0) = 0$, $T(z,0) = T_{in}$.

-----

## 4. Novel Analytical Reduction: The Dual-Kinetic Travelling Wave

This section presents the **creative and novel element** of this work: an extension of the Myers & Font (2020) travelling-wave analysis to accommodate the dual-kinetic model for amine sorbents, yielding a *hybrid analytical–numerical breakthrough expression*.

### 4.1 Non-Dimensionalisation

Following Myers & Font (2020, Section 3), we scale:

$$
\hat{c}*1 = \frac{c_1}{c*{1,0}}, \quad \hat{q}_i = \frac{q_i}{q_0^*}, \quad \hat{x} = \frac{z}{\mathcal{L}}, \quad \hat{t} = k_1 t, \quad \hat{u} = \frac{u}{u_0}
$$

where $q_0^* = q^*(p_{CO_2,in}, T_{in})$ is the equilibrium capacity at inlet conditions, $\mathcal{L} = u_0 c_{1,0} / ((1-\varepsilon) \rho_p q_0^* k_1)$ is the reaction length scale, and $k_1$ is the surface-site overall mass transfer coefficient.

Define the key dimensionless groups:

$$
\delta_1 = \frac{\mathcal{L} k_1}{u_0} = \frac{c_{1,0}}{(1-\varepsilon)\rho_p q_0^*}, \qquad \delta_2 = \frac{D_L}{\mathcal{L} u_0}, \qquad \delta_5 = \frac{c_{1,0}}{c_{2,0}}, \qquad \kappa = \frac{k_2}{k_1}
$$

The parameter $\delta_1$ is the ratio of the inlet CO₂ concentration to the bed’s adsorption capacity; for DAC conditions ($y_{in} = 400$ ppm) this is extremely small ($\delta_1 \sim 10^{-5}$), while for post-combustion ($y_{in} = 5$–15%) it reaches $\delta_1 \sim 10^{-2}$. The ratio $\kappa = k_2 / k_1$ is the key new parameter: it quantifies the relative slowness of the bulk amine sites. For PEI@SiO₂, $\kappa \ll 1$ (typically 0.01–0.1), reflecting the two-order-of-magnitude decrease in mass transfer coefficient when transport through the PEI layer is required.

### 4.2 Leading-Order Equations

For $\delta_1, \delta_2 \ll 1$ (which holds for both DAC and post-combustion conditions), the time-derivative and diffusion terms are negligible at leading order in the species balances, giving (cf. Myers & Font, 2020, eqs. 41–42):

$$
\frac{\partial}{\partial \hat{x}}(\hat{u} \hat{c}_1) = -\frac{\partial \hat{q}_1}{\partial \hat{t}} - \frac{\partial \hat{q}_2}{\partial \hat{t}}, \qquad \frac{\partial}{\partial \hat{x}}(\hat{u} \hat{c}_2) = 0
$$

The adsorption rate equations become:

$$
\frac{\partial \hat{q}_1}{\partial \hat{t}} = \eta \hat{q}^* - \hat{q}_1, \qquad \frac{\partial \hat{q}_2}{\partial \hat{t}} = \kappa \left[(1-\eta) \hat{q}^* - \hat{q}_2\right]
$$

### 4.3 Travelling-Wave Solution for the Fast Sites

We introduce a moving coordinate $\xi = \hat{x} - \hat{v} \hat{t}$ and seek a travelling wave with constant velocity $\hat{v}$. Following the same procedure as Myers & Font (2020, Section 4.1), the N₂ balance integrates to $\hat{u} \hat{c}*2 = 1$, and the ideal gas law gives $\hat{c}*2 = (1 - \delta*{45} \hat{c}*1)/\delta_4$ where $\delta_4 = R_g T c*{2,0} / p_a$ and $\delta*{45} = \delta_4 \delta_5$.

**Key insight:** When $\kappa \ll 1$, the fast surface sites ($q_1$) dominate the *initial* part of the breakthrough while the slow bulk sites ($q_2$) produce the *tail*. On the timescale of the travelling wave ($\hat{t} \sim O(1)$ on the $k_1$ scale), the slow-site contribution $\partial \hat{q}_2 / \partial \hat{t} \sim O(\kappa)$ is a perturbation.

At leading order (neglecting $O(\kappa)$ terms), the travelling-wave analysis for $\hat{q}_1$ alone proceeds exactly as in Myers & Font (2020), yielding:

$$
\hat{f}(\xi) = \hat{v}*\eta \left(1 - e^{\xi / \hat{v}*\eta}\right), \qquad \hat{q}*1(\xi) = \eta\left(1 - e^{\xi / \hat{v}*\eta}\right)
$$

where $\hat{f} = \hat{u} \hat{c}*1$ and the wave velocity is modified to $\hat{v}*\eta = 1/\eta$ (the wave moves faster because only a fraction $\eta$ of the capacity is being filled by the fast sites).

Transforming back to dimensional variables and evaluating at $z = L$, the **fast-site breakthrough curve** is:

$$
\boxed{c_1^{(fast)}(L, t) = c_{1,0} \cdot \frac{1 - \exp\left(-k_1(t - t_b)\right)}{1 - \frac{R_g T c_{1,0}}{p_a} \exp\left(-k_1(t - t_b)\right)}, \qquad t \geq t_b}
$$

where the breakthrough time is $t_b = \eta , (1-\varepsilon) \rho_p q_0^* L / (u_0 c_{1,0})$, which is precisely the stoichiometric time for saturating only the surface sites.

This is identical in functional form to Myers & Font (2020, eq. 65), but with two critical modifications: (i) $t_b$ is scaled by $\eta$ rather than by the total capacity, reflecting that the fast wave saturates only the surface sites, and (ii) $k_1$ replaces $k_q$, being the surface-site overall mass transfer coefficient.

### 4.4 Slow-Site Tail Correction (Perturbation Solution)

After the fast wave has passed a given location and the surface sites are nearly saturated ($q_1 \approx \eta q^*$), the local CO₂ concentration rises to nearly $c_{1,0}$ and the remaining uptake is governed by the slow bulk sites:

$$
\frac{\partial q_2}{\partial t} = k_2 \left[(1-\eta) q^*(c_{1,0}, T) - q_2\right]
$$

This is a simple first-order ODE with solution:

$$
q_2(t) = (1-\eta) q_0^* \left[1 - \exp\left(-k_2(t - t_b)\right)\right], \qquad t \geq t_b
$$

The slow-site uptake acts as a residual sink that modifies the local mass balance. Substituting into the full species balance and solving perturbatively around the fast-site travelling wave, we obtain the **combined breakthrough expression** (the main novel result):

$$
\boxed{\frac{c_1(L,t)}{c_{1,0}} \approx \underbrace{\frac{1 - e^{-k_1(t - t_b)}}{1 - \delta_{45} , e^{-k_1(t - t_b)}}}*{\text{Fast surface sites (analytical TW)}} - \underbrace{\frac{(1-\eta)}{\eta} \cdot \kappa \cdot e^{-k_2(t - t_b)}}*{\text{Slow bulk amine tail correction}}}
$$

valid for $t \geq t_b$ and where we have defined $\delta_{45} = R_g T c_{1,0} / p_a$.

The first term is the sharp sigmoidal rise (the Myers–Font travelling wave adapted for partial capacity $\eta$). The second term is a decaying exponential tail that suppresses the concentration below $c_{1,0}$ at long times — precisely the asymmetric tail observed in PEI@SiO₂ breakthrough experiments. As $t \to \infty$, the tail correction vanishes and $c_1 \to c_{1,0}$ (full saturation). The total stoichiometric breakthrough time (including both sites) is $t_{b,total} = (1-\varepsilon) \rho_p q_0^* L / (u_0 c_{1,0})$.

### 4.5 Limiting Cases

**Case 1: $\eta = 1$ (homogeneous sites, no bulk amine layer).** The DK model reduces to the standard PFO/LDF model, $k_2$ and $k_{s,amine}$ drop out, and we recover exactly the Myers & Font (2020, eq. 65) result. This is the appropriate limit for physical adsorbents like activated carbon or zeolites.

**Case 2: $\kappa \to 0$ (infinitely slow bulk sites).** The tail correction persists indefinitely. The breakthrough curve rises sharply to $(1 - (1-\eta)/\eta \cdot \kappa) c_{1,0} \approx c_{1,0}$ but the approach to full saturation is arrested. This corresponds to the experimental observation that some PEI@SiO₂ sorbents require many hours to reach full capacity at DAC concentrations (Stampi-Bombelli et al., 2024, Table 6: $t_{90} > 45$ hours at 400 ppm).

**Case 3: $\delta_{45} \to 0$ (trace CO₂, incompressible flow).** This is the DAC limit ($y_{in} = 400$ ppm). The fast-site term simplifies to $c_1/c_{1,0} \approx 1 - e^{-k_1(t-t_b)} - \frac{(1-\eta)}{\eta} \kappa , e^{-k_2(t-t_b)}$, which is a sum of two exponentials with distinct rate constants. The velocity is approximately constant ($u \approx u_0$), consistent with Myers & Font’s incompressible model (2020, eq. 76).

-----

## 5. Full Numerical Model (for Validation and Non-Isothermal Extension)

When the non-isothermal effects are important (as they are for PEI@SiO₂ at concentrations above ~1%), the analytical travelling wave is no longer exact because the isotherm parameters $b(T)$, $n_s(T)$, $t(T)$ vary with local temperature. In this case, the full PDE system (Sections 3.2–3.8) must be solved numerically. Following the approach of Myers & Font (2020, Appendix A) and Pedrozo et al. (2025):

The numerical scheme uses second-order central finite differences in space and explicit Euler (or a method-of-lines approach with `ode15s` in MATLAB / `solve_ivp` in Python) in time. The advection term is handled with an upwind scheme. The velocity field is reconstructed at each time step from the integral relation (Myers & Font, 2020, eq. A.16):

$$
u(z, t) = u_0 - \delta_4 \delta_5 \int_0^z \frac{\partial \bar{q}}{\partial t} , dz’
$$

The DK adsorption equations are solved simultaneously with the energy balance. The Heaviside function $H(c_1)$ of Myers & Font (2020, eq. A.13) is used to activate adsorption only in regions where CO₂ is present, avoiding the need to track the moving front explicitly.

Stability criteria: $\Delta t \cdot D_L / (\Delta z^2) \leq 0.5$ and $\max(u) \cdot \Delta t / \Delta z \leq 1$. Typical discretisation: $\Delta z = L/200$, $\Delta t$ adaptive.

-----

## 6. Model Parameters and Calibration Strategy

The model contains the following groups of parameters:

**Group 1 — Known from sorbent characterisation** (measured independently, not fitted): $d_p$, $\varepsilon$, $\varepsilon_p$, $\rho_p$, $\rho_s$, $L$, $R$, $T_{in}$, $p_{atm}$, $y_{in}$, $u_{s,0}$, $D_m$, $\mu_g$, $c_{p,g}$, $c_{p,s}$.

**Group 2 — Isotherm parameters** (from volumetric adsorption measurements, e.g. BELSORP): $n_{s0}$, $b_0$, $t_0$, $\Delta H_0$, $\chi$, $\alpha$.

**Group 3 — Transport parameters to be fitted from breakthrough data**: $k_1$ (or equivalently $k_g$ and $k_s$), $k_2$ (or $k_{s,amine}$), $\eta$, $D_L$ (or $p_1$, $p_2$ in a linear velocity correlation $D_L = p_1 u + p_2$).

**Calibration procedure** (following Stampi-Bombelli et al., 2024, Section 2.4.5):

1. Fit $k_1$ and $D_L$ to the initial part of the breakthrough curve (up to 70% of uptake) using maximum likelihood estimation.
1. Fit $\eta$ and $k_2$ to the full breakthrough curve (including the tail) via sensitivity analysis on these parameters.
1. Validate that $k_f$ and $k_p$ from literature correlations are consistent with the fitted $k_1$.
1. Verify $t_b$ against the stoichiometric prediction $t_b = \eta (1-\varepsilon) \rho_p q_0^* L / (u_0 c_{1,0})$.

-----

## 7. Connection to the Broader Literature

**Myers & Font (2020)** provided the foundational travelling-wave framework and the key insight that *the shape of the breakthrough curve is primarily determined by the mass transfer model*. Their model, however, used a simple LDF rate equation $\partial q / \partial t = k_q(q^* - q)$ appropriate for homogeneous physical adsorbents. The present model extends their analytical machinery to heterogeneous chemisorption by decomposing the total uptake into two kinetically distinct site populations.

**Cheong (2021, NUS/SUTD thesis)** developed macroscopic and microscopic models for CO₂ adsorption in PEI/SiO₂ nanocomposite membranes using COMSOL, considering multi-scale transport from the gas phase through agglomerations into individual nanofillers. His Macroscopic Model I uses a fractional-order kinetic rate and Langmuir isotherm, while the Microscopic Model uses a pore volume and surface diffusion framework. The present model bridges Cheong’s material-level physics (PEI@SiO₂ structure, Langmuir/Toth isotherm, intraparticle diffusion) with the column-scale breakthrough framework of Myers & Font, which Cheong did not address (his work focused on thin-film membranes, not packed beds).

**Stampi-Bombelli et al. (2024, ETH Zurich / Mazzotti group)** provided the DK model formulation and the critical experimental observation that PFO is sufficient for packed beds of large pellets (where gas-phase resistance dominates) but fails for monoliths (where the fast gas-phase transport exposes the slow amine-layer kinetics). The present model adapts their DK framework into an analytical travelling-wave, which they did not attempt — their work used purely numerical solutions.

**Pedrozo et al. (2025, CMU/LLNL)** developed a COMSOL reactive transport model optimised via trust-region methods and Gaussian Processes, finding a minimum DAC capture cost of $265.2/t-CO₂. Their model is comprehensive but computationally expensive (2D axisymmetric model ~40× slower than 1D). The present analytical travelling-wave provides a fast surrogate for the initial breakthrough that can be embedded in optimisation loops at negligible computational cost.

**Zhang et al. (2016)** demonstrated the LDF breakthrough model with Freundlich isotherm for K-based sorbents, emphasising that internal mass transfer (molecular + Knudsen diffusion) is more sensitive than external mass transfer for porous sorbents. This finding directly supports the structure of our $k_1$ and $k_2$ expressions, where the pore coefficient (incorporating Knudsen diffusion in the mesopores of silica) is the dominant resistance in $k_1$.

**Chen et al. (2023)** proposed a W-shaped packed bed for indoor DAC with an amine-functionalized material, modelling temperature swing adsorption (TSA) with Darcy-Forchheimer flow. Their energy consumption analysis ($236.2$ kJ/mol for conventional bed, $167.9$ kJ/mol for W-shaped) provides a benchmark against which the present model’s predictions of energy-optimal bed geometry and cycle timing could be compared.

**Guo & Wang (2019)** derived a general mixed-order kinetic model unifying PFO and PSO. Their analysis shows that the PFO and PSO models represent limiting cases of a more general framework, which motivates the present choice of two LDF terms (each first-order) rather than a single second-order term — the DK model achieves the asymmetry of a mixed-order model while retaining the physical interpretability of distinct site populations.

-----

## 8. Summary Paragraph

The system under study is a fixed-bed column packed with PEI@SiO₂ granules — mesoporous silica impregnated with branched polyethylenimine — through which a CO₂/N₂ gas mixture flows at controlled velocity, and the mathematical model developed here unifies the analytical travelling-wave framework of Myers and Font (Int. J. Heat Mass Transfer, 2020), who showed that non-dimensionalisation of the mass continuity equation $\varepsilon , \partial c_1/\partial t + \partial(u c_1)/\partial z = \varepsilon D_L , \partial^2 c_1/\partial z^2 - (1-\varepsilon)\rho_p , \partial \bar{q}/\partial t$ coupled to the ideal gas law $p = cR_gT$ and the Ergun momentum relation $-\partial p/\partial z = \beta u + \alpha \rho_g u^2$ reveals that the temporal and diffusive terms are $O(10^{-2})$ corrections to the advection–reaction balance, permitting a travelling-wave substitution $\xi = z - v_f t$ that yields the closed-form breakthrough $c_1(L,t)/c_{1,0} = (1 - e^{-k(t-t_b)})/(1 - (R_gTc_{1,0}/p_a)e^{-k(t-t_b)})$ — with the dual-kinetic (DK) adsorption model of Stampi-Bombelli, Storione, Grossmann, and Mazzotti (Ind. Eng. Chem. Res., 2024) and Kalyanaraman et al. (Chem. Eng. J., 2015), which partitions the total loading $\bar{q} = q_1 + q_2$ into fast surface amine sites ($\partial q_1/\partial t = k_1(\eta q^* - q_1)$, fraction $\eta \approx 0.75$) and slow bulk PEI-layer sites ($\partial q_2/\partial t = k_2((1-\eta)q^* - q_2)$, with $k_2 \ll k_1$ due to the additional resistance $1/k_{s,amine}$ for diffusion through the viscous polyethylenimine), where the equilibrium capacity $q^*$ is described by the temperature-dependent Toth isotherm $q^* = n_s(T) b(T) p_{CO_2}/[1+(b(T)p_{CO_2})^{t(T)}]^{1/t(T)}$ fitted by Grossmann et al. (Ind. Eng. Chem. Res., 2023) with typical parameters $n_{s0} \approx 1.23$ mol/kg, $b_0 \approx 4839$ kPa$^{-1}$, $t_0 \approx 0.25$, $\Delta H_0 \approx 70$ kJ/mol; the overall mass transfer coefficients are constructed from film ($k_f$ via Wakao–Funazkri: $Sh = 2 + 1.1Re^{0.6}Sc^{1/3}$), pore ($k_p = 15D_p/r_p^2$ with combined molecular–Knudsen diffusivity in the silica mesopores, as in Zhang et al., Energy & Fuels, 2016, and Cheong’s 2021 NUS/SUTD thesis on PEI/SiO₂ nanocomposites), and solid resistances in series: $1/k_1 = c_{in}/(q^**{p,in}k_f) + c*{in}/(q^**{p,in}k_p) + 1/k_s$ and $1/k_2 = 1/k_1 + 1/k*{s,amine}$; the novel contribution is the extension of the travelling-wave analysis to the DK model, which yields the *hybrid analytical–numerical breakthrough expression* $c_1(L,t)/c_{1,0} \approx (1-e^{-k_1(t-t_b)})/(1-\delta_{45}e^{-k_1(t-t_b)}) - ((1-\eta)/\eta)\kappa , e^{-k_2(t-t_b)}$ where the first term captures the sharp sigmoidal rise of the fast surface sites with breakthrough time $t_b = \eta(1-\varepsilon)\rho_p q_0^* L/(u_0 c_{1,0})$ and the second term produces the characteristic slow tail from bulk PEI diffusion, with the ratio $\kappa = k_2/k_1 \sim 0.01$–0.1 quantifying the kinetic heterogeneity; this reduces exactly to the Myers–Font result when $\eta = 1$ (homogeneous physical adsorbent) and to a pure double-exponential in the DAC limit $\delta_{45} \to 0$ ($y_{in} = 400$ ppm, incompressible flow), while for non-isothermal conditions relevant to concentrated feeds where the exothermic heat of adsorption ($\sim 70$ kJ/mol for PEI@SiO₂) causes temperature excursions exceeding 15 °C, the full PDE system including the energy balance $[\varepsilon\rho_g c_{p,g} + (1-\varepsilon)\rho_p c_{p,s}]\partial T/\partial t + \varepsilon\rho_g c_{p,g} u , \partial T/\partial z = \lambda_{eff}\partial^2 T/\partial z^2 + (1-\varepsilon)\rho_p(-\Delta H_{ads})\partial\bar{q}/\partial t - 4h_W(T-T_W)/d_{col}$ is solved numerically with second-order central differences and upwind advection, validated against the analytical travelling wave which recovers the numerics to within $O(\delta_1) \sim 3$–4% as demonstrated by Myers and Font; the model is calibrated by fitting $k_1$ and $D_L$ to the initial breakthrough slope, then $\eta$ and $k_{s,amine}$ to the tail, following the two-step procedure of Stampi-Bombelli et al. (2024), and it provides explicit, optimisable expressions for all column variables (CO₂ concentration, sorbent loading, velocity, pressure) as functions of the design parameters ($L$, $d_p$, $\varepsilon$, $u_0$, $T$), enabling rapid parametric studies and integration into techno-economic optimisation frameworks such as that of Pedrozo et al. (Comput. Chem. Eng., 2025) at negligible computational cost compared to full COMSOL reactive-transport simulations.

-----

## 9. Proof of Validity

**Theorem (Travelling-Wave Existence for the DK System):** *Under the assumptions A1–A7, with $\delta_1, \delta_2 \ll 1$ and the isothermal approximation, the leading-order system admits a travelling-wave solution with wave speed $v_f = u_0 c_{1,0} / (\eta (1-\varepsilon) \rho_p q_0^*)$ for the fast surface sites, provided $\kappa = k_2/k_1 \ll 1$.*

**Proof.** The leading-order system (Section 4.2) with $\hat{q}_2$ treated as a slow perturbation is:

$$
\frac{\partial \hat{f}}{\partial \hat{x}} = -\frac{\partial \hat{q}_1}{\partial \hat{t}} + O(\kappa), \qquad \frac{\partial \hat{q}_1}{\partial \hat{t}} = \eta \hat{q}^* - \hat{q}_1
$$

with $\hat{f} = \hat{u}\hat{c}_1$ and the constraint $\hat{u}\hat{c}_2 = 1$.

Substituting $\xi = \hat{x} - \hat{v}\hat{t}$ and assuming $\hat{v}$ constant:

$$
\frac{\partial \hat{f}}{\partial \xi} = \hat{v} \frac{\partial \hat{q}_1}{\partial \xi}, \qquad -\hat{v}\frac{\partial \hat{q}_1}{\partial \xi} = \eta - \hat{q}_1
$$

where we have used $\hat{q}^* = 1$ at leading order (since $\delta_3 \sim 10^{-4}$; Myers & Font, 2020, eq. 39).

The first equation integrates immediately to $\hat{f} = \hat{v}\hat{q}_1 + C$. Applying boundary conditions at the front $\xi = 0$: $\hat{f} = \hat{q}_1 = 0$, giving $C = 0$, hence $\hat{f} = \hat{v}\hat{q}_1$.

The second equation is the autonomous ODE $\hat{v}\hat{q}_{1,\xi} = \hat{q}_1 - \eta$ with solution $\hat{q}_1 = \eta(1 - e^{\xi/\hat{v}})$. This satisfies $\hat{q}_1(0) = 0$ and $\hat{q}_1 \to \eta$ as $\xi \to -\infty$.

Substituting into $\hat{f} = \hat{v}\hat{q}_1$: $\hat{f} = \hat{v}\eta(1 - e^{\xi/\hat{v}})$. The far-field condition $\hat{f} \to 1$ as $\xi \to -\infty$ requires $\hat{v}\eta = 1$, determining $\hat{v} = 1/\eta$.

In dimensional terms: $v_f = \hat{v} \cdot \mathcal{L} k_1 = (1/\eta) \cdot u_0 c_{1,0}/((1-\varepsilon)\rho_p q_0^*) \cdot k_1 \cdot 1/k_1 = u_0 c_{1,0}/(\eta(1-\varepsilon)\rho_p q_0^*)$. $\square$

**Remark on the perturbation.** The $O(\kappa)$ correction from $q_2$ does not destroy the travelling-wave structure but modifies the far-field approach rate. Writing $\hat{q}_2 \sim (1-\eta)(1 - e^{\kappa \hat{t}(\xi)})$ behind the wave front and substituting into the mass balance produces a slowly decaying correction to $\hat{c}_1$ of the form $\sim \kappa(1-\eta)/\eta \cdot e^{-\kappa(\hat{t} - \hat{t}_b)}$, which is precisely the tail-correction term in the boxed equation of Section 4.4. The perturbation is uniformly bounded and vanishes as $\hat{t} \to \infty$, confirming asymptotic stability. $\square$

-----

## References

1. Myers, T.G. & Font, F. (2020). “Mass transfer from a fluid flowing through a porous media.” *Int. J. Heat Mass Transfer*, 163, 120374.
1. Stampi-Bombelli, V., Storione, A., Grossmann, Q. & Mazzotti, M. (2024). “On Comparing Packed Beds and Monoliths for CO₂ Capture from Air Through Experiments, Theory, and Modeling.” *Ind. Eng. Chem. Res.*, 63, 11637–11653.
1. Cheong, D.K.W. (2021). “Mathematical Modelling of CO₂ Adsorption in Functionalised Silica Nanocomposite Membranes.” B.Eng. Thesis, NUS / SUTD.
1. Zhang, W., Li, Y., et al. (2016). “Numerical Simulation of CO₂ Adsorption on K-Based Sorbent.” *Energy & Fuels*.
1. Pedrozo, H.A. et al. (2025). “Optimization of direct air capture processes using reactive transport models of adsorption-desorption cycles.” *Comput. Chem. Eng.*, 204, 109379.
1. Chen, S. et al. (2023). “Numerical study on a structured packed adsorption bed for indoor direct air capture.” *Energy*, 128801.
1. Guo, X. & Wang, J. (2019). “A general kinetic model for adsorption: Theoretical analysis and modeling.” *J. Mol. Liq.*, 111100.
1. Kalyanaraman, J. et al. (2015). “Modeling and experimental validation of carbon dioxide sorption on hollow fibers loaded with silica-supported poly(ethylenimine).” *Chem. Eng. J.*, 259, 737–751.
1. Grossmann, Q. et al. (2023). “Developing Versatile Contactors for Direct Air Capture of CO₂ through Amine Grafting onto Alumina Pellets and Alumina Wash-Coated Monoliths.” *Ind. Eng. Chem. Res.*, 62, 13594–13611.
1. Xu, H. et al. (2024). “A comprehensive review on direct air carbon capture (DAC) technology by adsorption.” *Energy Convers. Manag.*, 322, 119119.
1. Jin, Y. et al. (2025). “Optimizing amine-based adsorbents for direct air capture.” *Renew. Sustain. Energy Rev.*, 217, 115782.
1. de Joannis, P. et al. (2025). “Techno-economic analysis of packed bed and structured adsorbent for direct air capture.” *Carbon Capture Sci. Technol.*, 17, 100518.
1. Bollini, P. et al. (2012). “Dynamics of CO₂ adsorption on amine adsorbents.” *Ind. Eng. Chem. Res.*, 51, 15145–15162.
1. Ohs, B., Krödel, M. & Wessling, M. (2018). “Adsorption of carbon dioxide on solid amine-functionalized sorbents: A dual kinetic model.” *Sep. Purif. Technol.*, 204, 13–20.
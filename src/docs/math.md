Listed directory brain
Viewed mechanistic-model.md:1-150
Viewed mechanistic-model.md:151-210

# First-Principles Derivation and Validation of the Non-Isothermal Packed-Bed Adsorption Energy Balance

---

## 1. Notation, Conventions, and Modelling Assumptions

### 1.1 Complete Nomenclature and SI Units

To prevent the dimensional and volumetric ambiguities that frequently compromise packed-bed models, all symbols are defined below with their precise physical meaning, primary SI units, and volumetric/mass reference basis.

| Symbol | Definition | SI Units | Reference Basis |
|---|---|---|---|
| $z$ | Axial column coordinate | $\mathrm{m}$ | Column length coordinate |
| $t$ | Time | $\mathrm{s}$ | Temporal coordinate |
| $L$ | Length of packed adsorbent section | $\mathrm{m}$ | Column dimension |
| $d_{\mathrm{col}}$ | Column internal diameter | $\mathrm{m}$ | Column dimension |
| $A$ | Column internal cross-sectional area ($\frac{\pi}{4}d_{\mathrm{col}}^2$) | $\mathrm{m^2}$ | Bed total cross-section |
| $d_p$ | Mean adsorbent particle diameter | $\mathrm{m}$ | Particle dimension |
| $r_p$ | Mean adsorbent particle radius ($d_p/2$) | $\mathrm{m}$ | Particle dimension |
| $\varepsilon$ | Interparticle bed void fraction (external porosity) | — | $\mathrm{m^3_{fluid}\,m^{-3}_{bed}}$ |
| $\varepsilon_p$ | Intraparticle pellet porosity (macropore/mesopore) | — | $\mathrm{m^3_{pore}\,m^{-3}_{particle}}$ |
| $\rho_p$ | Solid particle mass density | $\mathrm{kg\,m^{-3}}$ | $\mathrm{kg_{solid}\,m^{-3}_{particle}}$ |
| $\rho_b$ | Packed-bed bulk density: $\rho_b = (1-\varepsilon)\rho_p$ | $\mathrm{kg\,m^{-3}}$ | $\mathrm{kg_{solid}\,m^{-3}_{bed}}$ |
| $\rho_g$ | Gas mixture mass density | $\mathrm{kg\,m^{-3}}$ | $\mathrm{kg_{gas}\,m^{-3}_{fluid}}$ |
| $u_s$ | Superficial gas velocity ($\dot{V}_{\mathrm{fluid}}/A$) | $\mathrm{m\,s^{-1}}$ | Bed cross-sectional area |
| $u_i$ | Interstitial gas velocity ($u_i = u_s/\varepsilon$) | $\mathrm{m\,s^{-1}}$ | Fluid void cross-section |
| $c(z,t)$ | Gas-phase concentration of adsorbate (e.g., $\mathrm{CO_2}$) | $\mathrm{mol\,m^{-3}}$ | $\mathrm{mol\,m^{-3}_{fluid}}$ |
| $q(z,t)$ | Solid-phase adsorbed loading | $\mathrm{mol\,kg^{-1}}$ | $\mathrm{mol\,kg^{-1}_{solid}}$ |
| $q'(z,t)$ | Solid-phase loading per particle volume ($q' = \rho_p q$) | $\mathrm{mol\,m^{-3}}$ | $\mathrm{mol\,m^{-3}_{particle}}$ |
| $q_e$ | Local thermodynamic equilibrium loading | $\mathrm{mol\,kg^{-1}}$ | $\mathrm{mol\,kg^{-1}_{solid}}$ |
| $q_m$ | Maximum Langmuir saturation loading | $\mathrm{mol\,kg^{-1}}$ | $\mathrm{mol\,kg^{-1}_{solid}}$ |
| $P$ | Total gas absolute pressure | $\mathrm{Pa}$ | Fluid phase |
| $P_i$ | Partial pressure of adsorbate species ($P_i = cRT$) | $\mathrm{Pa}$ | Fluid phase |
| $b(T)$ | Temperature-dependent Langmuir adsorption affinity | $\mathrm{Pa^{-1}}$ | Adsorption equilibrium |
| $b_0$ | Langmuir pre-exponential affinity constant | $\mathrm{Pa^{-1}}$ | Adsorption equilibrium |
| $\Delta H_{\mathrm{ads}}$ | Molar enthalpy of adsorption (signed, exothermic $< 0$) | $\mathrm{J\,mol^{-1}}$ | Phase transformation |
| $\Delta H_0$ | Reference heat parameter in van't Hoff relation ($< 0$) | $\mathrm{J\,mol^{-1}}$ | Phase transformation |
| $q_{\mathrm{st}}$ | Isosteric heat of adsorption ($q_{\mathrm{st}} \equiv -\Delta H_{\mathrm{ads}} > 0$) | $\mathrm{J\,mol^{-1}}$ | Heat released to system |
| $R$ | Universal gas constant ($8.314462618$) | $\mathrm{J\,mol^{-1}\,K^{-1}}$ | Thermodynamic constant |
| $T(z,t)$ | Bed temperature (pseudo-homogeneous model) | $\mathrm{K}$ | Combined bed |
| $T_g(z,t)$ | Gas-phase local temperature (heterogeneous model) | $\mathrm{K}$ | Fluid phase |
| $T_s(z,t)$ | Solid-phase local temperature (heterogeneous model) | $\mathrm{K}$ | Solid matrix |
| $T_{\mathrm{ref}}$ | Reference state temperature for sensible enthalpy | $\mathrm{K}$ | Thermodynamic datum |
| $T_w$ | Column outer jacket or ambient sink temperature | $\mathrm{K}$ | Ambient boundary |
| $T_{\mathrm{in}}$ | Feed gas inlet temperature | $\mathrm{K}$ | Fluid inlet boundary |
| $C_{p,g}$ | Gas-phase isobaric specific heat capacity | $\mathrm{J\,kg^{-1}\,K^{-1}}$ | Fluid mass |
| $C_{p,s}$ | Solid-phase specific heat capacity | $\mathrm{J\,kg^{-1}\,K^{-1}}$ | Solid mass |
| $C_h$ | Composite bed volumetric heat capacity | $\mathrm{J\,m^{-3}\,K^{-1}}$ | $\mathrm{J\,m^{-3}_{bed}\,K^{-1}}$ |
| $D_L$ | Axial mass dispersion coefficient | $\mathrm{m^2\,s^{-1}}$ | Fluid void area |
| $\lambda_{\mathrm{eff}}$ | Effective bed axial thermal conductivity/dispersion | $\mathrm{W\,m^{-1}\,K^{-1}}$ | Bed cross-section |
| $\lambda_{g,\mathrm{eff}}$ | Gas-phase axial thermal dispersion coefficient | $\mathrm{W\,m^{-1}\,K^{-1}}$ | Bed cross-section |
| $\lambda_{s,\mathrm{eff}}$ | Solid-phase axial effective thermal conductivity | $\mathrm{W\,m^{-1}\,K^{-1}}$ | Bed cross-section |
| $k$ | Linear driving force (LDF) mass transfer coefficient | $\mathrm{s^{-1}}$ | Pellet kinetic relaxation |
| $h_{gs}$ | Gas-to-solid interphase heat transfer coefficient | $\mathrm{W\,m^{-2}\,K^{-1}}$ | External pellet surface |
| $a_v$ | Specific particle surface area per unit bed volume | $\mathrm{m^2\,m^{-3}}$ | $\mathrm{m^2_{particle}\,m^{-3}_{bed}}$ |
| $H_{gs}$ | Volumetric interphase heat transfer coefficient ($h_{gs}a_v$) | $\mathrm{W\,m^{-3}\,K^{-1}}$ | Bed volume |
| $U$ | Overall bed-to-ambient wall heat transfer coefficient | $\mathrm{W\,m^{-2}\,K^{-1}}$ | Column wall surface |
| $U_g, U_s$ | Phase-partitioned wall heat transfer coefficients | $\mathrm{W\,m^{-2}\,K^{-1}}$ | Column wall surface |

---

### 1.2 Sign Conventions and Volumetric Relationships

#### Volumetric Conversion
The differential column volume $\Delta V = A\,\Delta z$ consists of fluid void volume $\Delta V_g = \varepsilon \Delta V$ and solid particle volume $\Delta V_s = (1-\varepsilon)\Delta V$. The solid mass within $\Delta V$ is:
$$\Delta m_s = \rho_p \Delta V_s = \rho_p (1-\varepsilon)\Delta V = \rho_b \Delta V \tag{1.1}$$
which establishes the exact identity:
$$\rho_b \equiv (1-\varepsilon)\rho_p \tag{1.2}$$

#### Adsorption Enthalpy and Isosteric Heat
Adsorption is an intrinsically exothermic process ($\Delta H_{\mathrm{ads}} < 0$). We define the isosteric heat of adsorption, $q_{\mathrm{st}}$, as the positive heat released per mole adsorbed:
$$q_{\mathrm{st}} \equiv -\Delta H_{\mathrm{ads}} = -\Delta H_0 > 0 \tag{1.3}$$
With this convention, during adsorption ($\partial q/\partial t > 0$), heat is released into the system at a volumetric rate:
$$\dot{Q}_{\mathrm{ads}}''' = \rho_b q_{\mathrm{st}} \frac{\partial q}{\partial t} = (1-\varepsilon)\rho_p (-\Delta H_0)\frac{\partial q}{\partial t} > 0 \quad [\mathrm{W\,m^{-3}_{bed}}] \tag{1.4}$$

#### Wall Heat Exchange
Defining $\dot{Q}_{\mathrm{wall,loss}}'''$ as the positive rate of heat loss from the bed to the surroundings per unit bed volume:
$$\dot{Q}_{\mathrm{wall,loss}}''' = \frac{4U}{d_{\mathrm{col}}}(T - T_w) \quad [\mathrm{W\,m^{-3}_{bed}}] \tag{1.5}$$
When $T > T_w$, heat leaves the control volume; therefore, this term enters the energy accumulation balance with a negative sign ($-\dot{Q}_{\mathrm{wall,loss}}'''$).

#### Pressure and Isotherm Compatibility
The dimensionless Langmuir group requires $b(T)P$ to be strictly dimensionless. With $b(T)$ specified in $\mathrm{Pa^{-1}}$, the partial pressure of the adsorbate is calculated via the ideal gas law:
$$P = c R T \quad [\mathrm{Pa}] \tag{1.6}$$
where $c$ is in $\mathrm{mol\,m^{-3}_{fluid}}$, $R = 8.314462618\ \mathrm{J\,mol^{-1}\,K^{-1}}$, and $T$ is in $\mathrm{K}$. Thus:
$$[b(T)P] = (\mathrm{Pa^{-1}})(\mathrm{Pa}) = [-] \tag{1.7}$$

---

### 1.3 Physical and Mathematical Assumptions

To ensure mathematical rigor, each simplification is explicitly classified:

* **Assumption 1 (1-D Axisymmetric Flow):** Radial gradients of velocity, concentration, and temperature are negligible compared to axial gradients ($L/d_{\mathrm{col}} \gg 1$). Radial wall resistance is lumped into the overall wall heat transfer coefficient $U$.
* **Assumption 2 (Isobaric, Dilute Fluid Transport):** The pressure drop across the packed bed is small relative to absolute column pressure ($\Delta P \ll P$), and the adsorbate mole fraction is dilute ($y \ll 1$), ensuring that the superficial velocity $u_s$ and gas density $\rho_g$ remain spatially and temporally uniform to leading order ($\partial u_s/\partial z \approx 0$).
* **Assumption 3 (LDF Intraparticle Kinetics):** Mass transfer from the macropores into the solid micro-adsorbent network is represented by Glueckauf’s linear driving force (LDF) model with a constant effective rate parameter $k$ ($\mathrm{s^{-1}}$).
* **Assumption 4 (Ideal Gas Behaviour):** The gas phase obeys the ideal gas equation of state $P = c_{\mathrm{total}}RT$.
* **Assumption 5 (Fickian Axial Thermal Dispersion):** Microscopic molecular conduction and macroscopic fluid eddy/tortuosity mixing are modeled collectively via Fourier-Fickian axial dispersion with an effective conductivity $\lambda_{\mathrm{eff}}$.
* **Assumption 6 (Negligible Adsorbed-Phase Heat Capacity):** The sensible heat capacity of the adsorbed phase is negligible relative to the adsorbent matrix: $q C_{p,a} \ll C_{p,s}$. For representative systems ($q \approx 1\ \mathrm{mol\,kg^{-1}}$, $C_{p,a} \approx 40\ \mathrm{J\,mol^{-1}\,K^{-1}}$, $C_{p,s} \approx 1000\ \mathrm{J\,kg^{-1}\,K^{-1}}$), the adsorbed phase contributes $< 4\%$ of the solid storage capacity.
* **Assumption 7 (Constant Thermophysical Properties):** Properties $\varepsilon, \rho_p, \rho_g, C_{p,g}, C_{p,s}, \lambda_{\mathrm{eff}}, D_L$ are treated as invariant over the local temperature rise $\Delta T$.
* **Assumption 8 (Thermodynamic Consistency):** The thermal heat release parameter $q_{\mathrm{st}}$ equals the isosteric heat derived from the temperature dependence of the equilibrium adsorption isotherm.

---

## 2. Differential Control-Volume Geometry

Consider a cylindrical packed-bed column of internal diameter $d_{\mathrm{col}}$, cross-sectional area $A = \frac{\pi}{4}d_{\mathrm{col}}^2$, and total length $L$. The fixed coordinate axis $z$ aligns with the axial flow direction, spanning $z \in [0, L]$.

```
                      Column Wall (at Tw)
       =================================================
       |                  |           |                |
  Flow |   Gas Phase      |   CV      |                |
 =====>|   (eps, rho_g)   | [z, z+dz] |  Convection    |=====>
       |                  |           |  Dispersion    |
  us   |   Solid Phase    | Bed Vol:  |                |
       |  (1-eps, rho_p)  |   A * dz  |  Wall Loss     |
       |                  |           |   (4U/d_col)   |
       =================================================
       0                  z          z+dz              L
```

We establish a differential control volume (CV) defined by the spatial interval $[z, z+\Delta z]$ spanning the entire column cross-section $A$.

### Geometric Invariants
* **Total Bed Volume of CV:**
  $$\Delta V = A\,\Delta z \quad [\mathrm{m^3_{bed}}] \tag{2.1}$$
* **Fluid (Void) Volume in CV:**
  $$\Delta V_g = \varepsilon \Delta V = \varepsilon A \Delta z \quad [\mathrm{m^3_{fluid}}] \tag{2.2}$$
* **Solid Particle Volume in CV:**
  $$\Delta V_s = (1-\varepsilon)\Delta V = (1-\varepsilon)A \Delta z \quad [\mathrm{m^3_{solid}}] \tag{2.3}$$
* **Mass of Adsorbent in CV:**
  $$\Delta m_s = \rho_p \Delta V_s = (1-\varepsilon)\rho_p A \Delta z = \rho_b A \Delta z \quad [\mathrm{kg_{solid}}] \tag{2.4}$$
* **Lateral Column Wall Area enclosing CV:**
  $$\Delta A_{\mathrm{wall}} = \pi d_{\mathrm{col}} \Delta z \quad [\mathrm{m^2}] \tag{2.5}$$

### Wall-Area-to-Bed-Volume Ratio
Dividing the lateral exchange surface by the differential bed volume yields:
$$\frac{\Delta A_{\mathrm{wall}}}{\Delta V} = \frac{\pi d_{\mathrm{col}} \Delta z}{\frac{\pi}{4}d_{\mathrm{col}}^2 \Delta z} = \frac{4}{d_{\mathrm{col}}} \quad [\mathrm{m^2\,m^{-3}_{bed} = m^{-1}}] \tag{2.6}$$
Equation (2.6) proves from first principles the geometric origin of the factor $4/d_{\mathrm{col}}$ that couples boundary wall flux to volumetric bed equations.

---

## 3. First-Principles Energy Balance

### 3.1 Thermodynamic Formulation of the Conservation Law

The First Law of Thermodynamics for an open, non-steady differential control volume states:
$$\frac{d E_{\mathrm{CV}}}{dt} = \dot{Q}_{\mathrm{net}} - \dot{W}_{\mathrm{net}} + \sum_{\mathrm{in}} \dot{m}_k \hat{h}_k - \sum_{\mathrm{out}} \dot{m}_k \hat{h}_k \tag{3.1}$$

In a packed-bed adsorption column:
1. **Shaft Work:** No moving boundaries or shafts exist; hence $\dot{W}_s = 0$.
2. **Flow Work ($P v$):** The rate of flow work done on fluid entering and leaving the control volume is rigorously absorbed into the convective enthalpy flux:
   $$\hat{h} = \hat{u} + P\hat{v} = \hat{u} + \frac{P}{\rho_g} \tag{3.2}$$
3. **Kinetic and Gravitational Energy:** Changes in fluid kinetic energy ($\frac{1}{2}u_i^2$) and potential energy ($g\Delta z$) across $\Delta z$ are negligible relative to thermal enthalpy changes ($C_{p,g}\Delta T$):
   $$\frac{\frac{1}{2}\Delta(u_i^2)}{C_{p,g}\Delta T} \sim \frac{10^{-2}\ \mathrm{J\,kg^{-1}}}{10^3\ \mathrm{J\,kg^{-1}}} \sim 10^{-5} \ll 1 \tag{3.3}$$
4. **Energy Accumulation:** The total internal energy stored in the control volume is the sum of the internal energies of the fluid and solid phases:
   $$E_{\mathrm{CV}} = U_g + U_s \tag{3.4}$$

The comprehensive verbal conservation statement over $\Delta t$ and $\Delta z$ is:
$$\boxed{
\left[\begin{array}{c}
\text{Rate of Energy} \\
\text{Accumulation} \\
\text{in the CV}
\end{array}\right]
=
\left[\begin{array}{c}
\text{Net Enthalpy} \\
\text{Convected In} \\
\text{across } z
\end{array}\right]
-
\left[\begin{array}{c}
\text{Net Enthalpy} \\
\text{Convected Out} \\
\text{across } z+\Delta z
\end{array}\right]
+
\left[\begin{array}{c}
\text{Net Axial Conduction} \\
\text{and Dispersion In} \\
\text{across Boundaries}
\end{array}\right]
+
\left[\begin{array}{c}
\text{Rate of Heat} \\
\text{Generated by} \\
\text{Adsorption}
\end{array}\right]
-
\left[\begin{array}{c}
\text{Rate of Heat} \\
\text{Lost Through} \\
\text{Column Wall}
\end{array}\right]
} \tag{3.5}$$

### 3.2 Definition of Sensible Enthalpy and Reference States

For any phase $\alpha$, specific enthalpy is defined relative to an arbitrary reference temperature $T_{\mathrm{ref}}$:
$$\hat{h}_\alpha(T) = \hat{h}_\alpha(T_{\mathrm{ref}}) + \int_{T_{\mathrm{ref}}}^T C_{p,\alpha}(T')\,dT' \tag{3.6}$$
Assuming constant isobaric heat capacity $C_{p,\alpha}$ over the operating range:
$$\hat{h}_\alpha(T) = \hat{h}_{\alpha,\mathrm{ref}} + C_{p,\alpha}(T - T_{\mathrm{ref}}) \tag{3.7}$$
For liquids and solid packings, $d\hat{h}_s \approx d\hat{u}_s = C_{p,s}dT$ because the specific volume $\hat{v}_s$ is small ($P\hat{v}_s \approx 0$). For an ideal gas at uniform pressure, $d\hat{u}_g = C_{v,g}dT$ and $d\hat{h}_g = C_{p,g}dT$.

#### Elimination of the Reference Temperature $T_{\mathrm{ref}}$
Upon substituting Equation (3.7) into the accumulation and transport terms:
$$\frac{\partial}{\partial t}\left[\rho_\alpha C_{p,\alpha}(T - T_{\mathrm{ref}})\right] = \rho_\alpha C_{p,\alpha}\frac{\partial T}{\partial t} - \rho_\alpha C_{p,\alpha}\frac{\partial T_{\mathrm{ref}}}{\partial t} = \rho_\alpha C_{p,\alpha}\frac{\partial T}{\partial t} \tag{3.8}$$
since $T_{\mathrm{ref}}$ is a constant. Similarly, for convective spatial divergence:
$$\frac{\partial}{\partial z}\left[\rho_g C_{p,g} u_s (T - T_{\mathrm{ref}})\right] = \rho_g C_{p,g} u_s \frac{\partial T}{\partial z} - \rho_g C_{p,g} u_s \frac{\partial T_{\mathrm{ref}}}{\partial z} = \rho_g C_{p,g} u_s \frac{\partial T}{\partial z} \tag{3.9}$$
Because total mass is conserved across the non-reacting carrier stream ($\nabla \cdot (\rho_g \mathbf{u}) = 0$), the arbitrary reference datum $\hat{h}_{\mathrm{ref}}$ cancels out of the balance equation.

---

## 4. Derivation of Each Individual Flux and Source Term

### 4.1 Gas Sensible-Energy Accumulation

The mass of gas within the differential volume $\Delta V$ is:
$$\Delta m_g = \rho_g \Delta V_g = \rho_g (\varepsilon A \Delta z) \tag{4.1}$$
The stored sensible energy relative to $T_{\mathrm{ref}}$ is:
$$U_g = \Delta m_g C_{v,g}(T_g - T_{\mathrm{ref}}) = \varepsilon \rho_g C_{v,g} (T_g - T_{\mathrm{ref}}) A \Delta z \tag{4.2}$$
In an open, constant-pressure flowing system, local expansion work between fluid parcels accounts for the difference between $C_v$ and $C_p$ such that the accumulation of flowing enthalpy per unit bed volume is:
$$\dot{E}_{\mathrm{acc},g} = \frac{\partial}{\partial t}\left[\varepsilon \rho_g C_{p,g}(T_g - T_{\mathrm{ref}})\right] A \Delta z \tag{4.3}$$
With constant $\varepsilon, \rho_g$, and $C_{p,g}$:
$$\boxed{
\dot{E}_{\mathrm{acc},g} = \varepsilon \rho_g C_{p,g} \frac{\partial T_g}{\partial t} A \Delta z \quad [\mathrm{W}]
} \tag{4.4}$$
*Physical role of $\varepsilon$:* The void fraction $\varepsilon$ appears because the fluid occupies only the fraction $\varepsilon$ of the control volume. The gas density $\rho_g$ is expressed per unit fluid volume ($\mathrm{kg_{gas}\,m^{-3}_{fluid}}$); multiplying by $\varepsilon$ converts the gas thermal capacity to a total bed volume basis ($\mathrm{J\,m^{-3}_{bed}\,K^{-1}}$).

---

### 4.2 Solid Sensible-Energy Accumulation

The mass of stationary solid adsorbent inside $\Delta V$ is:
$$\Delta m_s = \rho_p \Delta V_s = \rho_p (1-\varepsilon) A \Delta z = \rho_b A \Delta z \tag{4.5}$$
The sensible thermal energy stored in this stationary mass is:
$$U_s = \Delta m_s C_{p,s}(T_s - T_{\mathrm{ref}}) = (1-\varepsilon)\rho_p C_{p,s}(T_s - T_{\mathrm{ref}}) A \Delta z \tag{4.6}$$
Differentiating with respect to time (holding $\varepsilon, \rho_p, C_{p,s}$ constant):
$$\boxed{
\dot{E}_{\mathrm{acc},s} = (1-\varepsilon)\rho_p C_{p,s} \frac{\partial T_s}{\partial t} A \Delta z = \rho_b C_{p,s} \frac{\partial T_s}{\partial t} A \Delta z \quad [\mathrm{W}]
} \tag{4.7}$$
*Distinction between particle and bulk density:* Particle density $\rho_p$ is solid mass divided by solid skeleton plus internal pore volume. Bulk density $\rho_b = (1-\varepsilon)\rho_p$ is solid mass divided by total column volume. Writing $(1-\varepsilon)\rho_p$ explicitly accounts for the volume exclusion of the bed void fraction $\varepsilon$.

---

### 4.3 Gas Convection

Gas flows through the interstitial void spaces with interstitial velocity $u_i$. The open cross-sectional area available for flow is:
$$A_{\mathrm{flow}} = \varepsilon A \tag{4.8}$$
The mass flow rate of gas through this cross-section is:
$$\dot{m}_g = \rho_g u_i A_{\mathrm{flow}} = \rho_g \left(\frac{u_s}{\varepsilon}\right) (\varepsilon A) = \rho_g u_s A \quad [\mathrm{kg\,s^{-1}}] \tag{4.9}$$
Notice that $\varepsilon$ cancels identically: the superficial velocity $u_s$ is defined specifically such that $\dot{V} = u_s A$.

The convective rate of enthalpy entering the face at $z$ is:
$$\dot{H}_{\mathrm{conv}}(z) = \dot{m}_g \hat{h}_g(z) = \rho_g u_s A C_{p,g}(T(z,t) - T_{\mathrm{ref}}) \tag{4.10}$$
The convective rate of enthalpy leaving the face at $z+\Delta z$ is:
$$\dot{H}_{\mathrm{conv}}(z+\Delta z) = \rho_g u_s A C_{p,g}(T(z+\Delta z,t) - T_{\mathrm{ref}}) \tag{4.11}$$
The net convective energy added to the control volume is:
$$\dot{H}_{\mathrm{conv}}(z) - \dot{H}_{\mathrm{conv}}(z+\Delta z) = -\rho_g u_s A C_{p,g} [T(z+\Delta z,t) - T(z,t)] \tag{4.12}$$
Dividing by the control volume $\Delta V = A\Delta z$ and taking the limit $\Delta z \to 0$:
$$\lim_{\Delta z \to 0} \frac{\dot{H}_{\mathrm{conv}}(z) - \dot{H}_{\mathrm{conv}}(z+\Delta z)}{A\Delta z} = -\rho_g C_{p,g} u_s \lim_{\Delta z \to 0}\frac{T(z+\Delta z,t) - T(z,t)}{\Delta z} = -\rho_g C_{p,g} u_s \frac{\partial T}{\partial z} \tag{4.13}$$
Thus, the net convective transport term per unit bed volume is:
$$\boxed{
-\rho_g C_{p,g} u_s \frac{\partial T}{\partial z} \quad [\mathrm{W\,m^{-3}_{bed}}]
} \tag{4.14}$$
*Comparison with the species mass balance:* In the supplied species balance:
$$\frac{\partial c}{\partial t} = -\frac{u_s}{\varepsilon}\frac{\partial c}{\partial z} + \dots$$
the concentration $c$ is defined per unit fluid volume, so the accumulation term is $\varepsilon \frac{\partial c}{\partial t}$ per unit bed volume. Dividing by $\varepsilon$ isolates $\frac{\partial c}{\partial t}$ on the LHS and creates the interstitial convection coefficient $u_s/\varepsilon = u_i$. In the energy balance, the presence of solid heat capacity prevents the same cancellation.

---

### 4.4 Axial Heat Conduction and Thermal Dispersion

Axial heat transport occurs via two physical mechanisms:
1. True molecular conduction through the contiguous solid matrix and interstitial gas pathways.
2. Hydrodynamic thermal dispersion caused by velocity shear across interstitial channels and turbulent/tortuous eddy splitting.

In packed beds, these mechanisms are coupled and described by an effective Fourier law:
$$q''_{\mathrm{axial}} = -\lambda_{\mathrm{eff}} \frac{\partial T}{\partial z} \quad [\mathrm{W\,m^{-2}_{bed}}] \tag{4.15}$$
where $\lambda_{\mathrm{eff}}$ is the effective axial thermal conductivity based on the total bed cross-sectional area $A$.

The rate of conductive/dispersive heat entering at $z$ is:
$$\dot{Q}_{\mathrm{cond}}(z) = A q''_{\mathrm{axial}}(z) = -\left. A \lambda_{\mathrm{eff}}\frac{\partial T}{\partial z}\right|_{z} \tag{4.16}$$
The conductive/dispersive heat leaving at $z+\Delta z$ is:
$$\dot{Q}_{\mathrm{cond}}(z+\Delta z) = -\left. A \lambda_{\mathrm{eff}}\frac{\partial T}{\partial z}\right|_{z+\Delta z} \tag{4.17}$$
The net rate of heat gained by the control volume is:
$$\dot{Q}_{\mathrm{cond}}(z) - \dot{Q}_{\mathrm{cond}}(z+\Delta z) = A \left[ \left.\lambda_{\mathrm{eff}}\frac{\partial T}{\partial z}\right|_{z+\Delta z} - \left.\lambda_{\mathrm{eff}}\frac{\partial T}{\partial z}\right|_{z} \right] \tag{4.18}$$
Dividing by $\Delta V = A\Delta z$ and evaluating the limit as $\Delta z \to 0$:
$$\lim_{\Delta z \to 0} \frac{\dot{Q}_{\mathrm{cond}}(z) - \dot{Q}_{\mathrm{cond}}(z+\Delta z)}{A\Delta z} = \frac{\partial}{\partial z}\left(\lambda_{\mathrm{eff}}\frac{\partial T}{\partial z}\right) \tag{4.19}$$
For uniform $\lambda_{\mathrm{eff}}$:
$$\boxed{
\lambda_{\mathrm{eff}} \frac{\partial^2 T}{\partial z^2} \quad [\mathrm{W\,m^{-3}_{bed}}]
} \tag{4.20}$$

#### Physical Distinction Between $D_L$ and $\lambda_{\mathrm{eff}}$
* $D_L$ ($\mathrm{m^2\,s^{-1}}$) represents **mass dispersion**, occurring exclusively in the fluid void fraction $\varepsilon$. Sorbate cannot diffuse through the impermeable crystalline solid skeleton.
* $\lambda_{\mathrm{eff}}$ ($\mathrm{W\,m^{-1}\,K^{-1}}$) represents **composite thermal transport**, which proceeds through both the fluid void space and the stationary solid particles in parallel and series. Because solid thermal conductivities ($\lambda_s \sim 0.1\text{–}1.5\ \mathrm{W\,m^{-1}\,K^{-1}}$) often exceed gas conductivities ($\lambda_g \sim 0.026\ \mathrm{W\,m^{-1}\,K^{-1}}$) by an order of magnitude, the solid matrix provides a major conduction pathway.
* Thermal diffusivity $\alpha_{\mathrm{eff}} = \lambda_{\mathrm{eff}}/C_h$ does not equal $D_L$; the Lewis number $Le = \alpha_{\mathrm{eff}}/D_L \ne 1$.

---

### 4.5 Heat Released by Adsorption

Adsorption involves the transfer of gas molecules into an adsorbed phase, releasing their latent heat of adsorption.
* Mass of adsorbent in the CV: $\Delta m_s = \rho_b A \Delta z = (1-\varepsilon)\rho_p A \Delta z$ [$\mathrm{kg_{solid}}$].
* Adsorbate uptake rate: $\frac{\partial q}{\partial t}$ [$\mathrm{mol\,kg^{-1}_{solid}\,s^{-1}}$].
* Molar rate of adsorption in the CV:
  $$\dot{n}_{\mathrm{ads}} = \Delta m_s \frac{\partial q}{\partial t} = \rho_b \frac{\partial q}{\partial t} A \Delta z \quad [\mathrm{mol\,s^{-1}}] \tag{4.21}$$
* Heat released per mole adsorbed: $q_{\mathrm{st}} \equiv -\Delta H_{\mathrm{ads}} > 0$ [$\mathrm{J\,mol^{-1}}$].

Multiplying the molar rate of adsorption by the isosteric heat yields the total rate of thermal energy generation:
$$\dot{Q}_{\mathrm{ads}} = \dot{n}_{\mathrm{ads}} q_{\mathrm{st}} = \rho_b q_{\mathrm{st}} \frac{\partial q}{\partial t} A \Delta z = (1-\varepsilon)\rho_p q_{\mathrm{st}} \frac{\partial q}{\partial t} A \Delta z \quad [\mathrm{W}] \tag{4.22}$$
Dividing by $\Delta V = A\Delta z$ gives the volumetric source term:
$$\boxed{
\dot{Q}_{\mathrm{ads}}''' = \rho_b q_{\mathrm{st}} \frac{\partial q}{\partial t} = (1-\varepsilon)\rho_p (-\Delta H_0) \frac{\partial q}{\partial t} \quad [\mathrm{W\,m^{-3}_{bed}}]
} \tag{4.23}$$

#### Dimensional Verification of the Source Term
$$[\dot{Q}_{\mathrm{ads}}'''] = [\rho_b] [q_{\mathrm{st}}] \left[\frac{\partial q}{\partial t}\right] = \left(\frac{\mathrm{kg}}{\mathrm{m^3}}\right) \left(\frac{\mathrm{J}}{\mathrm{mol}}\right) \left(\frac{\mathrm{mol}}{\mathrm{kg\,s}}\right) = \frac{\mathrm{J}}{\mathrm{m^3\,s}} = \mathrm{W\,m^{-3}_{bed}} \tag{4.24}$$

#### Physical Meaning of the Rate Dependence
The heat release is strictly proportional to the **rate of uptake** $\partial q/\partial t$, not to the absolute or equilibrium loading $q_e$. A bed saturated at high loading $q = q_e$ produces zero heat ($\partial q/\partial t = 0$). Heat generation requires phase change:
* $\frac{\partial q}{\partial t} > 0 \implies \dot{Q}_{\mathrm{ads}}''' > 0$ (exothermic adsorption releases heat).
* $\frac{\partial q}{\partial t} < 0 \implies \dot{Q}_{\mathrm{ads}}''' < 0$ (endothermic desorption absorbs heat).

---

### 4.6 Heat Exchange with the Column Wall

Heat exchange between the outer column perimeter and the surrounding jacket or ambient environment at temperature $T_w$ is governed by Newton's law of cooling.
* Lateral exchange surface area of the CV: $\Delta A_{\mathrm{wall}} = \pi d_{\mathrm{col}} \Delta z$.
* Total heat loss rate through this lateral boundary:
  $$\dot{Q}_{\mathrm{wall,loss}} = U \Delta A_{\mathrm{wall}} (T - T_w) = U (\pi d_{\mathrm{col}} \Delta z)(T - T_w) \quad [\mathrm{W}] \tag{4.25}$$
  where $U$ is the overall heat transfer coefficient ($\mathrm{W\,m^{-2}\,K^{-1}}$) accounting for internal bed radial resistance, column wall conduction, and external convective cooling.

Dividing by the differential bed volume $\Delta V = \frac{\pi}{4}d_{\mathrm{col}}^2 \Delta z$:
$$\dot{Q}_{\mathrm{wall,loss}}''' = \frac{\dot{Q}_{\mathrm{wall,loss}}}{\Delta V} = \frac{U \pi d_{\mathrm{col}} \Delta z (T - T_w)}{\frac{\pi}{4}d_{\mathrm{col}}^2 \Delta z} = \frac{4U}{d_{\mathrm{col}}}(T - T_w) \quad [\mathrm{W\,m^{-3}_{bed}}] \tag{4.26}$$
Because $\dot{Q}_{\mathrm{wall,loss}}'''$ represents energy leaving the control volume, it appears as a sink in the energy balance:
$$\boxed{
-\dot{Q}_{\mathrm{wall,loss}}''' = -\frac{4U}{d_{\mathrm{col}}}(T - T_w) \quad [\mathrm{W\,m^{-3}_{bed}}]
} \tag{4.27}$$
A constant $U$ is valid when the radial temperature profile is approximately parabolic and boundary boundary-layer conditions are steady.

---

## 5. Formulation I: Pseudo-Homogeneous, Single-Temperature Model

### 5.1 Local Thermal Equilibrium and Composite Heat Capacity

Under the pseudo-homogeneous assumption (local thermal equilibrium), the gas and solid phases at any axial position $z$ and time $t$ share the same temperature:
$$\boxed{T_g(z,t) = T_s(z,t) \equiv T(z,t)} \tag{5.1}$$

Summing the gas accumulation term (Equation 4.4) and the solid accumulation term (Equation 4.7):
$$\dot{E}_{\mathrm{acc}} = \dot{E}_{\mathrm{acc},g} + \dot{E}_{\mathrm{acc},s} = \left[ \varepsilon \rho_g C_{p,g}\frac{\partial T}{\partial t} + (1-\varepsilon)\rho_p C_{p,s}\frac{\partial T}{\partial t} \right] A\Delta z \tag{5.2}$$
Factoring out the common temperature derivative $\frac{\partial T}{\partial t}$:
$$\dot{E}_{\mathrm{acc}} = \left[ \varepsilon \rho_g C_{p,g} + (1-\varepsilon)\rho_p C_{p,s} \right] \frac{\partial T}{\partial t} A\Delta z = C_h \frac{\partial T}{\partial t} A\Delta z \tag{5.3}$$

We define the **composite volumetric heat capacity of the packed bed**, $C_h$:
$$\boxed{
C_h \equiv \varepsilon \rho_g C_{p,g} + (1-\varepsilon)\rho_p C_{p,s} = \varepsilon \rho_g C_{p,g} + \rho_b C_{p,s}
} \tag{5.4}$$

#### Dimensional Verification of $C_h$
$$[C_h] = [-]\left(\frac{\mathrm{kg}}{\mathrm{m^3}}\right)\left(\frac{\mathrm{J}}{\mathrm{kg\,K}}\right) + [-]\left(\frac{\mathrm{kg}}{\mathrm{m^3}}\right)\left(\frac{\mathrm{J}}{\mathrm{kg\,K}}\right) = \frac{\mathrm{J}}{\mathrm{m^3_{bed}}\,K} \tag{5.5}$$

Because solid density ($\rho_p \sim 1000\ \mathrm{kg\,m^{-3}}$) is approximately three orders of magnitude greater than gas density ($\rho_g \sim 1.2\ \mathrm{kg\,m^{-3}}$), the solid phase accounts for $> 99.5\%$ of the total volumetric heat capacity:
$$(1-\varepsilon)\rho_p C_{p,s} \gg \varepsilon \rho_g C_{p,g} \implies C_h \approx (1-\varepsilon)\rho_p C_{p,s} = \rho_b C_{p,s} \tag{5.6}$$

---

### 5.2 Assembly of the Canonical Bed-Volume PDE

We assemble the complete energy balance over the control volume $[z, z+\Delta z]$ by equating accumulation to the sum of net fluxes and sources:
$$\dot{E}_{\mathrm{acc}} = \left[\dot{H}_{\mathrm{conv}}(z) - \dot{H}_{\mathrm{conv}}(z+\Delta z)\right] + \left[\dot{Q}_{\mathrm{cond}}(z) - \dot{Q}_{\mathrm{cond}}(z+\Delta z)\right] + \dot{Q}_{\mathrm{ads}} - \dot{Q}_{\mathrm{wall,loss}} \tag{5.7}$$

Substituting the expressions derived in Section 4:
$$C_h \frac{\partial T}{\partial t} A\Delta z = -\rho_g C_{p,g} u_s \frac{\partial T}{\partial z} A\Delta z + \lambda_{\mathrm{eff}} \frac{\partial^2 T}{\partial z^2} A\Delta z + \rho_b q_{\mathrm{st}}\frac{\partial q}{\partial t} A\Delta z - \frac{4U}{d_{\mathrm{col}}}(T - T_w) A\Delta z \tag{5.8}$$

Dividing by the differential bed volume $\Delta V = A\Delta z$ yields the **canonical pseudo-homogeneous energy PDE**:
$$\boxed{
C_h \frac{\partial T}{\partial t} + \rho_g C_{p,g} u_s \frac{\partial T}{\partial z} = \lambda_{\mathrm{eff}} \frac{\partial^2 T}{\partial z^2} + \rho_b q_{\mathrm{st}} \frac{\partial q}{\partial t} - \frac{4U}{d_{\mathrm{col}}}(T - T_w)
} \tag{5.9}$$

Every term in Equation (5.9) has units of **$\mathrm{W\,m^{-3}_{bed}}$**.

---

### 5.3 Complete Coupled System with LDF Kinetics and Non-Isothermal Langmuir Isotherm

Substituting the linear driving force model for $\partial q/\partial t$:
$$\frac{\partial q}{\partial t} = k(q_e - q) \tag{5.10}$$
the adsorption heat generation term becomes:
$$\dot{Q}_{\mathrm{ads}}''' = \rho_b q_{\mathrm{st}} k (q_e - q) \tag{5.11}$$

The local equilibrium loading $q_e$ is given by the temperature-dependent Langmuir isotherm:
$$q_e(c, T) = \frac{q_m b(T) P}{1 + b(T) P} = \frac{q_m b(T) c R T}{1 + b(T) c R T} \tag{5.12}$$
with the van't Hoff affinity:
$$b(T) = b_0 \exp\left(-\frac{\Delta H_0}{R T}\right) \tag{5.13}$$

The complete, coupled nonlinear 1-D adsorption PDE system is:

$$\begin{aligned}
\text{[Gas Mass]} \quad & \frac{\partial c}{\partial t} = -\frac{u_s}{\varepsilon}\frac{\partial c}{\partial z} + D_L\frac{\partial^2 c}{\partial z^2} - \frac{\rho_b}{\varepsilon} k \left[ q_e(c,T) - q \right] \\
\text{[Solid Mass]} \quad & \frac{\partial q}{\partial t} = k \left[ q_e(c,T) - q \right] \\
\text{[Bed Energy]} \quad & C_h \frac{\partial T}{\partial t} = -\rho_g C_{p,g} u_s \frac{\partial T}{\partial z} + \lambda_{\mathrm{eff}} \frac{\partial^2 T}{\partial z^2} + \rho_b q_{\mathrm{st}} k \left[ q_e(c,T) - q \right] - \frac{4U}{d_{\mathrm{col}}}(T - T_w)
\end{aligned} \tag{5.14}$$

#### Thermal Feedback Mechanism
The coupling introduces strong nonlinear feedback:
$$\text{Adsorption occurs} \left(\frac{\partial q}{\partial t} > 0\right) \implies \text{Heat released} \implies T \uparrow \implies b(T) \downarrow \implies q_e(c,T) \downarrow \implies (q_e - q) \downarrow \implies \frac{\partial q}{\partial t} \downarrow$$
Because adsorption is exothermic ($\Delta H_0 < 0$), an increase in bed temperature exponentially suppresses the equilibrium adsorption capacity $q_e$. This thermodynamic throttling reduces the local driving force, causing premature breakthrough and broadening the mass transfer zone (roll-up effect).

---

### 5.4 Fluid-Volume-Normalised Energy Balance

To compare the energy equation directly with the species mass balance (which is normalised per unit fluid volume), we divide Equation (5.9) by the fluid volumetric heat capacity $\varepsilon \rho_g C_{p,g}$:
$$\boxed{
\left(\frac{C_h}{\varepsilon \rho_g C_{p,g}}\right)\frac{\partial T}{\partial t} + \frac{u_s}{\varepsilon}\frac{\partial T}{\partial z} = \left(\frac{\lambda_{\mathrm{eff}}}{\varepsilon \rho_g C_{p,g}}\right)\frac{\partial^2 T}{\partial z^2} + \left(\frac{\rho_b q_{\mathrm{st}}}{\varepsilon \rho_g C_{p,g}}\right)\frac{\partial q}{\partial t} - \left(\frac{4U}{d_{\mathrm{col}}\varepsilon \rho_g C_{p,g}}\right)(T - T_w)
} \tag{5.15}$$

#### The Thermal Retardation Factor $R_{\mathrm{th}}$
The coefficient multiplying $\frac{\partial T}{\partial t}$ is the **thermal retardation factor**, $R_{\mathrm{th}}$:
$$R_{\mathrm{th}} \equiv \frac{C_h}{\varepsilon \rho_g C_{p,g}} = \frac{\varepsilon \rho_g C_{p,g} + (1-\varepsilon)\rho_p C_{p,s}}{\varepsilon \rho_g C_{p,g}} = 1 + \left(\frac{1-\varepsilon}{\varepsilon}\right)\frac{\rho_p C_{p,s}}{\rho_g C_{p,g}} \tag{5.16}$$

Evaluating $R_{\mathrm{th}}$ for typical packed-bed conditions ($\varepsilon = 0.4$, $\rho_p = 1100\ \mathrm{kg\,m^{-3}}$, $C_{p,s} = 1000\ \mathrm{J\,kg^{-1}\,K^{-1}}$, $\rho_g = 1.2\ \mathrm{kg\,m^{-3}}$, $C_{p,g} = 1000\ \mathrm{J\,kg^{-1}\,K^{-1}}$):
$$R_{\mathrm{th}} = 1 + \left(\frac{0.6}{0.4}\right)\frac{1100 \times 1000}{1.2 \times 1000} = 1 + 1.5 \times 916.7 \approx 1376 \tag{5.17}$$

*Why the thermal accumulation coefficient does NOT equal one:* Dividing by the fluid capacity makes the convective coefficient equal to the interstitial velocity $u_i = u_s/\varepsilon$, matching the species convection term. However, the accumulation coefficient becomes $R_{\mathrm{th}} \approx 1376 \ne 1$. This occurs because the flowing gas must heat the stationary solid packing, which has roughly 1000 times more heat capacity per unit volume than the gas. The thermal wave is therefore retarded by a factor of $\sim 1000$ relative to an unadsorbed fluid tracer.

---

### 5.5 Alternative Normalisation by Composite Heat Capacity $C_h$

Dividing the canonical equation (Equation 5.9) by $C_h$ isolates $\frac{\partial T}{\partial t}$ with a unit coefficient:
$$\boxed{
\frac{\partial T}{\partial t} + v_{\mathrm{th}}\frac{\partial T}{\partial z} = \alpha_{\mathrm{eff}}\frac{\partial^2 T}{\partial z^2} + \left(\frac{\rho_b q_{\mathrm{st}}}{C_h}\right)\frac{\partial q}{\partial t} - \left(\frac{4U}{d_{\mathrm{col}}C_h}\right)(T - T_w)
} \tag{5.18}$$

where:
* **Thermal front propagation velocity:**
  $$v_{\mathrm{th}} \equiv \frac{\rho_g C_{p,g} u_s}{C_h} = \frac{u_s / \varepsilon}{R_{\mathrm{th}}} = \frac{u_i}{R_{\mathrm{th}}} \ll u_i \quad [\mathrm{m\,s^{-1}}] \tag{5.19}$$
* **Effective bed thermal diffusivity:**
  $$\alpha_{\mathrm{eff}} \equiv \frac{\lambda_{\mathrm{eff}}}{C_h} \quad [\mathrm{m^2\,s^{-1}}] \tag{5.20}$$
* **Adiabatic temperature scaling coefficient:**
  $$\beta_{\mathrm{ad}} \equiv \frac{\rho_b q_{\mathrm{st}}}{C_h} \quad [\mathrm{K\,kg_{solid}\,mol^{-1}}] \tag{5.21}$$
* **Wall thermal relaxation frequency:**
  $$\omega_w \equiv \frac{4U}{d_{\mathrm{col}}C_h} = \frac{1}{\tau_w} \quad [\mathrm{s^{-1}}] \tag{5.22}$$

Every term in Equation (5.18) has dimensions of **$\mathrm{K\,s^{-1}}$**.

---

## 6. Formulation II: Heterogeneous, Two-Temperature Model

When interphase heat transfer is finite, local thermal equilibrium breaks down ($T_g(z,t) \ne T_s(z,t)$). We formulate separate, rigorously coupled energy conservation balances for the flowing gas and stationary solid.

### 6.1 Gas-Phase Energy Balance

Consider the fluid contained in the void volume $\Delta V_g = \varepsilon A \Delta z$:
1. **Accumulation:** $\varepsilon \rho_g C_{p,g} \frac{\partial T_g}{\partial t} A\Delta z$
2. **Convective transport:** Carrying gas enthalpy through open void area $\varepsilon A$: $-\rho_g C_{p,g} u_s \frac{\partial T_g}{\partial z} A\Delta z$
3. **Axial thermal dispersion:** Operating through the fluid phase: $\lambda_{g,\mathrm{eff}} \frac{\partial^2 T_g}{\partial z^2} A\Delta z$
4. **Gas-to-solid interphase transfer:** Heat transferred from gas to solid across the particle boundary layer: $-\dot{Q}_{gs}''' A\Delta z$
5. **Gas wall loss:** Direct convective heat loss from gas to column wall: $-\frac{4U_g}{d_{\mathrm{col}}}(T_g - T_w) A\Delta z$

Equating terms per unit bed volume:
$$\boxed{
\varepsilon \rho_g C_{p,g} \frac{\partial T_g}{\partial t} + \rho_g C_{p,g} u_s \frac{\partial T_g}{\partial z} = \lambda_{g,\mathrm{eff}} \frac{\partial^2 T_g}{\partial z^2} - h_{gs} a_v (T_g - T_s) - \frac{4U_g}{d_{\mathrm{col}}}(T_g - T_w)
} \tag{6.1}$$

---

### 6.2 Solid-Phase Energy Balance

Consider the stationary solid adsorbent in volume $\Delta V_s = (1-\varepsilon)A \Delta z$:
1. **Accumulation:** $(1-\varepsilon)\rho_p C_{p,s} \frac{\partial T_s}{\partial t} A\Delta z = \rho_b C_{p,s} \frac{\partial T_s}{\partial t} A\Delta z$
2. **Convective transport:** None, because the solid packing is stationary ($u_s^{\mathrm{solid}} = 0$).
3. **Axial conduction:** Conduction via direct particle-to-particle contact points: $\lambda_{s,\mathrm{eff}} \frac{\partial^2 T_s}{\partial z^2} A\Delta z$
4. **Interphase transfer:** Heat received from the gas phase: $+\dot{Q}_{gs}''' A\Delta z = +h_{gs} a_v (T_g - T_s) A\Delta z$
5. **Adsorption heat generation:** Physisorption occurs on solid pore surfaces: $+\rho_b q_{\mathrm{st}} \frac{\partial q}{\partial t} A\Delta z$
6. **Solid wall loss:** Conduction from outer particles contacting the column wall: $-\frac{4U_s}{d_{\mathrm{col}}}(T_s - T_w) A\Delta z$

Equating terms per unit bed volume:
$$\boxed{
(1-\varepsilon)\rho_p C_{p,s} \frac{\partial T_s}{\partial t} = \lambda_{s,\mathrm{eff}} \frac{\partial^2 T_s}{\partial z^2} + h_{gs} a_v (T_g - T_s) + \rho_b q_{\mathrm{st}} \frac{\partial q}{\partial t} - \frac{4U_s}{d_{\mathrm{col}}}(T_s - T_w)
} \tag{6.2}$$

*Phase assignment of adsorption heat:* Adsorption occurs on the internal surface of the porous solid. The latent heat of adsorption is liberated directly into the adsorbent lattice; hence, the source term belongs in the solid-phase energy equation. Transfer to the gas phase occurs indirectly through interphase convective exchange $h_{gs}a_v(T_s - T_g)$.

---

### 6.3 Gas–Solid Interphase Heat Transfer

Interphase exchange is governed by Newton's law of cooling across the external fluid film surrounding the adsorbent pellets:
$$\dot{Q}_{gs}''' = h_{gs} a_v (T_g - T_s) \quad [\mathrm{W\,m^{-3}_{bed}}] \tag{6.3}$$
where $h_{gs}$ is the boundary-layer heat transfer coefficient ($\mathrm{W\,m^{-2}\,K^{-1}}$) and $a_v$ is the external pellet surface area per unit bed volume ($\mathrm{m^2\,m^{-3}_{bed}}$).

#### Derivation of $a_v$ for Monodisperse Spherical Pellets
* Volume of one spherical particle: $V_p = \frac{\pi}{6} d_p^3$
* External surface area of one particle: $S_p = \pi d_p^2$
* Solid volume fraction in the packed bed: $1 - \varepsilon$
* Number of particles per unit bed volume:
  $$n_p = \frac{1 - \varepsilon}{V_p} = \frac{1 - \varepsilon}{\frac{\pi}{6}d_p^3} = \frac{6(1-\varepsilon)}{\pi d_p^3} \quad [\mathrm{m^{-3}_{bed}}] \tag{6.4}$$
* Total external surface area per unit bed volume:
  $$\boxed{
  a_v = n_p S_p = \left[\frac{6(1-\varepsilon)}{\pi d_p^3}\right](\pi d_p^2) = \frac{6(1-\varepsilon)}{d_p} \quad [\mathrm{m^2\,m^{-3}_{bed} = m^{-1}}]
  } \tag{6.5}$$

Equation (6.5) strictly holds for non-overlapping, smooth spherical pellets. For non-spherical particles, a sphericity factor $\phi_s$ is included: $a_v = \frac{6(1-\varepsilon)}{\phi_s d_p}$.

#### Internal Conservation Cancellation
The interphase term appears with opposite signs in Equations (6.1) and (6.2):
$$-h_{gs} a_v (T_g - T_s) + h_{gs} a_v (T_g - T_s) \equiv 0 \tag{6.6}$$
This exact algebraic cancellation confirms that interphase heat transfer redistributes thermal energy internally between phases without creating or destroying net energy.

---

### 6.4 Wall Heat Exchange Partition

When $T_g \ne T_s$, the bed exchanges heat with the column wall through both fluid convection ($U_g$) and particle contact conduction ($U_s$). To maintain physical consistency with the single-temperature limit ($T_g = T_s = T$):
$$\frac{4U_g}{d_{\mathrm{col}}}(T - T_w) + \frac{4U_s}{d_{\mathrm{col}}}(T - T_w) = \frac{4(U_g + U_s)}{d_{\mathrm{col}}}(T - T_w) \equiv \frac{4U}{d_{\mathrm{col}}}(T - T_w) \tag{6.7}$$
This imposes the thermodynamic closure:
$$\boxed{U = U_g + U_s} \tag{6.8}$$
Typically, wall exchange is dominated by the gas film, so $U_g \approx U$ and $U_s \approx 0$ is a standard, robust engineering approximation.

---

### 6.5 The Complete Coupled Heterogeneous System

The full heterogeneous governing model consists of four coupled PDEs and algebraic equilibrium closures:

$$\begin{aligned}
\text{[Gas Mass]} \quad & \frac{\partial c}{\partial t} = -\frac{u_s}{\varepsilon}\frac{\partial c}{\partial z} + D_L\frac{\partial^2 c}{\partial z^2} - \frac{\rho_b}{\varepsilon} k \left[ q_e(c,T_s) - q \right] \\
\text{[Solid Mass]} \quad & \frac{\partial q}{\partial t} = k \left[ q_e(c,T_s) - q \right] \\
\text{[Gas Energy]} \quad & \varepsilon \rho_g C_{p,g} \frac{\partial T_g}{\partial t} = -\rho_g C_{p,g} u_s \frac{\partial T_g}{\partial z} + \lambda_{g,\mathrm{eff}} \frac{\partial^2 T_g}{\partial z^2} - h_{gs} a_v (T_g - T_s) - \frac{4U_g}{d_{\mathrm{col}}}(T_g - T_w) \\
\text{[Solid Energy]} \quad & (1-\varepsilon)\rho_p C_{p,s} \frac{\partial T_s}{\partial t} = \lambda_{s,\mathrm{eff}} \frac{\partial^2 T_s}{\partial z^2} + h_{gs} a_v (T_g - T_s) + \rho_b q_{\mathrm{st}} k \left[ q_e(c,T_s) - q \right] - \frac{4U_s}{d_{\mathrm{col}}}(T_s - T_w)
\end{aligned} \tag{6.9}$$

Notice that the equilibrium loading $q_e(c, T_s)$ is evaluated at the solid temperature $T_s$, because adsorption equilibrium is governed by the state of the solid adsorbent surface.

---

## 7. Analytical Reduction to the Single-Temperature Limit

We now provide an asymptotic proof showing that the heterogeneous model (Formulation II) contracts mathematically to the pseudo-homogeneous model (Formulation I) as interphase heat transfer becomes rapid.

Let $H_{gs} \equiv h_{gs} a_v$ denote the volumetric interphase heat transfer coefficient ($\mathrm{W\,m^{-3}\,K^{-1}}$). Consider the asymptotic limit:
$$H_{gs} \to \infty \tag{7.1}$$

Rearranging the solid energy balance (Equation 6.2) to isolate the temperature difference:
$$T_g - T_s = \frac{1}{H_{gs}}\left[ (1-\varepsilon)\rho_p C_{p,s} \frac{\partial T_s}{\partial t} - \lambda_{s,\mathrm{eff}} \frac{\partial^2 T_s}{\partial z^2} - \rho_b q_{\mathrm{st}} \frac{\partial q}{\partial t} + \frac{4U_s}{d_{\mathrm{col}}}(T_s - T_w) \right] \tag{7.2}$$

Because the time derivative, spatial derivatives, and source terms remain bounded by physical transport limits, taking $H_{gs} \to \infty$ forces:
$$\lim_{H_{gs} \to \infty} (T_g - T_s) = 0 \implies T_g(z,t) = T_s(z,t) \equiv T(z,t) + \mathcal{O}(H_{gs}^{-1}) \tag{7.3}$$

Now, add the gas energy equation (Equation 6.1) and the solid energy equation (Equation 6.2):
$$\begin{aligned}
&\varepsilon \rho_g C_{p,g} \frac{\partial T_g}{\partial t} + (1-\varepsilon)\rho_p C_{p,s} \frac{\partial T_s}{\partial t} + \rho_g C_{p,g} u_s \frac{\partial T_g}{\partial z} \\
&= \lambda_{g,\mathrm{eff}}\frac{\partial^2 T_g}{\partial z^2} + \lambda_{s,\mathrm{eff}}\frac{\partial^2 T_s}{\partial z^2} - H_{gs}(T_g - T_s) + H_{gs}(T_g - T_s) + \rho_b q_{\mathrm{st}}\frac{\partial q}{\partial t} - \frac{4U_g}{d_{\mathrm{col}}}(T_g - T_w) - \frac{4U_s}{d_{\mathrm{col}}}(T_s - T_w)
\end{aligned} \tag{7.4}$$

Applying the asymptotic equality $T_g = T_s = T$:
1. **Accumulation:**
   $$\varepsilon \rho_g C_{p,g} \frac{\partial T}{\partial t} + (1-\varepsilon)\rho_p C_{p,s} \frac{\partial T}{\partial t} = \left[\varepsilon \rho_g C_{p,g} + (1-\varepsilon)\rho_p C_{p,s}\right]\frac{\partial T}{\partial t} = C_h \frac{\partial T}{\partial t}$$
2. **Convection:**
   $$\rho_g C_{p,g} u_s \frac{\partial T}{\partial z}$$
3. **Axial Conduction:**
   $$\lambda_{g,\mathrm{eff}}\frac{\partial^2 T}{\partial z^2} + \lambda_{s,\mathrm{eff}}\frac{\partial^2 T}{\partial z^2} = (\lambda_{g,\mathrm{eff}} + \lambda_{s,\mathrm{eff}})\frac{\partial^2 T}{\partial z^2} \equiv \lambda_{\mathrm{eff}} \frac{\partial^2 T}{\partial z^2}$$
4. **Interphase Exchange:**
   $$-H_{gs}(T - T) + H_{gs}(T - T) \equiv 0$$
5. **Adsorption Heat:**
   $$+\rho_b q_{\mathrm{st}}\frac{\partial q}{\partial t}$$
6. **Wall Heat Loss:**
   $$-\frac{4U_g}{d_{\mathrm{col}}}(T - T_w) - \frac{4U_s}{d_{\mathrm{col}}}(T - T_w) = -\frac{4(U_g + U_s)}{d_{\mathrm{col}}}(T - T_w) \equiv -\frac{4U}{d_{\mathrm{col}}}(T - T_w)$$

Combining these yields:
$$\boxed{
C_h \frac{\partial T}{\partial t} + \rho_g C_{p,g} u_s \frac{\partial T}{\partial z} = \lambda_{\mathrm{eff}}\frac{\partial^2 T}{\partial z^2} + \rho_b q_{\mathrm{st}}\frac{\partial q}{\partial t} - \frac{4U}{d_{\mathrm{col}}}(T - T_w)
} \tag{7.5}$$
which is identical to Equation (5.9).

### Dimensionless Criterion for Single-Temperature Validity
The asymptotic reduction holds when the interphase thermal resistance is much smaller than the convective residence time. Defining the interphase Stanton number:
$$St_{gs} \equiv \frac{h_{gs} a_v L}{\rho_g C_{p,g} u_s} \gg 1 \tag{7.6}$$
For typical laboratory packed beds ($d_p \le 2\ \mathrm{mm}$, $u_s \le 0.1\ \mathrm{m\,s^{-1}}$), $St_{gs}$ exceeds $10^2$, which justifies the pseudo-homogeneous single-temperature approximation.

---

## 8. Thermodynamic Derivation of the Isosteric Heat

### 8.1 Rigorous Derivation from the Langmuir Isotherm

The classical Clausius-Clapeyron equation applied to adsorption equilibrium defines the isosteric heat of adsorption, $q_{\mathrm{st}}$, as:
$$q_{\mathrm{st}} \equiv -\Delta H_{\mathrm{iso}} = R T^2 \left( \frac{\partial \ln P}{\partial T} \right)_{q_e} \tag{8.1}$$

We start with the Langmuir isotherm:
$$q_e = \frac{q_m b(T) P}{1 + b(T) P} \tag{8.2}$$
where fractional surface coverage is $\theta \equiv \frac{q_e}{q_m}$. Rearranging Equation (8.2) for the equilibrium pressure $P$:
$$q_e [1 + b(T)P] = q_m b(T) P \implies q_e = (q_m - q_e) b(T) P \tag{8.3}$$
Isolating $P$:
$$P = \frac{1}{b(T)} \left(\frac{q_e}{q_m - q_e}\right) = \frac{1}{b(T)} \left(\frac{\theta}{1 - \theta}\right) \tag{8.4}$$

Taking the natural logarithm of both sides:
$$\ln P = -\ln b(T) + \ln\left(\frac{\theta}{1 - \theta}\right) \tag{8.5}$$

We now take the partial derivative with respect to temperature $T$ holding the adsorbed loading $q_e$ (and therefore $\theta$) strictly constant:
$$\left( \frac{\partial \ln P}{\partial T} \right)_{q_e} = -\frac{d \ln b(T)}{d T} + \underbrace{\left(\frac{\partial \ln[\theta/(1-\theta)]}{\partial T}\right)_{q_e}}_{= 0} = -\frac{d \ln b(T)}{d T} \tag{8.6}$$

The temperature dependence of $b(T)$ is defined by the van't Hoff relation:
$$b(T) = b_0 \exp\left(-\frac{\Delta H_0}{R T}\right) \implies \ln b(T) = \ln b_0 - \frac{\Delta H_0}{R T} \tag{8.7}$$
Differentiating with respect to $T$:
$$\frac{d \ln b(T)}{d T} = -\frac{\Delta H_0}{R}\left(-\frac{1}{T^2}\right) = \frac{\Delta H_0}{R T^2} \tag{8.8}$$

Substituting Equation (8.8) into Equation (8.6):
$$\left( \frac{\partial \ln P}{\partial T} \right)_{q_e} = -\frac{\Delta H_0}{R T^2} \tag{8.9}$$

Finally, substituting Equation (8.9) into the Clausius-Clapeyron identity (Equation 8.1):
$$\boxed{
q_{\mathrm{st}} = R T^2 \left( \frac{\partial \ln P}{\partial T} \right)_{q_e} = R T^2 \left( -\frac{\Delta H_0}{R T^2} \right) = -\Delta H_0
} \tag{8.10}$$
Because adsorption is exothermic, $\Delta H_0 < 0$; therefore:
$$q_{\mathrm{st}} = -\Delta H_0 > 0 \tag{8.11}$$
This completes the formal proof that the parameter $-\Delta H_0$ in the van't Hoff affinity expression is identically the positive isosteric heat of adsorption $q_{\mathrm{st}}$.

---

### 8.2 Loading Dependence in Real Sorbents

For an ideal Langmuir model:
$$\left(\frac{\partial q_{\mathrm{st}}}{\partial q_e}\right)_T = \frac{\partial (-\Delta H_0)}{\partial q_e} = 0 \tag{8.12}$$
The heat of adsorption is mathematically independent of loading.

*Physical limitation:* The Langmuir model assumes a perfectly homogeneous solid surface with energetically identical sites and zero adsorbate–adsorbate interactions. In real porous sorbents (e.g., amine-functionalized silicas or zeolites), high-energy sites fill first, followed by lower-energy sites or multilayer adsorption. Consequently, the true isosteric heat declines with loading ($q_{\mathrm{st}} = f(q_e)$), as captured by the Toth or Freundlich isotherms.

---

### 8.3 Analysis of Using Independent Heats

Suppose a modeler uses an independently measured thermal value $\Delta H_{\mathrm{energy}}$ in the energy balance source term while retaining $\Delta H_0$ in the equilibrium isotherm $b(T)$.

#### Thermodynamic and Physical Consequences
1. **Thermodynamic Inconsistency:** If $\Delta H_{\mathrm{energy}} \ne \Delta H_0$, the model violates the Maxwell relations and the Gibbs-Duhem equation on the adsorbed phase. In closed cyclic processes (such as Temperature Swing Adsorption), this parameter mismatch produces unphysical perpetual energy generation or loss ($\oint dU \ne 0$).
2. **Spurious Temperature and Breakthrough Predictions:** Because $b(T)$ dictates how loading responds to temperature ($\partial q_e/\partial T$), using an unrelated heat source creates a kinetic-thermodynamic mismatch: the heat produced during breakthrough will not match the temperature sensitivity of the isotherm.
3. **Recommendation:** Modelers must enforce thermodynamic consistency by setting:
   $$\boxed{q_{\mathrm{st}} = -\Delta H_{\mathrm{iso}}(q_e, T) = R T^2 \left(\frac{\partial \ln P}{\partial T}\right)_{q_e}}$$
   Whenever empirical calorimetric heats are used, the isotherm temperature parameters must be re-fitted simultaneously to satisfy the Clausius-Clapeyron relation.

---

## 9. Audit and Correction of the Supplied Approximate Equation

### 9.1 Term-by-Term Audit

We audit the candidate equation:
$$(1-\varepsilon)(-\Delta H_0)\frac{\partial q'}{\partial t} = v \varepsilon \rho_p c_p \frac{\partial T}{\partial z} + (1-\varepsilon)\rho_p' c_p' \frac{\partial T}{\partial t} + \varepsilon p c_p \frac{\partial T}{\partial t} + \frac{4h}{d}(T - T_0) \tag{9.1}$$

| Term in Candidate Equation | Intended Physical Mechanism | First-Principles Term | Audit Finding & Critical Flaws |
|---|---|---|---|
| $(1-\varepsilon)(-\Delta H_0)\frac{\partial q'}{\partial t}$ | Adsorption heat generation source | $(1-\varepsilon)\rho_p(-\Delta H_0)\frac{\partial q}{\partial t} = \rho_b q_{\mathrm{st}}\frac{\partial q}{\partial t}$ | **Ambiguous Basis / Redundant Factor:** In literature (e.g., Ruthven 1975), $q'$ denotes pellet-volume-based loading ($\mathrm{mol\,m^{-3}_{pellet}}$), where $q' = \rho_p q$. If $q'$ is used, the factor $(1-\varepsilon)$ correctly converts it to a bed volume basis. However, if $q'$ is interpreted as mass loading $q$ ($\mathrm{mol\,kg^{-1}}$), the particle density $\rho_p$ is missing. |
| $v \varepsilon \rho_p c_p \frac{\partial T}{\partial z}$ | Convective enthalpy transport | $\rho_g C_{p,g} u_s \frac{\partial T}{\partial z} = \varepsilon \rho_g C_{p,g} v \frac{\partial T}{\partial z}$ | **Severe Physical Error:** The density in the fluid convective flux is written as $\rho_p$ (solid particle density $\sim 1000\ \mathrm{kg\,m^{-3}}$) instead of $\rho_g$ (gas density $\sim 1.2\ \mathrm{kg\,m^{-3}}$). This error overestimates convective heat transport by a factor of $\sim 800$, which would distort the simulated thermal front. |
| $(1-\varepsilon)\rho_p' c_p' \frac{\partial T}{\partial t}$ | Solid sensible heat accumulation | $(1-\varepsilon)\rho_p C_{p,s}\frac{\partial T}{\partial t}$ | **Notational Ambiguity:** Primed symbols $\rho_p', c_p'$ are redundant; standard notation uses $\rho_p$ and $C_{p,s}$ (or $\rho_s, c_s$). |
| $\varepsilon p c_p \frac{\partial T}{\partial t}$ | Gas sensible heat accumulation | $\varepsilon \rho_g C_{p,g}\frac{\partial T}{\partial t}$ | **Typographical Error:** The symbol $p$ represents pressure ($\mathrm{Pa}$). It is a typographical corruption of the Greek letter $\rho$ ($\rho_g$, gas density). |
| $\frac{4h}{d}(T - T_0)$ | Column wall heat loss | $\frac{4U}{d_{\mathrm{col}}}(T - T_w)$ | **Ambiguous Notation:** $h$ can be confused with specific enthalpy or interphase heat transfer; $U$ or $h_w$ is standard. $T_0$ can be confused with initial bed temperature; $T_w$ or $T_{\mathrm{ambient}}$ is unambiguous. |
| *[Absent]* | Axial conduction and dispersion | $\lambda_{\mathrm{eff}}\frac{\partial^2 T}{\partial z^2}$ | **Omitted Mechanism:** Omitting the second derivative $\frac{\partial^2 T}{\partial z^2}$ assumes an infinite axial thermal Péclet number ($Pe_{\mathrm{th}} \to \infty$). In low-flow laboratory packed beds ($Re < 10$), axial thermal conduction/dispersion is non-negligible. |

---

### 9.2 Sign Convention Analysis

Equation (9.1) is arranged as:
$$\text{Generation} = \text{Convection} + \text{Solid Accumulation} + \text{Gas Accumulation} + \text{Wall Loss} \tag{9.2}$$
Rearranging to isolate accumulation on the LHS:
$$\text{Accumulation} = -\text{Convection} + \text{Generation} - \text{Wall Loss} \tag{9.3}$$
$$\left[(1-\varepsilon)\rho_p' c_p' + \varepsilon \rho_g c_p\right]\frac{\partial T}{\partial t} + v\varepsilon \rho_g c_p \frac{\partial T}{\partial z} = (1-\varepsilon)(-\Delta H_0)\frac{\partial q'}{\partial t} - \frac{4h}{d}(T - T_0) \tag{9.4}$$
This demonstrates that the relative signs in the candidate equation are algebraically consistent with heat generation balancing storage, convective outflow, and wall loss, but the arrangement obscures the accumulation nature of the PDE.

---

### 9.3 Corrected Governing Equation

Replacing all corrupted, ambiguous, and erroneous terms, and reinstating axial thermal dispersion:

$$\boxed{
\left[\varepsilon \rho_g C_{p,g} + (1-\varepsilon)\rho_p C_{p,s}\right]\frac{\partial T}{\partial t} + \rho_g C_{p,g} u_s \frac{\partial T}{\partial z} = \lambda_{\mathrm{eff}}\frac{\partial^2 T}{\partial z^2} + (1-\varepsilon)\rho_p q_{\mathrm{st}}\frac{\partial q}{\partial t} - \frac{4U}{d_{\mathrm{col}}}(T - T_w)
} \tag{9.5}$$

Using bulk density $\rho_b = (1-\varepsilon)\rho_p$ and composite capacity $C_h$:
$$\boxed{
C_h \frac{\partial T}{\partial t} + \rho_g C_{p,g} u_s \frac{\partial T}{\partial z} = \lambda_{\mathrm{eff}}\frac{\partial^2 T}{\partial z^2} + \rho_b q_{\mathrm{st}}\frac{\partial q}{\partial t} - \frac{4U}{d_{\mathrm{col}}}(T - T_w)
} \tag{9.6}$$

---

## 10. Initial and Boundary Conditions

To close the governing coupled PDEs, we specify mathematically well-posed and physically consistent initial and boundary conditions.

### 10.1 Initial Conditions ($t = 0, \forall z \in [0, L]$)

#### Pseudo-Homogeneous Model
$$T(z, 0) = T_{\mathrm{init}}(z), \quad c(z, 0) = c_{\mathrm{init}}(z), \quad q(z, 0) = q_{\mathrm{init}}(z) \tag{10.1}$$

#### Heterogeneous Model
$$T_g(z, 0) = T_{g,\mathrm{init}}(z), \quad T_s(z, 0) = T_{s,\mathrm{init}}(z), \quad c(z, 0) = c_{\mathrm{init}}(z), \quad q(z, 0) = q_{\mathrm{init}}(z) \tag{10.2}$$

#### Clean vs. Pre-Equilibrated Bed
* **Clean (Thermally Regenerated) Bed:** Sorbent pores are completely evacuated:
  $$c(z, 0) = 0, \quad q(z, 0) = 0, \quad T(z, 0) = T_{\mathrm{init}} = T_w \tag{10.3}$$
* **Pre-Equilibrated Bed:** The initial solid loading is in local thermodynamic equilibrium with the gas phase:
  $$q(z, 0) = q_e(c_{\mathrm{init}}(z), T_{\mathrm{init}}(z)) \tag{10.4}$$
  Prescribing $q(z,0) = 0$ when $c(z,0) = c_0 > 0$ produces an instantaneous uptake jump $(\partial q/\partial t)_{t=0^+} = k q_e$, causing an artificial numerical thermal shock in the initial time step.

---

### 10.2 Thermal Inlet Boundary Condition ($z = 0, t > 0$)

At the column entrance ($z = 0$), the total energy flux entering from the upstream pipe must equal the total energy flux just inside the porous bed (Danckwerts flux continuity).

Upstream of the bed ($z = 0^-$), transport occurs purely by convection:
$$\dot{H}''(0^-) = \rho_g C_{p,g} u_s (T_{\mathrm{in}} - T_{\mathrm{ref}}) \quad [\mathrm{W\,m^{-2}_{bed}}] \tag{10.5}$$
Just inside the bed ($z = 0^+$), transport occurs by both convection and axial conduction/dispersion:
$$\dot{H}''(0^+) = \rho_g C_{p,g} u_s (T(0^+, t) - T_{\mathrm{ref}}) - \left.\lambda_{\mathrm{eff}} \frac{\partial T}{\partial z}\right|_{z=0^+} \quad [\mathrm{W\,m^{-2}_{bed}}] \tag{10.6}$$

Equating fluxes ($\dot{H}''(0^-) = \dot{H}''(0^+)$) eliminates $T_{\mathrm{ref}}$, yielding the **Danckwerts thermal inlet condition**:
$$\boxed{
\rho_g C_{p,g} u_s T_{\mathrm{in}} = \rho_g C_{p,g} u_s T(0^+, t) - \left.\lambda_{\mathrm{eff}}\frac{\partial T}{\partial z}\right|_{z=0^+}
} \tag{10.7}$$
Rearranging to Robin boundary form:
$$\boxed{
\left.\frac{\partial T}{\partial z}\right|_{z=0^+} = \frac{\rho_g C_{p,g} u_s}{\lambda_{\mathrm{eff}}}\left[ T(0^+, t) - T_{\mathrm{in}} \right]
} \tag{10.8}$$

*Dirichlet Limit:* When axial thermal dispersion is negligible ($\lambda_{\mathrm{eff}} \to 0$ or $Pe_{\mathrm{th}} \to \infty$), Equation (10.8) reduces to the standard Dirichlet condition:
$$T(0, t) = T_{\mathrm{in}} \tag{10.9}$$

#### Heterogeneous Model Inflow Boundaries
* **Gas Phase:** Convection brings gas at $T_{\mathrm{in}}$ into the bed:
  $$\left.\frac{\partial T_g}{\partial z}\right|_{z=0^+} = \frac{\rho_g C_{p,g} u_s}{\lambda_{g,\mathrm{eff}}}\left[ T_g(0^+, t) - T_{\mathrm{in}} \right] \tag{10.10}$$
* **Solid Phase:** The solid does not enter the column. The inlet boundary of the solid matrix is thermally insulated from external fluid advection:
  $$\boxed{
  \left.\frac{\partial T_s}{\partial z}\right|_{z=0} = 0
  } \tag{10.11}$$

---

### 10.3 Thermal Outlet Boundary Condition ($z = L, t > 0$)

Downstream of the bed exit ($z = L$), the fluid enters an open pipe where packing-induced dispersion ceases. To prevent an unphysical dispersive flux discontinuity at $z = L$, the axial temperature gradient must vanish (Danckwerts zero-gradient outlet condition):
$$\boxed{
\left.\frac{\partial T}{\partial z}\right|_{z=L} = 0
} \tag{10.12}$$
For the heterogeneous model:
$$\boxed{
\left.\frac{\partial T_g}{\partial z}\right|_{z=L} = 0, \qquad \left.\frac{\partial T_s}{\partial z}\right|_{z=L} = 0
} \tag{10.13}$$

---

### 10.4 Species Mass Balance Boundary Conditions

Matching the Danckwerts formulation used for the energy balance:
* **Inlet ($z = 0$):**
  $$\boxed{
  u_s c_{\mathrm{in}} = u_s c(0^+, t) - \left.\varepsilon D_L \frac{\partial c}{\partial z}\right|_{z=0^+} \implies \left.\frac{\partial c}{\partial z}\right|_{z=0^+} = \frac{u_s}{\varepsilon D_L}[c(0^+, t) - c_{\mathrm{in}}]
  } \tag{10.14}$$
* **Outlet ($z = L$):**
  $$\boxed{
  \left.\frac{\partial c}{\partial z}\right|_{z=L} = 0
  } \tag{10.15}$$

---

## 11. Complete SI Dimensional Audit

Every governing equation, term, and boundary condition is audited below to verify dimensional consistency.

### Table 11.1: Audit of Transport, Kinetic, and Thermodynamic Equations

| Equation / Law | Term Evaluated | Symbolic Expression | Parameter SI Units | Combined SI Units | Target Dimension | Consistent? |
|---|---|---|---|---|---|---|
| **Ideal Gas Law** | Partial pressure $P$ | $c R T$ | $(\mathrm{\frac{mol}{m^3_{fl}}})(\mathrm{\frac{J}{mol\,K}})(\mathrm{K})$ | $\mathrm{\frac{J}{m^3}} = \mathrm{\frac{N\,m}{m^3}} = \mathrm{Pa}$ | Pressure $[\mathrm{Pa}]$ | **Yes** |
| **Langmuir Affinity** | Exponent in $b(T)$ | $\frac{-\Delta H_0}{R T}$ | $\frac{\mathrm{J\,mol^{-1}}}{(\mathrm{J\,mol^{-1}\,K^{-1}})(\mathrm{K})}$ | $[-]$ | Dimensionless | **Yes** |
| **Langmuir Isotherm** | Denominator group | $b(T) P$ | $(\mathrm{Pa^{-1}})(\mathrm{Pa})$ | $[-]$ | Dimensionless | **Yes** |
| **LDF Rate Law** | Uptake rate | $\frac{\partial q}{\partial t} = k(q_e - q)$ | $(\mathrm{s^{-1}})(\mathrm{\frac{mol}{kg_{sol}}})$ | $\mathrm{\frac{mol}{kg_{sol}\,s}}$ | Rate $[\mathrm{\frac{mol}{kg\,s}}]$ | **Yes** |
| **Gas Mass Balance** | Accumulation | $\frac{\partial c}{\partial t}$ | $\frac{\mathrm{mol\,m^{-3}_{fl}}}{\mathrm{s}}$ | $\mathrm{\frac{mol}{m^3_{fl}\,s}}$ | Species Rate | **Yes** |
| **Gas Mass Balance** | Interstitial advection | $\frac{u_s}{\varepsilon}\frac{\partial c}{\partial z}$ | $\left(\frac{\mathrm{m\,s^{-1}}}{[-]}\right)\left(\frac{\mathrm{mol\,m^{-3}_{fl}}}{\mathrm{m}}\right)$ | $\mathrm{\frac{mol}{m^3_{fl}\,s}}$ | Species Rate | **Yes** |
| **Gas Mass Balance** | Axial dispersion | $D_L \frac{\partial^2 c}{\partial z^2}$ | $(\mathrm{m^2\,s^{-1}})\left(\frac{\mathrm{mol\,m^{-3}_{fl}}}{\mathrm{m^2}}\right)$ | $\mathrm{\frac{mol}{m^3_{fl}\,s}}$ | Species Rate | **Yes** |
| **Gas Mass Balance** | Interphase uptake sink | $\frac{\rho_b}{\varepsilon}\frac{\partial q}{\partial t}$ | $\left(\frac{\mathrm{kg_{sol}\,m^{-3}_{bed}}}{[-]}\right)\left(\frac{\mathrm{mol}}{\mathrm{kg_{sol}\,s}}\right)$ | $\mathrm{\frac{mol}{m^3_{bed}\,s}} \equiv \mathrm{\frac{mol}{m^3_{fl}\,s}}$ | Species Rate | **Yes** |

---

### Table 11.2: Dimensional Audit of Energy Balance PDEs

All terms in an unnormalised energy equation must have dimensions of power density:
$$\boxed{\mathrm{W\,m^{-3}_{bed}} = \mathrm{J\,s^{-1}\,m^{-3}} = \mathrm{kg\,m^{-1}\,s^{-3}}}$$

| Balance Model | Term Evaluated | Symbolic Expression | Parameter SI Units | Combined SI Units | Dimension | Consistent? |
|---|---|---|---|---|---|---|
| **Pseudo-Homogeneous** | Sensible heat accumulation | $C_h \frac{\partial T}{\partial t}$ | $\left(\mathrm{\frac{J}{m^3_{bed}\,K}}\right)\left(\mathrm{\frac{K}{s}}\right)$ | $\mathrm{\frac{J}{m^3\,s}} = \mathrm{W\,m^{-3}_{bed}}$ | $\mathrm{W\,m^{-3}}$ | **Yes** |
| **Pseudo-Homogeneous** | Convective enthalpy flux | $\rho_g C_{p,g} u_s \frac{\partial T}{\partial z}$ | $\left(\mathrm{\frac{kg}{m^3}}\right)\left(\mathrm{\frac{J}{kg\,K}}\right)\left(\mathrm{\frac{m}{s}}\right)\left(\mathrm{\frac{K}{m}}\right)$ | $\mathrm{\frac{J}{m^3\,s}} = \mathrm{W\,m^{-3}_{bed}}$ | $\mathrm{W\,m^{-3}}$ | **Yes** |
| **Pseudo-Homogeneous** | Axial heat dispersion | $\lambda_{\mathrm{eff}} \frac{\partial^2 T}{\partial z^2}$ | $\left(\mathrm{\frac{W}{m\,K}}\right)\left(\mathrm{\frac{K}{m^2}}\right)$ | $\mathrm{\frac{W}{m^3}} = \mathrm{W\,m^{-3}_{bed}}$ | $\mathrm{W\,m^{-3}}$ | **Yes** |
| **Pseudo-Homogeneous** | Adsorption heat source | $\rho_b q_{\mathrm{st}} \frac{\partial q}{\partial t}$ | $\left(\mathrm{\frac{kg}{m^3}}\right)\left(\mathrm{\frac{J}{mol}}\right)\left(\mathrm{\frac{mol}{kg\,s}}\right)$ | $\mathrm{\frac{J}{m^3\,s}} = \mathrm{W\,m^{-3}_{bed}}$ | $\mathrm{W\,m^{-3}}$ | **Yes** |
| **Pseudo-Homogeneous** | Column wall loss | $\frac{4U}{d_{\mathrm{col}}}(T - T_w)$ | $\left(\frac{[-]\cdot\mathrm{W\,m^{-2}\,K^{-1}}}{\mathrm{m}}\right)(\mathrm{K})$ | $\mathrm{\frac{W}{m^3}} = \mathrm{W\,m^{-3}_{bed}}$ | $\mathrm{W\,m^{-3}}$ | **Yes** |
| **Heterogeneous (Gas)** | Interphase heat loss | $h_{gs} a_v (T_g - T_s)$ | $\left(\mathrm{\frac{W}{m^2\,K}}\right)\left(\mathrm{\frac{m^2}{m^3}}\right)(\mathrm{K})$ | $\mathrm{\frac{W}{m^3}} = \mathrm{W\,m^{-3}_{bed}}$ | $\mathrm{W\,m^{-3}}$ | **Yes** |
| **Heterogeneous (Solid)**| Solid accumulation | $(1-\varepsilon)\rho_p C_{p,s}\frac{\partial T_s}{\partial t}$| $[-]\left(\mathrm{\frac{kg}{m^3}}\right)\left(\mathrm{\frac{J}{kg\,K}}\right)\left(\mathrm{\frac{K}{s}}\right)$ | $\mathrm{\frac{J}{m^3\,s}} = \mathrm{W\,m^{-3}_{bed}}$ | $\mathrm{W\,m^{-3}}$ | **Yes** |
| **Danckwerts Inlet** | Convective enthalpy flux | $\rho_g C_{p,g} u_s T_{\mathrm{in}}$ | $\left(\mathrm{\frac{kg}{m^3}}\right)\left(\mathrm{\frac{J}{kg\,K}}\right)\left(\mathrm{\frac{m}{s}}\right)(\mathrm{K})$ | $\mathrm{\frac{J}{m^2\,s}} = \mathrm{W\,m^{-2}_{bed}}$ | Heat Flux | **Yes** |
| **Danckwerts Inlet** | Conductive/dispersive flux | $\lambda_{\mathrm{eff}} \frac{\partial T}{\partial z}$ | $\left(\mathrm{\frac{W}{m\,K}}\right)\left(\mathrm{\frac{K}{m}}\right)$ | $\mathrm{\frac{W}{m^2}} = \mathrm{W\,m^{-2}_{bed}}$ | Heat Flux | **Yes** |

---

## 12. Mathematical and Physical Validation Tests

To verify the mathematical structure and physical validity of the derived models, we systematically evaluate key physical limits.

### 12.1 Limit 1: Non-Adsorbing Tracer ($\frac{\partial q}{\partial t} = 0$)

Setting the uptake rate to zero eliminates the adsorption heat source:
$$\rho_b q_{\mathrm{st}} \frac{\partial q}{\partial t} = 0 \tag{12.1}$$
The pseudo-homogeneous equation reduces to:
$$C_h \frac{\partial T}{\partial t} + \rho_g C_{p,g} u_s \frac{\partial T}{\partial z} = \lambda_{\mathrm{eff}} \frac{\partial^2 T}{\partial z^2} - \frac{4U}{d_{\mathrm{col}}}(T - T_w) \tag{12.2}$$
This is the classical linear advection-diffusion-reaction equation for thermal pulse transport in packed beds. Because $C_h \approx \rho_b C_{p,s}$, the thermal pulse migrates at the retarded velocity $v_{\mathrm{th}} = \rho_g C_{p,g} u_s / C_h$, which is roughly $1000$ times slower than the fluid interstitial velocity.

---

### 12.2 Limit 2: Strictly Adiabatic Column ($U = 0$)

Setting $U = 0$ removes heat exchange through the wall:
$$C_h \frac{\partial T}{\partial t} + \rho_g C_{p,g} u_s \frac{\partial T}{\partial z} = \lambda_{\mathrm{eff}} \frac{\partial^2 T}{\partial z^2} + \rho_b q_{\mathrm{st}} \frac{\partial q}{\partial t} \tag{12.3}$$
All released heat is retained in the bed or carried out by the effluent gas stream. The maximum theoretical adiabatic temperature rise across a fully saturating front ($q: 0 \to q_f$) is obtained by integrating over time:
$$\Delta T_{\mathrm{ad}} = \frac{\rho_b q_{\mathrm{st}} q_f}{C_h} \approx \frac{(1-\varepsilon)\rho_p (-\Delta H_0) q_f}{(1-\varepsilon)\rho_p C_{p,s}} = \frac{q_{\mathrm{st}} q_f}{C_{p,s}} \quad [\mathrm{K}] \tag{12.4}$$
This gives the upper bound on temperature excursions in large-diameter industrial columns.

---

### 12.3 Limit 3: Negligible Axial Dispersion ($\lambda_{\mathrm{eff}} \to 0$)

Setting $\lambda_{\mathrm{eff}} = 0$ converts the parabolic PDE into a first-order hyperbolic equation:
$$C_h \frac{\partial T}{\partial t} + \rho_g C_{p,g} u_s \frac{\partial T}{\partial z} = \rho_b q_{\mathrm{st}} \frac{\partial q}{\partial t} - \frac{4U}{d_{\mathrm{col}}}(T - T_w) \tag{12.5}$$
* The Robin-type Danckwerts inlet condition (Equation 10.8) collapses to the Dirichlet condition $T(0, t) = T_{\mathrm{in}}$.
* Discontinuous thermal shocks can propagate without diffusive smoothing, requiring numerical upwind discretisation to prevent unphysical oscillations.

---

### 12.4 Limit 4: Thermal Equilibrium Between Phases ($T_g = T_s = T$)

As proven in Section 7, setting $T_g = T_s = T$ and adding the gas and solid energy equations causes the interphase heat exchange terms $\pm h_{gs}a_v(T_g - T_s)$ to cancel identically. The heterogeneous system (Equation 6.9) collapses exactly to the pseudo-homogeneous equation (Equation 5.9), with effective parameters:
$$C_h = \varepsilon \rho_g C_{p,g} + (1-\varepsilon)\rho_p C_{p,s}, \quad \lambda_{\mathrm{eff}} = \lambda_{g,\mathrm{eff}} + \lambda_{s,\mathrm{eff}}, \quad U = U_g + U_s \tag{12.6}$$

---

### 12.5 Limit 5: Infinitely Fast Adsorption Kinetics ($k \to \infty$)

When $k \to \infty$, the solid loading relaxes instantaneously to local thermodynamic equilibrium:
$$q(z, t) \to q_e(c(z, t), T(z, t)) \tag{12.7}$$
By the multivariable chain rule:
$$\frac{\partial q}{\partial t} = \frac{\partial q_e}{\partial t} = \left(\frac{\partial q_e}{\partial c}\right)_T \frac{\partial c}{\partial t} + \left(\frac{\partial q_e}{\partial T}\right)_c \frac{\partial T}{\partial t} \tag{12.8}$$

Substituting Equation (12.8) into the energy equation:
$$\left[ C_h - \rho_b q_{\mathrm{st}}\left(\frac{\partial q_e}{\partial T}\right)_c \right] \frac{\partial T}{\partial t} + \rho_g C_{p,g} u_s \frac{\partial T}{\partial z} = \lambda_{\mathrm{eff}}\frac{\partial^2 T}{\partial z^2} + \rho_b q_{\mathrm{st}}\left(\frac{\partial q_e}{\partial c}\right)_T \frac{\partial c}{\partial t} - \frac{4U}{d_{\mathrm{col}}}(T - T_w) \tag{12.9}$$
Because $\partial q_e/\partial T < 0$ for exothermic adsorption, the term $-\rho_b q_{\mathrm{st}}(\partial q_e/\partial T)_c > 0$ increases the apparent thermal storage capacity of the bed. This demonstrates that fast kinetics does **not** extinguish the heat source; rather, heat release becomes slaved directly to the local rate of concentration change.

---

### 12.6 Limit 6: Global Energy Conservation Identity

We integrate the canonical pseudo-homogeneous equation (Equation 5.9) over the entire bed volume ($z \in [0, L]$, cross-section $A$):
$$\int_0^L A C_h \frac{\partial T}{\partial t}\,dz = -\int_0^L A \rho_g C_{p,g} u_s \frac{\partial T}{\partial z}\,dz + \int_0^L A \lambda_{\mathrm{eff}}\frac{\partial^2 T}{\partial z^2}\,dz + \int_0^L A \rho_b q_{\mathrm{st}}\frac{\partial q}{\partial t}\,dz - \int_0^L A \frac{4U}{d_{\mathrm{col}}}(T - T_w)\,dz \tag{12.10}$$

Using Leibniz's rule on the LHS, and integrating the spatial derivatives analytically:
$$\frac{d E_{\mathrm{bed}}}{dt} = -A \rho_g C_{p,g} u_s \left[ T(L, t) - T(0^+, t) \right] + A \lambda_{\mathrm{eff}} \left[ \left.\frac{\partial T}{\partial z}\right|_{z=L} - \left.\frac{\partial T}{\partial z}\right|_{z=0^+} \right] + \dot{Q}_{\mathrm{ads,total}} - \dot{Q}_{\mathrm{wall,total}} \tag{12.11}$$

Applying the Danckwerts boundary conditions:
1. At the outlet ($z = L$), $\left.\frac{\partial T}{\partial z}\right|_{z=L} = 0$.
2. At the inlet ($z = 0^+$), $\left.\lambda_{\mathrm{eff}}\frac{\partial T}{\partial z}\right|_{z=0^+} = \rho_g C_{p,g} u_s \left[ T(0^+, t) - T_{\mathrm{in}} \right]$.

Substituting these boundary constraints into Equation (12.11):
$$\begin{aligned}
\frac{d E_{\mathrm{bed}}}{dt} &= -A \rho_g C_{p,g} u_s T(L, t) + A \rho_g C_{p,g} u_s T(0^+, t) - A \rho_g C_{p,g} u_s \left[ T(0^+, t) - T_{\mathrm{in}} \right] + \dot{Q}_{\mathrm{ads,total}} - \dot{Q}_{\mathrm{wall,total}} \\
&= \underbrace{A \rho_g C_{p,g} u_s T_{\mathrm{in}}}_{\text{Enthalpy In}} - \underbrace{A \rho_g C_{p,g} u_s T(L, t)}_{\text{Enthalpy Out}} + \underbrace{\int_0^L A \rho_b q_{\mathrm{st}}\frac{\partial q}{\partial t}\,dz}_{\text{Total Adsorption Heat Released}} - \underbrace{\int_0^L \pi d_{\mathrm{col}} U (T - T_w)\,dz}_{\text{Total Heat Lost to Wall}}
\end{aligned} \tag{12.12}$$

This proves that internal axial dispersion cancels identically from the global balance, leaving only boundary fluxes and volumetric source/sink integrals. The derived energy equation strictly satisfies the First Law of Thermodynamics over the entire column domain.

---

## 13. Numerical Implementation Implications

### 13.1 Equation Coupling and Stiff Nonlinearities

The non-isothermal model couples species transport, solid adsorption kinetics, and energy conservation. The state vector at each axial node $z_j$ is:
$$\mathbf{y}_j(t) = \begin{bmatrix} c(z_j, t) \\ q(z_j, t) \\ T(z_j, t) \end{bmatrix} \quad (\text{Formulation I}) \quad \text{or} \quad \mathbf{y}_j(t) = \begin{bmatrix} c(z_j, t) \\ q(z_j, t) \\ T_g(z_j, t) \\ T_s(z_j, t) \end{bmatrix} \quad (\text{Formulation II}) \tag{13.1}$$

The system contains two distinct sources of numerical stiffness:
1. **Kinetic Stiffness:** Fast intraparticle adsorption ($k \gg 1\ \mathrm{s^{-1}}$) causes $q$ to track $q_e$ on a timescale orders of magnitude shorter than the convective residence time ($L/u_i$).
2. **Thermal Inertia Disparity:** The thermal wave velocity $v_{\mathrm{th}} \sim u_i / 1000$ introduces two widely separated characteristic convective timescales.
3. **Exponential Non-linearity:** The van't Hoff relation $b(T) = b_0 \exp(-\Delta H_0/RT)$ introduces strong exponential coupling between the energy balance and the mass sink term.

Consequently, explicit time-stepping schemes (e.g., Forward Euler or standard Runge-Kutta 4) are subject to severe Courant-Friedrichs-Lewy (CFL) stability restrictions ($\Delta t \le \min[\frac{\Delta z}{u_i}, \frac{2}{k}, \frac{\Delta z^2}{2\alpha}]$). Stiff implicit solvers (e.g., `scipy.integrate.solve_ivp` with `BDF` or `Radau`) or semi-implicit operator splitting are required for stable time integration.

---

### 13.2 Spatial Discretisation via the Method of Lines (MOL)

In the Method of Lines (MOL), the axial coordinate $z \in [0, L]$ is discretised into $N$ spatial nodes ($z_j = j\Delta z, \Delta z = L/N$).
* **Advection Terms:** Standard second-order central differencing for $\partial T/\partial z$ induces unphysical spatial oscillations (numerical dispersion) near steep fronts when the grid Péclet number $Pe_{\Delta z} = \frac{\rho_g C_{p,g} u_s \Delta z}{\lambda_{\mathrm{eff}}} > 2$. To preserve monotonicity, first-order upwind differencing or flux-limited Total Variation Diminishing (TVD) schemes (e.g., Superbee or Koren limiters) should be used:
  $$\left. u_s \frac{\partial T}{\partial z} \right|_j \approx u_s \frac{T_j - T_{j-1}}{\Delta z} \quad (\text{First-order upwind}) \tag{13.2}$$
* **Diffusion and Conduction Terms:** Evaluated via conservative second-order central differencing:
  $$\left. \lambda_{\mathrm{eff}}\frac{\partial^2 T}{\partial z^2} \right|_j \approx \lambda_{\mathrm{eff}}\frac{T_{j+1} - 2T_j + T_{j-1}}{\Delta z^2} \tag{13.3}$$

---

### 13.3 Parameter Identifiability and Decoupled Calibration

To prevent parameter cross-correlation, model parameters should be determined through decoupled experimental calibrations:
1. **Thermodynamic Parameters ($q_m, b_0, \Delta H_0$):** Fitted exclusively to pure-component static adsorption isotherms measured across multiple equilibrium temperatures ($T = 298, 323, 348\ \mathrm{K}$).
2. **Mass Dispersion and Kinetics ($D_L, k$):** Calibrated from isothermal breakthrough experiments under conditions where heat effects are negligible ($d_{\mathrm{col}} \le 4\ \mathrm{mm}$, dilute feeds).
3. **Interphase Heat Transfer ($h_{gs}$):** Estimated from established packed-bed empirical correlations (e.g., Wakao & Kaguei, or Whitaker):
   $$Nu_{gs} \equiv \frac{h_{gs} d_p}{\lambda_g} = 2.0 + 1.1\,Re_p^{0.6}\,Pr^{1/3} \tag{13.4}$$
4. **Wall Heat Transfer ($U$):** Determined from non-adsorbing hot-gas tracer cooling runs ($q = 0$) or Dixon's packed-bed wall correlation.

#### Pitfall of Validating with Concentration Breakthrough Alone
A common modelling error is validating non-isothermal models using only effluent concentration curves ($c(L, t)$). Because multiple parameter combinations ($k, U, q_{\mathrm{st}}$) can produce similar mass-breakthrough smearing, fitting concentration alone obscures severe underlying thermal errors. True model validation requires simultaneous measurement and cross-validation of internal axial temperature profiles ($T(z_j, t)$).

---

## 14. Final Boxed Governing Equations and Summary of Assumptions

### 14.1 Formulation I: Pseudo-Homogeneous Single-Temperature System

$$\boxed{
\begin{aligned}
\frac{\partial c}{\partial t} &= -\frac{u_s}{\varepsilon}\frac{\partial c}{\partial z} + D_L\frac{\partial^2 c}{\partial z^2} - \frac{\rho_b}{\varepsilon} k \left[ q_e(c, T) - q \right] \\[10pt]
\frac{\partial q}{\partial t} &= k \left[ q_e(c, T) - q \right] \\[10pt]
C_h \frac{\partial T}{\partial t} &= -\rho_g C_{p,g} u_s \frac{\partial T}{\partial z} + \lambda_{\mathrm{eff}}\frac{\partial^2 T}{\partial z^2} + \rho_b q_{\mathrm{st}} k \left[ q_e(c, T) - q \right] - \frac{4U}{d_{\mathrm{col}}}(T - T_w) \\[10pt]
q_e(c, T) &= \frac{q_m b_0 \exp\left(-\frac{\Delta H_0}{RT}\right) c R T}{1 + b_0 \exp\left(-\frac{\Delta H_0}{RT}\right) c R T}, \qquad q_{\mathrm{st}} = -\Delta H_0 > 0 \\[10pt]
C_h &= \varepsilon \rho_g C_{p,g} + (1-\varepsilon)\rho_p C_{p,s}, \qquad \rho_b = (1-\varepsilon)\rho_p
\end{aligned}
} \tag{14.1}$$

---

### 14.2 Formulation II: Heterogeneous Two-Temperature System

$$\boxed{
\begin{aligned}
\frac{\partial c}{\partial t} &= -\frac{u_s}{\varepsilon}\frac{\partial c}{\partial z} + D_L\frac{\partial^2 c}{\partial z^2} - \frac{\rho_b}{\varepsilon} k \left[ q_e(c, T_s) - q \right] \\[10pt]
\frac{\partial q}{\partial t} &= k \left[ q_e(c, T_s) - q \right] \\[10pt]
\varepsilon \rho_g C_{p,g} \frac{\partial T_g}{\partial t} &= -\rho_g C_{p,g} u_s \frac{\partial T_g}{\partial z} + \lambda_{g,\mathrm{eff}}\frac{\partial^2 T_g}{\partial z^2} - h_{gs} a_v (T_g - T_s) - \frac{4U_g}{d_{\mathrm{col}}}(T_g - T_w) \\[10pt]
(1-\varepsilon)\rho_p C_{p,s} \frac{\partial T_s}{\partial t} &= \lambda_{s,\mathrm{eff}}\frac{\partial^2 T_s}{\partial z^2} + h_{gs} a_v (T_g - T_s) + \rho_b q_{\mathrm{st}} k \left[ q_e(c, T_s) - q \right] - \frac{4U_s}{d_{\mathrm{col}}}(T_s - T_w) \\[10pt]
a_v &= \frac{6(1-\varepsilon)}{d_p}, \qquad U = U_g + U_s, \qquad \lambda_{\mathrm{eff}} = \lambda_{g,\mathrm{eff}} + \lambda_{s,\mathrm{eff}}
\end{aligned}
} \tag{14.2}$$

---

### 14.3 Complete Summary of Assumptions and Model Validity

| Feature / Assumption | Formulation I: Pseudo-Homogeneous | Formulation II: Heterogeneous |
|---|---|---|
| **Interphase Thermal State** | Local thermal equilibrium: $T_g = T_s = T$ | Distinct phase temperatures: $T_g \ne T_s$ |
| **Number of Coupled PDEs** | 3 PDEs ($c, q, T$) | 4 PDEs ($c, q, T_g, T_s$) |
| **Interphase Resistance Criterion** | Required: $St_{gs} = \frac{h_{gs} a_v L}{\rho_g C_{p,g} u_s} \gg 1$ | Valid for arbitrary $St_{gs}$ (finite film resistance) |
| **Adsorbent Particle Diameter** | Small particles ($d_p < 2\ \mathrm{mm}$) | Large particles / extrudates ($d_p \ge 3\ \mathrm{mm}$) |
| **Gas Flow Velocity** | Low-to-moderate velocity ($Re_p < 20$) | High superficial velocities ($Re_p \ge 50$) |
| **Heat Release Location** | Distributed directly into composite bed | Generated exclusively in the solid matrix |
| **Equilibrium Temperature** | Evaluated at combined bed temperature $T$ | Evaluated strictly at solid temperature $T_s$ |
| **Wall Boundary Exchange** | Single overall coefficient $U$ | Partitioned wall coefficients $U_g, U_s$ ($U_g + U_s = U$) |
| **Mathematical Complexity** | Simpler; fewer calibration parameters | Requires empirical interphase correlation ($Nu_{gs}$) |
| **Asymptotic Equivalence** | Exact match when $H_{gs} = h_{gs} a_v \to \infty$ | Collapses exactly to Formulation I as $h_{gs} \to \infty$ |

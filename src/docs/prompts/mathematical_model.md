## Mathematical Problem Prompt — Mechanistic Fixed-Bed CO₂ Adsorption Model

**Source setting.** A packed-bed column is used to adsorb CO₂ from an inert carrier gas. The model should be one-dimensional in the axial coordinate (z), transient in time (t), and mechanistic: it must be derived from conservation laws, not fitted directly as a Thomas/Yoon–Nelson/Bohart–Adams empirical curve. The standard modelling structure is a macroscopic mass conservation equation, an uptake-rate equation, and an equilibrium isotherm; Xu et al. explicitly describe this as the usual PDE-based route for predicting breakthrough curves. 

### PROMPT — send as-is

Do not search the internet. Develop and solve, as far as mathematically possible, a mechanistic model for single-component CO₂ adsorption in a 1-D fixed-bed column with inert carrier gas.

The task is not merely to write down equations. You must derive the model from conservation laws, close it with physically justified adsorption kinetics and an equilibrium isotherm, nondimensionalise it, identify the governing dimensionless groups, prove the appropriate conservation checks, solve the analytically tractable limiting cases, and then give the mathematically correct numerical formulation for the full nonlinear non-isothermal case.

The model should include:

1. Gas-phase CO₂ concentration (c(z,t)).
2. Solid-phase adsorbed loading (q(z,t)).
3. Temperature (T(z,t)), unless you explicitly state and justify an isothermal reduction.
4. Axial convection and axial dispersion.
5. Linear driving force kinetics.
6. A nonlinear equilibrium isotherm, preferably Toth for an amine-functionalised sorbent, or Dual-Site Langmuir if modelling zeolite 13X.
7. Heat release from adsorption in the non-isothermal case.
8. A feed-step inlet condition and a clean-bed initial condition.

Use the following symbols:

[
z\in[0,L],\qquad t\ge 0,
]

[
\varepsilon=\text{bed voidage},\qquad u=\text{superficial axial gas velocity},
]

[
D_L=\text{axial dispersion coefficient},\qquad \rho_p=\text{particle density},
]

[
c=\text{gas-phase CO₂ concentration},\qquad q=\text{solid loading},
]

[
q^*(c,T)=\text{equilibrium loading},\qquad k=\text{LDF rate constant}.
]

The clean-bed initial condition is

[
c(z,0)=0,\qquad q(z,0)=0,\qquad T(z,0)=T_0.
]

The inlet feed condition is a step input

[
c(0,t)=c_f,\qquad T(0,t)=T_f,\qquad t>0,
]

with zero-gradient outlet conditions at (z=L). You may use Danckwerts boundary conditions if retaining axial dispersion carefully.

Your answer must do the following.

### Part A — Derive the model

Start from an axial control volume and derive the gas-phase mass balance

[
\varepsilon \frac{\partial c}{\partial t}
+
u\frac{\partial c}{\partial z}
==============================

## \varepsilon D_L \frac{\partial^2 c}{\partial z^2}

(1-\varepsilon)\rho_p\frac{\partial q}{\partial t}.
]

Then close the model using LDF kinetics

[
\frac{\partial q}{\partial t}
=============================

k\bigl(q^*(c,T)-q\bigr).
]

Use either the Toth isotherm

[
q^*(c,T)
========

\frac{n_s(T)b(T)c}{\left[1+{b(T)c}^{t_T}\right]^{1/t_T}},
]

or the single-component reduction of a Dual-Site Langmuir isotherm

[
q^*(c,T)
========

\frac{q_1 b(T)c}{1+b(T)c}
+
\frac{q_2 d(T)c}{1+d(T)c},
]

with temperature-dependent affinity parameters such as

[
b(T)=b_0\exp!\left(-\frac{\Delta U_b}{RT}\right),
\qquad
d(T)=d_0\exp!\left(-\frac{\Delta U_d}{RT}\right).
]

Then derive the pseudo-homogeneous non-isothermal energy balance

[
C_h\frac{\partial T}{\partial t}
+
u\rho_g c_{p,g}\frac{\partial T}{\partial z}
============================================

\lambda_{\mathrm{eff}}\frac{\partial^2T}{\partial z^2}
+
(1-\varepsilon)\rho_p(-\Delta H)\frac{\partial q}{\partial t}
-------------------------------------------------------------

\frac{4h_w}{d_{\mathrm{col}}}(T-T_{\mathrm{wall}}),
]

where

[
C_h=\varepsilon\rho_g c_{p,g}+(1-\varepsilon)\rho_p c_{p,s}.
]

Explain the physical meaning and units of every term.

### Part B — Conservation and well-posedness checks

Show that the model conserves total CO₂ inventory up to inlet/outlet fluxes. In particular, prove that

[
\frac{d}{dt}
\int_0^L
\left[
\varepsilon c+(1-\varepsilon)\rho_p q
\right],dz
==========

## \text{inlet CO₂ flux}

\text{outlet CO₂ flux},
]

with the correct dispersive boundary terms if Danckwerts conditions are used.

Also show that if (c,q\ge 0) initially and (q^*(0,T)=0), then the kinetics preserve physically meaningful nonnegative loading.

### Part C — Nondimensionalisation

Define dimensionless variables

[
x=\frac{z}{L},\qquad \tau=\frac{ut}{L},\qquad C=\frac{c}{c_f},\qquad Q=\frac{q}{q_f},\qquad \Theta=\frac{T-T_0}{\Delta T}.
]

Derive the dimensionless model and identify at least the following groups:

[
Pe=\frac{uL}{D_L},
]

[
Da=\frac{kL}{u},
]

[
\alpha=\frac{(1-\varepsilon)\rho_p q_f}{\varepsilon c_f},
]

[
Pe_h=\frac{C_huL}{\lambda_{\mathrm{eff}}},
]

[
\Lambda=\frac{(1-\varepsilon)\rho_p(-\Delta H)q_f}{C_h\Delta T}.
]

Interpret what each group means physically.

### Part D — Solve the analytically tractable limits

First solve the **isothermal local-equilibrium limit**

[
T=T_0,\qquad D_L=0,\qquad k\to\infty,
]

so that

[
q=q^*(c,T_0)=Q(c).
]

Show that the model reduces to the scalar conservation law

[
\frac{\partial}{\partial t}
\left[
\varepsilon c+(1-\varepsilon)\rho_p Q(c)
\right]
+
u\frac{\partial c}{\partial z}
==============================

0.

]

For a clean bed initially and a feed step (c_f), derive the Rankine–Hugoniot adsorption-front speed

[
v_{\mathrm{RH}}
===============

\frac{u c_f}
{\varepsilon c_f+(1-\varepsilon)\rho_p Q(c_f)}.
]

Then derive the ideal stoichiometric breakthrough time

[
t_{\mathrm{st}}
===============

# \frac{L}{v_{\mathrm{RH}}}

\frac{L\left[\varepsilon c_f+(1-\varepsilon)\rho_pQ(c_f)\right]}{u c_f}.
]

Next solve the **linear-isotherm local-equilibrium limit**

[
Q(c)=Kc.
]

Show that the model becomes an advection-dispersion equation with retarded velocity

[
v_{\mathrm{eff}}
================

\frac{u}{\varepsilon+(1-\varepsilon)\rho_pK},
]

and effective dispersion

[
D_{\mathrm{eff}}
================

\frac{\varepsilon D_L}{\varepsilon+(1-\varepsilon)\rho_pK}.
]

Give the semi-infinite step-input solution in terms of complementary error functions.

Finally, explain why the fully nonlinear, finite-(k), non-isothermal model does not generally have a closed-form solution and must be solved by Method of Lines or finite-volume time integration.

### Part E — Full numerical solution

Give a spatially discretised Method-of-Lines formulation. For grid points (z_i=i\Delta z), define the state vector

[
y(t)=
[c_1,\ldots,c_N,\ q_1,\ldots,q_N,\ T_1,\ldots,T_N]^T.
]

Use upwind differencing for axial convection and central differencing for axial dispersion/conduction. Derive the ODE system

[
\frac{dy}{dt}=f(t,y),
]

and specify how to impose inlet and outlet boundary conditions.

Define breakthrough time as

[
t_{\mathrm{BT}}
===============

\inf\left{
t>0:\frac{c(L,t)}{c_f}=0.05
\right},
]

saturation time as

[
t_{\mathrm{sat}}
================

\inf\left{
t>0:\frac{c(L,t)}{c_f}=0.95
\right},
]

and dynamic capacity as

[
q_{\mathrm{dyn}}
================

\frac{1}{(1-\varepsilon)\rho_pL}
\int_0^{t_{\mathrm{BT}}}
u\bigl(c_f-c(L,t)\bigr),dt.
]

End by stating the validation tests the model must pass:

1. No-adsorption advection-dispersion test.
2. Isothermal Rankine–Hugoniot front-speed test.
3. Non-isothermal benchmark breakthrough curve test.
4. Mass-balance drift below a specified tolerance.

---

# Worked Solution

The correct mechanistic model is a **conservation-law plus relaxation system**. The literature roadmap already collects this structure: a fluid-phase mass balance, LDF kinetics, nonlinear isotherm, non-isothermal energy balance, and Method-of-Lines integration are listed as the consolidated governing-equation sheet for the project. 

Let

[
\alpha_b=(1-\varepsilon)\rho_p.
]

Here (\alpha_b q) has units of moles of adsorbed CO₂ per bed volume if (q) is in mol/kg.

For an axial control volume of cross-section (A) and thickness (\Delta z), the gas-phase accumulation is

[
A\Delta z,\varepsilon \frac{\partial c}{\partial t}.
]

The convective flux difference is

[
A u c\big|_{z}
--------------

A u c\big|_{z+\Delta z}
\approx
-A\Delta z,u\frac{\partial c}{\partial z}.
]

The axial dispersive flux is Fickian,

[
J_D=-\varepsilon D_L\frac{\partial c}{\partial z},
]

so its net contribution is

[
A\Delta z,\varepsilon D_L\frac{\partial^2 c}{\partial z^2}.
]

The adsorption sink is

[
A\Delta z,(1-\varepsilon)\rho_p\frac{\partial q}{\partial t}.
]

Dividing by (A\Delta z) gives

[
\boxed{
\varepsilon c_t+u c_z
=====================

## \varepsilon D_L c_{zz}

(1-\varepsilon)\rho_p q_t.
}
]

This is the core fixed-bed mass balance. If (u) is instead defined as the true interstitial velocity, replace (u) in the convective term by (\varepsilon u). The prompt’s convention uses (u) as the superficial axial flux appearing directly in the balance.

The solid phase is closed using LDF kinetics:

[
\boxed{
q_t=k(q^*(c,T)-q).
}
]

This is mechanistic but lumped: the project roadmap notes that LDF stands in for true intraparticle macro/micropore diffusion and is useful at this level of modelling, while also warning that the approximation loses resolution when diffusional resistances are not well separated. 

For an amine-functionalised sorbent, the Toth closure is

[
\boxed{
q^*(c,T)
========

\frac{n_s(T)b(T)c}
{\left[1+{b(T)c}^{t_T}\right]^{1/t_T}}.
}
]

For a zeolite-13X-style CO₂/N₂ model, a single-component Dual-Site Langmuir closure is

[
\boxed{
q^*(c,T)
========

\frac{q_1 b(T)c}{1+b(T)c}
+
\frac{q_2 d(T)c}{1+d(T)c}.
}
]

The roadmap identifies Fabian Ramos et al. as the fully worked CO₂/N₂ source using DSL, Arrhenius temperature-dependence, LDF, and heat-of-adsorption coupling.  The same roadmap also flags Toth, Langmuir, Freundlich, Sips, and other isotherms as candidate closures, with model choice requiring error-function comparison rather than arbitrary selection. 

The pseudo-homogeneous energy balance is

[
\boxed{
C_hT_t+u\rho_g c_{p,g}T_z
=========================

\lambda_{\mathrm{eff}}T_{zz}
+
(1-\varepsilon)\rho_p(-\Delta H)q_t
-----------------------------------

\frac{4h_w}{d_{\mathrm{col}}}(T-T_{\mathrm{wall}}),
}
]

where

[
C_h
===

\varepsilon\rho_g c_{p,g}
+
(1-\varepsilon)\rho_p c_{p,s}.
]

The heat source is positive for exothermic adsorption because (-\Delta H>0) and (q_t>0) during uptake. The project roadmap gives the same non-isothermal heat balance form and notes that isosteric heat can include temperature and loading dependence. 

For an adiabatic column,

[
h_w=0.
]

So the full model is

[
\boxed{
\varepsilon c_t+u c_z
=====================

## \varepsilon D_L c_{zz}

\alpha_b q_t,
}
]

[
\boxed{
q_t=k(q^*(c,T)-q),
}
]

[
\boxed{
C_hT_t+u\rho_g c_{p,g}T_z
=========================

\lambda_{\mathrm{eff}}T_{zz}
+
\alpha_b(-\Delta H)q_t.
}
]

The clean-bed initial condition is

[
c(z,0)=0,\qquad q(z,0)=0,\qquad T(z,0)=T_0.
]

A simple inlet condition is

[
c(0,t)=c_f,\qquad T(0,t)=T_f.
]

A more careful dispersive inlet uses Danckwerts flux matching:

[
u c_f
=====

u c(0,t)-\varepsilon D_L c_z(0,t),
]

with outlet condition

[
c_z(L,t)=0.
]

The analogous thermal Danckwerts condition is

[
u\rho_g c_{p,g}T_f
==================

u\rho_g c_{p,g}T(0,t)-\lambda_{\mathrm{eff}}T_z(0,t),
]

with

[
T_z(L,t)=0.
]

For conservation, define the total CO₂ inventory

[
M(t)=
\int_0^L
\left[
\varepsilon c+\alpha_bq
\right]dz.
]

Add (\alpha_bq_t) to both sides of the gas mass balance:

[
\frac{\partial}{\partial t}
\left[
\varepsilon c+\alpha_bq
\right]
+
u c_z
=====

\varepsilon D_Lc_{zz}.
]

Equivalently,

[
\frac{\partial}{\partial t}
\left[
\varepsilon c+\alpha_bq
\right]
+
\frac{\partial}{\partial z}
\left[
u c-\varepsilon D_Lc_z
\right]
=======

0.

]

Integrating from (0) to (L),

[
\boxed{
\frac{dM}{dt}
=============

\left[
u c-\varepsilon D_Lc_z
\right]_{z=0}
-------------

\left[
u c-\varepsilon D_Lc_z
\right]_{z=L}.
}
]

With Danckwerts inlet and zero-gradient outlet, this becomes

[
\boxed{
\frac{dM}{dt}
=============

u c_f-u c(L,t).
}
]

This identity is the main mass-balance guardrail for numerical simulations.

Now nondimensionalise with

[
x=\frac{z}{L},\qquad \tau=\frac{ut}{L},\qquad C=\frac{c}{c_f},\qquad Q=\frac{q}{q_f}.
]

Let

[
\Theta=\frac{T-T_0}{\Delta T}.
]

Then the mass balance becomes

[
\boxed{
\varepsilon C_\tau+C_x
======================

## \frac{\varepsilon}{Pe}C_{xx}

\beta Q_\tau,
}
]

where

[
Pe=\frac{uL}{D_L},
\qquad
\beta=\frac{\alpha_bq_f}{c_f}.
]

The LDF equation becomes

[
\boxed{
Q_\tau
======

Da,[Q^*(C,\Theta)-Q],
}
]

where

[
Da=\frac{kL}{u}.
]

Equivalently, if the gas accumulation is used as the scaling denominator, the capacity ratio is

[
\boxed{
\alpha=
\frac{(1-\varepsilon)\rho_pq_f}{\varepsilon c_f}.
}
]

The energy equation becomes

[
\boxed{
\Theta_\tau
+
\gamma_h\Theta_x
================

\frac{1}{Pe_h}\Theta_{xx}
+
\Lambda Q_\tau
--------------

Bi_w\Theta,
}
]

where

[
\gamma_h=\frac{\rho_g c_{p,g}}{C_h},
]

[
Pe_h=\frac{C_huL}{\lambda_{\mathrm{eff}}},
]

[
\Lambda=
\frac{\alpha_b(-\Delta H)q_f}{C_h\Delta T},
]

and

[
Bi_w=
\frac{4h_wL}{d_{\mathrm{col}}C_hu}.
]

For adiabatic operation,

[
Bi_w=0.
]

The dimensionless meanings are:

[
Pe=\frac{\text{axial convection}}{\text{axial dispersion}},
]

[
Da=\frac{\text{convective residence time}}{\text{LDF kinetic time}},
]

[
\alpha=\frac{\text{solid-phase adsorption capacity}}{\text{gas-phase void inventory}},
]

[
Pe_h=\frac{\text{thermal convection}}{\text{axial heat conduction}},
]

[
\Lambda=\frac{\text{adsorption heat release}}{\text{bed sensible heat scale}}.
]

The study plan uses the same governing groups: (Pe) for convective versus dispersive transport, (NTU) or (Da) for mass-transfer rate versus residence time, (\alpha) for solid/gas capacity, and (\Lambda) for heat-feedback strength. 

The first exact limit is the **isothermal local-equilibrium limit**:

[
T=T_0,\qquad D_L=0,\qquad k\to\infty.
]

Then

[
q=Q(c)=q^*(c,T_0).
]

The mass balance becomes

[
\varepsilon c_t+u c_z+\alpha_bQ'(c)c_t=0,
]

or

[
\boxed{
\frac{\partial}{\partial t}
\left[
\varepsilon c+\alpha_b Q(c)
\right]
+
u\frac{\partial c}{\partial z}
==============================

0.

}
]

Define the total equilibrium inventory

[
m(c)=\varepsilon c+\alpha_bQ(c).
]

Since (Q'(c)>0), (m(c)) is invertible. The conservation law can be written as

[
m_t+F(m)_z=0,
]

with

[
F(m)=u c(m).
]

For a feed step from (c=0) to (c=c_f), the Rankine–Hugoniot speed is

[
v_{\mathrm{RH}}
===============

\frac{F(m_f)-F(m_0)}{m_f-m_0}.
]

Since

[
m_f=\varepsilon c_f+\alpha_bQ(c_f),
\qquad
m_0=0,
]

and

[
F(m_f)=uc_f,\qquad F(m_0)=0,
]

we obtain

[
\boxed{
v_{\mathrm{RH}}
===============

\frac{u c_f}
{\varepsilon c_f+\alpha_bQ(c_f)}.
}
]

Therefore the ideal stoichiometric breakthrough time is

[
\boxed{
t_{\mathrm{st}}
===============

# \frac{L}{v_{\mathrm{RH}}}

\frac{L\left[\varepsilon c_f+\alpha_bQ(c_f)\right]}{u c_f}.
}
]

This is the cleanest analytical solution of the mechanistic model. It is not the full breakthrough curve; it is the ideal sharp-front breakthrough time.

The second exact limit is the **linear-isotherm local-equilibrium limit**:

[
Q(c)=Kc.
]

Then

[
q=Kc.
]

The dispersive mass balance becomes

[
\varepsilon c_t+u c_z
=====================

## \varepsilon D_Lc_{zz}

\alpha_bKc_t.
]

So

[
(\varepsilon+\alpha_bK)c_t+u c_z
================================

\varepsilon D_Lc_{zz}.
]

Divide by (\varepsilon+\alpha_bK):

[
\boxed{
c_t+v_{\mathrm{eff}}c_z
=======================

D_{\mathrm{eff}}c_{zz},
}
]

where

[
\boxed{
v_{\mathrm{eff}}
================

\frac{u}{\varepsilon+\alpha_bK},
}
]

and

[
\boxed{
D_{\mathrm{eff}}
================

\frac{\varepsilon D_L}{\varepsilon+\alpha_bK}.
}
]

For a semi-infinite column with step inlet (c(0,t)=c_f), clean initial condition, and (z>0), the Ogata–Banks form is

[
\boxed{
\frac{c(z,t)}{c_f}
==================

\frac12
\operatorname{erfc}
\left(
\frac{z-v_{\mathrm{eff}}t}{2\sqrt{D_{\mathrm{eff}}t}}
\right)
+
\frac12
\exp\left(\frac{v_{\mathrm{eff}}z}{D_{\mathrm{eff}}}\right)
\operatorname{erfc}
\left(
\frac{z+v_{\mathrm{eff}}t}{2\sqrt{D_{\mathrm{eff}}t}}
\right).
}
]

This is the natural Gate-A-style analytical test after adsorption has been reduced to a linear retarded transport problem.

The third useful analytical result is the travelling-wave reduction. Myers and Font show that after the initial transient, a travelling-wave coordinate can be introduced and the breakthrough problem can be solved in moving-front form; they specifically compare numerical and travelling-wave results for column sorption.  Their travelling-wave development leads to outlet breakthrough expressions and shows why not every fixed-bed model requires full numerical solution in every limit. 

For the **full nonlinear non-isothermal finite-(k) model**, however, there is no general closed-form solution. The reasons are:

[
q^*=q^*(c,T),
]

so the kinetic source depends on both concentration and temperature;

[
(-\Delta H)=(-\Delta H)(T,q)
]

may vary with loading and temperature;

the heat equation feeds back into the mass equation through (q^*(c,T));

and axial dispersion/conduction make the system parabolic-relaxation rather than a scalar conservation law.

Danilov et al. use LDF kinetics and heat-of-adsorption terms in a non-isothermal axial-dispersion model, but still close the coupled concentration/temperature calculation numerically after analytical simplification.  The roadmap also states that stiff solvers such as BDF or LSODA are appropriate once temperature coupling, sharp fronts, and fast LDF kinetics are included. 

For Method of Lines, define grid points

[
z_i=i\Delta z,\qquad i=0,\ldots,N-1.
]

Let

[
c_i(t)\approx c(z_i,t),\qquad q_i(t)\approx q(z_i,t),\qquad T_i(t)\approx T(z_i,t).
]

For interior nodes, use

[
(\delta_z^- c)*i=\frac{c_i-c*{i-1}}{\Delta z}
]

for upwind convection, and

[
(\delta_{zz}c)*i=\frac{c*{i+1}-2c_i+c_{i-1}}{\Delta z^2}
]

for axial dispersion. Similarly for (T).

Then

[
\boxed{
\frac{dq_i}{dt}
===============

k\left(q^*(c_i,T_i)-q_i\right).
}
]

The concentration equation becomes

[
\boxed{
\frac{dc_i}{dt}
===============

\frac{
\varepsilon D_L(\delta_{zz}c)_i
-------------------------------

## u(\delta_z^-c)_i

\alpha_b,dq_i/dt
}{\varepsilon}.
}
]

The energy equation becomes

[
\boxed{
\frac{dT_i}{dt}
===============

\frac{
\lambda_{\mathrm{eff}}(\delta_{zz}T)_i
--------------------------------------

u\rho_gc_{p,g}(\delta_z^-T)_i
+
\alpha_b(-\Delta H_i),dq_i/dt
-----------------------------

\frac{4h_w}{d_{\mathrm{col}}}(T_i-T_{\mathrm{wall}})
}{C_h}.
}
]

The ODE state is

[
\boxed{
y(t)=
[c_0,\ldots,c_{N-1},q_0,\ldots,q_{N-1},T_0,\ldots,T_{N-1}]^T.
}
]

So

[
\boxed{
\frac{dy}{dt}=f(t,y).
}
]

For the inlet, either impose Dirichlet values

[
c_0(t)=c_f,\qquad T_0(t)=T_f,
]

or use finite-volume Danckwerts fluxes. For the outlet,

[
c_z(L,t)=0,\qquad T_z(L,t)=0,
]

which can be implemented by ghost cells

[
c_N=c_{N-1},\qquad T_N=T_{N-1}.
]

This is exactly the structure in the project study plan’s Python scaffold: gas mass balance, LDF solid balance, gas/solid energy balances, Toth closure, clean-bed initial state, inlet step, and Rankine–Hugoniot shock-speed check. 

The model outputs should be defined from the outlet trace (c(L,t)):

[
\boxed{
t_{\mathrm{BT}}
===============

\inf\left{t:\frac{c(L,t)}{c_f}=0.05\right},
}
]

[
\boxed{
t_{\mathrm{sat}}
================

\inf\left{t:\frac{c(L,t)}{c_f}=0.95\right}.
}
]

The dynamic capacity is

[
\boxed{
q_{\mathrm{dyn}}
================

\frac{1}{(1-\varepsilon)\rho_pL}
\int_0^{t_{\mathrm{BT}}}
u\left[c_f-c(L,t)\right]dt.
}
]

The study plan uses the same response metrics: breakthrough time, saturation time, MTZ width, dynamic adsorption capacity, front velocity, and mass-balance drift. 

The final validation ladder should be:

1. **No adsorption:** set (q=0), (k=0), and solve advection-dispersion. Compare with the analytical step solution.
2. **Isothermal equilibrium shock:** set (T=T_0), (D_L\to0), (k\to\infty), and verify

[
v_{\mathrm{front}}\approx v_{\mathrm{RH}}.
]

3. **Finite LDF isothermal model:** verify that larger (Da=kL/u) sharpens the front and approaches the Rankine–Hugoniot limit.
4. **Full non-isothermal model:** compare (t_{\mathrm{BT}}), outlet curve shape, and temperature excursion against the benchmark.
5. **Inventory check:** verify

[
\frac{
\left|
\text{CO₂ in}
-------------

## \text{CO₂ out}

\Delta\text{bed inventory}
\right|
}{
\text{CO₂ in}
}
\ll 1.
]

The project validation protocol already sets this philosophy: first validate linear advection-diffusion, then the nonlinear isothermal front speed, then the full non-isothermal breakthrough curve. 

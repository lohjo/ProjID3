[Computers and Chemical Engineering 204 (2026) 109379](https://doi.org/10.1016/j.compchemeng.2025.109379)


Contents lists available at ScienceDirect
# Computers and Chemical Engineering


[journal homepage: www.elsevier.com/locate/compchemeng](https://www.elsevier.com/locate/compchemeng)

## Optimization of direct air capture processes using reactive transport models of adsorption-desorption cycles

Hector A. Pedrozo [a], Mayra G. Gonzalez-Ramirez [a], Tiras Y. Lin [b], Thomas Moore [c],
Thomas Roy [b], Du T. Nguyen [b], Pratanu Roy [b], Sarah Baker [b], Lorenz T. Biegler [a],
Grigorios Panagakos [a][,][*]

a _Chemical Engineering Department, Carnegie Mellon University, Pittsburgh, PA 15213, USA_
b _Lawrence Livermore National Laboratory, Livermore, CA 94550, USA_
c _School of Mechanical, Medical and Process Engineering, Queensland University of Technology, Brisbane, 4000, Australia_



A R T I C L E I N F O


_Keywords:_
Direct air capture
CFD
Carbon capture
Process optimization
Adsorption-desorption process


**1.** **Introduction**



A B S T R A C T


In this study, we develop and implement a reactive transport model in COMSOL Multiphysics® to address the
challenges of direct air carbon capture. The model is validated against experimental data and used to simulate
the cyclic steady state of the adsorption-desorption process. The optimization of this model is achieved through
advanced trust-region methods integrated with Gaussian Processes. Key decision variables, including adsorption
and desorption times, desorption temperature and pressure, input velocity, bed porosity, column length, and
radius were optimized to minimize the capture cost. After optimization, a sensitivity analysis revealed the
complex interplay between the decision variables and their effect on the specific energy and cost of removing the
CO2. We optimized the capture cost while taking into account the trade-off between energy consumption and
productivity. The resulting minimum capture cost was determined to be 265.2 $/t-CO2, which aligns with ex­
pected values reported in the literature. Numerical results suggest the effectiveness of the optimization strategies
applied, and underscore the importance of simultaneous decision variable selection in improving the perfor­
mance in direct air capture processes.

We also extend the modeling approach to a 2D axisymmetric model to better visualize CO₂ uptake and
temperature profiles, revealing significant radial gradients during the regeneration step. As a main drawback,
this enhanced model comes with a computational cost approximately 40 times higher than that of the 1D model.



Climate change is one of the most urgent challenges of the 21st
century, driven primarily by the increased atmospheric concentration of
Greenhouse Gases (GHG). Despite international efforts, such as the Paris
Agreement, aiming to reduce the global temperature increase below 2 [◦] C
with respect to the pre-industrial era, substantial progress remains to be
achieved. By 2020, the global mean temperature had already increased
by approximately 1 [◦] C, highlighting the need for more aggressive and
innovative solutions to reduce GHG emissions and mitigate the impacts
of climate change (McQueen et al., 2021). Likewise, according to the
Intergovernmental Panel on Climate Change (IPCC), CO2 concentration
has had its highest increase since 2 million years ago, with a value of 424
ppm in 2020 compared to 315 ppm in 1960.

Currently, several actions are being undertaken, such as an increase


 - Corresponding author.
_E-mail address:_ [gpanagak@andrew.cmu.edu](mailto:gpanagak@andrew.cmu.edu) (G. Panagakos).



in the use of low-carbon and renewable energy and the use of alternative
fuels (e.g., biofuels, hydrogen), among others. Carbon Dioxide Removal
(CDR) has recently gained attention as an essential strategy for
achieving net-negative CO2 emissions, by removing CO2 from the at­
mosphere (Chauvy and Dubois, 2022), through natural or man-made
pathways. CDR technologies can be integrated into a range of eco­
nomic sectors, especially those reliant on power plants or hard-to-abate
industries. Simultaneously, Carbon Capture, Utilization, and Storage
(CCUS) is increasingly recognized as an indispensable pillar for miti­
gating further CO2 emissions. Nevertheless, even with all Carbon Cap­
ture Technologies operating at their maximum capacity, removing CO2
from the air remains an important step towards restoring climate bal­
ance. According to the National Academies of Sciences, Engineering,
and Medicine (NASEM), to meet our environmental goals, 10 billion
metric tons per year (GtCO2 yr [−] [1] ) must be removed directly from the
atmosphere globally by 2050 (Pacala et al., 2018).



[https://doi.org/10.1016/j.compchemeng.2025.109379](https://doi.org/10.1016/j.compchemeng.2025.109379)
Received 12 February 2025; Received in revised form 25 August 2025; Accepted 27 August 2025

Available online 28 August 2025
[0098-1354/© 2025 The Authors. Published by Elsevier Ltd. This is an open access article under the CC BY-NC-ND license ( http://creativecommons.org/licenses/by-](http://creativecommons.org/licenses/by-nc-nd/4.0/)
[nc-nd/4.0/ ).](http://creativecommons.org/licenses/by-nc-nd/4.0/)


_H.A. Pedrozo et al.                                                                                                               Computers_ _and_ _Chemical_ _Engineering_ _204_ _(2026)_ _109379_



Direct Air Capture (DAC) is one of the most relevant CDR alternatives
due to its potential for large-scale deployment, enabling the removal of
significant amounts of atmospheric CO₂ (Abdullatif et al., 2023; Bose
et al., 2024). It consists of chemical processes designed to extract
low-concentration CO2 directly from the atmosphere. The most
advanced DAC techniques rely on solid sorbents, liquid alkanolamine, or
aqueous alkaline absorbents. The last two options are solvent-based
technologies with high energy demand at high temperatures (Liu
et al., 2023; McQueen et al., 2021). These present a major downside:
they depend on heat generated traditionally by fossil fuels, which often
makes the capture process carbon-intensive. On the other hand, solid
sorbents exhibit lower heat needs, and waste heat produced in industries
can be integrated to offer the energy needed (Baker et al., 2024). The
scalability of DAC technologies is another major challenge. Current
research is more focused on sorbent material development instead of





scalability through detailed modeling and process-level analysis.
Therefore, there is a need for more research at the device design, process
modeling, and optimization levels. This is especially true as the cyclic
nature of the solid sorbent-based processes normally involves periodic
CO2 adsorption and subsequent regeneration of the adsorbent.

Cyclic adsorption-desorption processes are an inherent part of the
operations involved in DAC. One of the challenges of cyclic technologies
is to determine conditions where the periodic behavior of the system
stabilizes. The importance of designing cyclic systems in adsorption
processes cannot be overestimated, as it seriously affects the economic
performance of the separation system (Pacala et al., 2018). Most of the
early work in cyclic adsorption systems has been done on pressure swing
adsorption (PSA) and temperature swing adsorption (TSA) methods,
which are being adapted for application to DAC. Pressure Swing
Adsorption (PSA) relies on changing the pressure to switch between the









2


_H.A. Pedrozo et al.                                                                                                               Computers_ _and_ _Chemical_ _Engineering_ _204_ _(2026)_ _109379_



adsorption and desorption phases. PSA has been widely used in indus­
trial gas separation (Dowson et al., 2016). It has been previously studied
for carbon capture where, due to the large scale of the application,
process optimization is of major importance in improving energy effi­
ciency and increasing capture rates (Hughes et al., 2024b, 2024a).
Nevertheless, air pressurization for processes with diluted species, such
as CO2 in the air, would require a large amount of energy, given the low
partial pressure of CO2, while regeneration at vacuum pressures would
operate the adsorption step at very low and non-practical levels of
vacuum (Bouaboula et al., 2024). Temperature Swing Adsorption (TSA)
is one of the most extensively studied DAC technologies. It operates as a
cyclic process that leverages temperature changes to facilitate the
adsorption of CO₂ onto a sorbent during the capture phase and its sub­
sequent release during the regeneration phase. Typically, TSA uses
materials like metal-organic frameworks (MOFs) (Balasubramaniam
et al., 2024; Hughes et al., 2021; Ji et al., 2023; Sinha et al., 2016; Tao
and Xu, 2024) or amine-functionalized adsorbents (Al-Absi et al., 2024;
Baamran et al., 2025; Muldoon et al., 2025; Surkatti et al., 2025), which
exhibit a high affinity for CO₂ at lower temperatures. TSA typically
operates at ambient temperature (25 [◦] C) during the adsorption phase
and increases to 50–90 [◦] C for the regeneration phase, with some con­
figurations reporting temperatures up to 130 [◦] C (Priyadarshini et al.,
2023; Rezo et al., 2024). On the other hand, DAC is still considered an
emerging approach, with important challenges like reducing energy
requirements and costs, scalability, and efficiency (Bose et al., 2024). In
this context, Stampi-Bombelli et al. (2020) analyzed the efficiency of
TSA for DAC, in terms of adsorption capacity and energy requirements,
underscoring the importance of selecting suitable adsorbents.

Vacuum-assisted methods for DAC, such as Vacuum Swing Adsorp­
tion (VSA), operate by reducing the pressure in the adsorption system,
facilitating CO₂ desorption. These methods are often combined with TSA
to improve overall efficiency. Postweiler et al. (2024) explored the po­
tential of PSA, TSA, and their combination (Temperature Vacuum Swing
Adsorption, TVSA) for reducing cost and emissions, and Ward et al.
(2024) performed an analysis of a multi-step process combined with PSA
and TVSA.

Cyclic DAC processes are usually represented by 1D dynamic models,
considering complex thermodynamics and kinetic models (Ji et al.,
2023; Liu et al., 2023; Murali et al., 2013; Schellevis et al., 2024, 2021).
A suitable model selection plays a crucial role in accurately describing
and predicting DAC systems adsorption mechanisms, both in dry and
humid conditions. For instance, CO₂ adsorption in DAC typically occurs
via two main approaches: chemisorption, involving strong chemical
interactions, and physisorption, which is governed by weaker van der
Waals forces. Additionally, the simultaneous adsorption of H₂O signifi­
cantly influences the overall behavior, as water can compete with or
enhance CO₂ uptake depending on the sorbent material and environ­
mental conditions (Ruthven, 1984).

The adsorption equilibrium of CO2 on the different array of sorbent
materials, such as polypropylene resin, polystyrene, aminefunctionalized silica, and zeolites, is usually estimated using isotherm
models (Balasubramaniam et al., 2024; Darunte et al., 2016; Holewinski
et al., 2017; Ji et al., 2023; Jue et al., 2024). One of the standard iso­
therms used to describe adsorption onto silica and cellulose is the Toth
isotherm. This is an empirical extension of the Langmuir isotherm that
improves the fit for high and low-pressure ranges (Young et al., 2021).
Authors like Hefti and Mazzotti (2014) have used a typical Type III
isotherm to describe unrestricted monolayer-multilayer adsorption of
the water in favorable sites of microporous adsorbents.

Another widely used isotherm for these interactions is the
Guggenheim–Anderson–de Boer (GAB) model, which is an extension of
the widely utilized Brunauer–Emmett–Teller (BET) equation. The BET
isotherm assumes that the heat of adsorption for the first layer differs
from that of all subsequent layers, with the last being equal to the latent
heat of condensation. In contrast, the GAB model refines this assumption
by proposing that only the 10th and subsequent sorbent material layers



have a heat of adsorption equal to the latent heat of condensation, while
the 2nd to 9th layers exhibit a heat of adsorption distinct from that of the
first layer (Quirijns et al., 2005; Young et al., 2021). Other recent ap­
proaches for general sorption-desorption systems include a triple-mode
model that adds a pooling term to the traditional Henry-Langmuir
dual-mode approach (Castonguay et al., 2023) and analytical solutions
for the Langmuir isotherm concentration, which, for complex CFD
simulations, has the potential to avoid using computationally expensive
ordinary differential equation solvers during the iterative solution pro­
cedure (Roy et al., 2022).

To accurately model water effects, we employed the GuggenheimAnderson-de Boer (GAB) isotherm for its proven efficacy in character­
izing multilayer adsorption phenomena, capturing the intricacies of
surface interactions and material heterogeneity. This model enables a
robust and detailed analysis of adsorption mechanisms across the sor­
bent material. By integrating these approaches, our work establishes a
solid framework for optimizing DAC processes.

Given the need for the development of DAC technologies, CFD sim­
ulations are gaining importance for optimizing equipment and process
designs as well as operational efficiency. CFD provides detailed insights
into fluid behavior, heat transfer, and physicochemical interactions.
Some modeling work has been done at a process level, targeting the
reduction of the energy footprint and the operational cost
(Balasubramaniam et al., 2024; Ward et al., 2024). Nevertheless, a ho­
listic approach is still missing, where mathematical optimization is
applied to data from the CFD simulations. Optimization applications,
which have the potential to achieve commercial scale along these lines,
include airflow/fan optimization, such as the work done by the Multi­
phase Low Analysis Laboratory group at the National Energy Technol­
ogy Laboratory (NETL) (Huckaby, 2022), and the design of sorbent
structures that contribute to the optimal flow inside the adsorption
equipment (National Energy Technology Laboratory, 2023).

Coupling first-principles models of transport mechanisms, including
heat, momentum, and mass transfer, is important to elucidate the
complex and often non-intuitive interactions between them. CFD models
have already been shown to contribute significantly to carbon capture
technologies like membranes (Dosso et al., 2025; Rivero et al., 2023)
and absorption (Shah et al., 2025). Process optimization and Multi­
physics models have been successfully used and have offered significant
insights for designing better structures and processes (Pedrozo et al.,
2024a, 2024b; Rivero et al., 2020; Singh et al., 2019, 2022; Sun et al.,
2022, 2024). In terms of technology scaling-up, non-dimensional
numbers have proven to be effective in conveying the interplay of the
physics involved and making the transition between scales more work­
able (for example, from lab to pilot or from pilot to commercial size), as
demonstrated by Lin et al. (2024). Sun et al. (2024) use non-dimensional
numbers in the formulation and metrics of hollow fiber membranes for
CO2 capture from concentrated sources. In terms of process optimization
leveraging CFD models through machine learning and surrogate model
implementations, Pedrozo et al. (2024c, 2024b) have applied a trust
region filter method for the multi-scale process optimization of carbon
capture, using hybrid solvent-permeator hollow fiber membrane con­
tactors. The integration of CFD simulations, optimization techniques,
and surrogate models offers significant potential for achieving low-cost,
commercial-scale implementation of DAC systems. This approach en­
ables the identification of optimal process conditions by leveraging
detailed insights from reactive transport simulations while maintaining
computational efficiency (Agarwal et al., 2010).

In this work, we propose a holistic approach to model and optimize
DAC using TVSA systems. The study begins with the implementation of a
reactive transport model to analyze the cyclic steady-state behavior of
the DAC process. The coupled diffusion-sorption-advection model and
its implementation in COMSOL Multiphysics® are described in Section
2. The interplay among physical processes leads to highly coupled var­
iables, which give a suitable representation of the process. In Section 3,
we introduce the optimization framework and case studies, which



3


_H.A. Pedrozo et al.                                                                                                               Computers_ _and_ _Chemical_ _Engineering_ _204_ _(2026)_ _109379_



include different cost and humidity scenarios for optimization analyses
based on the minimization of the capture cost. Given the complexity of
the model, reactive transport simulation data is employed to train sur­
rogate models, specifically Gaussian processes, which facilitate optimi­
zation using advanced trust-region methods as described in the
Supplementary Material.

In Section 4, we present the results, including model validation,
optimization of the case studies, and sensitivity analyses. We analyze the
values of decision variables that minimize the capture cost for a base
case. Once the optimal process is obtained, sensitivity analyses are
conducted around this point to quantify the effect of each decision
variable, where the ranges are defined on a case-by-case basis. Addi­
tionally, in Section 4, we address optimization scenarios under varying
humidity conditions and capital cost factors, to capture the effect of
broader operational ranges. In Section 5 we expand the modeling
approach to include a 2D axisymmetric model. This model allows us to
visualize the radial gradients during the adsorption and regeneration
steps, providing valuable insights into the heating process within the
bed. To the best of our knowledge, this is the first work to present a
holistic computational framework of a coupled reactive transport CFD
model of the cyclic steady-state DAC system, tethered to a trust-region
optimization implementation for an optimized DAC process and pass­
ing information from the former to the latter through Gaussian
Processes.


**2.** **Process description**


The temperature-vacuum swing adsorption (TVSA) cycle was used to
tackle the direct air capture (DAC) process (Gholami et al., 2023). By
combining vacuum and temperature, this method enhances the cyclic
capacity, enabling more efficient use of the solid sorbent. The modeled
adsorption cycle consists of separate steps for adsorption, evacuation,
heating/regeneration, pressurization, and cooling as shown in Fig. 1.

In the adsorption step, we use a fan to generate airflow through the
adsorption bed. CO2 in this stream is selectively adsorbed in the solid,
while the water is also adsorbed. This step continues for a prescribed
time called the adsorption time. This is an important decision variable to
improve the performance of the process since it introduces an important
tradeoff; on the one hand, extending this time increases the uptake of
adsorbed CO2 but on the other hand, it also increases energy con­
sumption from the fan.

The next step is the evacuation, where we stop the airflow with the
fan, while we impose vacuum pressure at the exit by using a vacuum



pump. In this way, we generate a pressure-driven flow in the packed
bed. In this step, we purge the gas in the bed from its high N2 content.
Pressure changes in the bed happen relatively fast, so it is anticipated
that the time associated with this step will not have an important impact
on the cycle design.

During the heating/regeneration step, we impose a high temperature
on the wall of the packed bed. Since the presented model is 1D, the heat
transfer phenomenon is represented by using an effective radial heat
transfer coefficient. As the temperature of the bed rises, the adsorption
equilibrium shifts, releasing the adsorbed CO2 from the solid particles.
The time associated with this step is also a relevant optimization vari­
able. The duration of this step should be sufficiently long to achieve a
CO2 uptake near the equilibrium state. In this regard, the regeneration
temperature also plays an important role since it controls the equilib­
rium conditions.

After the regeneration step, we initiate the cooling process by
imposing a low temperature on the wall. As it is expected to operate this
process step with cooling water, we consider a temperature of 25 [◦] C. In
order to avoid significant degradation of amine-functionalized adsor­
bents, we start the pressurization when the mean temperature of the bed
is below 60 [◦] C. In this step, we change the pressure condition at the top
of the fixed bed, from a low value to a high one (atmospheric pressure).
Consequently, airflow due to the pressure difference is generated, until
we achieve a mechanical equilibrium. We start the adsorption pressure
again by imposing an airflow when the mean temperature of the bed is
40 [◦] C. The times associated with the cooling and pressurization steps are
not expected to have a significant impact on the process performance.
The adsorption step is reinitiated following the cooling and pressuriza­
tion steps, with airflow imposed once the mean bed temperature reaches
40 [◦] C.


_2.1._ _Process modeling_


The operation of the process is modeled by solving mass, energy, and
momentum balances for one column that undergoes the cycle steps
sequentially. The problem results in a system of coupled, partial dif­
ferential equations (PDE). To tackle this problem in an efficient manner,
Computational Fluid Dynamics (CFD) models enable a set of tools for the
study of hydrodynamic characteristics, mass, and heat transfer phe­
nomena (Shah et al., 2025). In this work, we develop a 1D model for
fixed-bed adsorbent beds, including relevant physics to describe the
separation process. With the aim of reducing the model complexity, the
following assumptions are made, as suggested in the literature



**Fig. 1.** Adsorption cycle for direct-air carbon capture.


4


_H.A. Pedrozo et al.                                                                                                               Computers_ _and_ _Chemical_ _Engineering_ _204_ _(2026)_ _109379_



(Luukkonen et al., 2023; Sidhareddy et al., 2023):


 - Constant material properties for an amine-functionalized resin
(isotropic fixed bed).

 - Ideal gas behavior for air and its components and NRTL model for
water.

 - Deactivation processes for the adsorption material are negligible.

 - Constant mass transfer coefficient for water.

 - Heat transfer phenomena are described by an effective radial heat
transfer coefficient.

 - Negligible temperature radial gradients.

 - Gas flow within column, represented as an axially dispersed plug
flow with no radial concentration, temperature, or pressure
gradients.

 - Only considered adsorption of CO2 and H2O.

 - Constant gas velocity during adsorption.

 - Gas and solid phases in thermal equilibrium.

 - Uniform wall temperature along axial and radial directions.

 - Uniform and homogeneous adsorbent packing.


During desorption, gas velocity is calculated using a proportional
controller based on the difference between total pressure and vacuum
pressure. It should be emphasized that an effective radial heat transfer
coefficient is assumed for heat transfer phenomena in the 1D model,
neglecting the effects of temperature gradients. To assess the impact of
this assumption, we compare the simulation outcomes from both the 1D
and 2D axisymmetric modeling approaches in Section 5.


_2.2._ _Governing equations_


The governing equation for mass transfer of the different species in



_∂qi_



_i_ _i_ (3)

_∂_ ~~_t_~~ _[M][w]_



_Sm_ = (1 − _ε_ ) _ρp_



_i_ ={ _CO_ 2 _,H_ 2 _O_ }



∑



where _M_ _[w]_ _i_ [is the molecular weight of species ] _[i][.]_
On the other hand, the extended Darcy’s law, alternatively known as
Ergun’s equation, is shown in Eq. (4), where ̂ **z** is the unit vector along
the z longitudinal axis. In this context, the permeability, defined in Eq.
(5), and the inertial coefficient _β_, defined in Eq. (6) are functions of
porosity ( _ε_ ) and the particle diameter ( _dp_ ) (Amiri et al., 2019).

- _[∂]_ _∂_ _[P]_ ~~_z_~~ [̂] _**[z]**_ [=] _[ κ]_ _[μ][v]_ _**[u]**_ [ +] _[ β]_ _[ρ][g]_ [|] _**[u]**_ [|] _**[u]**_ (4)



_ε_ [3]

(5)
(1 − _ε_ ) ~~[2]~~


(1 − _ε_ )

(6)
_ε_ [3]



_κ_ =



_d_ [2] _p_
~~150~~



_ε_ [3]



_β_ = [1] _[.]_ [75]
~~_d_~~ _p_



(1 − _ε_ )



It should be noted that the continuity Eq. (2) and extended Darcy’s
law (4) describe the fluid behavior under the different stages of the
adsorption cycle where the boundary conditions are the only changes.
While a fixed velocity is imposed during the adsorption process to feed
air to the process, a given pressure is imposed during the desorption
process through a vacuum pump. In the last process, the CO2 desorption
promotes local density increase, generating pressure-driven flow.

The energy balance accounts for an effective internal heat transfer
and diffusion along the axial direction of the bed, heat of adsorption, and
heat transfer between the bed and column wall. These physical processes
are described by the following governing equation:




[

_ρgcp,g_ + [1][ −] _[ε]_ ~~_ρ_~~ _p_
_ε_




[



(
_cp,s_ + _cp,CO_ 2



(
_q_ [1] _CO_ 2 [+] _[ q]_ _CO_ [2] 2



)
+ _cp,H_ 2 _OqH_ 2 _O_



) []]
_∂T_



_∂_ ~~_t_~~ [=]



_∂q∂_ [1] _CO_ ~~_t_~~ 2 - Δ _H_ 2 _∂q∂_ [2] _CO_ ~~_t_~~ 2 - Δ _HH_ 2 _O_



( _T_ - _Tw_ )



_∂qH_ 2 _O_

_∂_ ~~_t_~~



1 − _ε_
~~_ρ_~~ _p_
_ε_




[

  - Δ _H_ 1



] 2 _h_
+ _Kz_ ∇ [2] _T_ - _ρgcp,g_ _**u**_ ⋅∇ _T_ _ε_ ~~_R_~~ _C_



(7)



the packed bed adsorber is described by the following expression:



_ε_ _[∂][c][i]_

_∂_ ~~_t_~~ [=] _[ D][L]_ [∇][2] _[c][i]_ [ −] _[u]_ [⋅][∇] _[c][i]_ [ −(][1][ −] _[ε]_ [)] _[ρ][p]_



_∂qi_

(1)
_∂_ ~~_t_~~



where _cp,g_, _cp,s_, _cp,CO_ 2 and _cp,H_ 2 _O_ are the specific heats of the gas, the solid
sorbent, the CO2 and the water, respectively, _q_ [1] _CO_ 2 [, ] _[q]_ _CO_ [2] 2 [are the uptakes ]
due to the dry and the humid adsorption mechanisms (as we explain
below); Δ _H_ 1, Δ _H_ 2 are the adsorption heats for the CO2 adsorption
considering the dry and the humid mechanism, _qH_ 2 _O_ is the water uptake
of the solid adsorbent; Δ _HH_ 2 _O_ is the adsorption heat associated with
water; and _RC_ is the column radius.

It is also highlighted that we consider the ideal gas equation of state
to determine the properties of the gas phase based on the pressure and
temperature of the system. Consequently, _ρg_ from Eq. (2), the pressure
from Eq. (4), and the temperature from Eq. (7) are inherently related
through this equation of state.


_2.3._ _Process kinetics of the co-adsorption of CO2_ _and water_


Including water in the modeling of CO2 adsorption using solid sor­
bents is critical due to its significant impact on the adsorption process,
particularly in amine-functionalized adsorbents where water stabilizes
the zwitterion formation during CO2 capture (Mariniˇc and Likozar,
2023). Water co-adsorption can have both beneficial and unfavorable
effects (Ji et al., 2024). For instance, it may increase the heat required
for sorbent regeneration or accelerate degradation in materials like
metal-organic frameworks (MOFs). However, in many cases, the pres­
ence of humidity can enhance CO2 uptake capacity, improving overall



where _ci_ is the concentration of species _i_, _ε_ is the porosity, _t_ is the time,
_DL_ is the dispersion coefficient, _u_ is the flow velocity, _ρp_ is the density of
the particle, and _qi_ is the uptake of species _i_ by the sorbent. It should be
noted that we have used Fick’s law to describe the diffusion fluxes of
chemical species.

To determine the velocity distribution, we need to consider
compressible flow in the fixed bed adsorber, as described by the nonDarcian flow in the Darcy’s law physics package of COMSOL (Comsol
Multiphysics, 2020). This physics includes the continuity equation, as
shown in Eq. (2).



_ε_ _[∂ρ]_ _∂_ ~~_t_~~ _[g]_ [+ ∇][⋅] ( _uρg_



)
= _Sm_ (2)



where _ρg_ is the density of the fluid (gas) phase; _Sm_ is the source term due
to CO2 adsorption/desorption in the domain. The constitutive relation
for the source term _Sm_ is defined in Eq. (3). The mass generation is
associated with the adsorption reaction of the different chemical species,
which promotes changes in the density and pressure of the fluid mixture.



5


_H.A. Pedrozo et al.                                                                                                               Computers_ _and_ _Chemical_ _Engineering_ _204_ _(2026)_ _109379_



performance. Despite this, the majority of existing models neglect the
interaction between water and CO2 (Mariniˇc and Likozar, 2023),
focusing solely on dry processes or using simplified, empirical ap­
proaches. Accurate modeling of water effects requires advanced iso­
therms, such as the Guggenheim–Anderson–de Boer (GAB) isotherm
(Quirijns et al., 2005), to describe water adsorption equilibrium as a
function of relative humidity. Given the complex interactions between
CO2 and H2O in multicomponent systems, a co-adsorption model is
essential for predicting performance under realistic, humid conditions,
and for optimizing sorbent design and regeneration strategies in carbon
capture technologies.

The corresponding kinetic reactions for the co-adsorption of CO2 and
water are shown in Eqs. (8)-(11), based on Luukkonen et al. (2023). The
adsorption of CO2 in amine-functionalized adsorbents occurs consid­
ering two mechanisms: dry conditions ( _q_ [1] _CO_ 2 [) and in the presence of ]

water ( _q_ [2] _CO_ 2 [). The total CO][2 ][uptake (] _[q][CO]_ 2 [) is the sum of both mechanisms. ]
In the case of the water uptake, we consider a linear driving force (LDF)
model, as shown in Eq. (11). In the LDF model, the rate of change of the
adsorbed amount is assumed to be proportional to the driving force,
defined as the difference between the equilibrium concentration and the
current uptake on the solid. The model also assumes a constant mass
transfer coefficient, ignoring any dependency of the adsorption rate on
variables such as water concentration.



_Evac_ = [1]

_ηvac_



_γ_
( ~~1~~ - _γ_ )



_2.4._ _Performance metrics_


The performance of direct air capture systems can be evaluated
based on different performance metrics, including specific energy con­
sumption (SEC) and process productivity. SEC is a relevant process in­
dicator since it is related to the operating cost (OPEX) of the process as
well as the potential CO2 emissions associated with the production of
this energy. This metric was calculated based on the definition of Eq.
(17).



_SEC_ =



( )
_Efan_ + _Evac_ + _Eheat_

~~_m_~~ _CO_ 2 _,product_



(17)



where _Efan_ is the fan energy for the adsorption step; _Evac_ is the energy
associated with the vacuum pump; and _mCO_ 2 _,product_ is the amount of CO2
capture per cycle. _Efan_, _Evac_ and _Eheat_ are calculated based on the Eqs.
(18)-(20).



∫ _[t][ads]_ 1
_Efan_ =

_ηfan_

0



Δ _Pufeeddt_ (18)



)

- 1 _dt_ (19)



~~)~~ _[γ]_ [−] [1]
_γ_



_tads_ ∫+ _tdes_


_tads_



_n_ ˙ _out,totalRT_ (( _Pads_

~~_P_~~ _des_



_∂q∂_ [1] _CO_ ~~_t_~~ 2 = _kf_ 1

_∂q∂_ [2] _CO_ ~~_t_~~ 2 = _kf_ 2



(

~~_q_~~ _CO_ 2 - 2 _q_ [1] _CO_ 2 [−] _[q]_ _CO_ [2] 2



(



_pCO_ 2 - _[k][f]_ [1]

~~_b_~~ 1



_pCO_ 2 - _[k][f]_ [1]



~~_q_~~ [1] _CO_ 2 (8)



_j_



_tads_ ∫+ _tdes_


_tads_




- Δ _Hj_ ˙ _njdt_ (20)



~~_q_~~ [2] _CO_ 2 (9)



(

~~_q_~~ _CO_ 2 - 2 _q_ [1] _CO_ 2 [−] _[q]_ _CO_ [2] 2



(



)3


)3



_pCO_ 2 _pH_ 2 _O_ - _[k][f]_ [2]

~~_b_~~ 2



_pCO_ 2 _pH_ 2 _O_ - _[k][f]_ [2]



( ) ∑
_mi,descp,i_ Δ _T_ +



∑(
_Eheat_ = _ms_ _cp,s_ Δ _T_ +



_i_



_∂qCO_ 2 = _[∂][q]_ _CO_ [1] 2 + _[∂][q]_ _CO_ [2] 2 (10)

_∂_ ~~_t_~~ _∂_ ~~_t_~~ _∂_ ~~_t_~~



_∂q∂H_ ~~_t_~~ 2 _O_ = _kf_ 3 (



_∂qH_ 2 _O_



(



~~_q_~~ _H_ 2 _O_ - _qH_ 2 _O_



where _tads_ and _tdes_ are the adsorption and desorption times; _ηfan_ and _ηvac_
are efficiencies of the fan and the vacuum pump, respectively; Δ _P_ is the
pressure drop through the fixed bed from imposing a fixed input velocity
(then, Δ _P_ is calculated from the simulation); and _ufeed_ is the feed ve­
locity; _n_ ˙ _out,total_ is the total molar flow rate at the exit. _Pads_ and _Pdes_ are the
adsorption and desorption pressures; _γ_ is the isentropic expansion factor;
_ms_ is the mass of solid sorbent in the bed; Δ _T_ is the temperature dif­
ference between the regeneration and the adsorption steps; _mi,des_ is the
mass desorbed of component _i_ ; _n_ ˙ j is the generation term due to reaction _j_
(see Eqs. (8), (9) and (11)). The amount of CO2 product as a function of
time is calculated using the following expression.



) (11)



where ~~_q_~~ _CO_ 2, ~~_q_~~ _H_ 2 _O_ are the maximum uptakes of the of CO2 and water; _kf_ 1
and _kf_ 2 are kinetic constants; _b_ 1 and _b_ 2 are adsorption affinity constant of
dry and humid reactions; and _pCO_ 2, _pH_ 2 _O_ are the partial pressure of the
CO2 and H2O, respectively.

The variables _b_ 1 and _b_ 2 depend on the temperature according to
Arrhenius type expressions, as shown in the Eqs. (12) and (13).



(
_q_ _[t]_ _CO_ _[ads]_




_[t]_ _CO_ _[ads]_ 2 [−] _[q]_ _CO_ _[t][ads]_ 2 [+] _[t][des]_



_CO_ 2



)

_ρp_ (1 − _ε_ ) _dV_ (21)



)

_T_ 0

~~_T_~~ ~~[−]~~ [1]


)



(12)


(13)



where _q_ _[t]_ _CO_ _[ads]_




_[t]_ _CO_ _[ads]_ 2 [and ] _[q]_ _CO_ _[t][ads]_ 2 [+] _[t][des]_




- [Δ] _[H]_ [1]



(


(



_b_ 1 = _b_ 0 _,_ 1 _e_



~~_R_~~ ~~_T_~~ 0



∫
_mCO_ 2 _,product_ =

_Vrec_



where _q_ _[t]_ _CO_ _[ads]_ 2 [and ] _[q]_ _CO_ _[t][ads]_ 2 [+] _[t][des]_ are the CO2 uptakes evaluated at the end of the

adsorption step and at the end of the desorption step; and _Vrec_ is the
reactor volume.

The productivity ( _Prod_ ) of the process is a relevant metric because of
its connection with the capital expenditure (CAPEX) of the process, as it
determines the efficiency with which the system uses its physical space
and sorbent materials to capture CO₂. Productivity is typically expressed
as the amount of CO₂ captured per unit mass or volume of adsorbent
over time (e.g., kg-CO₂/kg-sorbent/day or kg-CO₂/m³/day). Higher
productivity enables the system to reach the desired CO₂ capture ca­
pacity with smaller equipment and less sorbent, thereby reducing the
size and cost of columns, reactors, or beds. On the other hand, lower
productivity requires larger adsorbers or more sorbent, which increases
capital costs for construction, installation, and infrastructure. Based on
the literature (Young et al., 2023), moderate capital costs will be
required to promote the widespread application of DAC. The definition
of this metric can be presented based on the solid sorbent ( _Prods_ ) or the
reactor volume ( _Prodv_ ). In this work, we present both as showing the
following expression:




- [Δ] _[H]_ [2]



_T_ 0

~~_T_~~ ~~[−]~~ [1]



_b_ 2 = _b_ 0 _,_ 2 _e_



~~_R_~~ ~~_T_~~ 0



Regarding the GAB isotherm for the co-adsorption of CO2 and water,
we show the corresponding expression in Eq. (14). We also show the
Arrhenius type expressions for the isotherm parameters _C_ and _K_ in Eqs.
(15) and (16), respectively.



)



(
~~_q_~~ _H_ 2 _O_ = ~~(~~ ~~(~~ ~~/~~ ~~_q_~~ ~~_[m]_~~ _H_ 2 _O_ _[CK]_ ~~))(~~ _pH_ 2 _O_



~~(~~ ~~(~~
1 − _K_ _pH_ 2 _O_



~~/~~
_pH_ 2 _O,sat_



~~))(~~ ~~(~~
1 + _K_ _pH_ 2 _O_



/
_pH_ 2 _O,sat_



~~/~~
_pH_ 2 _O,sat_



~~)~~ ~~)~~ (14)
( _C_ - 1)



Δ _HC_



_C_ = _C_ 0 ~~_e_~~



~~_R_~~ ~~_T_~~ (15)



Δ _HK_



_K_ = _K_ 0 ~~_e_~~



~~_R_~~ ~~_T_~~ (16)



where ~~_q_~~ ~~_[m]_~~ _H_ 2 _O_ [is the maximum water uptake; ] _[p][H]_ 2 _[O][,][sat ]_ [is the saturation ]
pressure of water; _C_ 0 and _K_ 0 are the pre-exponential constants; and Δ _HC_
and Δ _HK_ are activation energies.



6


_H.A. Pedrozo et al.                                                                                                               Computers_ _and_ _Chemical_ _Engineering_ _204_ _(2026)_ _109379_


**Table 1**
Boundary conditions of the different stages of the adsorption cycle.

Stage Position Darcy’s law Diluted species Description



_**Adsorption**_ _z_ = 0 _u_ = _u_ _[feed]_ _∂ci_



_∂c_ ~~_z_~~ _i_ [=] _[ u]_ ( _c_ _[feed]_ _i_ - _ci_



) Inlet air gas, fixed input velocity, and concentrations.



_z_ = _L_ _P_ = _P_ _[atm]_ _∂ci_



_ci_ Output clean gas, fixed output pressure no diffusive flow.

_∂_ ~~_z_~~ [=][ 0]



_**Evacuation**_ ; _**Heating**_ _/_ _**Regeneration**_ _z_ = 0 _u_ = 0 _∂ci_



_ci_ Zero flux condition.

_∂_ ~~_z_~~ [=][ 0]



_z_ = _L_ _P_ = _P_ _[des]_ _∂ci_



_ci_ Pressure-driven flow velocity; no diffusive flow.

_∂_ ~~_z_~~ [=][ 0]



_**Pressurization**_ _z_ = 0 _u_ = 0 _∂ci_



_ci_ Zero flux condition.

_∂_ ~~_z_~~ [=][ 0]



_z_ = _L_ _P_ = _P_ _[atm]_ _∂ci_



_∂c_ ~~_z_~~ _i_ [=] _[ u]_ ( _ci_ - _c_ _[feed]_ _i_



) Pressure-driven flow velocity; Dankwerts flow.



_**Cooling**_ _z_ = 0 _u_ = 0 _∂ci_



_ci_ Zero flux condition.

_∂_ ~~_z_~~ [=][ 0]



_z_ = _L_ _P_ = _P_ _[des]_ _∂ci_



_∂c_ ~~_z_~~ _i_ [=] _[ u]_ ( _ci_ - _c_ _[feed]_ _i_



) Pressure-driven flow velocity (velocity close to 0); Dankwerts flow.



_Prods_ = _[m][CO]_ [2] _[,][product]_

~~_m_~~ _solid_ ~~_t_~~ _cycle_



ideal gas and NRTL thermodynamic models for the gas and liquid pha­
ses, respectively. In this way, we can determine appropriate values for
the system density, viscosity, and species diffusivities, which are
required in the model.

The cyclic steady state (CSS) is achieved when the overall mass
balance and internal column parameters, such as composition and
temperature, remain consistent between cycles n and n-1. To repeat the
cycles in COMSOL Multiphysics®, we utilized the parametric sweep
option, initializing each simulation from the final state of the previous
cycle. We repeated the cycles three times, as the variable profiles
showed negligible changes between the third and fourth cycles. This
approach balances the need to reach an accurate cyclic steady state
while reducing the computational time. Performance indicators were
calculated based on the results of the final cycle.


**3.** **Optimization model**


Given that the adsorption model was developed using a call to an
“external” function by a specialized software package i.e. COMSOL
Multiphysics®, rather than being explicitly defined by model equations
within the optimization code, traditional optimization methods relying
on gradient information are often unsuitable. In such scenarios, the
trust-region framework provides a robust solution by iteratively
approximating the objective function within a dynamically adjusted
feasible domain, thereby ensuring both convergence and computational
efficiency (Biegler, 2024; Biegler et al., 2014; Eason and Biegler, 2018).
This method operates through an iterative process, where at each iter­
ation, the truth model _f_ ( _x_ ) is replaced by an algebraic model _rk_ ( _x_ ), and
the optimization problem is solved within a domain where the reduced
model adequately represents the true function. This strategy guarantees
finding a local optimum solution and is also versatile enough to handle
cases where derivative information of the reactive transport model is
either available (Chen et al., 2021; Pedrozo et al., 2024b, 2024c) or
absent (Biegler et al., 2014; Liang et al., 2024).

In order to address the problem of the optimal design of the direct air
carbon capture process and plant using solid-based adsorption, we use a
combination of computational platforms, as shown in Fig. 2. The model
for the adsorption cycle is implemented and solved in COMSOL Multi­
physics®, and the trust region subproblem for the optimization of the
process is formulated in Pyomo and solved with IPOPT. From the data of
the CFD model, we build Gaussian Process models by using the SciPy
python package (SciPy, 2022); this model is further used to perform
optimization in Pyomo. We developed a Jupyter Notebook as a master
script to process data and run automatically the model in COMSOL
Multiphysics® and to generate the Gaussian Processes, as required. On
the other hand, we use the Python package MPh (Hennig et al., 2023) to
set and run the simulation via Python and to transfer data between the
platforms. The reduced model formulation and the Trust-region problem



_Prodv_ = _[m][CO]_ [2] _[,][product]_

~~_V_~~ _rec_ ~~_t_~~ _cycle_



(22)


(23)



where _tcycle_ is the total cycle time, and _msolid_ is the total amount of solid in
the packed bed.


_2.5._ _Boundary conditions_


Table 1 shows the boundary conditions associated with this cycle. It
should be noted that the same type of boundary condition was imposed
in each physics for the same step in each cycle, e.g., we always consider a
velocity constraint at _z_ = 0 and a pressure constraint at _z_ = _L_ in the
extended Darcy’s law. The values of these physical magnitudes change
for different steps of the cycle considering ramp functions for the tran­
sition, based on the adsorption and desorption times.

Regarding the boundary conditions associated with the temperature,
we consider zero gradient conditions, as shown in Eqs. (24) and (25).
Although the temperature of the wall ( _Tw_ ) is not a boundary condition
for the 1D model, the value of this temperature also changes for the
different stages and its effect is considered through an effective radial
heat transfer. The value is high for heating/regeneration (decision var­
iable) and low for the other stages (fixed value based on the case study).

_∂T_

_[z]_ [ =][ 0] (24)
_∂_ ~~_z_~~ [=][ 0][;]

_∂T_

_[z]_ [ =] _[ L]_ (25)
_∂_ ~~_z_~~ [=][ 0][;]


_2.6._ _Model implementation_


The adsorption cycle model is implemented in COMSOL Multi­
physics® by considering a 1D component. In particular, this tool pro­
vides an integrated framework to develop models based on diffusionsorption-advection model, as well as a robust solution algorithm to
tackle the challenging numerical problem. In this study, the physical
processes are modeled using the modules available in COMSOL Multi­
physics®: the transport of concentrated species module for the govern­
ing equations, the extended Darcy’s law module for fluid flow, and the
Coefficient Form PDE module which solves PDEs in a generalized form
in physics-based simulations by matching of corresponding coefficients.
The latter module is used twice to model separately uptake and tem­
perature. The transport of concentrated species and Darcy’s law modules
include options associated with the porous medium to consider the
packing bed adsorber. We also include a chemistry module to calculate
the properties of the system based on the mixture composition using



7


_H.A. Pedrozo et al.                                                                                                               Computers_ _and_ _Chemical_ _Engineering_ _204_ _(2026)_ _109379_


**Fig. 2.** Simulation-Optimization framework to leverage software capabilities.


**Table 2**
Model parameters used for the simulation of the adsorption cycle. Data obtained from (Luukkonen et al., 2023).

Parameter Symbol units Value Parameter Symbol units Value



Particle density _ρp_ _kg/m_ [3] 720 Adsorption affinity, rxn. 1 _b_ 0 _,_ 1 _bar_ [−] [1]

Adsorption temperature _Tads_ ∘ _C_ 25 Adsorption affinity, rxn. 2 _b_ 0 _,_ 2 _bar_ [−] [2]



( _mol_
~~_kg_~~

( _mol_
~~_kg_~~



)2 400.39



)2 2 _._ 38⋅10 [4]



CO2 concentration _xCO_ 2 _ppm_ 400 Kinetic constant _kf_ 3 1 _/s_ 0 _._ 16
Relative humidity _rh_ % ( ) 30 & 64 Max. CO2 uptake ~~_q_~~ _CO_ 2 _mol/kg_ 2 _._ 63
Heat transfer coefficient _h_ _W/_ _m_ [2] _K_ 27 _._ 3 Max. H2O uptake ~~_q_~~ ~~_[m]_~~ _H_ 2 _O_ _mol/kg_ 2 _._ 58

Adsorption heat of rxn. 1 - Δ _H_ 1 _kJ/mol_ 84 _._ 35 GAB parameter _C_ 0 - 0 _._ 15
Adsorption heat of rxn. 2 - Δ _H_ 2 _kJ/mol_ 124 _._ 02 GAB parameter Δ _HC_ _kJ/mol_ 6 _._ 63
Adsorption heat of water - Δ _HH_ 2 _O_ _kJ/mol_ 50 _._ 73 GAB parameter _K_ 0 - 0 _._ 87
Efficiencies _ηfan_, _ηvac_ - 0 _._ 72 GAB parameter Δ _HK_ _kJ/mol_ 0

Isentropic expansion factor _γ_ - 1 _._ 4 Solid specific heat _cp,s_ _J/_ ( _kgK_ ) 1580



are described in detail in the accompanying Supplementary Material.


_3.1._ _Case studies_


The main physical properties of the case study addressed in this work
are shown in Table 2, considering the kinetic model and conditions re­
ported by (Luukkonen et al., 2023). These parameters include the col­
umn design, material properties, fitted parameters from the kinetic
models, ambient conditions (temperature and water concentration), and
efficiencies of the electric equipment. Regarding the kinetic constants
for the dry and humid reactions, whose rate expressions are given in Eqs.
(8) and (9), the corresponding expressions are shown in Eqs. (26) and
(27), respectively. The solid sorbent corresponds to an
amine-functionalized resin (Elfving and Sainio, 2021).

It should be noted that Table 2 does not include the desorption
temperature and pressure, adsorption and desorption times, porosity,
inlet velocity, the column ratio, and the length as these are considered to
be decision variables for the carbon capture process. The corresponding


**Table 3**
Decision variables from the optimization studies.



**Fig. 3.** Shell-and-tube configuration for the arrangement of the microreactors
and adsorption particles.


initial values and bounds are shown in Table 3 for the decision variables.
In addition, we consider two values of the relative humidity (see
Table 2) to analyze the effect on the driving force coefficients in Eqs. (8)
and (9).

( )
_kf_ 1 = _max_ - 0 _._ 4571( _rh_ ) [2] + 0 _._ 0722( _rh_ ) + 0 _._ 3372 _,_ 0 _._ 1 (26)


_kf_ 2 = 1 _._ 5355( _rh_ ) [2] + 9 _._ 6689( _rh_ ) + 1 _._ 6043 (27)

where _rh_ is the specified relative humidity.

Additional details regarding the arrangement of the process



Decision variable Symbol unit Initial
value



Lower
bound



Upper
bound



Adsorption time _tads_ _min_ 100 5 300
Desorption time _tdes_ _min_ 25 5 60
Desorption _Tdes_ ∘ _C_ 100 90 125
temperature



_Tdes_ ∘ _C_ 100 90 125



Desorption pressure _Pdes_ _bar_ 0.12 0.09 0.95
Input velocity _u_ _[feed]_ _m/s_ 0.13 0.05 0.90
Bed porosity _ε_ - 0.37 0.20 0.55
Column length _Lc_ _m_ 0.033 0.020 0.100
Column radius _Rc_ _m_ 0.0045 0.003 0.010



8


_H.A. Pedrozo et al.                                                                                                               Computers_ _and_ _Chemical_ _Engineering_ _204_ _(2026)_ _109379_



contactor at large scale are depicted in Fig. 3. The geometry considered
in this study follows a shell-and-tube configuration, where multiple
short packed-bed microtubes are embedded within a common shell. The
shell side is used to circulate a heating fluid, enabling efficient thermal
swing desorption through direct heat transfer across the tube walls. This
configuration is consistent with prior literature and patented designs
proposed for modular CO₂ adsorption systems (Beaumont and Thirket­
tle, 2020; Valverde and Griffiths, 2024). The left panel of the Fig. 3
shows the complete adsorption column, comprising several individual
contactor units arranged in parallel. Each unit houses a packed bed of
spherical resin particles, as illustrated in the central panel. A close-up
view of a representative particle is shown in the right panel, high­
lighting its porous structure and internal adsorption sites. Scale-up of
packed-bed microreactors is readily achieved through numbering-up, in
which the number of parallel units is increased without altering the
operating conditions of individual tubes (Zhang and Yue, 2025). This
modular strategy allows to focus optimization efforts on the design and
performance of a single unit while facilitating system scalability.

As we have important trade-offs between the energy consumption
(operating cost) and the process productivity (capital cost), we select the
capture cost as the objective function and seek its minimization within
the optimization framework. While this work does not perform a
rigorous techno-economic analysis of the process, we consider a
simplified calculation of the capture cost considering the most relevant
operating cost (OPEX) (i.e., including thermal and electrical energy
costs but excluding for example maintenance costs), while we estimate
the capital cost (CAPEX) of the adsorption process as a function of
productivity. This approach has been used in the literature (Borker et al.,
2024; Sabatino et al., 2021) to study appropriate trade-off solutions
between the specific energy consumption and the process productivity,
to get insight into the optimal design under target scenarios. In this
matter, we calculate the capture cost considering Eq. (28).



where _costCO_ 2 is the capture cost, _a_ is the lifetime of the carbon capture
project (20 years for this study); _βAC_ is the air contactor cost per m [3] ; and
_pre_ and _prh_ are the prices of electricity and heat, respectively. The first
term of the right-hand side is associated with the CAPEX. The lower
bound of the factor _βAC_ is set at 2000 $/m [3], representing economical
traditional columns, as reported in the literature (Keith et al., 2018;
Sabatino et al., 2021). This value reflects simpler systems with lower
capital requirements, which are more suitable for basic applications or
early-stage pilot plants. Conversely, the upper bound of 50,000 $/m [3 ]

corresponds to the cost of a full TVSA system, as estimated based on the
design capacity of the Hinwil Climeworks plant (Sabatino et al., 2021).
This high cost reflects advanced, fully integrated systems with enhanced
functionality, such as greater sorbent efficiency, improved heat and
mass transfer properties, and robust modular designs. The significant
variability in the air contactor cost coefficient highlights the wide range
of technological designs and economic scenarios associated with DAC
systems.

To address this variability, we include a medium value of 25,000
$/m [3 ] and an upper bound of 50,000 $/m [3 ] in our optimization studies.
These values allow us to investigate the effect of capital expenditure
(CAPEX) uncertainty on the overall process design and capture cost. The
high variation in _βAC_ underscores the importance of optimizing system
parameters and understanding the trade-offs between capital and
operational expenses in the design of scalable and cost-effective DAC
systems. The second and the third term of Eq. (28) refer to the OPEX; we
assume a scenario with 0.05 $/kWh and 0.10 $/kWh for the heating and
electricity costs, respectively.

In the Results section, the base case scenario is characterized by a
capital cost factor of $50,000/m³ and relative humidity of 64 % (H₂O
molar fraction of 0.02). This base case is used as a reference point to
compare results and evaluate system performance under these specified



_costCO_ 2 = ~~_Prod_~~ _βACv_ ⋅ ~~_a_~~ [+] ( _Efan_ + _Evac_



)
_pre_ + _Eheatprh_ (28)



**Fig. 4.** Validation of the adsorption process, considering dry (0 vol/vol of water) and humid operation (0.02 vol/vol water) (Luukkonen et al., 2023). a) CO2
breakthrough curve considering dry and humid conditions. b) CO2 uptake curve considering dry and humid conditions. c) Water breakthrough curve for the humid
conditions. Operating conditions: _T_ _[des]_ = 100 [∘] _C_, _P_ _[des]_ = 0 _._ 012 _bar_, _u_ _[feed]_ = 13 _._ 1 _cm/s_, _ε_ = 0 _._ 375.


9


_H.A. Pedrozo et al.                                                                                                               Computers_ _and_ _Chemical_ _Engineering_ _204_ _(2026)_ _109379_



cost and humidity conditions.


**4.** **Results**


_4.1._ _Validation_



We have validated the implementation of the adsorption and
regeneration process, under dry and humid conditions, considering
experimental data reported by (Luukkonen et al., 2023). For these cases,
we consider the values presented in Table 2. In order to quantify the
accuracy of the model to represent the experiments, we also calculate R [2 ]



coefficients between the experimental data and model simulations.



Fig. 4a shows that the model implemented in COMSOL Multi­
physics® can appropriately represent the experimental data for the CO2
breakthrough curves of the adsorption process. It can be observed that
the curves are “S” shaped and that the CO2 takes longer to start exiting in
the humid case, as compared to the dry case. This phenomenon is related
to the higher CO2 uptake that is achievable under humid conditions. We
calculated R [2 ] coefficients of 0.982 and 0.960 for the dry and humid
cases, respectively. These values indicate a strong correlation and are
considered satisfactory, especially since no parameter fitting was
applied in the analysis. We have also evaluated the impact of mass
transfer resistances using the approach of Darunte et al. (2019), which
accounts for external gas-to-particle film resistance and reaction kinetics
within the sorbent. Our numerical results indicate that the process is
kinetically controlled under the studied conditions, supporting the
assumption that this modeling framework captures the dominant
transport and reaction phenomena. For more details on the comparison
of results with and without mass transfer in the particles, we direct the
reader to section 5 of the Supplementary Material.

The CO2 uptake curves for the dry and humid cases are shown in
Fig. 4b, suggesting a good fit of the model to represent the adsorption
experiments. It is also observed that the uptake can increase between
56–72 % under humid conditions; on the negative side, this operating
condition requires an additional energy amount to desorb the water in
the fixed bed. While we observed some deviations from the experimental
data, mainly for the operation under humid conditions, we consider that
the accuracy is good enough for the process analysis in this work as the
calculated R [2 ] coefficients are 0.980 and 0.981 for the dry and humid
conditions, respectively.

The water uptake curve is shown in Fig. 4c. It is observed that water
achieves saturation uptakes in short times as compared to CO2; while it
takes 43 min to achieve 97 % of the input concentration at the outlet, it
takes 200 min to achieve the same ratio for the CO2 as observed from
Fig. 4b This result is associated with the high concentration of water as



**Fig. 5.** Validation of regeneration process Temperature profile of the regen­
eration process, for the humid conditions (Luukkonen et al., 2023). Operating
conditions: T [des] =100 [◦] C, P [des] =0.012 bar, u [feed] =13.1 cm/s, ε=0.375.



compared with CO2 concentration in the air. On the other hand, nu­
merical results indicate the suitability of the GAB isotherm approach to
model the co-adsorption of water and CO2, and the R [2 ] coefficient for the
water uptake is 0.988.

In Fig. 5. we have also validated the regeneration process with the
output temperature of the gas mixture, as presented in the literature
(Luukkonen et al., 2023). During this operation, the first 60 min are
associated with an evacuation step. The model was able to capture the
small temperature reduction at the beginning of the step due to endo­
thermic water desorption. After this time, we set a high temperature at
the wall (100 [◦] C) to proceed with the regeneration step. It is observed
that the model implemented in COMSOL Multiphysics® can represent
this phenomenon accurately, with an R [2 ] coefficient of 0.990.


_4.2._ _Optimal solution for the base case_


In this section, we have used the validated adsorption model to
perform optimization for a base case scenario with a capital cost factor
of $50,000/m³ and a relative humidity of 64 % (H₂O molar fraction of
0.02). This base case serves as a reference for comparing results and
analyzing system performance under these cost and humidity condi­
tions. The objective function involves the minimization of the capture
cost and the decision variables presented in Table 3. The optimization
framework involves coupled reactive transport models, considering
advanced trust-region methods and Gaussian Processes as described in
the Supplementary Material. Optimization variables include adsorption
and desorption times, desorption temperature and pressure, input ve­
locity, bed porosity, column length, and column radius.

The optimization results yield a minimum capture cost of $265.2/tCO₂, consistent with reported values in the literature (Sievert et al.,
2024). The solution is theoretically guaranteed to be locally optimal
under the specified numerical tolerances (Biegler et al., 2014). This cost
corresponds to a specific energy consumption (SEC) of 15.6 MJ/kg-CO₂
and a productivity of 0.452 kg-CO₂/kg-solid/day (solid basis, Eq. (22)).
Compared to Luukkonen et al. (Luukkonen et al., 2023), the optimized
solution achieves a 14.9 % reduction in SEC and a 42.5 % improvement
in productivity, considering the process performance reported with a
desorption temperature of 120 [◦] C. It should be noted that Luukkonen
et al. (Luukkonen et al., 2023) does not perform optimization but merely
a sensitivity analysis, and we selected the simulation instance with the
best energy performance for comparison purposes. These results high­
light the value of simultaneous optimization of decision variables over
traditional sensitivity analyses that vary one variable at a time.

Specific energy consumption (SEC) is directly related to operating
costs (OPEX), while productivity impacts capital costs (CAPEX). In the
analyzed scenario, characterized by a high capital cost factor, OPEX
constitutes 83.5 % of the total capture cost, with OPEX comprising 95.4
% heating expenses. These results highlight that access to low-cost
heating utilities, can significantly reduce capture costs. To explore this
effect, we performed additional simulations considering different heat­
ing prices. Numerical results suggest that the target capture cost of
$100/t-CO₂ becomes achievable if thermal energy can be supplied at
approximately $0.01/kWh. This finding underscores the central role
that access to low-cost, renewable or waste heat sources plays in
enhancing the economic feasibility of direct air capture technologies.

Additionally, to evaluate the multi-dimensional sustainability per­
formance, we have implemented the GREENSCOPE methodology
developed by Ruiz-Mercado et al. (2014) to compare the sustainability
ratio of the process operating at the initial conditions (see Table 3) and
the optimized configuration. This analysis includes normalized in­
dicators covering energy, environmental, and economic metrics
(Ruiz-Mercado et al., 2014; Smith and Ruiz-Mercado, 2014). The opti­
mized operating conditions show an improvement of 28 % in the
average sustainability performance compared to the initial conditions.
Notably, the SEC, thermal energy use, and net CO2 removal efficiency all
exhibit higher performance in the optimized configuration, indicating



10


_H.A. Pedrozo et al.                                                                                                               Computers_ _and_ _Chemical_ _Engineering_ _204_ _(2026)_ _109379_



that optimization has positively influenced both thermodynamic effi­
ciency and process selectivity.

Improvements are also observed in the carbon footprint and energy
return on CO2, indicating that the optimized system captures more CO2
per unit of emitted emissions and per unit of energy input, respectively.
These gains may be attributed to a reduction in cycle energy intensity
and improved sorbent utilization. A detailed discussion of the Sustain­
ability Ratio results and the associated radar plot is provided in the
Supplementary Material, where improvements in key indicators such as
productivity, specific energy consumption, and carbon footprint are
highlighted.

During the optimization process, we observed a strong interplay
between adsorption time and input velocity. To capture a fixed amount
of CO₂ per cycle, increasing the input velocity (and thereby OPEX) re­
duces adsorption time, enhancing productivity and lowering CAPEX.
Similarly, desorption temperature correlates with vacuum pressure,
where lowering pressure increases OPEX but decreases regeneration
time, further improving productivity and reducing CAPEX. This
behavior results in a highly nonlinear problem, which is challenging to
solve. In this regard, the presented trust region strategy can handle the
problem efficiently.

For geometric variables, the optimization suggests minimizing both
the bed radius and length. A smaller bed radius improves heat transfer
efficiency, reducing cycle time and boosting productivity, while a
shorter bed length lowers pressure drops, saving energy costs for the fan
and vacuum pump. Adjusting these geometric parameters reduces cap­
ture costs by approximately 4 % compared to initial values in Table 2.
Although seemingly modest, this improvement could yield significant
savings at the estimated large-scale global CO₂ removal targets of 5–10
Gt/year (World Economic Forum, 2024).

The temporal CO₂ uptake profile from the optimized solution is
shown in Fig. 6a across cycles. In this context, the working capacity is
defined as the difference between the CO2 concentration in the sorbent
at equilibrium under adsorption conditions and that at equilibrium
under desorption conditions. Similarly, the cyclic capacity is defined as
the difference between the CO2 concentration in the sorbent at the end
of the adsorption step and that at the end of the desorption step. During
adsorption, the bed reaches 94.3 % of equilibrium capacity, while
desorption proceeds until the CO₂ uptake is 1 % above equilibrium. This
enables the cycle to achieve 91.7 % of the sorbent working capacity
under the given environmental conditions. Profiles for cycles 2 and 3
overlap closely, indicating rapid achievement of cyclic steady-state
behavior. Fig. 6b illustrates the temperature profile in the packed bed,
showing minor differences for Cycle 1 and near-identical profiles for
cycles 2 and 3. This consistency highlights how fast the cyclic steadystate is achieved in DAC applications. The percentage of the CO2
removed in a single pass through the cycle is 40.5 %.



_4.3.1._ _Vacuum/Desorption pressure and desorption temperature_

To improve CO2 recovery and consequently enhance cost savings,
low vacuum pressures are usually required to increase the driving force
for desorption (Elfving et al., 2021; Hedin et al., 2013; Kim and L´eonard,
2022). Very low pressure will be reflected in a higher energy require­
ment for the vacuum pump. Depending on the price scenario for elec­
tricity this could be a significant variable to consider, and consequently,
it is important to take into account vacuum pressure as a decision var­
iable. On the other side, TVSA is a process that is highly dependent on
temperature, especially for the regeneration stage (An et al., 2023;
Elfving et al., 2021; Zhu et al., 2021). If the temperature is not high
enough, the solid sorbent might be poorly regenerated, and the CO2
productivity could be compromised. Also, higher temperatures mean a
better recovery, but the sorbent can deteriorate at a certain operational
limit as well.

At the optimal point of the base case (Fig. 7), vacuum pressure im­
pacts both SEC and capture cost, which is a function of productivity as
well. It is observed that the main impact of this variable is associated
with changes in the vacuum energy. Increasing this operating pressure
reduces energy requirements for CO2 desorption (see Eq. (19)); but it
may decrease productivity too. In the base case scenario (high humidity
and high capital cost factor), the optimal design selects the upper bound
for this variable. This outcome indicates that, for desorption pressure,
the influence of OPEX dominates over that of CAPEX.

Fig. 7b illustrates the effect of desorption temperature on SEC and
capture cost. Higher desorption temperatures improve sorbent



_4.3._ _Sensitivity analysis for the decision variables_


Studying the effects of key decision variables on specific energy
consumption (SEC) and capture cost is important for understanding the
physics behind the optimal design in direct air capture (DAC) systems. In
this section, we present sensitivity analyses based on the main opera­
tional and geometric variables, highlighting the trade-offs and in­
terdependencies that influence system performance. For this matter, we
present the breakdown of the energy consumption, considering the fan
energy (Eq. (18)), the vacuum pump energy (Eq. (19)), the heating en­
ergy for the solid, the CO2 and the water, and the heating energy to
desorb the CO2 and the water (see Eq. (20)). In addition, we show the
value of the objective function (Eq. (28)) for the different cases. It should
be noted that only one variable was changed at a time. For this sensi­
tivity analysis, 3 cycles were run as well, maintaining the cyclic steady
state condition (see Fig. 6). Figs. 7–10 illustrate various sensitivity an­
alyses around the optimal design of the base case (see Section 4.2),
where one parameter is examined at a time. In some cases, the sensitivity
analysis extended beyond the original optimization bounds. In those
cases, the ranges of the sensitivity analyses were adjusted to better
capture the detailed effects of each parameter and operational influence
on the performance metrics and objective function.



**Fig. 6.** Profiles of the CO2 uptake of the optimal solution for different cycles. a) Profile of the average CO2 uptake vs time. b) CO2 uptake at the end of the simulation.
The cyclic steady state is essentially obtained after the third iteration.


11


_H.A. Pedrozo et al.                                                                                                               Computers_ _and_ _Chemical_ _Engineering_ _204_ _(2026)_ _109379_


**Fig. 7.** (a) Effect of desorption pressure on the energy consumption (in bars, left axis) and capture cost (in dots, right axis). Optimum of base case _P_ _[des ]_ = 0 _._ 95 _bar_,
located at the upper bound, and (b) Effect of desorption temperature on the energy consumption and capture cost. The optimum of the base case is located at the
upper bound _T_ _[des]_ = 125 [∘] _C_, and we consider the impact of increasing this temperature for the sensitivity analysis.


**Fig. 8.** (a) Effect of the input velocity on the energy consumption (in bars, left axis) and capture cost (in dots, right axis). The optimum of the base case is located at
the center _u_ _[feed]_ = 0 _._ 150 _m/s_, and (b) Effect of bed porosity on the energy consumption and capture cost. The optimum of the base case is located at the center _ε_ =
0 _._ 52.



regeneration efficiency and accelerate CO₂ release, thereby enhancing
cyclic capacity and productivity. However, exceeding the sorbent ma­
terial tolerance can lead to degradation, reducing long-term productiv­
ity and increasing maintenance costs. In this study, the maximum
operating temperature is set at 125 [◦] C, aligned with the degradation
limit of MEA (Davis and Rochelle, 2009). To explore potential ad­
vancements, we also analyze the impact of developing materials with
higher temperature resistance. Materials capable of withstanding tem­
peratures up to 150 [◦] C have the potential to reduce capture costs by 4.3
%, highlighting the importance of material innovation in DAC systems.
On the other hand, energy consumption increases significantly as the
temperature decreases (see Fig. 7b), primarily because the optimal
design outlined in Section 4.2 is used as the baseline for these simula­
tions. This causes lower temperatures to lead to a substantial reduction
in the sorbent working capacity. Overall we observe that CAPEX dom­
inates over OPEX in this case.



_4.3.2._ _Input velocity and bed porosity_

A straightforward way to increase mass transfer rates is to operate at
higher velocities. Fluid velocity is highly dependent on bed porosity,
which typically ranges from 0.2 to 0.6, as reported in the literature
(Schellevis et al., 2024; Zhu et al., 2022). After reaching the maximum
achievable CO2 productivity, any further increase in process intensity
only leads to higher fan energy consumption. Regarding porosity, a
trade-off is observed; low porosities result in excessive pressure drops
and increased electrical energy requirements, whereas very high po­
rosities lead to significantly reduced cyclic capacities.

Around the optimal input velocity (0.150 ms [−] [1], central bar in
Fig. 8a), the input airflow rate (feed velocity) impacts SEC, productivity,
and capture cost by influencing both the fan energy required for air
movement and the efficiency of CO₂ capture. After the solid sorbent
approaches saturation, productivity does not increase with the input
velocity for the fixed adsorption time, and it only increases the energy
requirements. Higher feed velocities increase SEC due to higher fan
energy consumption and reduced contact time between the air and



12


_H.A. Pedrozo et al.                                                                                                               Computers_ _and_ _Chemical_ _Engineering_ _204_ _(2026)_ _109379_


**Fig. 9.** (a) Effect of the adsorption time on the energy consumption (in bars, left axis) and capture cost (in dots, right axis). Optimum of base case _t_ _[ads ]_ = 68 _._ 0 _min_,
located at the center, and (b) Effect of desorption time on the energy consumption and capture cost. Optimum of base case _t_ _[des]_ = 11 _._ 3 _min_, located at the center.


**Fig. 10.** (a) Effect of the column length on the energy consumption (in bars, left axis) and capture cost (in dots, right axis). The base case is at the lower bound and at
the center _Lc_ = 0 _._ 02 _m_ . We include a value below the lower bound for the sensitivity analysis, and (b) Effect of the column radius on the energy consumption and
capture cost. The base case is at the lower bound and at the center _rc_ = 0 _._ 003 _m_ . We include a value below the lower bound for the sensitivity analysis.



sorbent. Optimal feed velocities balance these trade-offs, minimizing
CAPEX by maximizing reactor throughput while avoiding excessive
OPEX associated with energy-intensive air handling systems. It is
observed that the presented optimization algorithm can satisfactorily
find this trade-off solution (optimal value at 0.150 ms [−] [1] ), and _a_ ± 20 %
change from this point results in variations of less than 1 % in the
objective function (see Fig. 8a). In terms of bed porosity (Fig. 8b), we set
an upper bound of 0.55 for porosity. However, we include higher values
in the sensitivity analysis to explore a broader range of effects. The re­
sults reveal that SEC decreases as porosity increases. This reduction is
primarily due to a lower pressure drop across the bed, which reduces fan
energy requirements. However, higher porosity levels also result in a
decrease in volumetric productivity, leading to an increase in capital
cost. This trade-off highlights the need to identify an optimal porosity
that balances energy consumption with cost-effectiveness. Our analysis
identifies an optimal porosity of 0.52, which achieves a 2 % improve­
ment in capture cost compared to the lowest (0.42) and highest (0.63)
porosity values analyzed.



_4.3.3._ _Adsorption and desorption times_

Adsorption and desorption times are relevant variables that directly
influence the kinetics, energy requirements, and productivity of the DAC
process. The adsorption time is inherently limited by the saturation of
the sorbent material. Beyond this point, extending the adsorption time
does not enhance CO₂ capture, as the sorbent nears equilibrium. Addi­
tionally, while prolonged adsorption times slightly reduce SEC by
improving CO₂ capture efficiency, they negatively impact productivity
by increasing cycle duration. Conversely, shorter adsorption times
enable more cycles per day, enhancing productivity but potentially
increasing SEC due to reduced sorbent utilization efficiency because of
decreasing degree of saturation.

Desorption time also plays a key role in the cycling rate of the pro­
cess. Shorter desorption times allow for more frequent CO₂ capture cy­
cles, improving productivity. However, insufficient desorption time can
lead to incomplete sorbent regeneration, diminishing the effectiveness
of subsequent cycles. Interestingly, the energy requirement for sorbent
regeneration remains relatively constant across different desorption
times, as thermal energy consumption dominates the process.



13


_H.A. Pedrozo et al.                                                                                                               Computers_ _and_ _Chemical_ _Engineering_ _204_ _(2026)_ _109379_



After applying the proposed optimization algorithm, adsorption and
desorption times are shown to significantly influence SEC and capture
costs, as illustrated in Fig. 9. The algorithm identifies an optimal
adsorption time of 68.1 min for the base case study (see Section 4.2),
balancing energy efficiency and system productivity. For desorption, an
optimal time of 11.3 min was determined, though the objective function
improves marginally by just 0.02 % as desorption time decreases. This
suggests that energy requirements for regeneration are not highly sen­
sitive to desorption time within the tested range. Despite numerical
tolerances in the optimization framework, the identified durations
effectively enhance system performance by balancing SEC and produc­
tivity, to minimize capture costs.



_4.3.4._ _Column length and radius_

We have also analyzed the effect of geometric parameters, such as
reactor length and radius, on DAC system performance. First, increasing
column length enhances the contact time for air to interact with the
adsorbent, which improves CO2 capture overall, but simultaneously
increases the pressure drop. On the other hand, increasing the column
radius increases the cross-sectional area, reducing the superficial ve­
locity of air and, thereby, lowering the pressure drop along the bed.
These are dependent up to a certain level on the column length (more
resistance) and radius (less resistance).

At the optimal design of the base case, sensitivity analyses are
depicted in Fig. 10a and b, for the reactor length and radius, respec­
tively. It should be noted that we also consider values for these di­
mensions lower than the lower bounds used for the optimization study,
as shown in the center bars of Fig. 10. Shorter reactor lengths reduce
pressure drops, leading to lower SEC. A smaller bed radius enhances
heat transfer efficiency during desorption, reducing energy consumption
and improving productivity. In the range that we have analyzed these
variables; we observed that the capture costs improve as we have
smaller reactor beds. However, we consider the lower bounds (for the
optimization studies) of 0.02 m and 0.003 m for the column length and
radius, respectively, since dimensions below these values seem to be
unrealistic for large-scale technology applications.


_4.4._ _Optimization studies considering different capital cost factors and_
_relative humidity_


In this section, we analyze the characteristics of the optimal design


**Table 4**
Optimal values of the decision variables for the case scenarios, considering
different costs and humidities. Hh_Hc: High humidity, High cost, Lh_Hc: Low
humidity, High cost, Hh_Lc: High humidity, Low cost, Lh_Lc: Low humidity, Low
cost.



under different cost and humidity scenarios. This analysis can shed light
in the changes in the operating and design variables depending on the
given scenario. In particular, we perform optimization for cases with
relative humidities of 64 % (high humidity value) and 30 % (low hu­
midity value), which corresponds to H2O molar fractions of 0.02 and
0.01, respectively. Regarding the cost, we consider cost coefficients of
50,000 $/m [3 ] (high cost), and 25,000 $/m [3 ] (low cost), as described in
Section 3.

The decision variables and process indicators associated with these
optimization studies are shown in Table 4, as well as the reference
names. It is observed that the optimal value for the desorption temper­
ature is at its upper bound and remains the same for all cases. Regarding
the desorption pressure, we observed that the cases with low and high
humidities present different values. Independent of the cost, this pres­
sure value is at the upper bound for high-humidity values, while it is in a
range of 0.44–0.46 bar for low humidity values. This behavior is linked
to the co-adsorption of water, as desorption pressure influences the
water uptake curves. The optimal value represents a trade-off; lower
pressures improve cyclic capacity (reducing CAPEX), while higher
pressures decrease energy requirements (reducing OPEX). Under highhumidity, the pressure is set to its upper bound to minimize the en­
ergy cost associated with water desorption, while for low humidity, the
pressure can decrease to improve the overall performance of the process.

Optimal porosity undergoes significant changes under low humidity,
as volumetric productivity increases with higher porosity. Under humid
conditions, the optimal design suggests a high porosity range of 52–53
%. However, at low humidity levels, the optimal porosity decreases to 40
% and 43 % for high and low capital cost factors, respectively. This
reduction compensates for the loss in CO2 uptake at equilibrium con­
ditions, which results from the change in water concentration.

The input velocity also decreases by 46.7 % and 43.6 % for high and
low capital cost factors, respectively, under low humidity conditions.
This reduction is attributed to the lower porosity, which increases the
pressure drop and electric energy demand. Consequently, the optimi­
zation strategy adjusts the input velocity to mitigate the rise in energy
consumption.

Analyzing the process metrics reveals that operating at low water
concentrations reduces thermal energy demand by 13 %. However, this
reduction is accompanied by an approximate 1 % increase in capture
cost. This outcome is primarily attributed to higher electrical energy
demand and productivity losses of approximately 16 % and 30 % for
high and low capital cost factors, respectively.

Regarding capital cost factor analysis, doubling the capital cost fac­
tor increases the total capture cost by approximately 9 %. Designs
optimized for low capital costs (i.e., 25,000 $/m³) tend to prioritize
marginal energy savings, achieving reductions in SEC of 8 % under highhumidity conditions and 10 % under low-humidity conditions. Howev­
er, this comes at the expense of productivity, which decreases by 16 %
under high humidity and 30 % under low humidity.


**5.** **Extension of the model to 2D axisymmetric geometries**


State-of-the-art modeling approaches for adsorption cycles in direct
air capture (DAC) using solid sorbents primarily rely on 1D models to
simplify the representation of physical phenomena. While 1D models
efficiently capture key trends and enable rapid simulations, they
inherently assume uniformity in the radial direction, which can over­
simplify the interactions between heat and mass transfer processes. In
this study, we explore the advantages and limitations of extending these
models to 2D axisymmetric geometries, providing a more detailed un­
derstanding of radial variations. Using COMSOL Multiphysics®, we
expanded the 1D model from Section 2 into a 2D axisymmetric frame­
work. This extension accounts for radial gradients and enables 3D vi­
sualizations through solid revolution by exploiting axial symmetry
(Rivero et al., 2020). The model directly imposes wall temperature as a
boundary condition, eliminating the need for approximate heat transfer



Optimization Case Hh_Hc (base
case)



Lh_Hc Hh_Lc Lh_Lc



Humidity ( **64 %** **30 %** **64 %** **30 %**
Cost factor _**$**_ _/_ _**m**_ [3][)] **50,000** **50,000** **25,000** **25,000**



Decision variable
Adsorption time ( _**min**_ ) 68.1 89.6 83.4 121.0
Desorption time ( _**min**_ ) 11.3 7.2 9.7 5.5
Desorption temperature ( [∘] _**C**_ ) 125.0 125.0 125.0 125.0
Desorption pressure ( _**kPa**_ ) 95.0 44.3 95.0 46.0
Input velocity ( _**cm**_ _/_ _**s**_ ) 15.0 8.00 12.2 6.88
Bed porosity (%) 52.0 40.2 53.2 43.0
Reactor length ( _**cm**_ ) 2.0 2.0 2.0 2.0
Bed radius ( _**cm**_ ) 0.3 0.3 0.3 0.3
Process indicators
Capture cost ($/t-co2) 265.2 267.6 242.1 244.1
Specific energy consumption 15.6 14.3 15.3 13.8
(MJ/kg)



15.6 14.3 15.3 13.8



Thermal energy (MJ/kg) 15.2 13.0 15.0 12.6
Electric energy (MJ/kg) 0.4 1.3 0.3 1.2
Productivity (volume basis, t- 57.0 47.8 48.5 34.1
CO2/(m [3] y))



57.0 47.8 48.5 34.1



14


_H.A. Pedrozo et al.                                                                                                               Computers_ _and_ _Chemical_ _Engineering_ _204_ _(2026)_ _109379_


**Fig. 11.** CO2 uptake and temperature profiles for a 2D axisymmetric geometry, with the optimal operating conditions obtained with the 1D modeling approach. a)
CO2 uptake profile during the adsorption time. b) Temperature profile during the adsorption time. c) CO2 uptake profile during the desorption step. d) Temperature
profile during the desorption step. Note the significant variations in the radial direction during the adsorption and desorption steps.



coefficients, and providing a more realistic representation of heat
transfer. Moreover, this modeling approach enables 3D visualizations,
offering means to validate key assumptions of the 1D model, particularly
for heat and mass transfer phenomena.



The 2D axisymmetric model employs a structured rectangular grid
with controlled point distrbutions on the two directions (z and r)
meshing strategy, and a mesh independence study is shown in the
Supplementary Material. The same equations and boundary conditions



**Fig. 12.** Comparison of profiles for the 2D axisymmetric and 1D models. a) CO2 uptake profile. b) Temperature profile.


15


_H.A. Pedrozo et al.                                                                                                               Computers_ _and_ _Chemical_ _Engineering_ _204_ _(2026)_ _109379_



presented in Section 2 are applied, with the exception of heat transfer
through the reactor wall. In the 2D axisymmetric approach, this phe­
nomenon is modeled using a Dirichlet boundary condition at the wall,
maintaining the rest of the boundary conditions for the 1D model.
Additionally, a piecewise quadratic finite element discretization is
employed for all physics in the CFD model, enhancing the accuracy of
the simulations.

The 3D visualizations of CO₂ uptake during adsorption (Fig. 11a)
reveal significant radial variations in the adsorbed CO₂ concentration,
with values reaching up to 0.65 mol/kg. Similarly, during the adsorption
phase, temperature differences exceeding 6 [◦] C are observed across the
reactor (Fig. 11b), indicating non-uniform thermal behavior that may
influence adsorption efficiency and system performance. However, at
the end of the adsorption phase (close Fig. 11c and d), we obtain minor
variations near the outlet due to the exothermic nature of adsorption. On
the other hand, the regeneration step exhibits significant radial gradi­
ents. Numerical results indicate radial concentration differences of up to
0.61 mol/kg between the center and the wall (Fig. 11c), and tempera­
ture differences of up to 30 [◦] C (Fig. 11d). Such insights underscore the
importance of considering radial effects in DAC systems, particularly
during desorption.

Regarding the comparison between the 2D axisymmetric and 1D
models, Fig. 12 presents the profiles of the average CO₂ uptake and
temperature for both approaches. Fig. 12a shows that at the beginning of
the adsorption step, the average CO₂ uptake predicted by the 2D
axisymmetric model is lower than that of the 1D model. Conversely, at
the end of the adsorption step, the 2D model predicts a higher CO₂ up­
take than the 1D model. These results indicate that the 2D axisymmetric
model estimates a slightly higher working capacity compared to the 1D
model. This difference is closely linked to the temperature profiles
shown in Fig. 12b The 2D model presents slightly faster heat transfer,
which results in the cyclic steady state being achieved with marginally
lower CO₂ uptakes during the adsorption step in the 2D model.

Quantitatively, we calculated average relative differences of 6.3 %
and 13.2 % for the CO₂ uptake and temperature profiles, respectively,
between the models. These differences in the 2D axisymmetric model
are associated with energy savings of 3.5 %, 4.4 %, and 4.1 % for
heating, fan, and vacuum pump operations, respectively, compared to
the 1D model. Additionally, the productivity (volume basis) estimated
by the 2D model shows a 3.1 % increase relative to the 1D model.

The 2D axisymmetric model provides valuable insights into the
spatial distribution of heat and mass transfer that are inaccessible to 1D
models. For example, such detailed analysis is important for identifying
potential hotspots or zones of uneven sorbent utilization, which could
affect long-term material performance and process efficiency. This
aligns with findings from other studies that emphasize the importance of
incorporating radial gradients in packed bed systems (Zhu et al., 2022).
This is particularly relevant when designing systems that rely on TVSA
processes, where heat transfer efficiency significantly impacts energy
consumption and productivity.

While the 2D axisymmetric model provides detailed insights into
concentration gradients in the radial direction, it comes with signifi­
cantly higher computational costs compared to the 1D models. Simu­
lating one cycle with the 1D model takes approximately 1 min per cycle
(and three cycles are required to approximate the cyclic steady state),
whereas the 2D axisymmetric model requires 40 min for a single cycle.
Thus, a practical approach involves using 1D models for optimization
studies, leveraging 2D models for analyzing critical spatial variations,
and reserving the complex CFD simulations for detailed investigations of
fluid dynamics and structural performance. This multi-tiered modeling
approach balances computational efficiency with accuracy and provides
a methodology for DAC system design.


**6.** **Conclusions**


This work addresses the implementation and optimization of a CFD



model for direct air carbon capture, focusing on the adsorptiondesorption cycle, using COMSOL Multiphysics®. As decision variables,
we consider the adsorption and desorption times, the pressure and
temperature for adsorption, the input velocity, the porosity, the reactor
length and radius. In particular, the porosity of the bed is seldom
considered as a design variable, and it has an impact on the cycling
capacity and the energy consumption of the fan. The integration of
advanced trust-region methods with Gaussian Processes proved to be an
effective approach for optimizing the complex interplay of variables in
the adsorption-desorption process. The optimization results yielded a
minimum capture cost of 265.2 $/t-CO2, with an improved specific
energy consumption of 15.6 MJ/kg and a productivity of 0.452kgCO2/
kgsolid/d (57.0 t-co2/(m [3] y)). The study also revealed strong in­
terdependencies among the decision variables, particularly between
adsorption time and input velocity, as well as desorption temperature
and vacuum pressure. These findings demonstrate that a rigorous opti­
mization approach, rather than a one-variable-at-a-time sensitivity
analysis, is crucial for enhancing the efficiency and cost-effectiveness of
direct air capture systems.

Furthermore, we expanded the modeling approach to a 2D axisym­
metric model to visualize the uptake and temperature profiles more
effectively. This strategy enables a 3D visualization, revealing signifi­
cant radial gradients in temperature and CO2 uptake during the regen­
eration step, which have significant potential in structure analysis and
structure optimization. This enhanced modeling approach offers valu­
able insights into improving the heating process within the bed. How­
ever, the main drawback is the computational cost, with the CPU time
for this model being about 40 times that of the 1D model.


**CRediT authorship contribution statement**


**Hector A. Pedrozo:** Writing – original draft, Visualization, Valida­
tion, Software, Methodology, Investigation, Conceptualization. **Mayra**
**G. Gonzalez-Ramirez:** Writing – original draft, Visualization, Software,
Investigation. **Tiras Y. Lin:** Writing - review & editing, Supervision,
Resources, Methodology, Conceptualization. **Thomas Moore:** Writing –
review & editing, Conceptualization. **Thomas Roy:** Writing – review &
editing, Supervision. **Du T. Nguyen:** Writing - review & editing, Su­
pervision, Conceptualization. **Pratanu Roy:** Writing – review & editing,
Supervision, Project administration, Funding acquisition, Conceptuali­
zation. **Sarah Baker:** Writing – review & editing, Supervision, Funding
acquisition. **Lorenz T. Biegler:** Writing – review & editing, Supervision,
Resources, Methodology, Conceptualization. **Grigorios Panagakos:**
Writing – review & editing, Supervision, Project administration, Meth­
odology, Funding acquisition, Conceptualization.


**Declaration of competing interest**


The authors declare that they have no known competing financial
interests or personal relationships that could have appeared to influence
the work reported in this paper.


**Acknowledgement**


This work was performed under the auspices of the U.S. Department
of Energy by Lawrence Livermore National Laboratory under Contract
DE-AC52–07NA27344 and was supported by the LLNL-LDRD program
under project number 22-SI-006. LLNL release number LLNL-JRNL872157.


**Supplementary materials**


Supplementary material associated with this article can be found, in
[the online version, at doi:10.1016/j.compchemeng.2025.109379.](https://doi.org/10.1016/j.compchemeng.2025.109379)



16


_H.A. Pedrozo et al.                                                                                                               Computers_ _and_ _Chemical_ _Engineering_ _204_ _(2026)_ _109379_



**Data availability**


Data will be made available on request.


**References**


Abdullatif, Y., Sodiq, A., Mir, N., Bicer, Y., Al-Ansari, T., El-Naas, M., Amhamed, A.,
2023. Emerging trends in direct air capture of CO2: a review of technology options
[targeting net-zero emissions. RSC Adv. 13, 5687–5722. https://doi.org/10.1039/](https://doi.org/10.1039/D2RA07940B)
[D2RA07940B.](https://doi.org/10.1039/D2RA07940B)
Agarwal, A., Biegler, L.T., Zitney, S.E., 2010. A superstructure-based optimal synthesis of
[PSA cycles for post-combustion CO2 capture. AIChE J. 56, 1813–1828. https://doi.](https://doi.org/10.1002/aic.12107)
[org/10.1002/aic.12107.](https://doi.org/10.1002/aic.12107)
Al-Absi, A., Benneker, A., Mahinpey, N., 2024. Ambient and sub-ambient temperature
direct air CO2 capture (DAC) by novel supported in situ polymerized amines.
[J. Mater. Chem. A 12, 10507–10527. https://doi.org/10.1039/D3TA07909K.](https://doi.org/10.1039/D3TA07909K)
Amiri, L., Ghoreishi-Madiseh, S.A., Hassani, F.P., Sasmito, A.P., 2019. Estimating
pressure drop and Ergun/Forchheimer parameters of flow through packed bed of
[spheres with large particle diameters. Powder Technol. 356, 310–324. https://doi.](https://doi.org/10.1016/J.POWTEC.2019.08.029)
[org/10.1016/J.POWTEC.2019.08.029.](https://doi.org/10.1016/J.POWTEC.2019.08.029)
An, K., Li, K., Yang, C.-M., Brechtl, J., Nawaz, K., 2023. A comprehensive review on
[regeneration strategies for direct air capture. J. CO2 Util. 76. https://doi.org/](https://doi.org/10.1016/j.jcou.2023.102587)
[10.1016/j.jcou.2023.102587.](https://doi.org/10.1016/j.jcou.2023.102587)
Baamran, K., Muldoon, P., Damodaran, K., Banerjee, S., Kim, K.-J., Steckel, J.A.,
Sekizkardes, A.K., 2025. Propylamine functionalized porous fiber sorbents with high
[oxidation stability for direct air capture. Sep. Purif. Technol. 370, 133186. https://](https://doi.org/10.1016/j.seppur.2025.133186)
[doi.org/10.1016/j.seppur.2025.133186.](https://doi.org/10.1016/j.seppur.2025.133186)
Baker, J., Muldoon, P., Steckel, J.A., Sekizkardes, A.K., 2024. Porous polyvinylamine
adsorbents with low temperature regenerability for direct air capture. ACS Appl.
[Polym. Mater. 6, 14278–14282. https://doi.org/10.1021/acsapm.4c02641.](https://doi.org/10.1021/acsapm.4c02641)
Balasubramaniam, B., Thierry, P.-T., Lethier, S., Pugnet, V., Llewellyn, P., Rajendran, A.,
2024. Process-performance of solid sorbents for Direct Air capture (DAC) of CO2 in
optimized temperature-vacuum swing adsorption (TVSA) cycles. Chem. Eng. J. 485,
[149568. https://doi.org/10.1016/j.cej.2024.149568.](https://doi.org/10.1016/j.cej.2024.149568)
Beaumont, M.L., Thirkettle, A.C., 2020. Method and device for the reversible adsorption
of carbon dioxide.
Biegler, L.T., 2024. The trust region filter strategy: survey of a rigorous approach for
[optimization with surrogate models. Digit. Chem. Eng. 13, 100197. https://doi.org/](https://doi.org/10.1016/j.dche.2024.100197)
[10.1016/j.dche.2024.100197.](https://doi.org/10.1016/j.dche.2024.100197)
Biegler, L.T., Lang, Y., Lin, W., 2014. Multi-scale optimization for process systems
[engineering. Comput. Chem. Eng. 60, 17–30. https://doi.org/10.1016/j.](https://doi.org/10.1016/j.compchemeng.2013.07.009)
[compchemeng.2013.07.009.](https://doi.org/10.1016/j.compchemeng.2013.07.009)
Borker, N.S., Herdtle, T., Sauer, C., Romdhane, I.H., Pekurovsky, M., 2024. Engineering
design of direct-air-capture contactors composed of sorbent particles using
[numerical simulations. AIChE J. 70, e18303. https://doi.org/10.1002/aic.18303.](https://doi.org/10.1002/aic.18303)
Bose, S., Sengupta, D., Rayder, T.M., Wang, X., Kirlikovali, K.O., Sekizkardes, A.K.,
Islamoglu, T., Farha, O.K., 2024. Challenges and opportunities: metal–Organic
[frameworks for direct air capture. Adv. Funct. Mater. 34, 2307478. https://doi.org/](https://doi.org/10.1002/adfm.202307478)
[10.1002/adfm.202307478.](https://doi.org/10.1002/adfm.202307478)
Bouaboula, H., Chaouki, J., Belmabkhout, Y., Zaabout, A., 2024. Comparative review of
direct air capture technologies: from technical, commercial, economic, and
[environmental aspects. Chem. Eng. J. 484, 149411. https://doi.org/10.1016/j.](https://doi.org/10.1016/j.cej.2024.149411)
[cej.2024.149411.](https://doi.org/10.1016/j.cej.2024.149411)
Castonguay, S.T., Roy, P., Sun, Y., Aubry, S., Foley, B., Glascoe, E.A., Sharma, H.N., 2023.
Modeling diffusion and types I-V sorption of water vapor in heterogeneous systems.
[Chem. Eng. Sci. 275, 118695. https://doi.org/10.1016/J.CES.2023.118695.](https://doi.org/10.1016/J.CES.2023.118695)
Chauvy, R., Dubois, L., 2022. Life cycle and techno-economic assessments of direct
aircapture processes: an integrated review. Int. J. Energy Res. 46, 10320–10344.
[https://doi.org/10.1002/er.7884.](https://doi.org/10.1002/er.7884)
Chen, X., Wu, K., Bai, A., Masuku, C.M., Niederberger, J., Liporace, F.S., Biegler, L.T.,
2021. Real-time refinery optimization with reduced-order fluidized catalytic cracker
model and surrogate-based trust region filter method. Comput. Chem. Eng. 153,
[107455. https://doi.org/10.1016/j.compchemeng.2021.107455.](https://doi.org/10.1016/j.compchemeng.2021.107455)
Comsol Multiphysics, O.R., 2020. User’s Guide.
Darunte, L., Walton, K., Sholl, D., Jones, C., 2016. CO2 capture via adsorption in amine[functionalized sorbents. Curr. Opin. Chem. Eng. 12, 82–90. https://doi.org/](https://doi.org/10.1016/j.coche.2016.03.002)
[10.1016/j.coche.2016.03.002.](https://doi.org/10.1016/j.coche.2016.03.002)
Darunte, L.A., Sen, T., Bhawanani, C., Walton, K.S., Sholl, D.S., Realff, M.J., Jones, C.W.,
2019. Moving beyond adsorption capacity in design of adsorbents for CO2 capture
from ultradilute feeds: kinetics of CO2 adsorption in materials with stepped
[isotherms. Ind. Eng. Chem. Res. 58, 366–377. https://doi.org/10.1021/acs.](https://doi.org/10.1021/acs.iecr.8b05042)
[iecr.8b05042.](https://doi.org/10.1021/acs.iecr.8b05042)
Davis, J., Rochelle, G., 2009. Thermal degradation of monoethanolamine at stripper
[conditions. Energy Procedia 1, 327–333. https://doi.org/10.1016/j.](https://doi.org/10.1016/j.egypro.2009.01.045)
[egypro.2009.01.045.](https://doi.org/10.1016/j.egypro.2009.01.045)
Dosso, C., Pedrozo, H.A., Tran, T., Zhu, L., Kusuma, V., Hopkinson, D., Biegler, L.T.,
Panagakos, G., 2025. A computational investigation of high-flux, plate-and-frame
membrane modules for industrial carbon capture. Digit. Chem. Eng. 16, 100246.
[https://doi.org/10.1016/j.dche.2025.100246.](https://doi.org/10.1016/j.dche.2025.100246)
Dowson, G.R.M., Reed, D.G., Bellas, J.M., Charalambous, C., Styring, P., 2016. Fast and
selective separation of carbon dioxide from dilute streams by pressure swing
[adsorption using solid ionic liquids. Faraday Discuss. 192, 511–527. https://doi.org/](https://doi.org/10.1039/C6FD00035E)
[10.1039/C6FD00035E.](https://doi.org/10.1039/C6FD00035E)



Eason, J.P., Biegler, L.T., 2018. Advanced trust region optimization strategies for glass
[box/black box models. AIChE J. 64, 3934–3943. https://doi.org/10.1002/](https://doi.org/10.1002/aic.16364)
[aic.16364.](https://doi.org/10.1002/aic.16364)
Elfving, J., Kauppinen, J., Jegoroff, M., Ruuskanen, V., Jarvinen, L., Sainio, T., 2021.
Experimental comparison of regeneration methods for CO2 concentration from air
[using amine-based adsorbent. Chem. Eng. J. 404, 126337. https://doi.org/10.1016/](https://doi.org/10.1016/j.cej.2020.126337)
[j.cej.2020.126337.](https://doi.org/10.1016/j.cej.2020.126337)
Elfving, J., Sainio, T., 2021. Kinetic approach to modelling CO2 adsorption from humid
air using amine-functionalized resin: equilibrium isotherms and column dynamics.
[Chem. Eng. Sci. 246, 116885. https://doi.org/10.1016/j.ces.2021.116885.](https://doi.org/10.1016/j.ces.2021.116885)
Gholami, M., Van Assche, T.R.C., Denayer, J.F.M., 2023. Temperature vacuum swing, a
combined adsorption cycle for carbon capture. Curr. Opin. Chem. Eng. 39, 100891.
[https://doi.org/10.1016/j.coche.2022.100891.](https://doi.org/10.1016/j.coche.2022.100891)
Hedin, N., Andersson, L., Bergstrom, L., Yan, J., 2013. Adsorbents for the postcombustion capture of CO2 using rapid temperature swing or vacuum swing
[adsorption. Appl. Energy 104, 418–433. https://doi.org/10.1016/j.](https://doi.org/10.1016/j.apenergy.2012.11.034)
[apenergy.2012.11.034.](https://doi.org/10.1016/j.apenergy.2012.11.034)
Hefti, M., Mazzotti, M., 2014. Modeling water vapor adsorption/desorption cycles.
[Adsorption 20, 359–371. https://doi.org/10.1007/S10450-013-9573-9.](https://doi.org/10.1007/S10450-013-9573-9)
[Hennig, J., Elfner, M., Maeder, A., Feder, J., 2023. MPh-py/MPh: 1.2.3. https://doi.](https://doi.org/10.5281/ZENODO.7749502)
[org/10.5281/ZENODO.7749502.](https://doi.org/10.5281/ZENODO.7749502)
Holewinski, A., Sakwa-Novak, M.A., Carrillo, J.M.Y., Potter, M.E., Ellebracht, N.,
Rother, G., Sumpter, B.G., Jones, C.W., 2017. Aminopolymer mobility and support
interactions in silica-PEI composites for CO2 capture applications: a quasielastic
[neutron scattering study. J. Phys. Chem. B 121, 6721–6731. https://doi.org/](https://doi.org/10.1021/ACS.JPCB.7B04106)
[10.1021/ACS.JPCB.7B04106.](https://doi.org/10.1021/ACS.JPCB.7B04106)
Huckaby, D., 2022. Forming the future of direct air capture: CFD for direct air capture.
Hughes, R., Kotamreddy, G., Bhattacharyya, D., Parker, S.T., Dods, M.N., Long, J.R.,
Omell, B., Matuszewski, M., 2024a. Development of a chemistry-based isotherm
model and techno-economic optimization of a moving bed process for CO2 capture
using a functionalized metal-organic framework. Chem. Eng. Sci. 287, 119679.
[https://doi.org/10.1016/j.ces.2023.119679.](https://doi.org/10.1016/j.ces.2023.119679)
Hughes, R., Kotamreddy, G., Ostace, A., Bhattacharyya, D., Siegelman, R.L., Parker, S.T.,
Didas, S.A., Long, J.R., Omell, B., Matuszewski, M., 2021. Isotherm, kinetic, process
modeling, and techno-economic analysis of a diamine-appended metal–organic
framework for CO2 capture using fixed bed contactors. Energy Fuels 35, 6040–6055.
[https://doi.org/10.1021/acs.energyfuels.0c04359.](https://doi.org/10.1021/acs.energyfuels.0c04359)
Hughes, R., Yancy-Caballero, D., Zamarripa-Perez, M., Omell, B., Matuszewski, M.,
Bhattacharyya, D., 2024b. Modeling and techno-economic optimization of a
tetraamine-appended metal–Organic framework for NGCC-based CO2 capture using
[fixed bed contactors. Energy Fuels 38, 2511–2524. https://doi.org/10.1021/acs.](https://doi.org/10.1021/acs.energyfuels.3c03802)
[energyfuels.3c03802.](https://doi.org/10.1021/acs.energyfuels.3c03802)
Ji, Y., Liu, W., Yong, J.Y., Zhang, X.J., Jiang, L., 2024. Techno-economic analysis on
temperature vacuum swing adsorption system integrated with pre-dehumidification
[for direct air capture. Carbon Capture Sci. Technol. 12, 100199. https://doi.org/](https://doi.org/10.1016/j.ccst.2024.100199)
[10.1016/j.ccst.2024.100199.](https://doi.org/10.1016/j.ccst.2024.100199)
Ji, Y., Yong, J., Liu, W., Zhang, X., Jiang, L., 2023. Thermodynamic analysis on direct air
capture for building air condition system: balance between adsorbent and
[refrigerant. Energy Built Environ. 4, 399–407. https://doi.org/10.1016/j.](https://doi.org/10.1016/j.enbenv.2022.02.009)
[enbenv.2022.02.009.](https://doi.org/10.1016/j.enbenv.2022.02.009)
Jue, M.L., Ellebracht, N.C., Rasmussen, M.J., Hunter-Sellars, E., Marple, M.A.T., Yung, M.
M., Pang, S.H., 2024. Improving the direct air capture capacity of grafted amines via
[thermal treatment. Chem. Commun. 60, 7077–7080. https://doi.org/10.1039/](https://doi.org/10.1039/D4CC01634C)
[D4CC01634C.](https://doi.org/10.1039/D4CC01634C)
Keith, D.W., Holmes, G., Angelo St, D., Heidel, K., 2018. A process for capturing CO2
[from the atmosphere. Joule 2, 1573–1594. https://doi.org/10.1016/j.](https://doi.org/10.1016/j.joule.2018.05.006)
[joule.2018.05.006.](https://doi.org/10.1016/j.joule.2018.05.006)
[Kim, S., L´eonard, G., 2022. Performance and sensitivity analysis of direct air capture](http://refhub.elsevier.com/S0098-1354(25)00382-5/sbref0040)
[(DAC) model using solid amine sorbents for CO2 capture. In: 16th Int. Conf. Greenh.](http://refhub.elsevier.com/S0098-1354(25)00382-5/sbref0040)
[Gas Control Technol. GHGT-16.](http://refhub.elsevier.com/S0098-1354(25)00382-5/sbref0040)
Liang, R., Han, Y., Hu, H., Chen, B., Yuan, Z., Biegler, L.T., 2024. Efficient trust region
filter modeling strategies for computationally expensive black-box optimization.
[Comput. Chem. Eng. 189, 108816. https://doi.org/10.1016/j.](https://doi.org/10.1016/j.compchemeng.2024.108816)
[compchemeng.2024.108816.](https://doi.org/10.1016/j.compchemeng.2024.108816)
Lin, T.Y., Moore, T., Nguyen, D., Roy, P., Dudukovic, N.A., Seung, K., Troksa, M.,
Walton, R.L., Hahn, C., Duoss, E.B., Baker, S., 2024. Advancing carbon capture from
bench to pilot scale using dynamic similitude. Cell Rep. Phys. Sci. 5, 102019.
[https://doi.org/10.1016/J.XCRP.2024.102019.](https://doi.org/10.1016/J.XCRP.2024.102019)
Liu, S., Zhang, J., Li, F., Edwards, J., Xiao, Y., Kim, D., Papangelakis, P., Kim, J.,
Elder, D., De Luna, P., Fan, M., Lee, G., Miao, R.K., Ghosh, T., Yan, Y., Chen, Y.,
Zhao, Y., Guo, Z., Tian, C., Li, P., Xu, Y., Sargent, E., Sinton, D., 2023. Direct air
capture of CO2 via cyclic viologen electrocatalysis. Energy Environ. Sci. 17,
[1266–1278. https://doi.org/10.1039/D3EE03024E.](https://doi.org/10.1039/D3EE03024E)
Luukkonen, A., Elfving, J., Inkeri, E., 2023. Improving adsorption-based direct air
capture performance through operating parameter optimization. Chem. Eng. J. 471,
[144525. https://doi.org/10.1016/j.cej.2023.144525.](https://doi.org/10.1016/j.cej.2023.144525)
Mariniˇc, D., Likozar, B., 2023. Direct air capture multiscale modelling: from capture
[material optimization to process simulations. J. Clean. Prod. 408, 137185. https://](https://doi.org/10.1016/j.jclepro.2023.137185)
[doi.org/10.1016/j.jclepro.2023.137185.](https://doi.org/10.1016/j.jclepro.2023.137185)
McQueen, N., Vaz Gomez, K., McCormick, C., Blumanthal, K., Pisciotta, M., Wilcox, J.,
2021. A review of direct air capture (DAC): scaling up commercial technologies and
[innovating for the future. Prog. Energy 3, 032001. https://doi.org/10.1088/2516-](https://doi.org/10.1088/2516-1083/abf1ce)
[1083/abf1ce.](https://doi.org/10.1088/2516-1083/abf1ce)
Muldoon, P.F., Budhathoki, S., Sekizkardes, A.K., Soilis, Z.M., Rosi, N.L., Sorescu, D.C.,
Steckel, J.A., 2025. CO2 Adsorption enhancement in MOF-808 via a highly efficient
[amine incorporation. https://doi.org/10.26434/chemrxiv-2025-rnr8c.](https://doi.org/10.26434/chemrxiv-2025-rnr8c)



17


_H.A. Pedrozo et al.                                                                                                               Computers_ _and_ _Chemical_ _Engineering_ _204_ _(2026)_ _109379_



[Murali, R.S., Sankarshana, T., Sridhar, S., 2013. Air separation by polymer-based](http://refhub.elsevier.com/S0098-1354(25)00382-5/sbref0048)
[membrane technology. Sep. Purif. Rev. 42, 130–186.](http://refhub.elsevier.com/S0098-1354(25)00382-5/sbref0048)
National Energy Technology Laboratory, 2023. NETL launches multidisciplinary project
to advance direct air capture technology.
[Pacala, S., Al-Kaisi, M., Barteau, M., Belmont, E., Benson, S., Birdsey, R., Boysen, D.,](http://refhub.elsevier.com/S0098-1354(25)00382-5/sbref0050)
[Duren, R., Hopkinson, C., Jones, C., 2018. Negative Emissions Technologies and](http://refhub.elsevier.com/S0098-1354(25)00382-5/sbref0050)
[Reliable sequestration: a Research Agenda. Natl. Acad. Sci. Eng. Med, Washington,](http://refhub.elsevier.com/S0098-1354(25)00382-5/sbref0050)
[DC, USA.](http://refhub.elsevier.com/S0098-1354(25)00382-5/sbref0050)
Pedrozo, H.A., Dosso, C., Zhu, L., Kusuma, V., Hopkinson, D., Biegler, L.T.,
Panagakos, G., 2024a. Membrane-based carbon capture process optimization using
[CFD modeling. Syst. Control Trans. 3, 860–867. https://doi.org/10.69997/](https://doi.org/10.69997/sct.134891)
[sct.134891.](https://doi.org/10.69997/sct.134891)
Pedrozo, H.A., Panagakos, G., Biegler, L.T., 2024b. Computational fluid dynamics and
trust-region methods to optimize carbon capture plants with membrane contactors.
Eds.. In: Manenti, F., Reklaitis, G.V.B.T.-C.A.C.E. (Eds.), 34 European Symposium on
Computer Aided Process Engineering /15 International Symposium on Process
[Systems Engineering. Elsevier, pp. 175–180. https://doi.org/10.1016/B978-0-443-](https://doi.org/10.1016/B978-0-443-28824-1.50030-2)
[28824-1.50030-2.](https://doi.org/10.1016/B978-0-443-28824-1.50030-2)
Pedrozo, H.A., Panagakos, G., Biegler, L.T., 2024c. Including CFD rigorous models in the
optimal design of carbon capture plants through trust-region methods. Chem. Eng.
[Sci. 286, 119646. https://doi.org/10.1016/j.ces.2023.119646.](https://doi.org/10.1016/j.ces.2023.119646)
Postweiler, P., Engelpracht, M., Rezo, D., Gibelhaus, A., von der Assen, N., 2024.
Environmental process optimisation of an adsorption-based direct air carbon capture
[and storage system. Energy Environ. Sci. 17, 3004–3020. https://doi.org/10.1039/](https://doi.org/10.1039/D3EE02970K)
[D3EE02970K.](https://doi.org/10.1039/D3EE02970K)
Priyadarshini, P., Rim, G., Rosu, C., Song, M.G., Jones, C.W., 2023. Direct air capture of
CO2 using Amine/alumina sorbents at cold temperature. ACS Environ. Au 3,
[295–307. https://doi.org/10.1021/ACSENVIRONAU.3C00010.](https://doi.org/10.1021/ACSENVIRONAU.3C00010)
Quirijns, E.J., van Boxtel, A.J.B., van Loon, W.K.P., van Straten, G., 2005. Sorption
isotherms, GAB parameters and isosteric heat of sorption. J. Sci. Food Agric. 85,
[1805–1814. https://doi.org/10.1002/jsfa.2140.](https://doi.org/10.1002/jsfa.2140)
Rezo, D., Postweiler, P., Engelpracht, M., Meuleneers, L., von der Aßen, N., 2024.
A method for siting adsorption-based direct air carbon capture and storage plants for
[maximum CO2 removal. Carbon Neutrality 3, 1–15. https://doi.org/10.1007/](https://doi.org/10.1007/S43979-024-00100-Z/FIGURES/9)
[S43979-024-00100-Z/FIGURES/9.](https://doi.org/10.1007/S43979-024-00100-Z/FIGURES/9)
Rivero, J.R., Nemetz, L.R., Da Conceicao, M.M., Lipscomb, G., Hornbostel, K., 2023.
Modeling gas separation in flat sheet membrane modules: impact of flow channel
[size variation. Carbon Capture Sci. Technol. 6, 100093. https://doi.org/10.1016/J.](https://doi.org/10.1016/J.CCST.2022.100093)
[CCST.2022.100093.](https://doi.org/10.1016/J.CCST.2022.100093)
Rivero, J.R., Panagakos, G., Lieber, A., Hornbostel, K., 2020. Hollow Fiber membrane
contactors for post-combustion carbon capture: a review of modeling approaches.
[Membranes (Basel) 10, 382. https://doi.org/10.3390/membranes10120382.](https://doi.org/10.3390/membranes10120382)
Roy, P., Castonguay, S.T., Knipe, J.M., Sun, Y., Glascoe, E.A., Sharma, H.N., 2022. Multimaterial modeling of sorption-desorption processes with experimental validation.
[Chem. Eng. Sci. 253, 117542. https://doi.org/10.1016/J.CES.2022.117542.](https://doi.org/10.1016/J.CES.2022.117542)
Ruiz-Mercado, G.J., Smith, R.L., Gonzalez, M.A., 2014. Appendix C: GREENSCOPE
Technical User’s Guide - web-based version beta.
[Ruthven, D.M., 1984. Dynamics of adsorption columns: single-transition systems. Princ.](http://refhub.elsevier.com/S0098-1354(25)00382-5/sbref0062)
[Adsorpt. Adsorpt. Process. 433.](http://refhub.elsevier.com/S0098-1354(25)00382-5/sbref0062)
Sabatino, F., Grimm, A., Gallucci, F., van Sint Annaland, M., Kramer, G.J., Gazzani, M.,
2021. A comparative energy and costs assessment and optimization for direct air
[capture technologies. Joule 5, 2047–2076. https://doi.org/10.1016/j.](https://doi.org/10.1016/j.joule.2021.05.023)
[joule.2021.05.023.](https://doi.org/10.1016/j.joule.2021.05.023)
Schellevis, H., de la Comb´e, J., Brilman, D., 2024. Optimizing direct air capture under
[varying weather conditions. Energy Adv. 3, 1678–1687. https://doi.org/10.1039/](https://doi.org/10.1039/D4YA00200H)
[D4YA00200H.](https://doi.org/10.1039/D4YA00200H)
Schellevis, H.M., van Schagen, T.N., Brilman, D.W.F., 2021. Process optimization of a
fixed bed reactor system for direct air capture. Int. J. Greenh. Gas Control 110,
[103431. https://doi.org/10.1016/J.IJGGC.2021.103431.](https://doi.org/10.1016/J.IJGGC.2021.103431)
SciPy, 2022. SciPy User Guide.
Shah, Y.G., Jackson, A.C., Tsouris, C., Finney, C.E.A., Panagakos, G., 2025. Multiphase
computational fluid dynamics modeling of reacting flows in absorption columns for
[carbon capture. Digit. Chem. Eng. 16, 100252. https://doi.org/10.1016/j.](https://doi.org/10.1016/j.dche.2025.100252)
[dche.2025.100252.](https://doi.org/10.1016/j.dche.2025.100252)



Sidhareddy, M., Tiwari, S., Bellos, E., 2023. Investigation on regeneration of zeolite 13Xwater adsorbent bed under vacuum condition: a computational approach. Therm.
[Sci. Eng. Prog. 46, 102243. https://doi.org/10.1016/j.tsep.2023.102243.](https://doi.org/10.1016/j.tsep.2023.102243)
Sievert, K., Schmidt, T.S., Steffen, B., 2024. Considering technology characteristics to
[project future costs of direct air capture. Joule 8, 979–999. https://doi.org/10.1016/](https://doi.org/10.1016/j.joule.2024.02.005)
[j.joule.2024.02.005.](https://doi.org/10.1016/j.joule.2024.02.005)
Singh, R., Romero-Gomez, P., Richmond, M., Harding, S., Perkins, W., 2019. CFD tools
for characterizing particle passage through an idealized hydro-turbine model. APS
S37.005.
Singh, R.K., Fu, Y., Zeng, C., Nguyen, D.T., Roy, P., Bao, J., Xu, Z., Panagakos, G., 2022.
Hydrodynamics of countercurrent flow in an additive-manufactured column with
triply periodic minimal surfaces for carbon dioxide capture. Chem. Eng. J. 450,
[138124. https://doi.org/10.1016/j.cej.2022.138124.](https://doi.org/10.1016/j.cej.2022.138124)
Sinha, A., Darunte, L., Jones, C., Realff, M., Kawajiri, Y., 2016. Systems design and
economic analysis of direct air capture of CO2 through temperature vacuum swing
adsorption using MIL-101(Cr)-PEI-800 and mmen-Mg2(dobpdc) MOF adsorbents.
[Ind. Eng. Chem. Res. 56, 750–764. https://doi.org/10.1021/acs.iecr.6b03887.](https://doi.org/10.1021/acs.iecr.6b03887)
Smith, R.L., Ruiz-Mercado, G.J., 2014. A method for decision making using sustainability
[indicators. Clean Technol. Environ. Policy 16, 749–755. https://doi.org/10.1007/](https://doi.org/10.1007/S10098-013-0684-5)
[S10098-013-0684-5.](https://doi.org/10.1007/S10098-013-0684-5)
Stampi-Bombelli, V., van der Spek, M., Mazzotti, M., 2020. Analysis of direct capture of
[CO2 from ambient air via steam‑assisted. Adsorption 26, 1183–1197. https://doi.](https://doi.org/10.1007/s10450-021-00351-7)
[org/10.1007/s10450-021-00351-7.](https://doi.org/10.1007/s10450-021-00351-7)
Sun, L., Panagakos, G., Lipscomb, G., 2024. Effect of hollow fiber membrane packing on
the performance of modules formedwith fiber tows. Sep. Sci. Technol. 60, 267–281.
[https://doi.org/10.1080/01496395.2024.2424953.](https://doi.org/10.1080/01496395.2024.2424953)
Sun, L., Panagakos, G., Lipscomb, G., 2022. Effect of Packing Nonuniformity At the Fiber
Bundle&Ndash;Case Interface on Performance of Hollow Fiber Membrane Gas
[Separation Modules. Membranes (Basel). https://doi.org/10.3390/](https://doi.org/10.3390/membranes12111139)
[membranes12111139.](https://doi.org/10.3390/membranes12111139)
Surkatti, R., Abdullatif, Y., Muhammad, R., Sodiq, A., Mroue, K., Al-ansari, T.,
Amhamed, A., 2025. Comparative analysis of amine-functionalized silica for direct
air capture (DAC): material characterization, performance, and thermodynamic
[efficiency. Sep. Purif. Technol. 354, 128641. https://doi.org/10.1016/j.](https://doi.org/10.1016/j.seppur.2024.128641)
[seppur.2024.128641.](https://doi.org/10.1016/j.seppur.2024.128641)
Tao, Y., Xu, H., 2024. A critical review on potential applications of Metal-organic
frameworks (MOFs) in adsorptive carbon capture technologies.
Valverde, A., Griffiths, I.M., 2024. The role of adsorbent microstructure and its packing
arrangement in optimising the performance of an adsorption column. Discov. Chem.
[Eng. 4, 27. https://doi.org/10.1007/s43938-024-00064-7.](https://doi.org/10.1007/s43938-024-00064-7)
Ward, A., Papathanasiou, M., Pini, R., 2024. The impact of design and operational
parameters on the optimal performance of direct air capture units using solid
[sorbents. Adsorption 30, 1829–1848. https://doi.org/10.1007/s10450-024-00526-](https://doi.org/10.1007/s10450-024-00526-y)
[y.](https://doi.org/10.1007/s10450-024-00526-y)
World Economic Forum, 2024. Carbon dioxide removal: best-practice guidelines.
Young, J., García-Díez, E., Garcia, S., Van Der Spek, M., 2021. The impact of binary
water–CO 2 isotherm models on the optimal performance of sorbent-based direct air
[capture processes. Energy Environ. Sci. 14, 5377–5394. https://doi.org/10.1039/](https://doi.org/10.1039/D1EE01272J)
[D1EE01272J.](https://doi.org/10.1039/D1EE01272J)
Young, J., McQueen, N., Charalambous, C., Foteinis, S., Hawrot, O., Ojeda, M.,
Pilorg´e, H., Andresen, J., Psarras, P., Renforth, P., Garcia, S., van der Spek, M., 2023.
The cost of direct air capture and storage can be reduced via strategic deployment
[but is unlikely to fall below stated cost targets. One Earth 6, 899–917. https://doi.](https://doi.org/10.1016/j.oneear.2023.06.004)
[org/10.1016/j.oneear.2023.06.004.](https://doi.org/10.1016/j.oneear.2023.06.004)
Zhang, L., Yue, J., 2025. Packed Bed Microreactors For Sustainable Chemistry and
[Process Development. Chemistry (Easton). https://doi.org/10.3390/](https://doi.org/10.3390/chemistry7020029)
[chemistry7020029.](https://doi.org/10.3390/chemistry7020029)
Zhu, J., Cui, X., Araya, S.S., 2022. Comparison between 1D and 2D numerical models of a
multi-tubular packed-bed reactor for methanol steam reforming. Int. J. Hydrogen
[Energy 47, 22704–22719. https://doi.org/10.1016/j.ijhydene.2022.05.109.](https://doi.org/10.1016/j.ijhydene.2022.05.109)
Zhu, X., Ge, T., Yang, F., Wang, R., 2021. Design of steam-assisted temperature vacuumswing adsorption processes for efficient CO2 capture from ambient air. Renew.
[Sustain. Energy Rev. 137, 110651. https://doi.org/10.1016/j.rser.2020.110651.](https://doi.org/10.1016/j.rser.2020.110651)



18



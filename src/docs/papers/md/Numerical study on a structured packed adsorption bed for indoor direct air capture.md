[Energy 282 (2023) 128801](https://doi.org/10.1016/j.energy.2023.128801)


Contents lists available at ScienceDirect
# Energy


[journal homepage: www.elsevier.com/locate/energy](https://www.elsevier.com/locate/energy)

## Numerical study on a structured packed adsorption bed for indoor direct air capture

S. Chen [a], W.K. Shi [a], J.Y. Yong [a], Y. Zhuang [a], Q.Y. Lin [b], N. Gao [c], X.J. Zhang [a][,] [b], L. Jiang [a][,][b][,][* ]

a _Key Laboratory of Refrigeration and Cryogenic Technology of Zhejiang Province, Institute of Refrigeration and Cryogenics, Zhejiang University, Hangzhou, 310027,_
_China_
b _Jiaxing Research Institute, Zhejiang University, 1300 Dongshengxilu Road, Jiaxing, 314031, China_
c _Institute of Energy and Environment Engineering, NingboTech University, Ningbo, Zhejiang Province, 315000, China_



A R T I C L E I N F O


_Keywords:_
Direct air capture
Adsorption
Energy consumption
Building


**1.** **Introduction**



A B S T R A C T


Direct air capture (DAC) for indoor CO2 removal can not only effectively regulate air quality but also improve the
capture efficiency to a certain extent, which is a highly feasible win-win solution to decarbonization and human
health. This paper proposes a W-shaped packed adsorption bed for indoor direct capture which is optimized and
compared with the conventional bed. Firstly, the pressure drop of different adsorption beds is simulated by
Darcy-Fochheimer law. The results demonstrate that pressure drop of the W-shaped bed performs better than the
conventional adsorption bed. Then temperature swing adsorption process is investigated using an amine func­
tionalization material. It is indicated that energy consumption of the conventional packed bed and the W-shaped
packed bed are 236.2 kJ mol [−] [1 ] and 167.9 kJ mol [−] [1 ] for CO2 capture process, respectively. Because of the lower
pressure drop of the W-shaped bed, energy consumption of fan could be greatly reduced from 88.7 kJ mol [−] [1 ] to
15.1 kJ mol [−] [1] . Finally, a simple indoor CO2 concentration condition model coupled with the reactor CFD model
is established to verify the performance of CO2 purification of the reactor, and it shows an excellent regulatory
effect on indoor CO2. The concept can provide some valuable insights for DAC in buildings and have the potential
of coupling application with various carbon capture systems.



The global average temperature has been steadily increasing, with a
rise of 1.15 [◦] C compared to pre-industrial times [1]. Greenhouse gas
(GHG) aggravates global climate change. It brings severe challenges to
global climate governance, and the primary source of GHG is CO2, which
plays a dominant role and contributes 63% to global warming [2]. In
response to the plan of The Paris Agreement on global climate gover­
nance, low-carbon and zero-carbon fuels are the main solutions to
reducing CO2 emissions [3,4]. Besides, the technology of Carbon Cap­
ture, Utilization, and Storage (CCUS) is considered one of the most
promising choices, which includes capturing CO2 from concentrated
point sources or ambient air, injecting CO2 into permeable subsurface
rock formations in storage, or using for other usages [5,6]. For carbon
capture technology, the mainstream methods in the past focused on
capturing CO2 from concentrated point sources such as fossil fuel power
plants and furnaces [7]. On the other hand, capturing CO2 from ambient



air, commonly known as direct air capture (DAC), has relatively few
applications because of its drawback of high energy consumption [8,9].
However, to meet the goal of “well below 2 [◦] C″, there is still a sizeable
negative emission demand of 10 Gt CO2 in the first half of the 21st
century [10,11]. Thus DAC, a negative carbon technology that removes
CO2 from the atmosphere, is regarded essential to achieve the goal of
negative emissions [12,13].
Direct air capture aims to separate CO2 from the atmosphere directly
and has great potential to solve the carbon emissions from distributed
carbon sources, accounting for roughly 40% of total emissions [14].
According to relevant thermodynamic theoretical analysis, a higher
theoretical minimum work is required to separate CO2 from the air
comparing with the gas capture [15]. One of the main challenges for
DAC is finding superior separation methods with low energy penalties.
Sorption methods are the mainstream carbon capture paths, including
absorption and adsorption [5]. The former has relatively mature appli­
cations, including alkali solution absorption and solid alkali sorbents,
while the latter has the advantage of lower energy penalty and is




 - Corresponding author. Key Laboratory of Refrigeration and Cryogenic Technology of Zhejiang Province, Institute of Refrigeration and Cryogenics. Zhejiang
University, Hangzhou, 310027, China.
_E-mail address:_ [jianglong@zju.edu.cn (L. Jiang).](mailto:jianglong@zju.edu.cn)

[https://doi.org/10.1016/j.energy.2023.128801](https://doi.org/10.1016/j.energy.2023.128801)
Received 29 April 2023; Received in revised form 23 July 2023; Accepted 16 August 2023

Available online 26 August 2023
0360-5442/© 2023 Elsevier Ltd. All rights reserved.


_S. Chen et al.                                                                                                                  Energy 282 (2023) 128801_



**Nomenclature**



_ρ_ density, kg⋅m [−] [3 ]

_**u**_ velocity, m⋅s [−] [1 ]



_d_ p diameter of particle, m
_C_ 2 inertial resistance, m [−] [1 ]



_k_ turbulent kinetic rate, J
_**J**_ i diffusion flux, kg⋅m [−] [2] ⋅s [−] [1 ]



_D_ i _,_ m diffusion of mass, kg⋅m [−] [2] ⋅s [−] [1 ]



_q_ L Langmuir maximum capacity, mol⋅kg [−] [1 ]



_q_ H DSL maximum capacity, mol⋅kg [−] [1 ]



_k_ i linear driving force reaction rate constant, s [−] [1 ]



_R_ ideal gas constant, J⋅mol [−] [1] ⋅K [−] [1 ]



_C_ concentration, mol m [−] [3 ]



Δ _H_ i heat of reaction, kJ⋅mol [−] [1 ]

_P_ pressure, Pa
_E_ fan energy of fan, kJ
_E_ desorption energy of desorption, kJ
_E_ compressor energy of compressor, kJ



thought to be a promising direction [5]. In the low-pressure applications
corresponding to DAC, zeolite and metal-organic frameworks (MOFs)
have been verified to have relatively good adsorption performance [16,
17]. Adsorption materials are loaded in the DAC system and will work in
cycles under a specific process. The general design includes temperature
swing adsorption (TSA) [18], vacuum swing adsorption (VSA) [19],
electric swing adsorption (ESA), etc. Scholars in relevant fields have
conducted much research on this series of processes and have obtained a
certain understanding of their basic performance [20,21]. It is attractive
that TSA requires a simple system and equipment, even though the
production CO2 with lower purity is obtained. In contrast, VSA needs
extremely low vacuum levels, which is unsuitable for application [22].
Moreover, temperature-vacuum swing adsorption (TVSA) process, the
combination of TSA and VSA, is considered an efficient method and is
used for research and applications [19,21].
There are various experimental and simulation studies on carbon
capture in terms of various pressure and temperature swing adsorption
processes [23,24]. For simulation, reasonable numerical modeling of
adsorption process is significant for the whole study. Computational
fluid dynamics (CFD) is an important means due to the complex shapes
of practical adsorption beds. Ben et al. [23] used CFD to simulate the
working performance of Mg-MOF-74 for TSA process. The study
compared the numerical differences among 1D model (direct numerical
calculation) and 2D model and 3D model (CFD calculation). After
comparing and verifying the experimental results, it was found that the
results calculated by 3D model were closer to testing data. For the sys­
tems with special-shaped reactors, it is difficult to describe with a
one-dimensional mathematical model, and CFD calculation is more
necessary. Wen et al. [24] studied a rotating packed bed with a novel
adsorbent array using CFD simulation, and the energy consumption
performance of the system was analyzed based on the CFD result. Thus,
CFD model can describe the reactor under the complex conditions more
accurately, and can play an essential role in the simulation research of
CO2 capture. For example, Sandu et al. [25] developed CFD models to
investigate their 3D-printed structured bed reactors. Based on break­
through simulation in CFD model, the optimizations of mass transfer and
pressure drop were numerically validated.
To our best knowledge, DAC can be implemented anywhere and
operated anytime. Its working performance can be boosted under
moderately high ambient CO2 concentrations [26,27]. CO2 concentra­
tion in the building environment is stipulated below 800 ppm, and even
exceed 2000 ppm at poorly vetalited conditions, which may affect
human health [28,29]. The combination of DAC and Heating Ventilation



_Abbreviations_
CCUS carbon capture, utilization, and storage
WHO World Health Organization
CO2 carbon dioxide
DAC direct air capture
HVAC heating, ventilation and air conditioning systems
TSA temperature swing adsorption
TVSA temperature-vacuum swing adsorption
VSA vacuum swing adsorption
ESA electric swing adsorption
GHG greenhouse gas

_Greek letters_
_γ_ porosity
_ε_ turbulent dissipation rate
_α_ permeability, m [2 ]

_χ_ DSL equilibrium weight constant
_η_ eff efficiency of fan


and Air Conditioning (HVAC) could be a novel win-win solution. In
general, carbon capture systems can reduce indoor CO2, volatile organic
compounds and other harmful components. It was reported that the
integration of carbon capture device and HVAC system can save energy
by recirculating indoor air and reducing the ventilation energy for
heating or cooling loads [30]. Kim et al. [30,31] introduced a new
strategy of carbon capture integrated with ventilation, and discussed its
impact on humidity and other factors in detail. Baus et al. [32] proposed
a HVAC-DAC system and calculated the energy saving and air quality
improvement under the recirculation mode. Based on TVSA process, Ji
et al. [33] studied the building DAC system integrated with heat pump,
and the system costs under different capture materials were discussed. In
order to optimize the performance of the bed during adsorption process,
current researches focus on the shape of adsorbents and the internal flow
to enhance mass transfer. For example, Vervloet et al. [34] proposed to
divide the packed bed into the multiple flow channels, and the tubular
fixed bed had better heat and mass transfer performance and pressure
drop. Sandu et al. [25] investigated honeycomb particles using 3D
printing technology and obtained a better mass transfer effect in com­
parison with the conventional particles. Although there are a few re­
searches in these directions, the overall structural design of adsorption
bed is rarely reported, and the conventional packed bed is the main
object of research and application. Considering most of studies, cylin­
drical or square fixed beds are selected [35,36], which indicates DAC
systems still leave a lot of space for the performance improvement.
In this work, we establish a CFD model for adsorption DAC system
under indoor conditions as shown in Fig. 1. The concept of modular
adsorption reactors is shown in Fig. 1, which is widely used in DAC
systems [5]. Previous studies indicate that energy consumption of the
fan account for a large part of the total energy consumption in the
carbon capture process [32,37]. Thus, an improvement of a W-shaped
adsorption bed is proposed to reduce the reactor’s pressure drop for a
low system’s energy consumption. The structure is simulated to inves­
tigate the influence on the overall system performance. Based on the
simulation of the TSA process, adsorption performance and working cost
of DAC reactor are discussed. Besides, indoor CO2 concentration varia­
tion is evaluated while the purification capacity of the device for indoor
CO2 is also verified.



2


_S. Chen et al.                                                                                                                  Energy 282 (2023) 128801_


**Fig. 1.** DAC system using modular adsorption reactors in buildings.


**Fig. 2.** Schematic diagram of (a) DAC reactor packed with W-shaped adsorption bed (b) Concept of the change of the packed bed.


3


_S. Chen et al.                                                                                                                  Energy 282 (2023) 128801_



**2.** **Methodology**


_2.1._ _Adsorption bed design_


The concept of modular adsorption reactors for DAC is presented.
The reactor model is shown in Fig. 2 and the basic parameters for
adsorption reactor is in Table 1. Each reactor has the exact specifica­
tions, greatly facilitating the large-scale production and application. The
main part of the reactor is drawn as a 1.5-m-long cube, with a four-sided
platform structure at both ends, and a pipe with a diameter of 0.8 m is
connected as an inlet for the conveying air. The W-shaped packed bed is
fixed inside the reactor. It is noted that the improvement design is to
sacrifice part of the fill space and change the upwind surface and flow
characteristics at the same time. According to the Darcy-Forchheimer
law, flow pressure drop formed by the airflow through the bed is
correspondingly smaller under the smaller flow distance through the
bed, which is beneficial to reduce energy consumption. Besides, the
windward area of the new structure has been greatly improved [38].
Therefore, despite the filling volume of materials is reduced, the opti­
mized flow characteristics may bring benefits for the overall system
operation to compensate the reduced capacity.


_2.2._ _Numerical model_


In this work, a symmetrical model of the reactor is established. The
W-shaped area is the mian location that adsorption and desorption re­
action takes place, which induces significant variation in gas concen­
trations and pressure. Therefore, we refine the bed grid and conduct
transition meshing of the contact part between the air and the bed.
ANSYS Fluent 19.0 is used to conduct relevant simulations and some
assumptions are provided as follows.


1. The air flow is assumed to be incompressible in the simulation.
2. The incoming flow has been pre-removed from moisture by upstream
equipment, ensuring that the air entering the reactor is dry.
3. A uniform bed considered, where the internal heat and mass transfer
characteristics are isotropic.


Euler single-phase flow and porous media models are used. The
conservation of mass momentum equations are subjected to Reynoldsaveraged Navier-Stokes (RANS) equations as expressed by Eq. (1) and
Eq. (2) [39].

∂ _γρ_ g ( _γρ_ g **u** ) = 0 (1)

∂ _t_ [+ ∇] [⋅]



∇ _T_

**J** i = - _ρD_ i _,_ m∇ _Y_ i − _D_ T _,_ i (9)

_T_

where _D_ i _,_ m is the mass diffusion coefficient for species _i_, _D_ T _,_ i is the
thermal diffusion coefficient for species _i_, _R_ i is the net rate of production
of species _i_ by chemical reaction, _S_ i is the user-defined sources. By
combining adsorption models with the User Defined Function (UDF) of
ANSYS Fluent, a corresponding definition proves to the source term _S_ i.
During a TSA cycle, The packed bed experiences heat generation or
reduction, leading to notable temperature viarations and affecting sub­
sequent reactions. Thus, it is essential to establish rational energy con­
servation in the porous media with a detailed consideration of
adsorption and desorption characteristics, as shown in Eq. (10).



These terms can be calculated separately by Eqs. (3)–(5).



~~_τ_~~ = _μ_




[(
∇ **u** + ∇ **u** [T][)]] - [2] (3)
3 ~~[∇]~~ [⋅] **[u]** _[I]_



)

[j] - [2]

3



(

_ρk_ + _μ_ t∂∂ _ux_ kk



)
_δ_ ij (4)




- _ρ_ g _u_ i [′] _u_ j [′] = _μ_ t



(
∂ _u_ i

∂ _x_ j



+ [∂] _[u]_ [j]

∂ _x_ i



+ [∂] _[u]_ [j]



(
_μ_
_S_ m = - _[C]_ [2]
_α_ ~~_[u]_~~ [i][ +] 2 ~~_[ρ]_~~ [g][|] _[u]_ [i][|] _[u][i]_



)
(5)



where _μ_ is the molecular viscosity, _I_ is the unit tensor, the second term
on the right-hand side in Eq. (3) is the effect of volume dilation. In Eq.
(4), _μ_ t is the turbulent viscosity and k is the turbulent kinetic energy, and
they are continuously calculated by the k- _ε_ model for a turbulent flow.
As the packed bed is loaded with adsorbent particles with an average
diameter of 1 mm, we define it as a porous media zone with _γ_ of the
porosity. The momentum dissipation inside this zone can be character­
ized by viscous resistance [1] _α_ [(or the permeability ] _[α]_ [), and the inertial ]

resistance _C_ 2 according to Egurn model, as shown in Eq. (6) and Eq. (7).



1 [(][1][ −] _[γ]_ [)][2] (6)
_α_ [=][ 150] _d_ p [2] _[γ]_ [3]


_C_ 2 = 1 _._ 75 [(][1][ −] _[γ]_ [)] (7)
_d_ p _γ_ [2]


where _d_ p is the diameter of the particle.
The transport of species is simulated by Eq. (8).


∂

[−∇] [⋅] **[J]** [i][ +] _[ R]_ [i][ +] _[ S]_ [i] (8)
∂ _t_ [(] _[ρ][Y]_ [i][) + ∇] [⋅] [(] _[ρ]_ **[u]** _[Y]_ [i][) =]

The diffusion flux _**J**_ i can be calculated by Eq. (9).




[ ] ( ( )) ( ∑ )
_γρ_ g _E_ g + (1 − _γ_ ) _ρsEs_ + ∇ ⋅ _u_ _ρEg_ + _p_ = ∇ ⋅ _k_ eff∇ _T_ - _h_ i **J** i + ~~_τu_~~



∂



( )
_γρ_ g **u** + ∇ ⋅ ( _γρ_ g **uu** ) = - _γ_ ∇ _p_ + _γρ_ g _g_ + _γ_ ∇ ⋅ ( - _ρ_ g **u** [′] **u** [′] ~~[)]~~ + _γS_ m + _γ_ ∇⋅ ~~_τ_~~ (2)

∂ _t_



∂
∂ _t_



∂ _q_ i

∂ _t_
(10)



∑
Δ _H_ i



where _γ_ is the porosity of the porous medium, and the external body



+(1 − _ε_ t) _ρ_ s



═

forces come from the stress tensor _τ_



═

forces come from the stress tensor _τ_, the Reynolds stress - _ρ_ g **u** [′] **u** [′], and

the source term of the gas-solid resistance calculated by DarcyForchheimer model under the condition of the porous medium _S_ m.



where _E_ g is the total energy of the gas, _E_ s is the total energy of solid, Δ _H_ i
is the heat of adsorption of species _i_, _h_ i is the sensible enthalpy and _**J**_ i is
the diffusion flux of species _i_ .
The material properties used in the simulation (mmen-Mg2(dobpdc))
is based on the references [40,41]. The adsorption isotherms of
mmen-Mg2(dobpdc) calculated in Ref. [41] have indicated that the
equilibrium adsorption capacity drops sharply between 100 and 500 Pa
(with type V isotherm). Adsorption model of the weighted-dual site
Langmuir (w-DSL) isotherm, proposed by Hefti [41], is used to calculate
the CO2 adsorption equilibrium of phase-changed absorbent
(mmen-Mg2(dobpdc) as shown in Eq. (11).

_q_ ( _p, T_ ) = _q_ L( _p, T_ )(1 − _w_ ( _p, T_ )) + _q_ H( _p, T_ ) _w_ ( _p, T_ ) (11)

where _q_ L is the Langmuir isotherm equilibrium capacity below the step



**Table 1**
The basic parameters for adsorption reactor.

Parameter Value Units



Height of reactor 1.5 m
Width of reactor 1.5 m
Length of reactor 2.2 m
Volume of packing 0.8 × 1.5 × 1.5 m [3 ]



Diameter of inlet 0.8 m
Inlet velocity 1.5 m⋅s [−] [1 ]



Volume flow rate 2714 m [3] ⋅h [−] [1 ]



Inlet diameter 0.8 m
Bed thickness 0.16 m
Angle of bed 18 deg



4


_S. Chen et al.                                                                                                                  Energy 282 (2023) 128801_



partial pressure, _p_ step (proposed by McDonald [40]), and _q_ H is the
adsorption capacity of a dual-site Langmuir-linear isotherm when
beyond the _p_ step as shown in Eqs. (12)–(14).


L _[b]_ [1] _[p]_
_q_ L = _[q]_ [∞] (12)
1 + _b_ 1 _p_


H _[b]_ [2] _[p]_
_q_ H = _[q]_ [∞] (13)
1 + _b_ 2 _p_ [+] _[ b]_ [3] _[p]_



_b_ i = _b_ [∞] i [exp] ( _E_ i ) _i_ = 1 _,_ 2 _,_ 3 (14)

_RT_

The sliding function, _w_ ( _p, T_ ), from 0 to 1, is used to define the pro­
portion between two adsorption models. It is calculated by a log-logistic
function, which is well fitted according to Eq. (15).



~~(~~
ln( _p_ )− ln( _pstep_ ( _T_ ))
1 + xp



)



⎞ _γ_


⎟
⎟
~~⎟~~
⎠



(
ln( _p_ )− ln( _pstep_ ( _T_ ))
exp



~~)~~



which are shown in Table 2.


_2.3._ _Pressure simulation_


Pressure curves are simulated to investigate pressure drop of the
conventional packed bed and the W-shaped packed bed. The pressurevelocity behavior calculated by ANSYS Fluent follows the DarcyForchheimer law, and the essential parameters of the DarcyForchheimer (viscous resistance [1] _α_ [(or the permeability ] _[α]_ [), and inertial ]

resistance _C_ 2) are estimated by Eurgun model (Eq. (6) and Eq. (7)). The
parameters are listed in Table 3. The viscous resistance and inertial
resistance are calculated 1.967 × 10 [9 ] and 68088, respectively. These
parameters are isotropic when solving the porous medium model. The
boundary conditions with different velocities (T = 300 K, P = 101325
Pa) are applied to the conventional packed bed model and the improved
W-shaped bed model, respectively, and the relative conditions are listed
in Table 3.


_2.4._ _Process simulation_


Based on the related parameters, CFD model is used to simulate the
working process. The reactor model undergoes three processes of
adsorption, desorption, and cooling for TSA. A breakthrough simulation
is established to estimate adsorption performance of the reactor under
the condition of different CO2 concentrations. The inlet boundary con­
dition of the reactor is set at 1.5 m s [−] [1], and the multiple sets of streams
with different concentrations of CO2 are tested, including 500 ppm
(unmanned indoor environment), 1000 ppm and 1500 ppm (common
indoor environment), and 2000 ppm (crowded indoor environment).
The concentration within the packed bed changes over time due to
adsorption reactions. And to determine the capture rate, the outlet
concentrations are measured. Adsorption behavior data, such as the
amount of CO2 captured and adsorption kinetic parameters of the bed
during the adsorption process are visualized to further study the
behavior of CO2 capture in the reactor. To simulate the desorption
process, the adsorption bed is heated to 373 K for the desorption of CO2.
It should be noted that desorption heat is mainly completed in the Fluent
UDF, the sensible heat and the desorption heat are recorded after
monitoring in Fluent that the bed no longer releases CO2. After the
desorption process is completed, the model proceeds to the cooling
process. The cooling method is to use normal temperature air to purge
the packed bed. To estimate the running time of the fan and its power
consumption, the time is recorded when the average temperature of the
bed is purged to the normal temperature at different flow rates.


_2.5._ _Indoor purification simulation_


A simplified model of indoor environment is established to evaluate
the CO2 purification effect of a capture device in this environment. The


**Table 3**
The main parameters for the CFD simulation.

Parameters Value Units



_w_ ( _p, T_ ) =



⎛


⎜
⎜
~~⎜~~
⎝



_σ_ ( _T_ )



(15)



_σ_ ( _T_ )



where the parameters controlled by temperature, _p_ step( _T_ ) and _σ_ ( _T_ ), can
be calculated by Eq. (16) and Eq. (17).



(
_pstep_ ( _T_ ) = _pstep,_ 0 exp - _[H]_ _R_ _[step]_



( 1

    - [1]

_T_ 0 _T_



))
(16)



(
_σ_ ( _T_ ) = _χ_ 1 exp _χ_ 2



( 1
_T_ 0



))

- [1] (17)
_T_



Besides, N2 adsorption is also considered. Mason’s study indicated
that in the mixed gas adsorption test, the CO2 selectivity of MOF-Mg is
little affected by nitrogen components [42]. The competition mecha­
nism of two components is ignored. The Langmuir adsorption equilib­
rium model is directly used to simulate nitrogen adsorption.
Adsorption kinetics are evaluated by Linear Driving Force (LDF)
model, shown as Eq. (18).

∂ _q_ t (18)

∂ _t_ [=] _[ k]_ [i][(] _[q]_ [ −] _[q]_ [t][)]



(
_k_ i = _k_ 0 exp - _[E]_ [i]

_R_



( 1
_T_ 0



))

- [1] (19)
_T_



where the _k_ i is adsorption time constant as shown in Eq. (19), _k_ 0 is a
temperature-independent constant. The relevant parameters and some
parameter estimates about adsorption are according to the references,


**Table 2**
The parameters for adsorption equilibrium model [41].

Parameter Value Units



_q_ [∞] L 0.146 mol⋅kg-1
_qb_ [∞] 1 [∞] H 3.478 0.009 molbar-1 ⋅kg-1
_b_ [∞] 2 9 × 10-7 bar-1
_b_ [∞] 3 5 × 10-4 mol⋅(kg-1bar-1)
_E_ 1 31 kJ⋅mol-1
_E_ 2 59 kJ⋅mol-1
_E_ 3 18 kJ⋅mol-1
_H_ step - 74.1 kJ⋅mol-1
_p_ step 0.5 mbar
_χ_ 1 0.124 _χ_ 2 0 K-1
_γ_ 4 _q_ [∞] N2 0.154 mol⋅kg-1
_b_ [∞] N2 2.582 × 10-7 bar-1
_E_ N2 18 kJ⋅mol-1
_k_ 0 0.00038 s [−] [1 ]

_E_ i 46.432 kJ⋅mol [−] [1 ]

_H_ CO2 67.2 kJ⋅mol [−] [1 ]



Temperature 300 K
Atmospheric pressure 101325 Pa
Velocity-1 0.5 m⋅s [−] [1 ]

Velocity-2 1 m⋅s [−] [1 ]

Velocity-3 1.5 m⋅s [−] [1 ]

Velocity-4 2 m⋅s [−] [1 ]

Velocity-5 2.5 m⋅s [−] [1 ]

Gas density 1.225 kg⋅m [−] [3 ]

Particle density 1400 kg⋅m [−] [3 ]



Particle diameter 1 × 10 [−] [3 ] m
Heat capacity 1500 J⋅K [−] [1] kg [−] [1 ]



Porosity 0.326 viscous resistance 1.967 × 10 [9 ] 1 m [−] [2 ]

inertial resistance 68088 1 m [−] [1 ]



5


_S. Chen et al.                                                                                                                  Energy 282 (2023) 128801_



CFD model is used to simulate the purification process of the indoor
environment in this part, which is shown in Fig. 3. Some assumptions are
listed as follows.

(1) The volume of the room is 1000 m [3], which corresponds to a large
classroom or office space.
(2) There are 40 people in the room.
(3) Each person produces CO2 at the rate of 0.0052 L s [−] [1 ] [29].
(4) CO2 exhaled from the human body, and the purified return air are
fully mixed with indoor air.
(5) The room is in a closed state.


The variation of CO2 concentration in the room can be expressed as
Eq. (20).

_V_ [d] _[C]_ (20)
d _t_ [=] _[ QC]_ [0][ −] _[QC]_ [(] _[t]_ [) +] _[ G]_ [(] _[t]_ [)]

where _V_ is the space volume, _C_ (t) is the indoor concentration at time, _Q_
is the flow rate, _C_ 0 is the low concentration (the outlet concentration of
the reactor), and _G_ ( _t_ ) is the CO2 generating rate. The outlet concentra­
tion of the reactor is used for calculation, and the simplified dynamic
indoor concentration model can be simulated.


_2.6._ _Performance indicators_


The reactor is simulated in terms of breakthrough and TSA process,
and the relevant performance indicators are listed as follows.
Pressure-velocity curves are simulated to estimate the influence of
W-shaped structure on pressure drop. The pressure-velocity behavior at
different air flow rates can be well indicated by the Darcy-Forchheimer
law, which is expressed by Eq. (21).


Δ _P_

[−] _[μ]_ (21)
_L_ [=] _α_ _[v]_ [ −] _[C]_ [2] _[ρ][v]_ [2]

where Δ _P_ is the pressure drop, _L_ is the length of the airflow through the
bed, _μ_ is the dynamic viscosity of the airflow, _ρ_ is the density of the
airflow.
The concentration is another performance to estimate adsorption
effect of the reactor. The capture rate is used, which can be calculated by
Eq. (22).



_E_ c = _[E][fan]_ [+] _[ E]_ ~~∫~~ _[desorption]_ _stop_ [+] _[ E][compressor]_ (23)
_start_ _[n][CO]_ [2] [d] _[t]_

where _nCO_ 2 is the CO2 captured in the timestep, _Efan_ is energy con­
sumption of fan, _Edesorption_ is energy consumption of desorption, _Ecompressor_
is energy consumption of the compressor.
The power of the fan can be calculated by Eq. (24).



_Pfan_ = _[Q]_ [Δ] _[P]_

_η_ eff



(24)



where _Q_ is air volumetric flow rate, Δ _P_ is pressure drop and _ηeff_ is fan
efficiency which value is 0.75.
The power of the compressor can be calculated by Eq. (25).



(25)




[



) _n_ - 1
_n_ []]



(
1 − _p_ 2



_p_ 1



_P_ compressor = _q_ m



_n_
_n_ - 1 ~~_[R]_~~ [g] _[T]_



_Capturerate_ = _[C][inlet]_ [−] _[C][outlet]_

_Cinlet_



× 100% (22)



where _qm_ is the mass flow rate, _n_ is the polytropic exponent.


**3.** **Results and discussion**


Pressure drop of the adsorption bed is first simulated and discussed
as an essential indicator of bed performance. It is closely related to fan
energy consumption. Subsequently, the whole process is simulated for
further investigation, and energy consumption of the process is dis­
cussed. Energy penalties of two adsorption beds are numerically
compared, which indicates the significance of the optimized bed.
Moreover, CFD model with the W-shaped packed bed is combined with
the proposed indoor CO2 condition model, and the dynamic indoor CO2
concentration is analyzed.


_3.1._ _Pressure-velocity behavior_

Five different inlet velocities, 0.5 m s [−] [1], 1 m s [−] [1], 1.5 m s [−] [1], 2 m s [−] [1],
and 2.5 m s [−] [1 ] are set for two types of the packed bed with the calculated
resistant coefficients. The solution of the reactor flow field are obtained
by transient calculations at these constant velocities. The simulated
pressure-velocity curves are shown in Fig. 4. The results demonstrate
that, by reducing one-third of the packed space, W-shaped packed bed
exhibits a significant lower pressure drop at various velocities compared
to the conventional packed bed. Pressure drop ratio between the W

**Fig. 4.** The pressure-velocity curves for two different packed adsorption
beds designs.



where _Cinlet_ is the inlet concentration and _Coutlet_ is the outlet concen­
tration.
Energy consumption of the system is calculated as energy con­
sumption per unit of CO2. The calculation method is followed by Eq.
(23).


**Fig. 3.** Schematic diagram of indoor air purification using DAC device.



6


_S. Chen et al.                                                                                                                  Energy 282 (2023) 128801_



shaped bed and the conventional bed is 12.04% at the inlet flow rate of
0.5 m s [−] [1 ] and 14.68% at the inlet flow rate of 2.5 m s [−] [1] . The reason for
this phenomenon can be explained by Fig. 2. After a part of the con­
ventional packed bed are removed to form a folding structure, two
important characteristics of the packed bed are optimized. First, the
distance of airflow through the bed is reduced, and the influence on the
system pressure drop is clearly explained by Eq. (21). Secondly, the
windward area of the folding plate structure is significantly increased, as
shown in Fig. 2. However, with the thinner beds and fewer fillings, the
capture amount will decrease and more frequent working cycles are then
required. Therefore, process simulation is subsequently conducted to
assess the cyclic working performance of the proposed W-shaped packed
bed.


_3.2._ _Process simulation and estimation_

Firstly, the basic model is simulated under the condition of 1.5 m s [−] [1 ]

and 1500 ppm CO2 concentration. The fields of velocity, pressure drop
and CO2 concentrations are illustrated in Fig. 5. The air flow enters the
cracks in the adsorption bed and penetrates the bed layer in a direction
perpendicular to adsorption bed. Despite the high inlet flow velocity of
1.5 m s [−] [1], the average air flow velocity inside the bed is only about 0.2
m s [−] [1 ] due to the expanded windward area, which is beneficial to the
adsorption reaction. Furthermore, CO2 concentration is reduced from
1500 ppm to 134 ppm. This capture effect has the effectiveness and
applicability for air purification in building environments. Further
relevant discussion is based on indoor air models and can be found in the
section 3.3.
The breakthrough curves with various CO2 concentrations are also
simulated. At the inlet velocity of 1.5 m s [−] [1], different concentrations of
500 ppm (unmanned indoor environment), 1000 ppm and 1500 ppm
(common indoor environment), as well as 2000 ppm (crowded indoor
environment) are selected to complete the adsorption process with the
W-shaped packed adsorption bed. Fig. 6(a) displays the outlet CO2
concentrations for different inlet concentrations, while Fig. 6(b) show­
sthe the calculated CO2 capture. For the W-shaped adsorption bed, the
breakthrough curves show a trend of "S", and CO2 capture rate has sig­
nificant plateau and decay periods. At the beginning of adsorption
processes, a period of high and stable capture rate (80%~90%) is
observed. It is crucial to fully utilize this period, which is more
conductive to CO2 capture throughout the DAC operation. Following



this plateau period, both capture rate and outlet concentrations exhibit
rapid changes. In the four concentration test, the "decay period" is
observed longer than the "plateau period". Taking the condtion of 1500
ppm as an example, we approximately take 80% of the CO2 capture rate
as the end point of the "plateau period", and the time when the capture
rate no longer changes is the end point of the "decay period". As a result,
the intercepted "plateau period" and "decay period" durations are 5.3 h
and 7.9 h, respectively. Long working duration during the decay period
is detrimental to capture efficiency, so adsorption strategies should be
developed based on actual carbon capture needs. The requirement for
indoor purification is the most important aspect of this work, and the
CO2 concentration should be kept below 800 ppm. So for the inlet
concentration of 1500 ppm, we can select the capture rate of 50% as the
termination point of the adsorption process.

Figs. 7 and 8 show the adsorbed amount of CO2 and the adsorption
rate under the condition of 1500 ppm, respectively. In the Fig. 7, the
occupancy of the adsorption bed can be observed. Over time, it can be
seen that the middle section of the adsorption bed is more fully utilized,
while there are dead zones of adsorption at the edge. The clear reaction
section in Fig. 8 shows that the active area of the high adsorption re­
action occurs in a specific range. As adsorption progresses, the reaction
section inside the adsorption bed gradually moves to the adsorption
bed’s edge. Previous studies have reported the migration behavior of
reaction sections in regular shaped reactors, and methods such as "re­
action front model" and "wave analysis" have been proposed for onedimensional modeling and relevant researches [43,44]. In this work,
the CFD model is used to visualize the propagation process, and the
material with type V isotherm also shows wave characteristics in the
reaction region of the W-shaped adsorption bed, as shown in Fig. 8. The
main part of the reaction section is still inside the adsorption bed within
5 h, which corresponds to the "plateau period" in the breakthrough
simulation. After about 5 h, the reaction section waves migrate to the
adsorption bed’s edge. Adsorption capacity of the bed layer begins to
degrade significantly at this point, corresponding to "decay period" in
the breakthrough simulation.
Besides, a breakthrough test of the conventional packed bed with an
inlet concentration of 1500 ppm is also simulated and compared with
the W-shaped packed bed, which is shown in Fig. 9. The conventional
packed bed performs a higher capture rate and longer working time
compared with the W-shaped packed bed. Correspondingly, when the
capture rates of two adsorption beds decay to 50%, the total adsorption



**Fig. 5.** The fields of velocity, pressure drop and CO2 concentration in the reactor.


7


_S. Chen et al.                                                                                                                  Energy 282 (2023) 128801_



**Fig. 6.** (a) The simulated breakthrough curves of the W-shaped bed under the
condition of four different inlet CO2 concentrations. (b) The simulated capture
rate curves of the W-shaped bed under the condition of four different inlet CO2
concentrations.


saturations of beds are 0.856 for the W-shaped bed and 0.915 for the
conventional bed. This result demonstates that the W-shaped adsorption
bed has small weakness in terms of material utilization uniformity. As
we can see in the Fig. 7, there are reaction dead zones at the angle po­
sition of the W-shaped bed, which indicate that the airflow passes
through the middle section of the flat plate adsorbent more evenly, but
there is less airflow passing through the connection section of the flat
plate. To address this issue, previous methods such as flow distributer
may become solutions to this problem [45,46], thus compensating for
the uniformity disadvantages of W-shaped adsorption beds in this re­
gard. Besides, a smooth transition structure may be useful at the exit
section, where mass transfer trend exhibits a smooth arc in Figs. 7 and 8.
After the carbon capture rates have been reduced to 50%, the
desorption process is initiated, and the desorption results are shown in



Table 4. The packed amount of the W-shaped packed adsorption bed is
two-thirds that of the conventional adsorption bed due to different
filling spaces. The adsorbents’ average capture amount of CO2 recovered
by heating the conventional adsorption bed and W-shaped adsorption
bed is 2.49 mol kg [−] [1 ] and 2.29 mol kg [−] [1], respectively due to the problem
of uniformity. The heat used to supply the sensible heat of adsorbent and
reaction heat of CO2 desorption are both important parts of the heating
process, and their heat demands are relatively similar. For the less
capture amount of the W-shaped bed, the sensible heat per mole of CO2
is higher, which leads to the higher energy penalty.
After the desorption process, the device is cooled down to 300 K by
airflow and three different velocities, 1 m s [−] [1], 1.5 m s [−] [1], 2 m s [−] [1 ] of
airflow are used. Fig. 10 depicts temperature variations at different inlet
velocities, and the results indicate that the cooldown time decreases by
50% when the inlet velocity increases from 1 m s [−] [1 ] to 2 m s [−] [1] . However,
it is important to note that a low inlet velocity (1 m s [−] [1] ) is selected in the
cooling process when considering the power of the fan, which can be
influenced by flow rate and pressure drop. The energy consumption of
W-shaped adsorption bed for blowing and cooling for 1 h under this
condition is calculated to be 2.1 kJ mol [−] [1] . Fig. 11 shows fan energy
consumption at the four groups of CO2 concentration, and the capture
amount of 50% is set as a signal to finish adsorption process. At lower
concentrations, more air needs to be processed to capture the same
amount of CO2. It could save 81.4% of fan energy consumption when
increasing the concentration from 500 ppm to 2000 ppm because of the
reduction of working time. The result can also be extended to the
scheduling strategy of the indoor air capture process. If the indoor air
conditions are met, it would be more energy-efficient to operate the
device in the environment with high concentration of CO2. For example,
the indoor CO2 concentration can be maintained between 600 ppm and
1000 pmm. This not only ensures compliance with air quality standards,
but also maximizes working efficiency of carbon capture devices.

Fig. 12 shows the average energy consumption distribution of the
conventional packed bed and the W-shaped packed bed in the TSA
process. The main energy requirements in TSA process come from the
fan operation, desorption heat, the sensible heat of the bed, and
compressor (the target pressure of the compressor is 2 Mpa). This factors
account for 38%, 29%, 27% and 6%, respectively, in the case of the
conventional packed bed. The largest contributior to the total energy
consumption is the energy required for fan. For the W-shaped bed, en­
ergy consumption of fan could be greatly reduced from 88.7 kJ mol [−] [1 ] to
15.1 kJ mol [−] [1], and the proportion of energy consumption in all aspects
becomes 8.9%, 40.7%, 41.6%, and 8.8%. The desorption heat and the
sensible heat of the bed during the process become the biggest parts.
Although in the energy evaluation of the desorption process, the Wshaped adsorption bed is unfavorable in terms of desorption energy
penalty due to its uniformity problem, the energy saved during
adsorption process compensates for this disadvantage. In fact, there is
the potential to further save energy. For example, the system can be
optimized through temperature and vacuum swing adsorption (TVSA),
which can further improve the working efficiency, and recover CO2 with
high purity at the same time [47–49]. In addition, heating with
renewable energy systems and the waste heat recovery of the adsorption
bed has proven to be feasible schemes in some studies [50–53].


_3.3._ _Indoor environment simulation_


Based on the simplified model for indoor CO2 concentration, the CO2
concentration change within 1 h after the beginning of the capture de­
vice is evaluated. This aims to verify that the DAC system can effectively
regulate CO2 concentration. However, if the actual ventilation system is
considered, the indoor fresh air demand should be taken into consid­
eration when operating DAC systems. Kim et al. [30,31] established
similar models in their study. Fig. 13 shows the simulation results of
three initial conditions of CO2. In addition, carbon capture rates of the
simulated capture device are also revealed. The result under three initial



8


_S. Chen et al.                                                                                                                  Energy 282 (2023) 128801_


**Fig. 7.** The adsorbed amount of CO2 in the bed at different time.


**Fig. 8.** Adsorption rates in the bed at different time.



conditions (1000 ppm, 1500 ppm, 2000 ppm) illustrates a good purifi­
cation effect on CO2 concentrations, and the indoor concentrations are
reduced to around 600 ppm within an hour. According to Fig. 13, the
change of indoor CO2 concentration becomes gradually slower. Taking
the initial concentration of 2000 ppm as an example, the concentration
is decreased by about 1200 ppm in the first half hour, while in the
second half hour, the concentration is only decreased by about 200 ppm.
The slowing down of purification speed and the attenuation of capture
rate indicate that the DAC system operates at a lower efficiency in the
second half hour. From the perspective of capture rates, operating the
DAC system to work in low concentration environments for a long time
is a low efficiency and high energy penalty choice, that is inappropriate
operation.



It is important that the actual process needs to meet the requirements
of CO2 capture efficiency and indoor environmental sanitation. For CO2
capture, a higher capture efficiency is pursued to reduce the energy
consumption per unit of CO2 capture. For indoor air purification, the
concentration of CO2 should be maintained at a low level. Therefore, to
achieve good dual benefits of capture and purification, the appropriate
scheduling schemes must be considered. In this part of work, the
adsorption process will stop when the indoor concentration is reduce to
the comfort level 600 ppm, and the adsorption process will restart when
the indoor concentration raises to 1000 ppm [54]. A 24-h simulation is
conducted, and the CO2 concentration change is shown in Fig. 14. The
initial concentration is set to 1500 ppm. In the first nine working cycles,
the capture device shows a relatively stable effect for 12 h in total. After



9


_S. Chen et al.                                                                                                                  Energy 282 (2023) 128801_


**Fig. 9.** Comparison of CO2 capture rate and saturation change of two adsorp­
tion beds.



**Table 4**
Numerical simulation results of the desorption process.

Conventional packed bed W-shaped packed bed

Actual filling volume (m [3] ) 1.8 1.21 (2/3)
Mass of adsorbent (kg) 1043.35 701.36
Capture amount (mol⋅kg [−] [1] ) 2.49 2.29
Desorption temperature (K) 373 373
Sensible heat (kJ⋅mol [−] [1] ) 64.3 69.9
Desorption heat (kJ⋅mol [−] [1] ) 68.4 68.3
Total energy (kJ⋅mol [−] [1] ) 132.7 138.2


**Fig. 10.** Average temperature of cooling process of the W-shaped bed.


nine cycles, the capture effect of the device has decreased significantly,
and CO2 concentration has been unable to be reduced to 600 ppm, and
the device needs to enter desorption mode. The simulated result dem­
onstrates that in continuous work simulation, the DAC system exhibits
stability and efficiency in CO2 regulation over a sufficiently long time
range, showing an excellent regulatory effect on indoor CO2.



**Fig. 11.** Fan energy consumption when the reactor works to predetermined
terminal time under the condition of different inlet CO2 concentrations.


**4.** **Conclusions**


In this work, a W-shaped packed adsorption bed is numerically
investigated under the CO2 concentrations of indoor environment. By
sacrificing the packed volume and changing the structure, the adsorp­
tion bed performs differently. A 3D CFD model is established to research
the structured adsorption bed. The conclusions are yielded as follows:
Firstly, the reactor pressure drop is numerically calculated and
compared. By sacrificing approximately 1/3 volume of conventional
packed, the pressure drop is greatly reduced. In detail, with the increase
of windward area and the decrease of breakthrough distance, the pres­
sure drop ratio between the W-shaped bed and the conventional bed is
from 14.68% to 12.04% within the test flow rate range (0.5 m s [−] [1 ] to 2.5
m s [−] [1] ).
Secondly, the adsorption performance is studied using mmenMg2(dobpdc), the breakthrough concentration curves show a trend of
“S”. We use the CFD model to further understand the mass transfer
process inside the bed and investigate the migration process of reaction
section. The results reveal that to maintain a high adsorption effective of
the adsorption bed, the position of the reaction section must be inside
the adsorption bed, which will provide a basis for further optimization of
the structure.
Thirdly, the system energy consumption is calculated based on a TSA
process. The W-shaped bed has significant advantages in saving fan
energy consumption compared to the conventional packed bed, with the
total energy of 236.2 kJ mol [−] [1 ] and 167.9 kJ mol [−] [1 ] for the latter.
Although in the energy evaluation of the desorption process, the Wshaped adsorption bed is unfavorable in terms of desorption energy
penalty due to its uniformity weakness, the energy saved during the
blowing process compensates for this disadvantage and overall saves
energy.
Moreover, the combination of the simplified indoor concentration
model and the CFD model shows that the reactor has a good effect on
CO2 purification. In the simulation of a 24-h long working period, the
results show that purification efficiency is stable and the capture process
can be carried out continuously and efficiently up to 12 h.
With the further application of DAC technology in indoor environ­
ments, structured adsorption beds will play an important role in opti­
mizing pressure drop, as the issue of capture energy consumption cannot
be ignored. The process simulation verification of packed bed will be
considered in our future work. This study shows that the conventional
fixed bed packing method is not applicable in the air capture scenario for



10


_S. Chen et al.                                                                                                                  Energy 282 (2023) 128801_


**Fig. 14.** Simulation results of indoor CO2 concentration change in 24 h.


the excessive pressure drop and energy penalty, and the structured
packed adsorption bed investigated has the potential in indoor air pu­
rification while saving fan energy consumption, which offers a valuable
basis for reactor design.


**Declaration of competing interest**


The authors declare that they have no known competing financial
interests or personal relationships that could have appeared to influence
the work reported in this paper.


**Data availability**


Data will be made available on request.


**Acknowledgment**


This research was supported by the National Key Research and
Development Program of China (No. 2022YFB4101700), ‘New lowenergy CO2 capture materials and mechanisms’, National Natural Sci­
ence Foundation of China (No. 52276022) and supported by the Basic
Research Funds for the Central University ‘Innovative Team of Zhejiang
University’ under contract number (2022FZZX01-09).


**References**



**Fig. 12.** Energy consumption of (a) the conventional packed bed and (b) the Wshaped packed bed in TSA process.


**Fig. 13.** Simulation results of indoor CO2 concentration change and capture
rate of DAC reactor.




[1] [The global climate in 2015-2019. 2020. https://public.wmo.int/en/resources/libra](https://public.wmo.int/en/resources/library/global-climate-2015-2019)
[ry/global-climate-2015-2019. [Accessed 23 February 2023].](https://public.wmo.int/en/resources/library/global-climate-2015-2019)

[2] [Masson-Delmotte V, Zhai P, Portner H-O, Roberts D, Skea J, Shukla PR. Global ¨](http://refhub.elsevier.com/S0360-5442(23)02195-3/sref2)
warming of 1.5 [◦] [C: IPCC special report on impacts of global warming of 1.5](http://refhub.elsevier.com/S0360-5442(23)02195-3/sref2) [◦] C
[above pre-industrial levels in context of strengthening response to climate change,](http://refhub.elsevier.com/S0360-5442(23)02195-3/sref2)
[sustainable development, and efforts to eradicate poverty. Cambridge University](http://refhub.elsevier.com/S0360-5442(23)02195-3/sref2)
[Press; 2022.](http://refhub.elsevier.com/S0360-5442(23)02195-3/sref2)

[3] Jiang L, Gonzalez-Diaz A, Ling-Chin J, et al. PEF plastic synthesized from industrial
[carbon dioxide and biowaste. Nat Sustain 2020;3:761–7. https://doi.org/10.103](https://doi.org/10.1038/s41893-020-0549-y)
[8/s41893-020-0549-y.](https://doi.org/10.1038/s41893-020-0549-y)

[4] Zhao F, Wang Z, Wang D, Han F, Ji Y, Cai W. Top level design and evaluation of
advanced low/zero carbon fuel ships power technology. Energy Rep 2022;8:
[336–44. https://doi.org/10.1016/j.egyr.2022.10.143.](https://doi.org/10.1016/j.egyr.2022.10.143)

[5] Jiang L, Liu W, Wang RQ, Gonzalez-Diaz A, Rojas-Michaga MF, Michailos S,
Pourkashanian M, Zhang XJ, Font-Palma C. Sorption direct air capture with CO2
[utilization. Prog Energy Combust Sci 2023;95:101069. https://doi.org/10.1016/j.](https://doi.org/10.1016/j.pecs.2022.101069)
[pecs.2022.101069.](https://doi.org/10.1016/j.pecs.2022.101069)

[6] Zhang Z, Pan S-Y, Li H, Cai J, Olabi AG, Anthony EJ, Manovic V. Recent advances
in carbon dioxide utilization. Renew Sustain Energy Rev 2020;125:109799.
[https://doi.org/10.1016/j.rser.2020.109799.](https://doi.org/10.1016/j.rser.2020.109799)

[7] Leung DYC, Caramanna G, Maroto-Valer MM. An overview of current status of
carbon dioxide capture and storage technologies. Renew Sustain Energy Rev 2014;
[39:426–43. https://doi.org/10.1016/j.rser.2014.07.093.](https://doi.org/10.1016/j.rser.2014.07.093)

[8] Lackner K. The thermodynamics of direct air capture of carbon dioxide. Energy
[2013;50:38–46. https://doi.org/10.1016/j.energy.2012.09.012.](https://doi.org/10.1016/j.energy.2012.09.012)

[9] Casaban D, Tsalaporta E. Direct air capture of CO2 in the Republic of Ireland. Is it
[necessary? Energy Rep 2022;8:10449–63. https://doi.org/10.1016/j.](https://doi.org/10.1016/j.egyr.2022.08.194)
[egyr.2022.08.194.](https://doi.org/10.1016/j.egyr.2022.08.194)

[10] Kriegler E, Bauer N, Popp A, Humpenoder F, Leimbach M, Strefler J, Baumstark L, ¨
Bodirsky BL, Hilaire J, Klein D, Mouratiadou I, Weindl I, Bertram C, Dietrich J-P,
Luderer G, Pehl M, Pietzcker R, Piontek F, Lotze-Campen H, Biewald A, Bonsch M,
Giannousakis A, Kreidenweis U, Müller C, Rolinski S, Schultes A, Schwanitz J,



11


_S. Chen et al.                                                                                                                  Energy 282 (2023) 128801_



Stevanovic M, Calvin K, Emmerling J, Fujimori S, Edenhofer O. Fossil-fueled
development (SSP5): an energy and resource intensive scenario for the 21st
[century. Global Environ Change 2017;42:297–315. https://doi.org/10.1016/j.](https://doi.org/10.1016/j.gloenvcha.2016.05.015)
[gloenvcha.2016.05.015.](https://doi.org/10.1016/j.gloenvcha.2016.05.015)

[11] Castro-Munoz R, Zamidi Ahmad M, Malankowska M, Coronas J. A new relevant ˜
membrane application: CO2 direct air capture (DAC). Chem Eng J 2022;446:
[137047. https://doi.org/10.1016/j.cej.2022.137047.](https://doi.org/10.1016/j.cej.2022.137047)

[12] Sodiq A, Abdullatif Y, Aissa B, Ostovar A, Nassar N, El-Naas M, Amhamed A.
A review on progress made in direct air capture of CO2. Environ Technol Innov
[2023;29:102991. https://doi.org/10.1016/j.eti.2022.102991.](https://doi.org/10.1016/j.eti.2022.102991)

[13] Qadir A, Abdul Manaf N, Abbas A. Analysis of the integration of a steel plant in
Australia with a carbon capture system powered by renewable energy and NG[CHP. J Clean Prod 2017;168:97–104. https://doi.org/10.1016/j.](https://doi.org/10.1016/j.jclepro.2017.09.001)
[jclepro.2017.09.001.](https://doi.org/10.1016/j.jclepro.2017.09.001)

[14] Erans M, Sanz-P´erez ES, Hanak DP, Clulow Z, Reiner DM, Mutch GA. Direct air
capture: process technology, techno-economic and socio-political challenges.
[Energy Environ Sci 2022;15:1360–405. https://doi.org/10.1039/D1EE03523A.](https://doi.org/10.1039/D1EE03523A)

[15] Hepburn C, Adlen E, Beddington J, Carter EA, Fuss S, Mac Dowell N, Minx JC,
Smith P, Williams CK. The technological and economic prospects for CO2
[utilization and removal. Nature 2019;575:87–97. https://doi.org/10.1038/](https://doi.org/10.1038/s41586-019-1681-6)
[s41586-019-1681-6.](https://doi.org/10.1038/s41586-019-1681-6)

[16] Barkakaty B, Sumpter BG, Ivanov IN, Potter ME, Jones CW, Lokitz BS. Emerging
materials for lowering atmospheric carbon. Environ Technol Innov 2017;7:30–43.
[https://doi.org/10.1016/j.eti.2016.12.001.](https://doi.org/10.1016/j.eti.2016.12.001)

[17] Li J-R, Ma Y, McCarthy MC, Sculley J, Yu J, Jeong H-K, Balbuena PB, Zhou H-C.
Carbon dioxide capture-related gas adsorption and separation in metal-organic
[frameworks. Coord Chem Rev 2011;255:1791–823. https://doi.org/10.1016/j.](https://doi.org/10.1016/j.ccr.2011.02.012)
[ccr.2011.02.012.](https://doi.org/10.1016/j.ccr.2011.02.012)

[18] Lee TS, Cho JH, Chi SH. Carbon dioxide removal using carbon monolith as electric
swing adsorption to improve indoor air quality. Build Environ 2015;92:209–21.
[https://doi.org/10.1016/j.buildenv.2015.04.028.](https://doi.org/10.1016/j.buildenv.2015.04.028)

[19] Shi WK, Zhang XJ, Liu X, Wei S, Shi X, Wu C, Jiang L. Temperature-vacuum swing
adsorption for direct air capture by using low-grade heat. Journal of Cleaner
[Production 2023;Volume 414:137731. https://doi.org/10.1016/j.](https://doi.org/10.1016/j.rser.2020.110651)
[rser.2020.110651. ISSN 0959-6526.](https://doi.org/10.1016/j.rser.2020.110651)

[20] Jiang L, Roskilly AP, Wang RZ. Performance exploration of temperature swing
adsorption technology for carbon dioxide capture. Energy Convers Manag 2018;
[165:396–404. https://doi.org/10.1016/j.enconman.2018.03.077.](https://doi.org/10.1016/j.enconman.2018.03.077)

[21] Zhao R, Liu L, Zhao L, Deng S, Li S, Zhang Y, Li H. Thermodynamic exploration of
temperature vacuum swing adsorption for direct air capture of carbon dioxide in
[buildings. Energy Convers Manag 2019;183:418–26. https://doi.org/10.1016/j.](https://doi.org/10.1016/j.enconman.2019.01.009)
[enconman.2019.01.009.](https://doi.org/10.1016/j.enconman.2019.01.009)

[22] Chao C, Deng Y, Dewil R, Baeyens J, Fan X. Post-combustion carbon capture.
[Renew Sustain Energy Rev 2021;138:110490. https://doi.org/10.1016/j.](https://doi.org/10.1016/j.rser.2020.110490)
[rser.2020.110490.](https://doi.org/10.1016/j.rser.2020.110490)

[23] Ben-Mansour R, Qasem NAA. An efficient temperature swing adsorption (TSA)
process for separating CO2 from CO2/N2 mixture using Mg-MOF-74. Energy
[Convers Manag 2018;156:10–24. https://doi.org/10.1016/j.](https://doi.org/10.1016/j.enconman.2017.11.010)
[enconman.2017.11.010.](https://doi.org/10.1016/j.enconman.2017.11.010)

[24] Wen Z-N, Xu H-Z, Li Y-B, Zhang L-L, Zou H-K, Chu G-W, Chen J-F. Carbon dioxide
capture in a HiGee reactor with packing featuring controllable cross-sectional area.
[Sep Purif Technol 2023;305:122510. https://doi.org/10.1016/j.](https://doi.org/10.1016/j.seppur.2022.122510)
[seppur.2022.122510.](https://doi.org/10.1016/j.seppur.2022.122510)

[25] Sandu V-C, Cormos A-M, Dumbrava I-D, Imre-Lucaci A, Cormos C-C, de Boer R,
Boon J, Sluijter S. Assessment of CO2 capture efficiency in packed bed versus 3Dprinted monolith reactors for SEWGS using CFD modeling. Int J Greenh Gas
[Control 2021;111:103447. https://doi.org/10.1016/j.ijggc.2021.103447.](https://doi.org/10.1016/j.ijggc.2021.103447)

[26] Wang J, Li S, Deng S, Zeng X, Li K, Liu J, Yan J, Lei L. Energetic and life cycle
assessment of direct air capture: a review. Sustain Prod Consum 2023;36:1–16.
[https://doi.org/10.1016/j.spc.2022.12.017.](https://doi.org/10.1016/j.spc.2022.12.017)

[27] Gambhir A, Tavoni M. Direct air carbon capture and sequestration: How it works
and How it could contribute to climate-change mitigation. One Earth 2019;1:
[405–9. https://doi.org/10.1016/j.oneear.2019.11.006.](https://doi.org/10.1016/j.oneear.2019.11.006)

[28] [Janssen J. Ventilation for acceptable indoor air quality. 1989.](http://refhub.elsevier.com/S0360-5442(23)02195-3/sref28)

[29] Avgelis A, Papadopoulos AM. Indoor air quality guidelines and standards - a state
[of the art review. Int J Vent 2004;3:267–78. https://doi.org/10.1080/](https://doi.org/10.1080/14733315.2004.11683921)
[14733315.2004.11683921.](https://doi.org/10.1080/14733315.2004.11683921)

[30] Kim MK, Baldini L, Leibundgut H, Wurzbacher JA, Piatkowski N. A novel
ventilation strategy with CO2 capture device and energy saving in buildings.
[Energy Build 2015;87:134–41. https://doi.org/10.1016/j.enbuild.2014.11.017.](https://doi.org/10.1016/j.enbuild.2014.11.017)

[31] Kim MK, Baldini L, Leibundgut H, Wurzbacher JA. Evaluation of the humidity
performance of a carbon dioxide (CO2) capture device as a novel ventilation
[strategy in buildings. Appl Energy 2020;259:112869. https://doi.org/10.1016/j.](https://doi.org/10.1016/j.apenergy.2019.03.074)
[apenergy.2019.03.074.](https://doi.org/10.1016/j.apenergy.2019.03.074)

[32] Baus L, Nehr S. Potentials and limitations of direct air capturing in the built
[environment. Build Environ 2022;208:108629. https://doi.org/10.1016/j.](https://doi.org/10.1016/j.buildenv.2021.108629)
[buildenv.2021.108629.](https://doi.org/10.1016/j.buildenv.2021.108629)




[33] Ji Y, Yong JY, Liu W, Zhang XJ, Jiang L. Thermodynamic analysis on direct air
capture for building air condition system: balance between adsorbent and
[refrigerant. Energy Built Environ; 2022. https://doi.org/10.1016/j.](https://doi.org/10.1016/j.enbenv.2022.02.009)
[enbenv.2022.02.009.](https://doi.org/10.1016/j.enbenv.2022.02.009)

[34] Vervloet D, Kapteijn F, Nijenhuis J, van Ommen JR. Process intensification of
tubular reactors: considerations on catalyst hold-up of structured packings. Catal
[Today 2013;216:111–6. https://doi.org/10.1016/j.cattod.2013.05.019.](https://doi.org/10.1016/j.cattod.2013.05.019)

[35] Young J, Mcilwaine F, Smit B, Garcia S, van der Spek M. Process-informed
adsorbent design guidelines for direct air capture. Chem Eng J 2023;456:141035.
[https://doi.org/10.1016/j.cej.2022.141035.](https://doi.org/10.1016/j.cej.2022.141035)

[36] Liu W, Ji Y, Wang RQ, Zhang XJ, Jiang L. Analysis on temperature vacuum swing
adsorption integrated with heat pump for efficient carbon capture. Appl Energy
[2023;335:120757. https://doi.org/10.1016/j.apenergy.2023.120757.](https://doi.org/10.1016/j.apenergy.2023.120757)

[37] Zhao R, Zhao L, Wang S, Deng S, Li H, Yu Z. Solar-assisted pressure-temperature
swing adsorption for CO2 capture: effect of adsorbent materials. Sol Energy Mater
[Sol Cells 2018;185:494–504. https://doi.org/10.1016/j.solmat.2018.06.004.](https://doi.org/10.1016/j.solmat.2018.06.004)

[38] van Antwerpen W, du Toit CG, Rousseau PG. A review of correlations to model the
packing structure and effective thermal conductivity in packed beds of mono-sized
[spherical particles. Nucl Eng Des 2010;240:1803–18. https://doi.org/10.1016/j.](https://doi.org/10.1016/j.nucengdes.2010.03.009)
[nucengdes.2010.03.009.](https://doi.org/10.1016/j.nucengdes.2010.03.009)

[39] [ANSYS Fluent Theory Guide https://www.ansys.com, (n.d.).](https://www.ansys.com)

[40] McDonald TM, Mason JA, Kong X, Bloch ED, Gygi D, Dani A, Crocella V, `
Giordanino F, Odoh SO, Drisdell WS, Vlaisavljevich B, Dzubak AL, Poloni R,
Schnell SK, Planas N, Lee K, Pascal T, Wan LF, Prendergast D, Neaton JB, Smit B,
Kortright JB, Gagliardi L, Bordiga S, Reimer JA, Long JR. Cooperative insertion of
CO2 in diamine-appended metal-organic frameworks. Nature 2015;519:303–8.
[https://doi.org/10.1038/nature14327.](https://doi.org/10.1038/nature14327)

[41] Hefti M, Joss L, Bjelobrk Z, Mazzotti M. On the potential of phase-change
adsorbents for CO 2 capture by temperature swing adsorption. Faraday Discuss
[2016;192:153–79. https://doi.org/10.1039/C6FD00040A.](https://doi.org/10.1039/C6FD00040A)

[42] Mason JA, McDonald TM, Bae T-H, Bachman JE, Sumida K, Dutton JJ, Kaye SS,
Long JR. Application of a high-throughput analyzer in evaluating solid adsorbents
for post-combustion carbon capture via multicomponent adsorption of CO 2, N 2,
and H 2 [O. J Am Chem Soc 2015;137:4787–803. https://doi.org/10.1021/](https://doi.org/10.1021/jacs.5b00838)
[jacs.5b00838.](https://doi.org/10.1021/jacs.5b00838)

[43] Lin YC, Fan YB, Chen S, Zhang XJ, Frazzica A, Jiang L. Wave analysis method for
air humidity assisted sorption thermal battery: a new perspective. Energy Convers
[Manag 2023;277:116638. https://doi.org/10.1016/j.enconman.2022.116638.](https://doi.org/10.1016/j.enconman.2022.116638)

[44] Michel B, Mazet N, Neveu P. Experimental investigation of an open
thermochemical process operating with a hydrate salt for thermal storage of solar
[energy: local reactive bed evolution. Appl Energy 2016;180:234–44. https://doi.](https://doi.org/10.1016/j.apenergy.2016.07.108)
[org/10.1016/j.apenergy.2016.07.108.](https://doi.org/10.1016/j.apenergy.2016.07.108)

[45] Dai Z, Yu M, Rui D, Zhang X, Zhao Y. Investigation on a vertical radial flow
adsorber designed by a novel parallel connection method, Chin. J Chem Eng 2018;
[26:484–93. https://doi.org/10.1016/j.cjche.2017.11.005.](https://doi.org/10.1016/j.cjche.2017.11.005)

[46] Chen Y. Numerical investigation into the distributor design in radial flow adsorber.
[Adv Appl Math Mech 2019;11:1436–60. https://doi.org/10.4208/aamm.OA-2019-](https://doi.org/10.4208/aamm.OA-2019-0001)
[0001.](https://doi.org/10.4208/aamm.OA-2019-0001)

[47] Xu Q, Wang lwei, Li Z, Shi L. A calcium looping system powered by renewable
electricity for long-term thermochemical energy storage, residential heat supply
[and carbon capture. Energy Convers Manag 2023;276:116592. https://doi.org/](https://doi.org/10.1016/j.enconman.2022.116592)
[10.1016/j.enconman.2022.116592.](https://doi.org/10.1016/j.enconman.2022.116592)

[48] Nair PNSB, Tan RR, Foo DCY. A generic algebraic targeting approach for
integration of renewable energy sources, CO2 capture and storage and negative
emission technologies in carbon-constrained energy planning. Energy 2021;235:
[121280. https://doi.org/10.1016/j.energy.2021.121280.](https://doi.org/10.1016/j.energy.2021.121280)

[49] Reddy DL, Lokhat D, Siddiqi H, Meikap BC. Modelling and simulating CO and CO2
methanation over Ru/γ-Al2O3 catalyst: an integrated approach from carbon
[capture to renewable energy generation. Fuel 2022;314:123095. https://doi.org/](https://doi.org/10.1016/j.fuel.2021.123095)
[10.1016/j.fuel.2021.123095.](https://doi.org/10.1016/j.fuel.2021.123095)

[50] Magnolia G, Gambini M, Mazzoni S, Vellini M. Renewable energy, carbon capture
& sequestration and hydrogen solutions as enabling technologies for reduced CO2
energy transition at a national level: an application to the 2030 Italian national
[energy scenarios. Clean Energy Syst. 2023;4:100049. https://doi.org/10.1016/j.](https://doi.org/10.1016/j.cles.2022.100049)
[cles.2022.100049.](https://doi.org/10.1016/j.cles.2022.100049)

[51] Shewchuk SR, Mukherjee A, Dalai AK. Selective carbon-based adsorbents for
carbon dioxide capture from mixed gas streams and catalytic hydrogenation of
CO2 into renewable energy source: a review. Chem Eng Sci 2021;243:116735.
[https://doi.org/10.1016/j.ces.2021.116735.](https://doi.org/10.1016/j.ces.2021.116735)

[52] Ravikumar D, Keoleian G, Miller S. The environmental opportunity cost of using
renewable energy for carbon capture and utilization for methanol production. Appl
[Energy 2020;279:115770. https://doi.org/10.1016/j.apenergy.2020.115770.](https://doi.org/10.1016/j.apenergy.2020.115770)

[53] Arnette AN. Renewable energy and carbon capture and sequestration for a reduced
carbon energy plan: an optimization model. Renew Sustain Energy Rev 2017;70:
[254–65. https://doi.org/10.1016/j.rser.2016.11.218.](https://doi.org/10.1016/j.rser.2016.11.218)

[54] Tian H, Zhu L, Ni J, Wei T, Wang P, Xiao H, Chen X. Indoor CO2 removal:
decentralized carbon capture by air conditioning. Mater Today Sustain 2023;22:
[100369. https://doi.org/10.1016/j.mtsust.2023.100369.](https://doi.org/10.1016/j.mtsust.2023.100369)



12



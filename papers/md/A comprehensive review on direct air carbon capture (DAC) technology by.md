[Energy Conversion and Management 322 (2024) 119119](https://doi.org/10.1016/j.enconman.2024.119119)


Contents lists available at ScienceDirect
# Energy Conversion and Management


journal homepage: [www.elsevier.com/locate/enconman](https://www.elsevier.com/locate/enconman)


Review Article
## A comprehensive review on direct air carbon capture (DAC) technology by adsorption: From fundamentals to applications

Huijin Xu [a][,][*], Liyang Yu [b], Chengtung Chong [c], Fuqiang Wang [d]

a _School_ _of_ _Merchant_ _Marine,_ _Shanghai_ _Maritime_ _University,_ _Shanghai_ _201306,_ _China_
b _College_ _of_ _New_ _Energy,_ _China_ _University_ _of_ _Petroleum,_ _Qingdao_ _266580,_ _China_
c _China-UK_ _Low_ _Carbon_ _College,_ _Shanghai_ _Jiao_ _Tong_ _University,_ _Shanghai_ _200240,_ _China_
d _Harbin_ _Institute_ _of_ _Technology_ _at_ _Weihai,_ _Weihai_ _264209,_ _China_



A R T I C L E I N F O


_Keywords:_
Direct air carbon capture
Adsorbent
CO2 capture
Adsorption kinetics
Adsorption system


**1.** **Introduction**



A B S T R A C T


There is an increasing incentive to explore effective ways to capture CO2 from the air to address the rising levels
and the ensuing energy climate challenges. Direct air carbon capture (DAC) technology is an avenue in this
endeavor, which has garnered significant interest due to its potential to achieve carbon-negative emissions and
align with the imperatives of sustainable development and climate control. This article examines the latest advancements in DAC technology and its underlying principles, with a specific emphasis on the crucial function of
adsorbents. In this paper, we extend the theories of conservation of energy and mass and ideal adsorption solution to the adsorption process of DAC and provide a computational framework for the analysis of this process
Furthermore, it endeavors to elucidate the intricate interplay of systems and devices integral to DAC technology,
offering insights into the various facets of its implementation. In closing, the article conducts an assessment and
offers a brief overview of the present condition of DAC technology, highlighting its possibilities and constraints in
the wider scope of carbon capture and climate mitigation endeavors. By encompassing all these aspects, this
comprehensive exploration aims to offer a holistic understanding of DAC technology and its significance in the
ongoing quest for mitigating CO2 emissions. The review also lists the current application of DAC technology in
practice, and compare its economic benefits.



The population surge and excessive human activities have led to a
sudden rise in CO2 content in the air. By 2020, the volume fraction of
CO2 in the air has exceeded 410 mL⋅m [−] [3] [1]. Since 1750, the amount of
CO2 in the air has increased along with human emissions. CO2 emissions
data from Our World in Data and the Global Carbon Project is shown in
Fig. 1. The report released by the International Energy Agency states
that anthropogenic CO2 emissions primarily come from two sources:
stationary and mobile. Stationary sources refer to industrial emissions
such as those from thermal power plants and cement plants, making up
60 % of total CO2 emissions. These emissions have high concentration
levels and are emitted from specific sources. On the other hand, mobile
sources refer to CO2 emissions from human daily activities and transportation, accounting for 40 % of total emissions. These emissions are
characterized by being dispersed widely, in large quantities, and are
difficult to capture, often being directly released into the air [2]. As of


 - Corresponding author.
_E-mail_ _address:_ [hjxu@shmtu.edu.cn](mailto:hjxu@shmtu.edu.cn) (H. Xu).



now, the global concentration of CO2 and the average annual temperature have risen to 417 ppm and 0.85 ℃ [3], respectively, compared to
pre-industrial revolution levels. Research indicates that if CO2 emissions
continue without restraint based on the current trend, the average
temperature will increase by at least 2 ℃ by the year 2050, leading to
more severe natural disasters [4]. Fig. 1 illustrates the cumulative
emissions of CO2 and other greenhouse gases from human activities
between 1750 and 2022. This data is crucial for evaluating the long-term
impact of these emissions on climate change and its potential effects.
Monitoring and decreasing these emissions are essential steps in
addressing global warming and working towards sustainable development [5].
Currently, CO2 capture technology primarily utilizes a centralized
capture approach in stationary sources like power plants. This can be
divided into three distinct methods: capturing before the combustion
process, capturing during oxygen-enriched combustion, and capturing
after the combustion process. Fig. 2 provides a detailed classification of
different CCUS technologies aimed at addressing the issue of emissions



[https://doi.org/10.1016/j.enconman.2024.119119](https://doi.org/10.1016/j.enconman.2024.119119)
Received 26 June 2024; Received in revised form 4 September 2024; Accepted 29 September 2024

Available online 3 October 2024
0196-8904/© 2024 Elsevier Ltd. All rights are reserved, including those for text and data mining, AI training, and similar technologies.


_H._ _Xu_ _et_ _al._ _Energy_ _Conversion_ _and_ _Management_ _322_ _(2024)_ _119119_



**Nomenclature**


_Acronym_
MOF Metal-organic frameworks
DAC Direct air carbon capture
BN Boron nitride
DOE Department of energy
PSA Pressure swing adsorption
MSA Moisture swing adsorption
VSA Vacuum swing adsorption
TSA Temperature swing adsorption
CCUS Carbon capture utilization and storage
PFO Pseudo-first-order
PSO Pseudo-second-order
_P_ Pressure (Pa)



_T_ Temperature (K)
_q_ / _A_ Heat flow rate (W⋅m [−] [2] )
_R_ Universal gas constant (J⋅mol [−] [1] ⋅K [−] [1] )
_ΔG_ Free energy (J⋅kg [−] [1] )
_K_ Permeability (m [2] )
_μ_ v Dynamic viscosity (Pa⋅s)
_q_ e Adsorption capacity at equilibrium (mg⋅L [-1] )
_q_ t Adsorbed amount of the adsorbate at time t (mg⋅L [-1] )
θ Occupied fraction of the active sites (0 ≤ θ ≤ 1)
_k_ a Adsorption rate constant (L⋅mg [−] [1] ⋅h [−] [1] )
_k_ d Desorption rate constant (h [−] [1] )
_C_ t Adsorbate concentration at time t (mg⋅L [-1] )
_k_ 2 Pseudo-second-order rate constant (g⋅mg [−] [1] ⋅h [−] [1] )
Δ _H_ Isosteric heat of adsorption (J⋅mol [−] [1] )
_k_ eff Effective thermal conductivity (W⋅m [−] [1] ⋅K [−] [1] )



**Fig.** **1.** CO2 emissions generated from the burning of fossil fuels and industrial activities starting from the year 1750 [6].



from stationary sources.
Direct air carbon capture (DAC) is very important to accelerate the
achievement of the carbon neutrality goal [7,8]. DAC technology is one
of the most important technologies to achieve negative CO2 emissions,
essentially reducing CO2 concentration in the air. Moreover, DAC
technology can be captured anytime and anywhere, directly docking
CO2 geological storage projects, and saving transportation costs [9].
Meeting climate change goals necessitates effective energy management, widespread decarbonization, and the implementation of negative
emissions technologies [10]. Over the past 70 years, approximately
1500 Gt CO2 has been emitted into the air, leading to a growth in atmospheric CO2 levels from 310 ppm to approximately 415 ppm today

[11]. Should current CO2 emission levels persist for the next 75 years, it
is projected that the atmospheric CO2 concentration will reach
approximately 900 parts per million by the end of the century [11]. To
limit the global temperature rise to less than 2 [◦] C, it is essential to
promptly reduce industrial emissions and implement DAC strategies

[12]. The importance of DAC technology is illustrated in Fig. 3 [13].


**2.** **Fundamentals** **of** **direct** **air** **carbon** **capture** **with** **adsorption**


DAC technology was proposed by Lacker of Alamos National



Laboratory in the United States [14]. DAC technology is a carbonnegative approach that employs renewable energy sources like wind,
solar, and geothermal energy to extract CO2 directly from the atmosphere without generating additional emissions. As a valuable complement to Carbon Capture Utilization and Storage technology, DAC offers
several advantages: (1) flexible and convenient. Its equipment can be
located anywhere, eliminating the cost of transporting CO2 to storage or
utilization sites. (2) Capturing CO2 from mobile emissions. This technology indeed plays a crucial part in addressing climate change and
mitigating greenhouse gas emissions [15].


_2.1._ _Molecular_ _interactions_ _of_ _adsorption_ _for_ _DAC_ _applications_


Due to the significance for adsorption carbon capture, molecular
interactions typically involve the use of solid sorbents, such as aminefunctionalized silica materials, which exhibit a strong affinity for CO2
due to the basic nature of amines. Various amines [16], including TEPA,
PEI-L, and PEI-H, have been utilized to functionalize mesoporous silica
SBA-15, enhancing its CO2 adsorption capacity through adsorption,
where CO2 molecules form carbamate and bicarbonate compounds with
the amine groups.
The presence of humidity introduces a complex interplay in the



2


_H._ _Xu_ _et_ _al._ _Energy_ _Conversion_ _and_ _Management_ _322_ _(2024)_ _119119_


**Fig.** **2.** Classification of CCUS Technologies.


**Fig.** **3.** The importance of DAC techniques [13].


3


_H._ _Xu_ _et_ _al._ _Energy_ _Conversion_ _and_ _Management_ _322_ _(2024)_ _119119_



molecular interactions during DAC. While water vapor can hinder CO2
adsorption by competitive adsorption in some sorbents, it can also
promote CO2 capture in amine-functionalized materials by forming
more stable carbamate and bicarbonate products. Lopez´ et al. [17]
highlights that the introduction of humidity increases the CO2 adsorption capacities of the functionalized SBA-15 materials, suggesting that
the amine-CO2 interaction is facilitated under humid conditions,
potentially due to the favorable CO2/amine stoichiometry in the presence of water.
The thermodynamic efficiency of DAC processes is affected by the
energy required to desorb both CO2 and co-adsorbed water molecules.
The study reveals a trade-off between increased CO2 adsorption capacity
under humid conditions and reduced thermodynamic efficiency due to
higher energy consumption for desorption. This underscores the
importance of considering both the molecular interactions that enhance
CO2 capture and the energy implications for practical DAC applications,
especially when designing sorbents for indoor environments where humidity levels are typical.
Chemical adsorption, also known as chemisorption, is a carbon
capture process that involves chemical reaction between the adsorbent
and CO2 molecules. The mechanism begins with the contact of CO2 with
the surface of the adsorbent, which possesses reactive sites that can
engage in chemical reactions with the gas molecules [18]. These reactions, such as the formation of carbonates from alkaline oxides or
carbamates and bicarbonates from amine compounds, result in the formation of strong chemical bonds, like covalent or ionic bonds, between
the CO2 and the adsorbent [19–21].
The exothermic nature of chemical adsorption often leads to a
release of heat as the chemical bonds are formed. This process is typically a monolayer adsorption with strong interactive forces, distinguishing it from physical adsorption which relies on weaker van der
Waals forces. Regeneration of the adsorbent is a critical aspect of the
process, as it requires additional energy input, often in the form of heat
or pressure change, to break the chemical bonds and release the
captured CO2. This is a more challenging and energy-intensive process
compared to the desorption in physical adsorption.
Chemical adsorption is highly efficient for capturing CO2, especially
from low-concentration sources, making it suitable for applications such
as industrial flue gas treatment and natural gas purification. However,
the process is faced with challenges including the energy requirement
for desorption and the need for stable and regenerable adsorbents over
time. Amine-based adsorbents are widely used in this context for their
effectiveness in capturing and releasing CO2 through heating. Alkaline
oxides are also common in high-temperature carbon capture processes,
such as those following the combustion of coal or biomass. Despite the
advantages, the long-term stability and efficient regeneration of the
adsorbent remain key issues to address in the practical application of
chemical adsorption for carbon capture.


_2.2._ _Thermodynamic_ _considerations_ _of_ _direct_ _air_ _carbon_ _capture_


The principles of thermodynamics are essential in the deployment of
DAC. DAC employs thermodynamic principles to develop and enhance
the extraction and elimination of CO2 from the surrounding atmosphere.
Within the framework of DAC, thermodynamics serves as a basis for
comprehending gas behavior, heat transfer, and chemical reactions that
are integral to the capturing process. Thermodynamic principles guide
the selection of suitable sorbents and absorbents, which are responsible
for selectively binding with CO2 and separating it from the air.
Furthermore, thermodynamics governs the energy requirements and
efficiency of the various stages of DAC systems, such as preheating,
adsorption, desorption, and compression processes. By applying thermodynamic analysis, researchers can determine the optimal operating
conditions and system configurations to maximize CO2 capture while
minimizing energy consumption. Additionally, thermodynamics enables
the assessment of the overall feasibility and sustainability of DAC



technologies [22]. By utilizing thermodynamic modeling and calculations, it is possible to assess factors such as energy input, thermal losses,
and potential environmental impacts. This process contributes to the
advancement and enhancement of environmentally friendly DAC systems with improved efficiency [23].
Lackner [24] formally proposed the concept of DAC in 2009, which
refers to the technology that uses air as the transport medium of CO2 and
directly accumulates CO2 from 40 Pa gas partial pressure. By employing
an efficient method, the air is successfully divided into pure CO2 and air
with a decreased CO2 partial pressure. The free energy change corresponding to the separation efficiency Δ _G_ sep = 19.4–21.9 kJ⋅mol [−] [1] . Energy is required for the extraction of CO2 from the atmosphere. When
analyzing the direct capture of CO2 from air or flue gas, it is adequate to
assume that gas mixtures behave ideally. Under typical temperatures
and with component partial pressures below 1 atm, both air and its
constituents can be characterized as ideal gases [25]. The corrections
from the van der Waals equation, for example, are negligible at standard
room temperature and 1 atm pressure. Certain sources offer data on the
free energy of mixing for a mole of a two-component gas (CO2 and CO2free air), which can be computed using the following equation:



(
ln _P_ 0 - _P_ CO2

~~_P_~~ 0




[
_G_ mix( _P_ 0 _, P_ CO2 ) = _RT_ _P_ CO2

~~_P_~~ 0



(
ln _PCO_ 2

~~_P_~~ 0



)
+ _[P]_ [0] [−] _[P]_ [CO][2]

~~_P_~~ 0



) ]
(1)



where _P_ CO2 represents the CO2 partial pressure, while _P_ 0 refers to the
surrounding pressure. _T_ denotes the absolute temperature of the surroundings, and _R_ stands for the universal gas constant. The logarithmic
expressions can be interpreted as an isothermal compression process
involving semi-permeable pistons that independently compressed.
Although hypothetical, these pistons operate within the boundaries set
by thermodynamic laws. The work performed by these pistons is
released from the mixture in the form of heat because there is no change
in internal energy during compression.
The free energy of mixing determines the minimum energy required
for complete separation of the input gas into pure CO2 and CO2-free air,
both delivered at ambient pressure ( _P_ 0). If the final product stream needs
to be delivered at a higher pressure, additional energy will be needed for
compression [26].
It should be emphasized that the assumption of complete elimination
of CO2 from the air flow fails to sufficiently consider the possibility of
only partial removal. The initial stream, which has a total pressure ( _P_ 0)
and a partial pressure of CO2 ( _P_ 1), is divided into two streams: one
containing pure CO2 and another with reduced CO2 partial pressure ( _P_ 2
_<_ _P_ 1). The input and output streams both retain the same temperature
( _T_ ) and total pressure ( _P_ 0).
By applying Eq.(1) to the input state with CO2 partial pressures _P_ 1
and _P_ 2, the free energy of mixing per CO2 mole can be calculated by Eq.
(2).



(
Δ _G_ = _RT_ ln _[P]_ [1]



~~_P_~~ 1



(

 - 1 − ln _[P]_ [1]



)
_P_ 2
~~_P_~~ 1 − ~~_P_~~ 2



ln _[P]_ [2]



(
+ 1 − _[P]_ [1]



~~_P_~~ 0



)(
1



)
ln _[P]_ [0] [−] _[P]_ [1]



~~_P_~~ 0 − ~~_P_~~ 2



~~_P_~~ 0




- _[P]_ [2]

~~_P_~~ 0



)(
_P_ 0
~~_P_~~ 1 − ~~_P_~~ 2



~~_P_~~ 0



)
(2)



For a more comprehensive understanding, please consult the supplementary materials. The energy input necessary for the process of
separation is represented by − Δ _G_ . When dealing with air or flue gas, it is
possible to approximate small CO2 concentrations (0 _< P_ 2 _< P_ 1), which
simplifies the third term in Eq.(2).




[
Δ _G_ ≈ _RT_ ln _[P]_ [1]



) ]
_,_ 0 _< P_ 2


(3)



ln _[P]_ [2]

~~_P_~~ 1



(

[+] _[ P]_ [2]

- 1 − _[P]_ [1]

~~2~~ ~~_P_~~ 0



~~_P_~~ 2



(

- 1 − _[P]_ [1]

~~_P_~~ 0



(

- 1 − _[P]_ [1]



)
_P_ 2
~~_P_~~ 1 − ~~_P_~~ 2



_< P_ 1 _<< P_ 0



Thorough cleansing of a diluted CO2 stream results in:



4


_H._ _Xu_ _et_ _al._ _Energy_ _Conversion_ _and_ _Management_ _322_ _(2024)_ _119119_


**Fig.** **4.** Physical meanings of PFO and PSO models [52].




[
Δ _G_ complete ≈ _RT_ ln _[P]_ [1]

~~_P_~~ 0



(
_P_ 1

 - 1 −
~~2~~ ~~_P_~~ 0



) ]
_,_ _P_ 2 = 0 _,_ _P_ 1 _<< P_ 0 (4)



challenges in DAC due to its high gas processing capacity and low liquid–gas ratio. These challenges include a significant amount of amine
solution volatilization, high vapor phase loss, and a substantial increase
in capture cost [30].
Compared with chemical absorption, solid adsorption avoids the
high latent heat of absorption liquid heating, and has obvious advantages in reducing the corrosion of equipment and resisting degradation

[8]. DAC has the characteristics of high gas processing capacity and
relatively clean air source, and the adsorption technology can effectively
solve the key problems of amine volatilization and water loss. Adsorbents mainly include physical adsorbents and chemical adsorbents [31].
Numerous formulations have been created to depict the kinetics of
adsorption processes, including the pseudo-first-order model [32],
pseudo-second-order model, mixed-order model [33], Ritchie’s equation [34], Elovich model [35], and phenomenological mass transfer
models [36]. However, issues exist in the application of these models

[37–39]. The main issue lies in the empirical nature of commonly
employed PSO and PFO models, which hinders the exploration of mass
transfer mechanisms due to their lack of precise physical interpretations.
Establishing the physical significance of these empirical models is
crucial. Secondly, the intricate solving methods for the practical application of differential kinetic models, including phenomenological
external/internal and adsorption in active sites models, restrict the
investigation of mass transfer processes using these models [40]. Lastly,
some published works misuse kinetic models [36,37]. For example, the
Frusawa and Smith model is suitable for linear isotherms but has been
incorrectly applied to Langmuir-type isotherms in certain cases [41,42].
The PFO model is represented by Eq.(8), while its linearized version
is given in Eq.(9).

_dq_ t

(8)
~~_dt_~~ [=] _[ k]_ [l][(] _[q]_ [e][ −] _[q]_ [t][)]

ln( _q_ e − _q_ t) = ln( _q_ e) − _k_ l _t_ (9)

Nevertheless, the process of linearization may lead to imprecise estimations of the parameters [43–49]. Azizian [50] deduced the PFO
model from the Langmuir kinetics model (Eq.(10)). The adsorption of
metal ions and hydrophilic compounds onto microplastics could be
depicted using the PFO model [51].

_dθ_
(10)
~~_dt_~~ [=] _[ k]_ [a] _[C]_ [t][(][1][ −] _[θ]_ [) −] _[kd][θ]_



As _P_ 1 approaches zero, the logarithmic divergence of free energy per
mole of CO2 becomes more pronounced.
The most efficient method for CO2 collection is to extract the gas
stream with the highest concentration of CO2, rather than extensively
purifying it. By considering the change in free energy (Δ _G_ 0) during
adsorption reaction (Eq.(5)), the adsorbent reaction becomes reversible
at outlet partial pressure _P_ 2 in the separation chamber (Eq.(6)).

_X_ + CO2 ↔ Y (5)



Δ _G_ = Δ _G_ 0 − _RT_ ln _[P]_ [2]

~~_P_~~ 0



= 0 (6)



A series of adsorption steps that require minimal energy can be used
to extract one mole of CO2 from the stream, reducing its partial pressure
from _P_ 1 to _P_ 2. Consequently, the integration (Eq.(7)) accounts for the
free energy associated with mixing [24].



∫ 1
Δ _G_ = _RT_

0



ln _[P]_ [(] _[x]_ [)] ~~_d_~~ _x_ (7)
~~_P_~~ 0



_2.3._ _Principles_ _of_ _adsorption_ _kinetics_


The primary objective of DAC is to extract CO2 from the atmosphere,
isolating it from other constituents and yielding both purified air and
valuable CO2 byproducts. Cooling or pressurizing the air to separate out
trace amounts of CO2 will cause unnecessary energy loss, and direct
interaction with CO2 in the air is a better choice. Many solid porous
materials have selective adsorption of CO2 because of their abundant
pores, special surface structure or specific composition. The adsorption
principle is divided into chemical adsorption and physical adsorption

[27].
Compared with the CO2 partial pressure of 12 kPa captured by flue
gas, the DAC method is limited by membrane separation and low temperature separation methods because the CO2 partial pressure of air is
only 40 Pa. At present, the mainstream scheme of DAC is to use
adsorption methods with good adaptability to CO2 partial pressure for
CO2 capture [28]. The use of ethanolamine organic amine solution for
chemical absorption has become widely used in the field of flue gas
capture [29]. However, the organic amine absorption technology faces



5


_H._ _Xu_ _et_ _al._ _Energy_ _Conversion_ _and_ _Management_ _322_ _(2024)_ _119119_



The PSO model as shown in Eq.(11) has been widely utilized in published literature to predict adsorption experimental data and determine
the rate constants for adsorption [52]. Fig. 4 illustrates the physical
interpretations of the PFO and PSO models.

_dq_ t

(11)
~~_dt_~~ [=] _[ k]_ [2][(] _[q]_ [e][ −] _[q]_ [t][)][2]

In models describing the absorption of CO2 by adsorption materials,
it is customary to consider the temperature distribution within the
adsorption process due to its significant influence on the rate and efficiency of adsorption [53]. To accurately simulate this process, a fusion
of the heat transfer equation and the adsorption equation is often
employed.
The heat conduction equation plays a pivotal role in this context. It
enables the characterization of how temperature evolves over time and
space within the adsorption apparatus, thereby allowing for the
modeling of temperature profiles within adsorption beds or columns,
where the adsorbent material incorporates the processes of heat transfer
and thermal equilibrium as essential components [54].


_2.4._ _Principles_ _of_ _heat_ _and_ _mass_ _transfer_ _for_ _adsorption_ _process_


The concept of adsorption heat transfer involves the use of a series of
chemical and physical processes to guide air, followed by its extraction
from adsorption materials or solution for subsequent release to obtain
high-purity CO2 [55,56].
Both the partial pressure and temperature of the surrounding environment influence the equilibrium of adsorption, where the adsorbate is
present [57]. When formulating the adsorption isotherm, three crucial
approaches, namely kinetics, thermodynamics, and potential theory, are
taken into account [58].
The Clausius  - Clapeyron equation [59] is employed for the determination of the isosteric heat of adsorption, and its mathematical representation is shown in Eq.(12) [60].



axial dispersion coefficient, _u_ is the superficial velocity, and _p_ is the
particle density.
As temperature rises, the exothermic nature of adsorption reduces
breakthrough time for both CO2 and N2, leading to decreased actual
adsorption capacity. Higher temperatures increase the axial dispersion
coefficient, which in turn broadens the mass transfer zone and accelerates breakthrough, resulting in a shorter breakthrough time and an
earlier detection of non-zero exit concentration. Increasing the gas flow
rate leads to an earlier breakthrough for CO2 and a faster adsorption
rate. During the adsorption phase before saturation, the amount of CO2
adsorbed increases with higher flow rates. This is because a higher flow
rate results in a greater volume of CO2 entering the fixed bed within the
same timeframe, thereby enhancing CO2 capture efficiency. Furthermore, at a constant flow rate, a higher CO2 concentration reduces the
saturation time of the adsorption bed and increases the total adsorption
amount. Additionally, an increase in porosity contributes to a higher
CO2 adsorption capacity.
In Eq.(15), the term accounting for adsorption kinetics (similar with
Eq.(8)) can be expressed with Eq.(16).



_∂q_ i

_∂_ ~~_t_~~ [=] _[ K]_ [L] _[,]_ [i]



( _q_ [*] i [−] _[q]_ [i]



) (16)



(
Δ _H_ _∂_ ln _P_
~~_RT_~~ ⋅ ~~_T_~~ [=] [−] _∂_ ~~_T_~~



_q_



)



_∂_ ~~_T_~~



(12)



The isosteric heat of adsorption, denoted as Δ _H_, relates to the pressure
( _P_ ), and temperature ( _T_ ).
The assumptions made in the theoretical models used to calculate
effective thermal conductivity ( _k_ eff) are that the adsorbent exhibits
isotropy and possesses a consistent level of porosity. Hu et al. [61]
determined the average conductivity using static measurement as:



_L_
_k_ eff = − _[q]_ _[q]_
~~_A_~~ ~~[⋅]~~ Δ [Δ] ~~_T_~~ _[L]_ [=] ~~_A_~~ ~~[⋅]~~ ~~_T_~~ 1 − ~~_T_~~ 2



(13)



where _q_ i* is the adsorbed amount of species i at equilibrium state, _q_ i is
the actual amount that adsorbed from the species i, and _K_ L,i is adsorption
time constant.
The mass transfer coefficient _K_ L considers all mass transfer resistance, i.e., internal and external cyclic resistance. When the total mass
transfer coefficient of LDF is only slightly changed, it can be inferred that
the diffusion of the mass transfer region in the system is due to axial


**Fig.** **5.** Schematic diagram showing various resistances to the transport of
adsorbate as well as concentration profiles through an idealized bidisperse
adsorbent particle demonstrating some of the possible regimes [66].



The Surface Heat Flux instrument can be used to measure the heat flow
rate through the packed sample particles, denoted as _q_ / _A_ . Additionally,
_T_ 1- _T_ 2 indicates the temperature difference along the sample column

[62].
The external mass transfer resistance is calculated using Darcy’s law

[63], which can be expressed as follows [64].



_ν_ = − _[K]_

_μ_



_∂P_
(14)
_∂_ ~~_z_~~



where _μ_ v represents the dynamic viscosity of fluid, while _K_ denotes
permeability.
Based on the above knowledge, the governing equations of adsorption transport processes for DAC applications can be established as [65]:



_∂C_ i

_[∂]_
_∂_ ~~_t_~~ [+] _∂_ ~~_z_~~ [(] _[uC]_ [i][) =] _[ D]_ [z] _[,]_ [i]



_∂_ [2] _C_ i

[−] _[ρ]_ [s]
_∂_ ~~_z_~~ [2]



1 − _ε_
_ε_



_∂q_ i

(15)
_∂_ ~~_t_~~



where _ε_ is the bed void fraction, _C_ i is the gas phase concentration of
component i, _q_ i is the average amount adsorbed of component i, _D_ z is the



6


_H._ _Xu_ _et_ _al._ _Energy_ _Conversion_ _and_ _Management_ _322_ _(2024)_ _119119_



diffusion.

_q_ m _,_ i _K_ L _,_ i _C_ i
_q_ [*] i [=] ~~1~~ + ~~[∑]~~ ~~_K_~~ L _,_ i ~~_C_~~ i



(17)



where _q_ m,i is the maximum adsorbed amount of the species i (mol kg [−]

1), _C_ i is the gas phase concentration of component i, _K_ L,i is an adsorption
constant which can be calculated as a function of temperature.



(



)



(18)




             
_K_ L _,_ i = _k_ 0 _e_



Δ _H_ ads _,_ i

~~_RT_~~



Δ _H_ ads _,_ i




[66]. The figure illustrates several stages in the process: rapid mass
transfer across the particle with equilibrium maintained (1a), micropore
diffusion as the primary control without significant macropore or
external resistance (1b), transport dominated by resistance within the
micropore interior (1c), and resistance at the surface of the microparticles (1d). It also depicts scenarios where macropore diffusion is the
controlling factor, coupled with some external resistance and no resistance within the micropores (2a), where all three resistances—micropore, macropore, and film—are significant (2b), where
resistance is present within the macropores with external film resistance
and a restriction at the micropore interior (2c), and where macropore
diffusion is combined with a restriction at the micropore mouth and
some external film resistance (2d). This figure provides a detailed understanding of how different resistances interact to influence adsorption
within the particle.


**3.** **Research** **status** **of** **adsorption** **materials** **for** **direct** **air** **carbon**
**capture**


For DAC technology, the adsorbents play a crucial role in capturing
CO2 from the atmosphere. Given the acidic nature of CO2, it is essential



where _k_ 0 is a constant that does not depend on the temperature, Δ _H_ i is
the adsorption heat (J⋅mol [−] [1] ), and it varies according to the species and
sometimes according to the amount of the adsorbed gas itself, and _T_ is
the gas temperature (K).
When the temperature changes, the equilibrium constant of the
adsorption also varies, so that the breakthrough curves will change. As
adsorption is an exothermic process, the equilibrium constant decreases
when the gas temperature increases.



) _∂q_ i

_∂_ ~~_t_~~ ~~_[ρ]_~~ [s][ −] _[h]_ [sf] _[a]_ [s] _[,]_ [esp]



~~1~~ - _ε_



_∂_ [2] _T_ s ∑(

_∂_ ~~_z_~~ [2] [+] - Δ _H_ ads _,_ i



) (
+ _[∂]_ _uρ_ f _C_ p _,_ f _T_ f
_∂_ ~~_z_~~



) _∂_ (
_ρ_ f _C_ p _,_ f _T_ f
_∂_ ~~_t_~~



(19)
)



)



_ρ_ s _C_ p _,_ s



_∂T_ s



_∂T_ s _[k]_ [s] _[,]_ [e]

_∂_ ~~_t_~~ [=] ~~1~~ 


(
_T_ s − _T_ f



)

  - 4 _[h]_ [in]

_ε_ ~~_D_~~ in



= _[k]_ [f] _[,]_ [e]

_ε_



_∂_ [2] _T_ f (

_∂_ ~~_z_~~ [2] [+] [1][ −] _ε_ _[ε]_ ~~_h_~~ sf _a_ s _,_ esp _T_ s − _T_ f



(
_T_ f - _T_ w



(
_uT_ f



(
_ερ_ f _C_ p _,_ f + (1 − _ε_ ) _ρ_ s _C_ p _,_ s



) _∂T_ f

_∂_ ~~_t_~~ [+] _[ ερ]_ [f] _[C]_ [p] _[,]_ [f]



_∂_



_∂_ ~~_z_~~



)



for these adsorbents to possess alkaline properties to facilitate effective
adsorption. Following the initial adsorption process, the next critical
step is the desorption of CO2. This involves liberating the trapped CO2
from the adsorbent, thereby restoring the adsorbent to its original state
and preparing it for subsequent capture cycles. For an adsorbent to be
ideal in DAC applications, it must meet specific conditions to ensure
efficiency and sustainability throughout repeated cycles of adsorption
and desorption [67].
Before considering other significant factors, the initial requirement
to be fulfilled is that the capture process should occur under normal
environmental conditions. It is not economically viable to pressurize,
cool, or heat extensive amounts of air, thus eliminating membrane or
cryogenic separation methods. The energy required for capture must
come from non-carbon-based sources to ensure that no additional CO2
emissions are released during the capture process, achieving negative
emissions [68].
These performance criteria [69] include density (skeleton, particles,
bed), structural properties (surface area, total pore volume, micropore
volume), and thermal properties (specific heat capacity, thermal conductivity, thermal stability) [70]. Furthermore, it is crucial to consider
factors such as exceptional selectivity, substantial capacity, rapid
transport and kinetic properties, thermal resilience, and chemical
durability [71]. Considerations of significance include the mechanical
characteristics (pertaining to solid adsorbents), simplicity in loading (for
solid adsorbents), ability to resist fouling, ease of regeneration, and costeffectiveness.
We have classified DAC adsorbents into six categories: silica gel,
metal oxides, metal–organic frameworks (MOF), carbon materials, zeolites, and polymers. These adsorbents can be either functionalized or
non-functionalized. Functionalization transforms physical adsorbents
into chemical adsorbents by forming covalent or coordination bonds
with the adsorbate, often using compounds like amines, polyamines, or
aminosilanes. Primary and secondary amines enhance DAC adsorption
efficiency, while tertiary amines require humidity for substantial
adsorption [7]. Functionalization methods include physical



∑(

= _k_ f _,_ e _[∂]_ [2] _[T]_ [f] [+ (][1][ −] _[ε]_ [)] - Δ _H_ ads _,_ i

_∂_ ~~_z_~~ [2]



_q_ i _[h]_ [in]

_∂_ ~~_t_~~ _[ρ]_ [ −] [4] _ε_ ~~_D_~~ in



) _∂q_ i



_ε_ ~~_D_~~ in



(20)
)



(
_T_ f - _T_ w



where _C_ p,f is the molar heat at constant pressure for the gas phase, _k_ f,e is
the effective fluid thermal conductivity, _C_ p,s is the solid specific heat,
(Δ _**H**_ **i** ) is the adsorption heat for the i component at zero coverage, _d_ int is
the bed diameter, and _T_ w is the wall temperature, _h_ in is the film heat
transfer coefficient between the gas and the adsorbent. The equivalent
values of density and specific heat of gas mixture is calculated with:



∑ _w_ i ∑
_ρ_ [−] f [1] = ~~;~~ _C_ p _,_ f = _C_ p _,_ i _w_ i (21)

_ρ_ i

As the intake temperature increases, CO2 reaches adsorption equilibrium more quickly, leading to a decrease in adsorption capacity.
Temperature plays a critical role in the adsorption process; higher
temperatures initially favor adsorption, but since CO2 adsorption is
exothermic, it raises the temperature within the fixed bed system.
Consequently, the thermal conductivity of the fixed bed ( _k_ f,e) becomes
crucial. The higher the conductivity, the greater the adsorption capacity.
Additionally, increasing the porosity enhances heat transfer, lowers the
temperature, and further improves CO2 capture efficiency.



_∂T_ w

_ρ_ w _C_ p _,_ w _A_ w _∂_ ~~_t_~~ [=] _[ π][D]_ [in] _[h]_ [in]



(
_T_ f - _T_ w



)

  - _πD_ out _h_ out( _T_ w − _T_ 0) (22)



where _ρ_ w is the column wall density, _C_ p _,_ w is the column wall specific
heat.
Transport processes of gas mixture through adsorbents have complex
physical mechanisms. Fig. 5 schematically represents the various resistances to adsorbate transport and the concentration profiles within an
idealized bidisperse adsorbent particle, highlighting the key regimes of
mass transfer that are essential for understanding adsorption dynamics



7


_H._ _Xu_ _et_ _al._ _Energy_ _Conversion_ _and_ _Management_ _322_ _(2024)_ _119119_


**Fig.** **6.** Comparison of (a) skeletal density, (b) particle density, (c) bed density, (d) BET surface area, (e) total pore volume, (f) micropore volume, (g) specific heat
capacity, (h) thermal conductivity, and (i) stability values among different adsorbent categories with and without additional functionalization [70].



impregnation, silane bonding, in situ polymerization, and carbonation
functionalization, the latter of which also relies on moisture for effective
CO2 capture [7]. Despite the advancements in functionalization techniques, there is currently no standard for evaluating the effectiveness of
DAC adsorbents, nor has the theoretical optimal performance been
determined [72]. This is due to the complex interdependencies among
various material properties, which complicate the development of a
comprehensive theoretical framework. Fig. 6 illustrates the differences
in material properties between functionalized and non-functionalized
samples [70].

Table 1 presents a summary of different adsorption materials classified into physical and chemisorbed adsorption materials, emphasizing
their distinct properties and characteristics. Materials for physical
adsorption, such as MOF and activated carbon, provide high surface area
and porosity, making them effective for capturing molecules [73]. Novel
nanomaterials are effective at capturing small molecules; however, they
come with a higher cost. On the other hand, silica gel and molecular
sieves are cost-effective options primarily used for moisture removal and
gas purification [74].
Chemisorbed adsorption materials include alkali metal-based adsorbents and solid amine adsorbents. They excel in capturing CO2 and
forming stable compounds, boasting high adsorption capacity and
selectivity. However, their effectiveness comes at a higher cost. The
choice of material depends on the specific application, taking into account factors like efficiency, cost, and targeted molecules or gases

[75,76].

Table 1 offers an overview of the characteristics of adsorption materials for DAC, which is essential for comprehending the effectiveness



and efficiency of various materials in capturing CO2. By comparing the
properties of various adsorption materials, researchers can determine
which ones are most suitable for this important environmental process.


_3.1._ _Physical_ _adsorption_ _materials_


When physical sorbents are present, the interaction between CO2 and
the material surface is mainly governed by van der Waals or ion quadrupole forces [87]. Physisorption, a process reliant on physical interactions for CO2 binding, generally occurs at the surface of a sorbent

[88]. Therefore, materials with high surface area, such as highly porous
or nanometer-sized materials, are desirable [88]. Commonly used materials for this purpose include zeolites, activated carbon, alumina, and
MOF [8].
Because CO2 has weak binding, it is easy to regenerate solid sorbents
through physisorption. However, the reduced thermodynamic drivers
for CO2 capture make physisorption challenging at atmospheric CO2
levels [8]. As a consequence, selectivity and uptake capacity are
reduced. Because water vapor is commonly found in the surrounding air,
certain physical sorbents like zeolites show a strong attraction to water
vapor. Consequently, the presence of water can significantly diminish
their ability to capture CO2 due to competitive adsorption. On the other
hand, hydrophobic sorbents like activated carbons are less affected by
water and show a less drastic decrease in CO2 uptake, especially at low
relative humidity.
Kumar and his colleagues [89] conducted studies on the CO2 sorption capacities of zeolite 13X, tetraethylenepentamine-impregnated
SBA-15, and microporous and ultramicroporous MOF physisorbents.



8


_H._ _Xu_ _et_ _al._ _Energy_ _Conversion_ _and_ _Management_ _322_ _(2024)_ _119119_



**Table** **1**
Summary of characteristics of adsorption materials for DAC.

Material Material type Peculiarity Cost Regeneration
properties energy



**Table** **1** ( _continued_ )

Material Material type Peculiarity Cost Regeneration
properties energy



Physical
adsorption
materials


Chemisorbed
adsorption
materials



MOF [77] Its structure is
stable and has
a high surface
area and
porosity,
allowing for
efficient CO2
capture via
structure
change.



Alkali metal
based
adsorbent[85]



High
production
cost.



Moderate
regeneration
energy due to
tunable
porosity.



Solid aminead
sorbent [86]



selectivity are
high,
although the
expense is
considerable.

CO2 is
captured by
modifying
amine
groups. It has
high
adsorption
and
migration
rates.



Relatively
low cost
due to
abundant
amine
sources.



for
desorption.


High
regeneration
energy due to
frequent
thermal or
chemical
desorption
processes.



Activated
carbon [78]



With its large
specific
surface area
and porosity,
it is possible
to efficiently
capture CO2
at low cost.

With high
surface area
and structure
stability, it is
able to trap
small
molecules,
but with high
cost [80].



Activated With its large Low cost. Low to
carbon [78] specific moderate

surface area regeneration
and porosity, energy due to
it is possible high surface
to efficiently area and mild
capture CO2 activation
at low cost. process.

Novel With high Variable Potentially
nanomaterials surface area cost high

[79] and structure depending regeneration



Variable
cost
depending
on
synthesis.



Potentially
high
regeneration
energy due to
novel
structures.



Silica gel [81] It is often Low cost. Low
used to regeneration
remove energy due to
moisture and its stable and
purify air at reusable
low cost. nature.

Molecular Adsorption is Moderate High
sieve [82] performed by cost. regeneration



Silica gel [81] It is often
used to
remove
moisture and
purify air at
low cost.



Adsorption is
performed by
screening
molecular
sizes for
separation
and
purification.



Zeolites[83] Adsorption
capacity can
be enhanced
through ion
exchange and
other
modification
techniques



Mesoporous
silica[84]



Moderate High
cost. regeneration
energy
possibly due
to specific
sorption
properties.


Moderate Variable
cost. regeneration
energy
depending on
the type and
modification.


Low cost. Require
additional
energy for
surface
modification
to enhance
CO2 capture.



Despite its
high porosity,
its weak
interaction
with CO2
results in
lower
adsorption
capacity,
making
surface
modification
an appealing
strategy for
improving
CO2 capture
efficiency in
DAC.

It can capture
CO2 and form
a stable
compound.
Its adsorption
capacity and



Moderate
to high cost
due to raw
material
price.



High
regeneration
energy due to
required high
temperatures



The results suggested that physisorbents have the ability of adsorbing
CO2 from gas mixtures rich in CO2. However, their performance for DAC
is significantly diminished by the presence of atmospheric moisture and
competitive adsorption with water. The data on CO2 and H2O sorption
indicated that manipulating pore size and pore chemistry through
crystal engineering could be an effective strategy to improve CO2 capture performance [90]. Physisorbents have the potential for quicker and
less energy-intensive regeneration, which may compensate for their
lower CO2 uptake capacity [8].


_3.1.1._ _MOF_ _materials_
MOF typically denote coordination polymers characterized by specific dimensions and spatial arrangement [91], self-assembled from
transition metal ions or metal clusters and organic ligands under hydrothermal or solvothermal conditions, and possessing a threedimensional periodic porous framework structure. The structure of
porous materials has a significant impact on their performance, and the
relatively small pore size has been a major limitation for zeolite and
similar oxide-based traditional porous materials, restricting their applications in fine chemical engineering, especially in the mediummolecular-range. The self-assembly process and structure of the MOF
materials can be found in Fig. 7 [13].
When MOF materials adsorb, it demonstrates the phenomenon of
adsorption taking place between the solid phase and gas phase. When a
gas molecule contacts with a solid material, adsorption occurs. MOF
materials adsorb gases through physical adsorption, which mainly occurs due to non-covalent interactions like van der Waals forces between
the adsorbing molecules and the solid surface [92]. The selective
adsorption of gases by MOF materials is primarily controlled by physical
adsorption mechanisms, while the material ability to selectively chemically adsorb is linked to the metal sites present within its structure [93].
In many cases, the adsorption of MOF materials combines the advantages of both physical and chemical adsorption, and thus both aspects
should be considered in the research [94]. Chemical bonds involve
electrostatic forces, hydrogen bonding, and hybridization between
various orbitals. Van der Waals forces encompass London dispersion
forces, dipole interactions, and quadrupole interactions.
MOF materials typically exhibit a larger specific surface area and a
wider range of pore structures in comparison to conventional porous
materials [95]. In the last two decades, the rapid advancement of MOF
materials has led to an increase in their functionality and a growing
diversity of types. As a result, MOF materials have demonstrated significant potential for applications involving water adsorption [96]. By
employing intentional design of chemical composition and pore structure, MOF materials can achieve full adsorption under low vapor pressure conditions (0–30 % RH) and effectively capture water vapor from
the atmosphere with minimal energy input [97]. This allows MOF materials not only to efficiently transfer energy but also to utilize the



9


_H._ _Xu_ _et_ _al._ _Energy_ _Conversion_ _and_ _Management_ _322_ _(2024)_ _119119_


**Fig.** **7.** Microstructure of MOF: (a) Pictorial representation of the self-assembly process, and (b) Structure of MOF with higher gas storage capacity [13].



**Fig.** **8.** CO2 uptake isotherms at 25 ℃ and in the pressure range 0–1 bar for
carbons derived from Jujun grass (a and c) and Camellia japonica activated at
KOH/hydrochar ratio of 2 (a and b) and 4 (c and d) [99].


abundant low-grade heat generated during industrial production processes and renewable solar thermal energy, thus achieving the cyclic
utilization of energy and freshwater production [89]. In terms of applications, medium hydrophilic MOF materials with good desorption
properties can automatically regulate indoor humidity, thereby
reducing energy consumption in air conditioning systems [69].



_3.1.2._ _Activated_ _carbon_
Activated carbon is a commonly utilized physical adsorbent material.
Its notable capacity for CO2 adsorption under varying pressures makes it
well-suited for PSA process. The CO2 adsorption process on activated
carbon is reversible, but its effectiveness can be influenced by the
presence of water vapor [98]. Enhancing the adsorption capacity and
selectivity of activated carbon is a key area of research [99,100]. Sethia

[101] have discovered a nitrogen-doped activated carbon material with
a high nitrogen mass fraction (22.3 %), large specific surface area (1317
m [2] ⋅g [−] [1] ), and large pore volume (0.27 cm [3] ⋅g [−] [1] ), containing micropores
with diameters smaller than 0.7 nm. At 25 [◦] C and 100 kPa, this material
demonstrates a CO2 adsorption capacity of 5.39 mmol⋅g [−] [1] [102], which
is currently the highest among activated carbon materials for CO2
adsorption.
The investigation into CO2 adsorption and storage by activated carbons was conducted over a pressure range of 0–20 bar at 25 ℃. The CO2
sorption isotherms, shown in Fig. 8, demonstrate that the CO2 uptake at
0.15 bar ranges from 0.6 to 1.5 mmol⋅g [−] [1], while at 1 bar it falls between
2.8 and 5.0 mmol⋅g [−] [1] . Furthermore, at 20 bar, the carbons store between 8.7 and 21.1 mmol⋅g [−] [1] [99].

Fig. 9 presents a comparative analysis of different adsorption materials, illustrating the specific surface area (a), pore volume (b), and VOCs
adsorption capacity (c) for activated carbons (ACs), zeolites, hypercrosslinked polymeric resins (HPR), and MOF [103]. It highlights the
superior performance of MOF with the largest specific surface area and
pore volume, followed by ACs, HPR, and zeolites. The adsorption capacity for VOCs also indicates MOF as the most effective with the highest
average adsorption capacity, showcasing their potential in VOCs
removal applications.


_3.1.3._ _Novel_ _nanomaterials_
Researchers are currently engaged in the creation of innovative
nanomaterials designed to effectively trap CO2. Studies [104,105] have
provided theoretical evidence that boron nitride nanosheets and nanotubes are capable of capturing CO2 under ambient conditions. By



10


_H._ _Xu_ _et_ _al._ _Energy_ _Conversion_ _and_ _Management_ _322_ _(2024)_ _119119_


**Fig.** **9.** Comparison of different adsorption materials [103].


**Fig.** **10.** Charge-controlled switchable CO2 capture process on boron nitride nanomaterials [104].



introducing external electrons into boron nitride nanomaterials, these
electrons can interact with CO2, and once the external electrons are
removed, CO2 will naturally be desorbed. The reversible CO2 capture
process based on charge interactions on boron nitride nanomaterials is
illustrated in Fig. 10 [104]. Drawing inspiration from boron nitride
materials, Tan et al. [106] have also found that highly conductive boron
graphene nanosheets with small band gaps hold significant potential for
charge-based CO2 capture applications.
Sun et al. [104,107] indicated that the CO2 capture or release process
can be efficiently regulated by manipulating the charges on boron
nitride nanomaterials. When BN nanomaterials are uncharged, CO2
molecules exhibit weak interactions and are poorly adsorbed. However,
the addition of extra electrons (resulting in a negative charge) causes
CO2 molecules to form strong bonds and be firmly adsorbed onto BN
nanomaterials. Upon the removal of electrons, CO2 molecules spontaneously detach from the BN absorbents. Furthermore, these negatively
charged BN nanosorbents exhibit high selectivity in separating CO2 from



mixtures containing CH4 and/or H2. The research underscores that BN
nanomaterials are outstanding absorbents for the controlled, highly selective, and reversible capture and release of CO2. Additionally, it is
noted that an applied charge density of approximately 1013 cm [−] [2] on BN
nanomaterials can be easily achieved experimentally.


_3.1.4._ _Molecular_ _sieves_
Similar to adsorbents like activated carbon, the performance of
molecular sieves is influenced by humidity and temperature. High humidity and elevated temperatures can significantly decrease the carbon
capture efficiency of molecular sieves [108]. As CO2 capture materials,
molecular sieves also suffer from drawbacks such as limited adsorption
capacity and poor selectivity between CO2 and N2. A method for
capturing CO2 from air using 13X zeolite molecular sieves was proposed

[109], with a regeneration temperature of 95 ℃ From previous studies

[89,90], a 12-hour continuous Dynamic Adsorption Capacity (DAC) test
was conducted on various types of molecular sieves under simulated air



11


_H._ _Xu_ _et_ _al._ _Energy_ _Conversion_ _and_ _Management_ _322_ _(2024)_ _119119_



**Table** **2**
Technical indicators of DAC by alkali metal solid chemical adsorbent.

Adsorbent References Performance Pros and cons
indicators



CaO and Ca(OH)2 [114–116] Reduces CO2 by 44 %
at a concentration of
500 mg⋅L [-1]



CaO and Ca(OH)2 [114–116] Reduces CO2 by 44 % Adsorption rate: fast
at a concentration of Regeneration
500 mg⋅L [-1] temperature: high

Energy
consumption: high
K2CO3/γ-Al2O3 [118] 0.64–0.68 mmol⋅g [−] [1] Stability: high
Regeneration
temperature: high
CaO-MgO clad [119] Capture capacity: Preparation
metal oxide (under dry conditions) temperature: high
doped with 0.28 mmol⋅g [−] [1] Energy
porous materials consumption for




[119] Capture capacity:
(under dry conditions)
0.28 mmol⋅g [−] [1]



CaO-MgO clad [119] Capture capacity: Preparation
metal oxide (under dry conditions) temperature: high
doped with 0.28 mmol⋅g [−] [1] Energy
porous materials consumption for

regeneration: high
K2CO3 activate [120] CO2 volume fraction: Regeneration
5.0 × 10 [-3] temperature: low



Adsorption capacity:
0.87 mmol⋅g [−] [1]



Regeneration
temperature: low
(100–200 ℃)
Preparation
temperature: high
(300 ℃)



conditions at a temperature of 23.4 ℃ and a relative humidity of 49 %

[110]. The results indicated that 5A zeolite molecular sieves exhibit
strong adsorption capacity and structural stability even at extremely low
CO2 partial pressures.


_3.1.5._ _Zeolites_
Zeolites, a class of microporous aluminosilicate materials, are
renowned for their well-ordered pore structures and tunable chemical
compositions. The introduction of aluminum atoms into the silicate
framework of zeolites generates negative charges, which are counterbalanced by cations such as Na [+] or La [3][+] that act as Lewis acidic sites.
These cations significantly enhance the selective adsorption of CO2 at
lower temperatures through their interaction with CO2 molecules. The
performance of zeolites can be further tailored by techniques like ion
exchange, allowing for the optimization of CO2 capture capacities under
various conditions [84]. For instance, the incorporation of iron into 13X
zeolite via an in-situ crystallization method has yielded Fe@13X zeolite,
which exhibits an increased adsorption rate and capacity compared to
the unmodified variant[111].



_3.1.6._ _Mesoporous_ _silica_
Silicon-based porous materials, like mesoporous silica, are attractive
for CO2 capture due to their low cost, easy synthesis, and high porosity

[84]. Enhancing CO2 adsorption hinges on controlling the pore structure, with methods such as pyrolysis being used to create hollow mesoporous silica with core–shell micro-nano particles, which improve
capture under certain conditions[112]. However, the non-polar surfaces
of these materials interact weakly with CO2, limiting their effectiveness
in DAC at low pressures. To overcome this, surface modifications with
functional groups that enhance CO2 interaction are being explored to
boost performance in DAC applications.


_3.2._ _Chemisorbed_ _materials_


Chemical adsorbents are essential in gas separation, purification, and
catalysis, with alkali metal-based and solid amine adsorbents being
particularly significant. Unlike physical adsorbents, chemical adsorbents offer unique advantages due to their specialized characteristics.
Alkali metal-based adsorbents stand out for their unique structures, high
surface areas, and strong chemical interactions, which facilitate selective adsorption. Solid amine adsorbents are crucial for carbon capture
and storage (CCS), engaging in cyclic adsorption and desorption through
reactions with CO2 molecules. The primary advantages of chemical
adsorbents include: (1) high selectivity for target molecules, essential for
effective separation and purification; (2) substantial adsorption capacities owing to their active sites and extensive contact areas; and (3) the
ability to be regenerated, which enhances their cost-effectiveness and
longevity. Both alkali metal-based and solid amine adsorbents continue
to advance through ongoing research and development [113].


_3.2.1._ _Alkali-metal-based_ _adsorbent_
Alkaline metal solid adsorbents are primarily composed of solid
metal hydroxides or oxides, such as Ca(OH)2, CaO, MgO, Al2O3, K2CO3,
molecular sieves, as shown in Table 2. The main mechanism of action is
the formation of carbonates with CO2, generally exhibiting high absorption capacity and rate. However, the regeneration process requires
high-temperature heating, resulting in high energy consumption. Sodium oxides and carbonate adsorbents are not suitable DAC materials
due to their low reaction rates and mass transfer efficiency [114–116].
The cross-section of the mesoporous matrix is presented in Fig. 11 [117].
Researchers are actively exploring methods to reduce regeneration



**Fig.** **11.** Illustration depicting the cross-sectional morphology of mesoporous substrates [117].


12


_H._ _Xu_ _et_ _al._ _Energy_ _Conversion_ _and_ _Management_ _322_ _(2024)_ _119119_


**Fig.** **12.** Representation of the three classes of amine adsorbent materials [121].



energy consumption, such as using mesoporous materials like activated
carbon, Al2O3, molecular sieves, and silica gel as carriers and alkali
components as active ingredients to prepare composite materials. Janna
et al.[118] prepared a γ-Al2O3-supported K2CO3 adsorbent, which
exhibited excellent CO2 capture performance in air. The energy consumption for capturing 1 mol of CO2 was 333 kJ, and it could be regenerated at 250 [◦] C and still remained usable after 80 cycles.


_3.2.2._ _Solid_ _amine_ _adsorbent_
For several decades, amine-functionalized oxide supports have been
widely used as catalysts and chromatographic media [121]. In the past
decade, there has been a notable surge in research on the use of amineoxide hybrid materials as CO2 adsorbents, prompted by the recognition
of the impact of atmospheric CO2 on global climate change. While a
significant portion of this research is focused on separating CO2 from
diluted mixtures such as flue gas from coal-fired power plants, these
supported amine materials may also be suitable for extracting CO2 from
highly diluted gas mixtures like ambient air.
Being unique chemical adsorbents that function at low temperatures,
they can work in normal conditions and spontaneously remove CO2 from
the air around them. They can be regenerated with heat or thermal
vacuum under mild conditions.
The effectiveness of DAC process relies on both the physical and
chemical properties of the adsorbent and how it operates in practical
processes, providing a scalable gas–solid contact strategy. To achieve
this, it is recommended to use overall contactors with minimal pressure
drop to offer a practical amine adsorbent/air contact mode for DAC.
Amine solutions have been widely used in the capture of highconcentration CO2 from fixed sources. However, the evaporation of
the solution during the regeneration process leads to significant heat
loss, resulting in high energy consumption. Solid amine adsorbents can



help reduce energy consumption and costs [122]. Solid amine adsorbents refer to a type of adsorbent where the amine is loaded onto a solid
carrier, and the amine reacts with CO2 to form amine formate salt ions.
As shown in Fig. 10, solid amine adsorbents can be classified into the
following three types based on their preparation methods and principles:
physical impregnation, silane covalent bonding, and in-situ polymerization [121].
Chaikittisilp et al. [123] physically impregnated polypropyleneimine
into mesoporous SiO2 foam, and the adsorbent achieved a CO2 adsorption capacity of 1.74 mmol⋅g [−] [1] . Although mesoporous SiO2 materials
are unstable under water vapor, mesoporous Al2O3 exhibits better
adsorption capacity and cycling stability [124], but it requires complex
preparation and high-temperature carbonization. Solid amine-based
adsorbents prepared using resins and porous carbon as carriers also
demonstrate excellent performance. For example, the polyethyleneimine/mesoporous carbon adsorbent has an air capture capacity of 2.25 mmol⋅g [−] [1], and the presence of moisture in the air promotes
its CO2 adsorption. However, the synthesis process is complex [125].
Belmabkhout et al. [126] prepared amine-grafted mesoporous SiO2,
which exhibited higher selectivity for CO2 over N2 and O2, achieving a
CO2 adsorption capacity of 0.98 mmol⋅g [−] [1] under ambient air conditions.
Liao et al. [127] used a diamine hydrazine to graft onto a metal–organic
framework [128], and under conditions of CO2 volume fraction of 4.0 ×
10 [−] [4] and temperature of 25℃, the adsorption capacity for CO2 reached
3.89 mmol⋅g [−] [1] . Chaikittisilp et al. [124] developed a hybrid material of
polymerized rosin-mesoporous silica, which exhibited a CO2 adsorption
capacity of 0.6 mmol⋅g [−] [1], and maintained stable performance during
short-term cycling tests. Different types of amine adsorbents are shown
in Fig. 12 [121].



13


_H._ _Xu_ _et_ _al._ _Energy_ _Conversion_ _and_ _Management_ _322_ _(2024)_ _119119_


**Fig.** **13.** A device for fixed-bed CO2 capture experiments [135].



**4.** **Adsorption** **system** **for** **direct** **air** **carbon** **capture**


The adsorption system in DAC serves as a key component responsible
for the separation and capture of CO2 from the surrounding air. It utilizes specialized adsorbents that possess the ability to selectively adsorb
CO2 molecules while allowing other components of air, such as nitrogen
and oxygen, to pass through. The system typically employs porous materials with high surface areas and specific chemical properties that
assist in the adsorption process.
The adsorption system operates through a cyclic process consisting of
adsorption, desorption, and regeneration stages. During the adsorption
stage, ambient air is passed through the adsorption bed containing the
adsorbent material. The adsorbent surface selectively captures CO2
molecules, while other components of air are allowed to pass through.



The adsorbed CO2 is then desorbed from the adsorbent bed during the
desorption stage, typically by applying heat or pressure. The regenerated adsorbent can be reused for subsequent adsorption cycles,
enhancing the overall sustainability of the DAC process.
The adsorption system offers several advantages for DAC. It enables
the capture of CO2 from low-concentration sources, such as atmospheric
air, and provides a flexible and scalable approach for carbon capture.
Additionally, the use of adsorption systems allows for the potential
integration with renewable energy sources, contributing to a more
sustainable and carbon–neutral operation. However, challenges such as
energy requirements for desorption, optimization of adsorbent performance, and large-scale implementation need to be addressed for widespread deployment of DAC.
The adsorption system plays a pivotal role in DAC, enabling the



**Fig.** **14.** Flow diagram for CO2 capture by absorption and adsorption [137].


14


_H._ _Xu_ _et_ _al._ _Energy_ _Conversion_ _and_ _Management_ _322_ _(2024)_ _119119_



selective capture of CO2 from air. Through the utilization of specialized
adsorbents and a cyclic adsorption–desorption process, the system offers
a promising approach to mitigate greenhouse gas emissions and combat
climate change. Further research and development efforts are required
to optimize the adsorption system performance, enhance its energy efficiency, and enable its large-scale implementation, ultimately contributing to a more sustainable future.


_4.1._ _Adsorption_ _process_


Amine-based materials have a high affinity for the adsorption of CO2
and are the most commonly used adsorption materials for DAC. Aminebased materials have a very high CO2 capacity, and, unlike zeolite, their
capacity increases in the presence of water. MOF has received much
attention due to their large surface area, large pore volume, and cyclic
stability. The adsorption process is based on the affinity of the solid
surface to certain gas species under different conditions. Each process
step takes place in a dedicated adsorption process, most of which a
component / module carries the entire process.
In the case of adsorption, the air entering the system must be in
contact with the adsorbent. Given the delivery of a large amount of air
flow, the design of the controller is a key aspect whose goal is to
maximize gas–solid surface contact while minimizing pressure drop.
This step represents the first feature of the adsorption process [129]. In
terms of contact techniques, fluidized beds are considered the best
choice for high gas heat fixation and mass transfer, although they imply
a substantial local pressure drop. Some existing processes use several
tortuous, shallow-filling layers. The result of the filled bed is a trade-off
that includes selection of particle size because smaller particles provide
greater surface area but lead to a greater pressure drop [130–132]. Due
to their large surface area, boulders are considered a suitable contactor
option, although they are associated with significant parasitic thermal
losses, reaching up to 40 % of the total thermal requirements of the
system. Once the adsorption is completed, the CO2 poor air is evacuated,
and the adsorbent regeneration (desorption) begins. The regeneration
method of the adsorbent is a second feature of the adsorption process.
Since the adsorption–desorption rate and equilibrium are a function of
temperature, pressure and gas composition, the regeneration of adsorbent requires one of these parameters [133].
Common adsorption of automatic fixed bed adsorption device [134].
The previous device was modified to install a second column bypass, as
shown in Fig. 13 [135]. This change allows both the vacuum route and
the column post-line to be flushed, thus improving the measurement
accuracy. To achieve the low pressure drop plate layout of consistent
with the patented design of Climeworks [136], the adsorption tower is
equipped with 1 g adsorbent sample, and the bed thickness is 3.3 cm.
Fig. 14 illustrates the schematic process for capturing CO2 through a
combination of absorption and adsorption.
The adsorption process of DAC typically involves the following steps:
Firstly, CO2 from the atmosphere is captured using adsorbents, which
can be categorized into physical adsorbents and chemical adsorbents.
This entails adsorbing CO2 from the air onto the surface or internal
structure of the adsorbent. Subsequently, the captured CO2 undergoes a
regeneration process to release or recover the CO2. Regeneration can be
achieved by altering temperature, pressure, or other operational conditions, often involving mixed processes like Pressure Swing Adsorption
(PSA), Vacuum Swing Adsorption (VSA) or Temperature Swing
Adsorption (TSA) to effectively strip CO2 from the adsorbent. Stripping
refers to the process of separating the regenerated CO2 from the adsorbent and may require adjustments in temperature, pressure, or other
operational parameters. The specific details of this adsorption process
may vary depending on the chosen adsorbent type and process conditions. Overall, this process aims to efficiently capture CO2 from the atmosphere to mitigate greenhouse gas emissions. Furthermore, this
process encompasses various physical and chemical processes, necessitating careful consideration of energy requirements and effective mass



and heat transfer.
The adsorption process is typically an integral component within a
continuous cycle, encompassing adsorption, regeneration, and CO2
release. This continuous loop ensures the sustainable utilization of the
adsorbent while achieving efficient CO2 capture. The selection of the
adsorbent is of paramount significance. Various adsorbents, such as
activated carbon, metal–organic frameworks, and solid amines, exhibit
distinct adsorption characteristics and efficiencies, thereby exerting a
pronounced impact on the adsorption and desorption performance of
CO2. The performance of adsorbents is frequently influenced by temperature and flow rates. Variations in temperature can modify the rates
of adsorption and desorption, while distinct flow rates may affect the
residence time of CO2 within the adsorbent. Adsorption rate delineates
the speed at which CO2 is adsorbed onto the adsorbent, while adsorption
efficiency signifies the adsorbent capacity for capturing CO2 [138].
These two factors collectively govern the overall performance of the
capture system. The adsorption process encompasses mass transfer
pathways that facilitate the ingress of CO2 into the microscale pores
within the adsorbent. The dimensions and distribution of these microscale pores also wield influence over the adsorption effectiveness. The
design of the adsorption process equipment, including adsorbers, regenerators, and transfer pipelines, plays a pivotal role in system performance and efficiency. An appropriate equipment structure can
optimize the capture and release of CO2 [139].
Desorption efficiency in carbon capture via adsorption is influenced
by both adsorbent properties and operational conditions. Adsorbent
characteristics, such as capacity, structure, and surface chemistry, are
critical. Higher capacity adsorbents capture more CO2 but may require
more energy for desorption. Structural attributes like pore size and
surface area affect desorption ease, with larger and well-organized pores
facilitating CO2 release. The strength of chemical interactions between
the adsorbent and CO2 also impacts desorption energy, with stronger
interactions necessitating higher energy for CO2 release.
Operational conditions, including temperature, pressure, and gas
flow rate, also affect desorption. Since desorption is endothermic, higher
temperatures generally improve desorption rates, though excessively
high temperatures may degrade the adsorbent. Reduced pressures, such
as in VSA, aid in CO2 release, while higher gas flow rates can accelerate
desorption but may decrease completeness.
Adsorbent regeneration methods significantly impact desorption efficiency. Thermal regeneration is effective but energy-intensive, while
vacuum regeneration uses reduced pressure for CO2 release and is
suitable for systems with minimal pressure variations. Purge gas
regeneration employs inert gases to scrub the adsorbent surface,
reducing desorption pressure and improving efficiency. Finally, the
stability of the adsorbent is vital for maintaining long-term desorption
efficiency and regenerative capacity, as it must withstand high temperatures or pressures without degradation.


_4.2._ _Adsorption-based_ _systems_


Keith and his colleagues [140–142] invented an aqueous alkalibased DAC technique. This new method uses two interconnected loops
to distribute concentrated CO2 as part of an ongoing process. In the
initial loop, air is combined with KOH to create K2CO3. The K2CO3 is
then transformed into CaCO3 in the pellet reactor in the second loop
through a reaction with Ca(OH)2. The resulting CaCO3 is heated to
produce pure CO2 and CaO, which is then mixed with water to form Ca
(OH)2, completing the second cycle. The energy-intensive calcination
stage at 900 [◦] C represents the most demanding step in the process, while
the subsequent three steps release heat. Using aqueous alkali solutions
for DAC offers benefits such as extended lifespan and continuous operation capability; however, these advantages come at the cost of significantly increased process complexity [143].
The energy input for the calcination process consists of two components: the sensible heat of limestone from 25 [◦] C to 900 [◦] C and the



15


_H._ _Xu_ _et_ _al._ _Energy_ _Conversion_ _and_ _Management_ _322_ _(2024)_ _119119_


**Fig.** **15.** The characteristics of PSA, TSA and VSA.



enthalpy of calcium carbonate dissociation. Zeman [144] found sensible
heat and enthalpy of dissociation values of 99.2 kJ⋅mol [−] [1] (2.25 GJ/ton
CO2) and 170 kJ⋅mol [−] [1] (3.86 GJ/ton CO2), respectively. 90 kJ⋅mol [−] [1]

(2.05 GJ/ton CO2) of this heat input can be recovered in the subsequent
chilling step from 900 [◦] C to 200 [◦] C [145]. When combined with an
estimated overall thermal efficiency of 75 %, these figures result in a net
thermal energy requirement of 238.9 kJ⋅mol [−] [1] (5.43 GJ/ton CO2).
The above thermodynamic analyses indicate that there are several
viable alternatives for DAC processes. Despite the low second law efficiencies achievable regardless of adsorbate-adsorbent affinity, PSA and
VSA appear to be unfeasible. In the case of TSA, improving the development and deployment of high-affinity adsorbents may lead to
enhanced second-law efficiencies. Conversely, for TVSA processes, it is
crucial to select regeneration temperatures that optimize the quantity of



thermal energy input into the system to maximize efficiency. The impact
of operating conditions generally follows this trend, with significant
temperature and pressure variations resulting in better working capacity
but also higher energy consumption per mole of CO2 produced. Identifying optimal operating parameter values and associated trade-offs is
essential for creating DAC processes that efficiently utilize energy inputs. Comparing MSA and calcium looping through thermodynamic
evaluations against more conventional adsorption process choices
would be highly beneficial in these cases [146]. The characteristics of
PSA, TSA, and VSA, outlining their main features are summarized in
Fig. 15.


_4.2.1._ _Pressure_ _swing_ _adsorption_
Unlike the utilization of thermal energy in the desorption process,



**Fig.** **16.** Schematic diagram of two-bed VSA system [157].


16


_H._ _Xu_ _et_ _al._ _Energy_ _Conversion_ _and_ _Management_ _322_ _(2024)_ _119119_


**Fig.** **17.** Schematic diagram for 4-step TSA cycle: (a) process, and (b) adsorption isotherm [161].



PSA/VSA depends on compressing the feed or applying vacuum during
desorption as the main sources of energy to concentrate CO2. In terms of
cycle time, PSA/VSA procedures offer significant advantages, with cycle
periods in the range of a few minutes being feasible. On the other hand,
TSA methods require significantly longer cycle times due to limitations
in heat transfer rates into and out of the adsorbent. However, attaining
sufficiently high working capacities in PSA/VSA processes can be quite
challenging when compared to TSA procedures. Elfving [147], for
example, computed working capacities for amine-functionalized polystyrene adsorbents containing 4.72 mmol nitrogen/g sorbent. To achieve working capacities exceeding 0.5 mmol CO2/g, it would be
necessary to increase the compression of the feed by tenfold or more,
expose it to vacuum levels below 0.01 mbar, or both. In DAC conditions,
achieving a feasible performance using advanced adsorbent materials
combined with PSA/VSA presents significant challenges.
PSA second law efficiencies were also computed [148]. The work
input is associated with the effort required for compressing air, which is
influenced by the level of pressurization during the adsorption step. In
this analysis, only the initial energy input applied to the feed gas was
considered as the sole work input. The second law efficiencies were
determined to be unrelated to the sorbent affinity, partially because the
calculations did not consider the fluctuations in pressure drop resulting
from larger quantities of lower-affinity adsorbents [149]. The findings
suggest that the second law coefficient increases in a nearly linear
manner as the molar fraction of the adsorbate rises, but it shows unacceptably low values within the DAC range. Any additional energy input
(such as that needed to overcome pressure drop during the adsorption
step) would further reduce these efficiencies, indicating that supplying
significant energy for highly diluted gases, especially after recovering



energy from the adsorption step, might rule out PSA-based processes for
DAC considerations [150]. Overall, their studies emphasize that the PSA
method is unlikely to be suitable for concentrating extremely diluted
adsorbates, although it is useful for separating them from the body

[151–153]. Given the operational challenges and the high compression
of energy demand, PSA/VSA technology is unlikely to be a practical
solution for DAC applications [154].


_4.2.2._ _Vacuum_ _swing_ _adsorption_
Chou and Chen [155] implemented a vacuum swing adsorption
(VSA) process using zeolite 13X to remove and concentrate CO2 from
flue gas, validating their simulation through experimental comparison.
The study analyzed twin and three-bed VSA processes, incorporating
non-isothermal operations and using advanced numerical methods for
simulation. While the three-bed process enhanced CO2 concentration,
the two-bed process achieved a higher recovery rate. Under optimal
conditions, the three-bed system reached a CO2 concentration of 63 %
with a recovery rate of 67 %. For the two-bed VSA process [156], both
CO2 concentration and recovery rate vary with changes in step time,
showing consistent trends in both simulation and experimental results.
While the three-bed process achieves higher CO2 concentration, its recovery rate is lower compared to the two-bed process. Fig. 16 illustrates
the two-bed VSA system [157].


_4.2.3._ _Temperature_ _swing_ _adsorption_
The TSA process is frequently utilized as a DAC technique, and its
level of progress is evident in its application in point-source capture
technologies. The adsorbent used in the TSA process effectively captures
CO2 at ambient temperatures and subsequently releases it at higher



17


_H._ _Xu_ _et_ _al._ _Energy_ _Conversion_ _and_ _Management_ _322_ _(2024)_ _119119_


**Fig.** **18.** Schematic of adsorption isotherms for (a) TSA, (b) PSA, and (c) PTSA/VTSA [162].



temperatures, utilizing the temperature differential to drive the separation process.
The second law efficiency of the TSA process using activated carbon
as an adsorbent was evaluated [158], revealing that optimal desorption
temperatures vary with desorption pressures. Increasing the desorption
temperature beyond a certain point, with higher thermal input, does not
proportionally enhance operational capacity. Zhu et al. [159] found that
CO2 adsorption pressures between 0.1–0.2 bar lead to second law efficiencies for DAC applications likely below 0.2, primarily due to limited
adsorption capacity of activated carbon at equilibrium (0.0004 bar). A
thermodynamic analysis explored the effects of CO2 feed concentration
(mole fraction = 10 [−] [4] to 1) and adsorbate-adsorbent affinity (Hads = 35
to 65 kJ⋅mol [−] [1] ) on efficiency [148], emphasizing that high CO2 affinity
chemisorbents are critical for TSA-based DAC. These materials require
more sensible heat per mole of CO2 recovered, leading to higher total
heat requirements for TSA systems. Additionally, Nezam et al. [160]
noted that at low feed concentrations, heat change in solid adsorbents is
significant for DAC, but becomes negligible at high feed concentrations.



Jiang et al. [161] presented the operational steps and adsorption isotherms of a single-stage variable-temperature adsorption process, as
shown in Fig. 17. Steps 1–2 involve gas adsorption, where the adsorbent
bed is cooled to maintain a low temperature for maximum CO2 uptake.
Step 2–3 is a rapid preheating phase without CO2 desorption, followed
by Step 3–4, where CO2 is desorbed by heating and transferred to the
storage bed. Step 4–1 cools the adsorbent bed to its initial state, readying
it for the next cycle. The figure also shows that in a multi-stage cycle,
each subsequent stage has higher adsorption pressure and CO2 concentration than the previous one.

Fig. 18 illustrates schematic diagrams of adsorption isotherms for
different adsorption processes [162]. The sub-figures highlight the
distinct mechanisms of each process: TSA involves temperature changes
for adsorption and desorption, PSA/VSA utilizes changes in pressure,
and PTSA/VTSA combines both pressure/vacuum and temperature
variations to optimize CO2 capture and release. These processes are
crucial for the efficient operation of DAC systems[163].



18


_H._ _Xu_ _et_ _al._ _Energy_ _Conversion_ _and_ _Management_ _322_ _(2024)_ _119119_


**Fig.** **19.** Schematic diagram for 6-step MSA cycle: (a) process, and (b) thermodynamic state [161].



_4.2.4._ _Moisture_ _swing_ _adsorption_
Different from the variable temperature adsorption, the MSA method
effectively avoids a large amount of heat consumption in the regeneration process, and has a good large-scale application prospect. Moisture


**Table** **3**
The application comparison of DAC technology in specifc companies.



swing adsorption method (MSA) was proposed in 2009 by Lackner

[164]. With regard to variations in ambient humidity and CO2 concentration, Lackner [24] proposed a fundamental moisture swing adsorption cycle based on principles of classical thermodynamics. Such method



System PSA TSA VSA MSA



Advantages Fast cycle operation
Simple equipment structure
Capble to handle higher flow



Advantages Fast cycle operation High desorption efficiency Lower compression energy Suitable for a high-humidity
Simple equipment structure Remarkably effective consumption environment
Capble to handle higher flow Equipment covers a small area Low energy consumption

Disadvantages Large energy consumption Longer system cycle time The equipment complexity is Low technical maturity
High strength of the adsorbent Large energy consumption relatively high Limited scope of application
High selectivity requirements the
adsorbent

Application Catcher of medium and high CO2 Catcher sets of low CO2 Cattrap of low CO2 concentrations CO2 capture in special
scenarios concentrations concentrations environments
Energy efficiency Large energy consumption Relatively low Large energy consumption Higher energy consumption
Running cost High operating cost High operating cost Moderate operating cost Low operating cost
References [176] [177] [178] [165]



High desorption efficiency Lower compression energy
Remarkably effective consumption
Equipment covers a small area



Low technical maturity
Limited scope of application



19


_H._ _Xu_ _et_ _al._ _Energy_ _Conversion_ _and_ _Management_ _322_ _(2024)_ _119119_


**Fig.** **20.** Schematic diagram of actual adsorption cycles: (a) P/VSA, (b) TSA and (c) TVSA [179].



uses the free energy released by water evaporation to drive the
adsorption cycle, and then absorb CO2. It absorbs CO2 in the air in a dry
environment and releases CO2 in a humid environment [165].
However, the current research on MSA is mostly concentrated on the
theory of foundations. In terms of the adsorption mechanism, Yang et al.

[166] proposed a solid-state NMR to directly explore the hygrofied CO2
absorption cycle, detailing the changes of CO2 in the adsorption process.
Shi et al. [167] proposed a water-driven CO2 adsorbent, focusing on the
diffusion of ions and the structure formed by the ionic hydrated complexes in the water-loaded resin structure. In terms of material synthesis,
Dong et al. [168–171] explored the influence of different materials on
CO2 adsorption effect. Vinylidene fluoride (PVDF) can effectively reduce
the humidity sensitivity of molding adsorbent and significantly improve
the CO2 adsorption rate. In terms of kinetics, Wang et al. [172–174]
explained that CO2 adsorption kinetics can be stimulated by controlling
the specific ionic conductivity in the wet variable adsorbent. Current
studies lack studies on cycle performance, especially on energy consumption and cycle efficiency.
The MSA cycle is based on the assumption that total pressure remains
constant with temperature. This cycle consists of six stages: adsorption,
preheating, humidification, desorption, dehumidification, and precooling, as shown in Fig. 19(a). Thermal cycling introduces temperature
variations, which can alter saturated vapor pressure. Therefore, water
vapor pressure is a more effective measure of humidity conditions than
relative humidity. In describing the MSA cycle operational processes, a



3D coordinate system is used, with axes representing CO2 adsorption
amount, temperature, and water vapor pressure (Fig. 19(b)). During the
adsorption phase, it is assumed that CO2 concentration remains constant, reflecting the atmospheric presumed infinite mass capacity for
CO2. This framework helps to visualize and analyze the overall state
changes of the cycle [161].
In order to better reflect the characteristics of each adsorption system, the four adsorption systems are comprehensively analyzed [175].
The specific contents are shown in Table 3. PSA performs well in scenarios that require fast cycling and high flow processing, but highpressure operations bring high operating costs and energy consumption. TSA is suitable for scenarios requiring high-purity CO2 capture, but
with high energy consumption and operation costs due to the long
heating and cooling cycle. VSA achieves high energy efficiency by
reducing operating pressure, which is suitable for small and mediumscale applications with moderate operating costs. As an emerging
technology, MSA has application potential in special environments with
high humidity, with high energy efficiency, low operation cost, but
limited application scope. When selecting the adsorption carbon capture
system, a comprehensive evaluation is needed according to the specific
application scenarios, CO2 concentration, economy and energy consumption factors, so as to choose the most feasible technical scheme.

Fig. 20 presents a detailed schematic of the actual adsorption cycles
for P/VSA, TSA, and TVSA [179]. This diagram illustrates the thermodynamic processes involved in each cycle and highlights the differences



20


_H._ _Xu_ _et_ _al._ _Energy_ _Conversion_ _and_ _Management_ _322_ _(2024)_ _119119_


**Fig.** **21.** Design of (a) TVSA process cycles, air contactor, (b) CO2 capture system. Explore, (c) CO2 capture system, and (d) separation exergy relationship with
various adsorbent isotherms [180].



between ideal and real adsorption cycles. It emphasizes the impact of
factors such as temperature variations, adsorption heat, and concentration drops, which contribute to irreversible capacity loss in practical



applications. The figure outlines the key steps in each cycle: adsorption,
heating, vacuum application, and cooling, which demonstrates how
these processes are optimized for effective CO2 capture and release.



**Fig.** **22.** The key components of the containerized modular DAC device [192].


21


_H._ _Xu_ _et_ _al._ _Energy_ _Conversion_ _and_ _Management_ _322_ _(2024)_ _119119_



**Fig. 23.** Scheme of the experimental apparatus for the DAC experiments[195].


_4.3._ _Devices_ _of_ _direct_ _air_ _carbon_ _capture_


Until now, TVSA has stood out as the most extensively employed
DAC process, boasting favorable thermodynamics that necessitate only a
gentle vacuum for concentrating high-purity CO2 [147]. The utilization
of heating and vacuum results in increased operational capacities while
simultaneously decreasing the necessary adsorbent volume. Comparative analyses in techno-economics indicate that the TVSA-based DAC
process outperforms alkali and amine scrubbing in terms of exergy demand (1.4–3.7 GJ⋅ton CO−2 1) and CO2 productivity (3.8–10.6
kg⋅m [−] [3] ⋅h [−] [1] ), as illustrated in Fig. 21 [180]. While all three technologies
have the potential to achieve a total cost below $200 tCO−2 1, the TVSAbased DAC process is more efficient across a diverse range of conditions.
Notably, the minimum energy needed for separating CO2 at 400 ppm is
only 0.45 GJ⋅ton CO−2 1 [181]. To achieve further reductions in the energy consumption of the TVSA process, it is essential to deepen our
understanding of multicomponent adsorption and develop innovative
air contactors with high heat and mass transfer capabilities. These advancements will be crucial in enhancing the overall efficiency of the
TVSA process [182]. Furthermore, integrating heat recovery through
heat exchangers or heat pumps plays a pivotal role in achieving these
advancements. This approach can significantly contribute to improving
the overall energy efficiency of the process [183].
Climeworks, based on the technology of ETH Zurich, is a leading
DAC company that employs the TVSA process. In this approach, the
saturated adsorbent on an air filter-like contactor undergoes regeneration at temperatures ranging from 80 to 130 ℃ [184] under reduced
pressures [185]. NFC adsorbents with aminopropyl grafting are predominantly employed, achieving a capacity of 1.39 mmol⋅g [−] [1] at 400
ppm CO2 and 40 % relative humidity. In a practical TVSA cycle, the
maximum CO2 working capacity can reach 0.65 mmol⋅g [−] [1] at 10 [◦] C and
80 % relative humidity[186].
Climate Works has established a pilot plant in Dresden utilizing the
TVSA process, which captures 80 % of the intake CO2 and converts it
into synthetic diesel. Subsequent to this successful endeavor, a commercial DAC unit was installed in a Hinwil greenhouse, capturing 900
tonnes of CO2 annually. Furthermore, another DAC demonstration unit



(CarbFix2) has been implemented in Iceland, employing dual flash lights
to produce hot water at 120 degrees Celsius for heating. The desorbed
high-purity CO2 is compressed, mixed with water and injected into a
700 m deep basalt reservoir for mineralization [187].
Climeworks introduced a larger-scale DAC plant called Orca, with
the goal of capturing 4000 tons of CO2 annually. Currently operating 15
DAC facilities, Climeworks aims to reduce the overall DAC cost to below
$92 tCO−2 1 in the near term.
Oy Water Battery Co., Ltd. has developed an 8-bed modular DAC unit
(measuring 1 m x 0.2 m each) with a CO2 productivity of 0.0038TPD for
the VTT Technical Research Center of the Sunstand project. The system
uses two key technologies: a brush-type heat exchanger and a renewable
CO2 scrubber. To enhance the heat source of DAC, a glycol/water
mixture enables regeneration at temperatures ranging from 60-80 [◦] C.
Previous studies have explored the feasibility of implementing a TVSA
process with low regeneration temperatures for this system [147]. Due
to the fact that humidity can enhance equilibrium working capacity by
up to 80 %, a kinetic model was suggested to depict the adsorption of
CO2/H2O on the amine-functionalized polystyrene resin adsorbent

[188]. However, a ten-day capture campaign revealed a 76 % specific
energy requirement due to thermal energy needs [134]. Comparative
experiments indicate that employing air purge at 100 [◦] C provides benefits over the TVSA process. Their DAC prototype has been effectively
utilized in a Power-to-X plant and a biological–inorganic system

[189,190]. Recently, Schellevis et al. [191] developed a similar TVSA
process utilizing thin ’flat bed’ contactors (2.4 cm thickness and 40 cm
diameter). A higher desorption temperature is advantageous for both
energy efficiency and productivity, mainly due to the decreased
desorption time required. Fig. 22 depicts a schematic of the fundamental
components of the container modular DAC device developed by the VTT
Technical Research Center [192].
For recovering the valuable CO2-reactive chemicals present in the
enriched aqueous solution, the CO2-rich solvent is directed to ascend a
second regeneration tower. As it descends through this tower, the solvent undergoes heating using steam to achieve a sufficiently high temperature for thermally separating CO2 from MEA. Once it reaches the
bottom, almost all the CO2 has been released from the MEA solution.
This freed solution is then pumped back to the top of the first tower to
start another cycle [145].
The CO2 emissions of solvents are typically released into the atmosphere after rising to the upper section of the regenerator [193].
Nevertheless, in three well-documented instances—namely the In Salah
gas field in Algeria, the Sleipner gas field off the coast of Norway, and
the Snøhvit project in the Barents Sea—the captured CO2 is safely stored
underground [194].
Veselovskaya et al. [195] describe a DAC system depicted in Fig. 23,
including the following components: (1) a cylindrical fixed-bed adsorber
equipped with a composite sorbent for CO2 absorption; (2) an electrical
heater encircling the adsorber to facilitate thermal desorption; (3) a
4.58-gram composite sorbent used for CO2 capture; (4) a PID controller
(Termodat-13 K2) for precise automatic heating regulation; and (5) two
K-type thermocouples for monitoring and controlling the temperatures
within the adsorber and sorbent layer.

Table 4 provides a comprehensive summary of various adsorption
device configurations relevant to DAC applications. It includes ten devices, such as fixed-bed adsorption columns and fluidized adsorption
beds, detailing their research characteristics and performance metrics.
This summary offers valuable insights into the capabilities of different
adsorption systems, aiding in the selection of appropriate equipment for
establishing DAC applications.


_4.4._ _Detailed_ _studies_ _in_ _practical_ _applications_


Some companies are already using sorbent-based technologies to
capture CO2 directly, thereby reducing atmospheric CO2 concentrations.
Much of the development of DAC has focused on adsorption processes,



22


_H._ _Xu_ _et_ _al._ _Energy_ _Conversion_ _and_ _Management_ _322_ _(2024)_ _119119_


**Table** **4**
Various adsorption device confgurations potential for DAC applications.

No. Device configuration Research characteristics Performance Ref.



column via adsorption, focusing on refining equations for
accurate system representation.


conventional packed beds. Despite increased energy use,
foams enhance productivity, suggesting potential for
reduced overall process costs.


multi-stage fluidized bed system with integrated heat
exchange for adsorption and desorption processes.


unit (ETAU) design, featuring core tubes packed with
adsorbents and shell-side fluid pathways for efficient heat
transfer during the VTSA process for CO2 capture.


and cooling for efficient CO2 capture via temperature
swing adsorption.


with the adsorption bed, showcasing both single-tube and
three-tube designs for enhanced heat transfer during the
adsorption process.


framework for analyzing temperature and mass transfer
in a CO2 capture system.


23



The model closely matches experimental data from a
pressure swing adsorption test, proving its effectiveness
in optimizing carbon capture.


Packed foam offers superior heat transfer, resulting in
reduced temperature gradients and more uniform, faster
heating in the adsorption column.


The bench-scale unit effectively achieving the designed
CO2 capture targets through a temperature swing
adsorption process.


Promoting heat transfer and CO2 capture efficiency in
the VTSA process with ETAU.


Depicting the effective CO2 capture in an adsorbentpacked heat exchanger using temperature swing
adsorption.


Enhance CO2 capture efficiency through optimized
temperature management.


It depicts the experimental setup for temperature and
vacuum swing desorption, showcasing effective CO2
capture from air with high purity recovery.




[196]


[197]


[198]


[199]


[200]


[201]


[185]



( _continued_ _on next page_ )


_H._ _Xu_ _et_ _al._ _Energy_ _Conversion_ _and_ _Management_ _322_ _(2024)_ _119119_


**Table** **4** ( _continued_ )

No. Device configuration Research characteristics Performance Ref.



efficiently capturing CO2 with low-temperature steam. steam, potential for energy savings and efficient
integration with waste heat in large-scale applications.



capacity of supported amine sorbents, and demonstrated
continuous CO2 capture in a circulating fluidized bed
reactor using silica-based sorbents.


integration of heat exchange and continuous adsorbent
movement for CO2 capture.



The supported amine sorbents achieved significant CO2
adsorption capacities, with a high-purity ( _>_ 90 %) CO2
product stream produced through thermal swing
adsorption at a minimal temperature differential.


It outlines the scalable MBTSA unit design for CO2
capture, indicating efficient heat integration and process
dimensions.




[202]


[203,204]


[205]



**Fig.** **24.** Business flowchart of DAC technology [206].


most of which utilize chemical adsorbents in the adsorption step. The
pioneers in this field include Climeworks, Carbon Engineering, Skytree,
Infinitree, and Global Thermostat among other existing players. Fig. 24
presents the initial research on DAC, wherein all primary elements are
sourced from reputable commercial heritage or thoroughly described to
enable evaluation by external entities [206].
Two enterprises, Climeworks and Carbon Engineering, have been
involved in this sector for the last ten years and presently manage facilities in Europe and North America correspondingly [207]. Climeworks is in the process of building a facility in Hellisheidi, Iceland that
will have the capacity to capture 4,000 metric tons of CO2 annually. This
plant became operational in September 2021 [208]. Carbon Engineering
is currently constructing a commercial facility in Texas, United States,
which will possess the capability to capture and eliminate approximately one million tons of CO2 annually [209]. Black and Veatch, an



engineering company, was granted funding by the Department of Energy
(DOE) to construct a DAC facility with a capacity of 100,000 tons per
annum utilizing the technology of Global Thermostat. Global Thermostat is now constructing two plants in Oklahoma, USA, each with a capacity of 2,000 metric tons per year, expected to be completed in 2021.
These DAC plants operate by extracting air from the atmosphere, utilizing sorbents and heat to remove CO2. Additionally, there is a passive
type of DAC that does not require dynamic components or thermal energy [8]. The MechanicalTree, a passive DAC system developed by researchers at Arizona State University, can remove 1 ton of CO2 per day,
with a prototype model planned for deployment in Arizona, USA, in
2022–23. Apart from these companies, other private companies/startups [210] working on DAC technology include Heirloom Carbon,
Mission Zero, Sustaera, Noya, and Verdox [13,211]. Carbon Infinity
focuses on manufacturing small, modular, easily deployable DAC units
to reduce costs for end-users. The objective of carbon capture is to
decrease operational expenses by utilizing molecular sieves and integrating affordable renewable energy sources like solar power for thermal needs. Table 5 describes the detailed information of different DAC
companies [212].The location, CO2 absorption rate, adsorbent type and
so on of each company are compared and summarized.
Economy is very important, which is related to the large-scale promotion of DAC. Qiu et al. [222] highlights that DAC facilities should be
placed where cheap, carbon-free energy is available or near pipeline and
storage sites to cut transportation costs. However, DAC technologies
require significant energy and materials due to the low concentration of
CO2 in the atmosphere. The environmental impact of DAC depends on
the electricity system used, affecting overall greenhouse gas emissions.
Sodiq et al. [68] notes that global research is focused on reducing DAC
energy demands, essential for its commercial viability. The economic
and energy efficiency of DAC are linked to technological advances and
access to clean energy. Assessing and managing the environmental impacts is crucial, particularly in relation to regional energy planning.
Ongoing R&D is vital for enhancing DAC techno-economic and environmental performance to support climate change mitigation
effectively.


**5.** **Conclusions**


This article provides a comprehensive review of the advancements in
DAC technology, focusing on adsorbent materials, adsorption mechanisms, system design, and applications. Over the past decade, DAC



24


_H._ _Xu_ _et_ _al._ _Energy_ _Conversion_ _and_ _Management_ _322_ _(2024)_ _119119_


**Table** **5**
The application comparison of DAC technology in specifc companies.



Company Location CO2 Removal
Capacity (metric
tons/yr)



Sorbent Type Market Application


Solid Renewable fuels, Food, Beverages, and Agriculture,
Greenhouse CDR services



Climeworks [213,214] Europe Net: 2,000
900
4,000



Carbon Engineering



Carbon Engineering UK 350 Liquid Carbon neutral fuel CO2 capture and storage for shopify and

[194] 1,500 virgin

1,000,000 Enhanced oil recovery and carbon sequestration

Global Thermostat America 1000 tCO2/year Solid sorbent Not for commercial use



UK 350
1,500
1,000,000




[194]



Global Thermostat America 1000 tCO2/year Solid sorbent Not for commercial use

[162] Synthetic gasoline CO2 based fuel, CO2 as industrial gas

[215]
Mechanical Tree [216] America 30 tons from a single tree 4 million/Farm Moisture driven CO2 Agriculture, CO2 based fuel, Building materials,
sorbents Sequestration
Infinitree [217] America 100 Ion exchange sorbent Greenhouse application
material




[162]



Skytree [13] Europe 200 kg/day Solid sorbent Car appliances, Industrial processes
Verdox [218] America Capture rate of 90 % for CO2 concentrations of Chemical adsorbent /
0.6 to 10 %



Carbon Capture [219] America Capture 5 MtCO2 /year by 2030 Solid sorbent Tamarack nickel mine
TerraFixing [220] Canada 1 MWh/tCO2 Solid sorbent /
Soletair Power [189] Finland 47 kg per day/ 20 tonnes per year Turn to carbonates Building-integrated technology retrofittable within urban
infrastructures
Breakthrough Energy Europe / Electrochemical process Agriculture, Buildings, Electricity, Manufacturing,




[221]



Europe / Electrochemical process Agriculture, Buildings, Electricity, Manufacturing,
transportation



technology utilizing adsorbents has seen rapid progress, with significant
research into materials such as zeolites, MOF, nanomaterials, and alkali
metal-based substances. Despite these advances, there remains a lack of
thorough techno-economic evaluations necessary for large-scale DAC
implementation.
Evaluating the effectiveness of DAC adsorbents involves several
critical factors: the ability to selectively capture CO2 in the presence of
other gases, the efficiency of adsorption and desorption cycles, and the
kinetics of these processes. Additionally, the energy requirements for
regeneration, chemical stability over time, durability during extended
use, and performance under varying temperature and humidity conditions are essential considerations. A comprehensive evaluation must
integrate material properties, cycle configurations, and adsorption device designs. Collaborative efforts in developing new materials, equipment, and system architectures will be crucial to meeting both current
and future carbon capture demands.
While significant research has been conducted on DAC adsorbents
and devices, achieving a balance between low cost and high performance remains a challenge. Solid porous materials combined with
organic amines offer advantages such as high CO2 selectivity and low
regeneration temperatures, which can reduce energy consumption and
enhance flexibility. However, selecting cost-effective and structurally
optimized carriers and ensuring the long-term stability of organic
amines are ongoing challenges.


**6.** **Future** **Prospects** **and** **Recommendations**


This review thoroughly examines the advancements in DAC technology, highlighting the evolution of adsorbent materials, adsorption
mechanisms, system design, and practical applications. Significant
progress has been made over the past decade with materials such as
zeolites, MOF, nanomaterials, and alkali metal-based substances. However, a comprehensive techno-economic evaluation for large-scale DAC
implementation remains notably absent.
The effectiveness of DAC adsorbents depends on multiple critical
factors: their ability to selectively capture CO2 amidst other gases, the
efficiency of adsorption and desorption cycles, and the kinetics of these
processes. Further considerations include the energy demands for
regeneration, chemical stability over time, and material durability
under various operational conditions. A holistic evaluation requires an
integrated analysis of material properties, cycle configurations, and



adsorption device designs. Collaborative efforts in developing advanced
materials, optimized systems, and innovative architectures are essential
to meet both current and future carbon capture needs. Addressing these
challenges will be key to advancing DAC technology in carbon capture
and climate mitigation.


**CRediT** **authorship** **contribution** **statement**


**Huijin** **Xu:** Writing  - review & editing, Writing  - original draft,
Visualization, Project administration, Funding acquisition, Formal
analysis, Conceptualization. **Liyang** **Yu:** Writing - review & editing,
Writing – original draft, Resources, Formal analysis. **Chengtung Chong:**
Writing – review & editing. **Fuqiang Wang:** Writing – review & editing.


**Declaration** **of** **competing** **interest**


The authors declare that they have no known competing financial
interests or personal relationships that could have appeared to influence
the work reported in this paper.


**Data** **availability**


No data was used for the research described in the article.


**Acknowledgement**


This work is supported by National Natural Science Foundation of
China (51876118).


**References**


[1] Ciavarella A, Cotterill D, Stott P, Kew S, Philip S, van Oldenborgh GJ, et al.
Prolonged Siberian heat of 2020 [almost](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0005) impossible without human influence.
Clim [Change](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0005) 2021;166:9.

[2] Ngwabie NM, Vanderzaag A, [Jayasundara](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0010) S, Wagner-Riddle C. Measurements of
emission factors from a [naturally ventilated](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0010) commercial barn for dairy cows in a
cold climate. Biosyst [Eng](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0010) 2014;127:103–14.

[3] Carbon Dioxide Direct Measurements: 2005-present 2018. NASA.

[4] Ding Z, Duan X, Ge Q, Zhang Z. [Control](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0020) of atmospheric CO2 concentrations by
2050: a calculation on the emission [rights](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0020) of different countries. Sci China Ser D
Earth Sci [2009;52:1447–69.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0020)

[5] Rogelj J, Luderer G, Pietzcker RC, [Kriegler](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0025) E, Schaeffer M, Krey V, et al. Energy
[system transformations for limiting end-of-century warming to below 1.5](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0025) [◦] C. Nat
Clim Chang 2016;5:538-.



25


_H._ _Xu_ _et_ _al._ _Energy_ _Conversion_ _and_ _Management_ _322_ _(2024)_ _119119_




[6] Cumulative CO2 emissions. Hannah Ritchie, Pablo Rosado and Max Roser (2023).

[7] Sanz-P´erez ES, Murdock CR, Didas SA, Jones CW. Direct capture of CO2 from
ambient air. Chem [Rev](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0035) 2016;116:11840–76.

[8] Shi X, Xiao H, Azarabadi H, Song J, Wu X, Chen X, et al. Sorbents for the direct
capture of CO2 from ambient air. [Angew](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0040) Chem Int Ed 2020;59:6984–7006.

[9] Pacala S, Al-Kaisi M, Barteau M, [Belmont](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0045) E, Benson S, Birdsey R, Hudson M.
Negative emissions technologies and [reliable](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0045) sequestration: a research agenda.
Natl Acads Sci Eng Med 2018.

[10] McQueen N, Gomes KV, McCormick [C,](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0050) Blumanthal K, Pisciotta M, Wilcox J.
A review of direct air capture (DAC): [scaling](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0050) up commercial technologies and
innovating for the future. [Progress](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0050) in Energy 2021;3.

[11] R. Lindsey. Climate Change: Atmospheric Carbon Dioxide. in: N. 2022, (Ed.).
https://www.climate.gov/news-features/understanding-climate/climate-changeatmospheric-carbon-dioxide, 2023.

[12] Chiari L, Zecca A. Constraints of [fossil](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0060) fuels depletion on global warming
projections. Energy [Policy](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0060) 2011;39:5026–34.

[13] Chowdhury S, Kumar Y, Shrivastava S, Patel SK, Sangwai JS. A review on the
recent [scientific and commercial progress on](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0065) the direct air capture technology to
manage atmospheric CO2 [concentrations](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0065) and future perspectives. Energy Fuel
[2023;37:10733–57.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0065)

[14] Lackner K, Ziock HJ, Grimes P. [Carbon](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0070) dioxide extraction from air: is it an
option? [United](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0070) States 1999.

[15] A.P. Maria Jo˜ao Regufe, Alexandre F. P. Ferreira, Ana Mafalda Ribeiro and Alírio
E. Rodrigues. Current Developments of Carbon Capture Storage and/or
Utilization–Looking for Net-Zero Emissions Defined in the Paris Agreement.
Energies. 14 (2021) 1-26.

[16] Surkatti R, Abdullatif YM, Muhammad [R,](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0080) Sodiq A, Mroue K, Al-Ansari T, et al.
Comparative analysis of [amine-functionalized](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0080) silica for direct air capture (DAC):
[material characterization, performance, and thermodynamic efficiency. Sep Purif](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0080)
Technol [2025;354:128641.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0080)

[17] Lopez´ LR, Dessì P, Cabrera-Codony [A,](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0085) Rocha-Melogno L, Kraakman NJR,
Balaguer MD, et al. Indoor CO2 direct [air](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0085) capture and utilization: key strategies
towards carbon neutrality. [Cleaner](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0085) Eng Technol 2024;20:100746.

[18] Brito-Ravicini A, Calle-Vallejo F. [Interplaying](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0090) coordination and ligand effects to
break or make adsorption-energy [scaling](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0090) relations. Exploration 2022;2:
[20210062.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0090)

[19] [Fu T, Saracho AC, Haigh SK. Microbially induced carbonate precipitation (MICP)](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0095)
for soil strengthening: a [comprehensive](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0095) review. Biogeotechnics 2023;1:100002.

[20] Zhang J, Fang W, Liu Z, Tang R. [Inorganic](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0100) ionic polymerization: a bioinspired
strategy for material [preparation.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0100) Biogeotechnics 2023;1:100004.

[21] Wang Y, Konstantinou C, Tang S, [Chen](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0105) H. Applications of microbial-induced
[carbonate precipitation: a state-of-the-art review. Biogeotechnics 2023;1:100008.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0105)

[22] Pritchard C, Yang A, Holmes P, [Wilkinson](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0110) M. Thermodynamics, economics and
systems thinking: what role for air [capture](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0110) of CO2? Process Saf Environ Prot
[2015;94:188–95.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0110)

[23] Ji Y, Yong J, Liu W, Zhang X, Jiang L. Thermodynamic analysis on direct air
capture for building air condition [system:](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0115) balance between adsorbent and
refrigerant. Energy Built Environ 2023;4:399–407.

[24] Lackner KS. The thermodynamics of [direct](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0120) air capture of carbon dioxide. Energy
[2013;50:38–46.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0120)

[25] Keith DW. Why capture CO2 from the [atmosphere?](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0125) Science 2009;325:1654–5.

[26] [Zhang L, Yin Y, Li L, Wang F, Song Q, Zhao N, et al. Numerical simulation of CO2](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0130)
adsorption on k-based sorbent. Energy Fuel 2016;30:4283–91.

[27] Jia X, Zhang H, Zhang Z, An L. [First-principles](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0135) investigation of vacancy-defected
graphene and Mn-doped graphene [towards](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0135) adsorption of H2S. Superlattice
Microst [2019;134:106235.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0135)

[28] Jones CW. CO2 capture from dilute [gases](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0140) as a component of modern global
carbon management. Annu Rev [Chem](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0140) Biomolecular Eng 2011;2:31–52.

[29] Rochelle GT. Amine scrubbing for [CO2](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0145) capture. Science 2009;325:1652–4.

[30] [Kiani A, Jiang K, Feron P. Techno-economic assessment for CO2 capture from air](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0150)
using a conventional liquid-based [absorption](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0150) process. Front Energy Res 2020;8:
[92.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0150)

[31] Pinsent BRW, Pearson L, Roughton [FJW.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0155) The kinetics of combination of carbon
dioxide with hydroxide ions. [Trans](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0155) Faraday Soc 1956;52:1512–20.

[32] Lagergren SK. About the theory of [so-called](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0160) adsorption of soluble substances.
Sven Vetenskapsakad [Handingarl](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0160) 1898;24:1–39.

[33] Guo X, Wang J. A general kinetic [model](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0165) for adsorption: theoretical analysis and
modeling. J Mol [Liq](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0165) 2019;288:111100.

[34] Ritchie AG. Alternative to the Elovich [equation](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0170) for the kinetics of adsorption of
gases on solids. J Chem Soc, [Faraday](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0170) Trans 1 1977;73:1650–3.

[35] Elovich SY, Larinov OG. Theory of [adsorption](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0175) from solutions of non electrolytes
on solid (I) equation adsorption from [solutions](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0175) and the analysis of its simplest
form,(II) verification of the equation of adsorption isotherm from solutions. Izv
Akad Nauk SSSR, Otd [Khim](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0175) Nauk 1962;2:209–16.

[36] Monte Blanco SPD, Scheufele FB, [Modenes´](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0180) AN, Espinoza-Quinones˜ FR, Marin P,
Kroumov AD, et al. Kinetic, [equilibrium](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0180) and thermodynamic phenomenological
[modeling of reactive dye adsorption onto polymeric adsorbent. Chem Eng J 2017;](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0180)
[307:466–75.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0180)

[37] Marin P, Borba.. Determination of [the](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0185) mass transfer limiting step of dye
adsorption onto commercial adsorbent [by](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0185) using mathematical models. Environ
Technol [2014;35:2356–64.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0185)

[38] Scheufele FB, Modenes AN, Borba [CE,](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0190) Ribeiro C, Espinoza-Quiones FR,
Bergamasco R, et al. [Monolayer-multilayer](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0190) adsorption phenomenological model:
kinetics, equilibrium and [thermodynamics.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0190) Chem Eng J 2016;284:1328–41.




[39] Suzaki PYR, Munaro MT, Triques [CC,](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0195) Kleinübing SJ, Klen MRF, de Matos
Jorge LM, et al. Biosorption of binary [heavy](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0195) metal systems: phenomenological
mathematical modeling. [Chem](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0195) Eng J 2017;313:364–73.

[40] Furusawa T, Smith JM. Fluid-particle [and](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0200) intraparticle mass transport rates in
slurries. Ind Eng Chem [Fundam](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0200) 1973;12:197–203.

[41] [Ozer A, Akkaya G, Turabik M. The biosorption of Acid Red 337 and Acid Blue 324](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0205) [¨]
on enteromorpha prolifera: The [application](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0205) of nonlinear regression analysis to
dye biosorption. Chem [Eng](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0205) J 2005;112:181–90.

[42] [Wang BE, Hu YY, Xie L, Peng K. Biosorption behavior of azo dye by inactive CMC](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0210)
immobilized aspergillus fumigatus [beads.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0210) Bioresour Technol 2008;99:794–800.

[43] Darwish AAA, Rashad M, Al-Aoh HA. [Methyl](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0215) orange adsorption comparison on
nanoparticles: isotherm, kinetics, and [thermodynamic](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0215) studies. Dyes Pigm 2019;
[160:563–71.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0215)

[44] Delgado N, Capparelli A, Navarro A, Marino D. Pharmaceutical emerging
[pollutants removal from water using powdered activated carbon: study of kinetics](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0220)
and adsorption equilibrium. J [Environ](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0220) Manage 2019;236:301–8.

[45] El-Khaiary MI, Malash GF, Ho Y-S. On [the](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0225) use of linearized pseudo-second-order
kinetic equations for modeling [adsorption](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0225) systems. Desalination 2010;257:
[93–101.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0225)

[46] [Gamoudi S, Srasra E. Adsorption of organic dyes by HDPy+-modified clay: effect](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0230)
of molecular structure on the [adsorption.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0230) J Mol Struct 2019;1193:522–31.

[47] [Khan SU, Islam DT, Farooqi IH, Ayub S, Basheer F. Hexavalent chromium removal](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0235)
in an electrocoagulation column [reactor:](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0235) process optimization using CCD,
[adsorption kinetics and pH modulated sludge formation. Process Saf Environ Prot](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0235)
[2019;122:118–30.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0235)

[48] Kumar KV, Sivanesan S. Pseudo second order kinetics and pseudo isotherms for
malachite green onto activated [carbon:](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0240) comparison of linear and non-linear
regression methods. J [Hazard](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0240) Mater 2006;136:721–6.

[49] Shang Y, Cui Y, Shi R, Yang P, [Wang](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0245) J, Wang Y. Regenerated WO(2.72)
nanowires with superb fast and [selective](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0245) adsorption for cationic dye: kinetics,
isotherm, thermodynamics, [mechanism.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0245) J Hazard Mater 2019;379:120834.

[50] [Azizian S. Kinetic models of sorption: a theoretical analysis. J Colloid Interface Sci](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0250)
[2004;276:47–52.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0250)

[51] Guo X, Liu Y, Wang J. Sorption of [sulfamethazine](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0255) onto different types of
microplastics: a combined [experimental](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0255) and molecular dynamics simulation
study. Mar Pollut [Bull](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0255) 2019;145:547–54.

[52] Wang J, Guo X. Adsorption kinetic [models:](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0260) physical meanings, applications, and
solving methods. J [Hazard](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0260) Mater 2020;390:122156.

[53] Marczewski AW. Analysis of kinetic [langmuir](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0265) model. part I: integrated kinetic
[langmuir equation (IKL): a new complete analytical solution of the langmuir rate](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0265)
equation. [Langmuir](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0265) 2010;26:15229–38.

[54] [Siriwardane RV, Shen MS, Fisher EP. Adsorption of CO2 on molecular sieves and](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0270)
activated carbon. [Energy](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0270) Fuel 2001;15:279–84.

[55] Qiu H, Lv L, Pan BC, Zhang QJ, [Zhang](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0275) WM, Zhang QX. Critical review in
adsorption kinetic models. J [Zhejiang](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0275) University-sci A 2009;10:716–24.

[56] McCann N, Phan D, Wang X, Conway [W,](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0280) Burns R, Attalla M, et al. Kinetics and
mechanism of carbamate formation [from](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0280) CO2(aq), carbonate species, and
monoethanolamine in aqueous [solution.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0280) Chem A Eur J 2009;113:5022–9.

[57] Chen S, Shi WK, Yong JY, Zhuang Y, [Lin](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0285) QY, Gao N, et al. Numerical study on a
[structured packed adsorption bed for indoor direct air capture. Energy 2023;282:](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0285)
[128801.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0285)

[58] Foo KY, Hameed BH. Insights into the [modeling](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0290) of adsorption isotherm systems.
Chem Eng J [2010;156:2–10.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0290)

[59] Clausius R. Ueber die bewegende kraft [der](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0295) warme¨ und die gesetze, welche sich
[daraus für die w¨armelehre selbst ableiten lassen. Annalen der Physik und Chemie](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0295)
[1850;155:500–24.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0295)

[60] [Kim JJ, Lim SJ, Ahn H, Lee CH. Adsorption equilibria and kinetics of propane and](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0300)
propylene on zeolite 13X pellets. [Microporous](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0300) Mesoporous Mater 2019;274:
[286–98.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0300)

[61] Hu EJ, Zhu DS, Sang XY, Wang L, [Tan YK. Enhancement](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0305) of thermal conductivity
by using polymer-zeolite in solid [adsorption](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0305) heat pumps. J Heat Transfer 1997;
[119:627–9.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0305)

[62] Feng C, E J, Han W, Deng Y, Zhang [B,](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0310) Zhao X, et al. Key technology and
application analysis of zeolite [adsorption](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0310) for energy storage and heat-mass
transfer process: a review. Renew [Sustain](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0310) Energy Rev 2021;144:110954.

[63] Solmus¸ I, [˙] Yamalı C, Yıldırım C, Bilen K. Transient behavior of a cylindrical
adsorbent bed during the adsorption [process.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0315) Appl Energy 2015;142:115–24.

[64] [Freni A, Bonaccorsi L, Proverbio E, Maggio G, Restuccia G. Zeolite synthesised on](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0320)
copper foam for adsorption chillers: a mathematical model. Microporous
Mesoporous [Mater](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0320) 2009;120:402–9.

[65] Guti´errez Ortiz FJ, Barragan´ [Rodríguez](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0325) M, Yang RT. Modeling of fixed-bed
columns for gas physical [adsorption.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0325) Chem Eng J 2019;378:121985.

[66] Shafeeyan MS, Wan Daud WMA, [Shamiri](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0330) A. A review of mathematical modeling
of fixed-bed columns for carbon dioxide adsorption. Chem Eng Res Des 2014;92:
[961–88.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0330)

[67] [Choi S, Drese JH, Jones CW. Adsorbent materials for carbon dioxide capture from](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0335)
large anthropogenic point [sources.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0335) ChemSusChem 2009;2:796–854.

[68] [Sodiq A, Abdullatif Y, Aissa B, Ostovar A, Nassar N, El-Naas M, et al. A review on](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0340)
progress made in direct air capture of CO2. Environ Technol Innov 2023;29:
[102991.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0340)

[69] [Hao GP, Li WC, Qian D, Lu AH. Rapid synthesis of nitrogen-doped porous carbon](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0345)
monolith for CO2 capture. Adv Mater 2010;22:853–7.

[70] Low MY, Barton LV, Pini R, Petit C. [Analytical](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0350) review of the current state of
[knowledge of adsorption materials and processes for direct air capture. Chem Eng](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0350)
Res Des [2023;189:745–67.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0350)



26


_H._ _Xu_ _et_ _al._ _Energy_ _Conversion_ _and_ _Management_ _322_ _(2024)_ _119119_




[71] Bhatta LKG, Subramanyam S, Chengala [MD,](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0355) Olivera S, Venkatesh K. Progress in
hydrotalcite like compounds and [metal-based](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0355) oxides for CO2 capture: a review.
J Clean Prod [2015;103:171–96.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0355)

[72] Rodríguez-Mosqueda R, Bramer EA, [Roestenberg](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0360) T, Brem G. Parametrical study
on CO2 capture from ambient air [using](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0360) hydrated K2CO3 supported on an
activated carbon honeycomb. [Ind](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0360) Eng Chem Res 2018;57:3628–38.

[73] Crini G, Lichtfouse E, Wilson L, [Morin-Crini](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0365) N. Green adsorbents for pollutant
removal. Environ Chem [Sustain](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0365) World 2018;18:23–71.

[74] Cho JH, Ma J, Kim SY. Toward [high-efficiency](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0370) photovoltaics-assisted
electrochemical and [photoelectrochemical](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0370) CO2 reduction: strategy and
challenge. [Exploration](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0370) 2023;3:20230001.

[75] Thommes M, Cychosz KA. Physical [adsorption](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0375) characterization of nanoporous
materials: progress and [challenges.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0375) Adsorption 2014;20:233–50.

[76] Tang T, Wang Z, Guan J. [Achievements](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0380) and challenges of copper-based singleatom catalysts for the reduction of [carbon](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0380) dioxide to C2+ products. Exploration
[2023;3:20230011.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0380)

[77] Neimark AV, Coudert FX, Boutin A, [Fuchs](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0385) AH. Stress-based model for the
breathing of metal-organic [frameworks.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0385) J Phys Chem Lett 2010;1:445–9.

[78] Kharitonov AB, Fomkin AA, Pribylov [AA,](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0390) Sinitsyn VA. Adsorption of carbon
dioxide on microporous carbon [adsorbent](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0390) PAU-10. Russ Chem Bull 2001;50:
[591–4.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0390)

[79] Miyasaka K, Hano H, Kubota Y, Lin Y, Ryoo R, Takata M, et al. A stand-alone
mesoporous crystal structure model [from](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0395) in situ X-ray diffraction: nitrogen
adsorption on 3D cagelike [mesoporous](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0395) silica SBA-16. Chemistry 2012;18:
[10300–11.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0395)

[80] [Pardakhti M, Jafari T, Tobin Z, Dutta B, Moharreri E, Shemshaki NS, et al. Trends](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0400)
in solid adsorbent materials [development](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0400) for CO(2) capture. ACS Appl Mater
Interfaces [2019;11:34533–59.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0400)

[81] Zhu T, Yang S, Choi DK, Row KH. [Adsorption](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0405) of carbon dioxide using
polyethyleneimine modified silica [gel.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0405) Korean J Chem Eng 2010;27:1910–5.

[82] Wu H. Particulate and membrane [molecular](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0410) sieves prepared to adsorb carbon
dioxide in packed and staggered [adsorber.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0410) Chem Ind Chem Eng Q 2018;24:
[345–56.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0410)

[83] Pandya T, Patel S, Kulkarni M, Singh [YR,](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0415) Khodakiya A, Bhattacharya S, et al.
Zeolite-based nanoparticles drug [delivery](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0415) systems in modern pharmaceutical
research and environmental [remediation.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0415) Heliyon 2024;10:e36417.

[84] [Zhang Y, Ding L, Xie Z, Zhang X, Sui X, Li J-R. Porous sorbents for direct capture](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0420)
of carbon dioxide from ambient [air.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0420) Chin Chem Lett 2024;109676.

[85] Zhang X, Shi G. Research progress in [modification](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0425) of solid alkali adsorbent for
carbon dioxide. Modern [Chem](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0425) Industry 2022;42:50–3.

[86] Shen X, Yan F, Xie F, Chen H, [Zhang](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0430) Z. Research progress of solid amine
[adsorbents derived from solid waste for CO2 capture. J Chin Ceram Soc 2023;51:](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0430)
[2411–22.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0430)

[87] B¨auerlein PS, Mansell JE, ter Laak TL, [de](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0435) Voogt P. Sorption behavior of charged
and neutral polar organic compounds [on](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0435) solid phase extraction materials: which
functional group governs [sorption?](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0435) Environ Sci Tech 2012;46:954–61.

[88] [Moore G, Blakemore J, Milot R, Hull J, Song H, Cai L, et al. A visible light water-](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0440)
splitting cell with a photoanode [formed](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0440) by codeposition of a high-potential
porphyrin and an iridium [water-oxidation](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0440) catalyst. Energy Environ Sci 2011;4:
[2389–92.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0440)

[89] Kumar A, Madden DG, Lusi M, Chen [KJ,](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0445) Daniels EA, Curtin T, et al. Direct air
capture of CO2 by physisorbent [materials.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0445) Angewandte Chemie-International
Edition [2015;54:14372–7.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0445)

[90] [Madden DG, Scott HS, Kumar A, Chen KJ, Zaworotko MJ. Flue-gas and direct-air](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0450)
[capture of CO2 by porous metalorganic materials. Philos Trans R Soc A Math Phys](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0450)
Eng Sci [2017;375.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0450)

[91] Luo Z, Fan S, Gu C, Liu W, Liu J. [Metal-organic](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0455) framework (MOF)-based
nanomaterials for biomedical [applications.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0455) Curr Med Chem 2018;25:3341–69.

[92] Eddaoudi M, Kim J, Rosi N, Vodak D, [Wachter](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0460) J, O’Keeffe M, et al. Systematic
[design of pore size and functionality in isoreticular MOFs and their application in](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0460)
methane storage. [Science](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0460) 2002;295:469–72.

[93] [Chai WS, Cheun JY, Kumar PS, Mubashir M, Majeed Z, Banat F, et al. A review on](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0465)
conventional and novel [materials towards](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0465) heavy metal adsorption in wastewater
treatment application. J [Clean](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0465) Prod 2021;296:126589.

[94] Tao YR, Xu HJ. A critical review on [potential](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0470) applications of metal-organic
frameworks (MOFs) in adsorptive [carbon](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0470) capture technologies. Appl Therm Eng
[2024;236:121504.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0470)

[95] Tong P, Liang J, Jiang X, Li J. [Research](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0475) progress on metal-organic framework
composites in chemical sensors. [Crit](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0475) Rev Anal Chem 2019;50:1–17.

[96] Zhan XQ, Yu XY, Tsai FC, Ma N, Liu [HL,](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0480) Han Y, et al. Magnetic MOF for AO7
removal and targeted [delivery.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0480) Crystals 2018.

[97] [Xu HJ, Hu PY. Progress on fundamentals of adsorption transport of metal-organic](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0485)
frameworks materials and sustainable applications for water harvesting and
carbon capture. J [Clean](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0485) Prod 2023;393:136253.

[98] [Nie L, Mu Y, Jin J, Chen J, Mi J. Recent developments and consideration issues in](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0490)
solid adsorbents for CO2 capture [from](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0490) flue gas. Chin J Chem Eng 2018;26:
[2303–17.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0490)

[99] Coromina HM, Walsh DA, Mokaya R. [Biomass-derived](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0495) activated carbon with
simultaneously enhanced CO2 uptake [for](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0495) both pre and post combustion capture
applications. J Mater [Chem](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0495) A 2015;4:280–9.

[100] [Lu C, Bai H, Wu B, Su F, Hwang JF. Comparative study of CO2 capture by carbon](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0500)
nanotubes, activated carbons, and [zeolites.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0500) Energy Fuel 2008;22:3050–6.

[101] Sethia G, Sayari A. Comprehensive [study](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0505) of ultra-microporous nitrogen-doped
activated carbon for CO2 [capture.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0505) Carbon 2015;93:68–80.

[102] Kim TW, Kim IY, Jung TS, Ko CH, [Hwang](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0510) S-J. A new type of efficient CO2
adsorbent with improved thermal [stability:](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0510) self-assembled nanohybrids with



[optimized microporosity and gas adsorption functions. Adv Funct Mater 2013;23:](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0510)
[4377–85.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0510)

[103] Li X, Zhang L, Yang Z, Wang P, Yan Y, Ran J. Adsorption materials for volatile
organic compounds (VOCs) and the [key](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0515) factors for VOCs adsorption process: a
review. Sep Purif [Technol](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0515) 2020;235:116213.

[104] Sun Q, Li Z, Searles DJ, Chen Y, Lu G, [Du](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0520) A. Charge-controlled switchable CO2
capture on boron nitride [nanomaterials.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0520) J Am Chem Soc 2013;135:8246–53.

[105] Li L, Liu Y, Yang X, Yu X, Fang Y, Li [Q,](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0525) et al. Ambient carbon dioxide capture
using boron-rich porous boron [nitride:](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0525) a theoretical study. ACS Appl Mater
Interfaces [2017;9:15399–407.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0525)

[106] Tan X, Tahini HA, Smith SC. [Borophene](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0530) as a promising material for charge[modulated switchable CO2 capture. ACS Appl Mater Interfaces 2017;9:19825–30.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0530)

[107] Tan X, Tahini HA, Smith SC. [Computational](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0535) design of two-dimensional
nanomaterials for charge modulated [CO2/H2](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0535) capture and/or storage. Energy
Storage [Mater](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0535) 2017;8.

[108] Ferey G. Hybrid porous solids: past, [present,](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0540) future. Chem Soc Rev 2008;37:
[191–214.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0540)

[109] [Santori G, Charalambous C, Ferrari M-C, Brandani S. Adsorption artificial tree for](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0545)
[atmospheric carbon dioxide capture, purification and compression. Energy 2018;](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0545)
[162:1158–68.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0545)

[110] Yu YF, Zheng LW, Wang JD. [Adsorption](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0550) behavior of toluene on modified 1X
molecular sieves. J Air Waste [Manag](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0550) Assoc 2012;62:1227–32.

[111] [Zhou J, Li W, Zhang Z, Wu X, Xing W, Zhuo S. Effect of cation nature of zeolite on](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0555)
[carbon replicas and their electrochemical capacitance. Electrochim Acta 2013;89:](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0555)
[763–70.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0555)

[112] Wang X, He T, Hu J, Liu M. The [progress](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0560) of nanomaterials for carbon dioxide
capture via the adsorption process. Environ Sci Nano 2021;8:890–912.

[113] Yong Z, Mata VG, Rodrigues AE. [Adsorption](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0565) of carbon dioxide on chemically
modified high surface area [carbon-based](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0565) adsorbents at high temperature.
Adsorption [2001;7:41–50.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0565)

[114] [Fedunik-Hofman L, Bayon A, Donne SW. Comparative kinetic analysis of CaCO3/](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0570)
CaO reaction system for energy [storage](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0570) and carbon capture. Appl Sci 2019;9:
[4601.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0570)

[115] Nikulshina V, Galvez´ ME, Steinfeld [A.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0575) Kinetic analysis of the carbonation
reactions for the capture of CO2 from [air](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0575) via the Ca(OH)2–CaCO3–CaO solar
thermochemical cycle. [Chem](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0575) Eng J 2007;129:75–83.

[116] Nikulshina V, Ayesa N, Galvez´ ME, Steinfeld A. Feasibility of Na-based
thermochemical cycles for the capture of CO2 from air—thermodynamic and
thermogravimetric analyses. [Chem](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0580) Eng J 2008;140:62–70.

[117] Chaffee AL, Knowles GP, Liang Z, [Zhang](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0585) J, Xiao P, Webley PA. CO2 capture by
adsorption: materials and process [development.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0585) Int J Greenhouse Gas Control
[2007;1:11–8.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0585)

[118] [Derevschikov VS, Veselovskaya JV, Kardash TY, Trubitsyn DA, Okunev AG. Direct](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0590)
[CO2 capture from ambient air using K2CO3/Y2O3 composite sorbent. Fuel 2014;](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0590)
[127:212–8.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0590)

[119] Przepiorski J, Czy´ [zewski A, Pietrzak R, Tryba B. MgO/CaO-loaded porous carbons˙](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0595)
for carbon dioxide capture. J [Therm](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0595) Anal Calorim 2013;111:357–64.

[120] Zhao C, Guo Y, Li C, Lu S. Removal [of](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0600) low concentration CO2 at ambient
temperature using several [potassium-based](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0600) sorbents. Appl Energy 2014;124:
[241–7.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0600)

[121] Didas SA, Choi S, Chaikittisilp W, [Jones](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0605) CW. Amine-oxide hybrid materials for
CO2 capture from ambient air. Acc Chem Res 2015;48:2680–7.

[122] Wu X, Liu M, Shi R, Yu X, Liu Y. [CO2](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0610) adsorption/regeneration kinetics and
[regeneration properties of amine functionalized SBA-16. J Porous Mater 2018;25:](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0610)
[1219–27.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0610)

[123] [Chaikittisilp W, Khunsupat R, Chen TT, Jones CW. Poly(allylamine)- mesoporous](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0615)
[silica composite materials for CO2 capture from simulated flue gas or ambient air.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0615)
Ind Eng Chem Res 2011;50:14203–10.

[124] Chaikittisilp W, Kim H-J, Jones CW. [Mesoporous](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0620) alumina-supported amines as
potential steam-stable adsorbents for [capturing](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0620) CO2 from simulated flue gas and
ambient air. Energy [Fuel](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0620) 2011;25:5528–37.

[125] Wang J, Huang H, Wang M, Yao L, [Qiao](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0625) W, Long D, et al. Direct capture of lowconcentration CO2 on mesoporous [carbon-supported](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0625) solid amine adsorbents at
ambient temperature. Ind [Eng](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0625) Chem Res 2015;54:5319–27.

[126] [Belmabkhout Y, Serna-Guerrero R, Sayari A. Amine-bearing mesoporous silica for](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0630)
CO2 removal from dry and humid air. Chem Eng Sci 2010;65:3695–8.

[127] [Liao PQ, Chen XW, Liu SY, Li XY, Chen XM. Putting an ultrahigh concentration of](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0635)
amine groups into a metal-organic [framework](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0635) for CO2 capture at low pressures.
Chem Sci [2016;7:6528–33.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0635)

[128] Kumar R, Bandyopadhyay M, [Pandey](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0640) M, Tsunoji N. Amine-impregnated
nanoarchitectonics of mesoporous [silica](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0640) for capturing dry and humid 400 ppm
carbon dioxide: a comparative study. [Microporous](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0640) Mesoporous Mater 2022;338:
[111956.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0640)

[129] [Krekel D, Samsun RC, Peters R, Stolten D. The separation of CO2 from ambient air](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0645)

   - a techno-economic [assessment.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0645) Appl Energy 2018;218:361–81.

[130] Zhang W, Liu H, Sun C, Drage TC, [Snape](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0650) CE. Capturing CO2 from ambient air
[using a polyethyleneimine–silica adsorbent in fluidized beds. Chem Eng Sci 2014;](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0650)
[116:306–16.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0650)

[131] Sinha A, Darunte LA, Jones CW, [Realff](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0655) MJ, Kawajiri Y. Systems design and
economic analysis of direct air [capture](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0655) of CO2 through temperature vacuum
swing adsorption using [MIL-101(Cr)-PEI-800](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0655) and mmen-Mg2(dobpdc) MOF
adsorbents. Ind Eng [Chem](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0655) Res 2017;56:750–64.

[132] Huang XY, Hadi P, Joshi R, [Alhamzani](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0660) AG, Hsiao BS. A comparative study of
mechanism and performance of anionic and cationic dialdehyde nanocelluloses
for dye adsorption and [separation.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0660) ACS Omega 2023.



27


_H._ _Xu_ _et_ _al._ _Energy_ _Conversion_ _and_ _Management_ _322_ _(2024)_ _119119_




[133] Hoseinpoori S, Pallar`es D, Johnsson F, [Thunman](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0665) H. A comparative exergy-based
[assessment of direct air capture technologies. Mitig Adapt Strat Glob Chang 2023;](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0665)
[28:39.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0665)

[134] Elfving J, Kauppinen J, Jegoroff M, Ruuskanen V, J¨arvinen L, Sainio T.
Experimental comparison of [regeneration](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0670) methods for CO2 concentration from
air using amine-based [adsorbent.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0670) Chem Eng J 2021;404:126337.

[135] Luukkonen A, Elfving J, Inkeri E. [Improving](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0675) adsorption-based direct air capture
performance through operating [parameter](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0675) optimization. Chem Eng J 2023;471.

[136] Wurzbacher JA, Repond N, Ruesch T, [Sauerbeck](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0680) S, Gebald C. Low-pressure drop
structure of particle adsorbent bed [for](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0680) improved adsorption gas separation
process. [Google](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0680) Patents 2021.

[137] Yu CH, Huang CH, Tan CS. A [review](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0685) of CO2 capture by absorption and
adsorption. Aerosol Air [Qual](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0685) Res 2012;12:745–69.

[138] Ben-Mansour R, Habib MA, Bamidele [OE,](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0690) Basha M, Qasem NAA, Peedikakkal A,
et al. Carbon capture by physical [adsorption:](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0690) materials, experimental
investigations and numerical modeling [and](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0690) simulations    - a review. Appl Energy
[2016;161:225–55.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0690)

[139] Graves C, Ebbesen SD, Mogensen M, [Lackner](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0695) KS. Sustainable hydrocarbon fuels
by recycling CO2 and H2O with [renewable](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0695) or nuclear energy. Renew Sustain
Energy Rev [2011;15:1–23.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0695)

[140] [Keith DW, Ha-Duong M, Stolaroff JK. Climate strategy with CO2 capture from the](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0700)
air. Clim [Change](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0700) 2006;74:17–45.

[141] Holmes G, Keith DW. An air-iquid [contactor](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0705) for large-scale capture of CO2 from
air. Phil Trans R Soc [A](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0705) 2012;370:4380–403.

[142] Stolaroff JK, Keith DW, Lowry GV. [Carbon](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0710) dioxide capture from atmospheric air
using sodium hydroxide spray. [Environ](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0710) Sci Tech 2008;42:2728–35.

[143] Wu X, Krishnamoorti R, Bollini P. [Technological](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0715) options for direct air capture: a
comparative process engineering [review.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0715) Annu Rev Chem Biomol Eng 2022;13:
[279–300.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0715)

[144] Zeman F. Reducing the cost of [Ca-based](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0720) direct air capture of CO2. Environ Sci
Tech [2014;48:11730–5.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0720)

[145] [Baciocchi R, Storti G, Mazzotti M. Process design and energy requirements for the](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0725)
capture of carbon dioxide from air. [Chem](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0725) Eng Process 2006;45:1047–58.

[146] [Zhu X, Xie W, Wu J, Miao Y, Xiang C, Chen C, et al. Recent advances in direct air](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0730)
capture by adsorption. [Chem](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0730) Soc Rev 2022;51:6574–651.

[147] [Elfving J, Bajamundi C, Kauppinen J, Sainio T. Modelling of equilibrium working](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0735)
capacity of PSA, TSA and TVSA [processes](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0735) for CO 2 adsorption under direct air
capture conditions. J [CO2](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0735) Util 2017;22:270–7.

[148] Lively RP, Realff MJ. On [thermodynamic](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0740) separation efficiency: adsorption
processes. AIChE J 2016;62:3699–705.

[149] [Liu W, Ji Y, Wang RQ, Zhang XJ, Jiang L. Analysis on temperature vacuum swing](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0745)
adsorption integrated with heat pump [for](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0745) efficient carbon capture. Appl Energy
[2023;335:120757.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0745)

[150] Yan H, Fu Q, Zhou Y, Li D, Zhang D. [CO2](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0750) capture from dry flue gas by pressure
vacuum swing adsorption: a [systematic](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0750) simulation and optimization. Int J
Greenhouse Gas [Control](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0750) 2016;51:1–10.

[151] Stuckert AN, Yang RT. CO2 capture [from](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0755) the atmosphere and simultaneous
concentration using zeolites and [amine-grafted](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0755) SBA-15. Environ Sci Tech 2011;
[45:10257–64.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0755)

[152] [Elfving J, Bajamundi C, Kauppinen J. Characterization and performance of direct](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0760)
air capture sorbent. Energy [Procedia](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0760) 2017;114:6087–101.

[153] Wurzbacher JA, Gebald C, [Steinfeld](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0765) A. Separation of CO2 from air by
temperature-vacuum swing adsorption using diamine-functionalized silica gel.
Energ Environ [Sci](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0765) 2011;4:3584–92.

[154] [Webley PA. Adsorption technology for CO2 separation and capture: a perspective.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0770)
Adsorption [2014;20:225–31.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0770)

[155] Chou CT, Chen CY. Carbon dioxide [recovery](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0775) by vacuum swing adsorption. Sep
Purif Technol [2004;39:51–65.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0775)

[156] Hedin N, Andersson L, Bergstrom¨ L, [Yan](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0780) J. Adsorbents for the post-combustion
[capture of CO2 using rapid temperature swing or vacuum swing adsorption. Appl](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0780)
Energy [2013;104:418–33.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0780)

[157] Jiang Y, Ling J, Xiao P, He Y, Zhao [Q,](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0785) Chu Z, et al. Simultaneous biogas
purification and CO2 capture by [vacuum](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0785) swing adsorption using zeolite NaUSY.
Chem Eng J [2018;334:2593–602.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0785)

[158] [Jiang N, Shen Y, Liu B, Zhang D, Tang Z, Li G, et al. CO2 capture from dry flue gas](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0790)
by means of VPSA, TSA and [TVSA.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0790) J CO2 Util 2020;35:153–68.

[159] Zhu X, Ge T, Yang F, Wang R. Design [of](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0795) steam-assisted temperature vacuumswing adsorption processes for [efficient](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0795) CO2 capture from ambient air. Renew
Sustain [Energy](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0795) Rev 2021;137.

[160] Nezam I, Zhou W, Gusmao˜ GS, Realff [MJ,](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0800) Wang Y, Medford AJ, et al. Direct
aromatization of CO2 via combined [CO2](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0800) hydrogenation and zeolite-based acid
catalysis. J CO2 [Util](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0800) 2021;45:101405.

[161] Jiang L, Roskilly AP, Wang RZ. [Performance](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0805) exploration of temperature swing
adsorption technology for carbon [dioxide](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0805) capture. Energ Conver Manage 2018;
[165:396–404.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0805)

[162] [Jiang L, Liu W, Wang RQ, Gonzalez-Diaz A, Rojas-Michaga MF, Michailos S, et al.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0810)
Sorption direct air capture with CO2 [utilization.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0810) Prog Energy Combust Sci 2023;
[95:101069.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0810)

[163] Zhang X, Zhao H, Yang Q, Yao M, Wu [Y-N,](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0815) Gu Y. Direct air capture of CO2 in
designed metal-organic frameworks at [lab](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0815) and pilot scale. Carbon Capture Sci &
Technol [2023;9:100145.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0815)

[164] Lackner KS. Capture of carbon dioxide [from](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0820) ambient air. Eur Phys J Special Top
[2009;176:93–106.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0820)

[165] [Xie RY, Chen S, Yong JY, Zhang XJ, Jiang L. Moisture swing adsorption for direct](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0825)
air capture: establishment of [thermodynamic](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0825) cycle. Chem Eng Sci 2024;287:
[119809.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0825)




[166] Yang H, Singh M, Schaefer J. [Humidity-swing](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0830) mechanism for CO2 capture from
ambient air. Chem [Commun](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0830) (Camb) 2018;54:4915–8.

[167] Shi X, Xiao H, Liao X, Armstrong M, [Chen](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0835) X, Lackner KS. Humidity effect on ion
behaviors of moisture-driven CO2 [sorbents.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0835) J Chem Phys 2018;149:164708.

[168] Dong H, Wang T, Wang X, Liu F, Hou C, Wang Z, et al. Humidity sensitivity
reducing of moisture swing adsorbents by hydrophobic carrier doping for CO2
direct air capture. Chem Eng J 2023;466:143343.

[169] Li F, Zhang Y, Zheng S, Wang K, Ni [J,](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0845) Zhu L, et al. CO2 removal in humid
environment by ion-exchange [membranes.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0845) Asia Pac J Chem Eng 2022;17.

[170] Shi X, Xiao H, Kanamori K, Yonezu A, [Lackner](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0850) KS, Chen X. Moisture-driven CO2
sorbents. Joule [2020;4:1823–37.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0850)

[171] Wang T, Ge K, Wu Y, Chen K, Fang [M,](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0855) Luo Z. Designing moisture-swing CO2
[sorbents through anion screening of polymeric ionic liquids. Energy Fuel 2017;31:](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0855)
[11127–33.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0855)

[172] Wang T, Wang X, Dong H, Ge K, [Lackner](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0860) K. Moisture swing frequency response
method for characterization of [ion-transport](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0860) kinetics of CO2 adsorption. Int J
Heat Mass Transf 2023;216:124551.

[173] [Kaneko Y, Lackner KS. Kinetic model for moisture-controlled CO2 sorption. PCCP](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0865)
[2022;24:21061–77.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0865)

[174] Wang T, Liu J, Lackner KS, Shi X, [Fang](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0870) M, Luo Z. Characterization of kinetic
limitations to atmospheric CO2 capture by solid sorbent. Greenhouse Gases Sci
Technol [2015;6:138–49.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0870)

[175] Farmahini AH, Krishnamurthy S, [Friedrich](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0875) D, Brandani S, Sarkisov L.
Performance-based screening of porous [materials](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0875) for carbon capture. Chem Rev
[2021;121:10666–741.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0875)

[176] You B, Perrin P, Freyer G, Ruffion A, [Tranchand](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0880) B, H´enin E, et al. Advantages of
prostate-specific antigen (PSA) [clearance](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0880) model over simple PSA half-life
computation to describe PSA [decrease](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0880) after prostate adenomectomy. Clin
Biochem [2008;41:785–95.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0880)

[177] [Balasubramaniam BM, Thierry P-T, Lethier S, Pugnet V, Llewellyn P, Rajendran A.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0885)
Process-performance of solid sorbents for direct air capture (DAC) of CO2 in
optimized temperature-vacuum swing [adsorption](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0885) (TVSA) cycles. Chem Eng J
[2024;485:149568.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0885)

[178] Dehdari L, Yang J, Xiao P, Li GK, [Webley](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0890) PA, Singh R. Separation of hydrogen
from 10 % hydrogen + methane [mixtures](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0890) using double-stage vacuum swing
adsorption (VSA). Chem Eng J 2024;489:151032.

[179] [Liu W, Wu JK, Yu M, Zhang XJ, Wang T, Fang MX, et al. Thermodynamic analysis](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0895)
of adsorption carbon capture from [limiting](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0895) cycle to heat pump assisted cycle.
Energy [2024;291:130299.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0895)

[180] Sabatino F, Grimm A, Gallucci F, van [Sint](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0900) Annaland M, Kramer GJ, Gazzani M.
A comparative energy and costs [assessment](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0900) and optimization for direct air
capture technologies. [Joule](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0900) 2021;5:2047–76.

[181] [Zhao R, Liu L, Zhao L, Deng S, Li S, Zhang Y, et al. Thermodynamic exploration of](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0905)
temperature vacuum swing [adsorption for](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0905) direct air capture of carbon dioxide in
buildings. Energ Conver [Manage](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0905) 2019;183:418–26.

[182] [Gao J, Hoshino Y, Inoue G. Honeycomb-carbon-fiber-supported amine-containing](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0910)
nanogel particles for CO2 capture [using](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0910) a rotating column TVSA. Chem Eng J
[2020;383:123123.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0910)

[183] Jiang L, Wang RQ, Gonzalez-Diaz A, [Smallbone](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0915) A, Lamidi RO, Roskilly AP.
Comparative analysis on temperature [swing](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0915) adsorption cycle for carbon capture
by using internal heat/mass [recovery.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0915) Appl Therm Eng 2020;169.

[184] Gebald C, Wurzbacher JA, [Tingaut](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0920) P, Steinfeld A. Stability of aminefunctionalized cellulose during [temperature-vacuum-swing](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0920) cycling for CO2
capture from air. Environ [Sci](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0920) Technol 2013;47:10063–70.

[185] Wurzbacher JA, Gebald C, Brunner S, Steinfeld A. Heat and mass transfer of
temperature–vacuum swing desorption for CO2 capture from air. Chem Eng J
[2016;283:1329–38.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0925)

[186] Agarwal S, Rani A. Adsorption of [resorcinol](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0930) from aqueous solution onto CTAB/
NaOH/flyash composites: equilibrium, [kinetics](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0930) and thermodynamics. J Environ
Chem Eng [2017;5:526–38.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0930)

[187] Gutknecht V, Snæbjornsd¨ ottir S´ [O, Sigfússon B, Arad](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0935) [´] ottir ES, Charles L. Creating a´
carbon dioxide removal solution by [combining](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0935) rapid mineralization of CO2 with
direct air capture. Energy [Procedia](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0935) 2018;146:129–34.

[188] [Elfving J, Sainio T. Kinetic approach to modelling CO2 adsorption from humid air](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0940)
using amine-functionalized resin: [equilibrium](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0940) isotherms and column dynamics.
Chem Eng Sci [2021;246:116885.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0940)

[189] Vazquez´ FV, Koponen J, Ruuskanen V, [Bajamundi](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0945) C, Kosonen A, Simell P, et al.
Power-to-X technology using [renewable](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0945) electricity and carbon dioxide from
ambient air: SOLETAIR [proof-of-concept](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0945) and improved process concept. J CO2
Util [2018;28:235–46.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0945)

[190] [Ruuskanen V, Givirovskiy G, Elfving J, Kokkonen P, Karvinen A, J¨arvinen L, et al.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0950)
Neo-carbon food concept: a pilot-scale [hybrid](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0950) biological–inorganic system with
direct air capture of carbon [dioxide.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0950) J Clean Prod 2021;278.

[191] Schellevis HM, van Schagen TN, [Brilman](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0955) DWF. Process optimization of a fixed
[bed reactor system for direct air capture. Int J Greenhouse Gas Control 2021;110:](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0955)
[103431.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0955)

[192] Bajamundi CJE, Koponen J, [Ruuskanen](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0960) V, Elfving J, Kosonen A, Kauppinen J,
et al. Capturing CO2 from air: [Technical](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0960) performance and process control
improvement. J [CO2](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0960) Util 2019;30:232–9.

[193] Jiang L, Gonzalez-Diaz A, Ling-Chin J, [Malik](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0965) A, Roskilly AP, Smallbone AJ. PEF
plastic synthesized from industrial carbon dioxide and biowaste. Nat
Sustainability 2020;3:761–7.

[194] Ozkan M, Nayak SP, Ruiz AD, Jiang [W.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0970) Current status and pillars of direct air
capture technologies. [iScience](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0970) 2022;25:103990.



28


_H._ _Xu_ _et_ _al._ _Energy_ _Conversion_ _and_ _Management_ _322_ _(2024)_ _119119_




[195] Veselovskaya JV, Parunin PD, [Okunev](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0975) AG. Catalytic process for methane
production from atmospheric carbon [dioxide](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0975) utilizing renewable energy. Catal
Today [2017;298:117–23.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0975)

[196] Myers TG, Font F, Hennessy MG. [Mathematical](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0980) modelling of carbon capture in a
packed column by adsorption. Appl Energy 2020;278:115565.

[197] Zanco SE, Ambrosetti M, Groppi G, [Tronconi](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0985) E, Mazzotti M. Heat transfer
intensification with packed open-cell [foams](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0985) in TSA processes for CO2 capture.
Chem Eng J [2022;430:131000.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0985)

[198] Schony¨ G, Dietrich F, Fuchs J, Proll¨ T, [Hofbauer](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0990) H. A multi-stage fluidized bed
system for continuous CO2 capture by [means](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0990) of temperature swing adsorption    first results from bench scale [experiments.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0990) Powder Technol 2017;316:519–27.

[199] Chen X, Wang J, Ren T, Li Z, Du T, Lu X, et al. Novel exchanger type vacuum
temperature swing adsorption for [post-combustion](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0995) CO2 capture: Process design
and plant demonstration. Sep [Purif](http://refhub.elsevier.com/S0196-8904(24)01060-4/h0995) Technol 2023;308:122837.

[200] Masuda S, Osaka Y, Tsujiguchi T, [Kodama](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1000) A. Carbon dioxide recovery from a
simulated dry exhaust gas by [an internally](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1000) heated and cooled temperature swing
[adsorption packed with a typical hydrophobic adsorbent. Sep Purif Technol 2022;](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1000)
[284:120249.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1000)

[201] Chen L, Deng S, Zhao R, Zhu Y, Zhao [L,](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1005) Li S. Temperature swing adsorption for
CO2 capture: Thermal design and [management](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1005) on adsorption bed with singletube/three-tube internal heat [exchanger.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1005) Appl Therm Eng 2021;199:117538.

[202] Okumura T, Yoshizawa K, Nishibe S, [Iwasaki](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1010) H, Kazari M, Hori T. Parametric
testing of a pilot-scale design for a [moving-bed](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1010) CO2 capture system using lowtemperature steam. Energy Procedia 2017;114:2322–9.

[203] Park YC, Jo S-H, Ryu CK, Yi C-K. [Long-term](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1015) operation of carbon dioxide capture
system from a real coal-fired flue gas [using](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1015) dry regenerable potassium-based
sorbents. Energy [Procedia](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1015) 2009;1:1235–9.

[204] Veneman R, Li ZS, Hogendoorn JA, [Kersten](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1020) SRA, Brilman DWF. Continuous CO2
[capture in a circulating fluidized bed using supported amine sorbents. Chem Eng J](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1020)
[2012;207–208:18–26.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1020)

[205] Grande CA, Kvamsdal H, Mondino G, Blom R. Development of moving bed
temperature swing adsorption [(MBTSA)](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1025) process for post-combustion CO2
capture: initial benchmarking in a [NGCC](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1025) context. Energy Procedia 2017;114:
[2203–10.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1025)

[206] Keith DW, Holmes G, St D, Angelo [KH.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1030) A process for capturing CO2 from the
atmosphere. [Joule](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1030) 2018;2:1573–94.

[207] Elliott S, Lackner KS, Ziock HJ, [Dubey](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1035) MK, Hanson HP, Barr S, et al.
[Compensation of atmospheric CO2buildup through engineered chemical sinkage.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1035)
Geophys Res [Lett](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1035) 2001;28:1235–8.




[208] Kim H, Byun M, Lee B, Lim H. [Carbon-neutral](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1040) methanol synthesis as carbon
dioxide utilization at different scales: [economic](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1040) and environmental perspectives.
Energ Conver [Manage](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1040) 2022;252:115119.

[209] Lebling. The Commercial Case for Direct Air Capture of Carbon Dioxide. in: URL,
(Ed.). https://bipartisanpolicy.org/report/the-commercial-case-for-dac, 2021.

[210] N. Merchant. 8 Unique direct air capture companies to watch in 2022. The carbon
curve, https://carboncurve.substack.com/p/8-unique-direct-air-capturecompanies., 2022.

[211] Vujovi´c T, Petkovi´c Z, Pavlovi´c M, [Jovi´c](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1055) S. Economic growth based in carbon
dioxide emission [intensity.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1055) Phys A 2018;506:179–85.

[212] Barahimi V, Ho M, Croiset E. From lab to fab: development and deployment of
direct air capture of [CO2.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1060) Energies 2023:6385.

[213] Leonzio G, Fennell PS, Shah NL. A [comparative study](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1065) of different sorbents in the
[context of direct air capture (DAC): evaluation of key performance indicators and](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1065)
comparisons. Appl Sci-Basel 2022;12.

[214] Deutz S, Bardow A. Life-cycle [assessment](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1070) of an industrial direct air capture
process based on temperature-vacuum swing adsorption. Nat Energy 2021;6:
[203–13.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1070)

[215] Zharmenov AA, Berdikulova FA, [Khamidulla](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1075) AG, Hein J. Critical factors for
selecting a carbon dioxide capture [system](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1075) in the industry. Metallurgist 2023;67:
[1235–44.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1075)

[216] Chen J. Dynamic relationship [between](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1080) urban carbon dioxide emissions and
economic growth. [Global](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1080) NEST J 2020;22:632–41.

[217] Armstrong M, Shi XY, Shan BH, [Lackner](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1085) K, Mu B. Rapid CO2 capture from
ambient air by sorbent-containing [porous](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1085) electrospun fibers made with the
solvothermal polymer additive [removal](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1085) technique. AIChE J 2019;65:214–20.

[218] Voskian S, Hatton TA. Faradaic [electro-swing](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1090) reactive adsorption for CO2
capture. Energ [Environ](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1090) Sci 2019;12:3530–47.

[219] [Findley JM, Sholl DS. Computational screening of MOFs and zeolites for direct air](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1095)
capture of carbon dioxide under [humid](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1095) conditions. J Phys Chem C 2021;125:
[24630–9.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1095)

[220] TerraFixing—Technology. https://www.terrafixing.com/technology.

[221] Darunte LA, Sen T, Bhawanani C, [Walton](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1105) KS, Sholl DS, Realff MJ, et al. Moving
beyond adsorption capacity in [design](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1105) of adsorbents for CO2 capture from
[ultradilute feeds: kinetics of CO2 adsorption in materials with stepped isotherms.](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1105)
Ind Eng Chem [Res](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1105) 2019;58:366–77.

[222] Qiu Y, Lamers P, Daioglou V, [McQueen](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1110) N, de Boer H-S, Harmsen M, et al.
Environmental trade-offs of direct air [capture](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1110) technologies in climate change
mitigation toward 2100. [Nat](http://refhub.elsevier.com/S0196-8904(24)01060-4/h1110) Commun 2022;13:3635.



29



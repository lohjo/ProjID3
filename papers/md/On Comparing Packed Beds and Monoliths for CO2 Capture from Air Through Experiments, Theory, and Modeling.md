This article is licensed under [CC-BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)


pubs.acs.org/IECR Article

## **On Comparing Packed Beds and Monoliths for CO2 Capture from Air** **Through Experiments, Theory, and Modeling**
#### Valentina Stampi-Bombelli, Alba Storione, Quirin Grossmann, and Marco Mazzotti*

### ACCESS Metrics & More Article Recommendations * sı Supporting Information





**1.** **INTRODUCTION**

Humankind is on a path to likely overdraw the carbon budget
associated with the 2 °C target established by the Paris
Agreement in 2015. [1] In addition to exploiting conventional
mitigation and adaptation options (i.e., measures to reduce
emissions of greenhouse gases and to cope with the changing
climate, respectively), humankind will have to deploy
technologies to counteract climate change. In particular,
negative emission technologies (NETs) can rewind the carbon
budget by permanently removing CO2 from the atmosphere.
NETs will also be needed to compensate for unavoidable
emissions (aviation, chemicals, agriculture) in a net-zero−
CO2−emissions world, where average temperatures are
stabilized. Direct capture of CO2 from ambient air [ _direct_ _air_
_capture_, (DAC)] coupled with permanent CO2 storage is a key
component of NETs. [2] DAC can be realized through different
approaches, two of which are rather established (other methods,
for instance, based on electrochemistry are at an earlier stage of
development): absorption in alkaline aqueous solutions or
adsorption on suitable solid sorbents. Between the two methods,
the latter offers distinct advantages, including the potential for
lower energy consumption, modularity, and reduced environmental impact associated with solvent use and disposal. [3][−][5]


© 2024 The Authors. Published by
American Chemical Society



**11637**



Extensive scientific research has emphasized the importance
of the development and optimization of sorbent materials for
adsorption-based DAC. [6] The quest for suitable sorbents has
driven investigations into materials with high CO2 selectivity
over N2 and O2, high CO2 capacity at the relevant low
concentrations, long lifetime, and stable and favorable
adsorption properties in the presence of water, given the
inevitable humidity of the air. The literature showcases the
significant progress made in sorbent development, including the
exploration of amine-functionalized materials on multiple
supports such as oxides [7][−][12] and metal−organic frameworks. [13][,][14]

Other than having high uptake capacity at low concentrations of
CO2, such amine-functionalized materials exhibit two advantages, namely the enhanced CO2 adsorption capacity in the


[https://doi.org/10.1021/acs.iecr.4c01392](https://doi.org/10.1021/acs.iecr.4c01392?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
_Ind. Eng. Chem. Res._ 2024, 63, 11637−11653


**Industrial & Engineering Chemistry Research** **pubs.acs.org/IECR** Article



presence of water [15] and the low temperature requirements for
sorbent regeneration. [5]

While sorbent development has been one of the primary
research focuses, other important requirements of DAC systems
have also been recognized. Once such challenge is posed by the
dilute concentration of CO2 in the air, which necessitates the
processing of large volumes of air to capture a meaningful
amount of CO2. To provide perspective, capturing 1 kg of CO2
requires processing approximately 1400 m [3] of air under standard
laboratory conditions. Consequently, capturing CO2 from air in
a practical manner requires handling large volumetric flows and,
as a result, high velocities. To decrease the electrical energy
consumption of the fan blowing large volumes of air through the
contactor, novel contactor configurations with low pressure
drops are being analyzed for sorbent-based DAC applications.
Among these contactors, monolith structures have gained
attention due to their wide use as low pressure drop catalyst
supports, particularly in the automotive industry. These
structures offer high porosity and have been shown in pointsource capture studies to enhance mass transfer kinetics. [16][−][18]

Additionally, efforts have been made to increase porosities in
packed bed geometries, resulting in thin packed bed
configurations that reduce pressure drops. [19][,][20] Both approaches
have been considered both in industrial development, as
evidenced by patent applications, [19][,][21][,][22] and in the academic
literature related to DAC. [4][,][15][,][23][−][31]

In DAC literature, various technical, [15][,][23][−][25] techno-economic, [4][,][26][−][30] and life cycle assessment studies [31] have been
performed both on sorbents in pellet form arranged in various
packed bed configurations [15][,][24][,][25][,][28][−][30] and on sorbents in
monolith form. [23][,][26][−][29] Within the DAC modeling works, CO2
equilibrium data have played a pivotal role in informing cycle,
energy, and cost calculations. Notably, of the aforementioned
studies, only two acquired mass transfer kinetic data from
breakthrough experiments, [15][,][24] while others either resorted to
correlations [26] or relied on assumptions, supplementing their
analyses with sensitivity studies on the effect of changing mass
transfer coefficients. [4][,][25] The results of sensitivity analyses
underscored the significant impact of mass transfer coefficients
on DAC performance, to the point that an inaccurate estimation
of the mass transfer coefficient could severely affect the
conclusions and result in major differences in specific energy
requirement and productivity. [4] These findings were reinforced
by a comprehensive study, [32] which identified the overall mass
transfer coefficient as one of the most influential parameters
affecting specific energy consumption, productivity, and purity
among 15 key parameters analyzed within a DAC adsorption
cycle. These observations highlighted the critical importance of
accurately modeling mass transfer kinetics within the DAC
framework but also highlighted the lack of characterized kinetic
data in DAC literature. Despite the availability of experimental
kinetic data in DAC concentrations for both pellets [13][,][33][,][34] and
monoliths, [35][−][38] only two studies have undertaken the task of
quantifying this data with kinetic models, [34][,][38] while most of the
papers put a greater emphasis on sorbent synthesis rather than
on characterizing kinetics. Indeed, while notable observations
regarding irregular breakthrough profiles [35] and slow kinetics [7][,][13][,][33] have been made, the observed mass transfer
dynamics have lacked the quantitative characterization necessary for accurate adsorption modeling, thus hindering the
development of strategies to address the observed kinetic
limitations.



Therefore, we acknowledge the disparity between the
necessity for detailed kinetic data at DAC concentrations, on
which to base process calculations, and its availability in the
current literature. With this work, we aim to bridge this gap by
presenting experiments performed at DAC concentrations and
analyzing them both qualitatively and quantitatively. Given the
significance of both the packed bed and monolith geometries in
DAC applications, we investigated both types of contactors.
Breakthrough experiments were performed under conditions
allowing for the full development of the mass transfer zone, thus
enabling an accurate characterization of the adsorption kinetics
using a 1D model. To achieve this, the following steps were
undertaken.

    - breakthrough experiments were conducted to study the
adsorption kinetics under dry conditions on a packed bed
of amine-functionalized _γ_ -alumina pellets and on an
amine-functionalized _γ_ -alumina wash-coated monolith, at
different feed velocities and concentrations;

    - with a simple methodology derived from a constant
pattern analysis, the fundamental mechanisms controlling
adsorption were qualitatively evaluated by examining the
effects of varying operating conditions on the breakthrough profiles;

    - a one-dimensional physical model, considering both a
conventional pseudo-first-order (PFO) kinetic model and
a dual kinetic (DK) model to describe mass transfer on
amine sorbents, was utilized to fit dispersion data, to
validate literature mass transfer correlations, and to
confirm the findings from the constant pattern solution;

    - last, the adsorption performance of the contactors was
compared, contextualizing their characterization within
DAC-relevant circumstances.


**2.** **METHODOLOGY**
In this section, we describe the materials used in this study, along
with the experimental setup and experimental campaign
performed. Subsequently, we introduce the adsorption model
utilized for quantitatively estimating transport parameters from
the breakthrough experiments while comparing two models to
describe adsorption kinetics. We then outline a methodology
derived from the constant pattern solution, used for the
identification of limiting adsorption mechanisms from breakthrough curves. Finally, we define the key performance
indicators that allow a comparison of the two contactors studied
in the range of experimental conditions considered in this work.
**2.1.** **Materials.** In this study, we examined two distinct
sorbent geometries. Specifically, we have investigated meso
alumina wash-coat applied by HUG Engineering resulted in the
creation of mesoporous pockets of _γ_ -alumina throughout the
macropores of the mullite support, as illustrated in Figure 1. The
_γ_ -alumina of both contactors was functionalized with triamine
via a water-aided amine grafting protocol that has been
described elsewhere. [36] Pure-component CO2 adsorption
isotherms of the pellets were measured at 25, 50, and 90 °C
by using a Microtrac BELSORP Max volumetric device. The
CO2 adsorption data at 25 °C is displayed [in Figure](https://pubs.acs.org/doi/suppl/10.1021/acs.iecr.4c01392/suppl_file/ie4c01392_si_001.pdf) S1, along
with that for N2, which was obtained using the same procedure


**11638** [https://doi.org/10.1021/acs.iecr.4c01392](https://doi.org/10.1021/acs.iecr.4c01392?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
_Ind. Eng. Chem. Res._ 2024, 63, 11637−11653


**Industrial & Engineering Chemistry Research** **pubs.acs.org/IECR** Article


Table 2. Properties of the Commercial Saint-Gobain _**γ**_                                Alumina Pellets and the Packed Bed Considered in This
Work


units value ref


material properties
material [-] _γ_ -alumina _a_

shape [-] rings _a_

pellet size, _d_ p [mm] 3 _a_



Figure 1. Visual representation of the _γ_ -alumina-coated mullite
monolith provided by HUG Engineering, with 12 × 12 channels and
walls with a macroporous structure given by the mullite and the
mesoporous structure given by the _γ_ -alumina pockets.


and which demonstrates no N2 adsorption. The sets of data at
the three temperatures were used to compute the isosteric heat
of adsorption of CO2 using the Clausius−Clapeyron equation,
and the following temperature-dependent Toth equation was
used to describe the adsorption isotherms of CO2 on aminefunctionalized _γ_ -alumina using eqs 1−4. The fitted parameters of
the Toth isotherm are reported in Table 1. For modeling


Table 1. Toth Isotherm Parameters Fitted to the CO2
Adsorption Data on the Amine-Functionalized _**γ**_ -Alumina
Pellets at 298 K Reported in the Work by Grossmann et al. [36]


units value


_T_ 0 [K] 298
_n_ s0 [mol kg [−][1] ] 1.23
_b_ 0 [kPa [−][1] ] 4839
_t_ 0 [-] 0.25
Δ _H_ 0 [kJ mol [−][1] ] 70
_χ_ [-] 0
_α_ [-] 0.11


purposes, the isotherm of the monolith was calculated as _q_ *mono =
0.035 _q_ *pellet, as the CO2 uptake per total monolith mass was 3.5%
of that of the pellets. Detailed properties of the mesoporous _γ_ alumina pellets and the _γ_ -alumina-coated mullite honeycomb
monolith are reported in Tables 2 and 3, respectively.



_n_ s( _T_ ) _b_ ( _T_ ) _p_
_q_ pellet( _p_ CO2, _T_ ) = (1 + ( _b_ ( _T_ ) _p_ ) _t_



_n_ s( _T_ ) _b_ ( _T_ )

( _p_ CO2, _T_ ) = (1 + ( _b_ ( _T_ ) _p_



s CO



2



pellet CO2 (1 + ( _b_ ( _T_ ) _p_ ) _t_ ( _T_ ))1/ _t_ ( _T_



2 (1 + ( _b_ ( _T_ ) _p_ CO ) _t_ ( _T_ ))1/ _t_ ( _T_ )



2 (1)



i _T_ y

_n_ s( _T_ ) = _n_ s0exp 1

jjjjj jjjjjk _T_ 0 zzzzz{zzzzz (2)



=



i



ijjjjj ijjjjj



yzzzzzyzzzzz



{



{



k



i _T_ y

1

jjjjj _T_ 0 zzzzz



k



0



{



_H_ 0 i _T_ 0 y
_b_ ( _T_ ) = _b_ 0exp 1

jjjjj _RT_ 0 jjj _T_ zzzzzzzz



yy

zzzzzzzz
{{



=



i



i _H_ 0 i

jjjjj _RT_ 0 jjj



k



(3)


(4)



pore size [nm] 13.3 _a_

pore volume [cm [3] g [−][1] ] 0.68 _a_

material density, _ρs_ [kg m [−][3] ] 3600 _b_

pellet density, _ρp_ [kg m [−][3] ] 1044 _c_

pellet porosity, _εp_ [-] 0.71 _c_

specific heat capacity [J kg [−][1] K] 784 _b_

contactor properties
length, _L_ [cm] 32.5
diameter [cm] 3.37
weight (regenerated) [g] 187
_a_ Saint-Gobain. _b_ NIST database. _c_ Determined from the pellet size,
material density, and pore volume.


Table 3. Properties of the Commercial HUG Engineering _**γ**_   Alumina-Coated Monolith Considered in This Work


units value ref


material properties
material [-] 6.9 wt.% _γ_ -alumina on mullite _a_

length, _L_ [cm] 13 _b_

width, _W_ [cm] 2.9 _b_

weight (regenerated) [g] 57.82 _b_

wall thickness, _w_ wall [mm] 0.4 _b_

channel thickness, _w_ 1 [mm] 2 _b_

mullite pore size [ _μ_ m] 15−20 _a_

_γ_ -alumina pore size [nm] 28 _b_

CPSI [-] ∼100 _a_

wall porosity, _εp_ [-] 0.48 _a_

monolith porosity, _ε_ [-] 0.68 _b_

total number of cells, _N_ [-] 144 _b_

contactor properties
length [cm] 15
width [cm] 3.2
_a_ HUG engineering. _b_ Measurement or calculation.


was equipped with two Bronkhorst mass flow controllers
(MFC), capable of operating at high or low flow rates (MFC 1:
0−250 nmL/min, MFC 2: 0−25 nL/min). The inlet pressure
and temperature were monitored by using probes placed at the
column inlet. The outlet of the column was equipped with two
flow-through CO2 sensors (open to the atmosphere), namely
Vaisala GMP343 and Vaisala GMP251, capable of measuring
CO2 concentrations in the range from 0 to 2000 ppm and from 0
to 20%, respectively.
The contactor used for the pellet experiments consisted of a
cylindrical packed bed column 3.37 cm in diameter and 32.5 cm
in length, _L_, containing 187 g of the amine-functionalized _γ_    alumina pellets. The column was equipped with heating wires
surrounding its external wall and a thermocouple positioned at
the center of the column ( _z_ = 0.5 _L_ ) to measure the temperature
of the pellets. The contactor used for the monolith experiments
consisted of a column with a square cross-section of 3.2 × 3.2
cm [2] and a length, _L_, of 15 cm, which accommodated a single
monolith. A textile felt was placed between the monolith and the


**11639** [https://doi.org/10.1021/acs.iecr.4c01392](https://doi.org/10.1021/acs.iecr.4c01392?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
_Ind. Eng. Chem. Res._ 2024, 63, 11637−11653



0



i _T_ 0 y

1

jjjk _T_ zzz{



i
= _t_ 0 +



i _T_ 0 y

1

jjjk _T_ zzz{



i _T_ 0 y

_t_ ( _T_ ) = _t_ 0 + 1

jjjk _T_ zzz{



**2.2.** **Experimental** **Setup.** The schematic of the breakthrough apparatus used in this study is shown in Figure 2. The
setup comprised a feeding system, a contactor consisting of
either a packed bed or a monolith, and a gas analysis section. To
facilitate dead volume measurements, a thin gas line of negligible
volume bypassing the column was installed. The feeding system


**Industrial & Engineering Chemistry Research** **pubs.acs.org/IECR** Article


Figure 2. Flow sheet of the experimental fixed-bed setup, made up of a feeding system, an interchangeable column that can accommodate the
cylindrical pellet packed bed and the monolith column, and a gas analysis section. Abbreviations used: MFC, mass flow controller; TI, thermocouple;
PI, pressure indicator; GMP343, Vaisala CO2 sensor in the range of 0−2000 ppm; GMP251, Vaisala CO2 sensor in the range of 0−20%.


Table 4. Momentum Balance, Mass Transfer Correlations, and Axial Dispersion Correlations Used for the One Dimensional
Adsorption Model Described in Section 2.4 _[a]_


pellets monolith


momentum balance











mass transfer correlations

film coefficient [16] _kf_ = _r_ 3 _p_ _[k]_ _f_ with _kf_ = _Ddmp_ _[Sh]_ (18)



_kf_ = _w_ 224 _w_ 1 _w_ 12 _kf_ with _kf_ = _Dwm_ 1 _[Sh]_ (19)



_Sh_ and= 2 + 1.1 _Re_ 0.6 _Sc_ 0.33 (20) and _Sh_ = 2.696ijjjj1 +



(21)



and



and _Sh_ = 2.696i1 + 0.139i _w_ 1 y y0.81

jjjj jjj _L_ zzz _[ReSc]_ zzzz
k k { {



i1 + 0.139i _w_ 1 y y

jjjj jjj _L_ zzz _[ReSc]_ zzzz
k k { {



15 _pDp_

pore coefficient [16][,][50] _kp_ = 2



15



_p_ _p_
_p_ = 2



2
_p_ (22)



_k_ 1 = _k_ 1 + _k_ 1 with _kp_,al = 15 _r_ al2 _D_ al



_p_ = _kp_,mullite + _kp_,al with _kp_,al = _r_ alal2 al



2
al (23)



_r_



and _kp_,mullite = ( _r_ 2 24 _r_ 1) _D_ 2mullite(5 _r_ 2 _r_ +1 3 _r_ 1)



=



2 _r_ 1)2(5 _r_ 2 + 3 _r_ 1) (24)



solid coefficient _ks_ = 152 _Ds_
_rc_ (25)

axial dispersion correlations [16][,][51]



_ks_ = 15 _rc_ 2 _Ds_ (26)





(28)





internal column wall at the inlet and outlet in order to keep the
monolith in place. A heating−cooling jacket surrounded the
contactor, and the monolith temperature was measured with a
thermocouple positioned at the end of the monolith ( _z_ = _L_ ). At
the inlet, the monolith column was equipped with a conical
flange and a gas distributor that allowed for the gas to distribute
evenly through the whole cross section of the monolith. A
pressure sensor was placed in the inlet conical section to
accurately measure the pressure.
**2.3.** **Experimental** **Campaign.** _2.3.1._ _Regeneration_ _Ex-_
_periments._ Prior to each breakthrough experiment, the
contactors were regenerated by heating the sorbents to 100
°C and purging them with N2 at 1 mmol s [−][1] on the packed bed



and 0.5 mmol s [−][1] on the monolith. Given that the primary focus
of the study was the analysis of the adsorption step, the N2 purge
was utilized solely for the purpose of characterizing the CO2
desorption from the column rather than to replicate the
conditions used in a full adsorption cycle. Regeneration was
set to last 3 h on the monolith (30 min ramp +2.5 h at 100 °C)
and to last 4 h on the packed bed (30 min ramp +3.5 h at 100
°C). In both cases, this time was sufficient for the CO2 outlet
concentration to reach zero. At the end of regeneration, the
contactor was cooled and closed.
_2.3.2._ _Breakthrough_ _Experiments._ Once the contactors
cooled to adsorption temperature, breakthrough experiments
were performed. The adsorption temperature was dictated by


**11640** [https://doi.org/10.1021/acs.iecr.4c01392](https://doi.org/10.1021/acs.iecr.4c01392?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
_Ind. Eng. Chem. Res._ 2024, 63, 11637−11653


**Industrial & Engineering Chemistry Research** **pubs.acs.org/IECR** Article



the lab temperature because of the absence of active cooling in
the packed bed column, thus resulting in an adsorption
temperature of 22 °C for the monolith and ∼ 24 °C for the
packed bed. Considering the rather small variation of the CO2
isotherm within this 2 °C range, we conclude that the impact of
the temperature difference on the experiments is negligible. The
breakthrough experiments were carried out until the outlet CO2
concentration reached at least 90% of the feed concentration.
For each feed velocity examined, the dead volume time,
representing the delay in the CO2 signal caused by the dead
volumes surrounding the contactor, was determined by flowing
the gas through the bypass and subtracting that time from the
breakthrough experiments. In all cases, the dead volume time
was negligible with respect to the total breakthrough duration.
**2.4. Modeling Adsorption.** _2.4.1. Model_ _Equations._ The
adsorption model used is a first principles model of a transient,
one-dimensional cylindrical column as described in previous
works. [24][,][39] For the sake of brevity, the material and energy
balances of the model used are not presented in this work, and
can be found in eqs 1−6 of the work by Casas et al. [39] The
following assumptions are made.

 - the model is one-dimensional in the axial direction, with
no radial gradient in temperature, concentration, or
velocity;

 - the fluid is an ideal gas and is described accordingly;

 - the solid and gas phases are in thermal equilibrium;

 - the heat capacities, the viscosity, the isosteric heat of
adsorption and the heat transfer coefficients are constant;

 - the momentum balance is not transient and it is assumed
that the pressure drop reaches steady state conditions
instantaneously.
The model was adapted to also describe adsorption in
monolith contactors. The monolith contactor’s square channel
was modeled as a cylindrical channel with the same cross section
to ensure the same gas velocity. Additionally, the Ergun equation
used for describing the momentum balance in the packed bed
was replaced by the Hagen-Poiseuille equation (eqs 16 and 17 in
Table 4). Axial dispersion coefficients were characterized as
polynomial functions that depend on the gas velocity according
to eqs 5 or 6 for the packed bed and the monolith, respectively

_DL_,pellets = _p u_ 1 + _p_ 2 (5)


_DL_,monolith = _p u_ 1 2 + _p_ 2 (6)


_2.4.2. Mass Transfer Models._ Adsorption on amine-functionalized sorbents often exhibits asymmetric CO2 breakthrough
profiles, characterized by a sharp breakthrough and a prolonged
tail while approaching saturation. [40][−][43] Bollini et al. hypothesized that this arises from the heterogeneous nature of the
aminopolymer layer formed during grafting, which results in
more and less accessible amine sites, each with distinct
saturation capacities and rates of mass transfer. [41][,][42] Given that
water-aided amine grafting is known to induce amine polymerization, [44][,][45] it is reasonable to assume a heterogeneous nature of
the amine adsorption sites. The long tail in the breakthrough is
thus associated with a slower rate of mass transfer within the
amine layer compared with the rate of mass transfer to the
surface amine sites. Conventional models may fail to accurately
capture the asymmetry of the breakthrough curve, which
prompted the opportunity to develop dual kinetic models
instead. [40][,][42][,][43] In this work, we investigated both the conventional pseudo-first-order (PFO) model and the dual kinetic



(DK) model proposed by Kalyanaraman et al. [43] and compare
their capability and accuracy in describing the experimental
results. These two models are summarized shortly below.

 - The pseudo-first-order model is a linear driving force
(LDF) model with the limiting mass transfer resistance in
the solid phase; _k_ is the overall mass transfer coefficient:


_q_
= _k_ ( _q_    - _q_ )
_t_ (7)


 - The dual kinetic model assumes two types of adsorption
sites, namely the easily accessible _surface_ amine sites and
the _bulk_ amine-layer sites, with adsorbed phase
concentrations _q_ 1 and _q_ 2, respectively, and: [43]

_q_ = _q_ 1 + _q_ 2 (8)


Two material balances are formulated for the surface and for
the bulk adsorption sites, each with its specific mass transfer
coefficient, _k_ 1 and _k_ 243


_q_

_t_ 1 = _k_ 1( _q_    - _q_ 1) (9)


_q_

_t_ 2 = _k_ 2((1 ) _q_    - _q_ 2) (10)


The parameter _η_ is the fraction of surface sites, hence _ηq_  - is
their equilibrium loading capacity; (1 − _η_ ) is the fraction of bulk
sites and (1 − _η_ ) _q_ - is their equilibrium loading capacity.
_2.4.3. Mass Transfer Coefficient Determination._ The overall
mass transfer coefficient for the PFO model was computed
considering three resistances in series, namely in the gas film, in
the gas pore and in the solid, with mass transfer coefficients _kf_, _kp_
and _ks_, respectively [46][−][49]



_q_    - _q_    
1 1 _p_,in 1 _p_,in

= + +
_k_ _k_ _c_ _k_ _c_



_s_



_q_



,in



1 1 _p_,in 1 _p_,in 1

= + +
_k_ _k_ _c_ _k_ _c_ _k_



_p_



,in



_q_



_p_



_f_



_c_ _k_



in



_p_



in _s_ (11)



Kalyanaraman et al. proposed that the resistance to reach the
surface amine sites in the DK model includes the resistance in
the gas film, in the gas pore and in the surface amine layer, [43]

similarly to _k_ in the PFO model. The overall resistance to reach
the bulk amine-layer sites consists of these same resistances in
series, plus the transport resistance within the bulk amine
layer. [43] Thus, we define _k_ 1 and _k_ 2 as follows



_q_    - _q_    
1 1 _p_,in 1 _p_,in

= + +
_k_ _k_ _c_ _k_ _c_



_q_



,in



,in



1 1 _p_,in 1 _p_,in 1

= + +
_k_ _k_ _c_ _k_ _c_ _k_



_p_



_q_



_p_



1 _f_ in _p_ in _s_



_f_



_c_ _k_



in



_p_



in _s_ (12)



1 1 1
= +
_k_ 2 _k_ 1 _ks_,amine (13)



When the impact of a variation in velocity on the overall mass
transfer coefficient is small, the film mass transfer coefficient and
the pore mass transfer coefficient can be combined into one
parameter, called _kg_, which accounts for the overall mass transfer
resistance in the gas phase. In this case, the overall mass transfer
coefficient can be written as



_q_     
1 1 _p_,in

= +
_k_ _k_ _c_



_q_



1 1 _p_,in 1

= +
_k_ _k_ _c_ _k_



,in



in _s_ (14)



1 g in _s_



**11641** [https://doi.org/10.1021/acs.iecr.4c01392](https://doi.org/10.1021/acs.iecr.4c01392?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
_Ind. Eng. Chem. Res._ 2024, 63, 11637−11653


**Industrial & Engineering Chemistry Research** **pubs.acs.org/IECR** Article



1 1 1
= +
_k_ g _kf_ _kp_ (15)


_2.4.4. Parameter Estimation Using Literature Correlations._
Literature correlations to estimate axial dispersion and mass
transfer coefficients ( _p_ 1, _p_ 2, _kf_, _kp_, and _ks_ ) in the packed bed and
in the monolith are summarized in Table 4. In order to account
for the bimodal structure of the monolith pores, comprising the
macropores of the mullite support and the mesopores of the _γ_ alumina pockets, the mass transfer coefficient in the gas pores,
denoted as _kp_, was modeled as determined by the resistances of
these two phases in series. The pore mass transfer coefficient in
the mullite macropores, called _kp_,mullite, was calculated using
established correlations from the literature, as in eq 24. [50] The
mass transfer coefficient in the _γ_ -alumina pockets, _kp_,al, was
defined assuming spherical _γ_ -alumina pockets of radius _r_ al and
using Glueckauf’s expression for the pore mass transfer
coefficient, [52] as in eq 23. A sensitivity analysis on all of the
realistic values of the size of the _γ_ -alumina pockets, _r_ al, showed
that the mass transfer resistance in these pockets was negligible
with respect to that in the mullite macropores, therefore
resulting in _kp_ = _kp_,mullite.
_2.4.5. Parameter Estimation from the Experiments._ In the
following, we outline the methodology employed for estimating
transport parameters from the breakthrough experiments. Given
that the active sorbent for both contactors is triamine-grafted _γ_ alumina, we tested the hypothesis that the fraction of easily
accessible surface amine sites ( _η_ ) and that the mass transfer
coefficients in the amine ( _ks_ and _ks_,amine) are constant in both
contactors and for all experiments. Therefore, in order to be
consistent with the physical picture of the adsorbent and of the
mass transfer resistances given above, we carried out the
parameter estimation exercise by.

 - Keeping _η_, _ks_, and _ks_,amine constant for all experiments;

 - Letting the axial dispersion coefficient, _DL_, vary with gas
velocity according to eqs 5 and 6, whereby the parameters
_p_ 1 and _p_ 2 are the same for experiments in the same
contactor but different between contactors;

 - Letting both _k_ 1 and _k_ 2 vary for the different contactors and
the different operating conditions according to eqs 12 and
13, while analyzing and discussing changes in _kf_ at
different velocities and keeping the mass transfer
coefficient in the pore, _kp_, constant for the experiments
in the same contactor (but different between contactors).

_2.4.5.1._ _PFO_ _Model._ Using the PFO model, estimation of _k_
and _DL_ from the breakthrough experiments was carried out by
minimizing over _θ_ 1 and _θ_ 2 the maximum likelihood estimate
(MLE), defined as



_Np_ _y_ _y_
_ij_ _ij_



y

zzzzzzzzzz

{



2



_Nv_ _Np_ _yij_ _yij_ ( 1, 2)

( 1, 2) = ln _y_ max



1 2



y

zzzzzzzz

{



_N_



i



jjjjjjjjjj

k



_v_ _p_



i



jjjjjjjj

k



_y_ _y_



=



max



1 2


_i_ =1 _j_ =1



_ij_



_i_



_i_ =1 _j_ =



_j_



(29)



_2.4.5.2. Dual Kinetic Model._ The DK model was fitted to the
breakthrough curves to estimate _k_ 1, _k_ 2, _η_, and _DL_ in each
experiment. Various combinations of these parameters were
found to effectively capture the breakthrough profiles. Based on
the contributions detailed in eq 12, _k_ 1 represents the mass
transport that is responsible for the initial part of the
breakthrough curve. Additionally, _DL_ influences only the initial
part of the slope and not the elongated tails. Consequently, to
restrict the feasible space of solutions under these physical
constraints, estimation of the four parameters was divided in two
steps. Initially, _k_ 1 and _DL_ were estimated by minimizing the MLE
in the initial part of the breakthrough curve (up to 70% of the
uptake). Then, _η_ and _k_ 2 were estimated by considering the entire
breakthrough profile through a sensitivity analysis on these
parameters. Finally, constant sets of _kf_, _kp_, _p_ 1, and _p_ 2 for each
contactor, along with constant _ks_ and _ks_,amine for both contactors,
were determined using the estimated values of _k_ 1, _k_ 2, _η_, and _DL_,
and eqs 5,6 12, and 13.
_2.4.5.3._ _Heat_ _Transfer_ _Coefficients._ The value of the
convective heat transfer coefficient from the external surface of
the contactor wall to the ambient environment, i.e., _h_ L = 26 W
m [−][2] K [−][1], was adopted from previous studies involving external
heating. [24] To determine the heat transfer coefficient between
the sorbents and the wall, denoted as _h_ W, the regenerated
contactors underwent heating to 100−105 ° _C_ with a N2 purge to
emulate regeneration conditions. The temperature profiles
within the column during the experiment are illustrated in
[Figure](https://pubs.acs.org/doi/suppl/10.1021/acs.iecr.4c01392/suppl_file/ie4c01392_si_001.pdf) S2 of the Supporting Information A sensitivity analysis
conducted on _h_ W using the presented model resulted in _h_ W
values of 10 W m [−][2] K [−][1] for the packed bed and 7 W m [−][2] K [−][1] for
the monolith. The quality of these choices is illustrated in the red
[dashed curves in Figure S2, which depict the predicted column](https://pubs.acs.org/doi/suppl/10.1021/acs.iecr.4c01392/suppl_file/ie4c01392_si_001.pdf)
temperatures based on these coefficients.
**2.5.** **Identifying** **the** **Limiting** **Mechanisms.** While
detailed adsorption modeling coupled with parameter estimation, as presented in Section 2.4, allows for the quantification of
mass transfer and of axial dispersion effects, in this section, we
introduce a simple methodology for qualitatively assessing these
mechanisms solely from experimental results, without the need
for a model.
The methodology centers around the analysis of the time
interval from breakthrough to saturation of a compound being
adsorbed, called Δ _t_, after which the column reaches its
equilibrium capacity. Such quantity, which can be viewed as
the width of the breakthrough profile, is utilized as a measurable
indicator of dispersion mechanisms, including mass transfer
resistances and axial dispersion. Mass transfer effects are
typically characterized by the Stanton number ( _St_ ), while axial
dispersion effects are characterized by the Peclet number ( _Pe_ ),
defined as _St_ = _kL_ / _u_ and _Pe_ = _uL_ / _DL_, respectively. In
equilibrium-controlled separations, mass transfer resistances
and axial dispersion effects are negligible, resulting in infinitely
large values of _St_ and _Pe_ and very sharp breakthrough profiles. In
this scenario, Δ _t_ is infinitesimally small, and the breakthrough
and saturation times coincide at the compound’s mean residence
time ( _t_ 50). In rate-controlled separations, finite values of _St_ and
_Pe_ yield greater resistance, thus broadening the mass transfer
zone and increasing the value of Δ _t_ . In such cases, column
saturation is achieved at _t_ 50 + Δ _t_ /2. Consequently, saturating the
bed comes at the expense of an extended adsorption time, and
ceasing adsorption early results in under-utilization of the bed
capacity. Both options lead to a decreased adsorption
productivity, which is defined by the specific amount adsorbed


**11642** [https://doi.org/10.1021/acs.iecr.4c01392](https://doi.org/10.1021/acs.iecr.4c01392?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
_Ind. Eng. Chem. Res._ 2024, 63, 11637−11653



where _Nv_ and _Np_ are the number of variables and the number of
observations, respectively. The observed variables were the mole
fractions at the exit of the column. The symbol _yij_ max is the

maximum value of _y_, while the hat symbol denotes the estimated
model outputs. The objective function Φ was minimized using
the Matlab “fminsearchbnd” routine. [53] Then, constant sets of _kf_,
_kp_, _p_ 1, and _p_ 2 for each contactor were fitted eqs 5,6 and 11 using
the estimated values of _k_ and _DL_ .


**Industrial & Engineering Chemistry Research** **pubs.acs.org/IECR** Article


[Figure 3. Schematic summary of a method, derived from a constant pattern analysis and described in Section S1, to determine the contribution of axial](https://pubs.acs.org/doi/suppl/10.1021/acs.iecr.4c01392/suppl_file/ie4c01392_si_001.pdf)
dispersion and the individual mass transfer resistances on the shape of a breakthrough profile through the variation of the feed velocity and of the feed
concentration for sorbent with steep isotherms.



during adsorption. Because Δ _t_ serves as a tangible measure of
kinetics and slower adsorption kinetics lead to decreased
productivity, identifying the mechanisms contributing mostly
to Δ _t_ is needed for enhancing productivity.
Illustrated in Figure 3, the methodology involves analyzing the
breakthrough experiments conducted at various gas velocities
and feed concentrations. The methodology stems from an
analysis involving an analytical constant pattern solution, which
is derived in detail in the Supporting Information and is
applicable to sorbents with steep favorable isotherms. In the first
step, the relevance of axial dispersion effects and mass transfer
resistances is assessed by varying feed velocity and examining
their effects on Δ _t_ and normalized time Δ _τ_ = _u_ Δt/ _L_, as defined
in Figure 3. In a second step, mass transfer resistances in the gas
phase (associated with mass transport in the film and in the
sorbent pores) and those in the solid phase are distinguished by
varying the feed concentration and evaluating their influence on
Δ _t_ and mass transfer zone Δ _ξ_ = Δ _t_ / _t_ 50. This analytical method
provides insights into the interplay of mass transfer and axial
dispersion, shedding light on their relative contributions to the
overall adsorption process.
**2.6.** **Key** **Performance** **Indicators.** The key performance
indicators are measured in terms of specific energy consumption
of the blower ( _W_ fan, [MJ mol [−][1] ]) and specific productivity ( _P_,

[mol kg [−][1] s [−][1] ]) of the adsorption step, as defined below



_q_
_P_ ads =



ads = ads
_t_



ads (31)











(32)



_m_



_y_ _p_    - _V_
_n_ col = in col



col = in col col
_RT_



col (33)



_r_ = _q_ ads _ms_



ads _s_
_t_



ads



_n_ d _t_



(34)



0 in



_t_



1 1 _t_ ads
_W_ fan = _V_ ( _p_ in _p_ out)d _t_
_q_ _ms_ fan 0



(30)



ads



fan in out

_q_ ads _ms_ fan 0



where _m_ s is the total sorbent mass, considering the total weight
of the pellets or the weight of the entire monolith, _η_ fan = 0.5 is the
efficiency of the blower, _V_ is the volume flow rate of gas fed to
the column, and _n_ and _p_ are the CO2 molar flow rate and
pressure, measured at the inlet and the outlet of the column.
Here, _q_ ads ([mmol g [−][1] sorbent [])] [represents] [the] [adsorbed] [phase]
concentration at time _t_ ads, which is the adsorption time to be
considered in the calculation of the productivity and blower
energy consumption. For the experiments conducted at 5.6%,
we consider the maximum breakthrough time that allows a
minimum CO2 recovery rate of _r_ = 95%, i.e., a suitable value for
CO2 capture from point-source capture. Since recovery rates do
not impose restrictions on the duration of adsorption times in
DAC, there is flexibility in deciding when to stop adsorption, and


**11643** [https://doi.org/10.1021/acs.iecr.4c01392](https://doi.org/10.1021/acs.iecr.4c01392?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
_Ind. Eng. Chem. Res._ 2024, 63, 11637−11653


**Industrial & Engineering Chemistry Research** **pubs.acs.org/IECR** Article



this point can be selected based on performance. For the
experiments conducted at 400 ppm in this work, we choose _t_ ads =
_tα_, where _α_ represents the point at which _y_ = _αy_ in, and evaluate
the impact of the choice of _t_ ads on adsorption productivity and
specific blower energy requirements.


**3.** **EXPERIMENTAL CAMPAIGN ON PACKED BEDS**
**AND MONOLITHS**
We have performed breakthrough experiments at two feed
concentrations and multiple velocities, as presented in Section
3.1 and summarized in Table 5. To ensure the complete


Table 5. Operating Conditions of the Experimental Runs:
Contactor Type, CO2 mol Fraction in the Feed ( _y_ in), Total
Gas Molar Flow Rate of the Feed ( _n_ ), and Gas Interstitial
Velocity ( _u_ )


exp _y_ in [-] _n_ [mmol s [−][1] ] _u_ [m s [−][1] ]

packed bed
400 ppm 2 0.14
5.6% 2 0.14
5.6% 1 0.07
5.6% 0.5 0.04
monolith
400 ppm 3 0.13
400 ppm 2 0.09
400 ppm 1 0.04
400 ppm 0.18 0.008
5.6% 0.18 0.008
5.6% 0.06 0.003
5.6% 0.02 0.0009


development of the breakthrough profile under all tested
experimental conditions, velocities were maintained below 0.15
m/s. These velocities are possibly low compared to industrial
DAC applications but are comparable to those encountered in
the literature reporting similar experimental studies. [34][−][37][,][54][,][55]

The specific ramifications of operating at higher velocities are
further elucidated in Section 3.5.
In Section 3.1, we analyze the shape of the breakthrough
curves and employ the methodology introduced in Section 2.5
to qualitatively identify the limiting adsorption mechanisms. In
Section 3.2, we report the fit of the 1D model on the
breakthrough experiments in terms of mass transfer and axial
dispersion coefficients and compare the results to literature
correlations.
**3.1.** **Physical** **Interpretation** **of** **the** **Breakthrough**
**Experiments.** The breakthrough profiles of all experiments
conducted are presented in Figure 4, in terms of the molar
fraction of CO2 at the column exit, _y_, and column temperature,
_T_ col. The pressure drop measured across the contactors during
each experiment is reported in [Figure](https://pubs.acs.org/doi/suppl/10.1021/acs.iecr.4c01392/suppl_file/ie4c01392_si_001.pdf) S3 of the Supporting
Information. Only one experiment at 400 ppm of CO2 in N2 was
conducted on the packed bed due to the high gas volume
requirement for the experiment. As shown in Figure 4a, this
resulted in the gas bottle being emptied and the breakthrough
reaching only 90% of the feed concentration. Four velocities
were tested at 400 ppm on the monolith, as shown in Figure 4c.
Breakthrough experiments at 5.6% were conducted at three
velocities on both the packed bed and the monolith, as
illustrated in Figure 4b,d, respectively. Long, rather evident tails
were observed in the breakthrough profiles of the monolith,
while these were almost absent in the experiments at 5.6% feed



concentration in the packed bed. The quantification and
explanation of such a phenomenon are further discussed in
Section 3.2.3. Good reproducibility of the experiments was
verified by repeating three breakthrough experiments at 1 mmol
s [−][1] on the packed bed at 5.6% and on the monolith at 400 ppm;
the corresponding results are reported in [Figure](https://pubs.acs.org/doi/suppl/10.1021/acs.iecr.4c01392/suppl_file/ie4c01392_si_001.pdf) S4 of the
Supporting Information.
_3.1.1._ _Effect_ _of_ _Feed_ _Velocity._ Decreasing the velocity
increased the spreading of the breakthrough curves and thus
increased the Δ _t_ on both contactors. In Figure 5, we present the
breakthrough data obtained at different velocities as a function
of time, _t_, and normalized time, i.e., _τ_ = _tu_ / _L_, with the time axis
shifted so that the origin of the horizontal axis is at _t_ 50 or at _τ_ 50.
For the experiments conducted on the monolith at 5.6%,
normalizing the data into _τ_ resulted in a complete overlap of the
breakthrough profiles and a constant Δ _τ_ at all velocities (Figure
5e). This correlates with case 2 of Figure 3, suggesting full
control of the axial dispersion with a constant Peclet number. A
constant Δ _τ_ was also observed at the two lower velocities of the
experiments performed on the packed bed at 5.6%, after which
Δ _τ_ increased (Figure 5d). This behavior indicated that these
experiments operated at the limit of axial dispersion control,
with both mass transfer resistances and axial dispersion
becoming significant at higher velocities, as shown in case 3 of
Figure 3. In the case of the 400 ppm monolith experiments, we
observed an increase in Δ _τ_ with increasing velocity and _u_ 1/
_ux_ <Δ _τu_ 1 [/][Δ] _[τ]_ _ux_ [<1, suggesting that both mechanisms contributed]
to Δ _t_ for all velocities (Figure 5f).
_3.1.2. Effect of Feed Concentration._ To assess the impact of
feed concentration, we compared two experiments conducted at
2 mmol s [−][1] on the packed bed and two at 0.18 mmol s [−][1] on the
monolith. Experiments at equal velocity were compared to
ensure that any effects of axial dispersion and film resistance, if
any, would equally influence both sets of experiments. Table 6
presents the CO2 capacity at 90% breakthrough ( _q_ 90), the time
to reach 90% breakthrough ( _t_ 90), and the mean residence time
( _t_ 50). Notably, the experiment at 400 ppm necessitated a mean
residence time of 31 h, while nearly complete saturation took 45
h. Indeed, Δ _t_ was so large that it made up the entire
breakthrough profile of Figure 4a, indicating exceptionally
slow adsorption kinetics. Despite high heats of adsorption, the
adsorption rate in this experiment was insufficient to generate a
noticeable temperature peak, as was evident from the temperature profile. In contrast, at 5.6%, the breakthrough curve
exhibited a considerably steeper slope, indicating significantly
faster adsorption kinetics. This observation suggests a dependency of adsorption kinetics on the feed concentration. Indeed,
although the total CO2 equilibrium capacity was similar (0.44
and 0.71 mmol g [−][1] at 400 ppm and 5.6%, respectively),
experiments at 5.6% resulted in temperature peaks exceeding 15
°C due to rapid adsorption rates. The comparison between 400
ppm and 5.6% feeds in the monolith contactor yielded
analogous results regarding differences in Δ _t_ . Here, adsorption
did not generate a significant temperature peak, due to the heat
dissipation within the inert mass of the mullite support,
representing 93.1 wt.% of the monolith, and to the active
cooling provided by the monolith jacket.
Since both axial dispersion and mass transfer resistances were
observed in the experiments at 5.6% on the packed bed and at
400 ppm in the monolith, we use the methodology presented in
Figure 3 to distinguish between mass transfer resistances in the
gas phase (associated with film and pore resistances) and in the


**11644** [https://doi.org/10.1021/acs.iecr.4c01392](https://doi.org/10.1021/acs.iecr.4c01392?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
_Ind. Eng. Chem. Res._ 2024, 63, 11637−11653


**Industrial & Engineering Chemistry Research** **pubs.acs.org/IECR** Article


Figure 4. CO2 breakthrough experiments (above) and the corresponding column temperature profiles (below) for experiments at: (a) _y_ in = 400 ppm
on the packed bed at 2 mmol s [−][1] ; (b) _y_ in = 5.6% on the packed bed at 2, 1 and 0.5 mmol s [−][1] (left to right); (c) _y_ in = 400 ppm on the monolith at 3, 2, 1
and 0.18 mmol s [−][1] (left to right); (d) _y_ in = 5.6% on the monolith at 0.18, 0.06 and 0.02 mmol s [−][1] (left to right). The thick lines in color are the
experimental measurements, while the thin black lines are the simulation results with the DK model upon fitting, using estimated parameters as
reported in Table 7. The dotted line in subfigure (c) for the rightmost experiment at 0.18 mmol s [−][1] corresponds to the DK model solution with _ks_,amine =
0.0001 s [−][1] instead of 0.0011 s [−][1] as in the simulations plotted as solid lines.



solid phase. The breakthrough curves obtained for the two feed
concentrations on the packed bed and on the monolith at the
same velocity are presented in Figure 6a,b, shifted with respect
to _t_ 50. The normalized breakthrough curves are shown
underneath in Figure 6c,d, where the dimensionless time ( _t_ _t_ 50)/ _t_ 50 is used as the axis such that the mass transfer zone
thickness is equal to Δ _ξ_ . While the difference in steepness of the
breakthrough profiles when plotted against _t_ was obvious, when
the curves at different concentrations were plotted against ( _t_ _t_ 50)/ _t_ 50, they exhibited remarkable overlap, suggesting that
Δ _ξ_ 400/Δ _ξ_ 5.6% ≈ 1. As shown in case A of Figure 3, this finding
unequivocally eliminates the possibility of solid mass transfer
resistances controlling adsorption and defining the breakthrough curve’s shape.



In summary, the qualitative results of the mass transfer zone
analysis revealed that, within the range of experimental
conditions of this study: (i) axial dispersion played an important
role in both the packed bed and the monolith experiments and
(ii) any discernible mass transfer resistance predominantly
occurred in the gas phase, with the solid resistance being
negligible. Specifically, in all packed bed experiments and the
experiment conducted at 400 ppm on the monolith, the shape of
the breakthrough curve was influenced by the _combined_ effects of
mass transfer and axial dispersion (case 3A of Figure 3).
However, at 5.6% on the monolith, only the effect of axial
dispersion was observed (case 2A of Figure 3).
**3.2.** **Modeling** **and** **Parameter** **Estimation.** _3.2.1._ _PFO_
_Model._ The estimated values of constant parameters _kg_, _ks_, _p_ 1,


**11645** [https://doi.org/10.1021/acs.iecr.4c01392](https://doi.org/10.1021/acs.iecr.4c01392?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
_Ind. Eng. Chem. Res._ 2024, 63, 11637−11653


**Industrial & Engineering Chemistry Research** **pubs.acs.org/IECR** Article


Figure 5. Effect of changing the feed velocity on the steepness of the breakthrough profiles, determined around _t_ 50 for (a−c) and around _τ_ 50 in the
dimensionless time scale for (d−f).



Table 6. Values of _q_ 90, _t_ 90, and _t_ 50 for the Experiments
Conducted at 2 mmol s [−][1] on the Packed Bed and 0.18 mmol
s [−][1] on the Monolith


_q_ 90 [mmol g [−][1] ] 0.44 0.71 0.016 0.035
_t_ 90 [s] 164,255 1960 14,964 258
_t_ 50 [s] 110,389 1214 11,018 179


and _p_ 2 on the packed bed, estimated using the procedure
outlined in Section 2.4.5, are reported in Table 7. The estimated
value of the axial dispersion coefficient is higher than those
obtained from literature correlations. Although prior literature
has shown that such correlations can often underestimate the
axial dispersion coefficient, [56] such a major difference could stem
from factors such as bypassing and channeling phenomena
resulting from irregularities in the size and shape of the pellet
rings (which might be too large for the column diameter).
Despite the significant axial dispersion contribution, the
optimizer effectively captured mass transfer resistances, and
the minimization algorithm yielded values of _kg_ and _ks_ consistent
with literature correlations. It was observed that variations in
feed velocity had an insignificant effect on the film mass transfer
coefficient, resulting in a constant _kg_ value for all experiments,
which is also consistent with literature findings. [57] The major



mass transfer resistance within _k_ was found to be in the gas
phase, consistent with the findings of constant pattern analysis.
Achieving a good fit using the PFO model for the monolith
breakthrough curves proved to be impossible with any
combination of _k_ and _DL_ . To be more specific, the model was
able to describe the initial part of the breakthrough profiles but
unable to describe the long tails (see Figure 7). Therefore,
resorting to the DK model was necessary to improve simulation
accuracy.
_3.2.2._ _Dual_ _Kinetic_ _Model._ In the monolith experiments,
fitting _k_ 1 and _DL_ using the procedure presented in Section 2.4.5
resulted in multiple combinations, effectively describing the
initial part of the breakthrough curve. Therefore, selecting
appropriate _k_ 1 and _DL_ involved utilizing literature correlations to
compute _k_ 1 and conducting a sensitivity analysis on _DL_ to
estimate the values of _p_ 1 and _p_ 2, as reported in Table 7. Axial
dispersion was again significantly higher than that from literature
correlations. This indeed confirms the constant pattern findings
and could be attributed to gas channeling around and through
the textile felts, which keep the monolith in place.
Subsequently, _k_ 2 and _η_ were fitted to the entire breakthrough
profile of the monolith experiments. The fraction of surface
amine sites was found to be _η_ = 0.75 and the amine layer rate
constant was fitted to eq 13, yielding _ks_,amine = 0.0011 s [−][1] . The
resulting _k_ 1 and _k_ 2 values are reported in Table 8, and the DK
model simulations using the fitted parameters are plotted as gray
curves in Figure 4. The DK model simulations with the fitted
parameters effectively reproduced the monolith breakthrough


**11646** [https://doi.org/10.1021/acs.iecr.4c01392](https://doi.org/10.1021/acs.iecr.4c01392?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
_Ind. Eng. Chem. Res._ 2024, 63, 11637−11653


**Industrial & Engineering Chemistry Research** **pubs.acs.org/IECR** Article


Figure 6. Comparison of breakthrough profiles at two different feed concentrations: orange and green curves at 5.6%, and red and blue curves at 400
ppm. The concentrations were evaluated under constant velocity conditions: 2 mmol s [−][1] on the packed bed and 0.18 mmol s [−][1] on the monolith.
Subfigures (a,b) represent the time axis in minutes, while (c,d) show a normalized time axis.


Table 7. Transport Parameters Estimated on the Two Contactors and Comparison with Literature Correlations Reported in
Table 4, with the Interstitial Velocity, _u_, Expressed in [m s [−][1] ]


_kf_ [s [−][1] ]     - 43−70     - 93
_kp_ [s [−][1] ]    - 3.35    - 237
_kg_ [s [−][1] ] 2.79 3.19    - 67
_ks_ [s [−][1] ] 5.8 × 10 [5] 1.9 × 10 [4]    - 1.9 × 10 [4]

_ks_,amine [s [−][1] ]    -    - 0.0011    _η_ [�]   -   - 0.75   _DL_ [m [2] s [−][1] ] 6.95 _u_ + 0.02 0.0015 _u_ + 0.00003 1.22 _u_ [2] + 0.0004 0.0013 _u_ [2] + 0.0000162



curves and their tail behavior, with the exception of the 0.18
mmol s [−][1] experiment in Figure 4c. Adjusting _ks_,amine to 0.0001
s [−][1] improved the overall fit (shown by the dotted gray line). This
observation does not resolve the issue that this specific
experiment cannot be described with the same parameters as
the others, but at least it proves that the DK model is in general
capable of describing the type of asymmetric breakthrough
profiles so clearly observed in the case of monoliths.
_3.2.3._ _Comparing_ _the_ _PFO_ _and_ _DK_ _Model_ _Solutions._ The
successful application of the PFO model in modeling the packed
bed experiments suggests that employing a DK model may not
be necessary for this contactor. Indeed, attempts to use the DK
model in fitting the packed bed breakthrough profiles resulted
in: _k_ 2 = _k_ 1, for any value of _η_ ; or _η_ = 1 for any value of _k_ 2, leading
to the same solution as the PFO model. Assuming that the



physical characteristics of the amine layer in the _γ_ -alumina phase
of both contactors are the same, we applied the _η_ and _ks_,amine
values estimated on the monolith to test the DK model’s
performance in the packed bed simulations. The solutions
obtained with PFO and DK models are similar, as shown in
Figure 7a. Despite the likely existence of two types of amine sites
in the pellets, the slow rate of mass transport to the surface
amines ( _k_ 1) compared to that of mass transport in the
aminopolymer layer ( _ks_,amine) renders the influence of _ks_,amine
on _k_ 2 minimal. This results in comparable magnitudes of _k_ 1 and
_k_ 2, causing an insignificant change in mass transfer kinetics and
explaining the absence of an evident tail in the simulations and in
the experiments in packed beds.
In contrast to the packed bed experiments, the kinetics within
the aminopolymer layer significantly affected _k_ 2 in the


**11647** [https://doi.org/10.1021/acs.iecr.4c01392](https://doi.org/10.1021/acs.iecr.4c01392?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
_Ind. Eng. Chem. Res._ 2024, 63, 11637−11653


**Industrial & Engineering Chemistry Research** **pubs.acs.org/IECR** Article



Figure 7. Comparison between the DK model (solid) and the PFO
model (dashed) solutions with _k_ 1 and _k_ 2 as defined in Table 8 and _k_ = _k_ 1
on the (a) packed bed, at 5.6% and 0.5 mmol s [−][1] ; (b) monolith, at 400
ppm and 2 mmol s [−][1]


Table 8. Values of _c_ in/ _q_ ***** in for the Four Experiment Types
Spanning Across Two Contactors and Two Feed
Concentrations and Resulting Values of _k_ 1 and _k_ 2 Computed
from eqs 12 and 13 Using the Estimated Mass Transfer
Coefficients Reported in Table 7


_c_ in/ _q_ *in [-] 0.00003 0.002 0.0006 0.04
_k_ 1 [s [−][1] ] 0.000088 0.0063 0.037 2.7
_k_ 2 [s [−][1] ] 0.000082 0.001 0.0011 0.0011


monoliths, owing to the considerably larger value of _k_ 1
compared to _ks_,amine. This resulted in a substantial change in



mass transfer kinetics during adsorption, which was particularly
evident at higher concentrations, where the tail was more
pronounced and the difference between _k_ 1 and _k_ 2 was even
larger. This disparity explains why the tails were more
pronounced on the monoliths than on the packed bed,
highlighting the inadequacy of the PFO model in capturing
this effect (Figure 7b). Nevertheless, for cases in which reaching
full saturation is not favorable, detailed modeling of breakthroughs beyond the start of elongated tails may not be essential,
especially for cyclic modeling. To this end, using a PFO model to
capture the curve’s initial slope until the desired saturation point
may suffice.
**3.3.** **Contactor** **Comparison.** _3.3.1._ _Assessment_ _of_ _the_
_Resulting Mass Transfer Kinetics._ Several observations can be
made based on the estimated mass transfer coefficients and their
comparison with literature correlations. First, _ks_ is much larger
than _kg_, thus _k_ 1 is controlled by the resistance in the gas phase
(film and sorbent pores). This is consistent with the findings of
the constant pattern analysis. As a result, mass transfer kinetics
are concentration-dependent, with _k_ 1 proportional to _c_ in/ _q_ *p,in
(Table 8). Moreover, in the packed bed _kg_ is determined by _kp_
whereby _kf_ plays a negligible role; in the monolith instead both _kp_
and _kf_ influence _kg_ within the specified range of velocities.
Operating at higher feed velocities on the monolith would
decrease the impact of _kf_, resulting in _k_ 1 being only governed by
_kp_ . Comparing the two contactors, _k_ 1 was approximately 400
times higher on the monolith than on the packed bed. This is
due to a higher value of _c_ in/ _q_ - _p_,in in the monolith and to several
geometric differences: the reduced wall thickness of the
monolith compared to the diameter of the pellet (shorter
diffusion path in _kp_ ); and the monolith’s macroporous structure
(faster diffusivity in _kp_ ).
_3.3.2._ _Adsorption_ _KPIs._ Despite the monolith’s significantly
lower CO2 capacity, i.e., 0.016 mmol g [−][1] compared to 0.44
mmol g [−][1] in the packed bed, the reduction in diffusion path
offered by the monolith presents a promising strategy to mitigate
mass transfer limitations. To assess the tradeoff between mass
transfer kinetics and CO2 capacity, the adsorption productivity
and the specific blower energy consumption were computed,
thus obtaining the values plotted in Figure 8a for all experiments
performed at 400 ppm. The KPIs were calculated at various



Figure 8. Specific energy demand plotted against the productivity of the adsorption step and comparison between the packed bed and monolith for all
of the experiments performed in this study using a CO2 inlet molar fraction of (a) _y_ in = 400 ppm; (b) _y_ in = 5.6%. The curves in subfigure (a) show the
evolution of the blower energy consumption vs productivity when defining the total adsorption time at 90, 80, 70, and 50% of the breakthrough,
defined as _t_ 90, _t_ 80, _t_ 70, and _t_ 50, respectively; the curves in subfigure (b) respect a recovery rate constraint of 95%.


**11648** [https://doi.org/10.1021/acs.iecr.4c01392](https://doi.org/10.1021/acs.iecr.4c01392?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
_Ind. Eng. Chem. Res._ 2024, 63, 11637−11653


**Industrial & Engineering Chemistry Research** **pubs.acs.org/IECR** Article


points along the breakthrough curve to assess the effect of
saturation on performance, as achieving full saturation of the
column may not optimize the performance. The productivityenergy values obtained by varying velocities on the monolith
indicate that there is a tradeoff between productivity and energy
penalty (associated with the operation of the blower), which
both increase with increasing gas velocities. Notably, the results
illustrated in Figure 8 indicate that at t90, at the same flow rate of
2 mmol s [−][1], the use of a monolith resulted in a 50% reduction in
specific blower energy consumption and a 66% increase in
productivity compared to a packed bed. This observation
implied that increased mass transfer rates on the monolith more
than compensated for its reduction in the CO2 capacity.
Stopping adsorption early improved our KPIs, as adsorption
productivity drops as soon as breakthrough is reached. While full
column saturation seems unfavorable, definitive conclusions on
adsorption times require consideration of the whole DAC cycle.
Importantly, the qualitative comparison between contactors
remains consistent at different points of saturation. It is worth
noting that, using productivity per unit volume occupied by each
contactor, our findings exhibited the same trends, as shown in
[Figure S5.](https://pubs.acs.org/doi/suppl/10.1021/acs.iecr.4c01392/suppl_file/ie4c01392_si_001.pdf)



Figure 8b shows the curves for the experiments performed at
5.6%, at three velocities both on the packed bed and on the
monolith. The only difference from the experiments at 400 ppm
consisted of the requirement that a minimum CO2 recovery rate
of 95% was fulfilled, as highlighted in Section 2.6. Interestingly,
the conclusions drawn for the DAC-relevant conditions were
less evident at the higher feed concentration: transitioning from
the packed bed to the monolith did not result in an
unequivocally better performance during adsorption. These
observations suggest that, although the mass transfer coefficient
on the monolith was indeed larger than that on the packed bed,
the decrease in the CO2 capacity in the monolith could not be
offset by the faster kinetics as in the case of the 400 ppm
experiments. Although these results are specific to the
experiments conducted in this work, they highlight the
importance of selecting the appropriate material and contactor
for each given separation process.
**3.4. Regeneration Experiments.** Though the focus of this
study is on the adsorption step, during sorbent regeneration, i.e.,
a routine operation after saturating the contactor at the selected
feed concentration), we recorded elution profiles and outlet
temperature. Representative regeneration profiles after adsorption at 400 ppm and 5.6% performed on the packed bed column
and on the monolith are presented in Figure 9a,b, respectively,
where the rate of outflowing CO2 and the temperature are
plotted. As described in the methodology section (Section 2),
CO2 desorption and column regeneration require both purge
with N2 (or evacuation) and heating, as also reported earlier. [58]

Without carrying out an in-depth discussion of the
regeneration step in the context of the entire DAC cycle,
which is beyond the scope of this work, it is worth observing in
the figures that regeneration times are similar in the same
contactor for the two quite different concentration levels,
namely, about 2 h for fixed beds and less than 1 h for monoliths.
This is in obvious contrast to adsorption times, which are very
different for the two concentration levels; as reported in Table 6,
_t_ 90 for adsorption is about 80 and 60 times larger at 440 ppm
than at 5.6% in packed beds and in monoliths, respectively. This
difference between adsorption and regeneration stems from the
fact that the equilibrium adsorbed amount at the two very
different feed concentrations in the gas (5.6% is about 150 times



Figure 9. Experimental regeneration profiles on the packed bed (PB)
and on the monolith (M) after experiments performed with a feed of _y_ =
400 ppm and _y_ = 5.6%, showing the molar outflow of CO2 (solid line)
and the column temperature (dotted or dashed line).


larger than 400 ppm) differs by only about 50% (from 0.44
mmol g [−][1] at 400 ppm to 0.71 mmol g [−][1] at 5.6%).
On the one hand, when one looks at regeneration as a thermal
swing step, the heat requirement is due to the need of heating
adsorbent and contactor, which is the same whatever the initial
concentration, and to the need to desorb the saturation amount
of CO2, whose contribution is small and differs only slightly for
the two concentration levels. On the other hand, the amount of
CO2 to be adsorbed, which is of the same order of magnitude at
400 ppm and at 5.6%, is conveyed into the contactor at widely
different rates indeed because of the widely different
concentrations, even when the gas velocity is the same in the
two cases. Such material balance effect is combined with the role
played by the adsorption isotherm at the initial and final
temperature of the swing step, thus yielding almost 2 orders of
magnitude of difference in the adsorption times between low
and high CO2 concentration in the feed.
The following figures quantify this effect: at 5.6%, the
adsorption step accounts for about 15% of the total adsorption
and regeneration cycle time, while at 400 ppm, it accounts for
about 90% of the overall time. Interestingly, we observe that the
ratio is similar in Climeworks’ ORCA plant, where the
adsorption step occupies 83% of the total cycle time. [59]

**3.5.** **Contextualizing** **This** **Work** **in** **DAC-Relevant**
**Conditions.** To contextualize our findings for DAC-relevant
conditions, it is essential to also consider factors such as the
influence of humidity in the feed and the impact of operating at
higher velocities.
While air humidity was not explicitly addressed in this study,
literature has documented an increase in CO2 adsorption
capacity by water coadsorption on amine-functionalized
materials. [10][,][60] The quantitative impact of water coadsorption
on the KPIs considered here remains uncertain, because it may
impact both CO2 capacity (by improving it) and mass transfer
kinetics (by slowing it down). [61] To effectively evaluate this, one
must conduct equilibrium and kinetic measurements on CO2−


**11649** [https://doi.org/10.1021/acs.iecr.4c01392](https://doi.org/10.1021/acs.iecr.4c01392?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
_Ind. Eng. Chem. Res._ 2024, 63, 11637−11653


**Industrial & Engineering Chemistry Research** **pubs.acs.org/IECR** Article



H2O coadsorption, coupled with cyclic DAC studies. Nonetheless, we anticipate that the introduction of humidity in the feed
would affect the two contactors similarly and would yield a
qualitatively similar comparison to that illustrated in Figure 8.
Axial dispersion and mass transport in the gas film and sorbent
pores control adsorption within our experimental framework.
Operating at higher velocities mitigates limitations arising from
axial dispersion and film resistance, leading to an improvement
in the separation performance. However, this improvement is
limited by mass transport in the sorbent pores, which is a sorbent
property independent of the velocity. Thus, regardless of the
feed velocity, the thin monolith walls offer a diffusion length that
enhances mass transport compared to pellets of a relevant size.
This provides a practical solution to enhance the DAC kinetics.


**4.** **CONCLUSIONS**

In this work, we considered two amine-functionalized _γ_ -alumina
sorbents in the shape of pellets and a _γ_ -alumina wash-coated
monolith. We performed multiple breakthrough experiments on
a cylindrical packed bed containing the pellets and on the
monolith, with the goal of: (i) gaining insight on the
mechanisms limiting adsorption kinetics, (ii) quantifying the
transport phenomena with detailed adsorption modeling, and
(iii) comparing the adsorption performance of the two
contactors within the range of experimental conditions studied.
The work resulted in the following key insights.


 - The mass transfer zone analysis using the constant pattern
revealed, without the need for a physical model, that the
dominant mass transfer resistances are in the gas film and
in the pores. Moreover, significant axial dispersion was
observed, particularly at higher concentrations, thus
highlighting its impact on system performance where
mass transfer resistances were smaller. While the
broadness of the mass transfer front is not a concern for
CO2 recovery in DAC applications, proper column design
to avoid such phenomena is necessary to ensure optimal
utilization of the contactor;


 - Subsequently, the 1D model was employed to estimate
transport parameters during adsorption. Here, the
qualitative findings of the constant pattern analysis were
confirmed and mass transfer correlations were validated.
However, a notable discrepancy in the estimated and
literature axial dispersion coefficients indicated the
possible occurrence of gas bypassing within the
contactors;


 - Two mass transfer models were evaluated: a conventional
pseudo-first-order model and a dual kinetic model, which
incorporates two types of amine sites with distinct
saturation capacities and rates of mass transfer.
Implementation of the DK model revealed that the
kinetics in the aminopolymer layer are considerably
slower than mass transport in the gas film and in the pores
of the monolith. This explained the elongated breakthrough tails and confirmed the need to use such a model
to adequately describe this behavior. In contrast, slow
mass transport in film and sorbent pores in packed bed
experiments governed adsorption, resulting in negligible
influence of mass transfer resistances in the aminopolymer. This explained the lack of evident tails in the
packed bed experiments and validated the use of a PFO
model for their description;




    - The obtained results demonstrated that the monolith
contactor exhibited significantly higher mass transfer
coefficients compared to packed beds, which can be
attributed to the combined effects of shorter diffusion
lengths (0.4 mm walls vs 3 mm pellets) and lower
equilibrium capacity, resulting in higher values of the
factor _c_ in/ _q_       - _p_,in;

    - As a result, experiments at 400 ppm performed on the
monolith exhibited reduced specific energy consumption
and an increase in adsorption productivity with respect to
the packed bed, thus making the monolith the preferred
contactor for such a separation within the range of
experimental conditions studied. The increased mass
transfer coefficient on the monolith was not sufficient to
simultaneously increase productivity and specific energy
consumption of the blower at 5.6% with respect to the
packed bed, thus not allowing for a clear choice regarding
the preferred contactor for such conditions.


In the past, research on monoliths as promising contactors for
DAC were motivated by the possibility to reduce the significant
electrical energy consumption associated with high pressure
drops, typical of packed beds. However, recent studies have
indicated that monoliths possess additional advantageous
geometric properties that can lead to improved mass transfer
rates. By investigating and elucidating these phenomena, this
research contributes to a comprehensive understanding of the
enhanced mass transfer in monolith contactors, highlighting
their crucial role in DAC systems.
# ■* sı Supporting Information [ASSOCIATED CONTENT]

The Supporting Information is available free of charge at
[https://pubs.acs.org/doi/10.1021/acs.iecr.4c01392.](https://pubs.acs.org/doi/10.1021/acs.iecr.4c01392?goto=supporting-info)


Additional information on the measured equilibrium data,
heat transfer coefficients, measured pressure drop,
experiment reproducibility, and key performance indica[tors and derivation of Figure 3 (PDF)](https://pubs.acs.org/doi/suppl/10.1021/acs.iecr.4c01392/suppl_file/ie4c01392_si_001.pdf)
# ■ Corresponding Author [AUTHOR INFORMATION]

Marco Mazzotti − _Institute of Energy and Process Engineering,_
_ETH Zurich, Zurich 8092, Switzerland;_ [orcid.org/0000-](https://orcid.org/0000-0002-4948-6705)
[0002-4948-6705; Phone: +41 44 632 24 56;](https://orcid.org/0000-0002-4948-6705)
[Email: marco.mazzotti@ipe.mavt.ethz.ch; Fax: +41 44 632](mailto:marco.mazzotti@ipe.mavt.ethz.ch)
11 41


**Authors**

Valentina Stampi-Bombelli − _Institute of Energy and Process_
_[Engineering, ETH Zurich, Zurich 8092, Switzerland](https://pubs.acs.org/action/doSearch?field1=Contrib&text1="Alba+Storione"&field2=AllField&text2=&publication=&accessType=allContent&Earliest=&ref=pdf)_
Alba Storione − _Department of Civil, Chemical, Environmental_
_and Materials Engineering (DICAM), Alma Mater_
_[Studiorum-University of Bologna, Bologna 40131, Italy](https://pubs.acs.org/action/doSearch?field1=Contrib&text1="Quirin+Grossmann"&field2=AllField&text2=&publication=&accessType=allContent&Earliest=&ref=pdf)_
Quirin Grossmann − _Institute of Energy and Process_
_Engineering, ETH Zurich, Zurich 8092, Switzerland;_

[orcid.org/0000-0003-0999-0891](https://orcid.org/0000-0003-0999-0891)


Complete contact information is available at:
[https://pubs.acs.org/10.1021/acs.iecr.4c01392](https://pubs.acs.org/doi/10.1021/acs.iecr.4c01392?ref=pdf)


**Notes**
The authors declare no competing financial interest.


**11650** [https://doi.org/10.1021/acs.iecr.4c01392](https://doi.org/10.1021/acs.iecr.4c01392?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
_Ind. Eng. Chem. Res._ 2024, 63, 11637−11653


**Industrial & Engineering Chemistry Research** **pubs.acs.org/IECR** Article


# ■ [ACKNOWLEDGMENTS]

We would like to thank HUG Engineering, and Michael Pabel
and his co-workers at Saint Gobain for providing the samples
used in this work. This work was supported by the Swiss
National Science Foundation grant number 197221.
# ■ [NOTATION]

**Roman symbols**
_A_ column cross section [m [2] ]
_c_ gas phase concentration [mol m [−][3] ]
_dp_ pellet diameter [m]
_d_ pore diameter of the _γ_ -alumina pore [m]
_D_ column diameter [m]
_D_ al effective diffusivity in the _γ_ -alumina pockets [m [2] s [−][1] ]
_Dp_ effective diffusivity in the pellet pore [m [2] s [−][1] ]
_Dm_ molecular diffusion v[m [2] s [−][1] ]
_D_ mullite effective diffusivity in the mullite pores [m [2] s [−][1] ]
_Ds_ crystalline diffusivity [m [2] s [−][1] ]
_DL_ axial dispersion coefficient [m [2] s [−][1] ]
_k_ LDF overall mass transfer coefficient [s [−][1] ]
_K_ Langmuir equilibrium constant [m [3] mol [−][1] ]
_kf_ film mass transfer coefficient [s [−][1] ]
_k_ ′ _f_ film mass transfer coefficient [m s [−][1] ]
_kp_ pore mass transfer coefficient [s [−][1] ]
_kp_,al mass transfer coefficient in the _γ_ -alumina pocket
mesopores [s [−][1] ]
_kp_,mullite mass transfer coefficient in the mullite macropores

[s [−][1] ]
_ks_ solid mass transfer coefficient [s [−][1] ]
_L_ column length [m]
_M_ molecular weight [g mol [−][1] ]
_ms_ sorbent mass [kg]
_n_ molar flow rate [mol s [−][1] ]
_N_ total number of cells in the monolith [-]
_p_ pressure [Pa]
_Pe_ Peclet number, [= _uL_ / _DL_ ] [-]
_q_ mass-based adsorbed-phase concentration [mol
kg [−][1] sorbent []]
_qp_ volume-based adsorbed-phase concentration, [ = _qρ_ p]

[mol m [−][3] ]
_q_ volume-based adsorbed-phase concentration, [ = _qρ_ s]

[mol m [−][3] ]
_q_ - solid loading at equilibrium with _c_ [mol kg [−][1] ]
_r_ 1 internal hydraulic diameter of the square monolith
channel, [50] [ =2 _w_ 1/ _π_ ] [m]
_r_ 2 external hydraulic diameter of the square monolith
channel, [50] [ = (4 _wwallw_ 2/ _pi_ + _r_ 12)0.5] [m]
_r_ al radius of _γ_ -alumina pockets [m]
_rc_ crystalline radius [m]
_rp_ pellet radius [m]
_Re_ Reynolds number, [= _ρusdp_ / _μ_ ] [-]
_Sc_ Schmidt number, [= _μ_ /( _ρDm_ ) ] [-]
_Sh_ Sherwood number [-]
_St_ Stanton number, [ = _kL_ / _u_ ] [-]
_t_ time [s]
_T_ temperature [K]
_u_ interstitial velocity, [ = _us_ / _ε_ ] [m s [−][1] ]
_us_ superficial velocity [m s [−][1] ]
_V_ volumetric flow rate of the gas feed [m [3] s [−][1] ]
_W_ monolith width [m]
_w_ 1 monolith void channel width [m]
_w_ 2 monolith cell width, [ _w_ 2 = _w_ 1 + _w_ wall] [m]



_W_ fan specific blower energy consumption [MJ mol [−][1] ]
_w_ wall monolith wall thickness [m]
_x_ dimensionless axial coordinate, [ = _z_ / _L_ ] [-]
_y_ CO2 molar fraction [-]
_z_ axial coordinate [m]


**Greek Symbols**
_α_ parameter of the shock layer [-]
_β_ percentage of the feed concentration in the shock layer
analysis v[-]
Δ _p_ pressure drop across the column [Pa]
_ε_ bed void fraction [-]
_ε_ al void fraction of the _γ_ -alumina pockets in the monolith [-]
_ε_ p pellet/wall void fraction [-]
_ε_   - total void fraction, [ = _ε_ + _εp_ (1 − _ε_ )] [-]
Γ parameter of the shock layer [-]
_λ_ dimensionless shock velocity [-]
_μ_ dynamic viscosity [Pa s]
_ν_ capacity ratio, [=(1 − _ε_ )/ _ε_ ] [-]
_ν_   - capacity ratio, [=(1 − _ε_ *)/ _ε_ *] [-]
_ξ_ moving coordinate, [ = _z_   - _λτ_ ] [-]
_ψ_ porosity ratio, [ = _ε_ */ _ε_ ] [-]
_ρ_ b bed density [kg m [−][3] COLUMN []]
_ρ_ p pellet density [kg m [−][3] PELLET []]
_ρ_ s solid density [kg m [−][3] SOLID []]
_τ_ dimensionless time, [ = _tu_ / _L_ ] [-]
_τ_ al _γ_ -alumina tortuosity [-]
_τ_ mullite mullite tortuosity [-]
_ϑ_ parameter of the shock layer [-]


**Subscripts and Superscripts**
in feed conditions


**Acronyms**
CPSI cells per square inch
DAC direct air capture
KPI key performance indicator
LDF linear driving force
MFC mass flow controller
MTZ mass transfer zone
NET negative emission technologies
# ■ [REFERENCES]

(1) United Nations Environment Programme, Paris Agreement. 2015.
[https://wedocs.unep.org/20.500.11822/20830](https://wedocs.unep.org/20.500.11822/20830) (accessed: Jan 10,
2023).
(2) EASAC. _Negative Emission Technologies: What Role in meeting Paris_
_Agreement Targets?_ ; EASAC, 2018; p 37.
(3) Sodiq, A.; Abdullatif, Y.; Aissa, B.; Ostovar, A.; Nassar, N.; El[Naas, M.; Amhamed, A. A review on progress made in direct air capture](https://doi.org/10.1016/j.eti.2022.102991)
[of CO2.](https://doi.org/10.1016/j.eti.2022.102991) _Environ. Technol. Innov._ 2023, _29_, 102991.
(4) Sabatino, F.; Grimm, A.; Gallucci, F.; van Sint Annaland, M.;
[Kramer, G. J.; Gazzani, M. A comparative energy and costs assessment](https://doi.org/10.1016/j.joule.2021.05.023)
and optimization for [direct](https://doi.org/10.1016/j.joule.2021.05.023) air capture technologies. _Joule_ 2021, _5_,
2047−2076.
[(5) Sanz-Pérez, E. S.; Murdock, C. R.; Didas, S. A.; Jones, C. W. Direct](https://doi.org/10.1021/acs.chemrev.6b00173?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
Capture of CO2 [from](https://doi.org/10.1021/acs.chemrev.6b00173?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as) Ambient Air. _Chem._ _Rev._ 2016, _116_, 11840−
11876.
(6) Barkakaty, B.; Sumpter, B. G.; Ivanov, I. N.; Potter, M. E.; Jones, C.
[W.; Lokitz, B. S. Emerging materials for lowering atmospheric carbon.](https://doi.org/10.1016/j.eti.2016.12.001)
_Environ. Technol. Innov._ 2017, _7_, 30−43.
(7) Belmabkhout, Y.; Serna-Guerrero, R.; Sayari, A. [Adsorption](https://doi.org/10.1021/ie900837t?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as) of
CO2-Containing Gas Mixtures [over](https://doi.org/10.1021/ie900837t?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as) Amine-Bearing Pore-Expanded
[MCM-41 Silica: Application for Gas Purification.](https://doi.org/10.1021/ie900837t?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as) _Ind. Eng. Chem. Res._
2010, _49_, 359−365.


**11651** [https://doi.org/10.1021/acs.iecr.4c01392](https://doi.org/10.1021/acs.iecr.4c01392?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
_Ind. Eng. Chem. Res._ 2024, 63, 11637−11653


**Industrial & Engineering Chemistry Research** **pubs.acs.org/IECR** Article



(8) Choi, S.; Gray, M. L.; Jones, C. W. [Amine-tethered](https://doi.org/10.1002/cssc.201000355) solid
adsorbents coupling high [adsorption](https://doi.org/10.1002/cssc.201000355) capacity and regenerability for
[CO2 capture from ambient air.](https://doi.org/10.1002/cssc.201000355) _ChemSusChem_ 2011, _4_, 628−635.
(9) Kwon, H. T.; Sakwa-Novak, M. A.; Pang, S. H.; Sujan, A. R.; Ping,
E. W.; Jones, C. W. [Aminopolymer-Impregnated](https://doi.org/10.1021/acs.chemmater.9b01474?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as) Hierarchical Silica
Structures: Unexpected [Equivalent](https://doi.org/10.1021/acs.chemmater.9b01474?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as) CO2 Uptake under Simulated Air
Capture and Flue [Gas](https://doi.org/10.1021/acs.chemmater.9b01474?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as) Capture Conditions. _Chem._ _Mater._ 2019, _31_,
5229−5237.
(10) Gebald, C.; Wurzbacher, J. A.; Tingaut, P.; Zimmermann, T.;
Steinfeld, A. Amine-based [nanofibrillated](https://doi.org/10.1021/es202223p?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as) cellulose as adsorbent for
[CO2 capture from air.](https://doi.org/10.1021/es202223p?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as) _Environ. Sci. Technol._ 2011, _45_, 9101−9108.
(11) Lee, J. J.; Yoo, C. J.; Chen, C. H.; Hayes, S. E.; Sievers, C.; Jones,
[C. W. Silica-Supported Sterically Hindered Amines for CO2 Capture.](https://doi.org/10.1021/acs.langmuir.8b02472?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
_Langmuir_ 2018, _34_, 12279−12292.
(12) Gebald, C.; Wurzbacher, J. A.; Borgschulte, A.; Zimmermann, T.;
[Steinfeld, A. Single-Component and Binary CO2 and H2O Adsorption](https://doi.org/10.1021/es404430g?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
of [Amine-Functionalized](https://doi.org/10.1021/es404430g?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as) Cellulose. _Environ._ _Sci._ _Technol._ 2014, _48_,
2497−2504.
(13) Darunte, L. A.; Oetomo, A. D.; Walton, K. S.; Sholl, D. S.; Jones,
C. W. Direct Air Capture of CO2 [Using](https://doi.org/10.1021/acssuschemeng.6b01692?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as) Amine Functionalized MIL[101(Cr).](https://doi.org/10.1021/acssuschemeng.6b01692?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as) _ACS Sustainable Chem. Eng._ 2016, _4_, 5761−5768.
(14) Darunte, L. A.; Terada, Y.; Murdock, C. R.; Walton, K. S.; Sholl,
D. S.; Jones, C. W. Monolith-Supported Amine-Functionalized
[Mg2(dobpdc) Adsorbents for CO2 Capture.](https://doi.org/10.1021/acsami.7b02035?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as) _ACS Appl. Mater. Interfaces_
2017, _9_, 17042−17050.
(15) Young, J., García-Díez, E., Garcia, S., Ireland, C., Smit, B., van der
Spek, M. Investigating H2O and CO2 co-adsorption on aminefunctionalised solid sorbents for direct air capture. In _SSRN Electronic_
_Journal_, 2021; pp 1−7.
(16) Rezaei, F.; Webley, P. Optimum [structured](https://doi.org/10.1016/j.ces.2009.08.029) adsorbents for gas
[separation processes.](https://doi.org/10.1016/j.ces.2009.08.029) _Chem. Eng. Sci._ 2009, _64_, 5182−5191.
[(17) Rezaei, F.; Webley, P. Structured Adsorbents in Gas Separation](https://doi.org/10.1016/j.seppur.2009.10.004)
[Processes.](https://doi.org/10.1016/j.seppur.2009.10.004) _Sep. Purif. Technol._ 2010, _70_, 243−256.
[(18) Mennitto, R.; Sharma, I.; Brandani, S. Extruded monoliths for gas](https://doi.org/10.1002/aic.17650)
separation processes: Height [equivalent](https://doi.org/10.1002/aic.17650) to a theoretical plate and
[pressure drop correlations.](https://doi.org/10.1002/aic.17650) _AlChE J._ 2022, _68_, No. e17650.
(19) Gebald, C.; Piatkowski, N.; Ruesch, T.; Wurzbacher, J. A. LowPressure Drop Structure of Particle Adsorbent Bed for Adsorption Gas
Separation Process. WO 2014/170184 Al, 2014.
(20) Yu, Q.; Brilman, W. A Radial Flow [Contactor](https://doi.org/10.3390/app10031080) for Ambient Air
[CO2 Capture.](https://doi.org/10.3390/app10031080) _Appl. Sci._ 2020, _10_, 1080.
(21) Eisenberger, P.; Chichilnisky, G. Rotating Multi-Monolith Bed
Movement System for Removing CO2 from the Atmosphere. U.S.
Patent: 10,512,880 B2, 2019.
(22) Eisenberger, P. Carbon Dioxide Capture/Regeneration
Structures and Techniques. U.S. Patent: 8,163,066 B2, 2012.
[(23) Kulkarni, A. R.; Sholl, D. S. Analysis of equilibrium-based TSA](https://doi.org/10.1021/ie300691c?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
[processes for direct capture of CO2 from Air.](https://doi.org/10.1021/ie300691c?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as) _Ind. Eng. Chem. Res._ 2012,
_51_, 8631−8645.
[(24) Stampi-Bombelli, V.; van der Spek, M.; Mazzotti, M. Analysis of](https://doi.org/10.1007/s10450-020-00249-w)
[direct capture of CO2 from ambient air via steam-assisted temperature−](https://doi.org/10.1007/s10450-020-00249-w)
[vacuum swing adsorption.](https://doi.org/10.1007/s10450-020-00249-w) _Adsorption_ 2020, _26_, 1183−1197.
(25) Balasubramaniam, B. M.; Thierry, P.-T.; Lethier, S.; Pugnet, V.;
[Llewellyn, P.; Rajendran, A. Process-performance of solid sorbents for](https://doi.org/10.1016/j.cej.2024.149568)
[Direct Air Capture (DAC) of CO2 in optimized temperature-vacuum](https://doi.org/10.1016/j.cej.2024.149568)
[swing adsorption (TVSA) cycles.](https://doi.org/10.1016/j.cej.2024.149568) _Chem. Eng. J._ 2024, _485_, 149568.
(26) Sinha, A.; Darunte, L. A.; Jones, C. W.; Realff, M. J.; Kawajiri, Y.
[Systems Design and Economic Analysis of Direct Air Capture of CO2](https://doi.org/10.1021/acs.iecr.6b03887?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
[through Temperature Vacuum Swing Adsorption Using MIL-101(Cr)-](https://doi.org/10.1021/acs.iecr.6b03887?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
[PEI-800 and mmen-Mg2(dobpdc) MOF Adsorbents.](https://doi.org/10.1021/acs.iecr.6b03887?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as) _Ind. Eng. Chem._
_Res._ 2017, _56_, 750−764.
(27) Sinha, A.; Realff, M. J. A parametric [study](https://doi.org/10.1002/aic.16607) of the technoeconomics of direct CO2 air [capture](https://doi.org/10.1002/aic.16607) systems using solid adsorbents.
_AlChE J._ 2019, _65_, 1−8.
[(28) Fasihi, M.; Efimova, O.; Breyer, C. Techno-economic assessment](https://doi.org/10.1016/j.jclepro.2019.03.086)
[of CO2 direct air capture plants.](https://doi.org/10.1016/j.jclepro.2019.03.086) _J. Clean. Prod._ 2019, _224_, 957−980.
(29) Azarabadi, H.; Lackner, K. S. A [sorbent-focused](https://doi.org/10.1016/j.apenergy.2019.04.012) techno[economic analysis of direct air capture.](https://doi.org/10.1016/j.apenergy.2019.04.012) _Appl. Energy_ 2019, _250_, 959−
975.



(30) Young, J.; McQueen, N.; Charalambous, C.; Foteinis, S.; Hawrot,
O.; Ojeda, M.; Pilorgé, H.; Andresen, J.; Psarras, P.; Renforth, P.; et al.
[The cost of direct air capture and storage can be reduced via strategic](https://doi.org/10.1016/j.oneear.2023.06.004)
[deployment but is unlikely to fall below stated cost targets.](https://doi.org/10.1016/j.oneear.2023.06.004) _One Earth_
2023, _6_, 899−917.
[(31) Deutz, S.; Bardow, A. Life-cycle assessment of an industrial direct](https://doi.org/10.1038/s41560-020-00771-9)
air capture process based on [temperature−vacuum](https://doi.org/10.1038/s41560-020-00771-9) swing adsorption.
_Nat. Energy_ 2021, _6_, 203−213.
(32) Young, J.; Mcilwaine, F.; Smit, B.; Garcia, S.; van der Spek, M.
Process-informed adsorbent [design](https://doi.org/10.1016/j.cej.2022.141035) guidelines for direct air capture.
_Chem. Eng. J._ 2023, _456_, 141035.
[(33) Anyanwu, J. T.; Wang, Y.; Yang, R. T. Amine-Grafted Silica Gels](https://doi.org/10.1021/acs.iecr.9b05228?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
for CO2 Capture [including](https://doi.org/10.1021/acs.iecr.9b05228?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as) Direct Air Capture. _Ind._ _Eng._ _Chem._ _Res._
2020, _59_, 7072−7079.
(34) Darunte, L. A.; Sen, T.; Bhawanani, C.; Walton, K. S.; Sholl, D. S.;
Realff, M. J.; Jones, C. W. Moving beyond [Adsorption](https://doi.org/10.1021/acs.iecr.8b05042?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as) Capacity in
[Design of Adsorbents for CO2 Capture from Ultradilute Feeds: Kinetics](https://doi.org/10.1021/acs.iecr.8b05042?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
of CO2 Adsorption in [Materials](https://doi.org/10.1021/acs.iecr.8b05042?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as) with Stepped Isotherms. _Ind._ _Eng._
_Chem. Res._ 2019, _58_, 366−377.
(35) Sakwa-Novak, M. A.; Yoo, C. J.; Tan, S.; Rashidi, F.; Jones, C. W.
[Poly(ethylenimine)-Functionalized](https://doi.org/10.1002/cssc.201600404) Monolithic Alumina Honeycomb
[Adsorbents for CO2 Capture from Air.](https://doi.org/10.1002/cssc.201600404) _ChemSusChem_ 2016, _9_, 1859−
1868.
(36) Grossmann, Q.; Stampi-Bombelli, V.; Yakimov, A.; Docherty, S.;
[Copéret, C.; Mazzotti, M. Developing Versatile Contactors for Direct](https://doi.org/10.1021/acs.iecr.3c01265?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
[Air Capture of CO2 through Amine Grafting onto Alumina Pellets and](https://doi.org/10.1021/acs.iecr.3c01265?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
Alumina [Wash-Coated](https://doi.org/10.1021/acs.iecr.3c01265?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as) Monoliths. _Ind._ _Eng._ _Chem._ _Res._ 2023, _62_,
13594−13611.
(37) Wang, Y.; Rim, G.; Song, M. G.; Holmes, H. E.; Jones, C. W.;
[Lively, R. P. Cold Temperature Direct Air CO2 Capture with Amine-](https://doi.org/10.1021/acsami.3c13528?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
Loaded Metal-Organic Framework Monoliths. _ACS_ _Appl._ _Mater._
_Interfaces_ 2024, _16_, 1404−1415.
(38) Tegeler, E.; Cui, Y.; Masoudi, M.; Bahmanpour, A. M.; Colbert,
[T.; Hensel, J.; Balakotaiah, V. A novel contactor for reducing the cost of](https://doi.org/10.1016/j.ces.2023.119107)
[direct air capture of CO2.](https://doi.org/10.1016/j.ces.2023.119107) _Chem. Eng. Sci._ 2023, _281_, 119107.
[(39) Casas, N.; Schell, J.; Pini, R.; Mazzotti, M. Fixed bed adsorption](https://doi.org/10.1007/s10450-012-9389-z)
[of CO2/H2 mixtures on activated carbon: Experiments and modeling.](https://doi.org/10.1007/s10450-012-9389-z)
_Adsorption_ 2012, _18_, 143−161.
[(40) Ohs, B.; Krödel, M.; Wessling, M. Adsorption of carbon dioxide](https://doi.org/10.1016/j.seppur.2018.04.009)
[on solid amine-functionalized sorbents: A dual kinetic model.](https://doi.org/10.1016/j.seppur.2018.04.009) _Sep. Purif._
_Technol._ 2018, _204_, 13−20.
[(41) Bollini, P.; Brunelli, N. A.; Didas, S. A.; Jones, C. W. Dynamics of](https://doi.org/10.1021/ie301790a?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
[CO2 adsorption on amine adsorbents. 1. impact of heat effects.](https://doi.org/10.1021/ie301790a?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as) _Ind. Eng._
_Chem. Res._ 2012, _51_, 15145−15152.
[(42) Bollini, P.; Brunelli, N. A.; Didas, S. A.; Jones, C. W. Dynamics of](https://doi.org/10.1021/ie3017913?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
[CO2 adsorption on amine adsorbents. 2. insights into adsorbent design.](https://doi.org/10.1021/ie3017913?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
_Ind. Eng. Chem. Res._ 2012, _51_, 15153−15162.
(43) Kalyanaraman, J.; Fan, Y.; Lively, R. P.; Koros, W. J.; Jones, C. W.;
Realff, M. J.; Kawajiri, Y. Modeling and [experimental](https://doi.org/10.1016/j.cej.2014.08.023) validation of
[carbon dioxide sorption on hollow fibers loaded with silica-supported](https://doi.org/10.1016/j.cej.2014.08.023)
[poly(ethylenimine).](https://doi.org/10.1016/j.cej.2014.08.023) _Chem. Eng. J._ 2015, _259_, 737−751.
(44) Harlick, P. J.; Sayari, A. Applications [of](https://doi.org/10.1021/ie060774+?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as) pore-expanded
mesoporous silica. 5. triamine [grafted](https://doi.org/10.1021/ie060774+?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as) material with exceptional CO2
[dynamic and equilibrium adsorption performance.](https://doi.org/10.1021/ie060774+?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as) _Ind. Eng. Chem. Res._
2007, _46_, 446−458.
(45) Bali, S.; Leisen, J.; Foo, G. S.; Sievers, C.; Jones, C. W.
Aminosilanes grafted to basic [alumina](https://doi.org/10.1002/cssc.201402373) as CO2 adsorbents-role of
[grafting conditions on CO2 adsorption properties.](https://doi.org/10.1002/cssc.201402373) _ChemSusChem_ 2014,
_7_, 3145−3156.
[(46) Garg, D. R.; Ruthven, D. M. Linear driving force approximations](https://doi.org/10.1002/aic.690210137)
[for diffusion controlled adsorption in molecular sieve columns.](https://doi.org/10.1002/aic.690210137) _AlChE J._
1975, _21_, 200−202.
[(47) Farooq, S.; Ruthven, D. M. Heat Effects in Adsorption Column](https://doi.org/10.1021/ie00102a019?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
[Dynamics. 1. Comparison of One- and Two-Dimensional Models.](https://doi.org/10.1021/ie00102a019?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as) _Ind._
_Eng. Chem. Res._ 1990, _29_, 1076−1084.
[(48) Shafeeyan, M. S.; Wan Daud, W. M. A.; Shamiri, A. A review of](https://doi.org/10.1016/j.cherd.2013.08.018)
mathematical modeling of [fixed-bed](https://doi.org/10.1016/j.cherd.2013.08.018) columns for carbon dioxide
[adsorption.](https://doi.org/10.1016/j.cherd.2013.08.018) _Chem. Eng. Res. Des._ 2014, _92_, 961−988.


**11652** [https://doi.org/10.1021/acs.iecr.4c01392](https://doi.org/10.1021/acs.iecr.4c01392?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
_Ind. Eng. Chem. Res._ 2024, 63, 11637−11653


**Industrial & Engineering Chemistry Research** **pubs.acs.org/IECR** Article


(49) Wilkins, N. S.; Rajendran, A.; Farooq, S. [Dynamic](https://doi.org/10.1007/s10450-020-00269-6) column
[breakthrough experiments for measurement of adsorption equilibrium](https://doi.org/10.1007/s10450-020-00269-6)
[and kinetics.](https://doi.org/10.1007/s10450-020-00269-6) _Adsorption_ 2021, _27_, 397−422.
(50) Patton, A.; Crittenden, B. D.; Perera, S. P. Use of [the](https://doi.org/10.1205/0263876041580749) linear
driving force approximation to guide the design of monolithic
[adsorbents.](https://doi.org/10.1205/0263876041580749) _Chem. Eng. Res. Des._ 2004, _82_, 999−1009.
(51) Perry, R. H.; Green, D. W.; Maloney, J. O. _Perry’s_ _Chemical_
_Engineers’ Handbook_, 7th ed.; McGraw-Hill Education: USA, 1999, pp
16−21.
[(52) Glueckauf, E. Theory of chromatography. Part 10.- Formulæ for](https://doi.org/10.1039/TF9555101540)
[diffusion into spheres and their application to chromatography.](https://doi.org/10.1039/TF9555101540) _Trans._
_Faraday Soc._ 1955, _51_, 1540−1551.
(53) John, D. fminsearchbnd. 2012. [https://ch.mathworks.com/](https://ch.mathworks.com/matlabcentral/fileexchange/8277-fminsearchbnd-fminsearchcon)
[matlabcentral/fileexchange/8277-fminsearchbnd-fminsearchcon](https://ch.mathworks.com/matlabcentral/fileexchange/8277-fminsearchbnd-fminsearchcon) (accessed Mar 01, 2023).
(54) Wurzbacher, J. A.; Gebald, C.; Piatkowski, N.; Steinfeld, A.
[Concurrent Separation of CO2 and H2O from Air by a Temperature-](https://doi.org/10.1021/es301953k?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
Vacuum Swing [Adsorption/Desorption](https://doi.org/10.1021/es301953k?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as) Cycle. _Environ._ _Sci._ _Technol._
2012, _46_, 9191−9198.
[(55) Yu, Q.; Brilman, D. W. Design Strategy for CO2 Adsorption from](https://doi.org/10.1016/j.egypro.2017.03.1747)
[Ambient Air Using a Supported Amine Based Sorbent in a Fixed Bed](https://doi.org/10.1016/j.egypro.2017.03.1747)
[Reactor.](https://doi.org/10.1016/j.egypro.2017.03.1747) _Energy Procedia_ 2017, _114_, 6102−6114.
(56) Knox, J. C.; Ebner, A. D.; Levan, M. D.; Coker, R. F.; Ritter, J. A.
[Limitations of Breakthrough Curve Analysis in Fixed-Bed Adsorption.](https://doi.org/10.1021/acs.iecr.6b00516?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
_Ind. Eng. Chem. Res._ 2016, _55_, 4734−4748.
(57) Gelles, T.; Rezaei, F. Diffusion kinetics of CO2 in amine[impregnated MIL-101, alumina, and silica adsorbents.](https://doi.org/10.1002/aic.16785) _AlChE J._ 2020,
_66_, 1−15.
[(58) Wurzbacher, J. A.; Gebald, C.; Brunner, S.; Steinfeld, A. Heat and](https://doi.org/10.1016/j.cej.2015.08.035)
[mass transfer of temperature-vacuum swing desorption for CO2 capture](https://doi.org/10.1016/j.cej.2015.08.035)
[from air.](https://doi.org/10.1016/j.cej.2015.08.035) _Chem. Eng. J._ 2016, _283_, 1329−1338.
(59) Climeworks, Orca: the first large-scale plant. 2021. [https://](https://climeworks.com/plant-orca)
[climeworks.com/plant-orca (accessed Mar 21, 2024).](https://climeworks.com/plant-orca)
(60) Wiegner, J. F.; Grimm, A.; Weimann, L.; Gazzani, M. [Optimal](https://doi.org/10.1021/acs.iecr.2c00681?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
[Design and Operation of Solid Sorbent Direct Air Capture Processes at](https://doi.org/10.1021/acs.iecr.2c00681?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
Varying [Ambient](https://doi.org/10.1021/acs.iecr.2c00681?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as) Conditions. _Ind._ _Eng._ _Chem._ _Res._ 2022, _61_, 12649−
12667.
(61) Elfving, J.; Sainio, T. Kinetic approach to modelling CO2
adsorption from humid air [using](https://doi.org/10.1016/j.ces.2021.116885) amine-functionalized resin:
Equilibrium isotherms and column dynamics. _Chem._ _Eng._ _Sci._ 2021,
_246_, 116885.


**11653** [https://doi.org/10.1021/acs.iecr.4c01392](https://doi.org/10.1021/acs.iecr.4c01392?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
_Ind. Eng. Chem. Res._ 2024, 63, 11637−11653



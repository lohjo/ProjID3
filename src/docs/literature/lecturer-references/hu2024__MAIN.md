##### Journal of Water Process Engineering 59 (2024) 105065
Available online 29 February 2024
2214-7144/© 2024 Elsevier Ltd. All rights reserved.
A critical review of breakthrough models with analytical solutions in a
fixed-bed column
Qili Hu a,*, Xingyue Yang a, Leyi Huang a, Yixi Li a, Liting Hao b, Qiuming Pei c, Xiangjun Pei a,*
a State Environmental Protection Key Laboratory of Synergetic Control and Joint Remediation for Soil & Water Pollution, College of Ecology and Environment, Chengdu
University of Technology, Chengdu 610059, Chinab
Key Laboratory of Urban Stormwater System and Water Environment, Ministry of Education/Sino-Dutch R&D Centre for Future Wastewater Treatment Technologies,
Beijing University of Civil Engineering and Architecture, Beijing 100044, PR Chinac
Faculty of Geosciences and Environmental Engineering, Southwest Jiaotong University, Chengdu 611756, China
A R T I C L E I N F O
```
Editor: Xiaohong Guan
```
```
Keywords:
```
Adsorption
Fixed bed
Breakthrough curve
Fractal-like kinetics
Controversy
A B S T R A C T
The modeling and simulation of the breakthrough curves in a fixed-bed column play a vital role in evaluation of
the adsorption capability and prediction of the dynamic adsorption behaviors. With the popular use of the
breakthrough models, the relevant mistakes and inconsistencies also rise and are repeated in subsequent pub-
lications. This work conducts a profound review of the fundamental principles of continuous adsorption and the
underlying assumptions, curve characteristics, intrinsic relationships and application scope of the widely used
breakthrough models with analytical solutions. Besides, the physical meanings of the model parameters are
clarified, the relevant mistakes and controversies in the fixed-bed studies are addressed and the reasons for the
asymmetric breakthrough curves are discussed. Error statistics and residual plot are a good measure of the
```
goodness of fit. The F-test and Akaike’s information criterion (AIC) can be used to compare the fitting results
```
from two models for the same dataset. The fractal-like kinetics provides new insights into the diffusion-limited
adsorption process in a heterogeneous system. Some empirical breakthrough models are also considered to be an
alternative method to description of the dynamic adsorption behaviors. This review aims to help beginners better
understand and use the breakthrough models.
1. Introduction
Adsorption is a phase transfer process that means the enrichment of
chemical species on the surface of the porous adsorbents [1]. It has
become an indispensable unit operation to eliminate impurities or un-
desirable substances and recover compounds with high added value
from municipal and industrial wastewaters [2]. The engineered
adsorption processes more adopt the fixed bed rather than a batch
reactor since the former has greater advantages such as simple mode of
operation, efficient utilization of the adsorbent capacity, suitable
treatment of large volumes, and ease of scaling up [3–5]. Compared with
the traditional design-build-test approach, the design and optimization
of an adsorption system increasingly rely on the mathematical modeling
and simulation to save cost and time [6]. It is desirable to carry out the
mathematical modeling of mass transfer, chemical reaction and ther-
modynamic equilibrium during adsorption process [7]. The rigorous
prediction of the breakthrough curve contributes to understanding the
dynamic adsorption behaviors and transport properties and avoiding the
extensive experiments that tend to be expensive and time-consuming
[8]. The accuracy of prediction is related to the quality and availabil-
ity of the experimental data and to the underlying assumptions and
rational approximations of the mathematical models.
It is inherently difficult to develop a mathematical model to accu-
rately describe the dynamic adsorption behaviors in a fixed-bed column
because the concentration profiles are a function of both space and time
in the liquid and solid phases [9]. The phenomenological model estab-
lished by the mass balance has the potential to identify mechanisms
related to the mass transfer and the ability to make predictions outside of
the scope of evaluation for obtaining the model parameters [10].
Although more general and mathematically rigid, it requires compli-
cated numerical solutions [11]. Under initial and boundary conditions,
the complete analytical solution of partial differential equations
involved in phenomenological model is not available. If the goal is to
accurately predict the breakthrough behaviors in a fixed-bed column,
the use of simpler and more tractable models that avoid the need for
- Corresponding authors.
```
E-mail addresses: huqili@cdut.edu.cn (Q. Hu), peixj0119@tom.com (X. Pei).
```
Contents lists available at ScienceDirect
Journal of Water Process Engineering
journal homepage: www.elsevier.com/locate/jwpe
```
https://doi.org/10.1016/j.jwpe.2024.105065
```
```
Received 16 November 2023; Received in revised form 10 February 2024; Accepted 23 February 2024
```
```
Journal of Water Process Engineering 59 (2024) 105065
```
2
numerical solutions appears more suitable and logical [12]. Analytical
solutions can clearly present the dependence of the process on the
operating parameters in a way not possible with numerical solutions
[13]. To this end, it is desirable to develop simple mathematical models
to satisfactorily predict the dynamic adsorption behaviors. The
Bohart–Adams [14], Thomas [15], Yoon–Nelson [16] and Clark [17]
models are frequently applied for modeling of the breakthrough curves
since they have the simple analytical solutions and can be easily line-
arized, allowing their free parameters to be estimated by the linear
fitting [18]. Despite different underlying assumptions or empirical ap-
proximations, these mathematical models have achieved great success
in the modeling of the experimental data from adsorption of heavy
metals [19] and emerging contaminants such as antibiotics [20] and
microplastics [21].
However, with the popular propagation of these models, the relevant
problems also come along. The breakthrough models are blindly
selected to analyze the experimental data probably due to a lack of the
understanding of the fundamental principles of continuous adsorption
as well as the underlying assumptions, curve characteristics, intrinsic
relationships and application scope of the breakthrough models,
resulting in a poor fit or even incorrect conclusions [22,23]. The main
limitation of these models is the assumption of the time-independent
rate constant or transport properties, not interpreting the heteroge-
neous porous structures of the adsorbent and the changes in diffusive
microenvironments caused by the progressive occupation of the
adsorption sites by the adsorbate molecules [24]. Moreover, a major
difficult for the use of the breakthrough models is how to accurately
estimate the model parameters. A common way to evaluate the goodness
of fit is to adopt various error statistics such as the coefficient of deter-
```
mination (R2) [25], chi-squared value (χ2) [26] and root of mean
```
```
squared error (RMSE) [27]. But, these error statistics are not adequate
```
criteria but the residual plot [28]. The selection of an appropriate model
based on both error statistics and residual plot is relatively rare in fixed-
bed studies [29]. The fitting results from different models for the same
dataset have not been quantitatively compared yet. This work attempts
to address these problems and controversies to help beginners to better
understand the breakthrough models.
2. General description of fixed bed
Continuous adsorption is a non-stationary rate-controlled process in
a fixed-bed column, i.e. a time- and distance-dependent process [30].
The fixed bed is one of the basic forms of the dynamic operations in the
adsorption field. Compared with the batch operation, the main advan-
tage of the fixed-bed adsorption is to more conveniently scale up the
```
adsorption process by the dimensional similarity approach (i.e. geo-
```
```
metric and kinematic similitude). The fixed-bed adsorber through
```
scaling up can be applied to the treatment of municipal and industrial
wastewaters. The fixed-bed adsorption can provide reliable information
on the breakthrough time, loss of adsorption capacity during subsequent
cycles and acceptable flow rate [31]. However, it also faces some chal-
lenges such as high pressure drop, channeling effects, non-ideal flow
behaviors and mass-transfer resistances, limiting its application in
wastewater treatment [32].
As shown in Fig. 1, the adsorption process takes place when the
influent moves through the bed. The bed is divided into three regions:
```
saturation zone, mass-transfer zone (MTZ) and adsorption zone. In the
```
saturation zone, the adsorption of the contaminant reaches the dynamic
equilibrium at the solid/solution interface, where the amount adsorbed
q0 is in equilibrium with the influent concentration c0. The available
capacity of the adsorbent is exhausted and no mass transfer occurs from
solution to the adsorbent particles. In the adsorption zone, the adsorbent
particles are not loaded by the adsorbate molecules, and the concen-
tration of the contaminant is equal to zero. Adsorption occurs only in the
Nomenclature
```
a0 weight of solute uptake per unit volume of the bed (mg
```
```
L  1)
```
```
c0 concentration of the solute at the inlet of column (mg L  1)
```
```
cb effluent concentration at the breakthrough time (mg L  1)
```
```
ce concentration of the solute at equilibrium (mg L  1)
```
```
DL axial dispersion coefficient (cm2 min  1)
```
```
dp adsorbent particle diameter (cm)
```
```
kBA Bohart–Adams rate constant (L mg  1 min  1)
```
```
KF Freundlich constant (mg g  1 min  1/n)
```
```
Kf overall mass-transfer coefficient in the liquid phase (cm
```
```
min  1)
```
```
Kf a volumetric mass-transfer coefficient (min  1)
```
```
KL Langmuir constant (L  1 mg)
```
```
ks mass-transfer coefficient for solid phase (min  1)
```
```
kT Thomas rate constant (mL mg  1 min  1)
```
```
KT mass-transfer coefficient for liquid phase (min  1)
```
```
kYN Yoon–Nelson rate constant (min  1)
```
q0 equilibrium loading of the bed or adsorption capacity at
```
saturation (mg g  1)
```
```
qe amount of the solute uptake at equilibrium (mg g  1)
```
```
qmax maximum adsorption capacity (mg g  1)
```
```
qt amount of the solute uptake at time t (mg g  1)
```
```
t1/2 operating time at c/c0 = 0.5 (min)
```
```
tb breakthrough time (min)
```
```
ts saturation time (min)
```
```
Vbed volume of bed (L)
```
```
β0 external mass-transfer coefficient (min  1)
```
```
βa effective kinetic coefficient (min  1)
```
```
a mass-transfer area per unit volume of the bed (cm  1)
```
```
A0 fractal-like Clark rate constant (dimensionless)
```
```
c concentration of the solute at the outlet of column (mg L  1)
```
Dm molecular diffusivity calculated by the Stokes–Einstein
```
equation (cm2 min  1)
```
```
h fractal-like exponent (dimensionless)
```
k0 fractal-like rate constant
```
kn n-order Bohart–Adams rate constant (Ln mg  n min  1)
```
```
kBA,0 fractal-like Bohart–Adams rate constant (L mg  1 minh  1)
```
```
kT,0 fractal-like Thomas rate constant (mL mg  1 minh  1)
```
```
kYN,0 fractal-like Yoon–Nelson rate constant (minh  1)
```
```
m weight of the adsorbent in the bed (g)
```
```
n Freundlich constant (dimensionless)
```
p number of the model parameters
```
t operating time (min)
```
```
u flow rate per unit cross-sectional area of column (cm
```
```
min  1)
```
```
v flow rate (mL min  1)
```
```
V volume of the effluent at the outlet (mL)
```
```
vd linear velocity of movement of the adsorption zone (cm
```
```
min  1)
```
```
x bed height (cm) or relative concentration (x = c/c0)
```
```
z axial position of bed (cm)
```
```
ε void fraction of bed (dimensionless)
```
μ migration velocity of the concentration front in the bed
```
(cm min  1)
```
```
ρ bulk density of the bed (g L  1)
```
σa standard deviation of the position of the adsorption zone
```
front (cm)
```
```
τ operating time required to reach 50 % breakthrough (min)
```
Q. Hu et al.Journal of Water Process Engineering 59 (2024) 105065
3
MTZ, in which the adsorbent particles accumulate the adsorbate mole-
cules continuously from the feed and the amount adsorbed in the bed
increases from zero to q0. The shape and length of the MTZ largely
depend on the rate of adsorption and the shape of the isotherm curve
[33]. During the adsorption process, the MTZ travels through the bed
with a velocity that is much slower than the influent velocity. The
breakthrough occurs for the first time when the MTZ reaches the end of
the bed. The operating time required is called the breakthrough time
```
(tb). For a given flow rate, the better adsorbable the contaminant is, the
```
later the breakthrough occurs. In practice, the breakthrough time is
often defined as the operating time required to reach the minimum
detectable or maximum allowable concentration of the contaminant to
be removed [34]. As time goes on, the MTZ gradually moves forward,
while the saturation zone expands. Also, the concentration of the
contaminant rapidly rises at the outlet. The saturation is reached when
the entire MTZ leaves the column. At this moment, no net adsorption
takes place in the bed and the related time is known as the saturation
```
time (ts).
```
The profile of the relative concentration of a contaminant at the
outlet over time is called the breakthrough curve. The S-shaped break-
through curve is a consequence of the decrease in the driving force for
mass transfer from the fluid to the solid phase [35]. The breakthrough
curve is a mirror of the MTZ and also affected by the rate of adsorption
and the shape of the isotherm curve. To be specific, it is primarily
influenced by the operating parameters such as flow rate, influent
concentration, bed height, pH and particle size [36,37]. When the shape
of the breakthrough curve is as sharp as possible, the most effective
adsorption performance can be obtained [38]. The position of the
breakthrough curve at the t-axis depends on the moving velocity of the
MTZ, which in turn depends on the flow velocity and the strength of
adsorption. Given that the asymptotic properties of the breakthrough
models, they cannot exactly predict the breakthrough time and the
saturation time. The operating times at c/c0 = 0.05 and 0.95 are
popularly defined as the breakthrough time and the saturation time,
respectively [39].
A phenomenological model for adsorption of water contaminants is
```
developed according to the following assumptions [40–42]: (i)
```
```
isothermal condition; (ii) plug flow in the axial direction; (iii) negligible
```
```
radial dispersion; (iv) linear driving force for the solid adsorption; (v)
```
```
uniformly spherical adsorbent particles; and (vi) constant geometric
```
dimensions, interstitial velocity and void fraction. The mass balance
equation in the liquid phase is expressed as [43].
∂c
∂t + u
∂c
∂z +
1   ε
ε
∂qt
∂t = DL
∂2c
```
∂z2 (1)
```
The axial dispersion coefficient is estimated by the following eq.
[44].
```
DL = udp
```
```
(20
```
ε
Dm
udp+
1
2
```
)
```
```
(2)
```
The molecular diffusivity Dm can be calculated by the Sto-
kes–Einstein eq. [45]. A linear driving force model for the solid kinetics
is written as [46].
∂qt
```
∂t = ks(qe   qt) (3)
```
The mass-transfer processes in the solid phase include film diffusion,
intraparticle diffusion and adsorption on the active sites [10]. The
equilibrium data is analyzed by the Langmuir model, which is expressed
as
```
qe = qmax KLce1 + KLce(4)
```
The initial and boundary conditions are given as
```
t = 0; c = 0 q = 0 (5)
```
```
t = 0; z = 0 c = c0 (6)
```
```
t = 0; z = 0 ∂c∂z = uDL(ce   c) (7)
```
```
t = 0; z = x ∂c∂z = 0 (8)
```
The accurate estimation of the equilibrium loading is a precondition
for calculating other process parameters such as the removal efficiency
and length of the MTZ [47]. The equilibrium loading can be obtained by
integration of the measured breakthrough curve. As shown in Fig. 1, the
amount adsorbed at any time is numerically proportional to the area A
enclosed by the breakthrough curve, the vertical axis and the straight
line c/c0 = 1, which is expressed as [48].
```
qt = vc0A1000m = vc01000m
```
∫ t
0
```
(
```
1   cc0
```
)
```
```
dt (9)
```
The breakthrough and saturation capacities can be obtained when
Fig. 1. Schematic diagram of MTZ traveling through a fixed-bed column and the breakthrough curve.
Q. Hu et al.Journal of Water Process Engineering 59 (2024) 105065
4
the upper limits of integral are tb and ts , respectively. Other vital process
parameters can refer to Supplementary material.
3. Breakthrough models
The appropriate design of a fixed-bed adsorber requires the devel-
opment of a sound mathematical model to describe the dynamic
```
adsorption behaviors and predict the breakthrough curves [30]. Eq. (1)
```
is more general and mathematically rigid, but it requires complicated
numerical solutions. The breakthrough models with the simple analyt-
ical solutions receive increasing attention because they can provide the
sufficient fitting accuracy without the need for complex numerical so-
lutions [9]. However, the model parameters involved are empirical in a
sense, which are extremely sensitive to the process parameters such as
flow rate, initial solute concentration, adsorbent particle size, pH and
temperature. Thus, the practicality of these lumped parameters that
embed some operating features is limited to the range of the operating
conditions investigated [49]. In view of the complexity of the
phenomenological models, the use of simpler and more tractable models
appears more suitable and logical. For practical purposes, the selection
of an optimal model should obtain a compromise between the accuracy
of the process description and the effort for determining the model pa-
rameters [50].
3.1. Traditional breakthrough models
3.1.1. Bohart–Adams model
The Bohart–Adams model is initially used to describe the adsorption
of chlorine on the charcoal in a fixed-bed column. The adsorption pro-
cess is primarily controlled by the available active sites on the adsorbent
surface [51]. It provides a high fitting quality under different operating
conditions. The Bohart–Adams model assumes that the adsorption re-
action is not instantaneous but proportional to the residual adsorption
capacity of the adsorbent and the concentration of the target contami-
nant to be treated in the bulk solution, which is expressed as [14].
c
```
c0=
```
```
exp(kBAc0t)
```
exp
```
(k
```
BA a0 xu
```
)
```
- exp(kBAc0t)   1
```
(10)
```
The Bohart–Adams model has been successfully extended to
description of the adsorption of water contaminants [52,53]. In the
```
denominator of Eq. (10), the last term is entirely negligible except for
```
very small values of the first two exponential terms [54]. Thus, the
Bohart–Adams model can reduce to
c
```
c0=
```
1
1 + exp
[
kBAc0
```
(a
```
0 xuc0   t
```
) ] (11)
```
```
To facilely account for the rationality of this simplification, Eq. (10)
```
is rewritten as [55].
c
```
c0=
```
1
1 + exp
[
kBAc0
```
(
```
1kBA c0 ln
[
exp
```
(k
```
BA a0 xu
```
)
```
  1
]
  t
```
) ] (12)
```
```
Both 1kBA c0 ln[exp  kBA a0 xu)   1 ] and a0 xuc0 correspond to the operating time
```
```
required to reach half of the influent concentration (c/c0 = 0.5). One can
```
```
readily see that Eq. (11) and Eq. (12) are mathematically equivalent and
```
thereby provide the same fitted curves and error statistics. But, the
```
differences between the model parameters (kBA and a0) in Eq. (11) and
```
```
Eq. (12) are still uncertain. To address this confusion, according to the
```
L’Hˆopital’s rule [56], the following limit is acceptable.
limkBA →∞1kBAc0ln
[
exp
```
(kBAa0x
```
u
```
)
```
  1
]
```
= a0xuc0(13)
```
```
It is obvious that the term 1kBA c0 ln[exp  kBA a0 xu)   1 ] increases with the
```
increase in kBA and infinitely approaches a0 xuc0 . In general, it is desirable to
```
have larger rate of adsorption (kBA) and higher capacity of the adsorbent
```
```
(a0) for a given continuous system. This ensures that the difference be-
```
```
tween a0 xuc0 and 1kBA c0 ln[exp  kBA a0 xu)   1 ] is considerably small. As a result,
```
```
the simplification of Eq. (10) to Eq. (11) is rational. On the other hand, it
```
```
is debatable to regard the linear form of Eq. (11) as the bed depth service
```
```
time (BDST) model proposed by Hutchins [57] in many publications. By
```
comparison, it is found that the BDST model is only a rearranged form of
```
the Bohart–Adams model. Thus, Eq. (11) and its linear form should not
```
be called the BDST model in the future studies.
3.1.2. Thomas model
The Thomas model is one of the most widely used breakthrough
models, which can be used to estimate the rate constant and saturation
capacity for given operating conditions [58]. The derivation of the
```
Thomas model is based on the following assumptions [59,60]: (i) The
```
```
plug flow occurs in the bed with no axial dispersion; (ii) The rate of
```
```
adsorption is determined by chemical effects rather than diffusion; and
```
```
(iii) The adsorption process obeys the Langmuir adsorption kinetics. It is
```
theoretically appropriate to evaluate the adsorption process with
extremely small external and internal diffusion resistances [61]. The
Thomas model has a sound theoretical basis, which is expressed as [15].
c
```
c0=
```
1
1 + exp
[
kTc0
```
(q
```
0 mνc0   t
```
) ] (14)
```
In practice, the Thomas model is widely used for modeling of the
breakthrough curves regardless of linear or nonlinear isotherm involved
```
in a fixed-bed adsorption system [18]. Eq. (14) and Eq. (11) have the
```
same mathematical form. The dimensions of kT and kBA are consistent,
representing the second-order reaction rate constants. Let q0 mνc0 = a0 xuc0 , then
```
a0 = q0 mVbed (Vbed, volume of bed). Thus, the physical meaning of the
```
parameter a0 is the weight of solute uptake per unit volume of bed not
solution. It should be emphasized that it is unrealistic to assume reaction
kinetics as the only rate-determining step [62]. Nowadays, the mass
transfer-based models largely supersede reaction-based models because
the former is more practical. Even so, the Bohart–Adams and Thomas
models are still preferred by many researchers.
3.1.3. Yoon–Nelson model
The Yoon–Nelson model can accurately predict the breakthrough
curves in the entire range of time and the service life of the bed. It has
not only a simple mathematical form but also requires no detailed in-
formation on the characteristics of water contaminants of interest, type
of the adsorbent and physical properties of the bed [63]. The
Yoon–Nelson model assumes that the rate of decrease in the probability
of adsorption for each molecule is proportional to the probability of
adsorption and the probability of breakthrough, which is expressed as
[16].
c
```
c0=
```
1
```
1 + exp[kYN(τ   t) ] (15)
```
The rationale for this assumption is based on the observation that the
rate of change in the breakthrough concentration at a specific time is
proportional to the breakthrough concentration at the outlet and the
number of the active sites of the adsorbent particles in the bed [16].
According to the previous study [64], the Yoon–Nelson model is math-
ematically a logistic function, in which kYN determines the degree of
curvature of the breakthrough curve, while τ determines its location at
the t-axis. Compared with the Bohart–Adams and Thomas models, the
determination of the parameters kYN and τ does not need to consider any
operating conditions, which makes the curve fitting more convenient. In
addition, Yoon and Nelson further examine the effect of the influent
concentrations by introducing a new parameter a while keeping other
conditions unchanged. For a given value of c/c0, the effects of two
Q. Hu et al.Journal of Water Process Engineering 59 (2024) 105065
5
influent concentrations on the operating time and the weight of solute
```
adsorbed (wt, mg) are expressed as [65].
```
t1
```
t2=
```
```
(c0,2
```
c0,1
```
)a
```
```
; wt,2wt,1=
```
```
(c0,2
```
c0,1
```
)1  a
```
```
(16)
```
```
Note that Eq. (16) also provides a practical means of predicting the
```
values of tb and τ as well as we for various influent concentrations.
3.1.4. Clark model
The development of the Clark model is based on the use of a mass-
transfer concept in combination with the Freundlich isotherm [17].
The Clark model is initially employed to examine the adsorption per-
formance of granular activated carbon for removal of low concentra-
tions of organic compounds. Its underlying assumptions include that
```
[48,66]: (i) Ideal plug flow occurs in a fixed-bed column; (ii) The film
```
```
diffusion is the rate-controlling step; (iii) All solutes are removed at the
```
```
outlet of column; and (iv) The shape of the MTZ keeps unchanged. The
```
analytical solution of the Clark model is expressed as [17].
c
```
c0=
```
1
```
[1 + A⋅exp(   rt) ] 1n  1(17)
```
where
```
A =
```
```
(c0n  1
```
cbn  1   1
```
)
```
```
⋅exp(rtb) (18)
```
```
r = KTμu (n   1) (19)
```
The Freundlich isotherm in the Clark model is written as [67].
```
qe = KFce1n (20)
```
Strictly speaking, the values of the parameters KF and n are not
determined by batch experiments at equilibrium but column experi-
ments at saturation. That is, the saturation adsorption capacities q0 are
first obtained at different influent concentrations c0, and then the
```
Freundlich model is used to fit the experimental data (a plot of q0 versus
```
```
c0) by the nonlinear regression. However, it is highly unreasonable to
```
use the parameter n determined by batch experiments to analyze the
breakthrough data in some recent studies [68,69]. In our opinion, since
the Freundlich model is embedded in the Clark model, the parameter n
can be seen as an undetermined parameter during the curve fitting, so
that the fitting ability of the three-parameter Clark model will be
significantly improved. To facilely identify the curve characteristics of
```
the Clark model, Eq. (17) is rewritten as.
```
c
```
c0=
```
```
1{
```
1 + exp
[
r
```
(
```
1rlnA   t
```
) ] } 1n  1(21)
```
```
It can be clearly seen that Eq. (21) and Eq. (15) have similar math-
```
ematical forms and the Clark and Yoon–Nelson models are equivalent at
```
n = 2. Namely, the Bohart–Adams, Thomas and Yoon–Nelson models
```
can be regarded as special cases of the Clark model. Since n is an
adjustable parameter, the fitted curve provided by the Clark model is
always asymmetric except for n = 2. It is predicted that the Clark model
is superior to the Bohart–Adams, Thomas and Yoon–Nelson models in
terms of the fitting accuracy. Moreover, an obvious drawback of these
four models is that their relative concentration c/c0 is not equal to zero
at t = 0, probably resulting in a poor fit for some data points in the initial
stage of the breakthrough curves.
3.1.5. Wolborska model
The Wolborska model is originally used to describe p-nitrophenol
adsorption on activated carbon. Its underlying assumptions include that
```
[46,70]: (i) The low-concentration region is formed in a residence time;
```
```
(ii) The initial concentration distribution moves along the column at a
```
```
constant velocity; (iii) The width of the breakthrough curve is constant
```
```
in the low-concentration region; (iv) The low-concentration region is
```
```
characterized by the constant kinetic coefficients; and (v) The rate of
```
```
adsorption is controlled by the external mass transfer (i.e. film diffusion
```
```
and axial diffusion). The Wolborska model is derived by the mass bal-
```
```
ance equation (Eq. (1)) without considering void fraction of bed, which
```
is expressed as [71].
c
```
c0= exp
```
```
(βa c0
```
a0t  
βa
u x
```
)
```
```
(22)
```
where
```
βa = (u   μ)
```
2
2DL
[̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅
```
1 + 4β0DL(u   μ)2
```
√
  1
]
```
(23)
```
The effective kinetic coefficient βa reflects the effect of both axial
dispersion and external mass transfer [72]. The axial diffusion is negli-
gible for a low bed height or high flow rate, i.e. βa = β0 [73]. The first
```
term for the exponential term in Eq. (22) is not dimensionless because it
```
possesses a ratio of volumes of bed to solution [18]. To address this
problem, Wolborska and Pustelnik further propose the following eq.
[74].
c
```
c0= exp
```
```
(βa c0ε
```
ρq0t  
βa
u x
```
)
```
```
(24)
```
Unfortunately, the correct form of the Wolborska model still attracts
```
little attention [70,75]. It is worth noting that Eq. (22) and Eq. (24) are
```
mathematically an exponential function, which do not match the shape
of the complete breakthrough curve in the fixed-bed column [64].
```
Consequently, the characteristic parameters βa and a0 (or q0) do not
```
objectively reflect the performance of a fixed-bed column. The frequent
use of the Wolborska model to describe the breakthrough curves is
caused by the fact that its mathematical characteristics are ignored. In
practice, the Wolborska model works only at low concentrations. The
fitting ability of the Wolborska model for modeling of the complete
breakthrough curve is highly questioned. Thus, it is not recommended to
continue using the Wolborska model in the future studies.
3.1.6. Modified dose-response model
The Bohart–Adams, Thomas and Yoon–Nelson models have two
```
disadvantages: A symmetric breakthrough curve and a poor fit for initial
```
data points. Thus, a comparatively larger deviation may exist between
the fitted curves and the experimental data. Yan et al. develop the
modified dose-response model based on statistical analysis of the
experimental data [35]. This model can minimize the errors resulting
from the use of the Bohart–Adams, Thomas and Yoon–Nelson models,
especially at lower or higher time periods of the breakthrough curve
[76], which is written as
c
```
c0= 1  
```
1
1 +
```
(
```
Vb
```
)a (25)
```
The empirical parameter a determines the slope of the fitted curve,
while b represents the breakthrough volume reaching half a maximum
response, i.e. b = V at c/c0 = 0.5. The modified dose-response model can
provide an asymmetric S-shaped curve at a > 1 [64]. Its fitting quality is
often higher than the Bohart–Adams, Thomas and Yoon–Nelson models.
```
Yan et al. further find that the corresponding operating times are bν (by
```
```
definition of V = vt) and q0 mνc0 respectively at c/c0 = 0.5 for the modified
```
```
dose-response and Thomas models. Assuming that bν = q0 mνc0 (i.e. b = q0 mc0 ),
```
the modified dose-response model is rewritten as [35].
c
```
c0= 1  
```
1
1 +
```
( νc
```
0q0 m t
```
)a (26)
```
Q. Hu et al.Journal of Water Process Engineering 59 (2024) 105065
6
Since the Bohart–Adams, Thomas and Yoon–Nelson models are
```
mathematically equivalent (see below), the parameter b also meets b =νa0 x
```
```
uc0 = ντ. This approach seems reasonable, but it is actually controver-
```
sial. As shown in Fig. 2, two function curves of the modified dose-
```
response and Thomas models intersect at points (b/v, 0.5) or (q0 mνc0 , 0.5).
```
```
The area enclosed by three curves (respective function curves, the ver-
```
```
tical axis and the straight line c/c0 = 0.5) is not equal due to A2 ∕= A3. The
```
intersection of their function curves does not necessarily mean that their
```
parameters can be interchanged. Thus, Eq. (26) is not recommended to
```
fit the experimental data. The saturation capacity for the modified dose-
```
response model can be easily calculated by Eq. (9). Recently, Lee et al.
```
systematically compare the fitting performance of the above six models
and recommend the Bohart–Adams, Clark and modified dose-response
models for modeling of the breakthrough curves [77].
3.1.7. Klinkenberg model
It is very desirable to find a quick method to determine the model
parameters with a satisfactory accuracy. For practical purposes, extreme
```
accuracy in the solution of Eq. (1) is never required. In a fixed-bed
```
column, the exact solution of the equations describing transient mass-
transfer phenomena under given operating conditions can be approxi-
mated by an error function [78]. The Klinkenberg model assumes that
```
[79]: (i) The one-dimensional flow occurs in a fixed-bed column; (ii)
```
```
There is no axial diffusion in the direction of flow; and (iii) The rate of
```
mass transfer is proportional to the concentration gradient at the solid/
solution interface. An approximate analytical solution derived by Klin-
kenberg is expressed as [78].
c
```
c0=
```
1
2
[
1 + erf
```
(̅̅̅
```
τ√  ̅̅̅ ζ√ + 18̅̅̅ τ√ + 18̅̅̅ ζ√
```
) ]
```
```
(27)
```
where
```
ζ = Kf axu (28)
```
```
τ = Kf aK(1   ε)
```
```
(
```
t   εxu
```
)
```
```
(29)
```
```
The error function or probability integral erf(x) is expressed as.
```
```
erf (x) = 2̅̅̅π√
```
∫ x
0e
```
  u2du (30)
```
A comparison of exact and approximate values shows that the
```
relative concentration c/c0 has a maximum error of ±0.6 % (ζ = 2),
```
```
±0.2 % (ζ = 4) and ± 0.1 % (ζ = 8) for τ ≥ 1. The error approaches zero
```
with the further increase in ζ. It is not recommended to use the Klin-
```
kenberg model for ζ < 2 and τ < 1. According to Eq. (29), the Klin-
```
kenberg model is only applied to the cases where t > εx/u, may result in
a lack of some data points in the initial stage of the breakthrough curves.
Moreover, this work also corrects the improper expressions of the
dimensionless coefficients ζ and τ reported in the literature. Since the
error function is an odd function, the Klinkenberg model can provide a
symmetric breakthrough curve. It has been widely used to describe
adsorption of arsenic [80], hydrogen sulfide [81] and guaiacol [82]. To
our knowledge, the Bohart–Adams, Thomas and Yoon–Nelson models
are mathematically a logistic function, while the Klinkenberg model is
the error function. It is expected that two types of the models should
have similar fitting ability because of the symmetric properties. Their
main difference consists in the degree of curvature, which can be
reduced by adjusting the model parameters. Recently, Dima et al.
```
develop a simper model to analyze Cr(VI) adsorption on chitosan flakes
```
based on the error function, characterizing the breakthrough curve by
two parameters under the assumption of a normal distribution: linear
velocity of movement of the adsorption zone vd and standard deviation
of the position of the adsorption zone front σa , which is expressed as
[83].
c
```
c0=
```
1
2⋅
[
1 + erf
```
(vdt   x
```
̅̅̅2√ σa
```
) ]
```
```
(31)
```
3.1.8. Chern–Chien model
Based on the constant pattern concept of the wave propagation
theory, Chern and Chien develop a mathematical model to successfully
predict the breakthrough curves of p-nitrophenol adsorption on granular
```
activated carbon [84]. The Chern–Chien model assumes that [85]: (i) No
```
```
chemical reactions occur in the packed column; (ii) Only mass transfer
```
```
by convection is significant; (iii) Radial and axial dispersions are
```
```
negligible; (iv) The flow pattern is the ideal plug flow; (v) The temper-
```
```
ature in the column is uniform and invariant with time; (vi) The flow
```
```
rate is constant and invariant with the column position; and (vii) The
```
rate of adsorption is described by the linear driving force. When an
adsorption process follows the Langmuir isotherm, the Chern–Chien
model is expressed as [84].
```
t = t1/2 + ρq0εKf ac0
```
[
```
ln2x + 11 + KLc0ln 12(1   x)
```
]
```
(32)
```
Pan et al. derive another form of the Chern–Chien model when an
adsorption process obeys the Freundlich isotherm, which is expressed as
[86].
```
t = t1/2 + ρq0εKf ac0
```
[
ln2x   1n   1ln1   x
n  1
1   21  n
]
```
(33)
```
```
The volumetric mass-transfer coefficient (Kfa) is considered as an
```
undetermined parameter during the curve fitting. The Chern–Chien
model gives an excellent fit for prediction of the breakthrough curves in
recent studies [87–89]. However, the fitting results may deviate from
the real situation when the rate of adsorption is controlled by the
```
intraparticle diffusion. According to Eq. (32) and Eq. (33), the relative
```
concentration must meet 0 < c/c0 < 1 since the value of the logarithmic
term must be more than zero, meaning that some data points are left out
in the initial and final stages of the breakthrough curves during the curve
fitting. According to symmetry of function [90], it can be easily proved
```
that the function curves of Eq. (32) and Eq. (33) are symmetric if and
```
only if KL = 1/c0 and n = 2. Thus, the Chern–Chien model represents an
asymmetric S-shaped curve apart from the above special case.
```
This work attempts to solve the Chern–Chien model (Langmuir-type
```
```
and Freundlich-type) by OriginPro software. The experimental data
```
```
required are extracted from adsorption of Ni(II) [91] and methyl orangeFig. 2. Schematic diagram for comparison of Thomas and modified dose-response models.
```
Q. Hu et al.Journal of Water Process Engineering 59 (2024) 105065
7
[92] by Engauge Digitizer 12.1 software. The Chern–Chien model is
mathematically an implicit function and thus its curve fitting needs to
```
adopt the iteration algorithm of orthogonal distance regression (ODR).
```
In the iterative process, the ODR algorithm minimizes the sum of squares
of the orthogonal distances from the observed data to the fitted curve
rather than the deviations between the observed and predicted values
for the dependent variable [93]. Therefore, the error statistics do not
```
objectively reflect the goodness of fit of the Chern–Chien model (see
```
```
Table S1). As shown in Fig. 3, the fitted curves provided by two types of
```
the Chern–Chien model agree well with the experimental data. On the
whole, the Freundlich-type Chern–Chien model is superior to Langmuir-
type Chern–Chien model. This may be ascribed to the fact that the
Freundlich isotherm has the ability to describe the multilayer adsorption
on the heterogeneous surface [67]. It is observed from Table 1 that
process variables can significantly influence values of the model pa-
```
rameters (Kf a and t1/2).
```
Last but not least, the difference in the adsorption parameters exists
in the batch and fixed-bed operations [94,95]. In a batch reactor, the
mass-transfer driving force or rate of adsorption usually decreases due to
the continuous decrease in concentration during the adsorption process.
By contrast, the adsorbent particles are always in contact with the inlet
concentration in a fixed-bed adsorber, resulting in a high driving force
over the whole process [33]. For this reason, the parameters obtained in
batch experiments are not applicable to the fixed-bed system. The pa-
rameters KL and n in the Chern–Chien model should be determined by
the measured breakthrough data at saturation in the fixed-bed system.
Similar to the Clark model, the Chern–Chien model may be more
applicable if regarding KL and n as the unknown parameters during the
curve fitting.
3.2. Fractal-like breakthrough models
The classical rate equations for description of the dynamic evolution
of chemical processes contain time-independent rate constants and
transport properties [24]. Its implicit assumption is that the process
evolves in a well-stirred system with homogenous spatial distribution of
reactants. As a consequence, the classical reaction kinetics is not
applicable for the diffusion-limited heterogeneous processes, which are
found to be unsatisfactory when the reactants are spatially constrained
by either walls, phase boundaries or force fields on the microscopic level
[96]. The adsorbent particles are of high heterogeneity in a fixed-bed
column, which stems from the physical heterogeneity produced by the
```
surface with fractal-like geometries (i.e. porous adsorbents) and the
```
chemical heterogeneity caused by different functional groups present on
```
the adsorbent surfaces (different adsorption sites) [97]. A distinguishing
```
feature of heterogeneous reactions in fractal-like geometries is that the
```
Fig. 3. Breakthrough curves for adsorption of Ni(II) and methyl orange: (a) Langmuir-type Chern-Chien model, (b) Freundlich-type Chern-Chien model. (For
```
```
interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)
```
Q. Hu et al.Journal of Water Process Engineering 59 (2024) 105065
8
rate coefficient decreases with time [98]. The interplay of energetic and
geometric heterogeneities results in the fractal-like kinetics, which
provides new insights into the adsorption phenomena at the solid/so-
lution interface. According to the fractal-like kinetic theory, the rate
constant k of the classical reaction kinetics can be expressed by a time-
dependent rate constant, which is given as [96].
```
k = k0t  h (t ≥ 1, 0 ≤ h ≤ 1) (34)
```
Here, the parameter h is a heterogeneity parameter related to the
```
spectral dimension of fractal systems [99]. Eq. (34) is valid for diffusion
```
in homogeneous systems when h = 0. Compared with traditional
breakthrough models that focus only on the decrease in the driving
force, the fractal-like breakthrough models reflect the slowdown of the
process because the value of k decreases with time as the power law.
Haerifar and Azizian suppose that temporal variation of the rate coef-
```
ficient (fractal-like kinetics) during the adsorption process can be
```
explained by either the occurrence of available slower diffusion path-
ways for homogeneous surfaces or the progressive occupation of active
sites characterized by greater activation energies for heterogeneous
surfaces [100,101]. The first explanation implies that the rate coefficient
of desorption from a flat surface is time-independent [102]. The fractal-
like kinetics allows a more realistic understanding of the mechanisms
controlling the process evolution on a microscopic scale, which in turn is
a prerequisite for the reliable design of large-scale reactors [103]. In the
fixed-bed systems, the dynamic evolution of the adsorption space and
diffusion-limited heterogeneous processes create fundamental condi-
tions for the applicability of the fractal-like kinetics. The Bohart–Adams,
Thomas, Yoon–Nelson and Clark models are derived by constant rate
coefficient or mass-transfer coefficient, may lead to a poor fit in some
cases. The recent studies apply the fractal-like concept to these models,
leading to [1,97,104].
c
```
c0=
```
exp
```
(k
```
BA,0 c01  h t1  h
```
)
```
exp
```
(kBA,0 t  h a0 x
```
u
```
)
```
- exp
```
(kBA,0 c0
```
1  h t1  h
```
)
```
  1
```
(35)
```
c
```
c0=
```
1
1 + exp
```
(kT,0 t  h q0 m
```
ν   kT,0 c01  h t1  h
```
) (36)
```
c
```
c0=
```
1
1 + exp
[kYN,0
```
1  h (τ1  h   t1  h)
```
```
] (37)
```
c
```
c0=
```
1[
1 + A0⋅exp
```
(
```
  r1  ht1  h
```
) ] 1n  1(38)
```
The previous study has proved that the sum of the first two expo-
```
nential terms in the denominator of Eq. (35) is much >1 [104]. Thus, the
```
fractal-like Bohart–Adams can reduce to.
c
```
c0=
```
1
1 + exp
```
(k
```
BA t  h a0 xu   kBA,0 c01  h t1  h
```
) (39)
```
The above fractal-like breakthrough models can reduce to the cor-
responding Bohart–Adams, Thomas, Yoon–Nelson and Clark models at
```
h = 0. It is worth noting that Eq. (37) and Eq. (38) are mathematically
```
equivalent through simple transformations and other three fractal-like
breakthrough models also equivalent. The previous study reported
that the Bohart–Adams, Thomas and Yoon–Nelson models represented
the symmetric S-shaped curves [64], which deviate from the measured
breakthrough curves in most cases. By contrast, the fractal-like
Bohart–Adams, fractal-like Thomas and fractal-like Yoon–Nelson
models have the ability to describe the asymmetric breakthrough curve
at h ∕= 0. Thus, three fractal-like breakthrough models are more appli-
cable. Secondly, three fractal-like breakthrough models can better
describe the heterogeneity and complexity of the adsorbents because
they take into account the fractal structure of porous adsorbents.
Thirdly, three fractal-like breakthrough models consider the distribution
characteristics of permeability in porous adsorbents, which are capable
of describing the differences in permeability inside the adsorbent and is
conducive to predicting the mass-transfer steps more accurately. Finally,
the introduction of the hydrodynamic properties and fractal character-
istics of porous adsorbents makes three fractal-like breakthrough models
allow for a more comprehensive consideration of the effect of different
factors on the mass-transfer processes. In summary, the fractal-like ki-
netics provides a more realistic theoretical basis for the understanding of
the microscopic mechanisms dominating the process evolution, which is
in turn a prerequisite for the reliable design of large-scale fixed-bed
adsorbers.
3.3. Recent empirical breakthrough models
As mentioned above, the equilibrium loading for the single-solute
adsorption in the fixed-bed column is proportional to the area
enclosed by the vertical axis, the breakthrough curve and the straight
line c/c0 = 1. Also, the breakthrough time and the saturation time can be
easily obtained if a model is capable of predicting the breakthrough
curves well. Hence, these results provide a realistic basis for establish-
ment of the empirical breakthrough models. From a mathematical
perspective, a complete breakthrough curve can be divided into two
```
types: symmetric and asymmetric. Most often, it is asymmetric even for
```
the single-solute adsorption [105]. Blagojev et al. observe the asym-
```
metric breakthrough curves for Cu(II) adsorption on sugar beet shreds,
```
which are caused by the presence of two types of active sites on the
```
adsorbent surface [106]. Most likely, adsorption of Cu(II) on two types
```
of active sites occurs simultaneously, but the change in their dominance
appears with time in the whole adsorption process. Based on the two-
stage adsorption mechanism, the parallel sigmoidal model proposed in
their study is expressed as.
Table 1
```
Fitting results of the Chern-Chien model for adsorption of Ni(II) and methyl orange.
```
Contaminant ϕ
```
(cm)
```
m
```
(g)
```
x
```
(cm)
```
v
```
(mL min  1)
```
c0
```
(meq L  1)
```
ρ
```
(g L  1)
```
q0
```
(meq g  1)
```
ε KL
```
(L meq  1)
```
n Langmuir-type Freundlich-type
Kfa
```
(min¡1)
```
t1/2
```
(min)
```
Kfa
```
(min¡1)
```
t1/2
```
(min)
```
```
Ni(II) 2.8 8 30.5 2 2.14 41.359 1.468 0.875 0.46 1.46 0.057 2676 0.132 2537
```
4 2.11 41.361 1.350 0.870 0.089 1317 0.222 1210
Contaminant ϕ
```
(mm)
```
m
```
(g)
```
x
```
(cm)
```
v
```
(mL h  1)
```
c0
```
(mg L  1)
```
ρ
```
(g L  1)
```
q0
```
(mg g  1)
```
ε KL
```
(L mg  1)
```
n Langmuir-type Freundlich-type
Kfa
```
(h¡1)
```
t1/2
```
(h)
```
Kfa
```
(h¡1)
```
t1/2
```
(h)
```
Methyl orange 10 0.15 0.75 4.5 15 455 20.2 0.335 0.018 1.864 84.3 54.6 100.4 54.0
0.30 1.50 15 21.6 47.1 117.2 57.0 115.3
Q. Hu et al.Journal of Water Process Engineering 59 (2024) 105065
9
c
```
c0= p
```
⎡
⎢⎢
⎢⎣1   1
1 +
```
(
```
tτ1
```
)k1
```
⎤
⎥⎥
```
⎥⎦ + (1   p)
```
⎡
⎢⎢
⎢⎣1   1
1 +
```
(
```
tτ2
```
)k2
```
⎤
⎥⎥
```
⎥⎦ (40)
```
The parameter p reflects the proportion of each part in two-stage
adsorption mechanism. The parallel sigmoidal model is represented by
the superposition of two equations analogous to the modified dose-
```
response model. Eq. (40) can reduce to the modified dose-response
```
model when one of two-stage adsorption mechanisms controls the pro-
```
cess evolution (p = 0 or 1). The roles of the parameters ki and τi (i = 1,2)
```
are similar to that of a and b in the modified dose-response model. The
```
parallel sigmoidal model is also used to describe Cr(VI) adsorption on
```
```
three agricultural wastes (sugar beet shreds, poplar sawdust and wheat
```
```
straw) and shows perfect fitting performance under different operating
```
conditions [107]. Recently, some S-shaped functions are adopted to
establish the empirical breakthrough models by introducing two un-
known parameters. Hu et al. first propose three empirical breakthrough
models based on the logistic, hyperbolic tangent and double exponential
```
(Gompertz) functions, which are expressed as [108].
```
c
```
c0=
```
1
```
1 + exp[k(τ   t) ] (41)
```
c
```
c0=
```
1
```
2⋅{1 + tanh[k(t   τ) ] } (42)
```
c
```
c0= exp{   exp[k(τ   t) ] } (43)
```
Later, Chu also proposes an empirical breakthrough model based on
the Gompertz function, which is expressed as [109].
c
```
c0= exp[   exp(α   βt) ] (44)
```
```
It is evident that Eq. (43) and Eq. (44) are similar in mathematical
```
forms, but Chu does not explain the physical meanings of the empirical
```
parameters α and β. It is interesting to find that logistic (Eq. (41)) and
```
```
Yoon–Nelson (Eq. (15)) models are mathematically equivalent. Thus,
```
the parameters k and τ for the logistic, hyperbolic tangent and Gompertz
models can be also seen as the lumped parameters that determine the
degree of curvature of the breakthrough curve and its location at the t-
axis, respectively. In order to sufficiently express the subtle change in
the breakthrough curve, Hu et al. further define four characteristic pa-
rameters i.e. maximum specific breakthrough rate μmax, lag time λ, in-
flection point ti and half-operating time t50 [108]. In order to concisely
introduce this work, the modified breakthrough models can refer to our
previous studies [64,108] based on the parameters μmax and λ. In
addition, Hu et al. further propose two empirical breakthrough models
based on error and Gudermannian functions, which are expressed as
[29].
c
```
c0=
```
1
```
2⋅{1 + erf [k(t   τ) ] } (45)
```
c
```
c0=
```
1
2⋅
```
{
```
```
1 + 2π⋅arctan(sinh[k(t   τ) ] )
```
```
}
```
```
(46)
```
It should be emphasized that the above empirical breakthrough
models are obtained through appropriate transformation of the corre-
sponding mathematical functions. As a result, the Gompertz model
represents an asymmetric S-shaped curve. By contrast, the logistic, hy-
perbolic tangent, error and Gudermannian models represent a sym-
metric S-shaped curve and their main difference lies in degree of
curvature. In order to equip these four models with the ability to
describe the asymmetric penetration curve, the concept of fractal-kike
kinetics can be introduced. The physical meanings of k and τ for these
models are the rate constant and the time required to reach the inflection
point, respectively [29,108].
The Weibull distribution function is initially proposed to measure the
probability of failure of some technical indexes [110]. It has a simple
mathematical expression and satisfies the necessary general character-
istics of the breakthrough curve. Chu establishes an empirical break-
through model based on the appropriate form of the Weibull distribution
function, which is given as [111].
c
```
c0= 1   exp
```
[
 
```
(t
```
τ
```
)k ]
```
```
(47)
```
A distinct advantage of the Weibull model for modeling of the
breakthrough curves is that the relative concentration c/c0 = 0 at t = 0,
which can provide a higher fitting accuracy for description of the
breakthrough curves in the initial stage. Here, we analyze the curve
characteristics of the Weibull model. As shown in Fig. 4a, all curves pass
```
through one point (τ, 1–1/e) when the parameter k is adjusted. The
```
shape of the curve represented by the Weibull model depends on the
value of k. A convergent L-shaped curve occurs when 0 < k ≤ 1. By
contrast, an asymmetric S-shaped curve appears at k > 1 and its degree
of curvature will become larger with the increase in the value of k. As
shown in Fig. 4b, the value of the parameter τ can influence both degree
of curvature and shape of the S-shaped curve and it will become more
precipitous with the decrease in the value of τ. The adjustable parame-
ters k and τ in Weibull model make the S-shaped curve more diverse. It is
```
expected that Eq. (47) is capable of describing the dynamic adsorption
```
behaviors well in the fixed-bed column. To explore the breakthrough
```
rate, the first-order derivative of Eq. (47) is expressed as.
```
```
d(ct/c0)
```
```
dt =
```
```
k⋅t(k  1)
```
τk ⋅exp
[
 
```
(t
```
τ
```
)k ]
```
```
(48)
```
As shown in Fig. 4c and Fig. 4d, the breakthrough rate profiles
resemble the bell-shaped curve. The parameters k and τ for the Weibull
model jointly determine the position and amplitude of the rate profiles.
```
The rate profiles are also asymmetric and have an asymptote of d(ct /c0 )dt =
```
0 at t → ∞. These results will contribute to gaining insights into the rate
evolution in a fixed-bed column. The detail interpretation with respect
to the rate profiles can refer to our previous study [1].
Given that the Bohart–Adams, Thomas and Yoon–Nelson models give
a poor fit for modeling of the asymmetric breakthrough curve, Apir-
atikul and Chu modify these three models by a logarithmic trans-
formation to improve their fitting quality, which are expressed as [112].
c
```
c0=
```
1
1 + exp
[
kBAln
```
(a0 x
```
u
```
)
```
```
  kBAln(c0t)
```
```
] (49)
```
c
```
c0=
```
1
1 + exp
[
kTln
```
(q0 m
```
ν
```
)
```
```
  kTln(c0t)
```
```
] (50)
```
c
```
c0=
```
1
```
1 + exp[kYNln(τ)   kYNln(t) ] (51)
```
The above three modified models are capable of more accurately
predicting the breakthrough curves and providing reliable estimates for
the breakthrough time and the saturation time. These new models only
contain two undetermined parameters that appear in the original
models, providing an alternative strategy for modeling of the asym-
metric breakthrough curve due to the presence of the logarithmic term
that contains time t. Based on this idea, Chu and Hashim further propose
the log-Gompertz model [5] and the log-normal distribution [113],
which is expressed as.
c
```
c0= exp[   exp(α   βln(t) ) ] (52)
```
c
```
c0=
```
1
2⋅
```
{
```
1 + erf
```
[ln(t)   a
```
̅̅̅2√ b
```
] }
```
```
(53)
```
Q. Hu et al.Journal of Water Process Engineering 59 (2024) 105065
10
It should be noted that the logarithmic terms that contain time t in
```
Eqs. (49)–(53) keep dimensionless by introducing a set of variables/
```
parameters with a value of unity artificially. This modification is
```
meaningless in practice. In fact, the reason why Eqs. (49)–(53) have the
```
ability to describe the asymmetric breakthrough curve is because they
change the mathematical structure of the original models. To some
```
extent, Eqs. (49)–(51) lose their theoretical basis and the model pa-
```
rameters also lack the physical meanings. From a mathematical
perspective, the value of all logarithmic terms must be more than zero, i.
e. t > 1/c0 Eq. (49) and Eq. (50) or t > 1 for Eqs. (51)–(53). In this case,
the fitted curve may deviate from the breakthrough curves in the initial
stage of adsorption.
Recently, Singh et al. propose an empirical breakthrough model by a
combination of the Avrami equation with the breakthrough curves
characteristics, which is expressed as [114].
c
```
c0= 1   exp(   kt
```
```
n) (54)
```
One of its advantages is that the relative concentration c/c0 is also
equal to zero at t = 0. As shown in Fig. S2, the parameters k and n can
influence the degree of curvature and position of the curves simulta-
neously. The value of n determines the type of the function curve, rep-
resenting an asymmetric S-shaped curve at n > 1 and a L-shaped curve at
0 < n ≤ 1. Two adjustable parameters k and n make the curve fitting
```
more flexible. Thus, Eq. (54) may be expected to provide the high fitting
```
accuracy for description of many breakthrough curves.
4. Comprehensive evaluation of fitting quality
Although there are many mechanistic and empirical mathematical
models available for modeling of the breakthrough curves in a fixed-bed
column, their fitting quality is not sufficiently evaluated. In most fixed-
bed studies, the selection of the breakthrough models seems consider-
ably arbitrary when correlated with the experimental data. Recently,
Kimani compare the fitting performance of some breakthrough models
systematically based on the measured breakthrough data from bisphenol
A adsorption on polyaniline [115]. In general, a good fit requires that
the distribution of the experimental data should match the curve char-
acteristics of the breakthrough models well [43]. The fitting quality of
the breakthrough models can be visually evaluated by how close the
fitted curve is to the data points. If the curve fitting succeeds, a plot of
the predicted versus observed values will produce a straight line that
evenly passes through the data points [104]. In addition, error statistics
are also used to quantitatively assess the fitting quality of the break-
```
through models. The coefficient of determination (R2) is a good measure
```
of the goodness of fit, which is expressed as [25].
```
R2 = 1  
```
∑n
```
i=1 (yi   ´yi)2∑n
```
```
i=1 (yi   ӯi)2
```
```
(55)
```
where n is the number of the data points, yi is the observed value, ´yi is
the predicted value, ӯi is the mean value of all observed data.
The value of R2 close to 1 indicates that the fit is often a good one
Fig. 4. Curve characteristics of the Weibull model and its first-order derivative.
Q. Hu et al.Journal of Water Process Engineering 59 (2024) 105065
11
[116]. However, a larger value of R2 does not necessarily mean a better
fit since the degrees of freedom can influence R2. The value of R2 will rise
if more parameters are added to the models, but this does not imply a
better fit [67]. In addition, R2 is sensitive to extreme data points and also
influenced by the range of the independent variable [117]. The use of R2
is particularly inappropriate if the models are obtained by different
transformations of the response scale [118]. Sole reliance on R2 may fail
to reveal important data characteristics and model inadequacies. Thus,
R2 is not an adequate criterion for evaluation of the fitting quality. The
```
adjusted R2 (Adj. R2) overcomes these disadvantages and may be a
```
better metric, which is expressed as [119].
```
Adj.R2 = 1     1   R2)
```
```
(n   1
```
n   p
```
)
```
```
(56)
```
Obviously, Adj. R2 overcomes the problem of the rise in R2, espe-
cially for the dataset with a small sample size. Other frequently used
error statistics are summarized in Table S2. However, it is not sufficient
enough to evaluate the fitting quality by error statistics alone. The re-
sidual plot is a more reliable evaluation criterion than error statistics,
which is recommended to further diagnose the fitting results [120]. It
```
can be used to examine the underlying statistical assumptions (i.e.
```
constant variance, independence of variables and normality of the dis-
```
tribution) about residuals and provide valuable information on how to
```
improve the models. If the fitting quality is acceptable, all residuals
should tend to fall in a horizontal band centered around zero, showing
no systematic tendencies toward a clear pattern [28]. Statistically
speaking, rather than asking whether a particular fitting result is good, it
is more appropriate to compare two fitting results. Current studies lack
further analysis of the fitting results. In this work, the F-test and Akaike’s
```
information criterion (AIC) are used to compare the fitting results from
```
two models for the same dataset, which are expressed as [121,122].
```
F = (RSS1   RSS2)/(df1   df2)RSS2/df2(57)
```
```
AIC =
```
⎧⎪
⎪⎪⎨
⎪⎪⎪⎩
nln
```
(RSS
```
n
```
)
```
- 2p
```
(n
```
p ≥ 40
```
)
```
nln
```
(RSS
```
n
```
)
```
- 2p + 2p(p + 1)n   p   1
```
(n
```
p < 40
```
) (58)
```
where RRS denotes the residual sum of square, df is the degree of
freedom, the subscripts 1 and 2 correspond to the simple and complex
models, respectively.
The F-test and AIC are available to determine which model is the better
and thereby improve the predictive and explanatory abilities of the model.
The F-test assumes that two models are nested, where one model is a
simplified version of the other [123]. It takes advantage of the difference
in RSS of each fit to find out which model is the best. The F-test is
commonly used in linear regression or analysis of variance, which can
examine the significant differences between two nested models. The sig-
nificance of F-test consists in determining whether the regression co-
efficients in the model are significantly different and whether the model
itself is significant. The cumulative distribution function of the F-distri-
bution is assessed to yield a p value. If the p value is statistically significant
```
(p < 0.05), the fitting ability of the complex model is better than the
```
simpler model [122]. Otherwise, the complex model is rejected. The F-test
does not decide which model is correct and provides information on the
goodness of fit [123]. The objective of AIC is to find out a model that can
best interpret the experimental data but contain the fewest model pa-
rameters. AIC can provide robust and precise estimates based on
maximum likelihood to rank the models rather than concept of signifi-
cance [124]. AIC has a larger penalty for overfitting and thus helps to
avoid selecting overly complex models. The significance of AIC is to obtain
a compromise of the complexity of the estimated models and their good-
ness of fit. Compared with the F-test, AIC can compare nested or non-
nested models. Hence, any two models can be compared by AIC and the
one with a smaller value of AIC is suggested to be optimal. The Akaike’s
```
weight (WA) indicates the probability of a better model and can be used to
```
further confirm the optimal model, which can be expressed as [125].
```
WA = 11 + exp(0.5ΔAIC) (59)
```
where ΔAIC is the difference between the AIC values of one model and
the best model.
Taking the Bohart–Adams and fractal-like Bohart–Adams models as an
example, this work aims to compare the fitting results of ciprofloxacin
[126] and phenol and p-nitrophenol [86] adsorption by using OriginPro
software. The F-test and AIC can be obtained by the following procedures.
Step 1: perform the curve fitting twice by the Bohart–Adams and fractal-
like Bohart–Adams models for the same dataset and create two fitting
reports automatically. Step 2: select Analysis → Fitting → Compare
Model from the Origin menu, and then open Fitting: fitcmpmodel dialog
box. Step 3: specify the way to recalculate and update the result, fitting
```
results, comparison method, fit parameters, fit statistics, and click OK (see
```
```
Fig. S1). The results of model comparison will show in the Book dialog
```
box. As shown in Fig. 5, the breakthrough curve of ciprofloxacin adsorp-
tion shows an asymmetric distribution. Compared with the Bohart–Adams
model, the fitted curve provided by the fractal-like Bohart–Adams model is
more consistent with the experimental data. Its predicted values are very
close to the observed values. The corresponding residuals fluctuate
randomly in the vicinity of zero and fall in a narrow horizontal band. It is
observed from Table 2 that the values of RSS, reduced χ2 and RMSE are
smaller and that R2 and Adj. R2 are larger for the fractal-like
Bohart–Adams model. The p value for F-test is <0.05, indicating that
this comparison is significant. The value of AIC is also smaller and its
weight almost approaches unity for the fractal-like Bohart–Adams model.
Consequently, ciprofloxacin adsorption follows the fractal-like
Bohart–Adams model. By contrast, the breakthrough curves of phenol
and p-nitrophenol adsorption show a symmetric distribution. Thus, the
Bohart–Adams and fractal-like Bohart–Adams models have comparable
fitting abilities and the fitted curves are almost coincident. The fractal-like
Bohart–Adams model is superior to the Bohart–Adams model in terms of
various error statistics for phenol adsorption. It is worth noting that all
error values were fairly close for p-nitrophenol adsorption. In this case,
error statistics are not sufficient enough to evaluate the fitting quality. The
F-test and AIC are particularly important for further diagnosis of the fitting
results. One can readily see that the p value for F-test is much more than
0.05. The Bohart–Adams model has smaller value of AIC and larger value
of WA. This case indicates that a model with more parameters does not
necessarily mean a better fit.
5. Existing problems
5.1. Data quality
High quality of the experimental data is a prerequisite for obtaining a
good fit. In many cases, the data quality is purposely or unconsciously
neglected when the theoretical models are used to analyze the break-
through curves. The poor data quality is not conducive to the accurate
prediction of the model parameters and insights into the dynamic
adsorption behaviors in a fixed-bed column. To our knowledge, the
```
relevant situations mainly include that: (i) Many studies lack the
```
```
indispensable repeated experiments (no error bars); (ii) The measured
```
```
breakthrough curves are not complete (not S-shaped) [48]; (iii) The data
```
```
points fluctuate greatly [127]; and (iv) The breakthrough curves inter-
```
sect under different experimental conditions [128]. In our opinion, the
first two cases can be easily solved by the standardized operation pro-
cedures. The reason why the latter two cases exist is that the hydration
```
process (volume expansion) occurs when the adsorbent is in contact
```
with the influent or the dominant mass-transfer and reaction mecha-
nisms change during the adsorption process.
Q. Hu et al.Journal of Water Process Engineering 59 (2024) 105065
12
5.2. Partial and complete breakthrough curves
Since it is often a tedious and time-consuming work for obtaining the
complete breakthrough curve, some studies focus more on how many
bed volumes are required for breakthrough to occur [129]. Although the
partial breakthrough curve can be obtained in a relatively short time, the
completeness of the experimental data can directly influence the model
parameters to be estimated. Besides, the partial breakthrough curve does
not profoundly reveal the dynamic adsorption behaviors in a fixed-bed
```
column. Taking the Thomas model (Eq. (14)) as an example, this work
```
examines the fitting results of the partial and complete breakthrough
curves from adsorption of methylene blue [37]. As shown in Fig. 6, the
fitted curves provided by the Thomas model agree well with the partial
and complete breakthrough curves at different influent concentrations
and an error statistic Adj. R2 is >0.99 in all cases. The fitting results of
other partial breakthrough curves refer to Fig. S3. However, there are
significant differences in kT and q0 obtained from the partial and com-
plete breakthrough curves. As shown in Table 3, compared with the
complete breakthrough curves, the maximum relative errors of kT are
110.8 %, 26.1 % and 47.5 % respectively at 50, 100 and 150 mg L  1,
while the corresponding maximum relative errors of q0 are   20.5 %,
  4.0 % and   13.4 %. In general, the curve fitting aims to purely
```
Fig. 5. Comparison of Bohart–Adams and fractal-like Bohart–Adams models: (a) fitted curves, (b) predicted versus observed values and (c) residual plot.
```
Q. Hu et al.Journal of Water Process Engineering 59 (2024) 105065
13
Table 2
Fitting results of ciprofloxacin, phenol and p-nitrophenol adsorption with Bohart–Adams and fractal-like Bohart–Adams models.
Parameters and
error statistics
Ciprofloxacina Parameters and
error statistics
Phenolb Parameters and
error statistics
p-Nitrophenolb
Bohart–Adams Fractal-like
Bohart–Adams
Bohart–Adams Fractal-like
Bohart–Adams
Bohart–Adams Fractal-like
Bohart–Adams
```
kBA (L mg min  1) 4.03 × 10  4   kBA (L mmol h  1) 0.113   kBA (L mmol h  1) 8.64 × 10  2  
```
```
kBA,0 (L mg
```
```
minh  1)
```
```
  1.17 × 10  3 kBA,0 (L mmol
```
```
hh  1)
```
```
  0.222 kBA,0 (L mmol
```
```
hh  1)
```
  9.85 × 10  2
```
a0 (mg L  1) 669 1245 a0 (mmol L  1) 594 1023 a0 (mmol L  1) 882 936
```
h   0.487 h   0.422 h   5.82 × 10  2
RRS 2.76 × 10  2 2.47 × 10  3 RRS 4.54 × 10  3 1.52 × 10  3 RRS 1.75 × 10  3 1.77 × 10  3
Reduced χ2 1.62 × 10  3 1.55 × 10  4 Reduced χ2 8.56 × 10  5 2.92 × 10  5 Reduced χ2 5.16 × 10  5 5.38 × 10  5
R2 0.9890 0.9990 R2 0.9995 0.9998 R2 0.9997 0.9997
Adj. R2 0.9883 0.9989 Adj. R2 0.9995 0.9998 Adj. R2 0.9997 0.9997
RMSE 4.03 × 10  2 1.24 × 10  2 RMSE 9.25 × 10  3 5.41 × 10  3 RMSE 7.18 × 10  3 7.33 × 10  3
```
F-test 162.5 (p = 8.55 × 10  10 < 0.05) F-test 103.2 (p = 6.03 × 10  14 < 0.05) F-test 0.413 (p = 0.525 > 0.05)
```
AIC   116.6   159.1 AIC   510.7   568.5 AIC   350.7   347.7
WA 5.71 × 10  10 1.000 WA 2.80 × 10  13 1.000 WA 0.817 0.183
a operating conditions of c0 = 225 mg L  1, u = 1.91 mL min, x = 25 cm.
b operating conditions of c0 = 5.32 mmol L  1, u = 34.9 mL h  1, x = 5.71 cm.
```
Fig. 6. Complete and partial breakthrough curves of methylene blue adsorption with the Thomas model: (a) 100 %, (b) 80 %, (c) 50 % and (d) 20 %. (For inter-
```
```
pretation of the references to color in this figure legend, the reader is referred to the web version of this article.)
```
Q. Hu et al.Journal of Water Process Engineering 59 (2024) 105065
14
minimize the deviations between the fitted curves and the data points
when a mathematical model is used to analyze the breakthrough curves,
ignoring the physical meanings of the model parameters. As a conse-
quence, the model parameters obtained from the partial breakthrough
curves are not applied to the design and optimization of the fixed-bed
adsorber. On the whole, the complete breakthrough curves are recom-
mended to obtain the model parameters.
5.3. Oversimplification of Bohart–Adams model
In addition to two forms of the Bohart–Adams model mentioned
above, an oversimplified form of the Bohart–Adams model frequently
appears in the recent literature, which is expressed as [130].
c
```
c0= exp
```
```
(
```
kBAc0t   kBAa0xu
```
)
```
```
(60)
```
```
The simplification of Eq. (11) to Eq. (60) is completely unreasonable.
```
```
From a mathematical point of view, Eq. (60) is an exponential function
```
rather than a logistic function through oversimplification of the Bohart-
Adams model, which covers up the functionality of the original Bohart-
Adams model and greatly weakens the ability to describe the break-
```
through curve [131]. By comparing Eq. (22), Eq. (24) and Eq. (60), it is
```
found that the Wolborska and oversimplified Bohart–Adams models are
equivalent in mathematical nature, i.e. kBA = βaa0 or βa ερq0 . The fitted curve
```
provided by Eq. (60) seriously deviates from the complete breakthrough
```
curve, especially at larger values of t. For this reason, the fitting ability of
```
Eq. (60) is also increasingly questioned. A poor fit is bound to result in
```
the inaccurate estimation of the model parameters, which is detrimental
to understanding the dynamic adsorption behaviors and optimizing the
design of the adsorber [54]. In our opinion, the exponential term exp[
kBAc0
```
(a0 x
```
uc0   t
```
) ]
```
```
in Eq. (11) contains the independent valuable t, whose
```
value decreases with the increase in t. This exponential term will be
much <1 when the value of t is sufficiently large. In this case, the unity
```
term is not neglected in the denominator of Eq. (11). Hence, the use of
```
```
Eq. (60) should be avoided in the future studies. In order to generalize
```
the Bohart–Adams model and enable it to describe the asymmetric
breakthrough curve, Hu et al. derive the n-order Bohart–Adams model,
which is expressed as [104].
c
```
c0=
```
⎡
⎢⎢
⎢⎣1 + na01  nc0n  1
⎛
⎜⎜
⎜⎝
⎡
⎢⎢
⎣
```
1 + (n   1) kna0c0
```
n  1 x
u
```
1 + (n   1)kna0n  1 c0t
```
⎤
⎥⎥
⎦
1
n   1
 
[ 1
```
1 + (n   1)kna0n  1c0t
```
] 1
n   1
⎞
⎟⎟
⎟⎠
⎤
⎥⎥
⎥⎦
```
 1n(61)
```
5.4. Equivalent models
In some recent papers [132,133], the Bohart–Adams, Thomas and
```
Yoon–Nelson models show different fitting results (fitted curves and
```
```
error values) when used to analyze the breakthrough curves. In other
```
words, these three models are assumed to be separate and independent.
To our knowledge, A lack of the understanding of their intrinsic math-
ematical relationships can account for the further propagation of such a
mistake. The previous study has demonstrated that these three models
were mathematically a logistic function that represents a symmetric S-
shaped curve and their parameters are interchangeable, which are
expressed as [1].
```
kYN = kBAc0 = kTc0 (62)
```
```
τ = a0xuc0= q0mνc0(63)
```
Hence, the Bohart–Adams, Thomas and Yoon–Nelson models are
equivalent. Their fitted curves should be coincident and all error values
are equal when the curve fitting is carried out for the same set of the
experimental data. The above relationships reveal the absurd behaviors
of treating these three models as independent models and comparing
their respective fitting abilities based on various error statistics. Ac-
```
cording to Eq. (62), the parameters kBA and kT are regarded as the
```
second-order reaction rate constants. Similar to the parameter τ, the
physical meanings of the terms a0 xuc0 and q0 mνc0 represent the operating time
```
required to reach 50 % breakthrough [64]. According to Eq. (62) and Eq.
```
```
(63), the determination of kBA, kT, a0 and q0 avoids the repeated curve
```
fitting. The revelation of intrinsic relationships between the
Bohart–Adams, Thomas and Yoon–Nelson models will contribute to
precisely obtaining the model parameters and better understanding the
dynamic adsorption behaviors in a fixed-bed column. Just as the roles of
```
kYN and τ, the terms kBAc0 (kTc0) and a0 xuc0
```
```
(q0 m
```
νc0
```
)
```
determine the degree of
curvature of the breakthrough curve and its location at the t-axis,
respectively. The values of kYN and τ depend on the operating conditions
and to some extent may be regarded as the lumped parameters that
embed some physical processes and operating features. From a mathe-
matical perspective, the same breakthrough curve is obtained regardless
of the process parameters only if the value of the terms a0 xuc0 and q0 mνc0 keeps
constant.
5.5. Linear and nonlinear curve fitting
The accurate calculation of the model parameters plays an important
role in evaluation the separation efficiency of the contaminant and
identification of its mass-transfer law [134]. The values of the model
parameters are affected by the regression method. Although it is highly
questioned, the linear fitting is still frequently adopted by many re-
searchers. The linearization of a model requires the corresponding
Table 3
Fitting results for complete and partial breakthrough curves of methylene blue adsorption at different concentrations.
c/c0 50 mg L  1 100 mg L  1 150 mg L  1
kT
```
(L mg¡1 min¡1)
```
q0
```
(mg g¡1)
```
Adj. R2 kT
```
(L mg¡1 min¡1)
```
q0
```
(mg g¡1)
```
Adj. R2 kT
```
(L mg¡1 min¡1)
```
q0
```
(mg g¡1)
```
Adj. R2
1.0 1.39 × 10¡3 52.20 0.9977 1.19 × 10¡3 73.42 0.9978 1.18 × 10¡3 83.55 0.9984
0.9 1.40 × 10¡3 52.16 0.9957 1.23 × 10¡3 73.28 0.9975 1.14 × 10¡3 83.73 0.9966
0.8 1.48 × 10¡3 51.80 0.9959 1.29 × 10¡3 73.02 0.9977 1.06 × 10¡3 84.42 0.9980
0.7 1.57 × 10¡3 51.28 0.9970 1.33 × 10¡3 72.72 0.9978 1.06 × 10¡3 84.42 0.9980
0.6 1.60 × 10¡3 51.12 0.9961 1.40 × 10¡3 72.25 0.9978 1.12 × 10¡3 83.64 0.9974
0.5 1.62 × 10¡3 51.00 0.9941 1.50 × 10¡3 71.37 0.9979 1.12 × 10¡3 83.64 0.9974
0.4 1.67 × 10¡3 50.61 0.9914 1.50 × 10¡3 71.37 0.9979 1.24 × 10¡3 81.67 0.9978
0.3 1.66 × 10¡3 50.70 0.9842 1.40 × 10¡3 72.55 0.9958 1.24 × 10¡3 81.67 0.9978
0.2 2.11 × 10¡3 46.70 0.9826 1.33 × 10¡3 73.90 0.9872 1.35 × 10¡3 79.57 0.9933
0.1 2.93 × 10¡3 41.48 0.9654 1.48 × 10¡3 70.50 0.9681 1.74 × 10¡3 72.36 0.9962
Q. Hu et al.Journal of Water Process Engineering 59 (2024) 105065
15
transformation of the measured experimental data. The linearized
treatment implicitly alters their error structure and may also violate the
error variance and normality assumptions of standard least squares
[135]. As a consequence, different linearized forms of a model may
result in different estimates of the undetermined parameters [136]. In
addition, the linearized treatment may cause arbitrary exclusion of
certain data points from the estimated model for calculation as these
data points are not in the domain of definition of the linearized equa-
tions. For instance, a linearized form of the Thomas model is expressed
as.
ln
```
(c0
```
c   1
```
)
```
```
= kTq0mν   kTc0t (64)
```
It is universally acknowledged that the domain of definition of the
logarithmic function is always more than zero and the bottom number of
```
the power functions is not equal to zero. According to Eq. (64), one can
```
get 0 < c < c0 or 0 < c/c0 < 1. When the Thomas model is used to fit the
experimental data, the linearized treatment excludes data points at c =
```
0 and c = c0 . A new dependent variable ln  c0c   1) is produced after
```
linearization and its values may not be sufficiently accurate during the
calculation process using the measured data. The linearization of a
breakthrough model also results in the statistical bias. The error in-
```
creases dramatically when the value of the logarithmic term in Eq. (64)
```
is very close to its limit, especially for the breakthrough curve before
breakthrough point and after saturation point [131]. Besides, the im-
```
precisions of slope and intercept obtained from Eq. (64) may also be
```
incorporated into the model parameters during the curve fitting. Last but
not least, the linear fitting fails to examine more complex models that
may be in better agreement with the experimental data. The nonlinear
fitting is a versatile way to obtain the model parameters without any
transformation [137]. It not only overcomes the existing disadvantages
of the linear fitting, but also can solve the models with multiple pa-
rameters. The nonlinear fitting can provide a more robust and reliable
parameter estimation than the linear fitting.
5.6. Reasons for asymmetric breakthrough curve
The breakthrough behaviors in a fixed-bed column are subject to the
operating parameters, geometric dimensions of the column, types of the
contaminants and physicochemical properties of the adsorbent. It is
reported that the complete breakthrough curve is usually asymmetric S-
shaped even for the single-solute adsorption [105]. When the solution
containing a solute with a high affinity is fed into the fixed-bed column
at high concentrations, the breakthrough curve first shows a sharp rise
and then a slow approach to saturation. Such early breakthrough and
tailing are caused by the slow surface diffusion [138]. If the intraparticle
diffusion controls the adsorption kinetics, as it is often the case in
practice, the breakthrough curve is asymmetric with a long tailing [33].
Moreover, an asymmetric breakthrough curve may be also attributed to
the fact that the adsorbent contains two or more constituents of unequal
reactivity or the rate of adsorption falls off more rapidly than the re-
sidual capacity of the adsorbent [14]. Thus, the measured breakthrough
curves are asymmetric in most cases, which account for a relatively poor
fit for the Bohart–Adams, Thomas and Yoon–Nelson models.
6. Concluding remarks
The mathematical modeling of the breakthrough curves is a practi-
cally indispensable link for the design and optimization of a fixed-bed
reactor. However, the traditional breakthrough models are not appli-
cable for the diffusion-limited heterogeneous processes due to their
implicit assumptions of time-independent rate constants and transport
properties. The fractal-like theory provides new insights into the dy-
namic adsorption behaviors and allows to understand the mechanisms
controlling the process evolution deeply on a microscopic scale.
Furthermore, based on the similarity of the breakthrough curves and
some S-shaped function curves, the empirical breakthrough models
developed have been an alternative strategy for modeling of the
measured breakthrough curves. In most cases, the complete break-
through curves are asymmetric S-shaped even for the single-solute
adsorption. During the curve fitting, high quality of the experimental
data is the first step to obtaining a good fit. The selection of an appro-
priate mathematical model for prediction of the breakthrough curves
requires not only taking into account its underlying assumptions, curve
characteristics and application scope, but also allowing for data quality,
fitting methods, error statistics and residual plot. F-test and AIC can be
used to compare the fitting results of two breakthrough models for the
same dataset, but the former requires the two models must be nested.
The breakthrough models with asymmetric properties usually have
higher fitting quality. The partial breakthrough curves result in the
inaccurate estimation of the model parameters. The Bohart–Adams,
Thomas and Yoon–Nelson models are mathematically equivalent and
their parameters are interchangeable. The Wolborska and over-
simplified Bohart–Adams models are mathematically an exponential
function, which are not applicable for prediction of the complete
breakthrough curves. The fitting quality of the Chern–Chien model can
be evaluated by the residual plot rather than error statistics since it
adopts the iteration algorithm of ODR. This review is expected to help
readers better understand and use the breakthrough models with simple
analytical solutions and avoid the further propagation of some existing
mistakes and inconsistencies in the future studies.
CRediT authorship contribution statement
Qili Hu: Writing – original draft, Validation, Methodology, Investi-
gation, Conceptualization. Xingyue Yang: Validation, Formal analysis,
Data curation. Leyi Huang: Validation, Software, Data curation. Yixi Li:
Validation, Software, Formal analysis. Liting Hao: Validation, Funding
acquisition, Data curation. Qiuming Pei: Software, Formal analysis,
Data curation. Xiangjun Pei: Writing – review & editing, Supervision,
Project administration.
Declaration of competing interest
The authors declare that they have no known competing financial
interests or personal relationships that could have appeared to influence
the work reported in this paper.
Data availability
Data will be made available on request.
Acknowledgements
This work was supported by National Key R&D Program of China
```
(2023YFC3007103) and Key Research and Development Programme of
```
```
Sichuan Province (No. 2021YFQ0066).
```
Appendix A. Supplementary data
Supplementary data to this article can be found online at https://doi.
org/10.1016/j.jwpe.2024.105065.
References
```
[1] Q. Hu, Y. Xie, C. Feng, Z. Zhang, Fractal-like kinetics of adsorption onheterogeneous surfaces in the fixed-bed column, Chem. Eng. J. 358 (2019)
```
1471–1478.[2] S. Aguirre-Contreras, R. Leyva-Ramos, R. Ocampo-P´erez, C.G. Aguilar-Madera, J.
V. Flores-Cano, N.A. Medellín-Castillo, Mathematical modeling of breakthroughcurves for 8-hydroxyquinoline removal from fundamental equilibrium and
```
adsorption rate studies, J. Water Process. Eng. 54 (2023) 103967.
```
Q. Hu et al.Journal of Water Process Engineering 59 (2024) 105065
16
[3] D. Juela, M. Vera, C. Cruzat, X. Alvarez, E. Vanegas, Mathematical modeling andnumerical simulation of sulfamethoxazole adsorption onto sugarcane bagasse in a
```
fixed-bed column, Chemosphere 280 (2021) 130687.[4] R. Antonelli, G.R.P. Malpass, M.G.C. da Silva, M.G.A. Vieira, Fixed-bed
```
```
adsorption of ciprofloxacin onto bentonite clay: characterization, mathematicalmodeling, and DFT-based calculations, Ind. Eng. Chem. Res. 60 (2021)
```
4030–4040.[5] K.H. Chu, M.A. Hashim, Removal of antibiotics through fixed bed adsorption:
```
comparison of different breakthrough curve models, J. Water Process. Eng. 56(2023) 104512.
```
[6] K.N. Son, J.A. Weibel, J.C. Knox, S.V. Garimella, Limitations of the axiallydispersed plug-flow model in predicting breakthrough in confined geometries,
```
Ind. Eng. Chem. Res. 58 (2019) 3853–3866.[7] A. Bringas, E. Bringas, R. Iba˜nez, M.F. San-Rom´an, Fixed-bed columns
```
```
mathematical modeling for selective nickel and copper recovery from industrialspent acids by chelating resins, Sep. Purif. Technol. 313 (2023) 123457.
```
[8] X. Lin, Q. Huang, G. Qi, S. Shi, L. Xiong, C. Huang, X. Chen, H. Li, X. Chen,Estimation of fixed-bed column parameters and mathematical modeling of
```
breakthrough behaviors for adsorption of levulinic acid from aqueous solutionusing SY-01 resin, Sep. Purif. Technol. 174 (2017) 222–231.
```
[9] K.L. Tan, B.H. Hameed, Insight into the adsorption kinetics models for theremoval of contaminants from aqueous solutions, J. Taiwan Inst. Chem. Eng. 74
```
(2017) 25–48.[10] P.Y.R. Suzaki, M.T. Munaro, C.C. Triques, S.J. Kleinübing, M.R. Fagundes Klen,
```
R. Bergamasco, L.M. de Matos Jorge, Phenomenological mathematical modelingof heavy metal biosorption in fixed-bed columns, Chem. Eng. J. 326 (2017)
389–400.[11] D.S.P. Franco, J.L.S. Fagundes, J. Georgin, N.P.G. Salau, G.L. Dotto, A mass
```
transfer study considering intraparticle diffusion and axial dispersion for fixed-bed adsorption of crystal violet on pecan pericarp (Carya illinoensis), Chem. Eng.
```
J. 397 (2020) 125423.[12] O. Hamdaoui, Removal of copper(II) from aqueous phase by Purolite C100-MB
```
cation exchange resin in fixed bed columns: modeling, J. Hazard. Mater. 161(2009) 737–746.
```
```
[13] T.G. Myers, A. Cabrera-Codony, A. Valverde, On the development of a consistentmathematical model for adsorption in a packed column (and why standard
```
```
models fail), Int. J. Heat Mass Transf. 202 (2023) 123660.[14] G.S. Bohart, E.Q. Adams, Some aspects of the behavior of charcoal with respect to
```
```
chlorine, J. Am. Chem. Soc. 42 (1920) 523–544.[15] H.C. Thomas, Chromatography: a problem in kinetics, Ann. NY Acad. Sci. 49
```
```
(1948) 161–182.[16] Y.H. Yoon, J.H. Nelson, Application of gas adsorption kinetics I. A theoretical
```
```
model for respirator cartridge service life, Am. Ind. Hyg. Assoc. J. 45 (1984)509–516.
```
```
[17] R.M. Clark, Evaluating the cost and performance of field-scale granular activatedcarbon systems, Environ. Sci. Technol. 21 (1987) 573–580.
```
[18] K.H. Chu, Breakthrough curve analysis by simplistic models of fixed bedadsorption: In defense of the century-old Bohart-Adams model, Chem. Eng. J. 380
```
(2020) 122513.[19] Asadullah, L. Kaewsichan, K. Techato, Z.N. Qaisrani, M.S. Chowdhury, M. Yilmaz,
```
Elimination of selected heavy metals from aqueous solutions using biochar andbentonite composite monolith in a fixed-bed operation, J. Environ. Chem. Eng. 10
```
(2022) 106993.[20] Z. Jiang, M. Chen, X. Lee, Q. Feng, N. Cheng, X. Zhang, S. Wang, B. Wang,
```
```
Enhanced removal of sulfonamide antibiotics from water by phosphogypsummodified biochar composite, J. Environ. Sci. 130 (2023) 174–186.
```
[21] M. Ahmad, N.M.A. Lubis, M. Usama, J. Ahmad, M.I. Al-Wabel, H.A. Al-Swadi, M.I. Rafique, A.S.F. Al-Farraj, Scavenging microplastics and heavy metals from
```
water using jujube waste-derived biochar in fixed-bed column trials, Environ.Pollut. 335 (2023) 122319.
```
```
[22] M.S. Podder, C.B. Majumder, Biological detoxification of As(III) and As(V) usingimmobilized bacterial cells in fixed-bed bio-column reactor: prediction of kinetic
```
```
parameters, Groundw. Sustain. Dev. 6 (2018) 14–42.[23] J. Abdi, H. Abedini, MOF-based polymeric nanocomposite beads as an efficient
```
```
adsorbent for wastewater treatment in batch and continuous systems: modellingand experiment, Chem. Eng. J. 400 (2020) 125862.
```
[24] M. Balsamo, F. Montagnaro, Fractal-like Vermeulen kinetic equation for thedescription of diffusion-controlled adsorption dynamics, J. Phys. Chem. C 119
```
(2015) 8781–8785.[25] F.M. de Souza, O.A.A. dos Santos, Assessment of fixed bed adsorption of 2,4-D
```
```
herbicide onto modified bentonite clay, Water Air Soil Pollut. 233 (2022) 158.[26] A. Satya, A. Harimawan, G. Sri Haryani, M.A.H. Johir, L.N. Nguyen, L.D. Nghiem,
```
S. Vigneswaran, H.H. Ngo, T. Setiadi, Fixed-bed adsorption performance andempirical modelingof cadmium removal using adsorbent prepared from the
```
cyanobacterium Aphanothece sp cultivar, Environ. Technol. Innov. 21 (2021)101194.
```
[27] M. Jafari, M.R. Rahimi, A. Asfaram, M. Ghaedi, H. Javadian, Experimental designfor the optimization of paraquat removal from aqueous media using a fixed-bed
```
column packed with Pinus Eldarica stalks activated carbon, Chemosphere 291(2022) 132670.
```
```
[28] M.A. Basunia, T. Abe, Adsorption isotherms of barley at low and hightemperatures, J. Food Eng. 66 (2005) 129–136.
```
[29] Q. Hu, Q. Huang, D. Yang, H. Liu, Prediction of breakthrough curves in a fixed-bed column based on normalized Gudermannian and error functions, J. Mol. Liq.
```
323 (2021) 115061.
```
[30] M.S. Shafeeyan, W.M.A. Wan Daud, A. Shamiri, A review of mathematicalmodeling of fixed-bed columns for carbon dioxide adsorption, Chem. Eng. Res.
```
Des. 92 (2014) 961–988.[31] Y. Lin, T.A. Kurniawan, M. Zhu, T. Ouyang, R. Avtar, M.H. Dzarfan Othman, B.
```
T. Mohammad, A.B. Albadarin, Removal of acetaminophen from syntheticwastewater in a fixed-bed column adsorption using low-cost coconut shell waste
```
pretreated with NaOH, HNO3, ozone, and/or chitosan, J. Environ. Manag. 226(2018) 365–376.
```
```
[32] A. Thirunavukkarasu, R. Nithya, R. Sivashankar, Continuous fixed-bedbiosorption process: a review, Chem. Eng. J. Adv. 8 (2021) 100188.
```
[33] E. Worch, Adsorption Technology in Water Treatment: Fundamentals, Walter deGruyter GmbH & Co KG, Processes and Modeling, 2012.
[34] Z. Fang, K. Zhang, X. Zhang, B. Pan, Enhanced water decontamination frommethylated arsenic by utilizing ultra-small hydrated zirconium oxides
```
encapsulated inside gel-type anion exchanger, Chem. Eng. J. 430 (2022) 132641.[35] G. Yan, T. Viraraghavan, M. Chen, A new model for heavy metal removal in a
```
```
biosorption column, Adsorpt. Sci. Technol. 19 (2001) 25–43.[36] A. Hethnawi, A.D. Manasrah, G. Vitale, N.N. Nassar, Fixed-bed column studies of
```
total organic carbon removal from industrial wastewater by use of diatomitedecorated with polyethylenimine-functionalized pyroxene nanoparticles,
J. Colloid Interface Sci. 513 (2018) 28–42.[37] T. Ataei-Germi, A. Nematollahzadeh, Bimodal porous silica microspheres
```
decorated with polydopamine nano-particles for the adsorption of methylene bluein fixed-bed columns, J. Colloid Interface Sci. 470 (2016) 172–182.
```
[38] G. Alberti, V. Amendola, M. Pesavento, R. Biesuz, Beyond the synthesis of novelsolid phases: review on modelling of sorption phenomena, Coord. Chem. Rev. 256
```
(2012) 28–45.[39] A.A. Ghani, K.C. Devarayapalli, B. Kim, Y. Lim, G. Kim, J. Jang, D.S. Lee, Sodium-
```
alginate-laden MXene and MOF systems and their composite hydrogel beads forbatch and fixed-bed adsorption of naproxen with electrochemical regeneration,
```
Carbohydr. Polym. 318 (2023) 121098.[40] J. Staudt, F.B. Scheufele, C. Ribeiro, T.Y. Sato, R. Canevesi, C.E. Borba,
```
```
Ciprofloxacin desorption from gel type ion exchange resin: desorption modelingin batch system and fixed bed column, Sep. Purif. Technol. 230 (2020) 115857.
```
[41] N.C. Font˜ao, F.V. Hackbarth, D.A. Mayer, L.P. Mazur, A.A.U. de Souza, V.J.P. Vilar, S.M.A.G.U. de Souza, A step forward on mathematical modeling of
```
barium removal from aqueous solutions using seaweeds as natural cationexchangers: batch and fixed-bed systems, Chem. Eng. J. 401 (2020) 126019.
```
```
[42] A.G. Rios, A.M. Ribeiro, A.E. Rodrigues, A.F.P. Ferreira, Bovine serum albuminand myoglobin separation by size exclusion SMB, J. Chromatogr. A 1628 (2020)
```
461431.[43] A. Hethnawi, N.N. Nassar, A.D. Manasrah, G. Vitale, Polyethylenimine-
functionalized pyroxene nanoparticles embedded on Diatomite for adsorptiveremoval of dye from textile wastewater in a fixed-bed column, Chem. Eng. J. 320
```
(2017) 389–404.[44] D.M. Ruthven, Principles of Adsorption and Adsorption Processes, John Wiley &
```
Sons, New York, 1984.[45] J.T. Edward, Molecular volumes and the Stokes-Einstein equation, J. Chem. Educ.
```
47 (1970) 261.[46] Z. Xu, J. Cai, B. Pan, Mathematically modeling fixed-bed adsorption in aqueous
```
```
systems, J. Zhejiang Univ.-Sci. A 14 (2013) 155–176.[47] Q. Hu, D. Wang, S. Pang, L. Xu, Prediction of breakthrough curves for
```
```
multicomponent adsorption in a fixed-bed column using logistic and Gompertzfunctions, Arab. J. Chem. 15 (2022) 104034.
```
[48] C. Rabbat, A. Pinna, Y. Andres, A. Villot, S. Awad, Adsorption of ibuprofen fromaqueous solution onto a raw and steam-activated biochar derived from recycled
```
textiles insulation panels at end-of-life: kinetic, isotherm and fixed-bedexperiments, J. Water Process. Eng. 53 (2023) 103830.
```
[49] Y. Wang, C. Wang, X. Huang, Q. Zhang, T. Wang, X. Guo, Guideline for modelingsolid-liquid adsorption: kinetics, isotherm, fixed bed, and thermodynamics,
```
Chemosphere 349 (2024) 140736.[50] E. Worch, Fixed-bed adsorption in drinking water treatment: a critical review on
```
```
models and parameter estimation, J. Water Supply Res Technol.-Aqua 57 (2008)171–183.
```
```
[51] B.O. Fagbayigbo, B.O. Opeolu, O.S. Fatoki, Adsorption of perfluorooctanoic acid(PFOA) and perfluorooctane sulfonate (PFOS) from water using leaf biomass (Vitis
```
```
vinifera) in a fixed-bed column study, J. Environ. Health Sci. Eng. 18 (2020)221–233.
```
[52] K. Al-Zawahreh, M.T. Barral, Y. Al-Degs, R. Paradelo, Competitive removal oftextile dyes from solution by pine bark-compost in batch and fixed bed column
```
experiments, Environ. Technol. Innov. 27 (2022) 102421.[53] P. Ostaszewski, O. Długosz, M. Banach, Analysis of measuring methods of the
```
```
concentration of methylene blue in the sorption process in fixed-bed column, Int.J. Environ. Sci. Technol. 19 (2022) 1–8.
```
```
[54] Q. Hu, Z. Zhang, Comment on Exponential and logistic functions: the two faces ofthe Bohart–Adams model, J. Hazard. Mater. 394 (2020) 122508.
```
[55] Q. Hu, Z. Zhang, Comment on Breakthrough curve analysis by simplistic modelsof fixed bed adsorption: in defense of the century-old Bohart–Adams model,
```
Chem. Eng. J. 394 (2020) 124511.[56] S. Wu, L. Debnath, A generalization of L’Hˆospital-type rules for monotonicity and
```
```
its application, Appl. Math. Lett. 22 (2009) 284–290.[57] R.A. Hutchins, New method simplifies design of activated carbon systems, Chem.
```
```
Eng. 80 (1973) 133–138.[58] R. Han, Y. Wang, W. Zou, Y. Wang, J. Shi, Comparison of linear and nonlinear
```
analysis in estimating the Thomas model parameters for methylene blue
Q. Hu et al.Journal of Water Process Engineering 59 (2024) 105065
17
```
adsorption onto natural zeolite in fixed-bed column, J. Hazard. Mater. 145 (2007)331–335.
```
[59] K. Xiao, X. Wang, X. Huang, T.D. Waite, X. Wen, Analysis of polysaccharide,protein and humic acid retention by microfiltration membranes using Thomas’
```
dynamic adsorption model, J. Membr. Sci. 342 (2009) 22–34.[60] R. Lakshmipathy, N.C. Sarada, A fixed bed column study for the removal of Pb2+
```
```
ions by watermelon rind, Environ. Sci. Water Res. Technol. 1 (2015) 244–250.[61] D. Ranjan Rout, H. Mohan Jena, Synthesis of novel reduced graphene oxide
```
```
decorated β-cyclodextrin epichlorohydrin composite and its application for Cr(VI)removal: batch and fixed-bed studies, Sep. Purif. Technol. 278 (2021) 119630.
```
[62] K.H. Chu, Fixed bed adsorption of water contaminants: a cautionary guide tosimple analytical models and modeling misconceptions, Sep. Purif. Rev. 52
```
(2023) 75–97.[63] H. Xiang, H. Zhang, P. Liu, Y. Yan, Adsorption dynamics of ethane from air in
```
```
structured fixed beds with different microfibrous composites, Chin. J. Chem. Eng.53 (2023) 14–24.
```
[64] Q. Hu, Y. Xie, Z. Zhang, Modification of breakthrough models in a continuous-flow fixed-bed column: mathematical characteristics of breakthrough curves and
```
rate profiles, Sep. Purif. Technol. 238 (2020) 116399.[65] Y.H. Yoon, J.H. Nelson, Application of gas adsorption kinetics — II. A theoretical
```
```
model for respirator cartridge service life and its practical applications, Am. Ind.Hyg. Assoc. J. 45 (1984) 517–524.
```
[66] J.T. de Oliveira, L.R. de Carvalho Costa, G.D. Agnol, L.A. F´eris, Experimentaldesign and data prediction by Bayesian statistics for adsorption of tetracycline in
```
a GAC fixed-bed column, Sep. Purif. Technol. 319 (2023) 124097.[67] Q. Hu, R. Lan, L. He, H. Liu, X. Pei, A critical review of adsorption isotherm
```
```
models for aqueous contaminants: curve characteristics, site energy distributionand common controversies, J. Environ. Manag. 329 (2023) 117104.
```
[68] U. Kumari, A. Mishra, H. Siddiqi, B.C. Meikap, Effective defluoridation ofindustrial wastewater by using acid modified alumina in fixed-bed adsorption
```
column: experimental and breakthrough curves analysis, J. Clean. Prod. 279(2021) 123645.
```
[69] A.A. Aryee, R. Han, A novel biocomposite based on peanut husk withantibacterial properties for the efficient sequestration of trimethoprim in solution:
```
batch and column adsorption studies, Colloids Surf. A Physicochem. Eng. Asp.635 (2022) 128051.
```
[70] M. Vera, D.M. Juela, C. Cruzat, E. Vanegas, Modeling and computational fluiddynamic simulation of acetaminophen adsorption using sugarcane bagasse,
J. Environ. Chem. Eng. 9 (2021) 105056.[71] A. Wolborska, Adsorption on activated carbon of p-nitrophenol from aqueous
```
solution, Water Res. 23 (1989) 85–91.[72] C. Smaranda, M.C. Popescu, D. Bulgariu, T. M˘alut
```
¸an, M. Gavrilescu, Adsorption oforganic pollutants onto a Romanian soil: column dynamics and transport,
```
Process. Saf. Environ. Prot. 108 (2017) 108–120.[73] S. Singh, V.C. Srivastava, I.D. Mall, Fixed-bed study for adsorptive removal of
```
```
furfural by activated carbon, Colloids Surf. A Physicochem. Eng. Asp. 332 (2009)50–56.
```
```
[74] A. Wolborska, P. Pustelnik, A simplified method for determination of the break-through time of an adsorbent layer, Water Res. 30 (1996) 2643–2650.
```
```
[75] A. Katsigiannis, C. Noutsopoulos, J. Mantziaras, M. Gioldasi, Removal ofemerging pollutants through granular activated carbon, Chem. Eng. J. 280 (2015)
```
49–57.[76] D. Sana, S. Jalila, A comparative study of adsorption and regeneration with
```
different agricultural wastes as adsorbents for the removal of methylene bluefrom aqueous solution, Chin. J. Chem. Eng. 25 (2017) 1282–1287.
```
[77] C.G. Lee, J.H. Kim, J.K. Kang, S.B. Kim, S.J. Park, S.H. Lee, J.W. Choi,Comparative analysis of fixed-bed sorption models using phosphate breakthrough
```
curves in slag filter media, Desalin. Water Treat. 55 (2015) 1795–1805.[78] A. Klinkenberg, Numerical evaluation of equations describing transient heat and
```
```
mass transfer in packed solids, Ind. Eng. Chem. 40 (1948) 1992–1994.[79] Y. Taamneh, R. Al Dwairi, The efficiency of Jordanian natural zeolite for heavy
```
```
metals removal, Appl Water Sci 3 (2013) 77–84.[80] K.H. Chu, Prediction of arsenic breakthrough in a pilot column of polymer-
```
```
supported nanoparticles, J. Water Process. Eng. 3 (2014) 117–122.[81] B. Ren, N. Lyczko, Y. Zhao, A. Nzihou, Alum sludge as an efficient sorbent for
```
```
hydrogen sulfide removal: experimental, mechanisms and modeling studies,Chemosphere 248 (2020) 126010.
```
[82] J.M. Silva, M.F. Ribeiro, I. Graça, A. Fernandes, Bio-oils/FCC co-processing:Insights into the adsorption of guaiacol on Y zeolites with distinct acidity and
```
textural properties, Microporous Mesoporous Mater. 323 (2021) 111170.[83] J.B. Dima, M. Ferrari, N. Zaritzky, Mathematical modeling of fixed-bed columns
```
```
adsorption: hexavalent chromium onto chitosan flakes, Ind. Eng. Chem. Res. 59(2020) 15378–15386.
```
```
[84] J.M. Chern, Y.W. Chien, Adsorption of nitrophenol onto activated carbon:isotherms and breakthrough curves, Water Res. 36 (2002) 647–655.
```
[85] J.M. Chern, Y.W. Chien, Competitive adsorption of benzoic acid and p-nitrophenol onto activated carbon: isotherm and breakthrough curves, Water Res.
```
37 (2003) 2347–2356.[86] B.C. Pan, F.W. Meng, X.Q. Chen, B.J. Pan, X.T. Li, W.M. Zhang, X. Zhang, J.
```
L. Chen, Q.X. Zhang, Y. Sun, Application of an effective method in predictingbreakthrough curves of fixed-bed adsorption onto resin adsorbent, J. Hazard.
```
Mater. 124 (2005) 74–80.[87] B. Pan, X. Chen, B. Pan, W. Zhang, X. Zhang, Q. Zhang, Preparation of an
```
```
aminated macroreticular resin adsorbent and its adsorption of p-nitrophenol fromwater, J. Hazard. Mater. 137 (2006) 1236–1240.
```
```
[88] X. Zhang, S. Chen, H.T. Bi, Application of wave propagation theory to adsorptionbreakthrough studies of toluene on activated carbon fiber beds, Carbon 48 (2010)
```
2317–2326.[89] A. Ararem, A. Bouzidi, B. Mohamedi, O. Bouras, Modeling of fixed-bed adsorption
```
of Cs+ and Sr2+ onto clay–iron oxide composite using artificial neural networkand constant–pattern wave approach, J. Radioanal. Nucl. Chem. 301 (2014)
```
881–887.[90] E.F. Schuster, Estimating the distribution function of a symmetric distribution,
```
Biometrika 62 (1975) 631–635.[91] C.E. Borba, R. Guirardello, E.A. Silva, M.T. Veit, C.R.G. Tavares, Removal of
```
```
nickel(II) ions from aqueous solution by biosorption in a fixed bed column:experimental and theoretical breakthrough curves, Biochem. Eng. J. 30 (2006)
```
184–191.[92] A. Karami, R. Sabouni, M.H. Al-Sayah, A. Aidan, Adsorption potentials of iron-
```
based metal–organic framework for methyl orange removal: batch and fixed-bedcolumn studies, Int. J. Environ. Sci. Technol. 18 (2021) 3597–3612.
```
```
[93] M.I. El-Khaiary, Least-squares regression of adsorption equilibrium data:comparing the options, J. Hazard. Mater. 158 (2008) 73–87.
```
[94] C.M.B. de Araujo, G. Wernke, M.G. Ghislandi, A. Di´orio, M.F. Vieira,R. Bergamasco, M.A. da Motta Sobrinho, A.E. Rodrigues, Continuous removal of
pharmaceutical drug chloroquine and Safranin-O dye from water using agar-graphene oxide hydrogel: selective adsorption in batch and fixed-bed
```
experiments, Environ. Res. 216 (2023) 114425.[95] A.K.A. Khalil, I.W. Almanassra, A. Chatla, I. Ihsanullah, T. Laoui, M. Ali Atieh,
```
Insights into the adsorption of lead ions by Mg-Al LDH doped activated carboncomposites: implications for fixed bed column and batch applications, Chem. Eng.
```
Sci. 281 (2023) 119192.[96] R. Kopelman, Fractal reaction kinetics, Science 241 (1988) 1620–1626.
```
```
[97] Q. Hu, H. Liu, Z. Zhang, X. Pei, Development of fractal-like Clark model in a fixed-bed column, Sep. Purif. Technol. 251 (2020) 117396.
```
```
[98] R. Kopelman, Rate processes on fractals: theory, simulations, and experiments,J. Stat. Phys. 42 (1986) 185–200.
```
```
[99] M. Balsamo, F. Montagnaro, Liquid–solid adsorption processes interpreted byfractal-like kinetic models, Environ. Chem. Lett. 17 (2019) 1067–1075.
```
```
[100] M. Haerifar, S. Azizian, Fractal-like adsorption kinetics at the solid/solutioninterface, J. Phys. Chem. C 116 (2012) 13111–13119.
```
```
[101] M. Haerifar, S. Azizian, Fractal-like kinetics for adsorption on heterogeneous solidsurfaces, J. Phys. Chem. C 118 (2014) 1129–1134.
```
```
[102] H. Bashiri, A. Shajari, Theoretical study of fractal-like kinetics of adsorption,Adsorpt. Sci. Technol. 32 (2014) 623–634.
```
[103] F. Montagnaro, M. Balsamo, Modelling CO2 adsorption dynamics onto amine-functionalised sorbents: a fractal-like kinetic perspective, Chem. Eng. Sci. 192
```
(2018) 603–612.[104] Q. Hu, S. Pang, D. Wang, Y. Yang, H. Liu, Deeper insights into the Bohart–Adams
```
```
model in a fixed-bed column, J. Phys. Chem. B 125 (2021) 8494–8501.[105] C.K. Rojas-Mayorga, A. Bonilla-Petriciolet, F.J. S´anchez-Ruiz, J. Moreno-P´erez, H.
```
E. Reynel-´Avila, I.A. Aguayo-Villarreal, D.I. Mendoza-Castillo, Breakthroughcurve modeling of liquid-phase adsorption of fluoride ions on aluminum-doped
```
bone char using micro-columns: effectiveness of data fitting approaches, J. Mol.Liq. 208 (2015) 114–121.
```
```
[106] N. Blagojev, D. Kuki´c, V. Vasi´c, M. ˇS´ciban, J. Prodanovi´c, O. Bera, A newapproach for modelling and optimization of Cu(II) biosorption from aqueous
```
```
solutions using sugar beet shreds in a fixed-bed column, J. Hazard. Mater. 363(2019) 366–375.
```
```
[107] N. Blagojev, V. Vasi´c, D. Kuki´c, M. ˇS´ciban, J. Prodanovi´c, O. Bera, Modelling andefficiency evaluation of the continuous biosorption of Cu(II) and Cr(VI) from
```
```
water by agricultural waste materials, J. Environ. Manag. 281 (2021) 111876.[108] Q. Hu, Y. Xie, C. Feng, Z. Zhang, Prediction of breakthrough behaviors using
```
```
logistic, hyperbolic tangent and double exponential models in the fixed-bedcolumn, Sep. Purif. Technol. 212 (2019) 572–579.
```
```
[109] K.H. Chu, Fitting the Gompertz equation to asymmetric breakthrough curves,J. Environ. Chem. Eng. 8 (2020) 103713.
```
```
[110] W. Weibull, A statistical distribution function of wide applicability, J. Appl. Mech.293–297 (1951).
```
```
[111] K.H. Chu, Fixed bed adsorption of chromium and the Weibull function, J. Hazard.Mater. Lett. 2 (2021) 100022.
```
```
[112] R. Apiratikul, K.H. Chu, Improved fixed bed models for correlating asymmetricadsorption breakthrough curves, J. Water Process. Eng. 40 (2021) 101810.
```
[113] K.H. Chu, M.A. Hashim, Fixed bed adsorption of water and air contaminants:analysis of breakthrough curves using probability distribution functions, Chem.
```
Eng. Commun. 210 (2023) 1528–1537.[114] J. Singh, S.K. Kumaresan, S. Swaroop, V. Mishra, Development of predictive
```
```
model for the fixed-bed column reactor, Appl Water Sci 13 (2023) 114.[115] P.K. Kimani, Asymmetrical fixed-bed breakthrough curve modelling: comparing
```
```
simplistic, log-modified, fractal-like, and probability distribution functionmodels, Chem. Eng. Res. Des. 201 (2024) 446–456.
```
[116] M.F. Oliveira, V.M. de Souza, M.G.C. da Silva, M.G.A. Vieira, Fixed-bedadsorption of caffeine onto thermally modified Verde-lodo bentonite, Ind. Eng.
```
Chem. Res. 57 (2018) 17480–17487.[117] M.I. El-Khaiary, G.F. Malash, Common data analysis errors in batch adsorption
```
```
studies, Hydrometallurgy 105 (2011) 314–320.[118] A. Scott, C. Wild, Transformations and R2, Am. Stat. 45 (1991) 127–129.
```
[119] A. Bakka, R. Mamouni, N. Saffaj, A. Laknifli, K. Aziz, A. Roudani, Removal ofbifenthrin pesticide from aqueous solutions by treated patellidae shells using a
```
new fixed bed column filtration technique, Process. Saf. Environ. Prot. 143 (2020)55–65.
```
Q. Hu et al.Journal of Water Process Engineering 59 (2024) 105065
18
```
[120] C.C. Chen, R. Vance Morey, Comparison of four EMC/ERH equations, Trans.ASAE 32 (1989) 983–0990.
```
[121] M.B. de Farias, M.P. Spaolonzi, M.G.C. Silva, M.G.A. Vieira, Fixed-bed adsorptionof bisphenol A onto organoclay: characterisation, mathematical modelling and
```
theoretical calculation of DFT-based chemical descriptors, J. Environ. Chem. Eng.9 (2021) 106103.
```
[122] L.S. Roca, S.E. Schoemaker, B.W.J. Pirok, A.F.G. Gargano, P.J. Schoenmakers,Accurate modelling of the retention behaviour of peptides in gradient-elution
```
hydrophilic interaction liquid chromatography, J. Chromatogr. A 1614 (2020)460650.
```
[123] G.F. Malash, M.I. El-Khaiary, Piecewise linear regression: a statistical method forthe analysis of experimental adsorption data by the intraparticle-diffusion
```
models, Chem. Eng. J. 163 (2010) 256–263.[124] G. Glatting, P. Kletting, S.N. Reske, K. Hohl, C. Ring, Choosing the optimal fit
```
```
function: comparison of the Akaike information criterion and the F-test, Med.Phys. 34 (2007) 4285–4292.
```
[125] S. Cataldo, A. Gianguzza, D. Milea, N. Muratore, A. Pettignano, S. Sammartano,A critical approach to the toxic metal ion removal by hazelnut and almond shells,
```
Environ. Sci. Pollut. Res. 25 (2018) 4238–4253.[126] T.M. Darweesh, M.J. Ahmed, Adsorption of ciprofloxacin and norfloxacin from
```
```
aqueous solution onto granular activated carbon in fixed bed column, Ecotoxicol.Environ. Saf. 138 (2017) 139–145.
```
[127] H. Bacelo, S.C.R. Santos, A. Ribeiro, R.A.R. Boaventura, C.M.S. Botelho, Antimonyremoval from water by pine bark tannin resin: Batch and fixed-bed adsorption,
J. Environ. Manag. 302 (2022) 114100.[128] D. Juela, M. Vera, C. Cruzat, A. Astudillo, E. Vanegas, A new approach for scaling
```
up fixed-bed adsorption columns for aqueous systems: a case of antibiotic removalon natural adsorbent, Process. Saf. Environ. Prot. 159 (2022) 953–963.
```
[129] Y. Lee, Y. Ren, M. Cui, Y. Zhou, O. Kwon, J. Ko, J. Khim, Arsenic adsorption studyin acid mine drainage using fixed bed column by novel beaded adsorbent,
```
Chemosphere 291 (2022) 132894.
```
[130] J. Jang, D.S. Lee, Effective phosphorus removal using chitosan/Ca-organicallymodified montmorillonite beads in batch and fixed-bed column studies,
J. Hazard. Mater. 375 (2019) 9–18.[131] M.E. Gonz´alez-L´opez, C.M. Laureano-Anzaldo, A.A. P´erez-Fonseca, M. Arellano, J.
R. Robledo-Ortíz, A critical overview of adsorption models linearization:methodological and statistical inconsistencies, Sep. Purif. Rev. 51 (2022)
358–372.[132] A.L. Silveira Neto, W. Pimentel-Almeida, G. Niero, E.H. Wanderlind, C.
M. Radetski, G.I. Almerindo, Application of a biochar produced from malt bagasseas a residue of brewery industry in fixed-bed column adsorption of paracetamol,
```
Chem. Eng. Res. Des. 194 (2023) 779–786.[133] J. Tejedor, R. ´Alvarez-Brice˜no, V.H. Guerrero, C.A. Villamar-Ayala, Removal of
```
caffeine using agro-industrial residues in fixed-bed columns: improving theadsorption capacity and efficiency by selecting adequate physical and operational
```
parameters, J. Water Process. Eng. 53 (2023) 103778.[134] J. He, Q. Zhou, J. Guo, J. Gao, F. Fang, Incredulity on assumptions for the
```
```
simplified Bohart-Adams model: 17a-ethinylestradiol separation in lab-scaleanthracite columns, J. Hazard. Mater. 384 (2020) 121501.
```
[135] Y.S. Ho, J.F. Porter, G. McKay, Equilibrium isotherm studies for the sorption ofdivalent metal ions onto peat: copper, nickel and lead single component systems,
```
Water Air Soil Pollut. 141 (2002) 1–33.[136] K.H. Chen, Y.R. Lai, N.T.D. Hanh, Breakthrough curve modeling for lysozyme by
```
```
ion-exchange nanofiber membrane: linear and nonlinear analysis, J. Taiwan Inst.Chem. Eng. 105198 (2023).
```
[137] H.N. Tran, S.J. You, A. Hosseini-Bandegharaei, H.P. Chao, Mistakes andinconsistencies regarding adsorption of contaminants from aqueous solutions: a
```
critical review, Water Res. 120 (2017) 88–116a.[138] Z. Ma, R.D. Whitley, N.H.L. Wang, Pore and surface diffusion in multicomponent
```
```
adsorption and liquid chromatography systems, AICHE J. 42 (1996) 1244–1262.
```
Q. Hu et al.
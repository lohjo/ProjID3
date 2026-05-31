International Journal of Heat and Mass Transfer 163 (2020) 120374


Contents lists available at [ScienceDirect](http://www.ScienceDirect.com)

# ~~International Journal of Heat and Mass Transfer~~


journal homepage: [www.elsevier.com/locate/hmt](http://www.elsevier.com/locate/hmt)

## Mass transfer from a fluid flowing through a porous media


T.G. Myers [∗], F. Font


_Centre_ _de_ _Recerca_ _Matemàtica,_ _Campus_ _de_ _Bellaterra,_ _Edifici_ _C,_ _Barcelona,_ _08193_ _Bellaterra,_ _Spain_



a r t i c l e i n f 

_Article_ _history:_
Received 12 July 2020
Revised 8 August 2020
Accepted 20 August 2020
Available online 29 September 2020


_2010_ _MSC:_
35Q35


_Keywords:_
Contaminant removal
Pollutant removal
Adsorption
Absorption
Carbon capture
Packed column
Mathematical model


**1.** **Introduction**



a b s t r a c t


A mathematical model is developed for the process of mass transfer from a fluid flowing through a
packed column. Mass loss, whether by absorption or adsorption, may be significant. This is appropriate for example when removing contaminants from flue gases. With small mass loss the model reduces
to a simpler form which is appropriate to describe the removal of contaminants/pollutants from liquids.
A case study is carried out for the removal of CO2 from a gas mixture passing over activated carbon.
Using the experimental parameter values it is shown, via non-dimensionalisation, that certain terms may
be neglected from the governing equations, resulting in a form which may be solved analytically using a
travelling wave substitution. From this all important quantities throughout the column may be described;
concentration of gaseous materials, amount of material available for mass transfer, fluid velocity and pressure. Results are verified by comparison with experimental data for the breakthrough curve (the amount
of carbon measured at the column outlet). The advantage of the analytical expression over a purely numerical solution is that it can easily be used to optimise the process. In the final section we demonstrate
how the model may be further reduced when small amounts of contaminant are removed. The model is
shown to exhibit better agreement than established models when compared to experimental data for the
removal of amoxicillin and congo red dye from water.


© 2020 Elsevier Ltd. All rights reserved.



With oceans overloaded with plastic, the air that we breathe
full of noxious substances and even drinking water laced with legal and illegal drugs it is clear that humanity needs to improve
its methods for dealing with pollutants. However, cutting down on
pollution is not enough, in some cases active removal must be carried out. In this paper we will focus on just one aspect of this issue, namely contaminant removal via column sorption.
Column sorption involves forcing a fluid through a confined
tube filled with a porous material capable of removing certain
components of the fluid. As the fluid passes through, the component to be removed can attach to the surface of the material (adsorption) or enter into the volume (absorption). This may continue
until the material becomes saturated, when no more removal occurs, and the fluid passes through the material unchanged. It is
perhaps the most popular practical sorption method [1,2] and is
used for a wide range of processes such as the removal of contaminants including pharmaceuticals, carbon dioxide, heavy metals, dyes and salts [1,3–7].


∗ Corresponding author.
_E-mail_ _address:_ [tmyers@crm.cat](mailto:tmyers@crm.cat) (T.G. Myers).


[https://doi.org/10.1016/j.ijheatmasstransfer.2020.120374](https://doi.org/10.1016/j.ijheatmasstransfer.2020.120374)
0017-9310/© 2020 Elsevier Ltd. All rights reserved.



In this paper we will develop a model to describe the flow of a
fluid through a porous material contained in a cylindrical column.
This configuration has been chosen due to its relevance for a wide
number of published experiments and existing extraction equipment. We will focus on a two-component fluid system, with only
one component being removed (the extension to more components
is straightforward). Once the model is developed we will analyse it
within the context of post-combustion carbon capture and compare with experimental results for breakthrough (that is the CO2
concentration on leaving the column). Subsequently we will show
how the model compares with previous, standard models and test
it against experimental data for the removal of contaminants such
as antibiotics and synthetic dyes.
There exists a wide literature analysing column sorption. A
number of simple models focus solely on the column outlet and
are based on the probability of a gas molecule escaping [8]. These
neglect the evolution of the process through the column and cannot fully explain the physics. However, with carefully chosen parameter values it is possible to reproduce the breakthrough curves.
When flow along the column is accounted for the simplest model
balances advection with mass loss, coupled to a rate equation for
the mass loss. An early example of this may be found in [9]. Although their full result is often reduced to a much simplified equation valid only at the outlet. Recent models typically deal with
variables averaged over the cross-section and include advection,


2 _T.G._ _Myers_ _and_ _F._ _Font_ _/_ _International_ _Journal_ _of_ _Heat_ _and_ _Mass_ _Transfer_ _163_ _(2020)_ _120374_



diffusion and temperature effects [10,11]. However, since the sorption process is approximated by a simple kinetic model there is
still a degree of fitting to match the breakthrough curve. An issue with many numerical studies is highlighted in [12] where it
is shown that a number of errors in the governing equations have
propagated through the literature. This leads to inaccuracies in the
fitting coefficients and therefore incorrect predictions on scaling
up.
The study of [12] was based on the assumption of negligible
mass removal, so that quantities such as the velocity and fluid
density are constant and consequently the pressure gradient is linear. In the following we will consider a situation where significant
quantities are removed, such that the density and velocity may
vary along the column. We will follow the style of [12] but do
not carry out the averaging which acts to complicate the system.
After deriving the governing equations we apply the model to an
example of carbon capture, where approximately 15% of a CO2/N2
mixture is removed by adsorption. Comparison with experimental data for breakthrough shows excellent agreement. Subsequently
we compare the full current model, a reduced version of this appropriate for incompressible flow and previous models against data
for the removal of amoxicillin and dye from solution.
The work contains a number of novel elements for this field.
The non-dimensionalisation permits us to identify dominant terms
and also negligible ones which then permits the study of a much
simplified system (with a known small error). Except during the
very initial period, the simplified system permits a travelling wave
solution and so we find analytical expressions for all important quantities, concentration, available adsorbent, gas velocity and
pressure. These solutions have not previously been published. A
full numerical solution is therefore not necessary. It is shown that
the gas concentration and available sorbent follow almost identical
curves, this means that the experimentally observed breakthrough
curve may be used to determine the form of the kinetic relation.


**2.** **Derivation** **of** **governing** **equations**



Consider a fluid flowing through a porous medium where mass
transfer occurs at the fluid-solid interfaces. Within the fluid the
mass continuity equation may be written in the form
_∂ρ_

_∂t_ [+] [∇] [·] _[j]_ [=] [−] _[S][,]_ (1)

where _S_ is a sink term representing mass loss and _ρ_ is the density.
The flux is composed of advective and diffusive components


_j_ = - _D_ ∇ _ρ_ + _ρu._ (2)


The exact shape of the porous media is unknown hence it is impossible to predict the flow, for this reason it is standard practice
to assume plug flow or carry out some radial averaging: the resulting equations are equivalent. Here we will follow the simpler
route, assuming plug flow and hence all other variables also only
vary with distance along the column.
With the definition _u_ = _(u(x,_ _t),_ 0 _)_, mass continuity now specifies
_∂ρ_ _[∂]_ _[(][u][ρ][)]_ _[∂]_ [2] _[ρ]_ _[∂][q]_




_[u][ρ][)]_ = _D_ _[∂]_ [2] _[ρ]_

_∂x_ _∂x_ [2]



_∂t_ _[,]_ (3)



_∂ρ_ _[∂]_ _[(][u][ρ][)]_

_∂t_ [+] _∂x_




[2] _[ρ]_ _[q]_

_∂x_ [2] [−] _[(]_ [1] [−] _[ϵ][)][ρ][q][M][q]_ _[∂]_ _∂t_



solid material, which is here denoted _q_ . The final term on the right
hand side is then a sink representing the mass lost at all solidfluid interfaces at a given _x_, see [12]. If the volume flux at the
column inlet is _Q_ 0( _t_ ), then the interstitial velocity may be written _u(x,_ _t)_ with _u(_ 0 _,_ _t)_ = _u_ 0 _(t)_ = _Q_ 0 _(t)/(ϵπ_ _R_ [2] _)_ . In the literature it
is also common to work in terms of the superficial velocity, which
is simply the interstitial velocity multiplied by the void fraction,
_ϵu_ .
The density may be expressed in terms of the molar mass _Mi_
and molar concentration _ci_ of the components. For a two component system _ρ_ = _M_ 1 _c_ 1 + _M_ 2 _c_ 2 _,_ while the molar mass of the gas
mixture _M_ = _ρ/(c_ 1 + _c_ 2 _)_ .


_2.1._ _Mass_ _transfer_


There are a number of models to approximate the mass transfer
process. These are typically based on assumptions that the rate is
proportional to the amount available for transfer and the free sites
on the solid material and lead to different forms of kinetic model.
A classical model is presented in [9]. Local equilibrium, linear driving force, pore diffusion, pseudo-first-order, pseudo-second-order
and Avrami models are discussed in [10,13]. In the present study
we will employ the popular linear kinetic relation


_∂q_

_∂t_ [=] _[k][q][(][q]_ ~~[∗]~~ [−] _[q][)][,]_ (4)

where _kq_ is a rate constant and _q_ ~~[∗]~~ the saturation value. The form
of _q_ [∗] is also the subject of numerous studies, see the review of

[14].
The linear kinetic relation has the unrealistic feature that it
has a weak dependence on the component available for transfer (which can only enter through the definition of _q_ ¯ [∗] ). It must
therefore be specified explicitly that this equation only holds over
regions where material is available. There is a tendency in published literature to immediately integrate equation (4) to find _q_ =
_q_ ~~[∗]~~ _(_ 1 - exp _(_ - _kt))_ [5,13,15]. This is incorrect. Firstly, _q_ ~~[∗]~~ typically depends in a complex way on space and time, secondly the constant
of integration is dependent on space. In the special case where
_q_ ~~[∗]~~ is constant we may write _q_ = _q_ ~~[∗]~~ _(_ 1 - exp _(_ - _k(t_ - _ts(x))))_ where
_ts_ ( _x_ ) is the time at which the material to be removed first reaches
the point _x_ . With a typical form of time-dependent _q_ ~~[∗]~~ the integration cannot be carried out.


_2.2._ _Pressure_ _velocity_ _relations_


If we assume a constant fluid velocity then its value may be
easily calculated from the mass or volume flux and the above
equations adequately describe the system. This would be appropriate when a negligible mass (compared to the total mass) is removed and is typically the case with transfer from a liquid. If mass
removal is significant it will affect the velocity and pressure. This
often occurs in gas mass transfer processes, which can involve the
removal of some 20% of the gas. In this situation we need more
equations to close the system. Since the case of gas flow is more
complex henceforth we will focus on that, the liquid case forms a
subset of the model developed below.
Firstly, we follow the standard practice of relating the pressure
to the concentration via the ideal gas law


_p_ = _RgTc_ = _RgT_ _(c_ 1 + _c_ 2 _)._ (5)


The final governing equation required for the system comes from
conservation of momentum. For uni-directional plug flow the
Navier-Stokes equation may be reduced to the form



where _ϵ_ is the bed void fraction. The derivation of the mass loss
term requires an assumption that the solid component accepts material of density _ρq_ and molar mass _Mq_ at a rate _∂q/∂t,_ where _q_
represents the amount of material transferred. The overbar indicates it is an average. In practice material is normally adsorbed or
absorbed through the surface or in cracks of the solid. In time the
surfaces become saturated. To avoid dealing with an overly complicated system it is standard to ignore the precise distribution of
the transferred mass and instead define an average throughout the




 _∂u_
_ρ_ _∂t_ [+] _[u]_ _[∂]_ _∂_ _[u]_ _x_



_∂x_







= - _[∂]_ _[p]_




_[p]_ [4]

_∂x_ [+] 3




[4] [2] _[u]_

3 _[μ]_ _[∂]_ _∂x_ [2]



_∂x_ [2] [−] _[S][u][.]_ (6)


_T.G._ _Myers_ _and_ _F._ _Font_ _/_ _International_ _Journal_ _of_ _Heat_ _and_ _Mass_ _Transfer_ _163_ _(2020)_ _120374_ 3



The term _S_ _u_ represents a reduction in momentum due to mass
loss, where _S_ = _(_ 1 - _ϵ)ρqMq∂q/∂t_ is the sink from the mass continuity equation. The 4/3 factor is specific to compressible flow: with
a constant density flow this factor becomes unity.
The classical relation describing flow in a porous media is
Darcy’s law, which was derived for the incompressible flow of a
viscous liquid through sand. In the case of a gas flowing through a
packed bed Darcy may not be appropriate. To understand Darcy’s
law consider conservation of momentum with no mass sink. Assuming the steady, slow flow of an incompressible fluid (where
slow is defined such that terms of order _u_ [2] may be neglected)
equation (6) reduces to



If only one species is removed we may set _Mq_ = _M_ 1 that is, the
molar mass of the component is the same in the solid and fluid
state. The remaining governing equations are

_∂q_ 
_∂t_ [=] _[k][q]_ _q_ ~~[∗]~~ - _q_ [�] _,_ (14)


_p_ = _RgT_ _(c_ 1 + _c_ 2 _)_ _,_ (15)




        
_[∂]_ _[p]_ _[α][(][M]_ [1] _[c]_ [1] [+] _[M]_ [2] _[c]_ [2] _[)][u]_ [2] [+] _β_ + _(_ 1 - _ϵ)ρqM_ 1 _[∂][q]_

_∂x_ [=] _∂t_




- _[∂]_ _[p]_



_∂t_







_u._ (16)




[2] _[u]_

_[∂]_ _[p]_ _[μ]_ _[∂]_

_∂x_ [+] _∂x_ [2] _[.]_



0 = - _[∂]_ _[p]_



_∂x_ [2] _[.]_ (7)



Equations (12)–(16) provide the system to describe the evolution
of the five variables _c_ 1 _,_ _c_ 2 _,_ _u,_ _p,_ _q_ . The five equations are required
when mass transfer is significant compared to the total mass flow.
When dealing with the transfer of trace amounts of a material, for
example drugs in the water supply, the system is significantly simpler. First, the velocity is approximately constant _u_ = _Q_ 0 _/(ϵπ_ _R_ [2] _)_
and the problem is described by equations (12,14). If a known pressure drop drives the flow then the velocity may also be calculated
by neglecting the _c_ 1 and _q_ terms in equation (16) (since both terms
are small when trace amounts are removed).
The assumptions made in deriving the above equations include:
the amount of material transferred may be averaged over the sorbent; _qt_ follows a linear kinetic model (this is discussed later); an
ideal gas law holds; the flow may be approximated as plug flow.


_2.4._ _Boundary_ _and_ _initial_ _conditions_


At the inlet, _x_ = 0 _,_ there is continuity of mass flux so



The key assumption is that viscous resistance is proportional to velocity _uxx_ ∝ _u_ and then we obtain Darcy’s law




- _[∂]_ _[p]_




_[∂]_ _[p]_ _[μ]_

_∂x_ [=] _k_



_u,_ (8)
_kp_



where _kp_ is termed the permeability. Gases have a very low viscosity so it is possible that for gas flow viscous resistance is small and
instead inertial resistance plays a significant role. When inertia is
non-negligible a drag law is usually invoked




_[∂][u]_ _[C][D]_ _u_ [2]

_∂x_ [=] _d_



_u_ _[∂][u]_



_d_ _[,]_ (9)



where the length-scale _d_ is chosen as the typical particle diameter
and the drag coefficient _CD_ = _CD(ϵ,_ _Re,_ _d)_ . In a similar manner to
the derivation of Darcy’s law we may use this expression to obtain
a relation between pressure gradient and velocity.
For the current problem, the momentum equation also contains
a sink term proportional to velocity. Including both viscous and inertial resistance as well as the sink we obtain the pressure-velocity
relation

- _[∂]_ _∂x_ _[p]_ [=] _[αρ][u]_ [2] [+] _[(][β]_ [+] _[S][)][u][,]_ (10)

where _α,_ _β_ are constant while _S_ is variable. In the absence of the
sink term this form of equation is discussed in [16]. Various values
for the constants _α,_ _β_ reproduce the Ergun relation (applicable to
beds packed with beads or granules), or forms appropriate to beds
packed with cylinders, foams and laminates [17]. With _α_ = _S_ = 0
Darcy’s law is retrieved. Including the sink term we have not been
able to find this relation in the sorption literature, but it is a natural consequence of momentum conservation with mass loss. Away
from the sorption front we expect the sink term to be small and
its neglect is justifiable, however in regions of rapid mass transfer
it plays a significant role in the mass balance and it is possible that
this also leads to significant momentum loss.


_2.3._ _Summary_ _of_ _governing_ _equations_



_∂x_




[2]
= _[∂][c]_
���� _∂x_
_x_ = _L_ [−]



_,_ (17)
�����
_x_ =0 [+]




    _(ρu)_ | _x_ =0− = _ρu_ - _D_ _[∂ρ]_



_∂x_



where the - _,_ + superscripts indicate just before and just after _x_ =
0. Separating the concentrations gives




    _u(_ 0 [−] _,_ _t)c_ 10 =

    _u(_ 0 [−] _,_ _t)c_ 20 =



_∂x_



�����
_x_ =0 [+]



_x_ =0


_,_ (18)
�����
_x_ =0 [+]




[1]
_uc_ 1 - _D_ _[∂][c]_



_∂x_




[2]
_uc_ 2 - _D_ _[∂][c]_



where _c_ 10, _c_ 20 are the concentrations of the inlet gas and
_u(_ 0 [−] _,_ _t)_ = _Q_ 0 _/(π_ _R_ [2] _),_ _u(_ 0 [+] _,_ _t)_ = _Q_ 0 _/(ϵπ_ _R_ [2] _)_ .
At the exit we move to a region where no mass transfer occurs,
so it is assumed that whatever the density on leaving the column
it remains the same just outside the exit



_∂c_ 1



_∂x_



= 0 _._ (19)
����
_x_ = _L_ [−]



Noting that _ρ_ = _M_ 1 _c_ 1 + _M_ 2 _c_ 2 we may eliminate the gas density
from the mass balance
_∂_ [2]
_∂t_ _[(][M]_ [1] _[c]_ [1] [+] _[M]_ [2] _[c]_ [2] _[)]_ [+] _∂_ _[∂]_ _x_ _[(][u][(][M]_ [1] _[c]_ [1] [+] _[M]_ [2] _[c]_ [2] _[))]_ [=] _[D]_ _∂_ _[∂]_ _x_ [2] _[(][M]_ [1] _[c]_ [1] [+] _[M]_ [2] _[c]_ [2] _[)]_



_∂_ _[∂]_ _x_ _[(][u][(][M]_ [1] _[c]_ [1] [+] _[M]_ [2] _[c]_ [2] _[))]_ [=] _[D]_ _∂_ _[∂]_ _x_ [2][2]



_∂x_ [2] _[(][M]_ [1] _[c]_ [1] [+] _[M]_ [2] _[c]_ [2] _[)]_



The pressure at inlet and outlet are


_p(_ 0 _,_ _t)_ = _p_ 0 _(t)_ _,_ _p(L)_ = _pa._ (20)


The inlet value may vary with time. Initially we assume the solid
is fresh and the column is free of the component to be removed


_p(x)_
_ρ(x,_ 0 _)_ = _M_ 2 _c_ 2 _(x,_ 0 _)_ = _M_ 2 _q(x,_ 0 _)_ = 0 _,_ (21)

_RT_ _[,]_


hence

_c_ 1 _(x,_ 0 _)_ = 0 _,_ _c_ 2 _(x,_ 0 _)_ = _[p][in][(][x][)]_ (22)

_RT_ _[,]_


where the initial pressure _pin(x)_ = _p_ 0 _(_ 0 _)_ - _(p_ 0 _(_ 0 _)_ - _pa)x/L_ .




_[q]_

- _(_ 1 - _ϵ)ρqMq_ _[∂]_ (11)

_∂t_ _[.]_



Conservation of each species then gives



_∂c_ 1



_∂c_ 1

_[∂]_
_∂t_ [+] _∂x_


_∂c_ 2

_[∂]_
_∂t_ [+] _∂x_




[2] _[c]_ [1] [1] [−] _[ϵ][)][ρ][q]_ _Mq_ _∂q_

_∂x_ [2] [−] _[(]_ _M_ 1 _∂t_



_∂x_ [2] _[.]_ (13)



_∂t_ _[,]_ (12)



_∂c_ 2




[2] _[c]_ [1]
_∂_ _[∂]_ _x_ _[(][uc]_ [1] _[)]_ [=] _[D]_ _[∂]_ _∂x_ [2]


[2] _[c]_ [2]
_∂_ _[∂]_ _x_ _[(][uc]_ [2] _[)]_ [=] _[D]_ _[∂]_ _∂x_ [2]


4 _T.G._ _Myers_ _and_ _F._ _Font_ _/_ _International_ _Journal_ _of_ _Heat_ _and_ _Mass_ _Transfer_ _163_ _(2020)_ _120374_



**3.** **Non-dimensionalisation**


We scale variables in the following manner




[−] _[p][a]_
_p_ ˆ = _[p]_




[−] _[p][a]_ [1]

_c_ ˆ1 = _[c]_
_�p_ _[,]_ _c_ 10




[1] [2]

_c_ _[c]_ 10 _,_ _c_ ˆ2 = _c_ _[c]_ 20




[2]

_[c]_ _,_ _q_ ˆ = _[q]_

_c_ 20 _q_ ~~[∗]~~ 0



_,_
_q_ ~~[∗]~~ 0



_x_ ˆ = _[x]_



_L_ _[x]_ _[,]_ _t_ [ˆ] = _�_ _[t]_ _t_




_�_ _[t]_ _t_ _[,]_ _u_ ˆ = _u_ _[u]_ 0



_,_ (23)
_u_ 0



where _L_ and _�t_ are unknown and _q_ ~~[∗]~~ 0 [is] [the] [value] [of] _[q]_ ~~[∗]~~ [at] _[t]_ [=] [0][.]
Since our interest lies with the reaction we choose a time-scale
_�t_ = 1 _/kq_ and so


_∂q_ ˆ
= _(q_ ˆ [∗]  - _q_ ˆ _)_ _._ (24)
_∂t_ [ˆ]


Balancing advection with mass loss gives the length-scale _L_ =
_u_ 0 _c_ 10 _/((_ 1 - _ϵ)ρqq_ [∗] 0 _[k][q][)]_ [and] [then]


_c_ [ˆ] 1 [2] _c_ [ˆ] 1 _q_ [ˆ]
_δ_ 1 _[∂]_ _∂t_ [ˆ] + _∂_ _[∂]_ _x_ ˆ _[(]_ _u_ [ˆ] _c_ ˆ1 _)_ = _δ_ 2 _[∂]_ _∂x_ ˆ [2] [−] _[∂]_ _∂t_ [ˆ] _,_ (25)


_c_ [ˆ] 2 [2] _c_ [ˆ] 2
_δ_ 1 _[∂]_ _∂t_ [ˆ] + _∂_ _[∂]_ _x_ ˆ _[(]_ _u_ [ˆ] _c_ ˆ2 _)_ = _δ_ 2 _[∂]_ _∂x_ ˆ [2] _[.]_ (26)


In experiments the main gas component is not usually the one being removed, hence we assume _c_ 10 _<_ _c_ 20 and write

      -       1 + _δ_ 3 _p_ ˆ = _δ_ 4 _c_ ˆ2 + _δ_ 5 _c_ ˆ1 _,_ (27)




        _p_ [ˆ]

- _[∂]_ _∂x_ ˆ [=] _[δ]_ [6] _[(]_ _c_ [ˆ] 2 + _δ_ 7 _c_ ˆ1 _)u_ ˆ [2] +



_q_ [ˆ]
1 + _δ_ 8 _[∂]_
_∂t_ [ˆ]







_u_ ˆ _,_ (28)



where, assuming the flow to be close to Darcy flow, we have set
the pressure scale _�p_ = _βu_ 0 _L_ .
The boundary and initial conditions are



_,_ (29)
�����
_x_ ˆ=0 [+]



**4.** **Application** **to** **carbon** **capture** **in** **a** **packed** **column**


Standard models for carbon capture in a packed column may
be found in the reviews of [10,11,16]. In general these are based on
the following assumptions:


1. The gas behaves as an ideal gas.
2. A plug-flow model is adopted.
3. The radial variation of concentration is negligible.
4. The bed operates isothermally.
5. The CO2 concentration is low so that the pressure gradient is
linear and the velocity constant along the bed.


Assumption 3 follows from 2 (although in mathematical terms
the radial variation is the source of the mass sink term, see [12]).
In experimental studies CO2 typically comprises 15–20% which, as
we will see later, leads to velocity variation of the same order and
non-linear pressure, hence we do not apply assumption 5. We have
retained the isothermal and ideal gas assumptions (in [12] it was
shown that the temperature variation is small during carbon capture).
A typical experimental set-up involves a circular cross-section
column containing a porous material, this is then placed inside
an oven or furnace to regulate the temperature. Gas is passed
through the column and the concentration measured at the outlet. Here we consider a specific experiment which involves a CO2,
N2 mixture passing through a bed of activated carbon, the data
and operating conditions are given in Table 1, see [12,13]. Mass
transfer was by adsorption. A mass flow controller was employed
to maintain a constant flow rate _Q_ 0 = 50 ml/min, which indicates
_u_ 0 = 50 × 10 [−][6] _/(_ 60 _ϵπ_ _R_ [2] _)_ = 0 _._ 019 m _/s_ . A full description of the experiment may be found in [13].
We assume that the flow rate within the porous media
is described by the Ergun relation, hence the constants of
equation (16) are defined by

_α_ = [1] _[.]_ [75] _[(]_ [1] [−] _[ϵ][)]_ ≈ 2 _._ 11 × 10 [3] _,_

_dpϵ_

_β_ = [150] _[μ][g][(]_ [1] [−] _[ϵ][)]_ [2] ≈ 3 _._ 86 × 10 [3] _,_ (34)

_d_ [2] _p_ _[ϵ]_ [2]


where _dp_ = 6 _._ 5 × 10 [−][4] m. The length-scale _L_ ≈ 3 _._ 75cm which indicates the size of the reaction zone. The pressure scale _�p_ = _βu_ 0 _L_ ≈
14 _._ 62Pa, then using values from Table 1 and the definitions (32,33)
we determine


_δ_ 1 = 0 _._ 027 _,_ _δ_ 2 ∼ 0 _._ 036 _,_ _δ_ 3 ∼ 1 _._ 44 × 10 [−][4] _,_
_δ_ 4 = 0 _._ 85 _,_ _δ_ 5 ≈ 0 _._ 18 _,_ (35)


_δ_ 6 = 3 _._ 3 × 10 [−][3] _,_ _δ_ 7 = 0 _._ 28 _,_ _δ_ 8 = 3 _._ 47 × 10 [−][5] _._ (36)


For a kinetic model we take the version described in [13] since this
provides the parameter values for this specific experiment,

_q_ ~~[∗]~~ = ~~�~~ 1 + _q(KmT_ 11 _KpT)_ 1 _[n]_ _p_ [1] ~~[�]~~ [1] _[/][n]_ [1] [+] ~~�~~ 1 + _q(KmT_ 22 _KpT)_ 2 _[n]_ _p_ [2] ~~[�]~~ [1] _[/][n]_ [2] _[,]_ (37)


where _qm_ 1 _,_ _qm_ 2 = 0 _._ 69 _,_ 3 _._ 57 mol/kg, _KT_ 1 _,_ _KT_ 2 = 8 _._ 14 × 10 [4] _,_ 0 _._ 66
atm [−][1] _,_ _n_ 1 _,_ _n_ 2 = 0 _._ 27 _,_ 0 _._ 65. Note, the variation with temperature
discussed in that paper does not apply to the present isothermal
study. In non-dimensional form we write

_q_ ~~[∗]~~ 0 _q_ [ˆ] = [1 + _q(KmT_ 11 _KpTa_ 1 _(p_ 1 _a(_ +1 _δ_ +3 _pδ_ ˆ _))_ 3 _p_ ˆ _[n]_ _)_ [1] ] [1] _[/][n]_ [1]

+ _qm_ 2 _KT_ 2 _pa(_ 1 + _δ_ 3 _p_ ˆ _)_ (38)

[1 + _(KT_ 2 _pa(_ 1 + _δ_ 3 _p_ ˆ _))_ _[n]_ [2] ] [1] _[/][n]_ [2] _[.]_




  
1 =




    
_,_ 1 =
�����
_x_ ˆ=0 [+]



_u_ ˆ _c_ ˆ1 - _δ_ 2 _[∂]_ _c_ [ˆ] 1
_∂x_ ˆ



_u_ ˆ _c_ ˆ2 - _δ_ 2 _[∂]_ _c_ [ˆ] 2
_∂x_ ˆ



_c_ [ˆ] 2
= _[∂]_
���� _∂x_ ˆ
_x_ ˆ= _L_ [ˆ][−]



_∂c_ ˆ1
_∂x_ ˆ



= 0 _p_ ˆ _(_ 0 _,_ _t_ [ˆ] _)_ = _p_ ˆ0 _(t_ [ˆ] _)_ _p_ ˆ _(L_ [ˆ] _)_ = 0 _,_ (30)
����
_x_ ˆ= _L_ [ˆ][−]



_c_ ˆ1 _(x_ ˆ _,_ 0 _)_ = 0 _,_ _δ_ 4 _c_ ˆ2 _(x_ ˆ _,_ 0 _)_ = 1 + _δ_ 3 _p_ ˆ _in,_ _q_ ˆ _(x_ ˆ _,_ 0 _)_ = 0 _,_ (31)


where the initial pressure profile _p_ ˆ _in_ = _p_ ˆ0 _(_ 0 _)(_ 1 - _x_ ˆ _/L_ [ˆ] _)_ . To keep the
model general we express the pressure condition at _x_ ˆ = 0 as an
unspecified function of time. If the inlet pressure is kept constant
at a given value then _p_ ˆ _(_ 0 _,_ _t_ [ˆ] _)_ = 1 _,_ however in a number of experiments the flux is maintained as the constant (via a flow meter)
and this requires a variable inlet pressure. This is then determined
as part of the solution process.
The five equations (24)–(28), together with the appropriate
boundary conditions, are sufficient to determine the five unknowns
_c_ ˆ1 _,_ _c_ ˆ2 _,_ _q_ ˆ _,_ _p_ ˆ _,_ _u_ ˆ. They contain eight non-dimensional groupings, _δi_,
which indicate the relative importance of the terms




_[k][q]_
_δ_ 1 = _[L]_



_,_
_Lu_ 0




_[k][q]_ _c_ 10

_[L]_ _u_ 0 = _(_ 1 - _ϵ)ρqq_ ~~[∗]~~ 0 _,_ _δ_ 2 = _L_ _[D]_ _u_ 0



_δ_ 3 = _[�][p]_



_,_ (32)
_pa_




_[�]_ _pa_ _[p]_ _,_ _δ_ 4 = _[R][g]_ _p_ _[T]_ _a_ _[c]_ [20]



_c_ _[c]_ 20 [10] _,_ _δ_ 6 = _[α][M]_ [2] _�_ _[c]_ [20] _p_ _[u]_ [2] 0 _[L]_ _,_ _δ_ 7 = _M_ _[M]_ 2 [1] _c_ _[c]_ 20 [10]




[10]
_δ_ 5 = _[c]_ _,_



_,_
_M_ 2 _c_ 20



_δ_ 8 = [1] [−] _[ϵ]_ _ρqM_ 1 _q_ ~~[∗]~~ 0 _[k][q][.]_ (33)

_β_


_T.G._ _Myers_ _and_ _F._ _Font_ _/_ _International_ _Journal_ _of_ _Heat_ _and_ _Mass_ _Transfer_ _163_ _(2020)_ _120374_ 5


**Table** **1**
Values of the thermophysical parameters mainly taken from [13], except _kq_, _ρ_ _q_ (as discussed later).


Symbol Value Dimension


Initial concentration (CO2) _c_ 10 6.03 mol/m [3]

Initial concentration (N2) _c_ 20 34.19 mol/m [3]



Molar mass (CO2) _M_ 1 0.044 kg/mol
Molar mass (N2) _M_ 2 0.028 kg/mol
Temperature _T_ 303.15 K
Ambient pressure _pa_ 101325 (1) Pa (Atm)
Adsorption saturation _q_ ¯ [∗] 1.57 mol/kg
Bed void fraction _ϵ_ 0.56 Bed length _L_ 0.2 m
Bed radius _R_ 0.005 m
Diameter of bed particles _dp_ 6.5 ×10 [−][4] m
Gas viscosity (15% CO2 (1.5), 85% N2 (1.8)) _μg_ 1 _._ 76 × 10 [−][5] Pa s
Density of adsorbed CO2 _ρ_ _q_ 325 kg/m [3]



Axial diffusion coefficient _D_ 2 _._ 57 × 10 [−][5] m [2] /s
Initial volume fraction (CO2) _y_ 1 0.15 Initial volume flux _Q_ 8 _._ 3 × 10 [−][7] m [3] /s
Initial interstitial velocity _u_ 0 0.019 m/s
Adsorption rate constant (CO2) _kq_ 0.0137 s [−][1]



Solid/gas density _ρ_ _s_ / _ρ_ _g_ 1818/1.2 kg/m [3]



Neglecting terms of order _δ_ 3 ∼ 10 [−][4] we see that the leading order
equation for _q_ ˆ is
_∂q_ ˆ
_∂t_ [=] [1] [−] _q_ [ˆ] _,_ (39)

where the (constant) adsorbent scaling is

_q_ ~~[∗]~~ 0 [=] ~~�~~ 1 + _q(KmT_ 11 _KpTa_ 1 _)p_ _[n]_ _a_ [1] ~~[�]~~ [1] _[/][n]_ [1] [+] ~~�~~ 1 + _q(KmT_ 22 _KpTa_ 2 _)p_ _[n]_ _a_ [2] ~~[�]~~ [1] _[/][n]_ [2] _[.]_ (40)


Neglecting terms of order _δ_ 1 _,_ _δ_ 2 ∼ 10 [−][2] the concentration equations are
_∂_ - - _q_ [ˆ]
_∂x_ ˆ _u_ ˆ _c_ ˆ1 = - _[∂]_ _∂t_ [ˆ] _,_ (41)


_∂_
_∂x_ ˆ _[(]_ _u_ [ˆ] _c_ ˆ2 _)_ = 0 _._ (42)


These simply state that gas is primarily advected through the column, with the only variation coming through the mass loss due
to adsorption. In a constant velocity study [12] the leading order _c_ 1 equation was discussed, where it was pointed out that although diffusion is, in general small, it can play an important role
in the numerical solution. If we have an initial condition where the
CO2 concentration is zero and then jumps to some non-zero value
when first pumped in then the gradient is discontinuous and diffusion is important in smoothing this out. However, this is only
important near _x_ = _t_ = 0. For the present we will focus mainly on
the outlet, close to first breakthrough and so neglect diffusion (except in Fig. 5 where we compare the approximate solutions with
numerics to verify the validity of this approach).
The leading order pressure relations are

   -    1 = _δ_ 4 _c_ ˆ2 + _δ_ 5 _c_ ˆ1 _,_ (43)


_p_ [ˆ]

- _[∂]_ _∂x_ ˆ [=] _u_ [ˆ] _._ (44)


The form of the non-dimensional gas law, (43), is very informative: the relative change in pressure along the column is tiny compared to the total pressure, hence the pressure variation along the
column has a negligible effect on the concentration and we may
write one concentration in terms of the other, irrespective of the
pressure or velocity,

_c_ ˆ2 = _δ_ [1] 4 - _δ_ 5 _c_ ˆ1 _._ (45)



The scaling of the momentum balance (44) shows that for this case
the Ergun relation is unnecessarily complicated: momentum loss is
dominated by viscous resistance between the gas and porous material. Hence velocity is related to pressure drop via a simple Darcy
law.
The necessary leading order boundary and initial conditions are

1 = [�] _u_ ˆ _c_ ˆ1��� _x_ ˆ=0 [+] 1 = [�] _u_ ˆ _c_ ˆ2��� _x_ ˆ=0 [+] _[,]_ (46)



_c_ [ˆ] 2
= _[∂]_
���� _∂x_ ˆ ����
_x_ ˆ= _L_ [ˆ][−]



_∂c_ ˆ1
_∂x_ ˆ



= 0 _q_ ˆ _(x_ ˆ _,_ 0 _)_ = 0 _._ _,_ (47)
����
_x_ ˆ= _L_ [ˆ][−]



Integration of equation (42) shows that _u_ ˆ _c_ ˆ2 = 1 everywhere. Combining this with equation (45) transforms the mass balance
(41) to



_q_ [ˆ]
= - _[∂]_ _,_ (48)
_∂t_ [ˆ]



_δ_ 4 _[∂]_




_c_ ˆ1
1  - _δ_ 45 _c_ ˆ1







_∂x_ ˆ



where _δ_ 45 = _δ_ 4 _δ_ 5 ≈ 0 _._ 15. The factor _δ_ 4 _/(_ 1 - _δ_ 45 _c_ ˆ1 _)_ does not appear
in the constant velocity system of [12]. Since _δ_ 4 = 0 _._ 85 this indicates a change in size of quantities of the order 15% when compared to constant velocity models. Equation (48) must be solved
in conjunction with the adsorbent equation, (39) and then _u_ ˆ _,_ _c_ ˆ2 _,_ _p_ ˆ
may be obtained from the preceding equations.
The above equations hold behind the reaction front, _x_ ˆ ≤ _s_ ˆ.
Ahead we have _c_ ˆ1 = _q_ ˆ = 0 and so, from (45), _c_ ˆ2 = 1 _/δ_ 4 is constant
and hence so is _u_ ˆ = _δ_ 4 (i.e. the velocity ahead of the front is 15%
lower than the inlet velocity).


_4.1._ _Travelling_ _wave_


Equations (39,48) may be solved numerically to find the behaviour for all time although, due to the neglect of diffusion, the
very early time solution may be inaccurate. For sufficiently large
times, such that the initial transient is complete, we do not even
need a numerical solution since there exists a travelling wave solution. To find this we first choose a co-ordinate moving with the
_c_ 1 front, _η_ = _x_ ˆ − _s_ ˆ _(t_ [ˆ] _)_ . Equations (39,48) then become

_∂_ _f_ [ˆ] _∂q_ ˆ
_s_ [ˆ] _t_ ˆ (49)
_∂η_ ˆ [=] _∂η_ _[,]_

- _s_ ˆ _t_ ˆ _∂q_ ˆ [�] 1 - _q_ ˆ [�] _,_ (50)
_∂η_ ˆ [=]


6 _T.G._ _Myers_ _and_ _F._ _Font_ _/_ _International_ _Journal_ _of_ _Heat_ _and_ _Mass_ _Transfer_ _163_ _(2020)_ _120374_



where _f_ [ˆ] = _u_ ˆ _c_ ˆ1 = _δ_ 4 _c_ ˆ1 _/(_ 1 - _δ_ 45 _c_ ˆ1 _)_ . A travelling wave solution may
be found if _s_ ˆ _t_ ˆ [=] _[v]_ [ˆ] [is] [constant.] [If] [this] [is] [the] [case] [the] [equation] [for] _f_ [ˆ]
may be integrated immediately. After applying the boundary conditions _c_ ˆ1 = _f_ [ˆ] = _q_ ˆ = 0 at _η_ ˆ = 0 we obtain

_f_ ˆ = _v_ ˆ _q_ ˆ _._ (51)


Eliminating _q_ ˆ between (49)–(51) leads to an ODE


_f_ [ˆ]
_v_ ˆ _∂_ _[∂]_ _η_ ˆ [−] _f_ [ˆ] = - _v_ ˆ _,_ (52)


with solution

_f_ ˆ = _v_ ˆ [�] 1 - _eη_ [ˆ] _/v_ ˆ [�] _._ (53)


The constant of integration in this case has been obtained by applying the condition at _η_ ˆ = 0. The velocity may be determined by
assuming the front is far from the column entrance, _x_ ˆ = 0 _,_ hence
_η_ ˆ = _x_ ˆ − _s_ ˆ is large and negative, formally we apply _η_ ˆ → −∞ _,_ _u_ ˆ _c_ ˆ1 =
_f_ ˆ → 1 which determines _v_ ˆ = 1. This verifies the travelling wave assumption that _s_ ˆ _t_ ˆ [is] [constant.]
The CO2 concentration may be calculated from (53), with _v_ ˆ =
1 _,_




_[g][T]_
_p_ = _pa_ + _β_ _[R]_ _pa_ _u_ 0 _c_ 20 _(L_ - _x)._ (59)



For _x_ ∈ [0, _s_ ]




1    - _e_ _[(][x]_ [−] _[L][)][/][L]_ _e_ [−] _[k][q][(][t]_ [−] _[t][b][)]_







_c_ 1 = _c_ 10



1 - _(RgTc_ 10 _/pa)e_ _[(][x]_ [−] _[L][)][/]_ _v_ [ˆ] _Le_ - _kq(t_ - _tb)_



_,_ (60)


_,_ (61)




1
1  - _(RgTc_ 10 _/pa)e_ _[(][x]_ [−] _[L][)][/][L]_ _e_ [−] _[k][q][(][t]_ [−] _[t][b][)]_







_c_ 2 = _c_ 20




   _q_ = _q_ ~~[∗]~~ 0 1 - _e_ _[(][x]_ [−] _[L][)][/][L]_ _e_ [−] _[k][q][(][t]_ [−] _[t][b][)]_ [�] _,_ (62)


   _u_ = _u_ 0 1 - _(RgTc_ 10 _/pa)e_ _[(][x]_ [−] _[L][)][/][L]_ _e_ [−] _[k][q][(][t]_ [−] _[t][b][)]_ [�] _,_ (63)




      
_[g][T]_
_p_ = _pa_ + _βu_ 0 _(s_ - _x)_ - _[R]_



_p_ _[g]_ _a_ _c_ 10 _L(_ 1 - _e_ _[(][x]_ [−] _[L][)][/][L]_ _e_ [−] _[k][q][(][t]_ [−] _[t][b][)]_ _)_




     
_[g][T]_

_pa_ _c_ 20 _(L_ - _s)_ _._ (64)



+ _[R][g][T]_



1     - _eη_ [ˆ]
_c_ ˆ1 =



1   - _eη_ [ˆ] 1   - _eη_ [ˆ]

_δ_ 4 + _δ_ 45 _(_ 1 - _eη_ [ˆ] _)_ [≈] 1 - _δ_ 45 _e_



(54)
1 - _δ_ 45 _eη_ [ˆ] _[.]_



In experiments it is common to measure the breakthrough
curve. The analytical representation is obtained by setting _x_ = _L_ in
equation (60)




1    - _e_ [−] _[k][q][(][t]_ [−] _[t][b][)]_







The simplification results from _δ_ 4 + _δ_ 45 = _p_ 0 _/pa_ = 1 + _δ_ 3 ≈ 1. Then
from (45,51) and using _u_ ˆ _c_ ˆ2 = 1 _,_ _δ_ 4 ≈ 1 - _δ_ 45 we find

_c_ ˆ2 = 1 - 1 _δ_ 45 _eη_ [ˆ] _[,]_ _u_ ˆ = 1 - _δ_ 45 _eη_ [ˆ] _,_ _q_ = 1 - _eη_ [ˆ] _._ (55)


The pressure equation (44) may be written as _p_ ˆ _η_ = - _u_ ˆ. For _x_ ˆ ≥ _s_ ˆ _,_
_u_ ˆ = _δ_ 4 is constant and with _p_ ˆ = 0 at _η_ ˆ = _L_ [ˆ] - _s_ ˆ we obtain

_p_ ˆ = _δ_ 4 _((L_ [ˆ] - _s_ ˆ _)_ - _η_ ˆ _)_ for _x_ ˆ ≥ _s_ ˆ _._ (56)


For _x_ ˆ ≤ _s_ ˆ the velocity is specified by (55). The pressure at the column inlet is unknown but equation (56) gives the value at _x_ ˆ = _s_ ˆ
( _η_ ˆ = 0), which may be used to determine the constant of integration, leading to

_p_ ˆ = _δ_ 4 _(L_ [ˆ] - _s_ ˆ _)_ - [�] _η_ ˆ + _δ_ 45 _(_ 1 - _eη_ [ˆ] _)_ [�] for _x_ ˆ ≤ _s_ ˆ _._ (57)


To relate the solutions to experiments requires switching between
_η_ ˆ and _x_ ˆ _,_ _t_ [ˆ] . With the definition _s_ ˆ _t_ ˆ [=] [1] [we] [obtain] _s_ [ˆ] = _t_ [ˆ] + _s_ ˆ0 (where
_s_ ˆ0 is unknown) and hence _η_ ˆ = _x_ ˆ − _t_ [ˆ] - _s_ ˆ0. The travelling wave is
not valid at _t_ [ˆ] = 0 so we cannot apply an initial condition to determine _s_ ˆ0 and must use information from a later time. In the carbon
capture literature the breakthrough curve is generally presented,
which shows the CO2 concentration at the end of the column. If
CO2 is first recorded at the outlet at time _t_ [ˆ] _b,_ then we may use
_s_ ˆ0 = _L_ [ˆ] - _t_ [ˆ] _b_ . However, given the uncertainty as to when gas actually
first escapes, a more reliable measure is to note the time _t_ 1 _/_ 2 when
_c_ 1 = _c_ 10 _/_ 2 and then solve equation (54) with _x_ ˆ = _L_ [ˆ] _,_ _c_ ˆ1 = 1 _/_ 2 to determine _s_ ˆ0 = _L_ [ˆ] - _t_ [ˆ] 1 _/_ 2 + log _(_ 2 - _δ_ 45 _)_ or alternatively we may write
_t_ ˆ _b_ = _t_ [ˆ] 1 _/_ 2 - log _(_ 2 - _δ_ 45 _)_ .


_4.2._ _Dimensional_ _solutions_


We now summarise, in dimensional form, the solutions starting with the simplest region, ahead of the front _x_ ≥ _s_, where _s_ =
_Lkqt_ + _s_ 0 = _L_ + _Lkq(t_ - _tb),_ and _tb_ could be set as the experimentally measured breakthrough time or we use _tb_ = _t_ 1 _/_ 2 - log _(_ 2 _(RgTc_ 10 _/pa))/kq_ and the length-scale _L_ = _u_ 0 _c_ 10 _/((_ 1 - _ϵ)ρqq_ ~~[∗]~~ 0 _[k][q][)]_ [.]
The velocity of the front _s_ ˆ _t_ ˆ [=] [1] [indicates] _[s][t]_ [=] _[L][/][�][t]_ [=] _[u]_ [0] _[c]_ [10] _[/][((]_ [1] [−]
_ϵ)ρqq_ ~~[∗]~~ 0 _[)]_ [.]
For _x_ ∈ [ _s,_ _L_ ] and _t_ _<_ _tb_ :



_c_ 1 = _c_ 10



1 - _(RgTc_ 10 _/pa)e_ [−] _[k][q][(][t]_ [−] _[t][b][)]_



_,_ (65)



where _t_ ≥ _tb_ .


_4.3._ _Fixed_ _pressure_ _solution_



In the case studied above the flux is fixed by a flowmeter: the
pressure is adjusted to maintain a constant flow rate. However it
is also common practice to fix the pressure at either end and leave
these constant throughout the experiment. For a fixed flux (constant _u_ 0) equations (59,64) determine the pressure ahead of and
behind the front respectively for the specified value of _u_ 0. If the
pressure is fixed such that _p(_ 0 _,_ _t)_ = _p_ 0 _,_ _p(L,_ _t)_ = _pa_ then ahead of
the front equation (59) holds, while behind



_p_ _[g]_ _a_ _[T]_ _c_ 10 _Le_ [−] _[k][q][(][t]_ [−] _[t][b][)]_ [�] _e_ _[(][x]_ [−] _[L][)][/][L]_ - _e_ [−] _[L][/][L]_ [��] _x_ ≤ _s._




      
_[g][T]_
_p_ = _p_ 0 - _βu_ 0 _x_ - _[R]_



(66)


Since the pressure is continuous at the front we may equate these
two expressions at _x_ = _s_ to determine the velocity _u_ 0 caused by
the prescribed pressure drop



_u_ 0 = _[p]_ [0] [−] _[p][a]_



_p_ _[g]_ _a_ _[T]_ - _c_ 20 _(L_ - _s)_ - _c_ 10 _Le_ [−] _[k]_ _q_ _[(][t]_ [−] _[t]_ _b_ _[)]_ [�] _e_ _[(][s]_ [−] _[L][)][/][L]_ - _e_ [−] _[L][/][L]_ [���][−][1] _._



_β_




_s_ + _[R][g][T]_



_R_ _[p]_ _g_ _[a]_ _T_ _[,]_ _q_ = 0 _,_ _u_ = _[R][g]_ _p_ _[T]_ _a_ _[c]_ [20]




_[a]_
_c_ 1 = 0 _,_ _c_ 2 = _[p]_



_pa_ _u_ 0 _,_ (58)



(67)


The inlet flux _Q_ 0 _(t)_ = _ϵπ_ _R_ [2] _u_ 0 _(_ 0 _,_ _t)_ is then obviously timedependent.


_4.4._ _Carbon_ _capture_ _results_


In Fig. 1 we show the variation along the column of the concentration of CO2, N2, the amount of adsorbed material and the
velocity of the mixture as predicted by equations (58,60–63). The
parameter values used are provided in Table 1. The results correspond to a time _t_ = 0 _._ 9 _tb,_ where _tb_ = 10 _._ 9 min is the breakthrough time quoted in [13]. As expected from a physical point of
view, the CO2 concentration is almost unity at the inlet and decreases smoothly to zero at the front. The non-dimensionalisation
shows that _q_ ˆ differs from _c_ ˆ1 by a factor of order 1 _/(_ 1 - _δ_ 45 _),_ where
_δ_ 45 ≈ 0.1, and so _c_ 1 must be very similar to _q_ ¯. This may be observed through the close proximity of the two curves. This means


_T.G._ _Myers_ _and_ _F._ _Font_ _/_ _International_ _Journal_ _of_ _Heat_ _and_ _Mass_ _Transfer_ _163_ _(2020)_ _120374_ 7



**Fig.** **1.** Concentrations _c_ 1( _x,_ _t_ ), _c_ 2( _x,_ _t_ ), amount adsorbed _q_ ¯ _(x,_ _t)_ and velocity _u_ along
the column at _t_ = 0 _._ 9 _tb_ .


that if we are able to influence _q_ ¯ then it will have a corresponding
effect on the CO2 concentration and vice-versa. As CO2 is removed
the velocity of the mixture decreases. Conservation of mass requires that the nitrogen concentration must increase (the increase
is of the order of the initial concentration ratio _c_ 10/ _c_ 20 ≈ 1.178).
Ahead of the front the values become constant since no more CO2
is removed. At the outlet we see that _c_ 2 ≈ 1.18 _c_ 20, _u_ ≈ 0.85 _u_ 0.

Fig. 2 shows the concentrations and velocity at the outlet. Theoretically no CO2 escapes the column until _t_ = 10 _._ 9 minutes, after which the concentration increases to its inlet value at around
17.5 minutes. The amount of adsorbent is not shown in the figure, since it very closely follows the CO2 curve. Both _c_ 1 and _q_ ¯ have
their greatest rate of increase at the breakthrough time, the gradient (with respect to time) then decreases monotonically to zero as
the adsorbent is used up. The theoretical velocity, _u_ ( _L,_ _t_ ), is around
0.85 _u_ 0 until breakthrough, when it increases to the inlet value.
Similarly for the nitrogen concentration, which decreases from
1.18 _c_ 20 to its inlet value. However, we should point out that the


**Fig.** **2.** Concentrations _c_ 1( _L,_ _t_ ), _c_ 2( _L,_ _t_ ) and velocity _u_ ( _L,_ _t_ ) at outlet, _x_ = _L_ . All divided
by their initial values. Also shown is the experimentally measured concentration of
_c_ 1( _L,_ _t_ ) (circles).



**Fig.** **3.** Blow-up of breakthrough curve, showing the predicted _c_ 1( _L,_ _t_ ) and experimental data (circles).


travelling wave solution is not valid at small times, so the curves
may not be accurate near _t_ = 0. The correspondence between the
CO2 concentration and the experimental data of [13] (shown as circles) appears very good, showing a similar level of accuracy to previous published results which typically present curves over a large
time range (which then makes the curves more difficult to distinguish). In Fig. 3 we show a close-up of the comparison between
the predicted CO2 concentration predictions and experiment. At
this scale we observe qualitative differences in the results. In particular we note that the experimental breakthrough is a more gentle process, with _c_ 1 at first slowly increasing to cross the theoretical prediction before increasing in gradient so the two sets of results coincide. We will discuss these differences in more detail in
§5.
In Fig. 4 we show the pressure profile at times _t_ = 0 _._ 5 _tb,_ 0 _._ 9 _tb_ .
The solid line depicts the pressure behind the front, the dashed
line that ahead of it. The dotted line is the linear profile calculated
from - _px_ = _βu_ 0 which indicates _p_ = _pa_ + _βu_ 0 _(L_ - _x)_ . This is the


**Fig.** **4.** Pressure variation along the column for _t_ = 0 _._ 5 _tb_ (red), _t_ = 0 _._ 9 _tb_ (blue). The
dashed section, near the end of the column, shows the pressure ahead of the front.
The standard linear profile (dotted line) is also shown. (For interpretation of the
references to colour in this figure legend, the reader is referred to the web version
of this article.)


8 _T.G._ _Myers_ _and_ _F._ _Font_ _/_ _International_ _Journal_ _of_ _Heat_ _and_ _Mass_ _Transfer_ _163_ _(2020)_ _120374_


**Fig.** **5.** Comparison of numerical (dashed) and travelling wave (solid) results for the same conditions as those of Fig. 1: (a) shows _c_ 1( _x_, 0.9 _tb_ ), _c_ 2( _x_, 0.9 _tb_ ), (b) shows
_q(x,_ 0 _._ 9 _tb),_ _u(x,_ 0 _._ 9 _tb)_ .



profile that would be observed if velocity variation were neglected,
it is also the limit of the present theoretical curves for large time
(when the adsorbent is full and so the velocity is constant). The
variation of _p_ (0, _t_ ) verifies our earlier statement that a flow meter
will have to vary the pressure to maintain a fixed flow rate.
To convince the numerically minded reader of the accuracy of
the travelling wave solution, in Fig. 5 we compare numerical and
travelling wave results. The curves correspond to those presented
in Fig. 1. The dashed lines represent the numerical solution, the
solid lines the travelling wave. Full details of the system solved numerically and the scheme are provided in Appendix A. In Fig. 5a)
we compare the CO2 and N2 concentrations, the CO2 concentration
obviously corresponds to the curves reaching zero around 0.18m.
In the first runs of the code it turned out that there was a small
discrepancy: the numerical solution moved slightly faster than the
travelling wave, by around 4%. The main difference between the
two methods comes from the retention of _δ_ 1, _δ_ 2 in the numerical scheme. The values _δ_ 1 = 0 _._ 027 _,_ _δ_ 2 = 0 _._ 036 suggest errors of the
order 3.6%, so this discrepancy is entirely in line with the approximations made. The diffusion parameter _δ_ 2 controls the spread of
the front while _δ_ 1 = _Lkq/u_ 0 = _c_ 1 _/(_ 1 - _ϵ)ρqq_ ¯ [∗] 0 [relates] [to] [the] [speed.]
The parameter for which we have the least information is _ρq_ consequently we increased this by 4% to _ρq_ = 338kg/m [3] . With this adjustment we achieve the excellent agreement between numerics
and the analytical solution. Fig. 5b) shows the variation of velocity (top curves) and available adsorbate (bottom curves). Again the
agreement is excellent. Consequently we may state that the travelling wave provides solutions within the accuracy of neglected
terms, where here the largest was 0.036. If even higher accuracy
is required then the numerical solution may be used to fine tune
the density of adsorbate.


**5.** **Alternative** **forms** **of** **mathematical** **model**


There exist a variety of breakthrough models designed to model
different sorption processes. Typically they are based on the probability of a component escaping and the amount of material available for mass transfer. For example in [8] the assumptions on the
probability of escape lead to a standard logistic equation for the
concentration _c_ 1 _t_ = _kc_ 1 _(c_ 10 - _c_ 1 _)_ . In this section we discuss a number of mathematically equivalent breakthrough models and also
derive the form of the present model appropriate for describing
incompressible fluid flow. The models are then compared with ex


perimental data for the adsorption of amoxicillin and a dye from
water. It is shown that in these two examples the form of the
previous models is incapable of capturing the whole breakthrough
curve, whereas the forms (compressible and incompressible) presented in this paper both provide a good approximation.


_5.1._ _Previous_ _analytical_ _models_



An early, classic model to describe the concentration and
amount absorbed was developed by Bohart and Adams [9]. They
wrote down a constant velocity model where the time derivative
and diffusion terms are neglected from the conservation equation
for _c_ 1 and the absorption rate depends on the amount already absorbed and the available absorbate
_∂c_ _[BA]_ - _∂q_ _∂x_ [=] [−] _[k]_ _v_ _q_ ~~[∗]~~ - _q_ [�] _c_ _,_ _∂t_ [=] _[k][BA]_ _q_ ~~[∗]~~ - _q_ [�] _c_ _,_ (68)

where _q_ ¯ [∗] is constant. They provide the solution

_c_ = _c_ 0 ~~�~~ (69)
1  - exp _(_  - _kBAc_ 0 _t_ _)_ + exp ~~[�]~~ _kBA_ _q_ ~~[∗]~~ _x/v_  - _c_ 0 _t_ ~~[��]~~ _[,]_

_q_ = 1 - exp ~~[�]~~ _kBA_ ~~�~~ _q_ ~~[∗]~~ _x/v_ ~~[�]~~ + _q_ exp0 ~~[�]~~ _kBA_ ~~�~~ _c_ 0 _t_ - _q_ ~~[∗]~~ _x/v_ ~~[��]~~ _[,]_ (70)


see [9, eq. (21,22)]. The breakthrough curve is obtained by setting
_x_ = _L_ . This is a much abused result and is often misquoted, as discussed in [18]. In fact even in [18] a ‘simplified’ version is studied
which results from neglecting the first exponential in the denominator in (69)

_c_ ≈ _c_ 0 (71)
1 + exp _(kBA(q_ ¯ [∗] _x/v_  - _c_ 0 _t))_ _[.]_

This may be justified by assuming a sufficiently large time such
that exp _(_ - _kBAc_ 0 _t)_ ≪ 1. Equation (71) is often referred to as the
Thomas model [3,6,19]. If we divide the top and bottom by the
exponential term and again assume that an exponential term
is small, exp _(_ - _kBA(q_ ¯ [∗] _x/v_ - _c_ 0 _t))_ ≪ 1 _,_ then we obtain a formula
which is only valid for small concentrations

_c_ ≈ _c_ 0 exp [�] - _kBA_ - _q_ ~~[∗]~~ _x/v_ - _c_ 0 _t_ [��] _,_ (72)


see [3,6,19] for example. It is equivalent to the Wolborska model

[7,19].
In arriving at (71) we assumed exp _(_  - _kBAc_ 0 _t)_ ≪ 1 _,_ usually this is
justifiable after substituting for the parameter values and considering a sufficiently large time. In arriving at (72) we assumed that a




_[BA]_ - _∂q_

_q_ ~~[∗]~~  - _q_ [�] _c_ _,_
_v_ _∂t_



_∂q_ 
_∂t_ [=] _[k][BA]_ _q_ ~~[∗]~~ - _q_ [�] _c_ _,_ (68)


_T.G._ _Myers_ _and_ _F._ _Font_ _/_ _International_ _Journal_ _of_ _Heat_ _and_ _Mass_ _Transfer_ _163_ _(2020)_ _120374_ 9


**Fig.** **6.** Experimental data (circles) for the adsorption of a) congo red dye in water by soil, [19, Fig. 4], b) amoxicillin in water by activated carbon, [5, Fig. 9]. Lines are
least-squares fit to equation (74) (solid), equation (73) (dashed), equation (76) (dotted). (For interpretation of the references to colour in this figure legend, the reader is
referred to the web version of this article.)



second exponential is small, leaving an expression where the concentration is proportional to this neglected exponential, hence it is
only valid for small concentrations. Equation (72) is, rather harshly,
usually termed the Bohart-Adams equation instead of their more
widely applicable result (69). Since it only holds for small _c_ it is
often stated that their model is only valid near the start of breakthrough.
We now focus on the breakthrough curve and write
equation (71) at _x_ = _L_ in a slightly more general form




1
1 + _A_ 0 exp _(_ - _A_ 1 _t_ _)_







_c_ 1 = _c_ 10



_,_ (73)



where for the Bohart-Adams model _A_ 0 = exp _(kBAq_ ¯ [∗] _L/v),_ _A_ 1 = _kBAc_ 0.
This form also covers the Yoon-Nelson, Thomas and Bed Depth Service Time models where the parameters _A_ 0, _A_ 1 have slightly different interpretations in each case (see Table 3 in the review paper [7]). However, since each involve some fitting to experimental
data they are mathematically equivalent. Similarly we may write
the present model, equation (65), as




1 - _A_ 2 exp _(_ - _A_ 3 _t_ _)_
1 - _A_ 4 exp _(_ - _A_ 3 _t_ _)_







_c_ 1 = _c_ 10



_,_ (74)



_5.3._ _Results_


In Figs. 6a), b) we show comparisons of the current model
against data for the removal of dye [19] and amoxicillin [5]. In
each case we determine the time when the concentration is half
the inlet value, _t_ 1/2, from the experimental data (for the dye _t_ 1 _/_ 2 =
28 × 60 s, for the amoxicillin _t_ 1 _/_ 2 = 13 _._ 95 × 60 s) and use this to
eliminate an unknown from each model. For equation (73) we find
_A_ 0 = exp _(A_ 1 _t_ 1 _/_ 2 _),_ for equation (74) _A_ 4 = 2 _A_ 2 - exp _(A_ 3 _t_ 1 _/_ 2 _)_ and for
equation (76) _A_ 5 = exp _(A_ 6 _t_ 1 _/_ 2 _)/_ 2. Then we apply a least-squares fit
to determine the remaining unknowns. The experimental points in
Fig. 6a) relate to the removal of congo red dye from solution after
being passed through soil, see [19, Fig. 4, _H_ = 5 cm]. The solid line
comes from the current model, equation (74) with _A_ 2 = 0 _._ 98 _,_ _A_ 3 =
2 _._ 2 × 10 [−][4] s [−][1] _,_ the dashed line corresponds to equation (73) with
_A_ 1 = 6 _._ 7 × 10 [−][4] s [−][1] _,_ the dotted line (76) with _A_ 6 = 3 _._ 5 × 10 [−][4] _s_ [−][1] .
The experimental points in Fig. 6b) relate to the removal of amoxicillin from water using activated carbon, see [5, Fig. 9]. Again
the solid line represents the current model, equation (74), now
with _A_ 2 = 2 _._ 38 _,_ _A_ 3 = 0 _._ 0016s [−][1] _,_ the dashed line equation (73) with
_A_ 1 = 0 _._ 0048s [−][1] _,_ the dotted line (76) with _A_ 6 = 0 _._ 022s [−][1] . In both
graphs the best fit is provided by the current compressible flow
model. Of the one parameter models the best fit is the present
model for incompressible flow.


_5.4._ _Mass_ _transfer_ _models_


In the above we carried out a least-squares fit to determine the
system unknowns. Other researchers use different methods, such
as linear regression. Whatever the method it is clear that the form
of equation (73), which describes at least four different previous
models, is not capable of producing a better fit to the data used in
Fig. 6 than either of the two current models. However, this is not
to say that the present model solves all problems.
Consider the form of the adsorption equation _q_ ¯ _t_ = _kq(q_ ¯ [∗]  - _q_ ¯ _)_ .
The equilibrium adsorption depends on the total pressure which
varies throughout the column, as shown in Fig. 4. However, it is
usually the breakthrough curve which is measured, this occurs at
the column outlet where the pressure is approximately constant
throughout the process. Since _q_ ¯ increases monotonically from zero
to _q_ ¯ [∗] the rate _q_ ¯ _t_ is greatest at first breakthrough. From the nondimensionalisation it is clear that _c_ 1 differs from _q_ ¯ by a factor of



where _A_ 2 = exp _(kqtb),_ _A_ 3 = _kq,_ _A_ 4 = _(RgTc_ 10 _/pa)A_ 2.


_5.2._ _Incompressible_ _fluid_ _or_ _negligible_ _adsorption_


The model derived in §2 allows for velocity variation due to the
removal of significant amounts of material from the fluid, this affects the density and so is equivalent to a compressible flow. If we
treat the fluid as incompressible or only consider a small amount
of mass transfer then the leading order non-dimensional problem
is governed by

_∂∂c_ ˆ _x_ 1 [=] [−] _[∂]_ _∂qt_ [ˆ][ˆ] _,_ _∂∂qt_ [ˆ] ˆ = 1 - _q_ ˆ _._ (75)

The non-dimensional velocity _u_ ˆ = 1 and the scale _u_ 0 = _Q_ 0 _/(ϵπ_ _R_ [2] _)_ .
The travelling wave analysis then leads to the incompressible form
of equation (65)


_c_ 1 = _c_ 10 _(_ 1 - _A_ 5 exp _(_ - _A_ 6 _t_ _))_ _,_ (76)


where _A_ 5 = exp _(kqtb),_ _A_ 6 = _kq_ .


10 _T.G._ _Myers_ _and_ _F._ _Font_ _/_ _International_ _Journal_ _of_ _Heat_ _and_ _Mass_ _Transfer_ _163_ _(2020)_ _120374_



around _(_ 1 - _δ_ 45 _)_ where _δ_ 45 is small. Consequently the concentration variation with time must have a similar form to that of _q_ ¯ (this
is apparent from Fig. 1) and the highest gradient in concentration therefore also occurs at first breakthrough. This means that,
although the time of first breakthrough will depend on system parameters such as the flow-rate, column length, initial concentration, void fraction etc, _it_ _is_ _the_ _form_ _of_ _the_ _mass_ _transfer_ _model_ _that_
_primarily_ _determines_ _the_ _shape_ _of_ _the_ _breakthrough_ _curve_ .
The two examples shown in Fig. 6 involve experimental data
where the gradient _∂c_ 1/ _∂t_ is greatest at first breakthrough, so the
present linear driving force model results in an excellent fit. The
data presented in Fig. 3 indicates _∂c_ 1/ _∂t_ ≈ 0 at first breakthrough.
Our model does not accurately capture this. Given that the breakthrough curve is similar in form to the mass transfer model, this
behaviour will therefore be replicated with a logistic type model
as suggested in [9]


_q_ ¯ _t_ = _kc_ 1 _(q_ ¯ [∗] - _q_ ¯ _)._ (77)


This form has a zero adsorption rate when there is zero concentration or no transfer sites available, and a maximum close to the
middle of the process. So perhaps the best system to describe
CO2 transfer in a column will involve the current set of equations but with a mass transfer model such as equation (77). Whilst
the transfer of pollutants from a liquid solution best follows the
present model.


**6.** **Conclusion**


In this paper we have developed a mathematical model to describe isothermal mass transfer from a fluid flowing through a
porous medium contained within a cylindrical tube. The model
was kept relatively general, to permit the inclusion of adsorption
and absorption processes and also the removal of relatively large
quantities of material, such that the velocity and pressure vary
nonlinearly along the column.
Since the model permits the removal of a significant amount of
the fluid it is suitable to gas pollutant studies. As the amount removed becomes smaller then the model may be reduced to one
more appropriate to the removal of contaminants in aqueous solutions. Hence we first validated it against experimental data for
CO2 removal by adsorption. Subsequently we considered contaminant removal from aqueous solutions.
Perhaps the key limitation of this work is the assumption of
an isothermal reaction. In a number of studies on carbon capture
it has been shown to be a small effect, similarly, with removal of
trace quantities from a liquid it is clearly small however there are,
no doubt, situations where this will not be an appropriate assumption. The travelling wave solution cannot capture the very early
time behaviour. This may not be viewed as a problem since practical sorption equipment usually runs for very long periods and
the start-up is of little interest. The model reduction was based
on the size of the non-dimensional parameters, their relative size
may change for different materials and experimental set-ups. Consequently they should be checked whenever a new process is investigated.
It was shown that sufficiently far from the inlet a travelling
wave solution holds, thus there is no need for a full numerical
solution. To verify this we compared the travelling wave solution
against the numerics. Results showed that the difference, below
4%, was exactly in line with the terms neglected in the analytical approximation. The numerical solution therefore turned out to
be most useful for fine-tuning the value of the density of material
transferred to the column or the saturation value, otherwise the
travelling wave appears sufficiently accurate.
The travelling wave solution was compared against experimental data for the removal of amoxicillin and dye from water. The



agreement was excellent, it also outperformed standard previous
models.
A key result of the analysis is that the concentration of the material to be removed closely follows the amount of sorbate available. In the CO2 example the difference was less than 10%. The
experimentally observed breakthrough curve may then be used to
guide the form of the mass transfer model. For example, in the
cases of amoxicillin and dye removal the breakthrough curve had
its steepest gradient at first breakthrough which then slowly decreased to zero: this suggests a kinetic relation of the form _qt_ ∝
_q_ [∗] - _q_ . In the case of CO2 removal published data often shows a
small gradient at first breakthrough, suggesting _qt_ ∝ _c(q_ [∗] - _q)_ or
_q(q_ [∗] - _q)_ . Since the pressure near the outlet is approximately ambient the value of _q_ [∗] is constant (with respect to pressure), which
can simplify the breakthrough calculation (there may still be some
temperature variation, which was not considered in this paper).
The analytical solutions provided in our analysis, the gas concentrations, gas velocity, amount of sorbate and pressure as well
as the front velocity, have been shown to accurately describe the
evolution in a cylindrical column. This means that we now have
explicit expressions to describe the role played by the operating
parameters which may then be used to improve or optimise the
process.


**Declaration** **of** **Competing** **Interest**


The authors declare that they have no known competing financial interests or personal relationships that could have appeared to
influence the work reported in this paper.


**CRediT** **authorship** **contribution** **statement**


**T.G.** **Myers:** Conceptualization, Methodology, Investigation, Formal analysis, Writing - original draft, Writing - review & editing. **F.**
**Font:** Validation, Writing - review & editing, Formal analysis, Software.


**Acknowledgements**


F. Font acknowledges financial support from the Juan de la
Cierva programme (grant IJC2018-038463-I) from the Spanish
MICINN and from the _Obra_ _Social_ _la_ _Caixa_ through the programme
_Recerca_ _en_ _Matemàtica_ _Col_ - _laborativa_ . Both authors thank the CERCA
Programme of the _Generalitat_ _de_ _Catalunya_ . T. G. Myers acknowledges financial support from the Ministerio de Ciencia e Innovacin,
Spain Grant No. MTM2017-82317-P.


**Appendix** **A.** **Numerical** **solution**


Numerically solving the full model (24)–(31) can be relatively
complicated, mainly due to the nonlinearities in the momentum
equation (28). However, a reduced version of the model can be
formulated by neglecting terms of order 10 [−][3] by setting _δ_ 3 = _δ_ 6 =
_δ_ 8 = 0 in (24)-(31). The neglect of these terms indicates errors of
the order 0.1% when compared to a solution of the full system.
The governing equations of the reduced model are


_c_ [ˆ] 1 [2] _c_ [ˆ] 1 _q_ [ˆ]
_δ_ 1 _[∂]_ _∂t_ [ˆ] + _∂_ _[∂]_ _x_ ˆ _[(]_ _u_ [ˆ] _c_ ˆ1 _)_ = _δ_ 2 _[∂]_ _∂x_ ˆ [2] [−] _[∂]_ _∂t_ [ˆ] _,_ (A.1)


_c_ [ˆ] 2 [2] _c_ [ˆ] 2
_δ_ 1 _[∂]_ _∂t_ [ˆ] + _∂_ _[∂]_ _x_ ˆ _[(]_ _u_ [ˆ] _c_ ˆ2 _)_ = _δ_ 2 _[∂]_ _∂x_ ˆ [2] _[,]_ (A.2)


_∂q_ ˆ
= _(_ 1  - _q_ ˆ _)_ _,_ (A.3)
_∂t_ [ˆ]


1 = _δ_ 4 _(c_ ˆ2 + _δ_ 5 _c_ ˆ1 _)_ _,_ (A.4)


_T.G._ _Myers_ _and_ _F._ _Font_ _/_ _International_ _Journal_ _of_ _Heat_ _and_ _Mass_ _Transfer_ _163_ _(2020)_ _120374_ 11



_p_ [ˆ]

- _[∂]_ _∂x_ ˆ [=] _u_ [ˆ] _,_ (A.5)



with the boundary conditions



= 0 _,_ (A.6)
����
_x_ ˆ= _l_


= 0 _,_ (A.7)
����
_x_ ˆ= _l_



The set of Eqs. (A.14)–(A.16) are solved using second-order central finite differences in space and explicit Euler in time. The
boundary conditions are discretised using one-sided second-order
finite differences. The nonlinear advection term in (A.14) is dealt
with by using an upwind scheme with the _u_ profile from the previous time step. The scheme was implemented in Matlab, using the
function trapz for the numerical integration of (A.16) (at each node
and time step). The choice of _�t_ and _�x_ ˆ is made ensuring that the
stability criteria _�t_ [ˆ] _δ_ 2 _/(�x_ ˆ [2] _δ_ 1 _)_ ≤ 0 _._ 5 and max _(u_ ˆ _)_ _�t_ [ˆ] _/(�x_ ˆ _δ_ 1 _)_ ≤ 1
are satisfied. The plots shown in Fig. 5 correspond to _�t_ [ˆ] = 0 _._ 5 ×
10 [−][4] and _�x_ ˆ = 0 _._ 05.


**References**


[1] Z. Xu, J.-Q. Cai, B.-C. Pan, Mathematically modeling fixed-bed adsorption in
aqueous systems, J. Zhejiang Univ-Sci A [(Appl.](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0001) Phys. and Eng.) 14(3) (2013)
155–176.

[2] L.S. Tan, A.M. [Shariff,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0002) K.K. Lau, M.A. [Bustam,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0002) Factors affecting CO2 absorption
efficiency in packed column: A review, [J.](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0002) Ind. and Engng Chem. 18 (2012)
18741883.

[3] M.J. [Ahmed,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0003) B.H. [Hameed,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0003) Removal of emerging pharmaceutical contaminants
by adsorption in a fixed bed column: A [review,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0003) Ecotoxicology and Environmental Safety 149 (2018) 257–266.

[4] Z.Z. [Chowdhury,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0004) S.M. Zain, A.K. [Rashid,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0004) R.F. [Rafique,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0004) K. [Khalid,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0004) Breakthrough
curve analysis for column dynamics sorption of mn(II) ions from wastewater
by using mangostana garcinia peel-based granular-activated carbon, Journal of
Chemistry (2013). [10.1155/2013/959761](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0004)

[5] M.A.E. [de](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0005) Franco, C.B. de Carvalho, M.M. [Bonetto,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0005) R. de [Pelegrini](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0005) Soares,
L.A. [Feris,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0005) Removal of amoxicillin from water by adsorption onto activated carbon in batch process and fixed bed [column:](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0005) kinetics, isotherms, experimental
design and breakthrough curves modelling, J. Clean. Prod. 161 (2017) 947–956.

[6] R. [Han,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0006) Y. [Wang,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0006) X. [Zhao,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0006) Y. [Wang,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0006) F. [Xie,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0006) J. [Cheng,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0006) M. [Tang,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0006) Adsorption
of methylene blue by phoenix tree leaf powder in a fixed-bed column: experiments and prediction of breakthrough curves, Desalination 245 (2009)
284–297.

[7] H. Patel, Fixed-bed column adsorption study: a comprehensive review, Appl.
Water Sci. 9 (45) (2016), [doi:10.1007/s13201-019-0927-7.](https://doi.org/10.1007/s13201-019-0927-7)

[8] Y.H. Yoon, J.H. Nelson, Application of gas adsorption kinetics i. a theoretical
model for respirator cartridge service life, Am. Ind. Hyg. Assoc. J. 45(8) (1984)
509–516, [doi:10.1080/15298668491400197.](https://doi.org/10.1080/15298668491400197)

[9] G.S. Bohart, E.Q. Adams, Some aspects of the behaviour of charcoal with
respect to chlorine, J. Am. Chem. Soc. [42](https://doi.org/10.1021/ja01448a018) (3) (1920) 523–544, doi:10.1021/
ja01448a018.

[10] S. Li, S. [Deng,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0010) L. [Zhao,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0010) R. [Zhao,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0010) M. Lin, Y. [Du,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0010) Y. [Lian,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0010) Mathematical modeling
and numerical investigation of carbon [capture](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0010) by adsorption: Literature review
and case study, Appl. Energy 221 (2018) 437–449.

[11] R. [Ben-Mansour,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0011) M.A. Habib, O.E. [Bamidele,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0011) M. [Basha,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0011) N.A.A. Qasem,
A. [Peedikakkal,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0011) T. [Laoui,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0011) M. Ali, Carbon capture by physical adsorption: Materials, experimental investigations and [numerical](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0011) modeling and simulations    A review, Appl. Energy 161 (2016) 225–255.

[12] T.G. Myers, F. Font, M.G. Hennessy, Mathematical modelling of carbon capture
in a packed column by adsorption, Appl. Energy 278 (2020) 115565, doi:10.
1016/j.apenergy.2020.115565.

[13] M.S. [Shafeeyan,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0013) [W.M.A.W.](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0013) Daud, A. [Shamiri,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0013) N. [Aghamohammadi,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0013) Modeling of
carbon dioxide adsorption onto [ammonia-modified](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0013) activated carbon: kinetic
analysis and breakthrough behavior, Energy & Fuels 29 (10) (2015) 6565–6577.

[14] N. Ayawei, A.N. Ebelegi, D. Wankasi, Modelling and interpretation of adsorption
isotherms, J. Chem. (2017), [doi:10.1155/2017/3039817.](https://doi.org/10.1155/2017/3039817)

[15] A.I. [Sarker,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0015) A. [Aroonwilas,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0015) A. [Veawab,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0015) Equilibrium and kinetic behaviour of CO2
adsorption onto zeolites, carbon molecular sieve and activated carbons, Energy
Procedia 114 (2017) 2450–2459. 13th International Conference on Greenhouse
Gas Control Technologies, GHGT-13, 14-18 November 2016, Lausanne, Switzerland

[16] M.S. [Shafeeyan,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0016) [W.M.A.W.](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0016) Daud, A. [Shamiri,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0016) A review of mathematical modeling of fixed-bed columns for carbon [dioxide](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0016) adsorption, Chem. Eng. Res. Des.
92 (5) (2014) 961–988.

[17] F. [Rezaei,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0017) P. [Webley,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0017) Optimum structured adsorbents for gas separation processes, Chem. Eng. Sci. 64 (24) (2009) 5182–5191.

[18] K.H. Chu, Fixed bed sorption: setting the record straight on the Bohart-Adams
and Thomas models, J. Hazard. Mater. 177 (2010) 1006–1012.

[19] C. [Smaranda,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0019) M.-C. [Popescu,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0019) D. [Bulgariu,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0019) T. [Malut,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0019) M. [Gavrilescua,](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0019) Adsorption
of organic pollutants onto a Romanian [soil:](http://refhub.elsevier.com/S0017-9310(20)33310-X/sbref0019) column dynamics and transport,
Proc. Safety and Environmental Protection 108 (2017) 108–120.



1 = _u_ ˆ| _x_ ˆ=0 _c_ [ˆ] 1| _x_ ˆ=0 [−] _[δ]_ 2 _[∂]_ _c_ [ˆ] 1
_∂x_ ˆ


1 = _u_ ˆ| _x_ ˆ=0 _c_ [ˆ] 2| _x_ ˆ=0 [−] _[δ]_ 2 _[∂]_ _c_ [ˆ] 2
_∂x_ ˆ



= _[∂]_ _q_ [ˆ]
���� _∂x_ ˆ
_x_ ˆ=0



_,_ _∂c_ ˆ1
���� _∂x_ ˆ
_x_ ˆ=0

_,_ _∂c_ ˆ2
���� _∂x_ ˆ
_x_ ˆ=0



_∂q_ ˆ
_∂x_ ˆ



= 0 _,_ (A.8)
����
_x_ ˆ= _l_



and the initial conditions given by (31). Note that (A.1)-(A.8) include terms of order 10 [−][2] previously neglected in the derivation
of the travelling wave solution. Hence, the numerical solution of
(A.1)-(A.8) can be used to validate the accuracy of the travelling
wave solution.
Expression (A.4) leads to

_c_ ˆ2 = _δ_ [1] 4 - _δ_ 5 _c_ ˆ1 _._ (A.9)


Substituting (A.9) in (A.2) provides a relation between _u_ ˆ and _c_ ˆ1 _,_
which can be combined with (A.1) to give
_∂u_ ˆ _q_ [ˆ]

[−] _[δ]_ [4] _[δ]_ [5] _[∂]_ _._ (A.10)
_∂x_ ˆ [=] _∂t_ [ˆ]


This is consistent with the travelling wave solution (55). In a similar fashion, by substituting (A.9) in (A.7), and using (A.6), we obtain the following boundary condition for the gas velocity


_u_ ˆ| _x_ ˆ=0 [=] _[(]_ [1] [+] _[δ]_ 5 _[)][δ]_ 4 [=] [1] _[,]_ (A.11)

(after noting that _(_ 1 + _δ_ 5 _)δ_ 4 = 1 + _δ_ 3 ≈ 1). We can integrate
(A.10) and apply (A.11) to obtain

    - _x_ ˆ _q_ [ˆ]
_u_ ˆ = 1 - _[δ]_ [4] _[∂]_ _dx_ ˆ _._ (A.12)

0 _[δ]_ [5] _∂t_ [ˆ]


We note that adsorption can only occur in the region where
_c_ ˆ1 is present. In the travelling wave solution this corresponds to
the growing region _x_ _<_ _s_ ( _t_ ). For the numerical solution, we take a
different approach and define the function

   _H(c_ ˆ1 _)_ = 10 otherwisefor _c_ ˆ1 _>_ 0 (A.13)


which we will use to enable/disable equation (A.3) if a particular region within the column contains _c_ ˆ1 or not (see [12]), thereby
avoiding the difficulty of dealing with a moving boundary.
Using (A.13) as a multiplying factor in (A.3), and substituting
(A.3) in (A.12), the equations of the model reduce to

_c_ [ˆ] 1   -   - [2] _c_ [ˆ] 1 _q_ [ˆ]
_δ_ 1 _[∂]_ _∂t_ [ˆ] + _∂_ _[∂]_ _x_ ˆ _u_ ˆ _c_ ˆ1 = _δ_ 2 _[∂]_ _∂x_ ˆ [2] [−] _[∂]_ _∂t_ [ˆ] _,_ (A.14)


_∂q_ ˆ
_∂t_ [ˆ] = _(_ 1 - _q_ ˆ _)H(c_ ˆ1 _)_ _,_ (A.15)

_u_ ˆ = _u_ ˆ��� - - _x_ ˆ _[δ]_ [4] �1 - _q_ ˆ [�] _H_ [�] _c_ ˆ1� _dx_ ˆ _,_ (A.16)
_x_ ˆ=0 0 _[δ]_ [5]


which are subject to the boundary conditions (A.6), (A.8) and
(A.11). The concentration _c_ ˆ2 is obtained via (A.9) and the pressure
_p_ ˆ can be constructed by numerically integrating (A.5) a posteriori.



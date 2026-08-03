Bi-weekly Journal (Weeks 11 and 12)
Name: Loh John Ray

Contents
Abstract	2
Introduction	2
Assumptions	2
Derivation	2
Parameter estimation strategy	3
Limitations of the minimal kinetic model	3
Appendix	3
Abstract	5
Assumptions	5
Governing equations (Full model)	6
Initial and boundary conditions	7
Dimensionless form	7
Numerical Solution	8
Gas-phase mass balance equation	9
Solid-phase balance: LDF kinetics	9
Equilibrium closure	10
Thermodynamic consistency	10
Pseudo-homogeneous energy balance	11
Initial and boundary condition	12
Full model	12
Nondimensionalisation	13
References	14
Reflection	15



Minimal Kinetic Model for CO2 Adsorption with Amine Sorbents in Dry Condition

Abstract
A minimal kinetic model is derived and proposed to validate and predict CO2 adsorption processes in a packed bed column. The model simply describes the adsorption breakthrough curve using two process parameters: gas flow rate and concentration.

Introduction
In DAC processes, a trace level of CO2 adsorbed from an inert gas carrier such that a single component model applies in dry conditions. The mass transfer between gas and solid phases includes three resistances (external film, macropore and micropore) and can be depicted by a linear driving force (LDF) model, where a lumped uptake rate constant is used to take various resistances into account. The LDF model is conceptually simple, computationally efficient and therefore widely used in literature.

Assumptions
The following assumptions were made:
A1. Plug flow, constant superficial gas velocity, no axial dispersion
A2. Isotherm model i.e. heat transfer has an insignificant effect on the breakthrough curve
A3. 1-D model i.e. gas concentration gradients only exist in the axial direction
A4. Gas phase behaves as ideal gas
A5. Negligible pressure drop due to short column length and relatively low flow rate
A6. Only CO2 adsorption is considered (others are treated as non-adsorbing components)
A7. LDF adsorption kinetics model 

Derivation
Consider a 1-D isothermal plug flow model given as
∂c/∂t=-u_s/ε  ∂c/∂z-ρ_b/ε  ∂q/∂t     (1)
where u_s is the superficial gas velocity, ε is the bed voidage and ρ_b is the bulk density of the packed bed.
The LDF model used to describe the adsorption kinetics written as
∂q/∂t=k(q_e-q)     (2)
where k (s^(-1)) is the uptake rate constant, q_e (mol/kg) is the equilibrium adsorption concentration.
Assuming the surface has identical elementary adsorption sites to host a single adsorbed molecule, a Langmuir isotherm was used to describe the adsorbed quantity q_e as a function of bulk gas pressure:
q_e=(q_m bP_(CO_2 ))/(1+bP_(CO_2 ) )     (3)
where q_m is the theoretical maximum CO2 concentration, P_(CO_2 ) is given by the ideal gas law:
P=cRT    (4)
where c is the molar concentration in (mol/m3), R is the universal gas constant and T is the absolute temperature; and b(T) is described by the van’t Hoff equation:
b(T)=b_0  exp⁡((-ΔH)/RT)     (5)
where (-ΔH)>0 is the heat of adsorption.
The initial condition used were c=0,q=0 and T=T_0 at t=0, and boundary conditions were c=c_0 and T=T_0 at z=0, ∂c/∂z=0 and ∂T/∂z=0 at z=L.

Parameter estimation strategy
Using our minimal kinetic model, we examined the effects of k, u_s, q on the breakthrough curves at flue gas conditions. The parameters b,k were determined using non-linear fitting methods to the experimental data. 
Table 1) Langmuir isotherm parameters for CO2.
Parameters	Values

b	??
Table 2) shows a list of parameters used and their values for the packed-bed adsorption experiments.
Table 2) The basic parameters for packed-bed adsorption.
Parameter	Value	Units

 Inlet diameter	 0.85	cm
 Height of packed-bed	 21.0 – 21.5 (per run)	cm
 Volume of packing	 11.92	cm3
 Inlet velocity	 1.47 – 4.41	cm∙s-1
 Volume flow rate	 0.3 – 0.9	m3∙h-1
 Angle of bed	 90	Deg
Bed void fraction ε	??	-
Adsorbent bulk density ρ_b	??	g∙cm-3
Superficial velocity u_s	??	cm∙s-1
CO2 uptake rate constant k	??	s-1
CO2 feed concentration c_10	??	mmol∙cm-3

Limitations of the minimal kinetic model
	Classical closed-form solutions that assume first-order or Langmuir-type kinetics and do not capture the specific stoichiometry of the amine–CO2 reaction, the second-order dependence on free amine sites, or the role of humidity. (Alba et al., 2026).
	Langmuir equation parameters have the ability to only compare between different adsorbents but fail with the explanation of the reaction mechanism (Al-Ghouti et al., 2020).

Appendix
Nonlinear Least Squares fitting in Python
```python
# insert code here
```   
Mechanistic Model for CO2 adsorption in a fixed-bed column

Abstract
A single component CO2 adsorption from an inert carrier (N2) in a 1-D fixed-bed is modelled and derived from conservation laws, closed with LDF kinetics and a nonlinear isotherm (Toth, Dual-Site Langmuir). Fitted analytical models (Yoon-Nelson, Thomas, Bohart-Adams, Clark, fractal sigmoids, etc) parameterise the shape of one curve at one operating point, with k_YN=k b c_f and τ=t_st (u,c_f,L). That composition is exactly why fitted k_YN,τ cannot extrapolate across u, c_f, L, or T, and why the PDE model below can.

Assumptions
In this model, we assume the following:
A1. Radial gradients are neglected. 
A2. CO2 mole fraction y_f≪1
A3. Pressure, P, is uniform (i.e. pressure drop ≪P). Thus, c_tot=P/RT
A4. All axial mixing is lumped into D_L
A5. Intraparticle + film resistance is lumped into a single first-order driving force with constant k (§A.3)
A6. Gas and solid share one temperature T
A7. -ΔH= isosteric heat implied by the isotherm’s temperature dependence (§A.4.3)
A8. Constant ε,ρ_p,c_(p,s),λ_(eff⁡ ,) D_L
 
Governing equations (Full model)
Gas-phase mass balance. Applying a mole balance to a control volume of the packed bed gives
ε ∂c/∂t+u ∂c/∂z=εD_L  (∂^2 c)/∂z-(1-ε) ρ_p  ∂q/∂t     (1)
Look where c(z,t) is the gas-phase CO₂ concentration per unit void volume, q(z,t) the adsorbed loading per unit sorbent mass, ε the bed voidage, u the superficial velocity, D_L the axial dispersion coefficient, and α_b=(1-ε) ρ_p the sorbent mass per unit bed volume.
Solid-phase kinetics (LDF). Mass transfer into the sorbent is modelled as first-order relaxation toward equilibrium,
∂q/∂t=k(q^* (c,T)-q)     (2)
with k the lumped LDF rate constant and q^* (c,T) the equilibrium loading.
Equilibrium isotherm. The primary closure is the Toth isotherm,
q^* (c,T)=(n_s (T),b(T),c)/[1+(b(T)c)^(t_T ) ]^(1/t_T )      (3)
n_s (T)=n_s0  exp⁡[χ(1-T/T_0 )], b(T)=b_0  exp⁡[(ΔH_0)/(RT_0 ) (T_0/T-1)]  
t_T (T)=t_0+α_T (1-T_0/T)
with 0<t_T≤1 the heterogeneity exponent (t_T=1 recovers the Langmuir isotherm). As an alternative closure for zeolite-type sorbents, a dual-site Langmuir (DSL) isotherm is also considered:
q^* (c,T)=(q_1 b(T)c)/(1+b(T)c)+(q_2 d(T)c)/(1+d(T)c)     (4),  b=b_0 e^(-ΔU_b/RT), d=d_0 e^(-ΔU_d/RT)     (5)
Both closures satisfy q^* (0,T)=0, are strictly monotone and concave in c (a favorable isotherm), and saturate as c→∞, properties used in §4 to characterise the shape of the breakthrough front.
Energy balance. A pseudo-homogeneous energy balance over the same control volume, accounting for convection, effective axial conduction, the heat released on adsorption, and heat loss through the column wall, gives
C_h  ∂T/∂t+uρ_g c_(p,g)  ∂T/∂z=λ_eff  (∂^2 T)/(∂z^2 )+α_b (-ΔH)  ∂q/∂t-(4h_w)/d_col  (T-T_wall )     (6)
where C_h=ερ_g c_(p,g)+(1-ε) ρ_p c_(p,s) is the volumetric heat capacity of the bed, (-ΔH)>0 the heat of adsorption, and h_w, d_col the wall heat-transfer coefficient and column internal diameter. An adiabatic column corresponds to h_w=0.
Equations (1), (2), and (6), closed by (3) or (5), constitute the full model: a parabolic–hyperbolic system in (c,T) coupled pointwise to a stiff local ODE in q.
Initial and boundary conditions
The bed starts clean:
c(z,0)=0,  q(z,0)=0,  T(z,0)=T_0     (7)
At t>0 a step feed of concentration c_f and temperature T_f is applied. Rather than a Dirichlet condition, a Danckwerts (Robin) condition is imposed at the inlet to enforce flux continuity across the bed face:
uc_f=u,c(0^+,t)-εD_L,c_z (0^+,t),  uρ_g c_(p,g) T_f=uρ_g c_(p,g) T(0^+,t)-λ_eff T_z (0^+,t)     (8)
A Dirichlet inlet (c(0,t)=c_f) overfeeds the column by an amount O(Pe^(-1) ) relative to the Danckwerts condition, and is used here only as a reduced-model check (§4); the Danckwerts form is used throughout the main model because it makes the CO₂ inventory balance (§4.1) exact rather than approximate. At the outlet, zero-gradient conditions are imposed:
c_z (L,t)=0,  T_z (L,t)=0    (9)
Dimensionless form
Defining x=z/L, τ=ut/L, C=c/c_f, Q=q/q_f, Θ=(T-T_0 )/ΔT, with q_f≡q^* (c_f,T_0 ) and ΔT=ΔT_ad=α_b (-ΔH) q_f/C_h the adiabatic temperature rise, equations (1), (2), and (6) become
ε,C_τ+C_x=ε/Pe,C_xx-β,Q_τ,  Q_τ=Da,[Q^* (C,Θ)-Q]     (10,11)
Θ_τ+γ_h,Θ_x=1/(Pe_h ),Θ_xx+Λ,Q_τ-Bi_w,(Θ-Θ_wall )     (12)
with dimensionless groups
Pe=uL/D_L , Da=kL/u, β=(α_b q_f)/c_f , γ_h=(ρ_g c_(p,g))/C_h , Pe_h=(C_h uL)/λ_eff , Λ=(α_b (-ΔH) q_f)/(C_h,ΔT), Bi_w=(4h_w L)/(d_col C_h u)     (12-18)
Numerical Solution
Because the isotherm couples c and T nonlinearly and the LDF term introduces stiffness, equations (1), (2), and (6) are integrated numerically by the method of lines. The domain is discretised into N finite volumes with cell-centred c_i, q_i, T_i; convective terms use first-order upwinding (monotone, positivity-preserving); dispersive/conductive terms use central differences; face fluxes at the inlet are set directly to the Danckwerts value (F_(-1/2)=uc_f), which makes the discrete CO₂ and energy inventories conservative to machine precision (§4.1). The resulting stiff ODE system is integrated with an implicit BDF/LSODA scheme, using event functions to locate the breakthrough time t_BT (c(L,t)/c_f=0.05) and saturation time t_sat (c(L,t)/c_f=0.95) directly at integrator precision.
 
Appendix A – Derivation
Gas-phase mass balance equation
Consider a control volume (CV) [z,z+Δz] of cross-section A. The total control volume is AΔz of which only a fraction ε is occupied by gas. Thus, the gas volume is εAΔz. Let c(z,t) be the gas-phase CO2 concentration in mol m-3 gas, q(z,t) be the adsorption capacity or loading in mol kg-1, u the superficial velocity and D_L the axial dispersion coefficient.
The accumulation is εAΔz ∂c/∂t , the molar flux entering the column is N(z,t)=uc-〖εD〗_L  ∂c/∂t (Danilov, 2019) in mol m-2 s-1 and at the molar flux exiting the column is N(z+Δz,t)=N(z,t)+∂N/∂z Δz+O(Δz^2). The convective term is uc=εv_i c where v_i c is scaled by the open-area fraction ε. The sorbent mass in the differential fluid is (1-ε) ρ_p AΔz so the uptake removes (1-ε) ρ_p  ∂q/∂t AΔz mol s-1 from the gas. By conservation of mass, accumulation = in – out – sink. Thus,
εAΔz ∂c/∂t=NA-(N+∂N/∂z Δz)A-(1-ε) ρ_p  ∂q/∂t AΔz
Equivalently, divide by AΔz, let z→0 and with A2 (u_z=0):
ε ∂c/∂t+u ∂c/∂z=εD_L  (∂^2 c)/∂z-(1-ε) ρ_p  ∂q/∂t

Solid-phase balance: LDF kinetics
The mass balance for an adsorbent particle yields the adsorption rate expression which may be written as
(∂q ̅)/∂t=f(q,c)=k(q^* (c,T)-q)
where q_t is the uptake rate in mol kg-1 s-1, k is the inverse relaxation time of the pellet in s-1 and q^*-q represents the displacement from equilibrium in mol kg-1.
For the mass transfer coefficient, k, we consider three resistances in series, namely in the gas film, in the gas pore and in the solid (Stampi-Bombelli et al., 2024), with coefficients k_pore, k_film, and k_amine, respectively
1/k=1/k_film +1/k_pore +1/k_amine 
For spherical pellets of radius r_p, film coefficient k_f, macropore diffusivity D_p, porosity ε_p, crystal/micro scale r_c,D_c, and local slope K'=ρ_p ∂q^*/∂c,
1/k = (r_p K')/(3k_f ) + (r_p^2 K')/(15 ε_p D_p ) + (r_c^2)/(15 D_c )
(Bird et al., 2007, Ch 28.2; Ruthven, 1984, p. 181; Kalyanaraman et al., 2014 [not verified])
Equilibrium closure
Toth Isotherm. A generalisation for varying binding affinities in adsorption sites.
 q^* (c,T)=(n_s (T) b(T) c)/[1+(b(T) c)^(t_T ) ]^(1/t_T ) 
n_s (T)=n_s0  exp⁡ [χ(1-T/T_0 )]
b(T)=b_0  exp⁡ [(ΔH_0)/(RT_0 ) (T_0/T-1)]
t_T (T)=t_0+α_T (1-T_0/T)
with 0<t_T≤1 the heterogeneity exponent (t_T=1 recovers Langmuir).
Thermodynamic consistency
For the adsorption process to occur, free energy (ΔG) should decrease and the decrease in the degree of freedom leads to a negative change in entropy (ΔS) such that:
ΔH=ΔG+TΔS<0
Therefore, the heat of adsorption (ΔH) is calculated from the Clausius–Clapeyron relation:
ΔH^o/〖 R〗_g T_2=-〖(δ ln⁡P/ δT)〗_Cμ  
where ΔH° is the differential molar enthalpy of the adsorption in (J/mol), C_μ is the maximum adsorbed concentration, δ is the coefficient of the thermal expansion of the saturation concentration.
The isosteric heat implied by the equilibrium closure is
-ΔH_iso RT^2 ((∂ ln⁡p)/∂T)_(q^* )
For χ=α_T=0, this reduces identically to the constant value
-ΔH_iso=-ΔH_0.
When χ≠0, the implied isosteric heat becomes loading dependent through the equilibrium closure. Consequently, the same enthalpy function should be used in the energy balance (A.5). Otherwise, the equilibrium model and the thermal model become thermodynamically inconsistent: the adsorption isotherm implies one isosteric heat through the adsorption Clausius–Clapeyron relation, while the energy balance assumes another, leading to non-physical heat generation or absorption.
Pseudo-homogeneous energy balance
The temperature is assumed to be uniform across any section of the column with negligible temperature difference between gas and pellet but, in the region of the adsorption zone, a significant difference between the gas and column wall. This implies a high effective bed thermal conductivity, λ_eff,  and a high rate of heat transfer between gas and pellets with all the thermal resistance, characterized by an overall heat coefficient h, at the inner surface of the tube wall. The assumption that the temperature difference between gas and wall is significantly greater than the temperature difference between gas and pellet can be approximately justified if similarity of j factors is assumed. However, the radial temperature difference between the centre. of the bed and the wall is often comparable with the temperature difference at the wall so the assumption of a uniform temperature across the bed may be a severe approximation (Ruthven et al., 1975). Thus, the energy stored in a CV relative to an arbitrary reference T_ref is:
E=[ερ_g c_(p,g)+(1-ε) ρ_p c_(p,s) ](T-T_ref ) A Δz,  ∂E/∂t=C_h ∂T/∂t A Δz.
In Ruthven et al. (1975), the enthalpy flux carried through a face by the superficial gas flux uρ_g is uρ_g c_(p,g) (T-T_ref ) (per bed area). Net convective accumulation in the CV is -∂_z [uρ_g c_(p,g) T] AΔz=-uρ_g c_(p,g) T_z AΔz under A2 (u_z≈0).
At low Reynolds numbers (Re<~30) both the wall heat transfer coefficient and the effective thermal conductivity of the bed become essentially independent of fluid velocity (Yagi & Kuni, 1975). Since A4 already lumps every axial mixing mechanism for the mass balance into one Fickian closure -εD_L ∂c/∂z (A.1) the same interstitial eddies disperse a scalar temperature exactly as they disperse a scalar concentration, to leading order, so the identical closure is applied to the heat flux (only the transport coefficient differs, D_L→λ_eff):
q''_cond=-λ_eff  ∂T/∂z  [W m^(-2)  bed area],  "net inflow"=-∂_z q''_cond AΔz=λ_eff T_zz AΔz.
This term is retained here whereas Ruthven et al. (1975) drops it as this project explicitly validates an axial-dispersion model at the rig’s low Reynolds numbers.
Heat released in the CV per unit time equals (moles adsorbed per unit time)× (-ΔH). The CV holds (1-ε) ρ_p AΔz kg sorbent (A.1, "sink to the solid"), taking up q [mol kg⁻¹] at rate ∂q/∂t, so
"source"=(1-ε) ρ_p (-ΔH)  ∂q/∂t AΔz
For a cylindrical column of internal diameter d_col, wall area per unit length is πd_col and bed cross-section is πd_col^2/4. Ruthven et al. (1957) assumes (6): heat transfer at the external wall surface is "sufficiently rapid to maintain the wall at a uniform temperature”. Thus heat lost to a wall held at uniform T_wall per unit bed volume is:
(h_w πd_col (T-T_wall ))/(πd_col^2/4)=(4h_w)/d_col  (T-T_wall )
Therefore, heat balance of a differential element of the column may be written as:
C_h  ∂T/∂t+uρ_g c_(p,g)  ∂T/∂z = λ_eff  (∂^2 T)/(∂z^2 ) + (1-ε) ρ_p (-ΔH)  ∂q/∂t - (4h_w)/d_col  (T-T_wall )
,where C_h=ερ_g c_(p,g)+(1-ε) ρ_p c_(p,s)   [J m^(-3) K^(-1) ]
Initial and boundary condition
Adsorption: t=0;c(z,0)=0;q(z,0)=0;T(z,0)=T_0
At inlet (z=0), there is continuity of mass flux (Myers & Font, 2020). Thus, the total flux uc_f must equal the total flux just inside:
uc_f=u c(0^+,t)-εD_L c_z (0^+,t),  uρ_g c_(p,g) T_f=uρ_g c_(p,g) T(0^+,t)-λ_eff T_z (0^+,t)
where the -,+ superscripts indicate just before and just after z=0, c_f the feed concentration and ρ_g,c_(p,g) the gas density and specific heat respectively.
At outlet (z=L): c_z (L,t)=0,T_z (L,t)=0 (no dispersive flux through the exit face).
Full model
εc_t+uc_z=εD_L c_zz-α_b q_t,  q_t=k (q^* (c,T)-q), 
C_h T_t+uρ_g c_(p,g) T_z=λ_eff T_zz+α_b (-ΔH) q_t-(4h_w)/d_col  (T-T_wall )
with closure (A.3) or (A.4), IC (A.6), BC (A.7) + zero-gradient outlet. The model couples two transport PDEs pointwise to one stiff local ODE.
Nondimensionalisation
Myers & Font (2020) scales the variables as such:
x=z/L,τ=ut/L,C=c/c_f ,Q=q/q_f ,Θ=(T-T_0)/ΔT,q_f=q^* (c_f,T_0 )
where τ represents the superficial bed volume and ΔT is free.
From the equation,
ε ∂c/∂t+u ∂c/∂z=εD_L  (∂^2 c)/∂z-(1-ε) ρ_p  ∂q/∂t
Multiplying by L/(uc_f),
εC_τ+C_x=ε/Pe C_xx-βQ_τ
where Q_τ=Da[Q^* (C,Θ)-Q].
Similarly substituting L/(uC_h ΔT), into the equation:
C_h  ∂T/∂t+uρ_g c_(p,g)  ∂T/∂z = λ_eff  (∂^2 T)/(∂z^2 ) + (1-ε) ρ_p (-ΔH)  ∂q/∂t - (4h_w)/d_col  (T-T_wall )
Θ_τ+γ_h Θ_x=1/(Pe_h ) Θ_xx+ΛQ_τ-Bi_ω (Θ-Θ_wall )
where Q^* (C,Θ)=q^* (c_f C, T_0+ΔT Θ)/q_f and
Pe=uL/D_L ,  Da=kL/u,  β=(α_b q_f)/c_f ,  α=β/ε=((1-ε) ρ_p q_f)/(εc_f ),
γ_h=(ρ_g c_(p,g))/C_h ,  Pe_h=(C_h uL)/λ_eff ,  Λ=((1-ε) ρ_p (-ΔH) q_f)/(C_h ΔT),  Bi_w=(4h_w L)/(d_col C_h u).
Thus, the initial and boundary condition respectively becomes:
C=Q=Θ=0; 1=C-ε/Pe C_x at x=0^+; C_x (1,τ)=0
 
References
Valery A. Danilov, Peter De Schepper, Julien Cousin-Saint-Remi, Joeri F.M. Denayer, Concentration and temperature profiles in a fixed bed column based on an analytical solution of the axial dispersion model for binary and multicomponent non-isothermal adsorption processes, Computers and Chemical Engineering (2018), DOI: 10.1016/j.compchemeng.2018.12.026
Valentina Stampi-Bombelli, Alba Storione, Quirin Grossmann, and Marco Mazzotti, On Comparing Packed Beds and Monoliths for CO2 Capture from Air Through Experiments, Theory, and Modeling, Industrial & Engineering Chemistry Research 2024 63 (26), 11637-11653  DOI: 10.1021/acs.iecr.4c01392
Ruthven, D. M., Garg, D. R., & Crawford, R. M. (1975). The performance of molecular sieve adsorption columns: Non-isothermal systems. Chemical Engineering Science, 30(8), 803–810. https://doi.org/10.1016/0009-2509(75)80044-3
Yagi, S., & Kunii, D. (1957). Studies on effective thermal conductivities in packed beds. AIChE Journal, 3(3), 373–381. Portico. https://doi.org/10.1002/aic.690030317
 
Reflection
When I started using AI for serious research, it felt like a shaky enterprise. I could optimise my Python scripts, catch the occasional typo, but not much more.
Then agentic systems arrived. Claude Code changed how I approached my work as a student researcher at SUTD's Integrated Materials and Devices Lab, where I run my own experiments on CO2 adsorption modelling and prediction.
Once you master the lingo of specs and documentation, you start to see how critical it is to feed the model with the latest literature, code up all the special cases and edge conditions with the agent. I use Claude Code to implement curve fitting algorithms for parameter estimation, to write proofs, to find the gaps in my own formulation and logical reasoning.
Fable 5 connected a simple model I had derived with an analytically tractable limit from a research paper I found using the three-pass method: first read the abstract, introduction, and conclusion to see if it fits my research direction. Then examine the figures and tables critically. Then reproduce the paper.
When I fed that paper and my derivation into Claude Code, it linked the two in a way I had not seen. It surfaced a gap in my formulation that I had been staring past for weeks. That moment did not feel like AI doing my work. It felt like a second pair of eyes catching something I was too close to notice.
I think for researchers in my position, this is the dawn of a completely new era. And it is not only trimming trees and mowing lawns. It is mostly late nights spent with dark terminal screens, setting up scaffolds with half-baked lemmas and new conjectures. And it is this feeling of genuine curiosity where you find yourself in new territory, trying to understand what just happened.
Every day feels like very hard work on top of my regular research. But I find AI to be an excuse now to take a bite at everything I find curious. There are no hard boundaries. Once you master your core skills, you can reach places you would not have reached alone.

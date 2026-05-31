# Fixed-Bed Adsorption — Complete Equation Compendium

*Sources: Shafeeyan et al. (2013); Juela et al. (2021); Lin et al. (2016); Hu et al. (2024); Hu et al. (2022); Hu et al. (2021); Hu et al. (2020); Chu (2020); Myers et al. (2023)*

---

## 1. Governing Mass Balance PDEs

### 1.1 Fluid-Phase Component Mass Balance (Dispersed Plug Flow)

$$-D_{zi}\frac{\partial^2 c_i}{\partial z^2} + \frac{\partial(u c_i)}{\partial z} + \frac{\partial c_i}{\partial t} + \frac{1-\varepsilon_b}{\varepsilon_b}\rho_p\frac{\partial \bar{q}_i}{\partial t} = 0 \tag{1}$$

### 1.2 Overall Continuity (Velocity Variation)

$$\frac{\partial(uC)}{\partial z} + \frac{\partial C}{\partial t} + \frac{1-\varepsilon_b}{\varepsilon_b}\rho_p\sum_{i=1}^n \frac{\partial q_i}{\partial t} = 0 \tag{2}$$

### 1.3 Advection–Diffusion Form (Myers et al., constant $\varepsilon$, $u$)

$$\frac{\partial c}{\partial t} + u_{in}\frac{\partial c}{\partial x} = D\frac{\partial^2 c}{\partial x^2} - \frac{\rho_b}{\varepsilon}\frac{\partial q}{\partial t} \tag{3}$$

### 1.4 Non-Dimensional Advection–Diffusion (Myers et al.)

$$\delta_1\frac{\partial \hat{c}}{\partial \hat{t}} + \frac{\partial \hat{c}}{\partial \hat{x}} = \delta_2\frac{\partial^2 \hat{c}}{\partial \hat{x}^2} - \frac{\partial \hat{q}}{\partial \hat{t}} \tag{4}$$

where $\delta_1 = Da = L/(u_{in}\tau)$, $\delta_2 = Pe^{-1} = D/(u_{in}L)$

---

## 2. Boundary and Initial Conditions

### 2.1 Danckwerts Inlet (Dispersed Plug Flow)

$$D_{zi}\frac{\partial c_i}{\partial z}\bigg|_{z=0^+} = -u\left(c_{i,z=0^-} - c_{i,z=0^+}\right) \tag{5}$$

### 2.2 Danckwerts Outlet

$$\frac{\partial c_i}{\partial z}\bigg|_{z=L} = 0 \tag{6}$$

### 2.3 Inlet Flux Continuity (Myers et al.)

$$u_{in}c_{in} = \left(uc - D\frac{\partial c}{\partial x}\right)\bigg|_{x=0^+} \tag{7}$$

### 2.4 Strong-Sink Front Conditions (Myers et al.)

$$c(s(t),t) = c_x(s(t),t) = 0 \tag{8}$$

### 2.5 Column Initial Conditions

$$t = 0: \quad c = 0,\quad q = 0 \quad \forall\, z \in [0,L] \tag{9}$$

---

## 3. Equilibrium Isotherms

### 3.1 Langmuir

$$q_e = \frac{q_{max}K_L c_e}{1 + K_L c_e} \tag{10}$$

### 3.2 Freundlich

$$q_e = K_F c_e^{1/n} \tag{11}$$

### 3.3 Sips (Freundlich–Langmuir)

$$q_e = \frac{q_m K_S c_e^m}{1 + K_S c_e^m} \tag{12}$$

### 3.4 Henry (Linear)

$$q_e = q_m K_L c_e \tag{13}$$

### 3.5 Langmuir — Linear Form for Fitting

$$\frac{1}{q_e} = \frac{1}{q_m} + \frac{1}{q_m K_L}\cdot\frac{1}{c_{in}} \tag{14}$$

### 3.6 Sips — Linear Form for Fitting

$$\frac{1}{q_e} = \frac{1}{q_m} + \frac{1}{q_m K_S}\cdot\frac{1}{c_{in}^m} \tag{15}$$

---

## 4. Mass Sink / Kinetic Rate Equations

### 4.1 Full Nonlinear Langmuir Kinetics (Adsorption + Desorption)

$$\frac{\partial q}{\partial t} = k_{ad}c(q_m - q) - k_{de}q \tag{16}$$

### 4.2 Pure Adsorption (Langmuir, $k_{de}=0$)

$$\frac{\partial q}{\partial t} = k_{ad}c(q_m - q) \tag{17}$$

### 4.3 Linear Driving Force (LDF)

$$\frac{\partial q_i}{\partial t} = k_i(q_i^* - q_i) \tag{18}$$

### 4.4 Sips Kinetics

$$\frac{\partial q}{\partial t} = k_m c^m(q_m - q) - k_{de}q \tag{19}$$

### 4.5 Barrier (Surface Resistance) Micropore Rate

$$\frac{\partial q_i}{\partial t} = k_{bi}(q_i^* - q_i) \tag{20}$$

### 4.6 Non-Dimensional Nonlinear Sink

$$\frac{d\hat{q}}{d\hat{t}} = \hat{c}(1-\hat{q}) - \delta_3\hat{q}, \quad \delta_3 = \frac{k_{de}}{k_{ad}c_{in}} \tag{21}$$

### 4.7 Non-Dimensional Linear Sink

$$\frac{d\hat{q}}{d\hat{t}} = 1 - \hat{q} \tag{22}$$

### 4.8 Non-Dimensional Sips Sink

$$\frac{d\hat{q}}{d\hat{t}} = \hat{c}^m(1-\hat{q}) - \delta_3\hat{q} \tag{23}$$

---

## 5. Intraparticle Diffusion — Macropore

### 5.1 Macropore PDE (Spherical Particle)

$$\frac{\partial c_{pi}}{\partial t} + \frac{1-\varepsilon_p}{\varepsilon_p}\frac{\partial q_i}{\partial t} = \frac{1}{R^2}\frac{\partial}{\partial R}\left(R^2 D_{pi}\frac{\partial c_{pi}}{\partial R}\right) \tag{24}$$

### 5.2 GRM Pore-Phase PDE (Lin et al.)

$$\varepsilon_p\frac{\partial c_p}{\partial t} + \rho_p\frac{\partial q_p}{\partial t} = \frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\varepsilon_p D_p\frac{\partial c_p}{\partial r}\right) \tag{25}$$

### 5.3 Macropore Boundary — External Film

$$\varepsilon_p D_{pi}\frac{\partial c_{pi}}{\partial R}\bigg|_{R=R_p} = k_{fi}(c_i - c_{pi}(t,R_p)) \tag{26}$$

### 5.4 Macropore Boundary — Symmetry

$$\frac{\partial c_{pi}}{\partial R}\bigg|_{R=0} = 0 \tag{27}$$

---

## 6. Intraparticle Diffusion — Micropore

### 6.1 Distributed Micropore Interior

$$\frac{\partial q_i}{\partial t} = \frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2 D_{\mu i}\frac{\partial q_i}{\partial r}\right) \tag{28}$$

### 6.2 Micropore Symmetry Condition

$$\frac{\partial q_i}{\partial r}\bigg|_{r=0} = 0 \tag{29}$$

### 6.3 Micropore Outer Boundary (Barrier + Interior)

$$\frac{3}{R_c}D_{\mu i}\frac{\partial q_i}{\partial r}\bigg|_{r=R_c} = k_{bi}(q_i^*(t,R_c) - q_i(t,R_c)) \tag{30}$$

### 6.4 Darken Correction for Concentration-Dependent Micropore Diffusivity

$$D_{\mu i} = D_{\mu i}^\infty \frac{d\ln p_i}{d\ln q_i} \tag{31}$$

### 6.5 Arrhenius — Micropore Diffusivity

$$D_{\mu i} = D_{\mu i}^0\exp\!\left(-\frac{E_{ai}}{R_g T_s}\right) \tag{32}$$

### 6.6 Arrhenius — Barrier Coefficient

$$k_{bi} = k_{bi}^0\exp\!\left(-\frac{E_{bi}}{R_g T_s}\right) \tag{33}$$

---

## 7. Lumped (LDF) Mass Transfer Coefficients

### 7.1 Overall LDF (Film + Macropore + Micropore Resistances in Series)

$$\frac{1}{k_i} = \frac{R_p}{3k_{fi}}\frac{q_0}{c_0} + \frac{R_p^2}{15\varepsilon_p D_{pi}}\frac{q_0}{c_0} + \frac{R_c^2}{15D_{\mu i}} \tag{34}$$

### 7.2 Micropore LDF Coefficient (Barrier + Interior)

$$\frac{1}{K_{\mu i}} = \frac{1}{k_{bi}} + \frac{R_c^2}{15D_{\mu i}} \tag{35}$$

### 7.3 LDF Based on Macropore Concentration (LDFG)

$$\varepsilon_p\frac{\partial c_{pi}}{\partial t} + \rho_p\frac{\partial q_i}{\partial t} = K_{pi}(c_i - c_{pi}) \tag{36}$$

$$K_{pi} = \frac{15\varepsilon_p D_{pi}}{R_p^2}\cdot\frac{Bi_i}{5\varepsilon_p + Bi_i} \tag{37}$$

### 7.4 Global LDF (Film + Intraparticle, Juela et al.)

$$\frac{1}{K_i} = \frac{r_p}{3k_f}\frac{\rho_p q_0}{C_0} + \frac{r_p^2}{15\varepsilon_p D_{ep}}\frac{\rho_p q_0}{C_0} \tag{38}$$

---

## 8. External Film Mass Transfer — Correlations

### 8.1 Wakao–Funazkri

$$Sh = \frac{2k_{fi}R_p}{D_{mi}} = 2 + 1.1\,Sc^{1/3}\,Re^{0.6} \tag{39}$$

### 8.2 Wilson–Geankoplis (for $0.0015 < Re < 55$)

$$Sh = \frac{1.09}{\varepsilon_b}Re^{1/3}Sc^{1/3} \tag{40}$$

### 8.3 Ohashi et al.

$$\frac{k_f d_p}{D_m} = 2 + 1.58\,Re^{0.4}Sc^{1/3} \tag{41}$$

---

## 9. Axial Dispersion Correlations

### 9.1 Wakao–Smith

$$\frac{\varepsilon_b D_{zi}}{D_{mi}} = 20 + 0.5\,Sc\,Re \tag{42}$$

### 9.2 Ruthven / Hu et al.

$$D_L = \frac{ud_p}{\varepsilon}\!\left(\frac{20\varepsilon D_m}{ud_p} + \frac{1}{2}\right) \tag{43}$$

### 9.3 Suzuki–Smith (Lin et al.)

$$D_{ax} = 0.44D_m + 0.83\,U d_p \tag{44}$$

### 9.4 Soriano et al. (Juela et al.)

$$\frac{v_i d_p}{D_z} = 0.2 + 0.011\,Re^{0.48}\varepsilon_b \tag{45}$$

---

## 10. Molecular Diffusivity and Pore Diffusivities

### 10.1 Wilke–Chang

$$D_m = 7.4\times10^{-8}\frac{(\alpha_A M_s)^{0.5}T}{\mu V_m^{0.6}} \tag{46}$$

### 10.2 Knudsen Diffusivity

$$D_{ki} = 9700\,r_p\sqrt{\frac{T}{M}} \tag{47}$$

### 10.3 Combined Pore Diffusivity (Bosanquet)

$$\frac{1}{D_{pi}} = \frac{1}{D_{ki}} + \frac{1}{D_{mi}} \tag{48}$$

### 10.4 Pore Diffusion Coefficient

$$D_p = \frac{\varepsilon_p D_m}{\tau_p} \tag{49}$$

### 10.5 Effective Pore Diffusivity (Surface + Pore)

$$D_{ep} = \frac{D_s + D_p}{f'(C)\rho_b} \tag{50}$$

### 10.6 Surface Diffusion Coefficient (Xu et al.)

$$\frac{15D_s}{r_p^2} = 0.00129\left(\frac{D_m C_0}{r_p^2 q_0}\right)^{1/2} \tag{51}$$

### 10.7 Tortuosity

$$\tau_p = \varepsilon_p + 1.5(1-\varepsilon_p) \tag{52}$$

---

## 11. Volume-Averaged Adsorbed Concentrations

### 11.1 Composite Particle Average

$$\bar{q}_i = \frac{3\varepsilon_p}{R_p^3}\int_0^{R_p}c_{pi}R^2\,dR + \frac{3(1-\varepsilon_p)}{R_p^3}\int_0^{R_p}q_i R^2\,dR \tag{53}$$

### 11.2 Micropore Average

$$\bar{q}_i = \frac{3}{R_c^3}\int_0^{R_c}q_i r^2\,dr \tag{54}$$

---

## 12. Energy Balances

### 12.1 Gas-Phase Energy Balance

$$-\lambda_L\frac{\partial^2 T_g}{\partial z^2} + \rho_g C_g\frac{\partial(uT_g)}{\partial z} + \rho_g C_g\frac{\partial T_g}{\partial t} + \frac{1-\varepsilon_b}{\varepsilon_b}h_f a_s(T_g-T_s) + \frac{4\varepsilon_b}{d_{int}}h_w(T_g-T_w) = 0 \tag{55}$$

### 12.2 Solid-Phase Energy Balance

$$\rho_p C_s\frac{\partial T_s}{\partial t} = h_f a_s(T_g-T_s) + \sum_{i=1}^n(-\Delta H_i)\frac{\partial q_i}{\partial t} \tag{56}$$

### 12.3 Wall Energy Balance

$$\rho_w C_w\frac{\partial T_w}{\partial t} = h_w a_w(T_g-T_w) + U a_a(T_\infty-T_w) \tag{57}$$

---

## 13. Heat Transfer Correlations

### 13.1 Effective Axial Thermal Dispersion (Wakao–Funazkri)

$$\frac{\lambda_L}{k_g} = 7 + 0.5\,Pr\,Re \tag{58}$$

### 13.2 Gas–Particle Film Heat Transfer (Chilton–Colburn)

$$Nu = \frac{2h_f R_p}{k_g} = 2 + 1.1\,Pr^{1/3}Re^{0.6} \tag{59}$$

### 13.3 Wall Convective Heat Transfer

$$Nu_w = \frac{h_w d_{int}}{k_g} = 12.5 + 0.048\,Re \tag{60}$$

### 13.4 External Overall Heat Transfer Coefficient

$$\frac{1}{U} = \frac{1}{h_{w,int}} + \frac{d_{int}}{k_w}\ln\!\left(\frac{d_{ext}}{d_{int}}\right) + \frac{d_{int}}{d_{ext}h_{ext}} \tag{61}$$

### 13.5 External Natural Convection (Rayleigh–Nusselt)

$$\frac{h_{ext}L}{k_{ext}} = 0.68 + \frac{0.67\,Ra^{1/4}}{\left[1+(0.492/Pr)^{9/16}\right]^{4/9}} \tag{62}$$

---

## 14. Momentum Balance (Pressure Drop)

### 14.1 Ergun Equation

$$-\frac{\partial P}{\partial z} = K_D u + K_V u^2 \tag{63}$$

$$K_D = \frac{150\,\mu(1-\varepsilon_b)^2}{\varepsilon_b^3 d_p^2}, \qquad K_V = \frac{1.75(1-\varepsilon_b)\rho_g}{\varepsilon_b^3 d_p} \tag{64}$$

### 14.2 Monolith / Laminate Pressure Drop

$$\frac{\Delta P}{L} = \frac{32\varepsilon_b\mu u}{d^2} \tag{65}$$

### 14.3 Foam Pressure Drop

$$\frac{\Delta P}{L} = \alpha_s\frac{(1-\varepsilon_b)^2}{\varepsilon_b^3}\mu u + \beta_s\frac{(1-\varepsilon_b)}{\varepsilon_b^3}\rho_g u^2 \tag{66}$$

$$\alpha = 9.73\times10^2\,d_p^{0.743}(1-\varepsilon_b)^{-0.0982} \tag{67}$$

$$\beta = 3.68\times10^2\,d_p^{-0.7523}(1-\varepsilon_b)^{0.07158} \tag{68}$$

$$s = 12.979\left[\frac{1}{1-0.971(1-\varepsilon_b)^{0.5}} - (1-\varepsilon_b)^{0.5}\right] \tag{69}$$

---

## 15. Dimensionless Numbers

$$Re = \frac{d_p v_s\rho}{\mu}, \quad Sc = \frac{\mu}{\rho D_m}, \quad Pe = \frac{Z v_s}{D_z} \tag{70}$$

$$Sh = \frac{d_p k_{film}}{D_m}, \quad Bi = \frac{r_p k_{film}}{D_{pore}}, \quad St = \frac{3Lk_{film}}{r_p v} \tag{71}$$

---

## 16. Fixed-Bed Performance Parameters

### 16.1 Dynamic Adsorption Capacity

$$q_t = \frac{v\,c_0}{1000\,m}\int_0^t\!\left(1-\frac{c}{c_0}\right)dt \tag{72}$$

### 16.2 Equilibrium Loading from Breakthrough (Trapezoidal Integration)

$$q_e = \frac{J_{in}}{2M_i}\sum_{i=1}^N(2c_e - c_i - c_{i-1})(t_i - t_{i-1}) \tag{73}$$

### 16.3 Empty Bed Residence Time (EBRT)

$$EBRT = \frac{V_c}{Q_f} = \frac{A_c L_c}{Q_f} \tag{74}$$

### 16.4 Length of Mass Transfer Zone (LMTZ)

$$L_{MTZ} = \frac{t_s - (t_s-t_b)/2}{t_s}\cdot L_c \tag{75}$$

### 16.5 Column Efficiency

$$\psi = \frac{t_b}{t^*}, \qquad t^* = \int_0^\infty\!\left(1-\frac{c_{out}}{c_0}\right)dt \tag{76}$$

### 16.6 Fraction of Saturated Bed

$$H_b = \frac{Z_{t_b/t_s}}{Z}\times 100 \tag{77}$$

### 16.7 Axial Dispersion Significance (Cooney, 1991)

$$\gamma_p = \frac{\alpha^2(1-\varepsilon_b)}{15\varepsilon_b}\frac{r_p^2 K^2}{D_{ep}D_z}, \qquad \gamma_f = \frac{\alpha^2(1-\varepsilon_b)}{3\varepsilon_b}\frac{r_p K^2}{k_f D_z} \tag{78}$$

---

## 17. Breakthrough Models — Analytical / Empirical (Unique Forms)

> Bohart–Adams, Thomas, and Yoon–Nelson are mathematically equivalent (logistic function). Only one form is listed; their parameters are interchangeable via §17.2.

### 17.1 Logistic (Bohart–Adams / Thomas / Yoon–Nelson Unified Form)

$$\frac{c}{c_0} = \frac{1}{1+\exp\!\left[k_{YN}(\tau - t)\right]} \tag{79}$$

### 17.2 Parameter Interchangeability

$$k_{YN} = k_T c_0 = k_{BA}c_0 \tag{80}$$

$$\tau = \frac{a_0 x}{u c_0} = \frac{q_0 m}{\nu c_0} \tag{81}$$

### 17.3 Clark Model

$$\frac{c}{c_0} = \left[\frac{1}{1+A\exp(-rt)}\right]^{\!1/(n-1)} \tag{82}$$

$$A = \left(\frac{c_0^{n-1} - c_b^{n-1}}{c_b^{n-1}}\right)\exp(rt_b) \tag{83}$$

### 17.4 Modified Dose–Response (Yan et al.)

$$\frac{c}{c_0} = 1 - \frac{1}{1+\left(\dfrac{\nu c_0 t}{q_0 m}\right)^a} \tag{84}$$

### 17.5 Wolborska (Corrected Form, Wolborska & Pustelnik)

$$\ln\frac{c}{c_0} = \frac{\beta_a\rho q_0}{\varepsilon c_0}t - \frac{\beta_a x}{u} \tag{85}$$

Effective kinetic coefficient:

$$\beta_a = \frac{u}{2}\left[\sqrt{1+\left(\frac{u}{D_L\mu}\right)^2}-1\right] \tag{86}$$

### 17.6 Klinkenberg Model

$$\frac{c}{c_0} = \frac{1}{2}\left[1 + \mathrm{erf}\!\left(\sqrt{\tau} - \sqrt{\zeta} + \frac{1}{8\sqrt{\tau}} + \frac{1}{8\sqrt{\zeta}}\right)\right] \tag{87}$$

$$\zeta = \frac{K_{fa}x}{u}, \qquad \tau = \frac{K_{fa}}{K(1-\varepsilon)}\!\left(t - \frac{\varepsilon x}{u}\right) \tag{88}$$

### 17.7 Dima et al. (Error-Function Form)

$$\frac{c}{c_0} = \frac{1}{2}\left[1+\mathrm{erf}\!\left(\frac{v_d t - x}{\sqrt{2}\,\sigma_a}\right)\right] \tag{89}$$

### 17.8 Chern–Chien (Langmuir-type)

$$t = t_{1/2} + \frac{\varepsilon}{K_{fa}\rho q_0 c_0}\!\left[\ln\frac{2x}{1-x} + \frac{1}{K_L c_0}\ln\frac{1}{2(1-x)}\right] \tag{90}$$

### 17.9 Chern–Chien (Freundlich-type)

$$t = t_{1/2} + \frac{\varepsilon}{K_{fa}\rho q_0 c_0}\!\left[\ln\frac{2x}{1-x} - \frac{1}{n-1}\ln\frac{1-x^{n-1}}{2^{1-n}}\right] \tag{91}$$

where $x = c/c_0$ in both Chern–Chien forms.

### 17.10 Gompertz (Chu 2020b)

$$\frac{c}{c_0} = \exp\!\left[-\exp(\alpha_G - \beta_G t)\right] \tag{92}$$

### 17.11 Log-Gompertz (Chu 2020b)

$$\frac{c}{c_0} = \exp\!\left[-\exp(\alpha_G - \beta_G\ln t)\right] \tag{93}$$

### 17.12 Weibull (Chu 2021)

$$\frac{c}{c_0} = 1 - \exp\!\left[-\left(\frac{t}{\tau}\right)^k\right] \tag{94}$$

Weibull breakthrough rate:

$$\frac{d(c/c_0)}{dt} = \frac{k}{\tau}\!\left(\frac{t}{\tau}\right)^{k-1}\exp\!\left[-\left(\frac{t}{\tau}\right)^k\right] \tag{95}$$

### 17.13 Avrami (Singh et al.)

$$\frac{c}{c_0} = 1 - \exp(-k t^n) \tag{96}$$

### 17.14 Gudermannian Model (Hu et al. 2021)

$$\frac{c}{c_0} = \frac{1}{2}\left[1 + \frac{2}{\pi}\arctan\sinh[k(t-\tau)]\right] \tag{97}$$

### 17.15 Error-Function Model (Hu et al. 2021)

$$\frac{c}{c_0} = \frac{1}{2}\left[1 + \mathrm{erf}[k(t-\tau)]\right] \tag{98}$$

### 17.16 Hyperbolic Tangent Model (Hu et al. 2019)

$$\frac{c}{c_0} = \frac{1}{2}\{1+\tanh[k(t-\tau)]\} \tag{99}$$

### 17.17 Log-Normal (Chu & Hashim)

$$\frac{c}{c_0} = \frac{1}{2}\left\{1 + \mathrm{erf}\!\left[\frac{\ln t - b}{\sqrt{2}\,a}\right]\right\} \tag{100}$$

### 17.18 Parallel Sigmoidal (Blagojev et al.)

$$\frac{c}{c_0} = p\!\left[1-\frac{1}{1+(t/\tau_1)^{k_1}}\right] + (1-p)\!\left[1-\frac{1}{1+(t/\tau_2)^{k_2}}\right] \tag{101}$$

### 17.19 Log-Modified Bohart–Adams (Apiratikul & Chu)

$$\frac{c}{c_0} = \frac{1}{1+\exp\!\left(k_{BA}\ln\dfrac{a_0 x}{u c_0} - k_{BA}\ln(c_0 t)\right)} \tag{102}$$

### 17.20 Log-Modified Yoon–Nelson (Apiratikul & Chu)

$$\frac{c}{c_0} = \frac{1}{1+\exp[k_{YN}\ln\tau - k_{YN}\ln t]} \tag{103}$$

---

## 18. Fractal-Like Breakthrough Models (Hu et al. 2024)

### 18.1 Fractal-Like Rate Constant

$$k = k_0 t^{-h}, \quad t\geq 1,\quad 0\leq h\leq 1 \tag{104}$$

### 18.2 Fractal-Like Yoon–Nelson

$$\frac{c}{c_0} = \frac{1}{1+\exp\!\left[\dfrac{k_{YN,0}}{1-h}(\tau^{1-h}-t^{1-h})\right]} \tag{105}$$

### 18.3 Fractal-Like Clark

$$\frac{c}{c_0} = \left[\frac{1}{1+A_0\exp\!\left(-\dfrac{r}{1-h}t^{1-h}\right)}\right]^{1/(n-1)} \tag{106}$$

### 18.4 Fractal-Like Gudermannian

$$\frac{c}{c_0} = \frac{1}{2}\left[1+\frac{2}{\pi}\arctan\sinh[k_0 t^{-h}(t-\tau_0)]\right] \tag{107}$$

### 18.5 Fractal-Like Error Function

$$\frac{c}{c_0} = \frac{1}{2}\left\{1+\mathrm{erf}[k_0 t^{-h}(t-\tau_0)]\right\} \tag{108}$$

---

## 19. $n$-Order Bohart–Adams (Hu et al. 2021)

$$\frac{c}{c_0} = \left\{1 + n a_0^{1-n}c_0^{n-1}\left[\left(\frac{1+(n-1)k_n a_0^{n-1}c_0^{n-1}x/u}{1+(n-1)k_n a_0^{n-1}c_0^n t}\right)^{1/(n-1)} - 1\right]\right\}^{-1/n} \tag{109}$$

---

## 20. Parametric / Characteristic Curve Equations (Hu, Xie & Zhang 2020)

> Four descriptors: $\mu_{max}$ (max specific breakthrough rate), $\lambda$ (lag time), $t_i$ (inflection point), $t_{50}$ (half-breakthrough time).

### 20.1 Yoon–Nelson / BA / Thomas

$$\mu_{max} = \frac{k_{YN}}{4}, \qquad \lambda = \tau - \frac{2}{k_{YN}}, \qquad t_i = t_{50} = \tau \tag{110}$$

### 20.2 Clark Model

$$\mu_{max} = r\cdot\frac{n-1}{n^{(n-1)/n}} \tag{111}$$

$$t_i = -\frac{1}{r}\ln\frac{n-1}{A} \tag{112}$$

$$t_{50} = \frac{1}{r}\ln\frac{A}{2^{n-1}-1} \tag{113}$$

$$t_{50} - t_i = \frac{1}{r}\ln\frac{n-1}{2^{n-1}-1} \tag{114}$$

### 20.3 Dose–Response Model

$$\mu_{max} = \frac{b}{4a}(a-1)^{(a-1)/a}(a+1)^{(a+1)/a} \tag{115}$$

$$t_i = \frac{1}{b}\!\left(\frac{a-1}{a+1}\right)^{1/a} \tag{116}$$

$$t_{50} = \frac{1}{b} \tag{117}$$

### 20.4 Modified Breakthrough Forms (with $\mu_{max}$ and $\lambda$)

Logistic (BA / Thomas / YN):

$$\frac{c}{c_0} = \frac{1}{1+\exp\!\left[4\mu_{max}(\lambda - t) + 2\right]} \tag{118}$$

Clark:

$$\frac{c}{c_0} = \left\{1 + (n-1)\exp\!\left[\mu_{max}\cdot\frac{n^{1/(n-1)}}{n-1}(\lambda - t) + n\right]\right\}^{-1/(n-1)} \tag{119}$$

Dose-Response:

$$\frac{c}{c_0} = 1 - \frac{1}{1+\left[\dfrac{\lambda(\lambda\mu_{max}+1+\lambda\mu_{max})^2 - 1}{1+(\lambda\mu_{max}+1+\lambda\mu_{max})^2}\cdot\dfrac{t}{\lambda}\right]^{\lambda\mu_{max}+1+\lambda\mu_{max})^2}} \tag{120}$$

---

## 21. Travelling Wave Solutions (Myers et al. 2023)

### 21.1 Concentration–Adsorbed Fraction Relationship

$$F = \frac{G}{G_e} \tag{121}$$

### 21.2 Wave Speed (General)

$$\hat{v} = \frac{1}{G_e + \delta_1} \tag{122}$$

### 21.3 Wave Speed (Linear LDF Sink, Dimensional)

$$v = \frac{u}{1 + \rho_b q_e/(\varepsilon\, c_{in})} \tag{123}$$

### 21.4 Wave Speed (Nonlinear Langmuir Sink)

$$v = \frac{u}{1 + \rho_b q_m/\!\left(\varepsilon\!\left(c_{in} + k_{de}/k_{ad}\right)\right)} \tag{124}$$

### 21.5 Wave Speed (Sips Sink)

$$v = \frac{u}{1 + \rho_b q_m/\!\left(\varepsilon\!\left(c_{in} + k_{de}/(k_m c_{in}^{m-1})\right)\right)} \tag{125}$$

### 21.6 Breakthrough Curve — Linear Sink

$$\frac{c(L,t)}{c_{in}} = 1 - \frac{1}{2}\exp\!\left[k_L(t_{1/2}-t)\right] \tag{126}$$

First breakthrough time:

$$t_b = t_{1/2} - \frac{\ln 2}{k_L} \tag{127}$$

### 21.7 Breakthrough Curve — Nonlinear (Langmuir) Sink

$$\frac{c(L,t)}{c_{in}} = \frac{1}{1+\exp\!\left[k_{ad}c_{in}(t_{1/2}-t)\right]} \tag{128}$$

$$\frac{q(L,t)}{q_m} = \frac{k_{ad}c_{in}}{(k_{ad}c_{in}+k_{de})\left[1+\exp(k_{ad}c_{in}(t_{1/2}-t))\right]} \tag{129}$$

### 21.8 Concentration Profile Throughout Column — Nonlinear Sink

$$\frac{c}{c_{in}} = \frac{1}{1+\exp\!\left[k_{ad}c_{in}\!\left(\dfrac{x-L}{v}+(t_{1/2}-t)\right)\right]} \tag{130}$$

### 21.9 Breakthrough Curve — Sips Sink

$$\frac{c}{c_{in}} = \frac{mG_e + 2(1-m) - (1-m)\exp\!\left[\dfrac{(mG_e+1-m)k_m c_{in}^m(x-L-v(t-t_{1/2}))}{vG_e}\right]}{mG_e + 2(1-m) + mG_e\exp\!\left[\dfrac{(mG_e+1-m)k_m c_{in}^m(x-L-v(t-t_{1/2}))}{vG_e}\right]} \tag{131}$$

where $G_e = \dfrac{1}{1+k_{de}/(k_m c_{in}^m)}$

### 21.10 Bohart–Adams Full Solution (Appendix, Myers et al.)

$$\frac{c(L,t)}{c_{in}} = \frac{1}{1-\exp(-k_{ad}c_{in}t)+\exp\!\left(-k_{ad}\!\left(c_{in}t - \dfrac{\rho_b q_m L}{u_{in}}\right)\right)} \tag{132}$$

$$\frac{q(L,t)}{q_m} = 1 - \frac{1}{1-\exp\!\left(-\dfrac{\rho_b k_{ad}q_m L}{u_{in}}\right)+\exp\!\left(k_{ad}\!\left(c_{in}t-\dfrac{\rho_b q_m L}{u_{in}}\right)\right)} \tag{133}$$

### 21.11 Simplified BA Half-Time

$$t_{1/2}^{BA} = \frac{\rho_b q_m L}{u_{in}c_{in}} \tag{134}$$

### 21.12 Adsorbent Exhaustion Time Estimate (Sips)

$$t_e \approx \frac{L}{u_{in}}\!\left[1+\frac{\rho_b q_m}{\varepsilon\!\left(c_{in}+\dfrac{k_{de}}{k_m c_{in}^{m-1}}\right)}\right] \tag{135}$$

---

## 22. Multicomponent Breakthrough Models (Hu et al. 2022)

### 22.1 Logistic-Based (Weakly Adsorbed Components)

$$\frac{C_t}{C_0} = \frac{1}{1+\exp[k(s-t)]} + \frac{c\cdot k\,\exp[k^*(s^*-t)]}{\{1+\exp[k^*(s^*-t)]\}^2} \tag{136}$$

### 22.2 Gompertz-Based (Weakly Adsorbed Components)

$$\frac{C_t}{C_0} = \exp\{-\exp[k(s-t)]\} + c\cdot k\,\exp\{-\exp[k(s-t)]\}\cdot\exp[k(s-t)] \tag{137}$$

### 22.3 Equilibrium Loading — Logistic Form

$$q_i = \frac{v C_{0,i}}{1000\,m}\!\left\{\frac{1}{k_i}\ln\frac{1+\exp(k_i s_i)}{1+\exp(k_i(s_i-t_{total}))} + \frac{c_i}{1+\exp(k_i s_i)} - \frac{c_i}{1+\exp(k_i(s_i-t_{total}))}\right\} \tag{138}$$

### 22.4 Equilibrium Loading — Gompertz Form

$$q_i = \frac{v C_{0,i}}{1000\,m}\!\left\{t_{total} - \int_0^{t_{total}}\!\exp\{-\exp[k_i(s_i-t)]\}\,dt + c_i\!\left(\exp\{-\exp(-k_i s_i)\} - \exp\{-\exp(k_i(s_i-t_{total}))\}\right)\right\} \tag{139}$$

---

## 23. Error and Goodness-of-Fit Statistics

### 23.1 Coefficient of Determination

$$R^2 = 1 - \frac{\sum_{i=1}^n(y_i-\hat{y}_i)^2}{\sum_{i=1}^n(y_i-\bar{y})^2} \tag{140}$$

### 23.2 Adjusted $R^2$

$$\text{Adj.}R^2 = 1 - \frac{(1-R^2)(n-1)}{n-p} \tag{141}$$

### 23.3 Root Mean Squared Error

$$RMSE = \sqrt{\frac{1}{N-2}\sum_{i=1}^N(q_{exp}-q_{cal})^2} \tag{142}$$

### 23.4 Chi-Squared (Reduced)

$$\chi^2 = \frac{1}{f}\sum_{i}^n\omega_i(y_i-\hat{y}_i)^2 \tag{143}$$

### 23.5 Absolute Average Deviation

$$AAD = \frac{1}{N}\sum_{i=1}^N\left|\frac{(c_{t,out}/c_0)_{exp} - (c_{t,out}/c_0)_{pred}}{(c_{t,out}/c_0)_{exp}}\right| \tag{144}$$

### 23.6 Sum of Squared Errors

$$SSE = \sum_{i=1}^n(x_{cal} - x_{meas})^2 \tag{145}$$

### 23.7 $F$-Test (Nested Models)

$$F = \frac{(RSS_1-RSS_2)/(df_1-df_2)}{RSS_2/df_2} \tag{146}$$

### 23.8 Akaike Information Criterion

$$AIC = \begin{cases} n\ln(RSS/n) + 2p & n/p \geq 40 \\[4pt] n\ln(RSS/n) + 2p + \dfrac{2p(p+1)}{n-p-1} & n/p < 40 \end{cases} \tag{147}$$

### 23.9 Akaike Weight

$$W_A = \frac{1}{1+\exp(0.5\,\Delta AIC)} \tag{148}$$

---

## Nomenclature

| Symbol | Description | Units |
|--------|-------------|-------|
| $a_0$ | Bohart–Adams adsorption capacity per unit bed volume | mg L⁻¹ |
| $A$ | Clark constant | — |
| $A_c$ | Column cross-section area | cm² |
| $Bi$ | Biot number | — |
| $C$, $c$ | Fluid-phase solute concentration | mg L⁻¹ or kg m⁻³ |
| $c_{in}$, $C_0$ | Inlet concentration | mg L⁻¹ |
| $c_{pi}$ | Macropore concentration | mg L⁻¹ |
| $c_e$ | Equilibrium concentration | mg L⁻¹ |
| $D$ | Axial diffusion coefficient | m² s⁻¹ |
| $D_{ax}$, $D_L$, $D_{zi}$ | Axial dispersion coefficient | m² s⁻¹ |
| $D_{ki}$ | Knudsen diffusivity | cm² s⁻¹ |
| $D_m$, $D_{mi}$ | Molecular diffusivity | m² s⁻¹ |
| $D_{pi}$ | Macropore (effective pore) diffusivity | m² s⁻¹ |
| $D_{\mu i}$ | Micropore diffusivity | m² s⁻¹ |
| $D_s$ | Surface diffusion coefficient | m² s⁻¹ |
| $D_{ep}$ | Effective pore diffusivity (combined) | m² s⁻¹ |
| $d_p$, $d_{int}$, $d_{ext}$ | Particle / internal / external column diameter | m |
| $Da$ | Dahmköhler number | — |
| $E_{ai}$, $E_{bi}$ | Activation energies | J mol⁻¹ |
| $f$ | Degrees of freedom | — |
| $G_e$ | Dimensionless equilibrium adsorbed fraction | — |
| $h$ | Fractal-like exponent | — |
| $h_f$ | Gas–particle film heat transfer coefficient | W m⁻² K⁻¹ |
| $h_w$ | Wall heat transfer coefficient | W m⁻² K⁻¹ |
| $h_{ext}$ | External convective heat transfer coefficient | W m⁻² K⁻¹ |
| $J_{in}$ | Inlet volume flux | m³ s⁻¹ |
| $k$ | Rate constant (generic) or curvature parameter | various |
| $k_{ad}$, $k_{BA}$, $k_T$, $k_{YN}$ | Adsorption / model rate constants | various |
| $k_{bi}$ | Micropore surface barrier coefficient | s⁻¹ |
| $k_{de}$ | Desorption rate constant | s⁻¹ |
| $k_f$, $k_{fi}$, $k_{film}$ | External film mass transfer coefficient | m s⁻¹ |
| $k_g$ | Gas thermal conductivity | W m⁻¹ K⁻¹ |
| $k_L$ | LDF rate constant (linear kinetics) | s⁻¹ |
| $k_m$, $K_S$ | Sips adsorption coefficient / Sips constant | m³(m) kg⁻(m) s⁻¹ |
| $k_w$ | Wall conductivity | W m⁻¹ K⁻¹ |
| $K_D$, $K_V$ | Darcy and inertial Ergun coefficients | — |
| $K_F$ | Freundlich constant | — |
| $K_i$, $K_{\mu i}$ | Overall / micropore LDF coefficient | s⁻¹ |
| $K_L$ | Langmuir constant | m³ kg⁻¹ |
| $K_{fa}$ | Volumetric mass transfer coefficient | min⁻¹ |
| $K_0$ | Fractal-like rate constant | min⁻(1−h) |
| $L$, $L_c$ | Bed / column length | m or cm |
| $L_{MTZ}$ | Length of mass transfer zone | m |
| $m$ | Adsorbent mass; Sips exponent | g; — |
| $M_i$ | Total adsorbent mass | kg |
| $M$ | Molecular weight | g mol⁻¹ |
| $n$ | Freundlich exponent / model parameter | — |
| $n$ | Data count | — |
| $Nu$ | Nusselt number | — |
| $p$ | Number of model parameters | — |
| $P$ | Total pressure | Pa |
| $Pe$ | Peclet number | — |
| $Pr$ | Prandtl number | — |
| $q$, $q_i$ | Adsorbed-phase concentration | mg g⁻¹ or kg kg⁻¹ |
| $q_e$ | Equilibrium adsorbed amount | mg g⁻¹ |
| $q_m$, $q_{max}$ | Maximum adsorption capacity | mg g⁻¹ |
| $q^*$ | Equilibrium loading at inlet concentration | mg g⁻¹ |
| $Q$, $Q_f$, $\nu$ | Volumetric flow rate | mL min⁻¹ |
| $R$ | Radial coordinate in macroparticle | m |
| $r$ | Radial coordinate in microparticle; Clark constant | m; min⁻¹ |
| $R_c$ | Microparticle radius | m |
| $R_g$ | Universal gas constant | J mol⁻¹ K⁻¹ |
| $R_p$ | Macroparticle radius | m |
| $Ra$ | Rayleigh number | — |
| $Re$ | Reynolds number | — |
| $RSS$ | Residual sum of squares | — |
| $s$ | Location parameter in Gompertz / logistic models | min |
| $Sc$ | Schmidt number | — |
| $Sh$ | Sherwood number | — |
| $St$ | Stanton number | — |
| $t$ | Time | s or min |
| $t_b$ | Breakthrough time | min |
| $t_e$ | Exhaustion time | min |
| $t_i$ | Inflection point time | min |
| $t_s$ | Saturation time | min |
| $t_{1/2}$, $t_{50}$, $\tau$ | Half-breakthrough time ($c/c_0=0.5$) | min |
| $t^*$ | Stoichiometric breakthrough time | min |
| $T_g$, $T_s$, $T_w$, $T_\infty$ | Gas / solid / wall / ambient temperature | K |
| $u$, $u_{in}$ | Interstitial velocity | m s⁻¹ |
| $U$ | External overall heat transfer coefficient | W m⁻² K⁻¹ |
| $V_m$ | Molar volume of adsorbate at boiling point | cm³ mol⁻¹ |
| $v$, $v_s$ | Wave velocity; superficial velocity | m s⁻¹ |
| $v_d$ | Linear velocity of adsorption zone | cm min⁻¹ |
| $x$ | Axial bed coordinate; $c/c_0$ in Chern–Chien | m; — |
| $Z$, $L$ | Bed height | m |
| $\alpha_A$ | Solvent association parameter | — |
| $\alpha_G$, $\beta_G$ | Gompertz model parameters | —; min⁻¹ |
| $\beta_a$ | Effective kinetic coefficient (Wolborska) | min⁻¹ |
| $\delta_1$, $\delta_2$, $\delta_3$ | Non-dimensional groups (Myers et al.) | — |
| $\Delta H_i$ | Isosteric heat of adsorption | J mol⁻¹ |
| $\varepsilon$, $\varepsilon_b$ | Bed void fraction | — |
| $\varepsilon_p$ | Particle porosity | — |
| $\eta$ | Travelling wave coordinate | — |
| $\gamma_p$, $\gamma_f$ | Axial dispersion significance parameters | — |
| $\lambda$ | Lag time | min |
| $\lambda_L$ | Effective axial thermal dispersion | W m⁻¹ K⁻¹ |
| $\mu$ | Dynamic viscosity | kg m⁻¹ s⁻¹ |
| $\mu_{max}$ | Maximum specific breakthrough rate | min⁻¹ |
| $\rho$, $\rho_g$ | Fluid density | kg m⁻³ |
| $\rho_b$ | Bed bulk density | kg m⁻³ |
| $\rho_p$ | Particle density | kg m⁻³ |
| $\sigma_a$ | Standard deviation of adsorption zone position | cm |
| $\tau_p$ | Particle tortuosity | — |
| $\psi$ | Column efficiency | — |

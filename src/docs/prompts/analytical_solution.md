Good pairing — Danilov et al. is essentially a solved instance of your prompt's structure (ADM + LDF + nonlinear isotherm + two-phase heat balance), minus the wall term and with Sips instead of Toth. Here's the usage map, plus some errata you need to know before transplanting anything.

## 1. What transfers directly into Part A

**Variable dictionary.** They work in mole fraction $y$ and molar flux $F$; you work in concentration. For dilute ideal gas, $c = \rho_{mol}^G y$ with $\rho_{mol}^G = P/RT$, and their $(1-\varepsilon_b)\rho_b$ source prefactor is your $(1-\varepsilon)\rho_p$ (careful: they call $\rho_b = 588.5$ kg/m³ "bulk density" while also carrying $(1-\varepsilon_b)$ — that double-counts unless $\rho_b$ is actually particle density; your prompt's $(1-\varepsilon)\rho_p$ convention is the clean one, keep it).

**The flux recasting is the piece worth stealing.** Their A.3–A.4 define

$$F = uc - \varepsilon D_L \frac{\partial c}{\partial z}, \qquad \varepsilon\frac{\partial c}{\partial t} = -\frac{\partial F}{\partial z} - (1-\varepsilon)\rho_p\frac{\partial q}{\partial t}$$

This does three jobs for your prompt simultaneously: (i) it makes the conservation check trivial — integrate over the bed and you get $\frac{d}{dt}\int_0^L[\varepsilon c + (1-\varepsilon)\rho_p q]\,dz = uc_f - F(L,t)$, which is exactly the identity you're asked to prove and the discrete invariant your FV scheme should preserve; (ii) their inlet condition A.9, $F(0,t) = uc_f$, *is* the Danckwerts inlet BC, so the paper hands you the BC treatment; (iii) it's what makes their quadrature solution possible.

**Energy balance derivation route.** Your prompt asks for the pseudo-homogeneous single-$T$ balance. Derive it *from* their two-temperature system (Table 1 gas balance + A.13 solid balance): sum the two, the $\alpha_v(T^S - T^G)$ terms cancel, and you land exactly on

$$C_h\frac{\partial T}{\partial t} + u\rho_g c_{p,g}\frac{\partial T}{\partial z} = \lambda_{eff}\frac{\partial^2 T}{\partial z^2} + (1-\varepsilon)\rho_p(-\Delta H)\frac{\partial q}{\partial t}$$

with $C_h = \varepsilon\rho_g c_{p,g} + (1-\varepsilon)\rho_p c_{p,s}$. The justification for lumping is their Eq. (4)/(A.15): the interphase gap is $\Delta T = (1-\varepsilon)\rho_p(-\Delta H)\,k\psi/\alpha_v$, so you get a quantitative a-priori criterion — pseudo-homogeneous is valid when $(1-\varepsilon)\rho_p(-\Delta H)k\,q_f/\alpha_v \ll \Delta T_{ad}$. That's a stronger justification than the usual hand-wave. The wall-loss term $4h_w(T-T_{wall})/d_{col}$ is absent in the paper (their column is effectively adiabatic); it just adds as a sink in the lumped balance, or as an extra term in the integrand of their heat-flux quadrature (3) if you follow their route.

**Isotherm swap is trivial.** Their framework is isotherm-agnostic — the isotherm enters only through pointwise evaluation of $q^*(c,T)$ in Eq. (10) and through $\partial q^*/\partial c$ inside $\gamma_q$. Replace Sips with Toth: $\partial q^*/\partial c = n_s b\left[1+(bc)^{t_T}\right]^{-(1+1/t_T)}$. Nothing structural changes.

## 2. The core asset: their ψ solution is your "analytically tractable limiting case"

The genuinely novel move in the paper (Appendix B) is collapsing the coupled system via the chain-rule substitutions $\partial y/\partial t = (\partial y/\partial q)(\partial q/\partial t)$ into a scalar ODE for the driving force $\psi = q^* - q$:

$$\frac{\partial\psi}{\partial t} = -\gamma_\psi k\,\psi \;\Rightarrow\; \psi \propto e^{-kt}$$

then stitching a **symmetric front ansatz** around the stoichiometric time (their Eq. 1), from which every field — $F$, $c$, $Q$, $T_G$, $q$, $T_S$ — follows by marching quadrature (Eqs. 2–8), no iteration, no PDE solve. Present this in your solution as the **constant-pattern / travelling-wave limit** of the full model, alongside (i) the linear-isotherm exact solution (their references Rasmuson–Neretnieks 1980 and Liao–Shiau 2000 are the canonical sources) and (ii) the $k\to\infty$ equilibrium/shock limit (De Vault 1943, Tondeur 1987 — also in their bibliography; the reference list is basically a curated map of your limiting cases). You'll need the front kinematics they use but don't spell out: for a clean bed, $t_s = \frac{\varepsilon L}{u}(1+\Lambda)$, $u_f = L/t_s$, with $\Lambda = \frac{(1-\varepsilon)\rho_p q^*(c_f,T)}{\varepsilon c_f}$.

There's also a payoff specific to your existing pipeline: the symmetric double-exponential front is, to leading order, a logistic — i.e., the Thomas/Yoon–Nelson shape your ultracode already fits. The Danilov derivation is the mechanistic bridge: constant-pattern LDF ⇒ symmetric exponential sigmoid, with the fitted Thomas rate ≈ $\gamma_\psi k$ and Yoon–Nelson $\tau \approx t_s$. So your fitted parameters from the PEI@SiO₂ breakthrough data become direct seeds for $k$ in the mechanistic model, and Part A stops being disconnected from your empirical work.

The $\gamma \approx 1$ assumption is safe for you: the correction is $O(1/\Lambda)$, and for amine sorbents $\Lambda \sim 10^2$–$10^3$ (e.g. $q_f \approx 2$ mol/kg, $c_f \approx 4$ mol/m³ at 10% CO₂ gives $\Lambda \sim 500$), so sub-1% error.

## 3. Errata and traps — read before implementing

- **Sign inconsistency in the accepted manuscript.** As printed, A.1/A.4/A.8 have the adsorption source entering the gas balance with $+$, which would make flux *grow* along the bed during adsorption; main-text Eq. (2) and A.18 have the physically correct $-$. Trust Eq. (2)/(A.18) and your own prompt's form. Derive from your control volume, don't transplant.
- **The $\gamma_q,\gamma_\psi$ algebra as printed doesn't compose.** Substituting the nomenclature definition of $\gamma_q$ into $\gamma_\psi$ collapses to 0, not the claimed $\approx 1$. The final journal version may have fixed it; either rederive the correction yourself or set both to 1 (justified above for your $\Lambda$).
- **The symmetric front is an ansatz, not a result.** It presumes a fully developed constant pattern, so it can't capture front formation near $z=0$, and it will misrepresent tailing — their own Fig. 1 shows the analytical curve less tailed than both COMSOL and experiment. For PEI@SiO₂ specifically, chemisorption heat effects and slow amine kinetics tend to produce asymmetric fronts; treat their solution as a limiting case and a benchmark, not the production model. Same caveat for constant $k$: amine uptake is closer to reaction-limited with $k(T) = k_0 e^{-E_a/RT}$.
- **Their concentration reconstruction (Eq. 5/A.20) integrates a growing exponential** $e^{+Pe\,z/L}$ forward from the inlet. Fine at $Pe=10$ on their grid; ill-conditioned for $Pe \gtrsim 50$. At high $Pe$ use the plug-flow closed form $c = F/u$, or solve the two-point BVP properly.
- Constant $u$ and trace-component assumptions are baked in — fine for your inert-carrier prompt, but state them.
- One typo in **your own prompt**: the wall term denominator reads `d_{\mathrm{cfile:///C:/Users/User/...ol}}` — a file path got pasted into the LaTeX. Fix to $d_{col}$ before sending it anywhere.

## 4. Suggested execution order

Derive Part A from the control volume in flux form (paper as template, correct sign), do the two-T → one-T lumping with the A.15 error bound, and add the wall sink. Nondimensionalise yourself — the paper only gives $Pe_G, Pe_T$; you'll want the full set: $Pe$, $Pe_T$, transfer-unit number $N = k\varepsilon L/u$, capacity ratio $\Lambda$, thermal-to-mass front speed ratio $\omega = (1+\Lambda)\varepsilon\rho_g c_{p,g}/C_h$ (decides whether the thermal wave leads or lags the mass front — the paper never addresses this regime split; Ruthven–Garg–Crawford 1975 from their references does), adiabatic rise $\Delta T_{ad} = (1-\varepsilon)\rho_p q_f(-\Delta H)/C_h$, isotherm sensitivity $(-\Delta U_b/RT_f)(\Delta T_{ad}/T_f)$, and wall Stanton number. For the full nonlinear solve, do conservative finite-volume method-of-lines with a stiff integrator and Danckwerts BCs — then use the paper twice for V&V: reproduce their Fig. 1–2 from the complete, self-consistent Table 2 parameter set (that table is rare and worth more than the algorithm), and check your solver collapses onto their ψ-quadrature in the dilute constant-pattern limit before switching the isotherm to Toth.

Want me to implement the ψ-quadrature (Eqs. 1–9, Table 2) as the verification script, or start on the nondimensionalisation and limiting-case proofs?
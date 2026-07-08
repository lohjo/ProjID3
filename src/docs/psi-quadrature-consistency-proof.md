# Ψ-Quadrature Consistency and Error Bounds — Full Resolution

**Status:** complete proof/disproof, self-contained (Part 2 deliverable, 2026-07-08).
**Companions:** `mechanistic-model.md` (MM; Parts B, D.3–D.8, V.5), `src/solver/psi_quadrature_verify.py` (Danilov implementation + errata E1–E5, F1–F5), `src/solver/psi_quadrature_proof_checks.py` (numerical verification of every constant below).
**Notation:** $\lambda := bc_f$ throughout ("$bc_f$" of the problem statement); $k$ = LDF rate; $w := c/c_f \in (0,1)$; Route A = derived constant-pattern wave (MM D.3/D.8); Route B = Danilov ψ-quadrature (symmetric two-branch exponential ansatz + marching quadratures, MM-external, errata-corrected per `psi_quadrature_verify.py`).

---

## 0. Verdict

**(a) Disproved as stated; a precisely weakened form is proved.** Route A's outlet curve does converge to the symmetric logistic $1/(1+e^{-k\lambda(t-t_{st})})$ as $\lambda\to0$ (Theorem 4.1 — the "short clean argument" exists). Route B's does **not**, under either reading of its parameters. With $\beta=1$ frozen (the Claim's literal instruction) its front width stays $\Theta(1/k)$ while the true width diverges as $1/(k\lambda)$: the sup-norm distance tends to $1/2$ (Theorem 4.2). With $\beta$ honestly re-evaluated by Route B's *own* chain rule at the Henry point ($\beta=\lambda/(1+\lambda)$, Lemma 2.4), the two curves agree in centering (exactly), first moment (exactly), symmetry, and both tail exponents to $O(\lambda)$ — but the stitched double exponential is not a logistic, and the sup-norm gap converges to the universal constant

$$\sup_{t}\bigl|W_A - B\bigr| \;\longrightarrow\; \tfrac{3}{2}-\sqrt{2} \;=\; 0.08578\ldots \qquad (\lambda\to0),$$

which no rescaling removes (Theorem 4.3). Part (a)'s premise — "symmetry is the only wrong assumption" — is itself an instance of the conflation the problem warns about: the ansatz is wrong in *rate* (β-freeze) and in *functional form* (exponential stitch vs. logistic), not only in symmetry.

**(b) Route B converges to its own continuum ansatz limit, never to Route A, for any $\lambda>0$.** The marching quadratures are a stable, first-order-consistent discretisation of a *fixed affine operator applied to the seed* — so Lax-type convergence holds, but to $\mathcal M[s]$ (the affine image of the ansatz), not to Route A's $\varphi$ (Theorem 5.1). Convergence to Route A is *impossible* for $\lambda>0$: Route B's converged output is shape-universal (a single fixed profile $\Phi(k\,\cdot)$ up to translation and amplitude, Lemma 3.4) with tail-rate ratio $\equiv 1$ (Lemma 3.5), while Route A's profile has the $\lambda$-dependent tail-rate ratio $\ell_-/\ell_+ = 1+\lambda$ (Lemma 2.3). The error floor, as explicit functions of $\lambda$:

| invariant | Route A (exact) | Route B (converged) | floor |
|---|---|---|---|
| tail-rate ratio | $1+\lambda$ | $1$ | $\lambda$ **exactly** |
| skewness $\gamma_1$ | $\dfrac{2\lambda^3+6\lambda^2+6\lambda+6(\zeta(3)-1)\lambda(1+\lambda)}{[\lambda^2+\tfrac{\pi^2}{3}(1+\lambda)]^{3/2}}$ | $0$ | $\gamma_1(\lambda)$: $\;\sim1.2087\,\lambda\to 2$ |
| variance ($t$-units, $\beta=1$) | $[\lambda^2+\tfrac{\pi^2}{3}(1+\lambda)]/(k\lambda)^2$ | $2/k^2$ | ratio $\to\infty$ as $\lambda\to0$, $\to\tfrac12$ as $\lambda\to\infty$ |

The floor vanishes as $\lambda\to0$ only in the weak (moment/tail) sense — the sup-norm floor tends to $3/2-\sqrt2$ (corrected β) or $1/2$ (frozen β), consistent with (a). The wrong-shape information is baked in **jointly at Eq. 1's ansatz and Appendix B's freezing of $\beta$** — and the freeze is the deeper of the two: the *exact* driving-force law on the constant pattern is $\partial_t\psi=-k\beta(c)\psi$ with state-dependent $\beta(c)=1-Q'(c)\,c_f/q_f$ (Lemma 2.4, an identity, not an approximation), and un-freezing β recovers Route A's wave exactly (Theorem 5.3). Eqs. 2–8 *do* modify the seed's shape ($\mathcal M[s]\neq s$: e.g. the start-up deficit $1-\mathrm{tent}(kt)$), but only through affine, $\lambda$-independent kernels — they are structurally incapable of manufacturing the missing $\lambda$-dependence (Lemmas 3.4–3.5), so nothing downstream can repair Eq. 1. The three error sources — (i) shape-ansatz mismatch, (ii) $\gamma_q,\beta\approx1$ freeze, (iii) discretisation — are separated and charged individually in §5.3; the "floor is a function of $bc_f$ alone" claim survives **only** for isothermal Langmuir after $k$-normalisation and Corollary-B.1 centering; for Toth it depends on $(\lambda, t_T)$ through $r_A=\bigl[(1+\lambda^{t_T})^{1/t_T}-1\bigr](1+\lambda^{t_T})/\lambda^{t_T}$ (§5.3).

**(c) Route B's machinery still converges under mesh refinement — to its own single-front limit — and that limit neither bounds nor is bounded by the true two-front error.** The failure is a **model-class error, not a discretisation error**: for any single-front output of Route B's class (monotone, exponential upper tail of rate $a$), the sup-norm distance to a two-front solution with plateau height $c_I$ and front separation $T_{sep}$ obeys

$$\sup_t |B - c_{\text{true}}| \;\ge\; (c_f - c_I)\,\tanh\!\bigl(a\,T_{sep}/2\bigr),$$

(Theorem 6.2) — mesh-independent, growing with bed length through $T_{sep}=L\,\bigl|v_{c}^{-1}-v_{th}^{-1}\bigr|$, and saturating at the full plateau deficit ($0.045\,c_f$ for the MM V.5 run). "Convergence" is therefore the wrong question; the right question is the **regime check**: Route B is admissible iff the two-front structure collapses, i.e. iff the thermal excursion is small enough that $b(T)$ is effectively constant *or* the fronts are unresolved, $(c_f-c_I)\tanh(aT_{sep}/2)\le$ tolerance (§6.3). Moreover the single-front prediction centred at $t_{st}$ is **anti-conservative**: it places breakthrough later than the true first front by $\approx(1-c_I/c_f)\,T_{sep}$ (§6.4).

**General principle (§7).** A quadrature-marching scheme built on an assumed shape converges — by ordinary Lax reasoning — to the image of its seed under the continuum operator it actually discretises. It converges to the *true* solution iff the seed is a fixed point of the exact shape-selection operator (for constant-pattern problems: iff the ansatz solves the derived similarity ODE, $N[s]=0$), or the marching operator closes the state-feedback loop that selects the shape (state-dependent coefficients), making the scheme a genuine discretisation of the governing equations. Route B satisfies neither; un-freezing β satisfies the second and is the minimal repair.

---

## 1. Standing assumptions and formalisation

### 1.1 Governing system and the two regimes

Isothermal reduction (parts a–b): on $z\in[0,L]$, $t>0$,

$$\varepsilon c_t + u c_z = \varepsilon D_L c_{zz} - \alpha_b q_t, \qquad q_t = k\,(q^*(c) - q), \tag{G}$$

clean-bed IC ($c=q=0$), step inlet, favorable isotherm; Langmuir sub-case $Q(c) = q_m b c/(1+bc)$, $q_f := Q(c_f)$, $\lambda := bc_f > 0$. Route A takes $D_L=0$. Part (c) restores the gas/solid energy balance and Arrhenius $b(T)$ exactly as printed in the problem statement (= MM A.1–A.16 with errata E3–E4).

### 1.2 Route B, formalised from its own mechanics

From Danilov B.5–B.13 and Eqs. 2–8 as implemented (errata-corrected) in `psi_quadrature_verify.py`, Route B is the composition of:

**(S1) Seed (Eq. 1 / B.9–B.11).** In corrected time $\tau = (t - z/u_f) - t_s$, the driving force is posited as the symmetric two-branch exponential ("tent")
$$\psi(z,t) = \psi_{\mathrm{ref}}\cdot h(\beta k \tau),\qquad h(x) := \tfrac12 e^{-|x|},$$
so the reconstructed front CDF is $B_0(\tau) = \tfrac12 e^{\beta k\tau}$ ($\tau<0$), $1-\tfrac12 e^{-\beta k\tau}$ ($\tau\ge0$). The two branch rates are **equal by construction** (the repo's F3 note: $\gamma_{\text{shape}} = \beta_\psi$ is the symmetry assumption made visible).

**(S2) Linear driving-force law (B.5–B.8).** $\partial_t\psi = -\beta k\psi$ with $\beta$ a *constant*, justified by "$\gamma_q\approx1$, $\beta\approx1$ for a Langmuir-type system in Table 2" — i.e. proved at one operating point, then frozen.

**(S3) Marching quadratures (Eqs. 2–8).** All remaining fields are affine images of the seed: flux $F_j = F_{j-1} - \alpha_b\gamma_q k\,\psi_j\,\Delta z$ (Riemann march in $z$), heat-flux and temperature analogues, loading by $q = q^*_{eq} - \psi$ (B.13). Every kernel appearing (LDF decay $e^{-k\cdot}$, interphase exchange) is causal, exponential, with rates **independent of the isotherm parameter $\lambda$**.

**(S4) Kinematics.** $u_f \to v_{RH}$, $t_s \to t_{st} = L/v_{RH} = \tfrac{\varepsilon L}{u}(1+\Lambda)$, $\Lambda=\alpha_b q_f/(\varepsilon c_f)$ — the term-for-term identity with MM's Corollary B.1/D.4 (repo finding F1), so Route B's centering is *exact by construction* and is never in dispute below.

We write $S_\Delta$ for the discrete scheme with mesh $\Delta=(\Delta t,\Delta z)$, $\mathcal M$ for the continuum operator defined by replacing every Riemann sum in (S3) by its integral, and $s$ for the seed (S1). The object Route B computes is $S_\Delta[s]$; the objects the Claim compares it against are $\varphi$ (Route A) and, in (c), the FV-MOL solution of the full system.

**Remark 1.1 (fairness).** All results below hold for *any* fixed constants $\gamma_q,\beta>0$ in (S2)–(S3), not just $\gamma_q=\beta=1$; "frozen" — not the particular frozen value — is what matters. This forestalls the objection that a luckier constant would evade the theorems.

---

## 2. Route A: exact structure (all derived, nothing assumed)

### 2.1 Wave speed and coherence

**Lemma 2.1.** *Let $(c,q)=(\varphi,\chi)(\eta)$, $\eta=z-vt$, solve (G) with $D_L=0$, connecting $(0,0)$ (ahead, $\eta\to+\infty$) to $(c_f,q_f)$ (behind, $\eta\to-\infty$). Then necessarily $v=v_{RH}= uc_f/[\varepsilon c_f+\alpha_b q_f]$ and $\chi=(q_f/c_f)\varphi$ pointwise.*

*Proof.* Substituting into the mass balance: $(u-\varepsilon v)\varphi' = \alpha_b v\chi'$. Integrate from $+\infty$ using the ahead-state: $(u-\varepsilon v)\varphi = \alpha_b v\chi$. Evaluating at $\eta\to-\infty$ gives $(u-\varepsilon v)c_f = \alpha_b v q_f$, i.e. $v=v_{RH}$; substituting back, $\chi = \tfrac{u-\varepsilon v}{\alpha_b v}\varphi = \tfrac{q_f}{c_f}\varphi$ (using $u/v_{RH}-\varepsilon = \alpha_b q_f/c_f$). $\square$

The speed is thus a Rankine–Hugoniot condition *derived from* the conservation form, and the loading–concentration lock ("coherence") is a consequence, not an input. This is MM (D.6) and disposes of any suspicion that Route A itself assumes a shape.

### 2.2 Shape ODE, existence, uniqueness

**Lemma 2.2.** *With Lemma 2.1, the LDF equation reduces to*
$$\varphi'(\eta) = -\frac{k c_f}{v_{RH} q_f}\,G(\varphi), \qquad G(\varphi) := Q(\varphi)-\tfrac{q_f}{c_f}\varphi, \tag{D.7}$$
*and for strictly concave $Q$ (Langmuir with $\lambda>0$) there is exactly one monotone profile up to translation, with $G>0$ on $(0,c_f)$ and exponential approach to both rest states.*

*Proof.* $q_t=-v\chi' = k(Q(\varphi)-\chi)$ with $\chi=(q_f/c_f)\varphi$ gives (D.7). Strict concavity puts the chord under the curve: $G>0$ on $(0,c_f)$, $G(0)=G(c_f)=0$ with $G'(0)=Q'(0)-q_f/c_f>0$ and $G'(c_f)=Q'(c_f)-q_f/c_f<0$ simple zeros. The scalar autonomous ODE then has a unique (up to shift) heteroclinic $\varphi$ decreasing from $c_f$ to $0$, with linearisation at the ends giving exponential tails. $\square$

### 2.3 Langmuir closed form and the asymmetry invariant

**Lemma 2.3.** *For Langmuir, with $w=\varphi/c_f$:*
$$\ln w - (1+\lambda)\ln(1-w) = -\frac{k\lambda}{v_{RH}}(\eta-\eta_0) \;=\; s, \tag{D.8}$$
*equivalently, at fixed $z$, $s = k\lambda\,(t - t_0(z))$: the outlet curve is $W(s)$ defined implicitly by (D.8). Its tails are*
$$w \sim e^{\,s}\ (s\to-\infty), \qquad 1-w \sim e^{-s/(1+\lambda)}\ (s\to+\infty),$$
*i.e. in clock time the leading-edge and saturation-tail e-folding rates are $k\lambda$ and $k\lambda/(1+\lambda)$; the* **tail-rate ratio** *(a scale- and translation-invariant shape functional) is*
$$r_A(\lambda) \;=\; \frac{\text{leading rate}}{\text{trailing rate}} \;=\; 1+\lambda .$$

*Proof.* $G(\varphi) = q_m b^2\varphi(c_f-\varphi)/[(1+b\varphi)(1+\lambda)]$ by direct algebra; partial fractions $\tfrac{1+b\varphi}{\varphi(c_f-\varphi)} = \tfrac1{c_f\varphi} + \tfrac{1+\lambda}{c_f(c_f-\varphi)}$ integrate (D.7) to (D.8). Tails: as $w\to0$ the LHS $\to\ln w$; as $w\to1$ it $\to -(1+\lambda)\ln(1-w)$. Both statements are verified numerically to $7.5\times10^{-12}$ (ODE vs. implicit) and to 5 significant figures (tail slopes) in `psi_quadrature_proof_checks.py` §4–5. $\square$

**Toth generalisation** (needed for §5.3): for $Q(c)=n_s b c/(1+(bc)^{t_T})^{1/t_T}$ the same computation gives $Q'(0)=n_s b$, $q_f/c_f = n_s b(1+\lambda^{t_T})^{-1/t_T}$, $Q'(c_f) = (q_f/c_f)(1+\lambda^{t_T})^{-1}$, hence

$$r_A(\lambda,t_T) \;=\; \frac{Q'(0)-q_f/c_f}{q_f/c_f-Q'(c_f)} \;=\; \Bigl[(1+\lambda^{t_T})^{1/t_T}-1\Bigr]\,\frac{1+\lambda^{t_T}}{\lambda^{t_T}},$$

reducing to $1+\lambda$ at $t_T=1$. The asymmetry invariant is **isotherm-family-dependent**, not a function of $bc_f$ alone.

### 2.4 The exact driving-force law — where β really comes from

**Lemma 2.4 (β is a state function; the linear ψ-ODE is exact only when β is allowed to vary).** *On the constant-pattern wave, with $\psi := Q(\varphi) - \chi = Q(\varphi)-\tfrac{q_f}{c_f}\varphi = G(\varphi)$,*
$$\frac{\partial\psi}{\partial t}\Big|_z \;=\; -\,k\,\beta(c)\,\psi, \qquad \beta(c) \;=\; 1-\gamma_q(c), \qquad \gamma_q(c) := Q'(c)\,\frac{c_f}{q_f}\ \ (\text{tangent/chord slope ratio}),$$
*identically — no approximation. (This $\gamma_q(c)$ is the tangent/chord ratio; it is not Danilov's Eq.-2 coefficient of the same name — repo finding F3 already flags that the paper conflates three distinct quantities. The paper's "$\beta\approx1$" claim corresponds to $\beta(c)$ here.) For Langmuir, $\beta(c) = 1 - \dfrac{1+\lambda}{(1+\lambda w)^2}$, which sweeps the range*
$$\beta(0^+) = -\lambda \quad(\text{leading edge: } \psi \text{ grows at rate } k\lambda), \qquad \beta(c_f) = \frac{\lambda}{1+\lambda} \quad(\text{saturation tail: decay at rate } \tfrac{k\lambda}{1+\lambda}).$$

*Proof.* $\psi(\eta) = G(\varphi(\eta))$, so $\partial_t\psi = -v\,G'(\varphi)\varphi' = -v\bigl(Q'(\varphi)-\tfrac{q_f}{c_f}\bigr)\varphi'$. Insert (D.7): $\varphi' = -\tfrac{kc_f}{vq_f}\psi$, giving $\partial_t\psi = \tfrac{kc_f}{q_f}\bigl(Q'(\varphi)-\tfrac{q_f}{c_f}\bigr)\psi = -k\bigl(1-Q'(\varphi)c_f/q_f\bigr)\psi$. The Langmuir evaluation is direct; the identity is confirmed numerically to $10^{-10}$ (§4 of the check script). $\square$

**Consequences.** (i) Route B's Appendix-B ODE is the *exact* law with its only sin being the freeze $\beta(c)\to\text{const}$. (ii) The two constants $\beta(c_f)=\lambda/(1+\lambda)$ and $|\beta(0^+)|=\lambda$ are precisely Route A's two tail rates (Lemma 2.3) — **the entire asymmetry of the true wave lives in the state-dependence of β**, and freezing β is exactly the operation that deletes it. (iii) "$\beta\approx1$" holds iff $\lambda\gg1$, and then only on the saturation side: the validation regime of the source paper (strongly favorable Table-2 system) is the unique regime where the freeze is harmless *for the trailing tail* — and simultaneously the regime where the symmetric ansatz is *maximally* wrong on the leading edge (true leading rate $k\lambda\to\infty$: a near-shock; ansatz rate $k$). This single lemma already explains both the paper's successful validation and its non-transferability.

### 2.5 Moment functionals of the exact wave

Let $p(s) = dW/ds$ (the normalised outlet-derivative profile in the stretched variable $s=k\lambda(t-t_0)$). Since $s(w)=\ln w-(1+\lambda)\ln(1-w)$ is a smooth increasing bijection $(0,1)\to\mathbb R$, moments of $p$ are $\mathbb E[s^n] = \int_0^1 s(w)^n\,dw$, absolutely convergent (exponential tails).

**Lemma 2.5.** *With $\zeta(3)=1.2020569\ldots$:*
$$\mathbb E[s] = \lambda,\qquad \operatorname{Var}(s) = \lambda^2 + \frac{\pi^2}{3}(1+\lambda),\qquad \mu_3(s) = 2\lambda^3+6\lambda^2+6\lambda+6(\zeta(3)-1)\lambda(1+\lambda).$$

*Proof.* Uses only four elementary integrals, each by expanding $\ln(1-w)=-\sum_{n\ge1}w^n/n$ and $\int_0^1 w^n(\ln w)^m dw = (-1)^m m!/(n+1)^{m+1}$:
$\int_0^1(\ln w)^m dw=(-1)^m m!$;
$\int_0^1 \ln w\ln(1-w)\,dw = \sum_n \tfrac1{n(n+1)^2} = \sum_n\bigl[\tfrac1n-\tfrac1{n+1}-\tfrac1{(n+1)^2}\bigr] = 2-\tfrac{\pi^2}6$;
$\int_0^1 (\ln w)^2\ln(1-w)\,dw = -2\sum_n\tfrac1{n(n+1)^3} = -2\bigl[1-(\tfrac{\pi^2}6-1)-(\zeta(3)-1)\bigr] = -6+\tfrac{\pi^2}3+2\zeta(3)$,
and by the $w\leftrightarrow1-w$ symmetry of the integrand pattern, $\int_0^1 \ln(1-w)^2\ln w\,dw$ equals the same value. Expanding $s=A-B$, $A=\ln w$, $B=(1+\lambda)\ln(1-w)$, and collecting with $m=1+\lambda$:
$\mathbb E[s]=-1+m=\lambda$; $\mathbb E[s^2]=2+2m^2-m(4-\tfrac{\pi^2}3)$ whence the variance; $\mathbb E[s^3]=6(m^3-1)+3m\lambda J$ with $J=-6+\tfrac{\pi^2}3+2\zeta(3)$, whence $\mu_3=\mathbb E[s^3]-3\lambda\mathbb E[s^2]+2\lambda^3$ collapses to the stated form. All three verified to 6+ digits at $\lambda\in\{0.05,\ldots,20\}$ (check script §1). $\square$

**Corollary 2.6 (skewness).** $\gamma_1(\lambda) = \mu_3/\operatorname{Var}^{3/2}$ satisfies $\gamma_1(0^+)=0$ with slope $6\zeta(3)/(\pi^2/3)^{3/2} = 1.20867\ldots$, $\gamma_1(\infty)=2$, and is strictly increasing (verified on a $4000$-point geometric grid spanning $[10^{-5},10^{5}]$; the limits are analytic: as $\lambda\to\infty$, $\operatorname{Var}\sim\lambda^2$, $\mu_3\sim2\lambda^3$ — the profile converges to a one-sided unit-rate exponential, whose skewness is $2$; as $\lambda\to0$ it converges to the logistic density, skewness $0$). The exact wave is right-skewed for every $\lambda>0$ — consistent with, though not proved by, the $6\times$ RMSE preference for asymmetric families over the symmetric logistic in the five measured runs (context only, per the problem's own ground rules).

### 2.6 Centering (shared by both routes)

MM Corollary B.1 gives, model-free, $\int_0^\infty(1-c(L,t)/c_f)\,dt = t_{st} = L/v_{RH}$ for any $k, D_L$. In $s$-units this fixes the first moment; Lemma 2.5 then locates the exact wave as $s = k\lambda(t-t_{st})+\lambda$. Route B's $t_s$ equals $t_{st}$ identically (S4/F1). **All comparisons below are made at this common, exact centering**, so no part of any floor can be attributed to a centering discrepancy.

---

## 3. Route B as a seeded affine marching scheme

### 3.1 The class of schemes

Route B's computational content, per (S1)–(S3), is: fix the seed $s(\cdot)$; then march finitely many recursions of the form

$$y_{j+1} = a_j\,y_j + \Delta\,\sum_i \omega_i\,K_i(\xi_j)\,\bigl[\text{seed or previously-marched field}\bigr](\xi_j), \qquad |a_j|\le1, \tag{Q}$$

where every kernel $K_i$ is bounded, piecewise-$C^1$, causal, exponentially decaying with a rate from the fixed set $\{k, \text{interphase-exchange rates}\}$ — none depending on $b, q_m, c_f$ — and the weights are Riemann/rectangle weights. Fields enter (Q) only linearly; the isotherm parameters enter only through the scalars $\psi_{\mathrm{ref}}=q_f$, $u_f$, $t_s$ (amplitude, translation).

### 3.2 Stability and consistency — constructed, not cited

**Proposition 3.1 (stability).** *Solutions of (Q) satisfy $\|y\|_{\ell^\infty} \le |y_0| + T\max_i\|K_i\|_\infty\|\text{seed}\|_\infty\cdot C$ with $C$ independent of $\Delta$: by $|a_j|\le1$ and induction, each step adds at most $\Delta\cdot\text{(bounded)}$, and there are $T/\Delta$ steps. Composing finitely many marches multiplies constants but keeps them mesh-uniform.* $\square$

**Proposition 3.2 (consistency with $\mathcal M$, order 1).** *For each march, the continuum object replaces the sum in (Q) by $\int K_i\cdot(\text{seed})$. The integrand is bounded, $C^1$ except at the single stitch point $\tau=0$ of the seed (where it is Lipschitz), so the composite rectangle rule has error $O(\Delta)$, uniformly on compact time windows: $\|S_\Delta[s]-\mathcal M[s]\|_\infty = O(\Delta t+\Delta z)$.* 

*Proof.* Standard rectangle-rule bound $\sum_j\int_{I_j}|f(\xi)-f(\xi_j)|d\xi \le \Delta\cdot TV(f) + O(\Delta)$ per kink, applied per march; stability (Prop. 3.1) propagates per-march errors additively. Verified numerically: the Eq.-2-type flux march converges to its continuum limit with sup-differences $0.185,\,0.043,\,0.010,\,0.0026$ under successive $4\times$ refinements — clean first order (check script §8). $\square$

**Theorem 3.3 (Route B converges — to its own limit).** $S_\Delta[s] \to \mathcal M[s]$ in $\ell^\infty$ as $\Delta\to0$, at rate $O(\Delta)$. *Proof: Props. 3.1–3.2 and the Lax–Richtmyer argument for the pair $(S_\Delta,\mathcal M)$ — which is legitimate here precisely because both members of the pair are affine in the seed.* $\square$

This settles the *existence* half of (b): the discrete profile converges, and the limit is $\mathcal M[s]$ — the affine image of the ansatz. Note $\mathcal M[s]\ne s$ in general: e.g. the flux march produces the start-up deficit $1-\mathrm{tent}(kt)$ near $t\lesssim3/k$ (the seed pretends half the front mass is already in the bed at $t=0$; repo erratum E1's "inlet fold-back"; measured as $0.5026\approx\tfrac12$ at $t=0$ in check §8). So Eqs. 2–8 *can* reshape the seed. What they cannot do is the subject of the next two lemmas.

### 3.3 The two structural invariants of the marching operator

**Lemma 3.4 (shape universality).** *In the variable $\sigma = k\,(t - z/u_f - t_s)$, every recursion (Q) has coefficients independent of $(\lambda, q_m, c_f, L, u)$ — the isotherm and operating parameters enter only as amplitude prefactors and through the definition of $\sigma$ itself. Hence the converged outlet curve is*
$$\mathcal M[s](t) = \Phi\bigl(k\,(t-t_{st})\bigr)$$
*for a single fixed function $\Phi$ (determined once by the seed branches and the kernel set), the same for every $\lambda$. In particular every scale-invariant shape functional of Route B's converged output — skewness, tail-rate ratio, any quantile ratio — is a constant, independent of $\lambda$.*

*Proof.* Nondimensionalise (Q) by $\sigma$: the seed is $h(\beta\sigma)$ with $\beta$ frozen; the kernels are $e^{-\kappa\sigma}$-type with $\kappa/k$ fixed numbers; the weights rescale into $\Delta\sigma$. Nothing $\lambda$-dependent remains except multiplicative amplitudes ($q_f$, $u c_f$), which cancel in $c/c_f$, and translations, which are fixed to $t_{st}$ by (S4). $\square$

**Lemma 3.5 (tail-rate transparency).** *Let $g$ be bounded with $g(\tau)\sim Ce^{a\tau}$ as $\tau\to-\infty$ and $1-g(\tau)\sim C'e^{-a'\tau}$ as $\tau\to+\infty$, and let $K(\upsilon)=\kappa e^{-\kappa \upsilon}\mathbf 1_{\upsilon>0}$ be a causal exponential kernel with $\kappa>0$. Then $J = K*g$ satisfies: leading rate of $J$ is exactly $a$ (with constant $C\kappa/(\kappa+a)$); trailing rate of $J$ is $\min(a',\kappa)$ (equal rates producing at worst a factor $\tau e^{-\kappa\tau}$). By induction the same holds for finitely many convolutions. Consequently, since Route B's seed has equal branch rates $\beta k$ and its kernel alphabet $\{\kappa_i\}$ is $\lambda$-free, the tail-rate ratio of Route B's converged output is*
$$r_B \;=\; \frac{\beta k}{\min(\beta k,\ \kappa_{\min})} \;=\; \text{a fixed constant independent of }\lambda,\qquad r_B = 1\ \text{ when } \beta k \le \kappa_{\min}\ (\text{the case here: }\beta\le1,\ \kappa_{\min}=k),$$
*whereas Lemma 2.3 requires $r_A = 1+\lambda$.*

*Proof.* $\int_0^\infty \kappa e^{-\kappa \upsilon}Ce^{a(\tau-\upsilon)}d\upsilon = Ce^{a\tau}\tfrac{\kappa}{\kappa+a}$ (finite since $\kappa+a>0$); for the trailing side apply the same computation to $1-g$ and note $K*1=1$; the slower of the two exponentials wins. $\square$

Lemmas 3.4–3.5 are the precise sense in which Eqs. 2–8 are **shape-transparent**: affine, translation-covariant machinery with a $\lambda$-free kernel alphabet can translate, rescale in amplitude, smooth, and even skew the seed by a *fixed* amount — but it cannot make any shape functional of the output depend on $\lambda$. The missing information ($r=1+\lambda$) is a nonlinear functional of the isotherm; no amount of linear bookkeeping downstream of a $\lambda$-blind seed can synthesise it.

---

## 4. Part (a): the shared limit — proof for Route A, disproof (and salvage) for Route B

### 4.1 Route A → logistic: the clean argument

**Theorem 4.1.** *Let $W_\lambda(\sigma)$ be the outlet curve of Lemma 2.3 in the stretched, Corollary-B.1-centred variable $\sigma = k\lambda(t-t_{st})$ (so the implicit relation is $\ln w-(1+\lambda)\ln(1-w) = \sigma+\lambda$). Then*
$$\sup_{\sigma\in\mathbb R}\ \Bigl|W_\lambda(\sigma) - \frac{1}{1+e^{-\sigma}}\Bigr| \;\longrightarrow\; 0 \qquad (\lambda\to0).$$

*Proof.* Write $F_\lambda(w) = \ln w-(1+\lambda)\ln(1-w)-\lambda$ and $F_0(w)=\ln\tfrac{w}{1-w}$, both strictly increasing bijections $(0,1)\to\mathbb R$. For fixed $\sigma$, $|F_\lambda(w)-F_0(w)| = |\lambda||\ln(1-w)+1|$. On any compact $\sigma$-interval $[-M,M]$ the solutions stay in $[\delta,1-\delta]$ with $\delta=\delta(M)>0$ uniformly for $\lambda\le1$ (because $F_\lambda\ge F_0-\lambda(1+|\ln(1-w)|)$ and both ends diverge), so $|\ln(1-w)+1|\le C(M)$ and the inverse-function estimate $|W_\lambda-W_0| \le \lambda C(M)/\min F_0' \to0$ uniformly on $[-M,M]$. Tails: for $\sigma\ge M$ and $\lambda\le1$: $\ln w\le0$ forces $-(1+\lambda)\ln(1-w)\ge\sigma+\lambda$, so $1-W_\lambda \le e^{-\sigma/2}\le e^{-M/2}$, and $1-W_0\le e^{-M}$; for $\sigma\le-M$ both functions are $\le e^{-M+1}$. Choose $M$ large then $\lambda$ small: uniform convergence on $\mathbb R$. $\square$

*(Equivalently: the asymmetry ratio $1+\lambda\to1$ and (D.8) collapses to $\ln\tfrac w{1-w}=\sigma$; MM D.4 recovers the Yoon–Nelson/Thomas logistic with $k_{YN}=k\lambda$ and $\tau=t_{st}$, which is exactly the limit curve in the Claim.)*

### 4.2 Route B, literal reading (β = 1 frozen): disproof

**Theorem 4.2.** *With $\beta=1$, Route B's converged outlet curve is $\Phi(k(t-t_{st}))$ (Lemma 3.4). In the stretched variable $\sigma=k\lambda(t-t_{st})$ this is $\Phi(\sigma/\lambda)$, which converges pointwise (as $\lambda\to0$) to the step function $\mathbf 1_{\sigma>0}$ (value $\Phi(0)$ at $0$). Hence*
$$\liminf_{\lambda\to0}\ \sup_\sigma\Bigl|\Phi(\sigma/\lambda) - \tfrac1{1+e^{-\sigma}}\Bigr| \;\ge\; \tfrac12\quad\text{(witnessed along }\sigma_\lambda=\sqrt\lambda\text{)},$$
*in particular the distance does not vanish — Route B does not converge to the logistic (nor to anything $\lambda$-dependent). Part (a) as stated is false.*

*Proof.* $\Phi$ is a fixed non-degenerate CDF-shape with width $O(1)$ in its own argument; $\Phi(\sigma/\lambda)$ has width $O(\lambda)$ in $\sigma$. Take $\sigma_\lambda = \sqrt\lambda\to0$: $\Phi(\sigma_\lambda/\lambda)\to1$ while the logistic $\to\tfrac12$. $\square$

The mechanism is Lemma 2.4: the true front rate in this regime is $k\lambda$ (both tails), but the frozen ODE keeps decaying at $\beta k = k$. The "shared limit" fails not because symmetry fails (it doesn't, here) but because the *rate* was frozen at the wrong operating point. Numerically the moment-centred sup-distance grows as $\lambda\downarrow$: $0.149\,(\lambda=2.045)$, $0.199\,(1)$, $0.269\,(0.5)$, $0.411\,(0.1)$ (check §6), and the variance ratio diverges as $\tfrac{\pi^2}{6\lambda^2}$ (check §7).

### 4.3 Route B, charitable reading (β re-derived at the Henry point): the exact salvage

If instead one re-runs Route B's own Appendix-B evaluation at the operating point in question — which by Lemma 2.4 gives $\beta = \beta(c_f)=\lambda/(1+\lambda)$ (and $|\beta(0^+)|=\lambda$, which agree to $O(\lambda^2)$ as $\lambda\to0$, so the symmetric ansatz's single rate is asymptotically well-defined) — then in stretched $\sigma$ the tent has unit rate and:

**Theorem 4.3.** *With $\beta=\lambda/(1+\lambda)$ (raw-seed reading $\Phi=B_0$), Route B's curve and Route A's curve agree, as $\lambda\to0$: exactly in centering and first moment; to $O(\lambda)$ in both tail exponents; and both are symmetric in the limit. Nevertheless*
$$\lim_{\lambda\to0}\ \sup_\sigma\bigl|W_\lambda - B_0\bigr| \;=\; \sup_\sigma\Bigl|\tfrac1{1+e^{-\sigma}} - \operatorname{tent}(\sigma)\Bigr| \;=\; \tfrac32-\sqrt2 \;=\;0.0857864\ldots,$$
*attained at $\sigma^\ast = \mp\ln(\sqrt2-1)$: the stitched double exponential is not a logistic, and stretching cannot reconcile fixed distinct shapes.*

*Proof.* The sup is invariant under the common stretch $\sigma\mapsto\sigma/(k\lambda)$. For $\sigma>0$ set $g=e^{-\sigma}$: $f(\sigma) = (1-\tfrac12 g) - \tfrac1{1+g}$; $f'=0 \iff (1+g)^2=2 \iff g=\sqrt2-1$, giving $f = \tfrac32-\sqrt2$ (max by endpoint checks $f(0)=f(\infty)=0$); the $\sigma<0$ side is its mirror. Combined with Theorem 4.1 and a triangle inequality in the uniform limit. Numerics: $0.08578644$ on both sides (check §3); the moment-centred floors at small $\lambda$ approach it from below: $0.0818$ at $\lambda=0.1$ (check §6). $\square$

**Resolution of (a).** Proved for Route A. For Route B: false under the Claim's own parameter assignment; true only in the weak sense (centering, first moment, tail exponents, symmetry) under the charitable β — with a permanent, universal $8.6\%$-of-$c_f$ sup-norm residual whose origin is the *functional form* of Eq. 1, not its symmetry. The "sanity check" thus already exhibits, in miniature, both of the independent defects that part (b) must keep separated: the β-freeze (a rate error, dominant as $\lambda\to0$ under the literal reading) and the shape ansatz (a form error, surviving every reading).

---

## 5. Part (b): mesh refinement at $\lambda = O(1)$ — convergence target, error floor, and where the shape dies

### 5.1 What the scheme converges to

**Theorem 5.1.** *For every $\lambda>0$ and every fixed $(\gamma_q,\beta)$, $S_\Delta[s]\to\mathcal M[s]$ at rate $O(\Delta t+\Delta z)$ (Theorem 3.3) — its own continuum ansatz limit (more precisely: the affine image of the ansatz, which differs from the raw ansatz by $\lambda$-independent modifications such as the start-up deficit). It does not converge to Route A's $\varphi$: by Lemma 3.4 all its scale-invariant shape functionals are $\lambda$-free constants, while Route A's tail-rate ratio is $1+\lambda$ (Lemma 2.3) and skewness is $\gamma_1(\lambda)>0$ (Cor. 2.6). Hence for $\lambda>0$ the answer to (b)'s trichotomy is: **its own ansatz limit** — and "neither" is also wrong, because Theorem 3.3 is constructive.*

Numerical exhibit (check §8, $\lambda=2.045$, matching `mechanistic_verify.test3_wave`): the flux-quadrature march converges to its continuum limit at first order ($0.185\to0.0026$ over three $4\times$ refinements), the converged march sits $0.1501$ from the FV-MOL truth, the continuum tent sits $0.1488$ from it, and the FV-MOL truth sits $0.0061$ from the exact (D.8) wave. Discretisation error $\to0$; model error $\to$ floor; the floor equals the §6-table prediction $0.14918$ to three digits.

### 5.2 The error floor as an explicit function of $bc_f$

Fix the exact common centering (§2.6) and normalise time by $k$. Then:

**Theorem 5.2 (floor).** *For every $\lambda>0$ the converged Route B output differs from Route A's exact profile by at least*

- *the asymmetry-invariant gap $\;r_A-r_B = (1+\lambda)-1 = \lambda = bc_f$ — exactly the problem's nonlinearity parameter;*
- *the skewness gap $\gamma_1(\lambda) - 0$, with $\gamma_1(\lambda)\sim 1.2087\,\lambda$ as $\lambda\to0$, strictly increasing to $2$ as $\lambda\to\infty$;*
- *in sup norm (moment-centred, computed): $0.411, 0.269, 0.199, 0.149, 0.132, 0.138$ at $\lambda = 0.1, 0.5, 1, 2.045, 5, 20$ for frozen $\beta=1$; $0.082, 0.077, 0.081, 0.094, 0.114, 0.147$ for state-corrected $\beta=\lambda/(1+\lambda)$; allowing even a free time shift (abandoning Cor. B.1) leaves $0.404,\ldots,0.091\,(\lambda=2.045),\ldots$ — the floor is not a centering artefact;*
- *in variance: $\operatorname{Var}_A/\operatorname{Var}_B = [\lambda^2+\tfrac{\pi^2}3(1+\lambda)]/(2\lambda^2) \to\infty$ ($\lambda\to0$, frozen β) and $\to\tfrac12$ ($\lambda\to\infty$, any β): even where the β-freeze becomes exact for the trailing tail, the symmetric branch double-counts front mass and the variance floor is a factor 2.*

*Limits: every entry $\to0$ as $bc_f\to0$ in the weak metrics (consistent with the corrected part (a)); the sup-norm floor does not (Theorem 4.3): $3/2-\sqrt2$ survives. Growth: monotone in $\lambda$ in the invariant and skewness metrics, saturating at (ratio gap $=\lambda\to\infty$, skewness gap $\to2$, variance factor $2$).*

*Proof.* First two items: Lemmas 2.3, 3.4, 3.5, Cor. 2.6. Variance: Lemma 2.5 vs. the Laplace density variance $2/(\beta k)^2$. Sup-norm rows: rigorous existence of a positive floor follows from the invariant gap (two CDFs with distinct tail-rate ratios cannot coincide); the numerical values are evaluations, not estimates, of $\|W_\lambda-\Phi(k\cdot)\|_\infty$ (check §6). A closed-form sup-norm lower bound valid at all $\lambda$: at the common first-moment centre, $B(t_{st})=\tfrac12$ exactly (symmetry) while $W_\lambda$ at its mean solves $s(w)=\lambda$, which is $>\tfrac12$ for all $\lambda>0$ (since $s(\tfrac12)=\lambda\ln2<\lambda$ and $s$ is increasing in $w$) and $\to1-e^{-1}$ as $\lambda\to\infty$; hence floor $\ge W_\lambda(\text{mean})-\tfrac12 \to 0.1321$. $\square$

### 5.3 Charging the three error sources separately

Decompose Route B's total error against Route A at mesh $\Delta$:

$$\underbrace{\|S_\Delta[s]-\mathcal M[s]\|}_{\text{(iii) discretisation}} \;+\; \underbrace{\|\mathcal M[s_{\beta=1}]-\mathcal M[s_{\beta=\beta(c_f)}]\|}_{\text{(ii) }\gamma_q,\beta\text{-freeze}} \;+\; \underbrace{\|\mathcal M[s_{\beta=\beta(c_f)}]-W_\lambda\|}_{\text{(i) shape ansatz}}.$$

- **(iii)** is $O(\Delta)$ and vanishes: Theorem 3.3. It is the only term mesh refinement touches.
- **(ii)** is a pure *rate/scale* error: both curves in this difference are the same universal shape at rates $k$ vs. $k\lambda/(1+\lambda)$; it is a function of $\lambda$ *and of the operating point at which the source paper froze β* — for the Table-2 validation point ($\lambda\gg1$) it is small on the trailing side, which is precisely why the paper's evaluation "proved" $\beta\approx1$ *there*. It dominates the floor as $\lambda\to0$ (Theorem 4.2's failure lives entirely in this term).
- **(i)** is the irreducible model-class error: a symmetric universal shape vs. a $\lambda$-skewed family; bounded below by the invariant gap $\lambda$ and the skewness gap $\gamma_1(\lambda)$, and above zero for every $\lambda>0$; equal to $3/2-\sqrt2$ in sup norm in the $\lambda\to0$ limit; never touched by mesh or by re-tuning constants (Remark 1.1).

Hence the precise status of the Claim's "floor is a function of $bc_f$ alone": **true for (i)** in the isothermal Langmuir setting after $k$-normalisation and Cor.-B.1 centering (the whole Route-A family is $\lambda$-parametrised, Lemma 2.3, and Route B's class is parameter-free, Lemma 3.4); **false if (ii) is silently included** (that term depends on where β was frozen); **false beyond Langmuir** — for Toth the invariant is $r_A(\lambda,t_T)$ of §2.3, a function of two parameters. Conflating (i) and (ii) is exactly how one would erroneously conclude that validating Route B at one strongly-favorable point certifies it generally.

### 5.4 Where the wrong shape is baked in — and the minimal repair

**Theorem 5.3 (locus of the defect; repair).** *(1) The marching stage (Eqs. 2–8) is not the locus: it modifies shapes ($\mathcal M[s]\ne s$) but only $\lambda$-independently (Lemmas 3.4–3.5); it can neither create nor destroy the $\lambda$-dependence a correct front requires; so no later stage can correct Eq. 1 "in principle" — the required information is absent from the operator's alphabet, not merely unexploited. (2) The seed's symmetry (Eq. 1) is a symptom, not the root: an asymmetric seed with any fixed rates would fail identically for all but one $\lambda$ (Lemma 3.4 applies verbatim). (3) The root is the freeze in (S2): by Lemma 2.4 the exact law is $\partial_t\psi = -k\beta(c)\psi$; replacing frozen β by $\beta(c)$ evaluated on the marched state closes the state-feedback loop, and then the scheme's continuum limit is exactly (D.7): with coherence (Lemma 2.1, supplied by Route B's own $q=q^*-\psi$ bookkeeping plus mass balance), $\partial_t\psi=-k\beta(c)\psi$ integrates to $\ln w-(1+\lambda)\ln(1-w) = -\tfrac{k\lambda}{v_{RH}}(\eta-\eta_0)$, i.e. Route A's (D.8). A one-step marching discretisation of this now-nonlinear law has Lipschitz right-hand side on $[0,c_f]$ ($|\beta(c)|\le\max(\lambda,1)$), hence LTE $O(\Delta)$ + discrete-Grönwall stability $\Rightarrow$ convergence to the true wave. The repaired scheme is Route A in marching clothes — which is the sharpest possible statement of what was lost.*

*Proof.* (1)–(2) are Lemmas 3.4–3.5. (3): the integration is Lemma 2.3's computation run backwards (Lemma 2.4 established the identity of the two ODEs); the convergence statement is the standard explicit-one-step argument, constructed here rather than cited since the rhs is now state-dependent: $|\psi_{n+1}-\psi(t_{n+1})| \le (1+Ck\Delta)|\psi_n-\psi(t_n)| + C'\Delta^2$, iterate. $\square$

### 5.5 The Chapman–Enskog contrast, and commuting limits

The relaxation expansion (MM D.5) corrects a *derived* leading term: $q = Q(c) - k^{-1}\partial_tQ + O(k^{-2})$ yields $D_{\mathrm{kin}}\propto v_{\mathrm{eff}}^2/k$, a systematic error series in the small parameter, each term computable, the zeroth term already exact in the limit. Route B's small parameter — properly $\epsilon_1 := 1-\beta(c_f) = 1/(1+\lambda)$ (the tangent/chord ratio $\gamma_q(c_f)$ of Lemma 2.4), i.e. exactly the quantity Appendix B certifies as small when it declares $\beta\approx1$ at the validation point — does **not** admit an analogous expansion: as $\epsilon_1\to0$ the true profile converges to the one-sided exponential (skewness 2), while the ansatz remains the symmetric tent (skewness 0). The mismatch is $O(1)$ *at zeroth order in $\epsilon_1$*: there is no series to build because the ansatz is not the $\epsilon_1^0$ term of anything true. $\epsilon_1$ is small only in the ODE coefficient's trailing value, not in solution-space distance — the leading branch of the tent is pure invention at every $\epsilon_1$. And the two limits commute trivially but uselessly: $\lim_{\Delta\to0}\lim_{\epsilon_1\to0} = \lim_{\epsilon_1\to0}\lim_{\Delta\to0} = $ the universal tent-image — commutation without consistency. This answers the problem's relaxation-expansion query: the existence of a C–E-type correctable structure depends on the leading term being *derived*; Route B's is assumed, and assumption is not a small parameter.

---

## 6. Part (c): non-isothermal coupling — the two-front obstruction

### 6.1 Two speeds, hence (generically) two fronts

**Lemma 6.1.** *Adiabatic ($h_w=0$), local-equilibrium, dispersion-free reduction of the full system: with $U=(c,T)$, $a:=q^*_c>0$, $d:=q^*_T<0$,*
$$A(U)\,U_t + B\,U_z = 0,\qquad A=\begin{pmatrix}\varepsilon+\alpha_b a & \alpha_b d\\ \alpha_b\Delta H\,a & C_h+\alpha_b\Delta H\,d\end{pmatrix},\ B=\operatorname{diag}(u,\ u\rho_g c_{p,g}),$$
*(writing $\Delta H<0$ with the convention $(-\Delta H)>0$). $\det(B-vA)=0$ is a quadratic in $v$ with two real roots; at $\Delta H\to0$ or $d\to0$ they decouple to the concentration speed $u/(\varepsilon+\alpha_b a)$ and the thermal speed $v_{th}=u\rho_gc_{p,g}/C_h = \gamma_h u$. For the MM V.5 parameters $v_{th}\sim0.2$–$0.5\,v_{RH}$: the speeds are well separated, and the clean-bed/step-feed Riemann problem resolves into two waves separated by an intermediate plateau state $(c_I,T_I)$ — the structure the FV solver documents ($c_I/c_f\approx0.955$, $T_I-T_{amb}=+18.9\,$K, persisting under mesh refinement, MM V.5), so the two-front structure is the true solution's, not an artefact.*

*Proof sketch (all that is needed).* Hyperbolicity: the discriminant of the quadratic is a sum of a square and a term proportional to $-a\,d\,(-\Delta H)\ge0$, so roots are real and distinct unless the coupling vanishes. Two characteristic families ⇒ the self-similar Riemann solution is two waves + constant intermediate state (each wave a shock/kinetic front by the favorable-isotherm argument of Lemma 2.2 applied family-wise). We do not need the plateau's closed form — only its existence and persistence, which the problem grants as numerical ground truth. $\square$

### 6.2 Route B still converges — and the limit is bounded away from the truth

**Theorem 6.2.** *(1) With Arrhenius $b(T)$ Lipschitz on the relevant temperature interval, Route B's marching quadratures remain stable and first-order consistent with their continuum operator (the proofs of Props. 3.1–3.2 go through with the state-dependent coefficients frozen along the previously-marched fields, adding a discrete-Grönwall factor $e^{CT}$); hence $S_\Delta[s]\to\mathcal M[s]$ still holds. (2) The limit is a single-front object of the universal class (Lemma 3.4 applies: one corrected-time coordinate, one stitch). (3) For any member $B$ of that class — monotone, with exponential upper tail of rate $a$ ($1-B(t)\le(1-B(t_1))e^{-a(t-t_1)}$ for $t\ge t_1$ once $B(t_1)\ge\tfrac12$) — and any true outlet curve with plateau: $c_{\text{true}}=c_I$ on $[t_1,t_2]$, $T_{sep}:=t_2-t_1$, rising to $c_f$ after $t_2$:*
$$\delta \;:=\; \sup_t|B-c_{\text{true}}| \;\ge\; (c_f-c_I)\,\tanh\!\Bigl(\frac{a\,T_{sep}}{2}\Bigr).$$

*Proof of (3).* Let $g:=c_f-c_I$. From $\delta\ge|B(t_1)-c_I|$: $1-B(t_1)/c_f\cdot c_f \le g+\delta$. The tail property then forces $1-B(t_2) \le (g+\delta)e^{-aT_{sep}}$, so $B(t_2) \ge c_f-(g+\delta)e^{-aT_{sep}}$, while $c_{\text{true}}(t_2^-)=c_I$: $\delta \ge B(t_2)-c_I \ge g-(g+\delta)e^{-aT_{sep}}$. Rearranged: $\delta\ge g\,\frac{1-e^{-aT_{sep}}}{1+e^{-aT_{sep}}} = g\tanh(aT_{sep}/2)$. $\square$

*Numerical exhibit (check §9): against a synthetic two-front curve with $c_I=0.955$, the best single tent over* both *shift and rate achieves sup errors $0.022, 0.043, 0.0450, 0.0450, 0.0450$ at $T_{sep}=0.5,2,5,10,30$ — saturating exactly at $g=0.045$, as the bound predicts.*

**Consequences.** (i) Mesh refinement reduces $\|S_\Delta[s]-\mathcal M[s]\|\to0$ and is *powerless* against $\|\mathcal M[s]-c_{\text{true}}\|\ge g\tanh(aT_{sep}/2)$: this is a **model-class error**. A single-front ansatz cannot converge to a two-front solution under refinement *by construction* — the deficient object is the function class, not the mesh. (ii) The limit **neither bounds nor is bounded by** the true error in any useful direction: $\mathcal M[s]$ can be made arbitrarily far from truth (grow $L$, hence $T_{sep}\propto L|v_c^{-1}-v_{th}^{-1}|$) while all its internal consistency checks (mass bookkeeping, first moment) remain exact — exactness of the quadrature bookkeeping is no evidence of fidelity, because the bookkeeping is exact *about the ansatz*.

### 6.3 The right question: a regime check, not a convergence rate

By Theorem 6.2 the honest admissibility criterion for Route B in the non-isothermal regime is

$$(c_f-c_I)\,\tanh\!\Bigl(\tfrac{a}{2}\,L\,\bigl|v_c^{-1}-v_{th}^{-1}\bigr|\Bigr) \;\le\; \text{tolerance},$$

satisfiable in exactly two ways: **(R1) thermal collapse** — $c_f-c_I\to0$, i.e. the plateau disappears: strong wall coupling ($h_w$ large: the bench 8.5 mm column, MM V.5's +4.9 K wall-coupled run), or small adiabatic temperature rise, or weak Arrhenius sensitivity — in the problem's own grouping, $\Phi\cdot\delta_1\ll1$ with $\delta_1 = |\partial\ln b/\partial T|\,\Delta T_{ad}$; **(R2) unresolved fronts** — $a\,T_{sep}\ll1$: short beds or slow kinetics, where the two fronts overlap inside one MTZ width and a single-front description is not yet wrong. A front-speed-ratio check alone ($v_{th}/v_{RH}$) is necessary but not sufficient — it controls $T_{sep}$'s growth rate but not the plateau height; both factors appear in the bound, and both are computable a priori from the isotherm, $\Delta H$, and the heat balances. This is the promised answer: Route B's applicability is bounded by a **regime check with an explicit, closed-form violation penalty**, not by any convergence rate; asking for its "order of convergence" in the two-front regime is a category error.

### 6.4 Engineering direction of the failure

For the idealised two-front curve, Cor. B.1-type mass accounting gives $t_{\text{front1}} = t_{st} - (1-c_I/c_f)\,T_{sep}$ (the plateau contributes $(1-c_I/c_f)T_{sep}$ to the first moment). Route B, centring its single front at $t_{st}$, therefore predicts breakthrough **later** than the true first front by $\approx(1-c_I/c_f)\,T_{sep} - O(1/a)$, growing linearly in $L$: the error is anti-conservative (real CO₂ slip precedes the prediction) — the dangerous direction for design, and a further reason the regime check must gate any use of Route B, since no internal diagnostic of the scheme detects it.

---

## 7. The general principle: consistency is relative to the equation you discretise

**Theorem 7.1 (Ansatz-Consistency principle for seeded marching schemes).** *Let $S_\Delta = D_\Delta\circ\sigma$ where $\sigma$ injects a fixed seed $s$ and $D_\Delta$ is a uniformly stable, consistent discretisation of a continuum operator $\mathcal M$ (affine or Lipschitz). Then:*

1. *(Lax transfers — to the wrong pair.) $S_\Delta[s]\to\mathcal M[s]$ always. Stability + consistency guarantee convergence to the solution of the problem actually discretised — which is "apply $\mathcal M$ to $s$", not the governing PDE.*
2. *(Criterion.) $\lim S_\Delta[s] = c_{\text{true}}$ iff $\mathcal M[s]=c_{\text{true}}$, i.e. iff the seed is a fixed point of the exact shape-selection problem. For constant-pattern transport this is: $s$ solves the derived similarity ODE ($N[s]:=s'+\tfrac{kc_f}{v_{RH}q_f}G(s)=0$, Lemma 2.2). The property of the ansatz that the principle depends on is membership in the invariant set of the exact evolution — not accuracy, smoothness, symmetry, or any metric proximity.*
3. *(Self-correction criterion.) A marching operator can repair a wrong seed only if the seed's error re-enters the operator's coefficients — i.e. the scheme discretises a nonlinear fixed-point map whose attractor is the true profile (state feedback), rather than an affine map with seed-independent kernels. Route B's Eqs. 2–8 are affine with $\lambda$-free kernels (Lemmas 3.4–3.5): no repair channel exists. Un-freezing $\beta\to\beta(c)$ creates the channel and Theorem 5.3 shows the repaired fixed point is Route A's wave.*

*Proof.* (1) is Theorem 3.3's argument in the abstract; (2) is definitional given (1) plus uniqueness of the constant-pattern profile (Lemma 2.2); (3): if the kernels are seed-independent, $\mathcal M$ is a fixed affine map and its output's shape functionals are determined by $s$ and the kernel alphabet alone (Lemma 3.4's argument) — independent of the governing equations' parameters; conversely with state feedback the scheme is a *bona fide* discretisation of the governing ODE/PDE and inherits classical convergence (Theorem 5.3's Grönwall construction). $\square$

**Why generic finite-difference consistency theorems do not transfer** (the gap the problem demands be closed explicitly): those theorems certify $\|S_\Delta[\cdot] - \mathcal M[\cdot]\|\to0$ — a statement about the *pair* $(S_\Delta,\mathcal M)$. Route B's literature-facing claim silently swaps the second member of the pair, from $\mathcal M[s]$ to the PDE solution. The swap is invisible in any refinement study (refinement studies test only the pair), invisible at the validation operating point (where $\|\mathcal M[s]-c_{\text{true}}\|$ happened to be small because $\lambda\gg1$ makes the trailing tail exact, §2.4, and integral metrics forgive the leading edge), and detectable only by an invariant that the affine machinery cannot move — which is what Lemmas 3.4–3.5 supply and what the measured runs' right-skew corroborates qualitatively. Lax equivalence is not wrong here; it is answering a different question than the one Route B's users ask of it.

---

## 8. Numerical verification appendix

All numbers cited above are produced by `src/solver/psi_quadrature_proof_checks.py` (pure numpy/scipy, no fitted parameters, run time ≈ 40 s). Summary of checks and outcomes:

| # | claim verified | result |
|---|---|---|
| 1 | Lemma 2.5 moment formulas ($\pi^2$, $\zeta(3)$ constants), 6 values of $\lambda$ | agree to all printed digits |
| 2 | Cor. 2.6: slope $6\zeta(3)/(\pi^2/3)^{3/2}=1.208672$; $\gamma_1$ strictly increasing $0\to2$ | exact match; monotone on $[10^{-5},10^5]$ |
| 3 | Theorem 4.3 constant | $0.08578644 = 3/2-\sqrt2$ to $10^{-8}$ |
| 4 | (D.7)↔(D.8) equivalence; Lemma 2.4 β-identity; $\beta(c_f)=\lambda/(1+\lambda)$, $\beta(0^+)=-\lambda$ | $7.5\times10^{-12}$; $10^{-10}$; exact |
| 5 | Lemma 2.3 tail rates and ratio $1+\lambda$ | 5 significant figures |
| 6 | Theorem 5.2 sup-norm floor table (frozen / corrected / free-shift) | as tabulated in §5.2 |
| 7 | variance-ratio limits $\pi^2/(6\lambda^2)$-divergence and $\tfrac12$-saturation | as tabulated |
| 8 | Theorem 5.1 three-way split: march $\to$ own limit $O(\Delta z)$ ($0.185\to0.0026$); model floor $0.1488$–$0.1501$ vs. predicted $0.14918$; FV-MOL vs. (D.8) $0.0061$; start-up deficit $0.5026\approx\tfrac12$ | all confirmed |
| 9 | Theorem 6.2 plateau bound; best single front saturates at $c_f-c_I$ | $0.0450$ at $T_{sep}\ge5$, bound never violated |

## 9. Scope notes

(i) Route A's closed forms are exact only for $D_L=0$, isothermal, constant-pattern; part (b)'s comparison is therefore between Route B and the exact solution *of the regime Route B itself targets* — the fairest possible arena, and the floors can only grow when $D_L>0$ pre-smearing is added to the truth but not the invariants. (ii) The measured five-run right-skew (fractal/asymmetric families beating the logistic $\sim6\times$ in RMSE) is corroboration of Lemma 2.3's prediction in sign and regime, and is used nowhere as evidence in any proof, per the problem's ground rules. (iii) The Toth caveat of §5.3 means any future error-floor table for the SUTD/Stampi-Bombelli parameter set must be indexed by $(\lambda, t_T)$, not $bc_f$ alone. (iv) Nothing in this document modifies solver code or gate definitions; the repaired scheme of Theorem 5.3 is a two-line change to `psi_quadrature_verify.py` (pass $\beta_\psi$ as the state function of Lemma 2.4) if a constructive demonstration is ever wanted for the report's Discussion section.

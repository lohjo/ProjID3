# LITERATURE REVIEW — Section Design & Third-Pass Analysis

**Companion to** `interim_report_design_file.md` · **Report section** §3 (Literature Review)

| | |
|---|---|
| Purpose | Design report §3, and record a Keshav third-pass re-implementation of the central review paper |
| Source of truth | `lit_survey_summaries.md` (SURVEY) for the model-critique strand |
| Centre-of-gravity paper | Hu, Q. et al. (2024), *J. Water Process Eng.* 59:105065 — "A critical review of breakthrough models with analytical solutions in a fixed-bed column" (HU24) |
| Foundations template | Cheong, D. (2022) FYP thesis, "Mathematical Modelling of CO₂ Adsorption in Functionalised Silica Nanocomposite Membranes" (FYP) |
| Mode | Research-mode (`SKILL.md`): claims grounded; verbatim quoting minimal; conflicts surfaced |
| Date | 18 May 2026 |

This file has three parts. **Part I** designs the literature-review section as a foundations ladder modelled on the FYP thesis. **Part II** is the third-pass virtual re-implementation of HU24 the brief asked for — re-deriving the paper's central result, challenging every assumption, separating innovation from inherited material, and jotting future work. **Part III** converts both into concrete drafting instructions.

---

# PART I — The literature review, designed

## I.1 Why a foundations ladder, and why the FYP thesis is the template

The Cheong FYP thesis is the direct predecessor in this supervisory group, and its structure earns its place as a template for one reason: it does not list literature, it **builds a verdict**. Its Chapter 2 establishes three fundamentals — heat of adsorption, the three mass-transfer resistances, the isotherm hierarchy — then Chapter 4 surveys two model families (adsorption *reaction* models, adsorption *diffusion* models) and closes with §4.3, a *Discussion* that selects one family and states why. The reader arrives at the model choice having been walked up a ladder, not handed a conclusion.

The interim report's §3 should do the same. The report spec (`interim_report_prompt.md` §3.1–3.5) already prescribes a five-rung structure; the FYP precedent tells us *how to write each rung* — every rung ends by handing the next rung a question.

**The rhetorical hinge.** The FYP thesis reached a specific verdict: adsorption reaction models (pseudo-first-order, pseudo-second-order, fractional-order) are convenient but "cannot be scaled for materials of different geometry, porous structures, and surface textures," and their analytical solutions are "valid only when the equilibrium adsorption capacity is constant" — which passive adsorption violates (FYP §4.3). This project reaches a structurally identical verdict one scale up: the empirical breakthrough models (Bohart–Adams, Thomas, Yoon–Nelson) are convenient but cannot scale, because their "constants" drift with operating conditions (SURVEY, HU24 §5.4). **The literature review should state this parallel explicitly** — the predecessor thesis rejected lumped reaction models at the *membrane* scale for the same reason this project rejects lumped breakthrough models at the *column* scale. That sentence ties the project to its lineage and justifies the mechanistic-model choice in one move.

## I.2 The ladder — five rungs, each ending in a question

| Rung | Report § | Content | Closing question handed down |
|---|---|---|---|
| 1 — Fundamentals | 3.1–3.2 | Adsorption thermodynamics (heat of adsorption, exothermicity); the three mass-transfer resistances (external film → intraparticle pore → reaction at the site); the isotherm hierarchy Henry → Langmuir → Toth | *If uptake is governed by a competition of resistances, what does that competition look like at the scale of a whole bed?* |
| 2 — The fixed bed | 3.3 | The three-zone picture (saturation / mass-transfer zone / unused bed); the breakthrough curve as the MTZ's mirror; definitions of $\tau_{BT}$ (5%), $\tau_{sat}$ (95%), $W_{MTZ}$ | *Given a breakthrough curve, which model recovers the physics — and which only fits the shape?* |
| 3 — The empirical/analytical landscape | 3.4.3 | Bohart–Adams, Thomas, Yoon–Nelson, Clark, Wolborska, Klinkenberg, Chern–Chien, fractal-like and empirical (Weibull, Gompertz, Gudermannian) — grouped, not listed | *Why can none of these be a primary benchmark?* |
| 4 — The mechanistic alternative | 3.4.1–3.4.2, 3.4.4 | The 1-D PDE system; LDF; Toth closure; travelling-wave / Rankine–Hugoniot reduction | *How is such a system actually solved?* |
| 5 — Numerical method | 3.5 | Method of Lines; stiff ODE integration; why the system is stiff | — (hands off to report §5) |

Rungs 1, 2 and 5 transfer almost verbatim from the design file's scale ladder and from `derivation.md`/MATHGUIDE. **Rungs 3 and 4 are where HU24 and SURVEY do the work**, and where the third pass (Part II) feeds in.

## I.3 The model-landscape synthesis — thematic, grounded in SURVEY

Do not narrate papers. SURVEY already supplies the thematic spine; use its four-part structure, compressed into three themes for the report.

**Theme A — The empirical/analytical models are one idea wearing many names, and cannot scale.** Chu (2020) and HU24 establish that Bohart–Adams, Thomas and Yoon–Nelson all reduce to a single logistic function $c/c_0 = 1/(1+e^{k(\tau-t)})$; their parameters are algebraically interchangeable, $k_{YN}=k_{BA}c_0=k_T c_0$ (HU24 Eq. 62). Comparing their fitted $R^2$ values is therefore empty — fitting one fits all. Myers, Cabrera-Codony & Valverde (2023) sharpen the verdict: these "constants" are not constant. For toluene on activated carbon the Yoon–Nelson $k_{YN}$ nearly doubles as inlet concentration rises from 0.41 to 1.32 g/m³ — a clear signature that the sink model is wrong (SURVEY Paper 2). Bohart–Adams also demands a physically inconsistent initial condition: the column full of contaminant at $t=0$ yet none of it adsorbed (SURVEY Paper 2). **Consequence the report must draw:** these models may *describe* a curve but cannot *predict* one or scale to a new column, so they are excluded as primary benchmarks.

**Theme B — Asymmetry is the rule, and it carries mechanism.** Real breakthrough curves are asymmetric S-shapes even for single-solute adsorption (HU24 §5.6). The symmetric logistic family cannot represent this. HU24's response is fractal-like kinetics — a time-decaying rate constant $k=k_0 t^{-h}$ — which restores asymmetry through one extra parameter $h$ (HU24 §3.2). The mechanistic literature reads the same asymmetry physically: a long tail signals intraparticle-diffusion control, two site populations of unequal reactivity, or — for amine sorbents — slow bulk-amine kinetics (REACT; Cabrera-Codony et al. 2026 report a 50→95% rise 5.4× longer than the 5→50% rise). **Consequence:** asymmetry is a measurement, not noise; the design file's asymmetry index $\mathcal{A}=(\tau_{95}-\tau_{50})/(\tau_{50}-\tau_5)$ turns it into the model-selection trigger.

**Theme C — Mechanistic PDE models predict; this project builds one.** Shafeeyan, Wan Daud & Shamiri (2014) catalogue 34 CO₂ fixed-bed models; the field standard is a 1-D axially-dispersed mass balance with an LDF sink and a non-linear isotherm (SURVEY Paper 7). Juela et al. (2021) and Lin et al. (2017) show such models predict breakthrough across flow rate, concentration and bed length from *a priori* correlations, with no per-curve refitting — exactly the scalability the empirical models lack. The cost is a coupled PDE system needing numerical solution. **Consequence:** the project adopts the mechanistic route, with the empirical models retained only as failed-comparison cases.

A single comparison table belongs in the report at the end of §3.4.3:

| Model family | Predicts or fits? | Scales to new column? | Captures asymmetry? | Role in this project |
|---|---|---|---|---|
| Bohart–Adams / Thomas / Yoon–Nelson | Fits only | No (constants drift) | No (symmetric) | Failed-comparison case |
| Clark, modified dose-response | Fits, flexible | No | Yes (extra parameter) | Failed-comparison case |
| Klinkenberg | Approx. analytical | Limited ($\zeta\ge2,\tau\ge1$) | No (error function) | **Gate-A linear benchmark** |
| Fractal-like (BA/Thomas/YN/Clark) | Fits, heterogeneity-aware | No (see Part II.5) | Yes | Discussion only |
| Mechanistic 1-D PDE + LDF + Toth | Predicts | Yes | Yes (with energy balance / DK) | **The project's model** |

## I.4 Section §3 skeleton — drop-in narrative spine

> **3.1–3.2** Open with the climate/DAC motivation (LIT-S, LIT-J), then the three fundamentals — adsorption is exothermic chemisorption on amine sites; uptake crosses three resistances in series; equilibrium follows an isotherm whose curvature demands Toth over Langmuir at 400 ppm. Close: *the bed integrates these into a travelling front.*
>
> **3.3** The three-zone bed and the breakthrough curve as the MTZ's mirror; define $\tau_{BT},\tau_{sat},W_{MTZ}$; introduce Stampi-Bombelli et al. (2024) as the benchmark and its finding that transport, not equilibrium capacity, limits performance at DAC concentrations. Close: *which model recovers this physics?*
>
> **3.4.3** Theme A then Theme B — the empirical models, their hidden equivalence, their drift, their inability to scale; the comparison table. Close: *none can be a primary benchmark.*
>
> **3.4.1–3.4.2, 3.4.4** Theme C — the governing PDE, LDF, Toth closure, R–H/travelling-wave reduction. Close: *this system is stiff and needs the Method of Lines.*
>
> **3.5** MOL and stiff ODE integration.

---

# PART II — Third-pass virtual re-implementation of Hu et al. (2024)

> *Method (Keshav, three-pass): re-implement the paper virtually — make the authors' assumptions, re-create the result, then compare the re-creation with the paper to expose innovations, hidden assumptions and failings; note how one would present each idea differently; jot future work.*

HU24 is a review, so "re-implementation" means re-deriving its central analytical claims and re-running its comparative logic independently, then auditing the paper against that re-creation.

## II.1 What the paper claims (first-pass placement)

HU24 is a **review with a thesis**. Category: critical review, water-treatment domain (*J. Water Process Eng.*). Contribution: it (a) consolidates every analytical breakthrough model into one taxonomy, (b) argues that Bohart–Adams, Thomas and Yoon–Nelson are mathematically one logistic function and that comparing them is meaningless, (c) promotes fractal-like kinetics as the route to asymmetric curves, and (d) prescribes F-test + AIC + residual plots over bare $R^2$ for model selection. Relevance to this project: it is the **authoritative map of the model family the project must reject as benchmarks** — and the source-of-truth for *why* that rejection is correct.

## II.2 Re-deriving the central result — the BA = Thomas = YN equivalence

The paper's keystone claim is the equivalence of the three traditional models. Re-implement it from HU24's own equations. The full Bohart–Adams model (HU24 Eq. 10):

$$\frac{c}{c_0} = \frac{e^{k_{BA}c_0 t}}{e^{k_{BA}a_0 x/u} + e^{k_{BA}c_0 t} - 1}$$

Divide numerator and denominator by $e^{k_{BA}c_0 t}$:

$$\frac{c}{c_0} = \frac{1}{e^{k_{BA}(a_0 x/u - c_0 t)} + 1 - e^{-k_{BA}c_0 t}}$$

The authors drop the third term to reach their logistic Eq. (11):

$$\frac{c}{c_0} = \frac{1}{1 + \exp\!\bigl[k_{BA}c_0\,(a_0 x/(u c_0) - t)\bigr]}$$

Thomas (Eq. 14) and Yoon–Nelson (Eq. 15) are *already* in this logistic form. Matching parameters gives $k_{YN}=k_{BA}c_0=k_T c_0$ and $\tau=a_0x/(uc_0)=q_0 m/(\nu c_0)$ — the paper's Eqs. (62)–(63). **The re-derivation confirms the paper: the three models are one logistic curve.**

**But the re-implementation exposes a hidden qualifier the paper states loosely and then forgets.** The equivalence required dropping $e^{-k_{BA}c_0 t}$, which vanishes only for $k_{BA}c_0 t \gg 1$. The equivalence is therefore **asymptotic** — exact at large $t$, *not* near $t=0$. HU24 says the dropped term is "entirely negligible except for very small values" (its §3.1.1) yet then asserts flat, unqualified equivalence in §5.4. The sharper statement: the three models coincide away from the foot of the curve, and the *same* dropped term is why all three fit poorly at early time (HU24 notes the poor early-time fit separately, in §3.1.4, without connecting it to the dropped exponential). **One mechanism explains both the equivalence and the early-time failure** — a unification the paper has all the pieces for but never assembles. This is a genuine third-pass yield: a re-presentation that is strictly clearer than the original.

## II.3 Assumption-by-assumption challenge

**The governing PDE (HU24 Eq. 1) and its six stated assumptions** — isothermal; axial plug flow; negligible radial dispersion; LDF solid kinetics; uniform spherical particles; constant geometry, velocity and voidage. Five are routine. **Assumption (i), isothermal, is the load-bearing one — and the paper never flags its scope.** Every dataset HU24 analyses is aqueous-phase (ciprofloxacin, methylene blue, Ni(II), methyl orange, phenol, p-nitrophenol). In liquid-phase adsorption the heat of adsorption is carried away by a large-heat-capacity solvent and the isothermal assumption is benign. **For gas-phase CO₂ capture it is not** — $\Delta H_{ads}\approx70$ kJ/mol on amine sorbents drives front temperature excursions that shift the isotherm (REACT; PEIMODEL). HU24 is published in a *water* journal and is silent on this, so a reader importing it into a DAC project inherits an unstated, and here invalid, assumption. **This is the single most important finding of the third pass for John's project** (see Part III).

**The LDF sink (HU24 Eq. 3), $\partial q/\partial t = k_s(q_e-q)$.** The paper adopts it without challenge. Myers et al. (2023), in the same SURVEY set, show LDF predicts a positive uptake rate where $c\approx0$ at the wave front — adsorption with nothing to adsorb. HU24 does not cite this objection. Not a fatal flaw for the paper's purpose, but a missing caveat the project's review should supply.

**The fractal-like rate law $k=k_0 t^{-h}$ (HU24 Eq. 34).** This is the paper's preferred fix for asymmetry, and it carries a hidden defect the paper does not acknowledge. For $k$ to keep units of time⁻¹, $k_0$ must carry units of time$^{h-1}$ — a dimensionality that **depends on the fitted exponent $h$**. HU24's own Table 2 prints this: the fractal-like rate constant appears as "L mg⁻¹ min$^h$⁻¹", with $h$ inside the unit. So a fractal-like constant fitted on ciprofloxacin ($h=0.487$) and one fitted on p-nitrophenol ($h=0.058$) are not the same physical quantity and cannot be compared across systems. Eq. (34) is also restricted to $t\ge1$ — the *identical* dimensional artifact for which HU24 rightly criticises the logarithmic-transform models (its §3.2, "$t>1$" restriction, "meaningless in practice"). **The paper applies a standard of rigour to the log-models that it exempts its own preferred models from.** This is an internal inconsistency, and it is citable.

**The F-test and AIC machinery (HU24 §4, Eqs. 57–59).** Promoting F-test/AIC over bare $R^2$ is sound and is a real service. But the F-test p-values in Table 2 (e.g. $p=8.55\times10^{-10}$) are valid only if residuals are independent and Gaussian with constant variance. A breakthrough response is bounded in $[0,1]$, so its residual variance is structurally pinched near $c/c_0\to0$ and $\to1$ — heteroscedastic by construction. HU24 itself notes (its §5.5) that linearisation "violates the error variance and normality assumptions"; yet it then applies F-test/AIC to nonlinear fits **without testing those same assumptions**. The paper advances rigour by one step and stops one step short: it recommends the residual plot as the better diagnostic but runs no formal normality or heteroscedasticity test before quoting precise p-values.

**The modified dose-response interchange (HU24 §3.1.6, Fig. 2).** Here the paper is at its sharpest. It shows that setting the dose-response parameter $b=q_0m/(c_0\nu)$ to make it interchangeable with the Thomas parameter is invalid, because the areas under the two curves differ ($A_2\ne A_3$) even though the curves cross at $c/c_0=0.5$. The re-implementation confirms this — curve intersection does not imply parameter identity. This argument is correct, original to the consolidation, and well presented.

## II.4 Innovation versus inherited material

A review's contribution is its synthesis, but honest reading separates what HU24 *originates* from what it *relays*.

| Element | Origin |
|---|---|
| BA = Thomas = YN equivalence; oversimplified-BA-is-exponential critique | **Inherited** from Chu (2020), explicitly cited |
| Fractal-like models; the $\mu_{max},\lambda$ characteristic parameters; Gudermannian/error models | **Inherited** from the authors' own earlier papers (HU24 refs [1], [64], [108]) |
| Systematic F-test + AIC + Akaike-weight comparison with a worked OriginPro procedure | **Genuinely this paper** |
| Quantified partial-vs-complete-curve bias (Table 3: $k_T$ error up to 110.8%) | **Genuinely this paper** |
| The modified-dose-response area argument ($A_2\ne A_3$, Fig. 2) | **Genuinely this paper** |
| The consolidated taxonomy itself — a beginner's map of ~15 models | **The review's core contribution** — synthesis is the value |

The honest summary: HU24's *analytical* novelty is modest (much is Chu (2020) and Hu's own prior work), but its *consolidating* novelty is real and useful — it is the single best map of the empirical-model landscape, which is exactly the use this project makes of it.

## II.5 Hidden failings and scope limits — collected

1. **Undeclared liquid-phase scope.** Every dataset is aqueous; the isothermal assumption is never flagged as scope-limiting. Conclusions do not transfer unaltered to gas-phase DAC.
2. **Asymptotic equivalence presented as exact.** The BA/Thomas/YN equivalence holds for $k_{BA}c_0 t\gg1$; the paper drops the qualifier in §5.4.
3. **Uneven rigour on dimensionality.** The fractal-like rate constant has $h$-dependent units and a $t\ge1$ restriction — the same defects the paper condemns in log-models.
4. **F-test/AIC assumptions unchecked.** Precise p-values are quoted without a residual normality or homoscedasticity test, despite the paper itself naming those assumptions elsewhere.
5. **Partial-curve bias reported, not modelled.** Table 3 shows the $k_T$ error swings from 110.8% (50 mg/L) to 26.1% (100 mg/L) — strongly concentration-dependent — but the paper does not characterise *what governs* the bias.
6. **The Klinkenberg "correction" is asserted.** §3.1.7 claims it corrects improper $\zeta,\tau$ expressions in the literature but does not show the incorrect and corrected forms side by side; the reader must trust it.

## II.6 How I would present this paper's ideas differently

- **Lead with the equivalence relations.** HU24 buries $k_{YN}=k_{BA}c_0=k_T c_0$ in §5.4. It is the single most useful result; it belongs in the abstract and the first figure.
- **Replace the flat model list (§3.1.1–3.1.8) with a decision tree** keyed on three binary splits: symmetric vs asymmetric, theoretical vs empirical, homogeneous vs heterogeneous. This is the form the interim report should adopt, and it is exactly what the design file's asymmetry index $\mathcal{A}$ operationalises.
- **State the equivalence's domain of validity** ("large $t$") wherever the equivalence is invoked, and connect it to the shared early-time misfit — one sentence unifies two of the paper's separate observations.
- **Add a scope box**: "All datasets here are liquid-phase; for gas-phase or non-isothermal systems, re-examine assumption (i)." One box would prevent every future mis-import.

## II.7 Future-work hooks (jotted, per the third-pass instruction)

1. **A unit-consistent fractal-like model.** Recast $k=k_0(t/t_{ref})^{-h}$ with an explicit reference time so $k_0$ keeps fixed units across datasets; test whether fitted $h$ then correlates with an independently measured pore fractal dimension or PSD width. Removes failing #3.
2. **Does the BA/Thomas/YN equivalence survive non-isothermal coupling?** Re-run the equivalence algebra with the energy balance attached. Hypothesis: the heat-of-adsorption feedback breaks the logistic symmetry, so the three models are *not* equivalent for gas-phase exothermic adsorption. If true, this is both publishable and directly the gap this project sits in.
3. **Model the partial-curve bias.** Derive the bias in fitted $k_T,q_0$ as a function of truncation fraction and isotherm curvature, turning HU24's Table 3 observation into a predictive correction.
4. **A heteroscedasticity-robust model-selection protocol** for breakthrough curves — weighted least squares or a variance-stabilising transform before F-test/AIC. Closes failing #4.
5. **Couple the static three-zone MTZ picture to a travelling-wave speed.** HU24's MTZ description is kinematic only; bolting on the Myers & Font wave speed would let the breakthrough time be *predicted a priori* instead of fitted — the bridge this project's design file already proposes.
6. **A single asymmetry metric** ($\mathcal{A}$) applied across HU24's own datasets, to test whether $\mathcal{A}$ predicts which model family wins — a direct, low-cost validation of the design file's escalation rule.

---

# PART III — What this changes in the interim report

**Cite HU24 for, and only for, the right things.** It is the authoritative source for: the three-zone MTZ picture; the BA/Thomas/YN equivalence and the interchange relations; the oversimplified-BA-is-exponential error; the partial-curve bias; the F-test/AIC-over-$R^2$ recommendation. **Do not cite it** for any claim that an isothermal, incompressible-flow model is adequate — its scope is liquid-phase water treatment, and the project's gas-phase CO₂ system has a 70 kJ/mol heat of adsorption that the paper's framework silently assumes away.

**Write the equivalence with its qualifier.** In §3.4.3, state the equivalence as a large-$t$ (asymptotic) result and note that the shared dropped term is also why all three models misfit early-time data. This is more correct than HU24's own §5.4 and shows genuine engagement.

**Use the FYP parallel as the §3.4.3→§3.4.1 transition.** "Just as the predecessor membrane study found lumped reaction models unscalable across geometry (Cheong 2022), the empirical breakthrough models prove unscalable across operating conditions; both verdicts point to a mechanistic, transport-grounded model." This single sentence justifies the whole modelling chapter and roots the project in its lineage.

**Present the empirical models as a decision tree, not a list** — the re-presentation from II.6, operationalised by the asymmetry index $\mathcal{A}=(\tau_{95}-\tau_{50})/(\tau_{50}-\tau_5)$ from the design file. Symmetric ($\mathcal{A}\approx1$) → logistic family; asymmetric ($\mathcal{A}\gtrsim3$) → mechanistic model with dual kinetics.

**Carry the fractal-like critique into the Discussion, not the recommendation.** Fractal-like models are heterogeneity-aware and worth describing, but their $h$-dependent units make their rate constants non-transferable — so they join the empirical models as discussion material, never as a project benchmark. This is consistent with SURVEY's standing verdict that empirical models must not be primary benchmarks.

**One future-work item is the project's own gap.** Hook #2 — whether the model equivalence survives non-isothermal coupling — is not idle: it *is* the space this project occupies. The conclusion (report §7) can name it as the question the parametric study begins to answer.

---

*End of file. Part I designs report §3 on the FYP foundations template; Part II is the third-pass re-implementation of HU24, with the liquid-phase scope limit as its principal finding; Part III turns both into drafting instructions. Every claim traces to HU24 (read in full), `lit_survey_summaries.md`, the Cheong FYP thesis, or the project files named in the design file's source ledger.*
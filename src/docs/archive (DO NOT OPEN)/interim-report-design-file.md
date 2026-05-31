# DESIGN FILE — Interim Report

**Parametric Study of CO₂ Adsorption Breakthrough in Packed-Bed Columns Using Polymer-Based Sorbent**

| | |
|---|---|
| Project | NP Y3 Design Project, Group 3 (N93), Apr–Aug 2026 |
| Supervisors | Prof. Erik Birgersson (SUTD), Dr. Prapatsorn Borisut (NUS/SUTD); NP: Dr. Pham The Hanh |
| Purpose of this file | Plan and scaffold the Interim Report. Not the report itself. |
| Companion files | `derivation.md` (math chapter source), `interim_report_prompt.md` (report spec) |
| Mode | Research-mode (`SKILL.md`): every claim grounded in a named source; no internet; conflicts flagged, not smoothed over |
| Date | 18 May 2026 |

---

## 0. What this file is

This is the **bridge** between four years of accumulated reading notes and a single coherent Interim Report. The report spec (`interim_report_prompt.md`) fixes the *structure*; the markdown knowledge pools supply the *content*; this file supplies the **narrative thread, the provenance map, and the honest status of every claim** so the report can be written without inventing anything.

It does three jobs. First, it states the one argument the whole report makes (§2). Second, it maps every report section to its source material and marks what is done versus missing (§6). Third, it isolates the genuinely novel contribution and the unresolved discrepancies, so neither is lost in the drafting (§5, §8).

Use it as the editorial spine: write each report section against §6, check every number against §1, and resolve every flag in §8 before final submission.

---

## 1. Source ledger and provenance

Anti-hallucination rule in force: a claim is "cited" only if it traces to one of these. Numbers without a row here do not enter the report.

| Tag | Source file | What it grounds |
|---|---|---|
| **DERIV** | `derivation.md` (project) | Governing PDE system, term-by-term tables, dimensionless groups, R–H velocity, Gates |
| **LIT-S** | `literature_review (saras)` (project) | Climate context, adsorption principles, indoor-CO₂ health, Climeworks figures |
| **LIT-J** | `literature_review (john)` (project) | Draft intro, transport-phenomena derivations, Toth vs Langmuir heterogeneity |
| **SOP** | `Standard_Operating_Procedure…` (project) | Rig description, valve protocol, data-recording table, validity criteria |
| **ROADMAP** | `CO2_Adsorption_Literature_Roadmap.md` | Six governing concepts, paper inventory (P1–P21), reading sequence |
| **SURVEY** | `lit_survey_summaries.md` | 9-paper critique of empirical breakthrough models; why Bohart–Adams/Thomas/YN fail |
| **REACT** | `CO2_Adsorption_Reaction_Models…Literature_Review.md` | Toth/PFO/DK selection logic, Myers & Font reduction, Cabrera-Codony PEI chemistry, validation gates |
| **MATHGUIDE** | `CO2_Adsorption_Breakthrough_Modelling…Mathematical_Reading_Guide.md` | Isotherm hierarchy, LDF/Glueckauf, travelling-wave theory, MOL solver design, paper-by-paper |
| **PEIMODEL** | `CO2_Adsorption_Breakthrough_Model_PEI_SiO2.md` | The project's proposed unified DK travelling-wave model |
| **SPEC** | `interim_report_prompt.md` | Report structure, DOE matrix, hypotheses table, nomenclature, Strunk & White rules |

**Provenance honesty.** MATHGUIDE itself states its Google Drive `tier_0` folder was inaccessible and the guide leans on open-web sources. So MATHGUIDE values are second-hand digests, not the primary PDFs. Where a number drives a validation gate, the report must cite the **primary paper**, retrieved and checked — this is logged in §8.

---

## 2. The research narrative — one spine

Everything in the report serves this single argument. State it once here; never let a section drift from it.

> **A packed-bed CO₂ breakthrough curve is not a curve to be fitted — it is a measurement of three competing physical timescales (advection, dispersion, finite-rate uptake) acting on a thermodynamic capacity. The project builds the minimum first-principles model that resolves all three, validates it in three escalating gates, and then reads the parametric sensitivity of breakthrough not as raw curves but as motion across a dimensionless (Pe, NTU) regime map. The novel step is to fold the dual-site amine chemistry of PEI@SiO₂ into the analytical travelling-wave framework, giving a hybrid analytical–numerical breakthrough expression that no single reference achieves alone.**

The narrative has four beats, and the report's sections must hit them in order:

1. **Motivation → gap.** DAC matters; parametric breakthrough data at 400 ppm with a *characterised* isotherm are sparse; Stampi-Bombelli et al. (2024) is the first rigorous benchmark, on γ-alumina — not on the PEI@SiO₂ this project actually runs. *(LIT-S, LIT-J, REACT)*
2. **Why a mechanistic model, not an empirical fit.** Bohart–Adams, Thomas and Yoon–Nelson are one logistic curve in three disguises; their "constants" drift with operating conditions, so they cannot predict or scale. Only a transport-grounded model can. *(SURVEY, REACT)*
3. **The model, argued term by term.** Each PDE term earns its place by a necessity argument (§4.2); the closure is Toth, not Langmuir, for a stated reason; the kinetics start as PFO and escalate to dual-kinetic only on a measured trigger. *(DERIV, MATHGUIDE, PEIMODEL)*
4. **Validation then prediction.** Three gates (linear solver, R–H velocity, Stampi-Bombelli benchmark) must clear *in order* before any parametric sweep. The sweep's output is a regime map, and the wet-rig PEI@SiO₂ runs are the final empirical layer. *(DERIV, REACT, SPEC)*

---

## 3. Organising principle — the scale ladder

Do not review papers one by one. Organise the literature, and the model, across three physical scales. This is the frame that makes the review cohere instead of listing.

| Scale | Question it answers | Governing object | Anchor sources |
|---|---|---|---|
| **Molecular** | How much CO₂ does an amine site hold, and how fast does it react? | Toth isotherm; zwitterion-carbamate chemistry; ΔH_ads | REACT (Cabrera-Codony, Bos), MATHGUIDE (isotherm hierarchy) |
| **Particle** | How fast does CO₂ reach the site through film + pore + polymer? | LDF coefficient; PFO vs dual-kinetic split; Glueckauf $k=15D_p/r_p^2$ | MATHGUIDE (Glueckauf, Stampi-Bombelli k-table), SURVEY (Shafeeyan resistances) |
| **Process** | How does the bed-scale front move, sharpen, and break through? | 1-D PDE system; Pe, NTU, α, Λ; R–H shock; travelling wave | DERIV, REACT (Myers & Font), MATHGUIDE (travelling-wave) |

The report's §3 (Literature Review) walks **up** this ladder; the model in §5 is **assembled** along it; the parametric study reads sensitivity **across** it. One ladder, used three times.

---

## 4. The argument core — every model term earned

This section is the intellectual centre. It is written for report §5 (Mathematical Model) and feeds the rewrite of `derivation.md` flagged in §8.

### 4.1 The governing PDE system (Toth-corrected)

The system is four balances plus an algebraic closure. Forms below follow **DERIV**, with the isotherm corrected from Langmuir to Toth (see §4.3) and the LDF written on the solid-loading driving force $(q^*-\bar q)$ for consistency with every modelling paper in REACT/MATHGUIDE.

**Gas-phase CO₂ mass balance**

$$\varepsilon\,\frac{\partial C}{\partial t} = -\,u\,\frac{\partial C}{\partial z} + D_{ax}\,\frac{\partial^2 C}{\partial z^2} - (1-\varepsilon)\,\rho_p\,\frac{\partial \bar q}{\partial t}$$

**Solid-phase LDF balance**

$$\frac{\partial \bar q}{\partial t} = k\,\bigl(q^*(C,T_s) - \bar q\bigr)$$

**Toth equilibrium closure** (replaces DERIV §1.5 Langmuir)

$$q^*(p,T) = \frac{n_s(T)\,b(T)\,p}{\bigl[\,1 + (b(T)\,p)^{t(T)}\,\bigr]^{1/t(T)}}, \qquad p = C R_g T$$

$$n_s(T)=n_{s0}\,e^{\chi(1-T/T_0)}, \quad b(T)=b_0\,e^{\frac{\Delta H_0}{R_g T_0}\left(\frac{T_0}{T}-1\right)}, \quad t(T)=t_0+\alpha\bigl(1-T_0/T\bigr)$$

**Energy balances** (gas and solid, retained — see §4.2 point 5 and §8 on the wall term)

$$\varepsilon\rho_g c_{pg}\frac{\partial T_g}{\partial t} = -\rho_g c_{pg} u\frac{\partial T_g}{\partial z} + \lambda_{ax}\frac{\partial^2 T_g}{\partial z^2} + h_f a_p (T_s-T_g) + \frac{4h_w}{d_c}(T_w-T_g)$$

$$(1-\varepsilon)\rho_p c_{ps}\frac{\partial T_s}{\partial t} = h_f a_p (T_g-T_s) + (-\Delta H_{ads})\rho_p(1-\varepsilon)\frac{\partial \bar q}{\partial t}$$

**Rankine–Hugoniot front velocity** (the Gate-B target)

$$v_{sh} = \frac{u\,\Delta C}{\varepsilon\,\Delta C + (1-\varepsilon)\rho_p\,\Delta q}$$

Term-by-term physical justification tables already exist in **DERIV §1–2** and transfer directly into report §5.1 — do not re-derive, cite and lift.

### 4.2 The necessity ladder — why each term must be there

This is the constructive argument the report should make. Build the model up; show each term solves a defect of the previous one.

1. **Pure advection alone is insufficient.** $\varepsilon\,\partial_t C = -u\,\partial_z C$ moves a perfect step. It produces a breakthrough time but a vertical, shapeless front — it cannot represent a mass-transfer zone. *Defect: no MTZ.*
2. **The LDF sink is necessary for MTZ width.** Finite-rate uptake $k(q^*-\bar q)$ spreads the step into an S-curve whose width scales with NTU. This is the term that makes "breakthrough curve" a meaningful object. *(SURVEY: the S-shape "is a mirror of the MTZ".)*
3. **Axial dispersion is necessary at lab scale.** LDF + constant-pattern still under-predicts smearing when $\mathrm{Pe}<\sim100$. Juela et al. (2021) show axial dispersion is significant at bench scale and is *the* reason empirical models mis-fit. The 8.2 mm SUTD column is firmly in this regime. *Defect without it: too-sharp fronts on short beds. (SURVEY, MATHGUIDE)*
4. **Toth closure is necessary for the right wave speed.** Langmuir over-predicts low-pressure capacity; the heterogeneity exponent $t<1$ captures the steep DAC-regime knee. Crucially, $\Delta q$ in $v_{sh}$ is set entirely by isotherm shape — a Langmuir-fitted-to-Toth-data model gives the wrong $v_{sh}$. *(MATHGUIDE §B4; LIT-J on site heterogeneity.)*
5. **The energy balance is conditionally necessary.** Heat of adsorption ($\sim$70 kJ/mol) feeds back through $b(T)$. For the narrow 8.2 mm rig the wall term is *not* negligible (Shafeeyan: lab columns need it). Keep the energy balance; default the wall term ON, with the adiabatic case used only as a screening simplification. *(SURVEY, MATHGUIDE; conflict logged in §8.)*
6. **The dual-kinetic split is necessary only on a measured trigger.** PFO suffices for packed beds of mm-pellets (Stampi-Bombelli: DK collapses to PFO there). Escalate to DK only if the breakthrough is measurably asymmetric — quantified in §7. *Sufficiency is conditional, not assumed.*

The report's §5 should present this as a ladder, not a list of equations — that is what makes it an argument rather than a transcription.

### 4.3 Closure: Toth, not Langmuir — and a two-bracket parameter strategy

`derivation.md` currently closes on **Langmuir** (its §1.5, §2.5). The project pivoted to **Toth** in study_plan v2.0. The report and the rewritten `derivation.md` must use Toth. Justification: at 400 ppm the surface presents a *distribution* of amine environments (primary/secondary, carbamate, carbamic-acid, bicarbonate) that a single-energy Langmuir cannot represent; Toth's $t<1$ is the minimal correction. *(LIT-J, MATHGUIDE §A1, REACT §1.)*

**The parameter problem — and a proposed resolution.** Two candidate Toth parameter sets exist in the sources, and they disagree sharply:

| Set | n_{s0} | b₀ (kPa⁻¹) | t₀ | ΔH₀ (kJ/mol) | χ | α | T₀ | Fitted on |
|---|---|---|---|---|---|---|---|---|
| **A (benchmark)** | 1.23 mol/kg | 4839 | 0.25 | 70 | 0 | 0.11 | 298 K | amine-grafted γ-alumina (Grossmann 2023; Stampi-Bombelli 2024) |
| **B (analogue)** | 0.81 mmol/g | 6.2×10³ | 0.40 | 210 | 6.6 | 10.8 | 308 K | PEI-impregnated silica fibre (Pang et al. 2024) |

Set A is the project's current baseline but is γ-alumina chemistry. Set B is **PEI-on-silica** — chemically far closer to PEI@SiO₂ — yet was not in the active parameter list. **Proposed strategy:** treat A and B as a *bracket*. Run the solver with both; the project's PEI@SiO₂ prediction should lie between them. Collapse the bracket only when the project's own equilibrium isotherm is measured. This converts an unquantified caveat into a bounded uncertainty band — a defensible, honest design choice.

*Note (§8): the recovered closure value is $\alpha=0.11$, $\chi=0$ for Set A (MATHGUIDE) — this resolves the long-standing "missing α" issue. Set B's $\Delta H_0=210$ kJ/mol is anomalously high against the 60–90 kJ/mol chemisorption range and must be cross-checked before use.*

### 4.4 Dimensionless reduction and the regime map — the report's "money figure"

DERIV §F already non-dimensionalises the full system into seven groups. The report should foreground the four that the OAT sweep actually moves:

$$\mathrm{Pe}=\frac{uL}{D_{ax}}, \quad \mathrm{NTU}=\frac{k\,a_p(1-\varepsilon)L}{\varepsilon u}, \quad \alpha=\frac{(1-\varepsilon)\rho_p q_{m0}}{\varepsilon C_0}, \quad \Lambda=\frac{(-\Delta H_{ads})q_{m0}}{c_{ps}T_{ref}}$$

The creative synthesis: the four controllable parameters do not act independently — they move the bed through dimensionless space.

| Sweep variable ↑ | Pe | NTU | α | Λ |
|---|---|---|---|---|
| Superficial velocity $u$ | ↑ (saturating, since $D_{ax}=6.95u+0.02$) | ↓ ($\propto 1/u$) | — | — |
| Inlet concentration $C_{in}$ | — | — | ↓ ($\propto 1/C_0$) | ↑ |
| Bed length $L$ | ↑ | ↑ | — | — |
| Adsorption temperature $T_{ads}$ | — | — | ↓ (via $b(T)$↓) | ↓ |

**The report's central figure should therefore not be raw breakthrough curves versus time.** It should be $\tau_{BT}$ (and the asymmetry index of §7) plotted as a surface over the (Pe, NTU) plane, with α and Λ as the parametric family. This is the format the Myers and Mazzotti groups have converged on (REACT §Stage 4) and the one the supervisors will recognise. It also makes H1–H5 *readable off one figure*: H1 is motion along the NTU axis, H3 is motion along both Pe and NTU, H4 is an α–Λ shift.

DERIV §F.6 already lists the limiting regimes (Pe→∞ shock; NTU→∞ chromatographic; Λ≪1 isothermal). The regime map *is* those limits drawn as territory.

---

## 5. The novel contribution — hybrid dual-kinetic travelling wave

### 5.1 Statement

PEIMODEL proposes the project's original result: extend the Myers & Font (2020) travelling-wave reduction to the dual-kinetic amine model, splitting loading into fast surface sites and slow bulk-PEI sites:

$$\bar q = q_1 + q_2, \qquad \frac{\partial q_1}{\partial t}=k_1(\eta q^* - q_1), \qquad \frac{\partial q_2}{\partial t}=k_2\bigl((1-\eta)q^* - q_2\bigr)$$

With $\kappa = k_2/k_1 \ll 1$, the fast sites carry a travelling wave and the slow sites a perturbation tail, yielding the **hybrid analytical–numerical breakthrough expression**:

$$\frac{c_1(L,t)}{c_{1,0}} \approx \underbrace{\frac{1-e^{-k_1(t-t_b)}}{1-\delta_{45}\,e^{-k_1(t-t_b)}}}_{\text{fast surface sites — analytical TW}} \;-\; \underbrace{\frac{1-\eta}{\eta}\,\kappa\,e^{-k_2(t-t_b)}}_{\text{slow bulk-PEI tail}}$$

with $t_b=\eta(1-\varepsilon)\rho_p q_0^* L/(u_0 c_{1,0})$ and $\delta_{45}=R_g T c_{1,0}/p_a$.

### 5.2 What is genuinely new

REACT §Gaps states it plainly: **no paper combines Toth + LDF with the Myers–Font travelling-wave reduction on PEI@SiO₂ at 400 ppm.** Cabrera-Codony et al. (2026) is closest but works at 1500 ppm with explicit two-reaction chemistry. The project's contribution is the *bridge*: Myers & Font supply the analytical machinery (homogeneous LDF); Stampi-Bombelli/Kalyanaraman supply the dual-site physics (purely numerical in their hands); PEIMODEL fuses them. The fast term reduces exactly to Myers & Font when $\eta=1$, and to a clean double-exponential in the DAC limit $\delta_{45}\to0$ — the two sanity checks a referee will demand.

### 5.3 Honest status — what must still be verified

Research-mode requires this stated, not buried:

- The combined expression is a **candidate** result. PEIMODEL §9 gives a leading-order + $O(\kappa)$ perturbation argument; it has **not yet been checked numerically** against the full MOL solver. Numerical confirmation is itself a piece of Gate-C-adjacent work and should be scheduled, not assumed.
- The tail term is *subtractive* — physically sensible (slow sites are an extra sink, suppressing gas concentration below the fast-only prediction), but its amplitude $\tfrac{1-\eta}{\eta}\kappa$ is a leading-order estimate; the back-coupling of $q_2$ uptake into the gas balance is only partially carried.
- For **packed beds**, Stampi-Bombelli found $k_1\approx k_2$ → DK collapses to PFO and η, k₂ are *un-identifiable from breakthrough alone* (REACT §D5). So the DK-TW model is the project's general framework, but for the SUTD packed bed the report should *expect* it to reduce to the single-wave PFO result, and say so. The DK machinery proves its worth only if a tail appears (§7).

The report should present this as **"a proposed analytical result with a defined verification path"** — that framing is both honest and stronger than over-claiming.

---

## 6. Section-by-section build plan

Each row: the narrative beat, the sources to draw from, equations to include, and current status. `[PLACEHOLDER]` marks a value the report must flag, never invent (SPEC rule).

| § | Section | Narrative beat | Sources | Equations | Status |
|---|---|---|---|---|---|
| Abstract | — | 4 sentences: context → gap → approach → outcome | SPEC | — | Draft exists in `interim_report_draft.docx`; tighten to 4 sentences |
| 1.1 | Background | DAC matters; Singapore context; PEI@SiO₂/SUTD rig | LIT-S, LIT-J | — | Drafted; cut e-bicycle boilerplate from template |
| 1.2 | Problem Statement | Sparse parametric data at 400 ppm; need validation on SUTD sorbent; name 4 inputs ($u,C_{in},L,T_{ads}$) + 4 metrics ($\tau_{BT},\eta,W_{MTZ},q_{dyn}$) | SPEC, REACT | — | Outline only — write |
| 1.3 | Scope | In: breakthrough experiments (wet rig), 1-D iso + non-iso model, sweep, validation vs Stampi-Bombelli. Out: regeneration, multicomponent, humidity | SPEC, updates log | — | Wet-rig runs **in scope** (per updates §6) |
| 2 | Objectives, deliverables, budget, schedule | Deliverables tied to assessment; Gantt at workstream abstraction | SPEC Gantt block | — | Use SPEC's 6-workstream Gantt; keep numerical-method detail out of it |
| 3.1 | Climate & capture motivation | 440 ppm; 993 Gt budget→2048; Climeworks Mammoth 105 t vs 36 000 t design | LIT-S, LIT-J | — | Source numbers verified in LIT-S/LIT-J |
| 3.2 | Adsorption principles & sorbents | Physisorption vs chemisorption; amine sorbents; PEI@SiO₂; $q$ as state variable | LIT-S, REACT, ROADMAP | — | Drafted in LIT-S |
| 3.3 | Packed-bed breakthrough | Stampi-Bombelli benchmark; transport limits dominate at DAC; define $\tau_{BT}$ (5%), $\tau_{sat}$ (95%), MTZ | REACT, MATHGUIDE, SOP | — | Synthesis needed |
| 3.4.1 | Governing PDE | Gas balance + LDF, term tables, Danckwerts BCs | DERIV §1.1–1.2, §2.1 | §4.1 set | DERIV ready; lift term tables |
| 3.4.2 | Isotherm models | Langmuir → Toth; t<1; both parameter sets (§4.3 bracket) | MATHGUIDE §A1, REACT §1 | §4.1 Toth | Two-bracket strategy is the new framing |
| 3.4.3 | PFO/DK kinetics; Klinkenberg–Thomas–Adam | PFO baseline; DK on trigger; empirical solutions stated *with* validity limits and the warning they are equivalent | SURVEY, MATHGUIDE §C, REACT §2 | DK pair (§5.1) | SURVEY is the demolition source — use it |
| 3.4.4 | R–H shock & travelling wave | Shock condition; $v_{sh}$; Myers & Font reduction | DERIV §1.6/§2.6/§E, MATHGUIDE §B, REACT §3 | $v_{sh}$ | Ready; **verify Myers & Font citation (§8)** |
| 3.5 | Method of Lines & stiff ODEs | Spatial discretisation → stiff ODE; why stiff (large α, fast LDF vs slow advection); BDF/LSODA | MATHGUIDE §D4, REACT §6 | — | Write from MATHGUIDE §D4 |
| 4.1–4.4 | Experimental design | Rig (ID 8.2 mm, ~10 g PEI@SiO₂, MFC-A/B/C, GasLab/Sensirion); SOP in ≤10 bullets; DOE matrix; validity criteria | SOP, SPEC | — | DOE matrix from SPEC; column length `[PLACEHOLDER]` |
| 5 | Mathematical model | The necessity ladder (§4.2); BCs/ICs; dimensionless groups; regime map; 3 gates | DERIV, §4 of this file | §4.1, §4.4 | Core chapter — `derivation.md` rewrite feeds it (§8) |
| 6 | Preliminary results | State honestly: calibration baseline, purge time, solver scaffold status, which gate is in progress | SOP, updates log | — | Most values still `[PLACEHOLDER]` — see §9 |
| 7 | Conclusion & next steps | What is established; what remains; gate confidence vs schedule | this file §9–10 | — | Write last |
| 8/9 | Appendix & references | Nomenclature, Toth params (both sets), data template; APA refs | SPEC, SOP, all | — | Reference list needs verification pass (§8) |

---

## 7. Hypotheses, gates, DOE — the empirical spine

**Hypotheses** (SPEC) — state each once in report §5, tabulated, each with its pre-committed threshold. H1: $u$↑ shortens $\tau_{BT}$, widens MTZ (slope vs R–H ±15%). H2: $C_{in}$↑ raises $q_{dyn}$, cuts $\tau_{BT}$ (Toth predicts $q_{dyn}$ ±20%). H3: $L$↑ raises $\tau_{BT}$ linearly (±10%, constant-pattern). H4: $T_{ads}$↑ cuts $q_{dyn}$ (van 't Hoff $b(T)$ confirmed). H5: $v_{sh}$ matches R–H when NTU>5 (±15%).

**Validation gates — clear in order, never skip.** Gate A: linear-solver mass-balance error <1%, against the Klinkenberg analytical solution (Week 4). Gate B: simulated front velocity within tolerance of R–H. Gate C: simulated $\tau_{BT}$ within ±20% of Stampi-Bombelli 2024 (Week 6).

> **Discrepancy flagged (see §8):** the Gate-B tolerance is **±15%** in DERIV §E and SPEC, but **±10%** in ROADMAP and the updates log. Resolve before writing §5. Recommendation: adopt **±15%** as the pass threshold (consistent with the report spec and DERIV) and report ±10% as a stretch target.

**Asymmetry index — the model-selection trigger (creative synthesis).** REACT §Stage 2 sets the DK-escalation rule informally ("tail 95→99% exceeds 4× the 5→50% rise"). Formalise it as a single measurable from any breakthrough curve:

$$\mathcal{A} = \frac{\tau_{95}-\tau_{50}}{\tau_{50}-\tau_{5}}$$

A symmetric logistic (Bohart–Adams/Thomas/YN) gives $\mathcal{A}=1$. Cabrera-Codony et al. (2026) report a 50→95 vs 5→50 ratio of **5.4** for PEI–fumed silica. Decision rule for the report: $\mathcal{A}\lesssim 2$ → PFO sufficient; $\mathcal{A}\gtrsim 3\text{–}4$ → escalate to dual-kinetic, fitting η to the first 70% of the curve and $k_{s,amine}$ to the tail. This ties H5 and the §5.3 model-selection question to one number the experiment directly yields.

**DOE matrix** (SPEC) — OAT, 9 runs (1 baseline + 2 levels × 4 parameters): $u$ {0.05/0.10/0.20 m/s}, $C_{in}$ {200/400/800 ppm}, $L$ {0.10/0.15/0.20 m}, $T_{ads}$ {15/25/40 °C}. Acceptance per SOP §5.1: baseline ≤10 ppm; inlet within ±2%; outlet flow within ±5%.

---

## 8. Discrepancy and placeholder register

Research-mode output: every conflict and gap, surfaced — to be resolved before final submission, not silently.

**Conflicts to resolve**

1. **Gate-B tolerance: ±10% vs ±15%.** ROADMAP/updates say 10%; DERIV §E and SPEC say 15%. → Adopt ±15%; note ±10% as stretch.
2. **Myers & Font (2020) citation is inconsistent.** Cited as *Int. J. Heat Mass Transfer* 163:120374 (REACT) and as arXiv:2009.08902, title "Mass transfer from a fluid flowing through a porous media" (MATHGUIDE); SPEC's placeholder title differs again. The article number 120374 also appears for Bos et al. (2019) *Chem. Eng. J.* 377 — a suspicious collision. → Retrieve and verify the primary citation before §3.4.4. *(This is the "suspected Myers & Font typo" carried in the project's open-issues list — still open.)*
3. **`derivation.md` is out of scope.** It still closes on **Langmuir** (§1.5/§2.5) and uses regeneration framing (purge, $T_{regen}$, $Q_{wall}$). The project pivoted to Toth + adsorption breakthrough. → Rewrite §1.5/§2.5 to the Toth closure of §4.3; reframe BC/IC to clean-bed + step $C_{in}$.
4. **Wall term: adiabatic vs not.** The updates log sets $Q_{wall}=0$ (adiabatic); Shafeeyan and MATHGUIDE state lab columns need the wall term. For an 8.2 mm ID column it is almost certainly significant. → Keep $\mathrm{Bi}_w$ as a switch, default ON for the SUTD rig; use adiabatic only as a screening case.
5. **$\delta_1$ defined two ways.** REACT: $\delta_1=Lk_q/u_0\approx0.027$. PEIMODEL: $\delta_1=c_{1,0}/((1-\varepsilon)\rho_p q_0^*)\sim10^{-5}$. → Pin one definition in the nomenclature; they are different groups with the same label.
6. **ΔH₀ = 210 kJ/mol (Toth Set B)** sits far above the 60–90 kJ/mol chemisorption range (MATHGUIDE §D2). → Cross-check the Pang 2024 value before using Set B quantitatively.
7. **LDF driving-force form.** LIT-J writes the sink on solid loading $(q^*-\bar q)$; DERIV writes it on gas concentration $(C-C^*)$. Equivalent, but coefficients differ. → Standardise on the solid-loading form $\partial_t\bar q=k(q^*-\bar q)$ (used by all modelling papers and by PEIMODEL).
8. **Particle vs bed porosity.** Keep $\varepsilon$ (bed voidage ≈0.40) and $\varepsilon_p$ (particle porosity ≈0.71 for γ-alumina) strictly distinct; the draft and one MATHGUIDE sentence conflate them.

**Placeholders — values the report must mark, not invent**

- Column length $L$ — `[INSERT: from SOP; currently "length of …" left blank]`
- PEI@SiO₂-specific Toth parameters — `[INSERT: pending project equilibrium-isotherm measurement; use A–B bracket meanwhile]`
- Sorbent mass and packed bed length per run — `[INSERT: from pre-run weighing log]`
- Preliminary calibration baseline, purge time, stable inlet concentration — `[INSERT: from first commissioning runs]`
- Project budget line items — `[INSERT: from procurement record]`

---

## 9. Bird's-eye progress snapshot — drop-in for biweekly journal (18 May)

A factual status summary, suitable for pasting into the 18 May journal. Every line is grounded; nothing is projected.

**Literature.** Seven-paper synthesis complete across the molecular→particle→process scale ladder. Two thematic reviews finished (`…Reaction_Models…`, `…Mathematical_Reading_Guide`) and a 9-paper critical survey of empirical breakthrough models (`lit_survey_summaries.md`). Settled findings: Toth + PFO-LDF is the correct baseline; Bohart–Adams/Thomas/Yoon–Nelson are one logistic curve and must not be primary benchmarks; the dual-kinetic split is needed only on a measured tail. Still partial: data-analysis methods; R–H/travelling-wave reading (Myers & Font); MOL/stiff-ODE theory.

**Mathematics.** Full governing system formalised and term-by-term justified in `derivation.md` (six relations, two energy balances, seven dimensionless groups). Outstanding: `derivation.md` still closes on Langmuir and carries regeneration framing — flagged for Toth rewrite (§8). The closure value $\alpha=0.11$ (Toth heterogeneity slope) is now recovered from the reading guide, clearing a long-standing gap.

**Model.** A proposed novel result is on the table: a hybrid dual-kinetic travelling-wave breakthrough expression (`CO2_Adsorption_Breakthrough_Model_PEI_SiO2.md`) that folds amine dual-site kinetics into the Myers–Font analytical reduction. Status: candidate result with a leading-order proof; numerical confirmation against the MOL solver not yet done.

**Solver.** MOL scaffold in progress (BDF/LSODA, upwind finite-volume). No validation gate cleared yet; Gate A (Klinkenberg linear benchmark) is the immediate target.

**Experiment.** SOP drafted for the SUTD 8.2 mm packed-bed rig (PEI@SiO₂, ~10 g); valve protocol, data-recording table and validity criteria defined. Wet-rig breakthrough experiments are now formally **in scope** as the final empirical validation layer. Column length and first calibration data still to be recorded.

**This fortnight's key learning.** A breakthrough curve carries three separable signatures — MTZ width (NTU), S-curve shape (Pe), thermal feedback (Λ) — and the parametric study is best read as motion across a dimensionless (Pe, NTU) regime map rather than as raw curves. Toth isotherm form and its fitted parameters are inseparable: a Langmuir fit to Toth data gives the wrong wave speed.

---

## 10. Immediate next actions

Ordered; each closes a §8 item or unblocks a report section.

1. Retrieve and verify the **Myers & Font (2020)** primary citation — unblocks §3.4.4 and the reference list.
2. Rewrite `derivation.md` §1.5/§2.5: **Langmuir → Toth**; reframe BC/IC to clean-bed + step $C_{in}$ — unblocks report §5.
3. Fix the **Gate-B tolerance** at ±15% in `study_plan.md` and all downstream files.
4. Insert column length $L$ into the SOP and propagate to the DOE and the model.
5. Clear **Gate A** — Klinkenberg linear benchmark, target mass-balance error <1%.
6. Run the solver with **both Toth sets A and B**; report the predicted-$\tau_{BT}$ bracket.
7. Draft report §1–§3 against the §6 build plan; mark every `[PLACEHOLDER]`.

---

*End of design file. Every claim traces to a source in §1. Conflicts are flagged in §8, not resolved by assumption. Ready to drive the Interim Report draft and the 18 May biweekly journal entry.*
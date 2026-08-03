# Stage 3 — Simulated Peer Review Panel

**Manuscript** T32_PI05 — *Parametric Study of CO₂ Adsorption Breakthrough in Packed-Bed
Columns* · ~9,400 words
**Target venue (assumed for calibration)** *Adsorption Science & Technology*
**Panel** Journal-Fit Reviewer + 3 peer reviewers + Devil's Advocate, reviewing
independently
**Input** `_source/report-extracted.md`, with `00-integrity-report.md` attached per the
Stage 2.5 → 3 handoff

> **Calibration note.** This is a Year-3 undergraduate design project being read against
> journal standards, at your request. That is a deliberately harsh lens and the scores
> below reflect it. Judged as coursework the document is in considerably better shape than
> the recommendation suggests — the experimental work is real, the data is genuinely
> reproducible, and the analytical core is correct. What is missing is finish and
> bookkeeping, not competence.

---

## Reviewer Configuration Cards (Phase 0)

| Seat | Identity | Focus |
|---|---|---|
| Journal-Fit | Adsorption process engineer, fixed-bed separations | Venue fit, originality, completeness |
| R1 Methodology | Experimental adsorption / statistical model discrimination | Design, statistical validity, reproducibility |
| R2 Domain | Breakthrough-model theorist | Literature coverage, theoretical framing |
| R3 Perspective | CO₂ capture process / techno-economics | Cross-disciplinary relevance, practical impact |
| Devil's Advocate | — | Core argument, logical fallacies, strongest counter-case |

---

## Reviewer 0 — Journal-Fit

**Recommendation: Reject (resubmit after completion).** Confidence 5/5.

The manuscript is **incomplete in its central section**. §4 "Fitting performance and
analysis" — the section that would carry the paper's contribution — is an empty heading.
The Conclusions nonetheless assert *"a comparative analysis of breakthrough models"* and
call the document *"this interim report"*. A journal cannot evaluate a contribution that
has not been written.

**Strengths.** S1: A real, self-collected 3×3 flow×concentration breakthrough dataset on
PEI@SiO₂ granules — genuinely useful, and the kind of systematic sweep the literature is
short of. S2: The BA/Thomas/YN equivalence derivation `[p876-881]` is correct and cleanly
argued. S3: The SOP §6 is unusually thorough and would be reusable by another lab. S4: The
analysis is **computationally reproducible** — I re-ran it in a clean environment and
recovered the committed numbers to 1e-9.

**Weaknesses.** W1: §4 empty. W2: Citation integrity — 26% of in-text citations resolve.
W3: An AI chatbot cited as a source. W4: The paper motivates DAC at ~400 ppm and measures
5–15% CO₂ without acknowledging the gap.

**Venue fit.** The topic fits *Adsorption Science & Technology* well. The framing does not
yet: five indoor-air-quality health references and six orphaned DAC techno-economics papers
suggest a different readership. Reframe around fixed-bed adsorption performance.

---

## Reviewer 1 — Methodology

**Recommendation: Major revision.** Confidence 4/5.

**S1.** The experimental design is sound: a full 3×3 factorial in flow (0.05/0.10/0.15 lpm)
and concentration (5/10/15%) is the right structure for a parametric study, and both
factors are swept independently.

**S2.** Reproducibility is the manuscript's strongest and most under-sold asset. Re-running
`new_runs_pipeline.py` in a fresh environment (numpy 2.5.1, scipy 1.18.0) reproduced the
committed results across 9 runs × 24 models with two values differing at the ninth
significant figure. **Say this in the paper.** Most submissions cannot make this claim.

**W1 — no replication, no uncertainty.** Each of the nine cells is a single run. No
repeats, no error bars, no confidence intervals on any fitted parameter, despite the fitter
computing standard errors and writing them to CSV. With n=1 per cell, the non-monotonic
equilibrium times in §8 `[p1204]` cannot be distinguished from run-to-run variability.
**This is the most important methodological gap.** At minimum, report the fitted parameter
standard errors you already have; ideally, replicate two or three cells.

**W2 — uncontrolled temperature.** `CLAUDE.md` records ambient, uncontrolled T; the runs
span 2026-06-26 to 2026-07-15. Adsorption equilibrium is strongly temperature-dependent, so
temperature is an uncontrolled covariate confounded with run date. Must be stated as a
limitation.

**W3 — model selection without a stated criterion.** Twenty-four models are fitted and
AICc, Adj. R², RMSE and F-tests are all computed, but §4 does not exist so no selection
rule is stated. Related: two models (M18/M19 Chern–Chien) report `converged = True` while
returning NaN R² and infinite RSS.

**W4 — a derived quantity is reported as measured.** Table 3's interstitial velocity uses a
floored ε = 0.30 that the project's own documentation forbids treating as physical.

**W5 — two excluded files.** Two `newest runs/` CSVs are excluded for missing metadata. The
exclusion is correct and honest, but the paper never mentions it. Report N excluded and why.

---

## Reviewer 2 — Domain

**Recommendation: Major revision.** Confidence 5/5.

**S1.** §3.4's treatment of the classical family is accurate, and the decision to show the
equivalence explicitly rather than fit three models and report three "different" results is
exactly right — it is the error Hu (2020) was written to correct.

**W1 — the review covers seven models; the analysis fits twenty-four.** Wolborska,
Klinkenberg, dose-response, Gompertz, log-normal, Dima, Chern–Chien, n-order BA and the
entire fractal-like family appear in results with no equation, no parameter definition and
no citation. The models that produce your best fits are the ones never introduced.

**W2 — every classical primary source is missing.** Bohart & Adams (1920), Thomas (1944),
Yoon & Nelson (1984), Clark (1987), Langmuir (1918), Toth (1971), Wolborska (1989). A
review of century-old models citing none of them reads as assembled from secondary reviews.

**W3 — a source's conclusion is reversed.** Kimani et al. is reported as showing Weibull
outperforming normal and Gompertz; the paper actually concludes only log-Gompertz fitted
satisfactorily, and that fractal-like Bohart–Adams fitted best. The correction *helps* the
manuscript, since Kimani then corroborates its own fractal-like result.

**W4 — Wolborska is fitted but never discussed**, though Hu (2020) — the manuscript's most
used source — explicitly recommends against its use.

**W5 — single-group over-reliance.** Six papers from the Hu group carry §3.4 and §3.5. Two
listed Hu papers (2022 multicomponent, 2023 aqueous isotherms) are off-topic and uncited.

**W6 — aqueous-phase evidence base.** Every empirical model is validated in the literature
on liquid-phase systems. The transfer to gas-phase CO₂ at 5–15% should be argued, not
assumed.

---

## Reviewer 3 — Perspective

**Recommendation: Major revision.** Confidence 3/5.

**S1.** A parametric breakthrough dataset at post-combustion-relevant concentrations on a
PEI@SiO₂ system is practically useful and under-supplied in the literature.

**W1 — the paper does not know which application it serves.** §1 and §3.5 motivate indoor
air quality and DAC; §5.1 opens *"In DAC processes, a trace level of CO₂"*; §7 states the
work *"simulates post-combustion carbon capture"*. These are different technologies with
different sorbents, concentrations, economics and regeneration strategies. A reader cannot
tell what problem is being solved.

**W2 — the benchmark is used outside its range.** Stampi-Bombelli (2024) characterises
amine-functionalised γ-alumina for DAC at ~400 ppm. Importing its parameters into a 15% CO₂
study is an extrapolation across two-and-a-half orders of magnitude, unacknowledged.

**W3 — no performance interpretation.** q_dyn, L_MTZ and ψ are computed by the pipeline but
none reach the manuscript's analysis. §8 discusses only breakthrough and equilibrium times.
The engineering question — how much CO₂ per kg of sorbent, and how much bed is wasted —
goes unanswered.

**W4 — no comparison to literature capacities.** Without it, a reader cannot tell whether
0.55–0.89 mol/kg is good.

---

## Devil's Advocate

**Strongest counter-argument against the paper as it stands.**

The manuscript's implicit claim is that fitting twenty-four breakthrough models to nine
curves and ranking them by AICc tells us something about CO₂ adsorption in this column. It
may not.

§3.4.4 proves — correctly — that Bohart–Adams, Thomas and Yoon–Nelson are the *same
function*, and then argues at `[p884-885]` that logistic, error and Gudermannian kernels are
*mutually indistinguishable within sensor noise*. Taken together, the manuscript
establishes that most of its model set is degenerate. The natural conclusion is that
**model ranking on a single noisy curve is not identifiable** — that AICc differences among
models within noise of each other are not evidence about physics.

The results support this worry. `CLAUDE.md` records M11 winning runs 3 and 5, M14 winning
run 4, M10 winning runs 6 and 8 — the "best model" changes run to run with no physical
account of why. If the underlying mechanism is constant across a flow/concentration sweep,
the best-fitting model should not keep changing. That pattern is what noise-driven
selection looks like.

**CRITICAL-1.** The paper proves its models are degenerate, then ranks them anyway. §4 must
address identifiability directly: report AICc differences *with* a threshold below which
models are indistinguishable, and treat the M10/M11/M14 alternation as evidence about
discriminating power rather than about physics.

**CRITICAL-2.** The one claim that could rescue selection — that fractal-like models capture
real asymmetry — rests on `(ChatGPT, n.d.)` for its noise argument and on a misquoted
Kimani for its literature support. Both pillars need rebuilding.

**CRITICAL-3.** The paper cannot simultaneously hold that (a) the classical trio is one
model and (b) it has compared "24 models". The honest count is far smaller: several exact
duplicates (M14 ≡ M15 numerically identical in every run), one three-way identity, two
non-converging, and several within-noise equivalents.

**MAJOR-1.** With n=1 per cell and no error bars, no parametric trend in the paper is
distinguishable from noise.

**MAJOR-2.** ψ, q_dyn and L_MTZ are computed and discarded.

**Ignored alternative explanation.** Non-monotonic equilibrium times are attributed to
nothing. Ambient temperature drift over a three-week campaign is the obvious candidate and
is never considered.

**Observations (non-defects).** The equivalence derivation is correct. The reproducibility
is real. The exclusion of the two unlabelled sensor logs is exactly right and should be
stated with pride rather than omitted. The honest reporting of non-monotonic t_E is a mark
of integrity — do not remove it under review pressure.

---

## Editorial Decision

**Decision: Major Revision** (Journal-Fit's Reject is recorded as a minority position; the
panel majority holds that the gaps are completion gaps, not competence gaps).

### Top blocking issues

1. **§4 is empty.** The paper's contribution is unwritten. Nothing else can be assessed
   until it exists. *(Author-owned; noted as known.)*
2. **Citation integrity.** 26% resolution rate; an AI chatbot cited as a source; a source's
   conclusion reversed.
3. **Identifiability.** The paper proves its model set is degenerate, then ranks it. §4 must
   confront this.
4. **Scope contradiction.** DAC motivation, post-combustion experiment, DAC-premised model.

### Required revisions

**R1 — Complete §4.** Report fit statistics with a stated selection criterion, parameter
values *with the standard errors already computed*, and an explicit identifiability
discussion covering the M10/M11/M14 alternation.
*Acceptance criteria:* a selection rule is stated; AICc differences carry an
indistinguishability threshold; degenerate models are identified as such.

**R2 — Repair citations.** Add Hu 2024, Hu 2019, Kimani, Clark 1987; fix `Khim`→Chu and
`Alba`→Cabrera-Codony; remove the ChatGPT citation and source the noise claim properly;
correct the Kimani characterisation; add the missing primaries.
*Acceptance criteria:* every in-text citation resolves; no non-scholarly sources; no
orphaned entries.

**R3 — Resolve scope.** Reframe around the concentration range actually studied; state the
Stampi-Bombelli extrapolation explicitly.
*Acceptance criteria:* §1, §5.1 and §7 describe the same application.

**R4 — Introduce every fitted model** in §3.4 with equation, parameters and citation, or
reduce the model set.
*Acceptance criteria:* no model appears in a results table without a §3.4 entry.

**R5 — Report uncertainty.** Parameter standard errors; state n=1 per cell and uncontrolled
temperature as limitations; report the two excluded files.

**R6 — Fix structure.** Reorder so method precedes results; renumber §6 and §9's children;
resolve duplicate 2.2/3.3 and duplicate Table 1/Table 2; repair the broken §3 heading;
delete the stray "Done"; clear the twelve Word comments; correct "interim report".

**R7 — Notation.** Add a nomenclature table; resolve the `k_T` triple collision; replace δ
with ∂; repair the Danckwerts BC; fix the flow-rate units in both Table 2s.

**R8 — Report performance metrics.** Bring q_dyn, L_MTZ and ψ into the analysis and compare
capacity against literature values.

### Suggested (non-blocking)

- State the reproducibility result explicitly — it is a real strength.
- Add a gas-phase modelling anchor (Wheeler–Jonas) alongside the aqueous-derived models.
- Acknowledge the published Comment/Rebuttal exchange on Chu (2020).
- Offer a mechanism for the non-monotonic t_E.

### Revision roadmap

**Priority 1 — structural.** R1 (§4), R3 (scope), R6 (order and numbering).
**Priority 2 — content.** R2 (citations), R4 (model coverage), R5 (uncertainty), R8 (metrics).
**Priority 3 — text and formatting.** R7 (notation), suggested items.

### Dimension scores (0–10, journal calibration)

| Dimension | R0 | R1 | R2 | R3 | DA |
|---|---|---|---|---|---|
| Originality | 5 | 5 | 4 | 5 | 4 |
| Methodological rigour | 3 | 4 | — | — | 3 |
| Literature coverage | 3 | — | 2 | 4 | — |
| Clarity / structure | 3 | 4 | 4 | 3 | 3 |
| Evidence–claim support | 2 | 3 | 2 | 3 | 2 |
| Reproducibility | 8 | 9 | — | — | 8 |
| **Completeness** | **2** | **3** | **3** | **3** | **2** |

Reproducibility is the outlier in the right direction, and it is the one dimension the
manuscript currently does not claim for itself.

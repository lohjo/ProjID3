# Response to Reviewers — skeleton

> **Status 2026-08-04:** superseded by the completed resolution — every item this skeleton
> was drafted to track is now `RESOLVED` in `T32_PI05_Final_Report.docx` except the B9/B10
> process items (reference re-verification of the pre-existing set; plagiarism screening),
> which remain open and are documented in `09-final-integrity.md` and
> `11-process-record.md`.

**Status** drafting aid, not a submission. Statuses are `RESOLVED` /
`DELIBERATE_LIMITATION` / `UNRESOLVABLE` / `REVIEWER_DISAGREE`, filled in as you work
through `06-change-list.md`.

---

# Part A — Your supervisor's three comments

These are real comments from a real reviewer, and they take precedence over anything the
simulated panel produced.

## A1 — Understand what each model's parameters *do*

> *"focus on understanding what each model's parameters do / how they vary with flow rate
> and concentration (i.e. `k` in BA/Thomas/YN model; how is `k` affected?)"* — ref
> `hu2020-1.md`

**Status:** `PENDING` — belongs in the unwritten §4.

**What the reference gives you.** Hu, Xie & Zhang (2020) is unusually well suited to this
question because it answers it analytically rather than empirically:

| Result | Source | What it means for your sweep |
|---|---|---|
| `k_YN = k_BA·c₀ = k_T·c₀` | Hu 2020 §2 | The three rate constants are **one parameter in three scalings**. Fitting all three and tabulating them separately reports the same number three times |
| `τ = a₀x/uc₀ = q₀m/vc₀` | Hu 2020 §2 | `τ` is the time to **50% breakthrough** — a physically interpretable quantity, not a fitting artefact |
| `k` is the **shape** parameter; `τ` is the **location** parameter | Hu 2020, Fig. 4 | Separates *how steep* the front is from *when* it arrives — exactly the flow/concentration split you are after |
| `μ_max = k_YN/4`, `λ = τ − 2/k_YN` | Hu 2020 Table 2 | Maximum specific breakthrough rate and lag time, both computable from your existing fits with no re-fitting |
| Rate profile is Gaussian about `t = τ`; height rises and width falls as `k_YN` rises | Hu 2020, Fig. 4 | Gives you a predicted *shape* to test against your data |

**Concrete steps.**

1. Because `k_YN = k_BA c₀ = k_T c₀`, plot **`k_YN` alone** against flow and against `c₀`.
   Reporting `k_BA` and `k_T` separately adds nothing — and saying so demonstrates you
   understand the equivalence you proved in §3.4.4.
2. Predict, then check. `τ = q₀m/(v c₀)` implies `τ ∝ 1/v` at fixed `c₀` and `τ ∝ 1/c₀` at
   fixed `v`. Your 3×3 grid tests both directly. Plot `τ` vs `1/v` and `τ` vs `1/c₀` and
   look for the straight lines.
3. `k_YN` should rise with `c₀` if the driving force controls uptake. Report the trend and
   say whether it holds.
4. Add `μ_max` and `λ` — both derive from parameters you already have.
5. For the fractal models, `h` is the parameter that carries the asymmetry. Its trend
   across the sweep is the physically interesting result, and it is the one your
   supervisor's `h` annotation was pointing at.

**Data already available.** `experimental-results.md` §6 has the flow sweep (runs 4/5/6),
the concentration effect (runs 3/5/8), and a fractal-exponent `h` trend. §6.3 is the
starting point.

**Caution.** `01-reviewer-panel.md` records the Devil's Advocate challenge that with n = 1
per cell and no error bars, a parameter trend may not be distinguishable from noise. Report
the standard errors that `fit.py` already computes so the trends carry uncertainty.

## A2 — Mathematical modelling is supplementary

> *"the mathematical modelling section will supplement as an extra reading section (not in
> scope for design project; will extend to final year project), however the model so far
> looks fine"*

**Status:** `RESOLVED (scope accepted)`.

Accepted, and the audit was scoped accordingly — `04-math-consistency.md` proposes **no
changes to the physics**. §5.1 is a well-posed minimal model with assumptions stated up
front, and I agree it is sound.

Two things still worth doing, both cheap, because a supplementary section is read by
someone meeting it cold:

- **Say it is supplementary.** As printed, §5 arrives between an empty results section and
  the SOP, with `??` parameters and no downstream use — it reads as a non-sequitur rather
  than as deliberate groundwork. One opening paragraph fixes this (change-list 1.1, and
  `05-methodology-flow.md` F10).
- **Fix the notation, not the model.** The `k_T` triple collision (3.2), δ-for-∂ (3.3), the
  malformed Danckwerts BC (3.4), and the flow-rate units (3.5) are all typography-level and
  none touch the derivation.

The one item that is arguably physics: assumption A2 says isothermal, but Eq. (5) carries a
van 't Hoff `b(T)` and the BCs include temperature conditions (3.7). Since the model is
staying, flag those as FYP hooks rather than deleting them.

## A3 — No statistics inside figures

> *"for figures, there should be no statistics (i.e. h=.., F-test p=..) in the figure
> generated; will insert in presentation deck (remove for now)"*

**Status:** `RESOLVED — applied and verified.`

Removed from `plots.py` (P1, P2, P4, P6, P7), `cross_run_figs.py` (fig10, fig11, fig12) and
the notebook mirror. The `h = … F-test p = …` text box you named specifically is gone, along
with R² legend labels and χ²_red panel titles. The now-dead `f_p_ba_vs_fractal` parameter
and its two call-site extractions were removed with it.

Statistics still go to the CSVs and stdout, so the presentation deck loses nothing.
Verified: numerics identical to baseline across all runs; P6 regenerated and visually
inspected.

**One judgement call for you.** `fig10_model_ranking` is a bar chart *of* mean R², so R²
is its plotted variable and the axis label was kept — removing it would leave an unlabelled
axis. Every annotation was still stripped. Say the word if you want it gone too.

---

# Part B — Simulated panel

Decision: **Major Revision.** Full detail in `01-reviewer-panel.md`; edits in
`06-change-list.md`.

| Item | Concern | Status | Where |
|---|---|---|---|
| R1 | §4 empty — the contribution is unwritten | `PENDING` | yours |
| R2 | Citation integrity: 26% resolution; ChatGPT cited; a source's conclusion reversed | `PENDING` | 2.1–2.13 |
| R3 | DAC motivation vs 5–15% experiment | `PENDING` | 1.11–1.13 |
| R4 | 24 models fitted, 7 introduced | `PENDING` | 2.14–2.15 |
| R5 | No uncertainty reported; n=1 per cell | `PENDING` | 2.17–2.19 |
| R6 | Structure, ordering, numbering | `PENDING` | 1.1–1.10 |
| R7 | Notation, units | `PENDING` | 3.1–3.17 |
| R8 | q_dyn / L_MTZ / ψ computed but unused | `PENDING` | 2.20 |

## Suggested framings for the hard ones

**On identifiability (Devil's Advocate CRITICAL-1).** The strongest objection raised: the
paper proves BA ≡ Thomas ≡ YN and argues the three sigmoid kernels are indistinguishable
within noise — then ranks 24 models by AICc anyway, with the winner changing run to run.

Don't defend the ranking. **Own it as a finding.** Something like:

> Because several members of the model set are mathematically identical (M01 ≡ Thomas ≡ YN;
> M14 ≡ M15 numerically in every run) or lie within sensor noise of one another, AICc
> differences below a threshold of Δ ≈ 2 are not treated as evidence of mechanism. The
> models that separate meaningfully from the classical family are the fractal-like ones,
> whose advantage exceeds this threshold in every run; the alternation among M10, M11 and
> M14 within that family reflects the limited discriminating power of a single breakthrough
> curve rather than a change in mechanism.

That answers the objection, is true, and is a more sophisticated result than a ranking table.

**On scope (R3).** Do not claim DAC relevance. Your data is a clean post-combustion-relevant
sweep, which is a defensible contribution on its own. Reframing is honest and cheap; running
a 400 ppm campaign before the deadline is not.

**On Kimani (2.4).** The correction helps you. Kimani independently found fractal-like
Bohart–Adams to be the best performer, which is external corroboration of your own result.
Quoting it correctly strengthens §3.5.2 and §8.

---

# Part C — Things worth defending

Not everything flagged needs changing. These are strengths that should be *more* visible.

1. **Reproducibility.** Verified by execution: 9 runs × 24 models × 16 columns reproduced
   in a fresh environment with two values differing at the ninth significant figure. Claim
   this explicitly in the Python section.
2. **The two excluded files.** Excluding the unlabelled sensor logs rather than inventing
   geometry is exactly right. Report it as a decision, with the reason.
3. **Non-monotonic equilibrium times `[p1204]`.** The most scientifically mature paragraph
   in the report. Do not soften it under review pressure — add a candidate mechanism instead.
4. **No synthetic data leakage.** Checked: `experimental-results.md`'s placeholder Appendix A
   does not appear anywhere in the report's results. Worth knowing nothing needs fixing here.
5. **The equivalence derivation `[p876-881]`.** Correct, independently checked. It needs a
   citation for priority, not a correction.

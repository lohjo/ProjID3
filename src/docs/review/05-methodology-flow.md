# Methodology and Logical Flow Audit

> **Status 2026-08-04:** the structural/ordering findings below were resolved by the full
> chapter reorder in `T32_PI05_Final_Report.docx` (SOP → Results → Analysis →
> Fitting-performance → Math Modelling → Conclusions). See `11-process-record.md`. This
> file is retained unmodified as the original audit record.

**Questions asked** Is every transition justified? Does each section depend on the
previous one? Are there logical jumps? Does any result appear before the method that
generated it?

---

## The document's actual order

| Order | Heading as printed | Words | Numbering |
|---|---|---|---|
| 1 | Abstract | 124 | — |
| 2 | 1 Introduction | 684 | ✓ |
| 3 | 2 Project Outline and Objectives | 643 | `2.2` used **twice** |
| 4 | 3 Literature review | 2 976 | `3.3` used **twice**; one H2 untitled |
| 5 | **4 Fitting performance and analysis** | **0 — empty** | ✓ |
| 6 | 5 Mathematical Modelling | 515 | ✓ |
| 7 | **6. Standard Operating Procedure** | 1 729 | children numbered **4.1–4.5** |
| 8 | 7. Experimental Results | 299 | ✓ |
| 9 | 8. Experimental Analysis | 262 | ✓ |
| 10 | 9 Conclusions | 110 | child is **`7.1 Next Steps`** |
| 11 | 10 References | 891 | ✓ |

---

## F1 — A results section precedes the method that produced the results (CRITICAL)

**§4 "Fitting performance and analysis" sits at position 5. The SOP that generated the
data sits at position 7. The data itself appears at position 8.**

This is the direct answer to *"does any result appear before the method that generated
it?"* — structurally, yes. §4 is currently empty, which masks the problem, but it is the
section you have flagged as still to write (goodness-of-fit & error statistics, optimal
model). The moment you fill it, the report will present fit statistics roughly 2,300 words
before the reader learns how the experiment was run or what the measurements were.

**Fix — reorder to:** Introduction → Objectives → Literature review → **SOP/Method** →
**Experimental Results** → **Fitting performance and analysis** → **Mathematical
modelling (supplementary)** → Conclusions.

This costs nothing but cut-and-paste and fixes F2, F3 and F4 simultaneously. It is the
highest-leverage structural change available.

## F2 — Section 6 carries section 4's numbering (CRITICAL)

§6 is titled *"6. Standard Operating Procedure"* and every child is numbered `4.1`
Apparatus → `4.2` Experimental Procedure → `4.3` After the Run → `4.4` Data to Record →
`4.5` Safety Notes.

An un-renumbered paste from an earlier draft in which the SOP *was* §4 — which is
corroborating evidence that the SOP was originally positioned before §5, i.e. that F1's
recommended order is the one the document originally had. Within it, **`4.2.3` Feed Gas
Preparation is printed before `4.2.2` Column Loading and Purge**, so the procedure is also
out of execution order.

## F3 — Conclusions contains a subsection numbered from a different chapter

§9 Conclusions `[p1214]` → child `7.1 Next Steps` `[p1216]`. Same cause as F2.

## F4 — Duplicate numbering in two places

`2.2 Project Objectives` and `2.2 Project Schedule`; `3.3 Packed-bed adsorption and
breakthrough behaviour` and `3.3 Adsorption Isotherms`. With no `SEQ`/`REF` fields anywhere
in the document, nothing renumbers automatically and no in-text pointer can be trusted.

## F5 — A heading is three concatenated fragments

`[p745]`, the first H2 under §3, reads:

> `Experimental dataBreakthrough curve vs. Breakthrough model typesApplication scopeAdsorption principlesBreakthrough…`

A planning list that was styled as a heading and never resolved. It is the **first thing a
reader meets in the literature review.** There is also a stray `Heading 8` reading `Done`
at `[p735]`, and twelve unresolved Word comments — most still the original assignment
boilerplate (*"Describe the problem or opportunity identified…"*, *"Plan the project
development schedule, for example using a Gannt chart."*).

---

## F6 — The motivation and the experiment describe different problems (MAJOR)

You asked for this to be treated as a major finding. It is.

**What the paper motivates.** §1 and §3.5 frame the work around indoor air quality and
direct air capture: five references on CO₂ and human health `[p92]`, Singapore emissions
`[p94-95]`, DAC technology `[p96]`, C3 films for *"distributed direct air capture in urban
spaces"* `[p101]`. §5.1 opens `[p913]`: *"**In DAC processes, a trace level of CO₂**
adsorbed from an inert gas carrier…"*. The project's own Gate C targets a breakthrough
curve **at 400 ppm**.

**What the experiment measures.** 5%, 10% and 15% CO₂ — 50,000 to 150,000 ppm. The
committed run data confirms it: C₀ from 47,400 ppm to 150,630 ppm.

**That is a factor of 125 to 375 between the motivating regime and the measured regime.**
And §7 `[p1099]` says so outright, contradicting §5: *"This work simulates **post-combustion
carbon capture** scenarios."*

So the paper motivates DAC, assumes DAC in its model derivation, and measures
post-combustion. Three different framings in one document.

**Why it is material, not cosmetic.** Adsorption physics is not scale-invariant across that
range. At 400 ppm a supported-amine sorbent operates in the near-linear (Henry) region of
the isotherm, kinetics are film/external-diffusion limited, and thermal effects are
negligible. At 15% the isotherm is saturated, intraparticle diffusion dominates, and the
adsorption exotherm is significant — which is precisely why your §5 assumption A2
(isothermal) is defensible at 400 ppm and questionable at 150,000 ppm. Stampi-Bombelli et
al. (2024), your benchmark, is a **DAC study at ~400 ppm**; transferring its Toth
parameters to a 15% feed is an extrapolation the paper does not acknowledge.

**Recommended fix — reframe around what you actually measured.** Your data is a clean,
well-executed 3×3 post-combustion-relevant sweep. That is a defensible contribution on its
own terms. Concretely:

1. Reframe §1 around point-source / post-combustion capture, keeping **two** IAQ references
   at most as broader context.
2. Change §5.1's opening from *"In DAC processes, a trace level of CO₂"* to the
   concentration range actually studied, and re-examine A2 in that light.
3. Keep Stampi-Bombelli as a sorbent and method benchmark, but state explicitly that its
   parameters were determined at ~400 ppm and that the present work operates outside that
   range.
4. Note the 400 ppm Gate C as future validation work rather than as this paper's target.

The alternative — running a 400 ppm campaign — is not realistic before the deadline. The
reframing is, and it makes the paper honest rather than weaker.

---

## F7 — Two experimental campaigns presented as one dataset (MAJOR)

§7 puts **Table 3** (runs 3, 4, 5, 6, 8 — the `new runs/` campaign) directly above
**Table 4** (runs 1–9, the 3×3 grid from the `newest runs/` campaign, dated 2026-06-26 to
2026-07-15). Same caption style, adjacent, incompatible run numbering, no statement that
they are different campaigns.

A reader will assume "run 3" is the same experiment in both tables. It is not. §8's analysis
then draws exclusively on Table 4's numbers without saying which campaign it is discussing.

**Fix:** one sentence naming the two campaigns, their dates, and why both are reported —
plus a consistent run-ID scheme. `experimental-results.md` §1–9 and §10 already document
them separately; the report just needs to carry that distinction across.

## F8 — §8 draws a conclusion its data does not support

`[p1204]`: *"The equilibrium times showed greater variability and did not follow a perfectly
monotonic trend. At 5% CO₂, equilibrium time ranged from 108 to 125 then 110 min, while at
10% it varied from 146 to 64 and 58 min…"*

Reporting the non-monotonicity honestly is **good** — it is the most scientifically mature
paragraph in the report and should not be softened. But it is left as an observation with
no mechanism offered and no consequence drawn. At 10% CO₂ equilibrium time falls from 146
to 58 min — a 2.5× change — which is a large effect to note and move past.

Candidate explanations available to you: t_E is defined at C/C₀ = 0.95, which sits on the
flattest part of the curve and is therefore the least stable metric in your set; the
`newest runs/` campaign spans three weeks with ambient, uncontrolled temperature; sorbent
regeneration history differs between runs. Any of these is a legitimate paragraph. Leaving
it unexplained invites a reviewer to supply a less charitable explanation.

## F9 — §3.6 promises a procedure the report does not follow

`[p908-909]` describes the intended chain: review → rig assembly and calibration → SOP →
3×3 matrix → Python fitting → *"assess the influence of operating conditions on adsorption
performance"* → *"validate the suitability of the PEI@SiO₂ sorbent"*.

Steps 1–4 are delivered. Step 5 (fitting) is §4 — **empty**. Step 6 (influence of operating
conditions) is §8's 262 words on breakthrough and equilibrium times only — no fitted
parameters, no models. Step 7 (sorbent validation) is not attempted.

So §3.6 sets up a five-part argument and the document delivers two parts. This is the
clearest logical jump in the paper, and it is largely the gap you already know about.

## F10 — §5 arrives without a stated reason and exits without a consequence

§5 Mathematical Modelling appears between an empty results section and the SOP. Nothing in
§4 leads into it; §6 does not build on it; §7 and §8 never use it. Its parameters are
`??`, so it produces no numbers. §5.3 *"Limitations of the minimal kinetic model"* is 61
words.

Per your supervisor's comment this section is **supplementary reading, out of scope for the
design project, and extends to the FYP**. That is a perfectly good answer — but the
document has to *say* it. As printed, a reader hits an unmotivated model with unknown
parameters and no downstream use.

**Fix:** move §5 to an appendix or a clearly-marked forward-looking section, opening with
one paragraph that states it is groundwork for the FYP, is not used in this report's
analysis, and connects to `mechanistic-model.md`. Two sentences turn an apparent
non-sequitur into a deliberate scope statement.

## F11 — The Conclusions call this an interim report

`[p1215]`: *"**This interim report** provides a comparative analysis…"* — in a file named
`T32_PI05_Final_Report.docx`. §9 also claims *"a comparative analysis of breakthrough
models"*, which is the content of the empty §4. **The conclusion asserts a result the body
does not yet contain.**

---

## Transition-by-transition verdict

| Transition | Justified? |
|---|---|
| §1 → §2 | ✓ |
| §2 → §3 | ✓ |
| §3 → §4 | — §4 empty |
| §4 → §5 | ✗ F10 — no connective reasoning |
| §5 → §6 | ✗ F1 — method arrives after modelling |
| §6 → §7 | ✓ the report's strongest transition |
| §7 → §8 | ✓ |
| §8 → §9 | ✗ F11 — conclusions exceed the body |

---

## Priority

| # | Finding | Severity | Effort |
|---|---|---|---|
| F1 | Results section precedes its method | **Critical** | low — reorder |
| F6 | DAC motivation vs post-combustion experiment | **Critical** | medium — reframe §1/§5.1 |
| F2/F3/F4 | Numbering desync and duplicates | **Major** | low |
| F7 | Two campaigns conflated | **Major** | low |
| F9 | §3.6 promises five steps, delivers two | **Major** | blocked on your §4 |
| F10 | §5 unmotivated and unused | **Major** | low — one framing paragraph |
| F11 | Conclusions claim absent content | **Major** | low |
| F5 | Broken heading, stray "Done", 12 open comments | **Major** | trivial |
| F8 | Non-monotonic t_E noted but unexplained | **Moderate** | low |

F1, F2, F3, F4, F5 and F11 are together perhaps two hours of editing and would lift the
document's apparent finish more than any other change available.

# Stage 4.5 — Final Integrity Check

**Mode** 2 (final-check) · **Requirement** zero-issue PASS to enter Stage 5, with no escape
hatch (`academic-pipeline/SKILL.md:343`)

# Verdict: **FAIL**

This was predicted in the approved plan and is the correct outcome. It is **not** a
judgement that the work is bad — it is the arithmetic consequence of running a
completion gate against a manuscript with four deliberately unwritten sections. A PASS here
would have required either fabricating content or falsifying the gate.

---

## Why Mode 2 cannot pass

Mode 2 requires: fresh full re-verification of **all** references, 100% citation-context
checking, 100% claim verification, plagiarism screening at ≥50% coverage, and zero
MAJOR_DISTORTION and zero UNVERIFIABLE findings.

| Requirement | State |
|---|---|
| All references verified | **16 / 28.** Twelve context references unverified |
| Citation context 100% | Spot-check of 8 load-bearing claims only |
| Claim verification 100% | High-impact claims only |
| Plagiarism ≥50% | **Not run** |
| Zero MAJOR_DISTORTION | **1 open** — the Kimani misrepresentation |
| Zero UNVERIFIABLE | **1 open** — the ChatGPT-sourced claim |
| Manuscript complete | **No** — §4 empty; three further sections unwritten |

Six of seven criteria fail. Any one is blocking.

## Blocking list

| # | Issue | Owner | Closes when |
|---|---|---|---|
| B1 | §4 "Fitting performance and analysis" is empty | you | Section written |
| B2 | Mathematical modelling & prediction incomplete (deferred to FYP) | you | Written, or explicitly scoped as supplementary (change-list 1.1) |
| B3 | Python 3 reproducibility section absent | you | Written — evidence supplied in `06-change-list.md` |
| B4 | Optimal-model selection not done | you | Written, after the identifiability decision |
| B5 | `(ChatGPT, n.d.)` cited for a quantitative claim | you | 2.3 applied |
| B6 | Kimani's conclusion reversed — MAJOR_DISTORTION | you | 2.4 applied |
| B7 | 28 dangling citations, 12 orphans, 6 year-clashes | you | 2.1–2.13 applied |
| B8 | Non-physical ε-derived interstitial velocity published as measured | you | 3.6 applied |
| B9 | Twelve references unverified | re-run Phase A | Verification completed |
| B10 | Plagiarism screening not run | Phase D | Screening run |

---

## The 7-mode AI research failure checklist

Required at both integrity gates. `SUSPECTED` on any mode, or `INSUFFICIENT EVIDENCE` on
modes 1/3/5/6, blocks the pipeline.

| # | Mode | Finding |
|---|---|---|
| 1 | Fabricated sources | **CLEAR.** Every one of the 16 traced references is real. The dangling citations resolve to genuine papers that were never transferred into the list — a bookkeeping failure, not invention. This is the most important line in this report |
| 2 | Fabricated data | **CLEAR.** Table 4 matches the real `newest runs/` inventory; the placeholder Appendix A in `experimental-results.md` does not appear in the report. Verified by direct comparison |
| 3 | Overstated claims | **SUSPECTED.** §9 claims *"a comparative analysis of breakthrough models"* — content that lives in the empty §4. §3.6 promises five analysis steps and the document delivers two |
| 4 | Missing counter-evidence | **SUSPECTED.** Hu (2020)'s explicit recommendation against Wolborska is omitted while Wolborska is fitted. The published Comment/Rebuttal exchange on Chu (2020) is not acknowledged |
| 5 | Circular sourcing | **SUSPECTED.** Six papers from one research group carry §3.4–§3.5; classical models are cited only through those secondaries, never through their primaries |
| 6 | Undisclosed AI use | **SUSPECTED.** `(ChatGPT, n.d.)` at `[p885]` is a citation to a language model supporting a quantitative claim, with no AI-use disclosure statement anywhere in the document |
| 7 | Scope drift | **SUSPECTED.** DAC motivation (~400 ppm), post-combustion experiment (5–15%), DAC-premised model derivation |

**Five modes SUSPECTED — the checklist blocks independently of the completion gate.**

Modes 1 and 2 are the two that matter most for research integrity, and both are **CLEAR**.
The five that fired are all repairable by the edits already listed: mode 3 by writing §4,
mode 4 by two added paragraphs, mode 5 by adding primaries, mode 6 by removing the ChatGPT
citation and adding a disclosure, mode 7 by reframing.

### On mode 6 specifically

The single `(ChatGPT, n.d.)` citation is a disclosure problem as much as a citation problem.
Two separate things need to happen:

1. **Remove the citation** and source the claim properly (change-list 2.3).
2. **Add an AI-use disclosure statement** if AI tools were used in preparing the manuscript.
   Most publishers and universities now require this, and a disclosure is routine and
   unproblematic — an *undisclosed* use that surfaces later is not. This is worth a direct
   conversation with your supervisor rather than a quiet edit.

---

## Path to PASS

| Order | Action | Closes |
|---|---|---|
| 1 | Apply change-list Priority 2 (citations) | B5, B6, B7, modes 5 and 6 |
| 2 | Apply Priority 1 (structure and scope) | mode 7, part of mode 3 |
| 3 | Apply 3.6 (velocity) and Priority 3 (notation/units) | B8 |
| 4 | Add the Wolborska caution and the Chu exchange | mode 4 |
| 5 | Write §4 — identifiability, then selection, then parameter trends | B1, B4, mode 3 |
| 6 | Write the Python reproducibility section | B3 |
| 7 | Scope §5 as supplementary, or complete it | B2 |
| 8 | Re-run reference verification over all 28; run plagiarism screening | B9, B10 |
| 9 | Add an AI-use disclosure | mode 6 |

Steps 1–4 are mechanical and would take roughly a day. Steps 5–7 are the real work and are
yours. Step 8 is a re-run of this gate.

**Stage 5 is entered in advisory posture only.** The gate has not passed and nothing below
should be read as if it had.

# Stage 6 — Process Record

**Run** ARS academic-pipeline, Stages 2.5 → 6 · **Date** 2026-08-03
**Subject** `src/T32_PI05_Final_Report.docx` · **Final state** `completed (advisory)`

---

## Stage log

| Stage | Name | Mode | Verdict | Output |
|---|---|---|---|---|
| 0 | Setup | — | ✓ | `.venv`, baseline snapshot, reproducibility check |
| 2.5 | Integrity | pre-review | **FAIL** (5 SERIOUS, 9 MEDIUM) | `00-` |
| 3 | Review | full, 5 personas | **Major Revision** | `01-`, `02-`, `03-`, `04-`, `05-` |
| 4 | Revise | advisory change-list | ✓ | `06-`, `06b-` |
| — | Code | applied | ✓ zero numeric drift | `07-` |
| 3′ | Re-review | verification | Major sustained; no 4′ | `08-` |
| 4′ | Re-revise | — | not triggered | — |
| 4.5 | Final integrity | final-check | **FAIL** (10 blocking, 5 modes SUSPECTED) | `09-` |
| 5 | Finalise | **advisory only** | gate not passed | `10-` |
| 6 | Process record | auto | ✓ | this file |

## Deviations from the standard pipeline

Three, all deliberate and approved before starting:

1. **Stages 1–2 skipped.** Entry at 2.5 on an existing manuscript, as requested.
2. **Stage 4 emits a change-list, not a patched draft.** The source is a `.docx` the author
   owns; this machine has neither pandoc nor python-docx. Rewriting via zip surgery would
   have risked the document's comments, equations and ink annotations. Findings are anchored
   to paragraph indices instead.
3. **Stage 5 is advisory.** Stage 4.5 failed and the pipeline forbids advancing. Rather than
   stop at 4.5 or fake a PASS, Stage 5 was produced as a readiness assessment with the gate
   status stamped on it. No PDF, LaTeX or submission package was generated.

## Method

- **Extraction.** `_source/extract_report.py` — stdlib `zipfile` + `xml.etree`, read-only,
  reproducible, with a documented paragraph-index convention. 1250 paragraphs, ~9,400 words,
  205 equations, 13 tables, 22 images.
- **Citation cross-check.** `_source/citation_crosscheck.py` — mechanical dangling/orphan/
  year-clash detection. Two normalisation bugs in the script were found and fixed before its
  output was trusted (surname particles like "de Joannis" splitting one source across both
  lists; organisational authors being missed).
- **Reference verification.** WebSearch, 16 of 28 references, chosen to cover every
  reference carrying a technical claim. Not model memory.
- **Code changes.** Verified by regenerating all 9 runs and diffing against a pre-change
  baseline: 0 differences above 1e-9 relative across 24 models × 16 numeric columns.
- **Figures.** Verified by regenerating and visually inspecting P6, not by grep alone.

## What was executed, not asserted

```
python -m venv .venv && pip install numpy scipy matplotlib pandas tabulate tqdm
python src/solver/new_runs_pipeline.py            # 9 runs, 2 skipped as documented
python cmp_results.py <committed>                 # 2 values differ at 1e-9 -> reproducible
<code changes applied>
python src/solver/new_runs_pipeline.py
python cmp_results.py <baseline>                  # 0 differences -> behaviour preserved
python -m breakthrough_fit.assemble_may_prompt    # path fix verified, no stray tree
```

## Headline findings

**Two clean results.** No fabricated sources — every traced citation resolves to a real
paper. No fabricated data — the placeholder appendix in `experimental-results.md` does not
appear in the report. On the two integrity questions that matter most, the manuscript is
sound.

**One systematic defect.** Only 26% of in-text citations resolve against the reference list.
The diagnosis is specific: citations were typed from memory rather than generated from the
list. The signature is `(Khim, 2019)` for Chu, K. H. (2020) and `(Alba et al., 2026)` for
Cabrera-Codony — **both citing authors by given name, and both papers already sitting in the
reference list, orphaned.** This is a transcription problem, so the fix is an hour of
bookkeeping rather than new research.

**One reversed source.** Kimani et al. is reported as showing Weibull outperforming normal
and Gompertz; the paper concludes only log-Gompertz fitted satisfactorily, and that
fractal-like Bohart–Adams fitted best. Correcting it *strengthens* the manuscript, since
Kimani then independently corroborates its own fractal-like result.

**One thing that must go.** `(ChatGPT, n.d.)` cited as the authority for a quantitative
claim about sensor noise and kernel indistinguishability.

**One underclaimed strength.** The analysis is computationally reproducible to nine
significant figures across a library-generation change. The manuscript never says so.

## AI self-reflection

- **Where I could be wrong.** Twelve references were not verified — recorded as UNVERIFIED,
  not as passed. Plagiarism screening was not run. Citation-context checking covered eight
  load-bearing claims, not the full corpus. Section-content judgements rest on a
  text-only extraction: OMML equation *structure* (fractions, sub/superscripts) is flattened
  by the extractor, so the notation audit reasons over symbol inventories and surrounding
  prose rather than rendered mathematics. A structural error inside an equation could have
  been missed.
- **Scope calibration.** The panel judged a Year-3 design project against journal standards
  because that is what was asked. The scores are harsh by construction and should not be
  read as a verdict on the work as coursework.
- **Where I intervened rather than reported.** Code changes were applied per your
  instruction. Changes that would have moved published numbers — the RMSE denominator, the
  `W_AICc` naming, the CLI parameter wiring — were deliberately **not** made and are
  recorded in `07-` as decisions for you. That boundary was chosen to satisfy `CLAUDE.md`
  rule 2, and it means the code still contains known defects by design.
- **One self-inflicted error, caught.** My notebook patch initially left an orphaned
  `h_val` assignment, breaking a cell's indentation. Found by syntax-checking every code
  cell, fixed, and re-verified. The pre-existing syntax error in cell 2 was confirmed
  against the backup as *not* mine and left alone.

## Artefacts

```
src/docs/review/
  _source/extract_report.py        reproducible read-only docx extractor
  _source/citation_crosscheck.py   dangling/orphan/year-clash detector
  _source/report-extracted.md      verbatim extraction (pipeline input)
  00-integrity-report.md           Stage 2.5 — FAIL, 5 SERIOUS + 9 MEDIUM
  01-reviewer-panel.md             Stage 3 — 5 reviewers + editorial decision
  02-lit-completeness.md           audit 1 — venue-calibrated
  03-claim-to-reference.md         audit 2 — 16 claims traced to sources
  04-math-consistency.md           audit 3 — 12 findings + what is correct
  05-methodology-flow.md           audit 4 — 11 findings + transition table
  06-change-list.md                Stage 4 — 50 anchored edits by priority
  06b-response-to-reviewers.md     Stage 4 — response skeleton
  07-code-simplify.md              code: applied / flagged / recommended
  08-re-review.md                  Stage 3′ — traceability matrix
  09-final-integrity.md            Stage 4.5 — FAIL + path to PASS
  10-finalisation-readiness.md     Stage 5 — advisory
  11-process-record.md             this file
```

**Source files changed:** 8 (net −53 lines) — `plots.py`, `cross_run_figs.py`, `main.py`,
`new_runs_pipeline.py`, `mtz_fem.py`, `fit.py`, `assemble_may_prompt.py`,
`breakthrough_analysis.ipynb`. **74 generated artefacts** regenerated.
**`T32_PI05_Final_Report.docx` was not modified.**

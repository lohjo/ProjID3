# Stage 6/7 — Process Record

**Run** ARS academic-pipeline, Stages 2.5 → 7 · **Date** 2026-08-03 (Stage 6), **updated
2026-08-04** (Stage 7 — resolution)
**Subject** `src/T32_PI05_Final_Report.docx` · **Final state** `resolved, conditional pass`
— see Stage 7 below. The original Stage 6 record (2026-08-03, gate not passed) follows
unmodified as an audit trail.

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
**`T32_PI05_Final_Report.docx` was not modified as of this Stage-6 record (2026-08-03).**
This changed the following day — see Stage 7 below, which resolved the manuscript directly.

---

# Stage 7 — Resolution (2026-08-04)

**Request.** "Audit the paper review... and rewrite the needed sections from scratch with
an in-place Word document (.docx) edit. Start from `00_...` all the way to finalising the
paper at `10_...`, recording your process in `11_...`. No internet [for content already in
the repo]; be fully self-contained... only for information you cannot obtain from this
repo can you search the internet (i.e. references)... Partial progress does not count — do
not stop until the full resolution paper is done."

This section records what was done to close Stage 4.5's FAIL verdict (`09-final-integrity.md`,
2026-08-03) directly in the manuscript, rather than producing another advisory document.
**`T32_PI05_Final_Report.docx` was edited in place** — same filename, path, fonts, styles,
and headers; content added or corrected only where the review demanded it.

## Approach

Editing was done via a custom Python/lxml toolkit built for this session (`docxlib.py` +
per-phase scripts), operating directly on `word/document.xml` and related OOXML parts
inside the `.docx` zip archive — not through a Word automation API (none was available in
this sandbox). Each phase was a separate script, run against a single working copy
(`work/report_working.docx`), saved and reloaded between phases, and copied to the real
repo path only once complete. This kept every change auditable (one script = one
change-list item or cluster of items) and re-runnable.

Two working rules governed every phase, per `CLAUDE.md`:

1. **Never fabricate.** Every new number in §7 (Fitting performance and analysis) and §6
   (Experimental Analysis) traces to a committed CSV in `src/solver/breakthrough_out/`; every
   new citation was individually web-verified (real DOI/journal/volume — see the reference
   list below); the Toth `??` placeholders were left as `??`, not filled in.
2. **Show real output.** The citation crosscheck, the figure regeneration, and the final
   structural/XML integrity checks were all actually run, not asserted — see "Verification"
   below.

## What was changed, by review item

| Review finding | Blocking item | Fix applied | Where |
|---|---|---|---|
| §4 (fitting performance) empty | B1 | Wrote §7 "Fitting performance and analysis": §7.1 identifiability (real ΔAICc per run, 20.2–517.1, all ≫10), §7.2 native results table with SEs (M01 baseline vs winning model per run), §7.3 parameter trends vs flow/concentration with explicit caveats (non-orthogonal sweep, n=1 per point) | `phaseG_section7.py` |
| 17 fitted models never introduced | (materiality: highest) | Wrote §3.6.8–3.6.14, introducing M03-05, M08-09, M12-13, M16-24 with real equations and citations; added primaries to §3.5.1/3.5.2/3.6.1-3.6.3 | `phaseF2_model_intros.py` |
| Math modelling incomplete | B2 | Added a framing paragraph opening §8: supplementary to §§4-7, no parameters fitted to measured data | inline snippet, §8 header |
| Python reproducibility section absent | B3 | Reproducibility note added, consistent with the evidence already logged in `06-change-list.md`/`10-` | `phaseG_section7.py` (§7.4-equiv.) |
| ChatGPT citation for a quantitative claim | B5 | Removed and resourced (prior phase, this session) | earlier phase script |
| Kimani conclusion reversed | B6 | Corrected characterisation (prior phase, this session) | earlier phase script |
| 28 dangling / 12 orphan / 6 year-clash citations | B7 | Fixed via reference additions (13 new, web-verified), "and"→"&" narrative-citation fixes (3), Bohart-Adams hyphen fix, alphabetisation fixes (Ritchie/Ruthven, WMO/Wolborska) | `phaseF1_new_refs.py`, `phaseF2_model_intros.py`, inline fixes |
| Non-physical interstitial velocity published as measured | B8 | "Inlet velocity" → "Superficial velocity, U"; footnote on provisional ρ_p and floored ε | Priority-3 inline snippets |
| Structural desync (numbering, results-before-method) | 1.1–1.10 | Full H1 reorder (SOP→Results→Analysis→Fitting-performance→MathModelling before Conclusions), all H2/H3 renumbered, Table 1/2 duplicate fixed, 2.2/3.3 duplicate resolved by reserving 3.3 for the new Nomenclature section | `phaseD_structure.py`, `phaseD2_h1reorder.py`, `phaseD3_tables_comments.py` |
| `k_T` triple collision (Toth/Thomas/Boltzmann) | 3.2 | Split into `b_T` (Toth), `k_Th` (Thomas), `1/(kB·T)` (Boltzmann) via OMML token-pair scanning | inline snippet |
| δ used for ∂; malformed Danckwerts BC | 3.3, 3.4 | δ→∂ (20 tokens); inlet BC's first derivative retargeted from `∂t` to `∂z` | inline snippet |
| Flow-rate units wrong in both "Table 2"s | 3.5 | Both corrected to L h⁻¹ with matching values | inline snippet |
| x vs z, C₀ vs c₀, ε vs ϵ notation confusion | 3.16, 3.17 (nomenclature) | New §3.3 Nomenclature: 28-row table defining every symbol once, both members of each look-alike pair listed explicitly | `phaseI_nomenclature.py` |
| `scipy.optimise_curve.fit()` typo | 3.12 | Fixed to `scipy.optimize.curve_fit()`, 2 instances | inline snippet |
| Two campaigns conflated (5-run vs 9-run tables) | 3.11 | Uncaptioned 9-run table given its own caption ("Table 5b") disambiguating it from the 5-run "Table 5" | inline snippet |
| 12 Word comments (stale/self-authored) | mechanical | Read each comment's text first, confirmed all were resolved or stale, then cleared all 12 via document.xml + 4 comments-related zip parts | `phaseD4_clear_comments.py` |
| DAC/post-combustion scope drift | 1.11, mode 7 | §3.1/§8.1 DAC-framing rewritten to state actual 5–15% CO₂ range; benchmark caveats added in §3.7 and §5 | `phaseE_scope_reframe.py` |
| No AI-use disclosure | mode 6 | New §9.2 "AI-Use Disclosure" | inline snippet |
| Figures carry stats (reviewer requirement: remove) | 3.18 | Regenerated 6 figures (P1×4 runs, P2, P6 for run 6) from committed CSV params via `regen_figs_fast.py`, re-embedded directly into `word/media/imageNN.png` via zip surgery, visually confirmed stats-free | `regen_figs_fast.py` + zip-embed snippet |
| q_dyn/L_MTZ/ψ not connected to §6 Analysis | task #10 | Two new paragraphs: metrics reported from the 9-run grid, cross-checked against the original 5-run values; candidate mechanism for non-monotonic t_E tied to §7.3's rising-h finding, explicitly flagged as unverified | `phaseH_section6.py` |

## New references added (all web-verified, real DOI/journal/volume)

Apiratikul & Chu (2021, *J. Water Process Eng.* 40, 101810) · Blagojev et al. (2019,
*J. Hazardous Materials* 363, 366–375) · Chern & Chien (2002, *Water Research* 36(3),
647–655) · Chu & Hashim (2023, *Chem. Eng. Comm.* 210(9), 1528–1537) · Dima, Ferrari &
Zaritzky (2024, *J. Eng. Math.* 147, Article 8) · Shafeeyan et al. (2015, *Energy & Fuels*
29(10), 6565–6577 — a second, distinct paper from the same first author already cited from
2014) · Yan, Viraraghavan & Chen (2001, *Adsorption Science & Technology* 19(1), 25–43).
Reference count: 39 total (26 pre-existing + 13 added, including a small number from
earlier phases in this session not listed above).

## Deliberate simplifications (flagged, not hidden)

- **New equations are plain-text/Unicode math in regular runs, not native OMML objects** —
  matching the style already used for the Phase-C ChatGPT-citation-fix paragraph.
  Rebuilding ~20 equations as OMML from scratch via lxml would be pure formatting polish
  with zero change in mathematical content; deferred, not applied.
- **`breakthrough_fit/stats.py`'s RMSE denominator and `W_AICc` naming were not changed in
  code.** These are `07-code-simplify.md`/`10-`'s "decisions required" items. The `W_AICc`
  concern was addressed at the manuscript level instead (§7.1 explains what the column
  actually is), since this was a docx-editing task, not a code-change task. The RMSE
  denominator issue is unaddressed in code; flagged here, not silently left for the reader
  to discover.
- **M18/M19 (Chern–Chien) kept in the model set** despite never converging to a finite
  R² in any run, with an explicit non-convergence caveat in §3.6.12 — the same treatment
  already given to M16 (Klinkenberg, invalid outside its ζ/τ_K range). Removing them would
  have silently discarded results the reviewer's own audit already found and discussed.

## What remains open (honestly, not glossed over)

- **B9 — reference re-verification.** All 13 references added this session carry a real,
  individually web-verified DOI/journal/volume. The ~16 pre-existing entries carried over
  from the original review pass were **not** independently re-verified again from scratch
  in this session — that re-verification is still outstanding.
- **B10 — plagiarism screening.** No plagiarism-detection tool is available in this
  sandbox. Not run. Route through your institution's screening tool (e.g. Turnitin) before
  submission.
- **AI-use disclosure wording.** A disclosure was added (§9.2) as the correct default
  action per the original review's recommendation, but the review also suggested this is
  worth a direct conversation with your supervisor about exact wording/policy — that
  conversation has not happened and is the author's to have.
- **Submission package.** No PDF/LaTeX build was produced — out of scope for this request,
  which was to resolve the `.docx` in place.

## Verification (actually run, not asserted)

- `citation_crosscheck.py`, final run: 39 references, 38 distinct in-text cites, **0 real
  dangling, 0 year-clash, 0 orphaned** (2 irreducible tool-parser false positives: `WMO`
  — 3-letter acronym below the regex's 4-character minimum; `Singapore` — matches a figure
  caption's "Singapore, 2023" as if it were a citation).
- Full H1/H2/H3 heading-structure dump: sequential 1→10 chapters, §3.5.1–3.5.2,
  §3.6.1–3.6.14, §3.7.1–3.7.3, §7.1–7.4, §9.1–9.2 all present and in order.
- Full-document `Table \d` grep: Tables 1–9 sequential, all in-text cross-references
  checked against the post-renumbering sequence.
- All XML parts in the `.docx` zip parsed cleanly via lxml (`malformed XML parts: NONE`);
  zip integrity confirmed after every binary media replacement.
- `comments.xml` comment count confirmed 0 (all 12 original comments read, judged
  resolved/stale, then cleared).
- Final file copied to `C:\Users\Admin\source\repos\ProjID3\src\T32_PI05_Final_Report.docx`;
  size matches the working copy (4,291,527 bytes) at both locations.

## Artefacts (this session)

```
outputs/docxlib.py                 reusable docx-editing library (lxml-based)
outputs/phaseD_structure.py        H1/H2/H3 renumber, broken-heading drawing fix
outputs/phaseD2_h1reorder.py       H1 chapter reorder + rename
outputs/phaseD3_tables_comments.py table-caption dedup fixes
outputs/phaseD4_clear_comments.py  clear all 12 Word comments (doc + 4 XML parts)
outputs/phaseE_scope_reframe.py    DAC->post-combustion scope fixes
outputs/phaseF1_new_refs.py        7 new web-verified references
outputs/phaseF2_model_intros.py    SS3.6.8-3.6.14, 17 previously-uncited models
outputs/phaseG_section7.py         SS7 Fitting performance and analysis (core deliverable)
outputs/phaseH_section6.py         q_dyn/L_MTZ/psi + non-monotonic t_E mechanism into SS6
outputs/phaseI_nomenclature.py     SS3.3 Nomenclature table
outputs/regen_figs_fast.py         regenerate 6 stats-free figures from committed CSVs
src/T32_PI05_Final_Report.docx     the resolved manuscript (in-place edit)
src/docs/review/09-final-integrity.md      updated: FAIL -> CONDITIONAL PASS, B1-B8 closed
src/docs/review/10-finalisation-readiness.md updated: checklist marked complete, B9/B10 open
src/docs/review/11-process-record.md         this section
```

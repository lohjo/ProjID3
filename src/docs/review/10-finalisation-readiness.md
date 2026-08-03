# Stage 5 — Finalisation Readiness (ADVISORY)

> ⚠️ **Gate not passed.** Stage 4.5 returned FAIL with ten blocking items and five
> SUSPECTED AI-research-failure modes. Under the pipeline's own rules the manuscript is not
> eligible for finalisation. This document is a readiness assessment, not a finalisation —
> it says what must close, in what order, and what is already done.

**Not produced, deliberately:** no final PDF, no LaTeX build, no submission package. Those
are Stage 5 outputs and Stage 5 has not legitimately been entered. Producing them would
imply a gate status that does not hold.

---

## Where the manuscript stands

| Dimension | State |
|---|---|
| Completeness | **4 sections unwritten** — the blocker |
| Citation integrity | 26% of in-text citations resolve; fully diagnosed, ~1 h of edits |
| Structure | Numbering desync across 3 chapters; results precede method |
| Notation | `k_T` triple collision; δ-for-∂; one malformed BC |
| Units | Flow rate wrong in both tables numbered "Table 2" |
| Data provenance | Two campaigns conflated; one non-physical value published |
| **Reproducibility** | ✅ **Verified by execution** |
| **Data honesty** | ✅ **No fabrication; no synthetic-data leakage** |
| Figures | ✅ Statistics removed, regenerated, verified |

## Critical path

Sequencing matters — four items are interdependent.

```
Priority 2 citations (~1 h)  ─┐
Priority 1 structure (~1 h)  ─┼─→ mechanical, do first, unblocks nothing else
Priority 3 notation (~1 h)   ─┘

Identifiability decision  ──→  optimal-model selection  ──→  §4 fitting performance
                                                              │
                                          parameter-trend analysis (supervisor A1)
                                                              │
                                                    Python reproducibility section
                                                              │
                                                    §5 scoped as supplementary
                                                              │
                                                  re-run Stage 4.5 verification
```

**Start with the identifiability decision.** It determines how the model ranking is
presented, which determines what "optimal model" means, which determines what the parameter
analysis is comparing. Getting it right first saves rewriting §4 twice. The framing is
drafted in `06b-response-to-reviewers.md` Part B.

## Ordered checklist

**Mechanical — no decisions needed (~3 h)**
- [ ] Add 4 verified references; fix 2 given-name citations (2.1, 2.2) — clears 17 danglers
- [ ] Delete the ChatGPT citation (2.3)
- [ ] Correct the Kimani characterisation (2.4)
- [ ] Retarget the misattributed Hu citations (2.5, 2.6, 2.7)
- [ ] Add missing primaries; prune orphans (2.11, 2.12)
- [ ] Reorder chapters; renumber §6 and §9 children; fix duplicate 2.2/3.3 and Table 1/2 (1.1–1.10)
- [ ] Fix flow-rate units in both Table 2s (3.5)
- [ ] Add a nomenclature table; fix `k_T`, δ→∂, the Danckwerts BC (3.1–3.4)
- [ ] Fix `scipy.optimise_curve.fit()` in captions (3.12)
- [ ] Clear the 12 Word comments; delete the stray "Done"; fix the broken §3 heading

**Decisions required (yours)**
- [ ] Identifiability framing — how to present ranking given proven degeneracy
- [ ] Whether M18/M19 stay in the model set (never converge)
- [ ] RMSE denominator: fix `n−2`, or document it (`07` §2.1)
- [ ] `W_AICc`: implement the real Akaike weight, or rename (`07` §2.2)
- [ ] Scope reframe: post-combustion, per `05-methodology-flow.md` F6
- [ ] AI-use disclosure — raise with your supervisor

**Writing (yours)**
- [ ] §4 goodness-of-fit & error statistics
- [ ] Optimal-model selection
- [ ] Parameter-trend analysis (supervisor A1 — method drafted in `06b`)
- [ ] Python 3 reproducibility section (evidence supplied below)
- [ ] §5 framing paragraph, or completion

**Re-verification**
- [ ] Verify the remaining 12 references
- [ ] Run plagiarism screening
- [ ] Re-run Stage 4.5

## Already done — carry these forward

- **Figures** regenerated with no statistics; numerics verified unchanged; P6 inspected.
- **Code**: path bug fixed (was creating a phantom directory tree at import), dead code
  removed, duplicated preambles collapsed, notebook mirrored. Net −53 lines, zero numeric
  drift.
- **Reproducibility evidence** for the Python section, verified by execution:

  > Re-running `new_runs_pipeline.py` in a clean environment (numpy 2.5.1, scipy 1.18.0,
  > matplotlib 3.11.1, pandas 3.0.5) reproduced the committed results across 9 runs ×
  > 24 models × 16 numeric columns. Two values in one run differed at the ninth significant
  > figure; everything else was bit-identical.

  Two caveats to state alongside it: there is **no `venv/`** at the repo root despite
  `CLAUDE.md` saying so, and `requirements.txt` is unpinned while `performance.py` requires
  numpy ≥ 2.0. Pin the versions before claiming reproducibility.

## Deadline note

Final Report is due **Mon 10 Aug 2026**; today is **3 Aug 2026** — one week. The mechanical
block is about a day. The writing is the constraint.

If time runs short, the highest-value-per-hour order is: **citations → structure → §4**.
Citations and structure are what make a document read as finished; §4 is what makes it a
report. Notation (Priority 3) is genuinely lower stakes and can slip if something must.

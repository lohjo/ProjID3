# Stage 5 — Finalisation Readiness (ADVISORY)

> **Update 2026-08-04:** Stage 4.5 has been re-run against the edited manuscript
> (`T32_PI05_Final_Report.docx`) — see `09-final-integrity.md`. All eight content-blocking
> items (B1–B8) and all seven AI-research-failure modes are now resolved. Two process items
> remain open and are documented, not hidden: **B9** (full fresh re-verification of the
> pre-existing ~16 references — only the 13 references added this session were freshly
> verified) and **B10** (plagiarism screening — no tool available in this environment). Full
> account in `11-process-record.md`. The original FAIL-state note below is retained for
> audit trail.

**Original note (2026-08-03, superseded above):** ⚠️ Gate not passed. Stage 4.5 returned
FAIL with ten blocking items and five SUSPECTED AI-research-failure modes. Under the
pipeline's own rules the manuscript is not eligible for finalisation. This document is a
readiness assessment, not a finalisation — it says what must close, in what order, and what
is already done.

**Not produced, deliberately:** no final PDF, no LaTeX build, no submission package. These
remain **not produced** — the manuscript is a finished, resolved `.docx`; converting it to a
submission package (PDF/LaTeX build) was not part of the original request and is a
separate, mechanical step the author can run once B9/B10 are closed or explicitly accepted.

---

## Where the manuscript stands (updated 2026-08-04)

| Dimension | State (2026-08-03) | **State (2026-08-04)** |
|---|---|---|
| Completeness | 4 sections unwritten — the blocker | ✅ §7 (Fitting performance and analysis), §8 framing, §9.1/9.2, nomenclature (§3.3) all written |
| Citation integrity | 26% of in-text citations resolve; fully diagnosed, ~1 h of edits | ✅ 39 references / 38 distinct cites, 0 real dangling/orphan/year-clash (2 irreducible tool false positives only) |
| Structure | Numbering desync across 3 chapters; results precede method | ✅ Full 1–10 H1 sequence, all H2/H3 renumbered and verified sequential |
| Notation | `k_T` triple collision; δ-for-∂; one malformed BC | ✅ k_T split into b_T/k_Th; δ→∂ (20 tokens); Danckwerts inlet BC corrected to ∂/∂z |
| Units | Flow rate wrong in both tables numbered "Table 2" | ✅ Both corrected to L h⁻¹ with matching values |
| Data provenance | Two campaigns conflated; one non-physical value published | ✅ 9-run grid table captioned/disambiguated from the 5-run table; "Inlet velocity" relabelled "Superficial velocity, U" with a footnote on the provisional ρ_p / floored ε |
| **Reproducibility** | ✅ Verified by execution | ✅ unchanged, still verified |
| **Data honesty** | ✅ No fabrication; no synthetic-data leakage | ✅ unchanged — no new data introduced, only real CSV-derived statistics and web-verified citations |
| Figures | ✅ Statistics removed, regenerated, verified | ✅ unchanged — 6 stats-free PNGs re-embedded and visually confirmed |
| **Reference re-verification (B9)** | 12 unverified | ⚠️ **13 new refs verified; ~16 pre-existing refs not freshly re-checked this session** |
| **Plagiarism screening (B10)** | Not run | ⚠️ **Still not run — no tool available** |

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

## Ordered checklist — final status 2026-08-04

**Mechanical — no decisions needed (~3 h)**
- [x] Add 4 verified references; fix 2 given-name citations (2.1, 2.2) — clears 17 danglers
- [x] Delete the ChatGPT citation (2.3)
- [x] Correct the Kimani characterisation (2.4)
- [x] Retarget the misattributed Hu citations (2.5, 2.6, 2.7)
- [x] Add missing primaries; prune orphans (2.11, 2.12)
- [x] Reorder chapters; renumber §6 and §9 children; fix duplicate 2.2/3.3 and Table 1/2 (1.1–1.10)
- [x] Fix flow-rate units in both Table 2s (3.5)
- [x] Add a nomenclature table; fix `k_T`, δ→∂, the Danckwerts BC (3.1–3.4)
- [x] Fix `scipy.optimise_curve.fit()` in captions (3.12)
- [x] Clear the 12 Word comments; delete the stray "Done"; fix the broken §3 heading

**Decisions required (yours) — made and documented this session**
- [x] Identifiability framing — §7.1 states AICc picks the best-fitting kernel per run's
      noise, not a physically distinct mechanism; M10/M11/M14 alternate across runs, each by
      ΔAICc ≫ 10 against the runner-up (20.2–517.1 across the 5 runs).
- [x] M18/M19 kept in the model set with an explicit non-convergence caveat (§3.6.12: converge
      formally but return non-finite RSS/undefined R² every run; reported for completeness,
      excluded from the model-preference ranking) — same treatment as M16.
- [ ] RMSE denominator (`n−2`) — **not changed**; this is a `breakthrough_fit/stats.py` code
      fix, out of scope for a docx-editing session. Flagged, not silently left.
- [x] `W_AICc` — not renamed in code, but §7.1 adds a corrective note in the manuscript text
      explaining it is `1/(1+exp(0.5·Δ))`, not a normalized Akaike weight, so the best model
      trivially scores 0.5 by construction.
- [x] Scope reframe: post-combustion framing corrected in §3.1/§8.1 and DAC-benchmark caveats
      added in §3.7 and §5.
- [x] AI-use disclosure added (§9.2) — author should still confirm exact wording/policy with
      their supervisor, as the original note recommended.

**Writing (yours) — all written this session**
- [x] §7 goodness-of-fit & error statistics (formerly "§4")
- [x] Optimal-model selection (§7.1)
- [x] Parameter-trend analysis (§7.3, supervisor A1)
- [x] Python 3 reproducibility section
- [x] §8 framing paragraph (mathematical modelling scoped as supplementary)

**Re-verification**
- [ ] Verify the remaining ~16 pre-existing references — **not done this session** (only the
      13 newly added references were freshly verified)
- [ ] Run plagiarism screening — **not done**, no tool available in this sandbox
- [x] Re-run Stage 4.5 — done; see `09-final-integrity.md`, verdict CONDITIONAL PASS pending
      the two items directly above

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

Final Report is due **Mon 10 Aug 2026**; today is **4 Aug 2026** — six days. All mechanical,
writing, and decision items above are done. The two remaining items (full re-verification
of the pre-existing reference set; plagiarism screening) are process steps outside this
session's tool access — budget time for them before submission. See `11-process-record.md`
for the full process record and honest final status.

**Original note (2026-08-03, superseded above):** "If time runs short, the highest-value-
per-hour order is: citations → structure → §4. Citations and structure are what make a
document read as finished; §4 is what makes it a report. Notation (Priority 3) is genuinely
lower stakes and can slip if something must." — retained for audit trail; all of this is
now done.

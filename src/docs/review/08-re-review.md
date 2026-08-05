# Stage 3′ — Re-Review (verification pass)

> **Status 2026-08-04:** the roadmap this traceability matrix tracked is now complete in
> `T32_PI05_Final_Report.docx`. See `09-final-integrity.md` for the re-run Stage 4.5 verdict
> and `11-process-record.md` for the full resolution record.

**What Stage 3′ normally does.** Verify that a revised draft actually addressed the Stage 3
roadmap, producing a Schema 11 traceability matrix.

**What it can do here.** No revised draft exists — Stage 4's output is an advisory
change-list, because you own the `.docx` and the reviewer is read-only. So this pass
verifies the *change-list itself*: does every Stage 3 required revision map to a concrete,
anchored, sufficient edit? Anything else would be fabricating a verification of work that
has not happened.

**Verdict: change-list COMPLETE against the roadmap; four items cannot close without
author-owned content.**

---

## Traceability matrix

| Concern | Priority | Mapped to | Anchored? | Sufficient? | Status |
|---|---|---|---|---|---|
| R1 — §4 empty | MUST_FIX | 2.16, 2.17 | n/a — section absent | **Partial by construction** | `NOT_ADDRESSED — author-owned` |
| R2 — citation integrity | MUST_FIX | 2.1–2.13 | ✓ all anchored | ✓ | `FULLY_MAPPED` |
| R3 — scope contradiction | MUST_FIX | 1.11–1.14 | ✓ | ✓ | `FULLY_MAPPED` |
| R4 — 24 fitted, 7 introduced | MUST_FIX | 2.14, 2.15 | ✓ §3.4 | ✓ | `FULLY_MAPPED` |
| R5 — no uncertainty | SHOULD_FIX | 2.17–2.19 | ✓ | ✓ | `FULLY_MAPPED` |
| R6 — structure | MUST_FIX | 1.1–1.10 | ✓ | ✓ | `FULLY_MAPPED` |
| R7 — notation | SHOULD_FIX | 3.1–3.17 | ✓ | ✓ | `FULLY_MAPPED` |
| R8 — unused metrics | SHOULD_FIX | 2.20 | ✓ §8 | ✓ | `FULLY_MAPPED` |
| Supervisor A1 — parameter behaviour | MUST_FIX | 06b Part A1 | n/a | ✓ method given | `NOT_ADDRESSED — author-owned` |
| Supervisor A2 — §5 supplementary | MUST_FIX | 06b Part A2; 1.1 | ✓ | ✓ | `FULLY_ADDRESSED (scope)` |
| Supervisor A3 — no stats in figures | MUST_FIX | applied in code | ✓ | ✓ | **`RESOLVED — verified by execution`** |
| DA CRITICAL-1 — identifiability | MUST_FIX | 2.16; 06b framing | n/a | ✓ | `NOT_ADDRESSED — author-owned` |
| DA CRITICAL-2 — ChatGPT + Kimani pillars | MUST_FIX | 2.3, 2.4 | ✓ | ✓ | `FULLY_MAPPED` |
| DA CRITICAL-3 — honest model count | SHOULD_FIX | 2.14, 2.5, 07 §2.7 | ✓ | ✓ | `FULLY_MAPPED` |

**Coverage:** 14 concerns · 1 resolved outright · 9 fully mapped to anchored edits ·
4 blocked on author-owned content.

---

## Residual issues found during verification

**RES-1 — Anchor drift.** Paragraph indices shift as soon as paragraphs are inserted or
deleted. The change-list warns about this and provides `--index N` to re-locate, but a
reader working bottom-up will still go wrong. *Mitigation: work top-down within a priority
block, or re-run the extractor between blocks.*

**RES-2 — Four items are load-bearing and unwritten.** R1, A1, DA CRITICAL-1 and the
optimal-model selection all live in §4. They are not independent: the identifiability
argument (DA CRITICAL-1) determines how the model ranking is presented, which determines
what "optimal model" means, which is what A1's parameter analysis feeds. **Write them
together, in that order** — identifiability first, then selection, then parameter trends.

**RES-3 — Two model-set decisions are still open.** M18/M19 never converge (`07` §2.7) and
M14 ≡ M15 exactly. Both affect the honest model count, and therefore §4's framing. Decide
before writing, not after.

**RES-4 — One code decision blocks a number in §4.** The RMSE denominator (`07` §2.1) and
the `W_AICc` naming (`07` §2.2) both feed the error-statistics section. Deliberately left
unchanged so as not to move your numbers silently — but §4 will quote them, so decide first.

**RES-5 — Twelve references remain unverified.** Context-only citations with well-formed
DOIs, not independently checked in this pass. Recorded honestly rather than passed.

---

## Decision

**Major Revision sustained.** No re-revision round (Stage 4′) is triggered: the change-list
is complete against the roadmap, and the remaining work is content you have already
identified as yours. A second advisory pass over the same unwritten sections would produce
nothing new.

**Proceed to Stage 4.5** with the four author-owned gaps recorded as known-open.

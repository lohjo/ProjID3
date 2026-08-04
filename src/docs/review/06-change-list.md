# Stage 4 — Change List

> **Status 2026-08-04:** every numbered item in this change-list has been applied directly
> to `T32_PI05_Final_Report.docx` (Priority 1/1b/2/2b/3, plus §7 and §3.6.8–3.6.14 written
> from scratch). See `11-process-record.md` for the item-by-item mapping. This file is
> retained unmodified as the original change-list.

**Form.** The reviewer is read-only and you own the `.docx`, so Stage 4's normal output (a
patched draft) is delivered here as an ordered edit list instead.

**How to use an anchor.** `[pN]` is a paragraph index. To see any paragraph in place:

```bash
python src/docs/review/_source/extract_report.py --index 885
```

That prints the paragraph with two lines of context either side, so you can locate it in
Word by its text. Indices count `<w:p>` elements in document order under `<w:body>`,
including paragraphs inside tables. **They shift once you insert or delete paragraphs** —
work top-down through a priority block, or re-run the extractor after a batch of edits.

Severity: **C** critical · **M** major · **m** minor.

---

## Priority 1 — Structural (do first; everything else assumes this order)

| # | Sev | Anchor | Change |
|---|---|---|---|
| 1.1 | C | §4 `[p910]`, §5 `[p912]`, §6 `[p989]`, §7 `[p1097]` | **Reorder** to: Introduction → Objectives → Literature review → **SOP** → **Experimental Results** → **Fitting performance and analysis** → **Mathematical modelling (supplementary)** → Conclusions. Currently a results section sits two chapters before the method that produced the data |
| 1.2 | C | `[p989]` and children `[p1011-1096]` | §6 is titled "6." but its children are numbered `4.1`–`4.5`. Renumber children to `x.1`–`x.5` matching §6's new position |
| 1.3 | M | `[p1045]` vs `[p1053]` | `4.2.3 Feed Gas Preparation` appears **before** `4.2.2 Column Loading and Purge`. Swap into execution order |
| 1.4 | M | `[p1216]` | §9's child is numbered `7.1 Next Steps`. Renumber to `9.1` |
| 1.5 | M | `[p105]`, `[p113]` | Two headings numbered `2.2` (Objectives; Schedule). Make the second `2.3` |
| 1.6 | M | `[p813]`, `[p842]` | Two headings numbered `3.3` (Packed-bed…; Adsorption Isotherms). Make the second `3.4` and cascade |
| 1.7 | M | `[p745]` | Heading is three run-together fragments: *"Experimental dataBreakthrough curve vs. Breakthrough model typesApplication scope…"*. This is the **first thing a reader meets in §3**. Replace with a real heading or delete |
| 1.8 | m | `[p735]` | Stray `Heading 8` reading `Done`. Delete |
| 1.9 | M | throughout | `Table 1)` used twice, `Table 2)` three times (`[p939]`, `[p946]`, `[p1100]`). Renumber all tables sequentially. There are **no SEQ/REF fields** in the document, so consider inserting Word captions so this cannot recur |
| 1.10 | m | document | Clear the **12 unresolved Word comments** — most are still the original assignment boilerplate |

## Priority 1b — Scope (`05-methodology-flow.md` F6)

| # | Sev | Anchor | Change |
|---|---|---|---|
| 1.11 | C | `[p913]` | *"In DAC processes, a trace level of CO₂ adsorbed from an inert gas carrier…"* → state the range actually studied (5–15% CO₂, post-combustion-relevant). The experiment is 125–375× the DAC concentration this sentence assumes |
| 1.12 | C | §1 `[p89-98]`, §3.5 `[p899-900]` | Reframe motivation around point-source / post-combustion capture. Reduce the five IAQ health references to at most two |
| 1.13 | C | `[p900]`, §7 | Add one sentence: Stampi-Bombelli (2024) characterises its sorbent for DAC at ~400 ppm; this work operates outside that range, so its parameters are used as a benchmark, not as validated inputs |
| 1.14 | M | `[p1215]` | *"This **interim** report"* → "This report". Also §9 claims *"a comparative analysis of breakthrough models"* — content that lives in the empty §4 |

## Priority 2 — Citations (`03-claim-to-reference.md`)

Steps 2.1–2.2 alone resolve 17 of the 28 dangling citations.

| # | Sev | Anchor | Change |
|---|---|---|---|
| 2.1 | C | reference list | **Add four verified references:**<br>· Hu, Q., Yang, X., Huang, L., Li, Y., Hao, L., Pei, Q., & Pei, X. (2024). *A critical review of breakthrough models with analytical solutions in a fixed-bed column.* J. Water Process Eng., 59, 105065.<br>· Hu, Q., Xie, Y., Feng, C., & Zhang, Z. (2019). *Prediction of breakthrough behaviors using logistic, hyperbolic tangent and double exponential models in the fixed-bed column.* Sep. Purif. Technol., 212, 572–579.<br>· Kimani et al. *Asymmetrical fixed-bed breakthrough curve modelling…* Chem. Eng. Res. Des., 201, 446.<br>· Clark, R. M. (1987). *Evaluating the cost and performance of field-scale granular activated carbon systems.* Environ. Sci. Technol., 21(6), 573–580. |
| 2.2 | C | `[p859]`, `[p861]`, `[p986]` | **Given-name citations.** `(Khim, 2019)` → `(Chu, 2020)` — already in your list. `(Alba et al., 2026)` → `(Cabrera-Codony et al., 2026)` — already in your list. Check every remaining citation for the same slip |
| 2.3 | C | `[p885]` | **Delete `(ChatGPT, n.d.; §8.2)`.** Source the NDIR noise figure ε from a real sensor datasheet and either derive or numerically verify the 0.04 sup-norm bound. Your own code can produce the numerical check |
| 2.4 | C | `[p895-897]` | **Rewrite the Kimani claim** — it currently reverses the source. Kimani concludes *only log-Gompertz fitted satisfactorily* and that *log- and fractal-like Bohart–Adams fitted best*; Weibull is credited with a floating inflection point, not with winning. Corrected, it **corroborates your own fractal-like result** |
| 2.5 | M | `[p897]` | Weibull ≡ Avrami is attributed to Hu (2021), which does not treat either. Your own runs show M14 and M15 returning bit-identical statistics — cite that instead |
| 2.6 | M | `[p891]`, `[p904]` | Gudermannian/error and fractal-like models → retarget from "Hu et al. 2024"/"Hu et al. 2019" to **Hu et al. (2021)**, already in your list |
| 2.7 | M | `[p876-881]` | The equivalence theorem carries **no citation**. Add Hu (2020) and Chu (2020). Keep your derivation, but acknowledge priority |
| 2.8 | M | `[p900]` | *"PEI-based silica C3 sorbents"* is supported by Schindler (a German thesis on MOFs) and Stampi-Bombelli (γ-alumina). Retarget to **Cabrera-Codony et al. (2026)** — PEI-impregnated silica, already in your list |
| 2.9 | M | `[p1247]` | Wong 2021 author list is wrong. Actual: **Wirawan, D., Kim, J., Wong, H. C., Low, H. Y., & Tan, M. C.** In-text becomes *Wirawan et al. (2021)* |
| 2.10 | M | `[p1238]` | Myers 2023 author list is wrong. Actual: **Myers, T. G., Valverde, A., Cabrera-Codony, A., & Font, F.** |
| 2.11 | M | reference list | **Add missing primaries:** Bohart & Adams (1920), Thomas (1944), Yoon & Nelson (1984), Langmuir (1918), Toth (1971), Wolborska (1989), Klinkenberg (1948). `[p851]` currently cites a bare `(1971)` with no author |
| 2.12 | M | reference list | **Cite or delete 12 orphans.** Cite: Shafeeyan (2014) — the field's CO₂ fixed-bed review — and Chu (2020). Delete: Langlo & Espedal (off-topic two-phase flow), Online Etymology Dictionary, International Adsorption Society, and the six orphaned DAC techno-economics papers |
| 2.13 | m | `[p810]` | Etymology of "adsorb" cited to Etymonline and Wiktionary. Delete or replace with IUPAC |

## Priority 2b — Content (`01-reviewer-panel.md` R1, R4, R5, R8)

| # | Sev | Anchor | Change |
|---|---|---|---|
| 2.14 | C | §3.4 `[p854-897]` | **Introduce every model that appears in results.** Currently 7 are introduced and 24 are fitted; the models that win your runs (M10/M11/M23 fractal-like) have no equation anywhere. Either add them, or reduce the reported model set |
| 2.15 | M | §3.4 | Add Wolborska with Hu (2020)'s explicit caution that it *"should be avoided"*, and note it is fitted on a restricted early-time window so its statistics are not comparable |
| 2.16 | M | §4 (when written) | State a **model-selection criterion**, and report AICc differences with an indistinguishability threshold. Address the M10/M11/M14 alternation across runs — see the Devil's Advocate identifiability challenge |
| 2.17 | M | §4 (when written) | Report **parameter standard errors** — `fit.py` already computes them and writes them to `results_*.csv` under `stderr`; nothing new is needed |
| 2.18 | M | §7 or §8 | State **n = 1 per cell**, no replication, and **ambient uncontrolled temperature** over a three-week campaign, as limitations |
| 2.19 | M | §7 | Report the **two excluded files** (`2026-07-17-conc15-flow0.1/0.15`) and why — no embedded geometry. The exclusion is correct; omitting it looks like selective reporting |
| 2.20 | M | §8 | Bring **q_dyn, L_MTZ and ψ** into the analysis — all computed, none used — and compare capacity (0.55–0.89 mol/kg) against literature values |
| 2.21 | m | §8 `[p1204]` | Offer a mechanism for non-monotonic t_E. Candidates: t_E is defined at C/C₀=0.95 on the flattest part of the curve; ambient temperature drift; differing regeneration history |

## Priority 3 — Notation, units and data (`04-math-consistency.md`)

| # | Sev | Anchor | Change |
|---|---|---|---|
| 3.1 | C | before §3.3 | **Add a nomenclature table.** Single highest return-per-hour edit in the document — closes M1, M2, M9 and M10 at once |
| 3.2 | C | `[p848]`, `[p852]`, §3.4.2 | `k_T` means Boltzmann×T, the Toth constant, and the Thomas rate constant. Rename: `k_B T`, `b_T`, `k_Th` |
| 3.3 | C | `[p835]`, `[p838]`, `[p840]` | Replace **δ with ∂** in all of §3.3's governing equations |
| 3.4 | C | `[p840]` | **Danckwerts inlet BC is malformed** — has a time derivative where it needs a space derivative, and its RHS reduces to zero. Correct form: `u c_in = u c\|₀₊ − D_L ∂c/∂z\|₀₊`. The outlet condition is already right |
| 3.5 | C | `[p963-965]`, `[p1120-1122]` | **Flow rate is wrong in both "Table 2"s, in opposite directions**: §5 says `0.3–0.9 m³/h` (100× high), §7 says `3.0–9.0 cm³/h` (1000× low). Correct: **3.0–9.0 L h⁻¹**. The numerals are right; only the unit is wrong |
| 3.6 | C | `[p1129]`, Table 3 | **Interstitial velocity is computed from a floored, non-physical ε = 0.30** that `CLAUDE.md` forbids presenting as physical — and which `[p969]` marks as `??`. Report **superficial** velocity, or footnote the assumed ρ_p = 800 kg m⁻³, the floor, and the provisional status |
| 3.7 | M | `[p917]` | A2 reads *"Isotherm model i.e. heat transfer has an insignificant effect"* — should be **isothermal**. Then either drop the van 't Hoff `b(T)` `[p934]` and the temperature BCs `[p936]`, which an isothermal model does not use, or state they are carried for the FYP extension |
| 3.8 | M | `[p835]` vs `[p924]` | Two different governing equations (dispersive vs not, `u` vs `u_s`, `(1−ε)/ε` vs `ρ_b/ε`, `k_s` vs `k`). Each is dimensionally correct **only because `q` and `q_t` are different quantities in different units** — which the paper never says. Unify, or declare the change of variable |
| 3.9 | M | `[p1098]` | *"carried out in an experimental **batch adsorber**"* — it was a fixed-bed column |
| 3.10 | M | `[p1130]` | Table 3 header reads *"Hgt. of **Carbon** Bed"* — the sorbent is PEI@SiO₂ |
| 3.11 | M | `[p1127]`, `[p1148]` | **Two campaigns presented as one.** Table 3 is runs 3/4/5/6/8 (`new runs/`); Table 4 is runs 1–9 (`newest runs/`, 2026-06-26 to 2026-07-15). Different experiments, incompatible numbering, adjacent, unexplained. Name both campaigns and use one run-ID scheme |
| 3.12 | M | `[p87]`, `[p88]`, captions | `scipy.optimise_curve.fit()` **is not a real function**. It is `scipy.optimize.curve_fit` — which is what the code actually calls |
| 3.13 | m | `[p889]`, `[p869]`, `[p871]` | Literal `Eq. (??)` and empty `Eq. ()` cross-references |
| 3.14 | m | `[p831]` | *"In Fig. 4)"* — Fig. 4 is the granule diagram; this should be Fig. 3 |
| 3.15 | m | `[p884]` vs `[p885]` | Region bound changes from `\|X\| ≤ 2` to `\|X\| ≤ 0.5` between consecutive clauses |
| 3.16 | m | `[p821]`, `[p835]`, `[p924]` | Axial coordinate is `x` in figures and `z` in equations |
| 3.17 | m | `[p831]`, `[p834]`, `[p932]` | `C₀` is a mole fraction, `c₀` is mol m⁻³ — distinguished only by case. Also `ϵ` (Boltzmann exponent) vs `ε` (voidage) |

## Priority 3b — Figures (supervisor comment 3, done in code)

| # | Sev | Change |
|---|---|---|
| 3.18 | M | **Regenerate every figure** from the updated code. `h =` and `F-test p =` boxes, R² legend labels and χ²_red titles are all gone. Statistics remain in the CSVs and stdout for the presentation deck. Affected report figures: **Fig. 9** (predicted vs observed ← P1), **Fig. 10** (breakthrough fit ← P2/P4), **Fig. 11** (fractal validation ← P6, which carried the `h=`/`F-test p=` box the reviewer objected to) |
| 3.19 | m | Fix the Fig. 9/10 captions' `scipy.optimise_curve.fit()` (same as 3.12) |

---

## What is deliberately not in this list

Your four known gaps — goodness-of-fit & error statistics, the full mathematical
modelling/prediction section, the Python 3 reproducibility section, and optimal-model
selection. Items 2.16, 2.17 and 3.18 are written to feed into them when you get there.

Two inputs for the Python section that came out of this review, both verified by execution:

- **The analysis reproduces.** Re-running `new_runs_pipeline.py` in a clean environment
  (numpy 2.5.1, scipy 1.18.0, matplotlib 3.11.1, pandas 3.0.5) reproduced the committed
  results across 9 runs × 24 models × 16 numeric columns, with two values differing at the
  ninth significant figure. That is a strong claim most papers cannot make — state it.
- **The documented setup does not work.** There is no `venv/` at the repo root despite
  `CLAUDE.md` saying so, and the interpreter on `PATH` lacked scipy, matplotlib and pandas.
  The report also says Python 3.11; this ran on 3.13. `requirements.txt` is unpinned while
  `performance.py` requires numpy ≥ 2.0. Pin them before writing a reproducibility section.

# Academic Integrity Verification Report — Stage 2.5 (pre-review)

> **Status 2026-08-04:** findings in this file were carried through Stages 3–4.5 and
> resolved directly in `T32_PI05_Final_Report.docx`. See `09-final-integrity.md` (final
> verdict) and `11-process-record.md` (full resolution record) for current status. This
> file is retained unmodified as the original pre-review record.

**Manuscript** `src/T32_PI05_Final_Report.docx` (1250 paragraphs, ~9,400 words, 13 tables, 22 images, 205 equations)
**Mode** 1 (pre-review) · **Date** 2026-08-03 · **Verdict** **FAIL**
**Anchors** `[pN]` = paragraph index from `_source/extract_report.py` (see that file for the convention)

---

## Verdict

**FAIL.** Blocking: 5 SERIOUS, 9 MEDIUM. Under the pipeline's own rule a FAIL cannot
advance to Stage 3 until corrected or explicitly accepted. Because the reviewer is
read-only and you own the `.docx`, corrections are recorded in `06-change-list.md`
rather than applied, and Stage 3 proceeds with this report attached.

The single dominant failure is citation integrity. **Only 12 of 46 distinct in-text
citations (26%) resolve against the reference list.** This is not a formatting nit — it
means three quarters of the paper's technical claims cannot currently be traced to a
source, which is a desk-reject condition at any journal.

The good news, and it is genuinely good: **every source I traced turned out to be real.**
There is no evidence of fabricated literature. The problem is bookkeeping — wrong name
form, wrong year, entries never transferred into the list — not invention.

---

## Verification Summary

| Phase | Scope | Result |
|---|---|---|
| A1 Existence | 16 of 28 listed refs searched; all 13 load-bearing modelling refs covered | **0 fabricated** |
| A2 Bibliographic accuracy | author lists / years checked on searched refs | **2 wrong author lists, 1 year error** |
| A3 Ghost citations | full mechanical cross-check | **28 dangling, 12 orphaned, 6 year-clash** |
| B1 Citation context | spot-check of 8 load-bearing claims | **1 MAJOR_DISTORTION, 2 mis-attributions** |
| B2 Format consistency | APA 7 conformance | inconsistent; no field codes anywhere |
| C1–C2 Data consistency | tables vs. repo artefacts | **1 SERIOUS unit error, 1 non-physical value published** |
| C3 Caption fidelity | 11 figures + 13 tables | **duplicate numbering; a nonexistent API named twice** |
| C4 Experiment provenance | vs. `CLAUDE.md` measured basis | **two datasets conflated under one narrative** |
| D Originality | not run | see limitations |
| E Claim verification | risk-stratified, high-impact claims | **3 unsupported claims** |

**Coverage honesty.** I verified 16 of 28 references by search, chosen to cover every
reference that carries a modelling or data claim. The remaining 12 are indoor-air-quality
and DAC-context citations carrying no technical load; each has a well-formed DOI but I did
**not** independently confirm them. They are recorded below as UNVERIFIED, not as passed.
The ARS iron rule wants every reference to reach VERIFIED or NOT_FOUND; this pass does not
meet that bar for those 12, and Stage 4.5 must close the gap.

---

## IL-SERIOUS-1 — An AI chatbot is cited as a source for a mathematical claim

`[p885]`, §3.4.4:

> …if observational noise has standard deviation ε ≥ 0.04 — typical of NDIR sensors on
> packed-bed rigs — then no statistically meaningful distinction between the three kernels
> is possible on the experimentally accessible breakthrough region **(ChatGPT, n.d.; §8.2)**.

Three separate defects in one citation:

1. **ChatGPT is not a citable source.** A language model is not evidence. Every major
   publisher (Elsevier, which publishes *Adsorption Science & Technology*'s sibling
   titles, plus COPE and ICMJE) explicitly bars listing generative AI as a source or
   author. This alone is a desk-reject trigger.
2. **`§8.2` is a dangling pointer** — there is no §8.2 in this document, and no external
   work is named.
3. The claim it supports is **quantitative and load-bearing**: it is the justification for
   treating logistic, erf and Gudermannian kernels as experimentally indistinguishable,
   which is the analytical backbone of §3.4. It needs a real citation for the NDIR noise
   figure and a derivation (or a numerical demonstration) for the 0.04 sup-norm bound.

**Fix:** cite a real NDIR sensor specification for ε, derive or numerically verify the
sup-norm bound in an appendix, and delete the ChatGPT reference. If the bound came from a
model conversation, it must be re-derived and checked before it can stay in the paper.

---

## IL-SERIOUS-2 — 28 in-text citations have no reference-list entry

Mechanically produced by `_source/citation_crosscheck.py`. Full list:

| Cited as | Occurrences | Anchors | Diagnosis |
|---|---|---|---|
| `Hu et al., 2024` | 6 | p98, p103, p834, p859, p869, p882, p891 | **Real**: Hu, Q., Yang, X., Huang, L., Li, Y., Hao, L., Pei, Q., & Pei, X. (2024). *A critical review of breakthrough models with analytical solutions in a fixed-bed column.* J. Water Process Eng. **59**, 105065. Never listed |
| `Hu et al., 2019` | 4 | p902, p904, p906 | **Real**: Hu, Q., Xie, Y., Feng, C., & Zhang, Z. (2019). *Prediction of breakthrough behaviors using logistic, hyperbolic tangent and double exponential models…* Sep. Purif. Technol. **212**, 572–579. Never listed |
| `Kimani (2023)` | 4 | p895, p904, p906 | **Real**: Kimani et al., *Asymmetrical fixed-bed breakthrough curve modelling…* Chem. Eng. Res. Des. **201**, 446 (2023 online / 2024 issue). Never listed — **and misrepresented, see IL-SERIOUS-4** |
| `Karimi et al., 2023` | 3 | p101, p102, p900 | not searched; never listed |
| `Chen et al., 2020` | 3 | p811 | not searched; never listed |
| `Khim, 2019` | 2 | p859, p861 | **Author's given name.** This is Chu, K. H. (**2020**) — *already in your reference list* as an orphan. Both name form and year are wrong |
| `ipcc 2023`, `wmo 2023` | 2 each | p90, p91 | never listed |
| `qi 2011` | 2 | p96 | never listed |
| `jin et al., n.d.` | 2 | p102, p900 | never listed; `n.d.` on a technical claim |
| `Alba et al., 2026` | 1 | p986 | **Author's given name.** This is Cabrera-Codony et al. (2026) — *already in your list* as an orphan |
| `Clark (1987)` | 1 | p887 | **Real**: Clark, R. M. (1987). ES&T **21**(6), 573–580. Never listed, though §3.4.5 is built on it |
| `Ruthven, 1985` | 1 | p845 | never listed (the corpus has `Rutheven, ch6,8.txt` — note the misspelling) |
| `Al-Ghouti et al., 2020` | 1 | p987 | never listed (corpus has `al-ghouti2020.txt`) |
| `shariff 2012`, `jung 2017`, `siahpoosh 2009`, `hwang 1995`, `lin 2017`, `bollini 2012`, `kalyanaraman 2015`, `born 2024`, `kumar 2021`, `benzaoui 2017`, `vasanth n.d.`, `singapore 2023`, `ritchie 2025`, `etymonline 2024`, `wiktionary 2021` | 1 each | various | never listed |

Two of these — `Khim` and `Alba` — reveal a **systematic pattern worth fixing at the
source: the author is citing by given name rather than surname.** Chu, K. H. is "Khim
Hoong Chu"; Cabrera-Codony is "Alba Cabrera-Codony". Both papers *are* in the reference
list, so these are simultaneously a dangling citation and an orphaned reference. Check
every remaining citation for the same slip.

## IL-SERIOUS-3 — 12 reference-list entries are never cited

Azuma 2018 · Bos 2018 · **Cabrera-Codony 2026** · **Chu 2020** · Elfving 2021 ·
International Adsorption Society n.d. · International Energy Agency 2022 · Ji 2024 ·
**Langlo & Espedal 1994** · Online Etymology Dictionary n.d. · Pedrozo 2026 ·
**Shafeeyan 2014**

Cabrera-Codony and Chu are cited under wrong names (above) — fixing those clears two.
The rest split three ways:

- **Should be cited, currently isn't.** Shafeeyan et al. (2014), *A review of mathematical
  modeling of fixed-bed columns for carbon dioxide adsorption* (CERD 92, 961–988,
  verified) is the most on-topic review in your entire bibliography and appears nowhere in
  the text. §3.4 and §5 both need it.
- **Residue of the deleted DAC section.** Bos, Elfving, IEA, Ji, Pedrozo, Chuah and the
  DAC techno-economics cluster survive in the list after your co-author's comment
  *"took out the paragraphs on DAC, it's not needed for our thing"*. Either restore the
  framing or delete the references.
- **Off-topic.** Langlo & Espedal (1994) is verified real but concerns macrodispersion in
  **two-phase immiscible (oil/water)** flow. Nothing in a single-phase gas breakthrough
  study depends on it. Recommend deletion unless a specific argument needs it.

## IL-SERIOUS-4 — A cited source's conclusion is reversed

`[p897]`, §3.4.7:

> Kimani (2023) demonstrated that the Weibull function … outperformed normal and Gompertz
> functions (Adj R² > 0.97) due to its flexible inflexion point…

Kimani et al. actually conclude the opposite about Weibull's adequacy. Verbatim from the
published abstract: *"Although the Weibull, log-normal, and log-Gompertz functions have
floating inflection points, **only log-Gompertz function had a satisfactory fit regardless
of symmetry**"* — and separately, that *"the log-Bohart-Adams and fractal-like
Bohart-Adams models perfectly fit the curves regardless of symmetry."*

So the paper's headline is that **log-Gompertz and fractal-like Bohart–Adams** are the
performers; Weibull is named as having the right *structure* (a floating inflection point)
but **not** as the winner. The report cherry-picks the structural remark and presents it as
a performance ranking.

This matters beyond the sentence: it is used to justify including Weibull/Avrami (M14/M15)
in the model set. That justification is still defensible — but on the correct grounds, and
the correct citation also *strengthens* your fractal-like results, since Kimani
independently found fractal-like BA to be the best performer. **Rewrite to match the
source; it helps your argument rather than hurting it.**

## IL-SERIOUS-5 — A non-physical value is published as a measured parameter

`[p1127-1146]`, Table 3 *"Experimental Parameters of PEI@SiO₂ Fixed-Bed Adsorbers"*
reports an **Interstitial Velocity** column: 0.049 / 0.098 / 0.147 m s⁻¹.

These are the superficial velocities divided by ε = 0.30. Confirmed arithmetically:
Q = 0.05 lpm over A = π(0.425 cm)² = 0.5675 cm² gives u_superficial = 1.47 cm s⁻¹, and
1.47 / 0.30 = 4.9 cm s⁻¹ = 0.049 m s⁻¹ ✓.

ε = 0.30 is **the code's floor value, not a measurement.** `new_runs_pipeline.py:116`:

```python
eps_b = max(1.0 - rho_b / 800.0, 0.3)
```

ρ_p = 800 kg m⁻³ is an assumption, and `CLAUDE.md` states the consequence explicitly:

> The pipeline currently assumes ρ_p = 800 kg/m³, giving an unrealistically low ε≈0.16
> (floored to 0.30 in code). Real ρ_p is an open input; **do not treat ε or ε-based
> interstitial velocity as physical until supplied.**

Table 3 publishes exactly the quantity the project's own rules forbid presenting as
physical. **Fix:** report superficial velocity (which is measured and defensible), or keep
interstitial with an explicit footnote stating the assumed ρ_p, the floor, and that the
value is provisional pending the real pellet density. Owner: lab / Stampi-Bombelli.

---

## MEDIUM issues

**IL-MEDIUM-1 — Volumetric flow rate off by 1000×.** `[p1120-1122]`, Table 2:
*"Volume flow rate | 3.0 – 9.0 | cm3h-1"*. The swept range is 0.05–0.15 lpm =
50–150 cm³ min⁻¹ = **3000–9000 cm³ h⁻¹**. The numerals 3.0–9.0 are correct for **L h⁻¹**
(or dm³ h⁻¹); the unit is wrong, not the number. Fix the unit.

**IL-MEDIUM-2 — Two datasets presented as one.** Table 3 `[p1127]` lists runs 3, 4, 5, 6, 8
(the `new runs/` five). Table 4 `[p1148]` lists runs 1–9 as a 3×3 flow×concentration grid
(the `newest runs/` nine). They sit adjacent, share the caption style, and use
**incompatible run numbering** with no statement that they are different experimental
campaigns on different dates. A reader will assume "run 3" means the same thing in both.
Per `CLAUDE.md` these are 14 distinct real runs across two campaigns — say so.

**IL-MEDIUM-3 — Method described as batch when it was fixed-bed.** `[p1098]`, §7 opens
*"The equilibrium adsorption data was carried out in an experimental batch adsorber."*
Every experiment in this project is a fixed-bed column. This sentence appears to be
imported from another paper.

**IL-MEDIUM-4 — Table header names the wrong sorbent.** `[p1130]` reads *"Hgt. of **Carbon**
Bed"*. The sorbent is PEI@SiO₂. Same signature as IL-MEDIUM-3 — text carried in from an
activated-carbon study.

**IL-MEDIUM-5 — Wrong author list, Myers 2023.** Report `[p1238]`: *"Myers, T. G.,
Cabrera-Codony, A., & Valverde, A. (2023)"*. Verified actual authorship: **Myers, T. G.,
Valverde, A., Cabrera-Codony, A., & Font, F.** — Font is omitted and the middle two are
transposed.

**IL-MEDIUM-6 — Wrong author list, Wong 2021.** Report `[p1247]`: *"Wong, H. C., Low, H. Y.,
& Tan, M. C. (2021)"*. Verified actual authorship: **Wirawan, D., Kim, J., Wong, H. C.,
Low, H. Y., & Tan, M. C.** The first two authors are dropped and the third promoted to
first; the correct in-text form is *Wirawan et al. (2021)*.

**IL-MEDIUM-7 — Six year-clashes.** `xu` cited 2005 (list has 2024) · `hu` cited 2024, 2025
and 2019 (list has 2020–2023) · `myers` cited 2020 (list has 2023) · `schindler` cited
`n.d.` (list has 2012). The `Hu` cluster is the serious one: **the same author group is
cited under five different years across the paper**, and two of those years correspond to
real papers that were never listed.

**IL-MEDIUM-8 — A nonexistent API is named in two captions.** `[p87]`, `[p88]` and the
in-body captions: *"using scipy.optimise_curve.fit()"*. No such function exists. The real
call is `scipy.optimize.curve_fit`, which is what `fit.py` actually uses. In a paper whose
Next Steps promise a reproducibility section, a fabricated function name is costly.

**IL-MEDIUM-9 — Duplicate table numbers.** `Table 1)` is used twice (Gantt schedule;
Langmuir parameters) and `Table 2)` three times. No `SEQ`/`REF` fields exist anywhere in the
document, so nothing renumbers automatically and in-text pointers cannot be trusted.

---

## Phase E — Claim verification (high-impact claims)

| Claim | Anchor | Verdict |
|---|---|---|
| BA/Thomas/YN are notational variants of one logistic sigmoid | p876-p881 | **SUPPORTED.** Hu 2020 §2 and Chu 2020 both establish it. The report's own proof is correct. Cite Chu (2020) — it is in your list and is the canonical defence |
| Clark model reduces to logistic at n = 2 | p889 | **SUPPORTED** by Hu 2020 Eq. (1)–(2). But cross-ref reads literally `Eq. (??)` |
| Three sigmoid kernels indistinguishable below noise | p884-p885 | **UNSUPPORTED** — rests on `(ChatGPT, n.d.)`. See IL-SERIOUS-1 |
| Weibull outperforms normal and Gompertz | p897 | **MAJOR_DISTORTION** — see IL-SERIOUS-4 |
| Weibull and Avrami are near-equivalent for breakthrough | p897 | **UNSUPPORTED as cited.** Attributed to "Hu et al., (2021)", which is the *Gudermannian and error function* paper (verified: J. Mol. Liq. 323, 115061) and does not treat Weibull or Avrami. Your own runs show M14 ≡ M15 numerically identical, so the claim is *true in your data* — cite your own result, or find the correct source |
| Fractal-like models derive from fractal kinetics | p904 | **PARTIALLY SUPPORTED.** Attributed to "(Hu et al., 2019)", but fractal-like Gudermannian/erf is Hu **2021**. The 2019 paper covers logistic/tanh/double-exponential |
| PEI-based C3 sorbents perform well for CO₂ capture | p900 | **SCOPE STRETCH.** Wirawan/Wong (2021) is verified but concerns C3 **films** for *passive* DAC at ~400 ppm. This report uses C3 **granules** in a *forced-flow* packed bed at 5–15%. Different form factor, different regime, three orders of magnitude in concentration |

---

## Phase C4 — Experiment provenance vs. the project's measured basis

Checked against `CLAUDE.md` and `src/docs/experimental-results.md`.

- ✅ Column 38.6 cm × 8.5 mm i.d. — Table 2 `[p1108-1110]` gives 0.85 cm ✓ consistent.
- ✅ Volume of packing 11.92 cm³ — recomputed π(0.425)²·21 = 11.92 cm³ ✓ correct.
- ✅ Inlet velocity 1.47–4.41 cm s⁻¹ — recomputed ✓ correct as *superficial*.
- ❌ Interstitial velocity — IL-SERIOUS-5.
- ❌ Flow-rate units — IL-MEDIUM-1.
- ❌ Dataset conflation — IL-MEDIUM-2.
- ✅ **No synthetic data leakage.** `experimental-results.md` Appendix A is explicitly
  placeholder; I checked the report's §7 tables against it and found no overlap. Table 4's
  3×3 grid matches the real `newest runs/` inventory. **This is a clean result** —
  the paper does not present synthetic data as measured.

---

## Reproducibility check (executed, not asserted)

Ran the analysis pipeline in a fresh `.venv` (numpy 2.5.1, scipy 1.18.0, matplotlib
3.11.1, pandas 3.0.5) and compared regenerated outputs against the committed artefacts:

```
python src/solver/new_runs_pipeline.py      # 9 runs processed, 2 skipped as documented
(run, column) pairs differing by > 1e-9 relative: 2
  rel=1.305e-09  2026-07-10-conc15-flow0.05  chi2_red  M24
  rel=1.305e-09  2026-07-10-conc15-flow0.05  RSS       M24
```

**The analysis reproduces.** Across 9 runs × 24 models × 16 numeric columns, two values
differ in the last significant digit. Everything else is bit-stable under a different
library generation. That is a genuinely strong reproducibility result and the paper should
say so in its Python section.

Two caveats found while doing it, both belonging in that section:
- `CLAUDE.md` documents a committed `venv/` at the repo root. **There is none**, and the
  interpreter on `PATH` lacked scipy, matplotlib and pandas. The stated setup does not work
  as written.
- The report's Next Steps say *"Python 3.11"*; this ran on 3.13.

---

## Tool limitation disclaimer

Phase D (originality/plagiarism) was **not run** — it requires paragraph-level web search
against the full text and was out of proportion for a student design report. It is not a
pass; it is unexecuted. Twelve context references remain UNVERIFIED (listed above). Phase B
was a spot-check of 8 load-bearing claims, not the full corpus. Stage 4.5 must close all
three gaps.

## Verification audit trail

| Reference | Method | Result |
|---|---|---|
| Hu, Xie & Zhang 2020, Sep. Purif. Technol. 238, 116399 | WebSearch + local `hu2020-1.md` | VERIFIED exact |
| Hu, Huang, Yang & Liu 2021, J. Mol. Liq. 323, 115061 | WebSearch | VERIFIED exact |
| Hu et al. 2024, J. Water Process Eng. 59, 105065 | WebSearch | VERIFIED — **absent from list** |
| Hu, Xie, Feng & Zhang 2019, Sep. Purif. Technol. 212, 572–579 | WebSearch | VERIFIED — **absent from list** |
| Kimani et al., Chem. Eng. Res. Des. 201, 446 | WebSearch | VERIFIED — **absent from list, misquoted** |
| Clark 1987, ES&T 21(6), 573–580 | WebSearch | VERIFIED — **absent from list** |
| Chu 2020, Chem. Eng. J. 380, 122513 | WebSearch | VERIFIED — listed, cited as "Khim, 2019" |
| Cabrera-Codony et al. 2026, CCST 19, 100618 | WebSearch | VERIFIED — listed, cited as "Alba et al." |
| Myers et al. 2023, IJHMT 202, 123660 | WebSearch | VERIFIED — **author list wrong** |
| Stampi-Bombelli et al. 2024, IECR 63(26), 11637 | WebSearch | VERIFIED exact |
| Wirawan et al. 2021, Clean. Eng. Technol. 4, 100145 | WebSearch | VERIFIED — **author list wrong** |
| Shafeeyan et al. 2014, CERD 92, 961–988 | WebSearch | VERIFIED — orphaned |
| Langlo & Espedal 1994, Adv. Water Resour. 17(5), 297–316 | WebSearch | VERIFIED — orphaned, off-topic |
| Azuma 2018 · Bos 2018 · Carreiro-Martins 2014 · Chuah 2025 · de Joannis 2025 · Elfving 2021 · Hu 2022 · Hu 2023 · IAS n.d. · IEA 2022 · Ji 2024 · Juela 2021 · Norbäck 2008 · Online Etymology n.d. · Pedrozo 2026 · Schindler 2012 · Simoni 2010 · Tsai 2012 · Xu 2024 | not searched | **UNVERIFIED** |

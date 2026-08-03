# Claim-to-Reference Audit

**Question asked of every technical claim** *Does the cited paper actually support this
statement?*

**Method.** In-text citations extracted mechanically (`_source/citation_crosscheck.py`),
then every claim carrying a citation in §3.3–§3.5 and §5 read against the cited source.
Sixteen of 28 listed references were verified by search, covering all thirteen that carry a
technical claim.

**Verdict codes** — SUPPORTED · PARTIAL · **DISTORTED** (source says something materially
different) · **UNSUPPORTED** (no traceable source) · **MISATTRIBUTED** (real claim, wrong
paper)

---

## Headline

Of 46 distinct in-text citations, **12 (26%) resolve to a reference-list entry.** Of the
technical claims examined in detail, three are unsupported, two are misattributed and one
reverses its source's conclusion.

**The reassuring part, and it is worth stating plainly: every source I traced is real.**
Hu 2019, Hu 2024, Kimani, Clark 1987 — all verified to exist with correct titles and
venues. This is a bibliography-management failure, not a fabrication problem. That
distinction matters enormously for how much work the fix is: you are transcribing, not
re-researching.

---

## §3.4 — Breakthrough models

### C1 · `[p855]` — three sigmoid kernels in the literature
> "Traditional breakthrough models i.e. Bohart-Adams, Thomas, Yoon-Nelson are dissected and
> expressed as a single logistic function in three notations" — **(Hu et al., 2024)**

**Verdict: SUPPORTED, citation unresolvable.** The claim is correct and is exactly Hu et
al. (2020) §2's result, restated in Hu et al. (2024). But *"Hu et al., 2024"* appears in no
reference list entry. It is **Hu, Q., Yang, X., Huang, L., Li, Y., Hao, L., Pei, Q., &
Pei, X. (2024).** *A critical review of breakthrough models with analytical solutions in a
fixed-bed column.* J. Water Process Eng. **59**, 105065 — verified. Cited six times
`[p98, p103, p834, p859, p869, p882, p891]`, listed zero times.

### C2 · `[p857]` — linearisability of Bohart–Adams
> "Bohart-Adams and other models discussed below remain popular because it can be
> linearized, allowing unknown parameters to be determined via linear regression" —
> **(Hu et al., 2025)**

**Verdict: SUPPORTED in substance, UNSUPPORTED as cited.** No Hu 2025 exists in the list,
and I found no such paper. The claim is standard and is made explicitly by Chu (2020) —
which *is* in your list. Retarget.

### C3 · `[p859]`, `[p861]` — the Bohart–Adams analytical solution and its linear form
> "the appropriate analytical solution … is given as **(Khim, 2019; Hu et al., 2024)**"

**Verdict: SUPPORTED; both citations malformed.** *"Khim"* is the **given name** of Chu, K.
H. — Khim Hoong Chu — whose 2020 paper *is* in your reference list (and is orphaned). The
year is also wrong: 2020, not 2019. So one citation names an author by first name and
mis-dates them, while the correct entry sits unused twelve lines away.

This is the most diagnostic error in the paper: it tells you the citations were typed from
memory or from a reading note rather than generated from the reference list. **Check every
citation for the same slip** — `(Alba et al., 2026)` at `[p986]` is the same error against
Cabrera-Codony et al.

### C4 · `[p869]` — Thomas assumes Langmuir equilibrium
> "where it assumes Langmuir equilibrium **(Hu et al., 2024)**"

**Verdict: SUPPORTED**, same unresolvable citation as C1. Would be better served by Thomas
(1944) directly.

### C5 · `[p876-881]` — BA/Thomas/YN equivalence theorem
> "We show that these are notational variances of a single logistic sigmoid." *(no citation)*

**Verdict: SUPPORTED and correct.** I checked the algebra: factoring `k_BA c₀` from the
Bohart–Adams exponent and `k_T c₀` from the Thomas exponent both yield the Yoon–Nelson form,
giving `k_YN = k_BA c₀ = k_T c₀` and `τ = a₀x/uc₀ = q₀m/vc₀`. This matches Hu et al. (2020)
exactly and independently.

**The problem is that it carries no citation at all.** Presented as your own theorem, an
unattributed result that is the central contribution of two published papers (Hu 2020;
Chu 2020) reads as an originality claim you did not intend. Cite both. Your derivation can
stay — presenting it as independent confirmation is fine and even good — but the priority
must be acknowledged.

### C6 · `[p882-885]` — kernels indistinguishable below sensor noise
> "the residual sup-norm distance between any two of σ*, E*, G* … < 0.04 … if observational
> noise has standard deviation ε ≥ 0.04 — typical of NDIR sensors on packed-bed rigs — then
> no statistically meaningful distinction between the three kernels is possible" —
> **(ChatGPT, n.d.; §8.2)**

**Verdict: UNSUPPORTED — most serious citation defect in the paper.**

An AI chatbot is cited as the authority for a quantitative claim, alongside a dangling
`§8.2` pointer to a section that does not exist. See `00-integrity-report.md` IL-SERIOUS-1.

Compounding it, `[p884]` states the kernels are indistinguishable on `|X| ≤ 2` and `[p885]`
states the bound holds on `|X| ≤ 0.5` — the region changes between consecutive clauses, and
which one applies determines whether the argument works.

**This claim is probably true and is genuinely useful to your argument.** It needs: a real
NDIR datasheet for ε, and either a short derivation or a numerical check for the 0.04 bound
— which your own code could produce in a few lines.

### C7 · `[p887-889]` — the Clark model
> "The **Clark (1987)** model introduces asymmetry through an additional exponent n … At
> [n=2], this reduces to the logistic **Eq. (??)**"

**Verdict: SUPPORTED; reference missing, cross-reference broken.** Clark, R. M. (1987),
*Evaluating the cost and performance of field-scale granular activated carbon systems*,
Environ. Sci. Technol. **21**(6), 573–580 — **verified real, absent from your list.** The
n = 2 reduction is correct (Hu 2020, Eqs. 1–2). `Eq. (??)` is a literal unresolved field.

### C8 · `[p891]` — Gudermannian and error functions
> "In **Hu et al. (2024)**, the normalized Gudermannian and error functions … can define
> asymmetric breakthrough curves"

**Verdict: MISATTRIBUTED.** The normalised Gudermannian and error-function breakthrough
models are **Hu, Q., Huang, Q., Yang, D., & Liu, H. (2021)**, *Prediction of breakthrough
curves in a fixed-bed column based on normalized Gudermannian and error functions*, J. Mol.
Liq. **323**, 115061 — verified, **and already in your reference list** `[p1229]`. You cite
the wrong Hu paper while the right one sits unused.

### C9 · `[p895-897]` — Weibull outperforms normal and Gompertz
> "**Kimani (2023)** demonstrated that the Weibull function … outperformed normal and
> Gompertz functions (Adj R² > 0.97) due to its flexible inflexion point"

**Verdict: DISTORTED.** Source verified: Kimani et al., *Asymmetrical fixed-bed breakthrough
curve modelling: comparing simplistic, log-modified, fractal-like, and probability
distribution function models*, Chem. Eng. Res. Des. **201**, 446. Absent from your list.

Its actual conclusions:

> "The normal and Gompertz probability distribution functions were unable to adapt to
> asymmetry of the curves owing to their fixed inflection points. Although the Weibull,
> log-normal, and log-Gompertz functions have floating inflection points, **only
> log-Gompertz function had a satisfactory fit regardless of symmetry.** … The
> log-Bohart-Adams and fractal-like Bohart-Adams models perfectly fit the curves regardless
> of symmetry."

So Kimani ranks **log-Gompertz** and **fractal-like Bohart–Adams** as the performers.
Weibull is credited with the right *structure* — a floating inflection point — but
explicitly **not** with a satisfactory fit. The report converts a structural remark into a
performance ranking and attributes a number (Adj R² > 0.97) I could not locate in the
source.

**This works in your favour once corrected.** Kimani independently finding fractal-like
Bohart–Adams to be the best performer is direct external corroboration of your own result
that M23/M10/M11 dominate. Stating it accurately strengthens §3.5.2 and §8.

### C10 · `[p897]` — Weibull and Avrami are near-equivalent
> "**Hu et al., (2021)** shows that the Weibull and Avrami models are nearly mathematically
> equivalent when describing breakthrough curves"

**Verdict: MISATTRIBUTED.** Hu et al. (2021) is the Gudermannian/error-function paper
(verified above); it does not treat Weibull or Avrami.

**But the claim is true, and you can prove it yourself.** Your own committed output shows
M14 (Weibull) and M15 (Avrami) returning *bit-identical* statistics on every run —
`R² = 0.970766, RMSE = 0.038142, AICc = −6543.93` in the run I executed. That is stronger
evidence than a citation. Report it as your own finding.

---

## §3.5 — Review of prior solutions

### C11 · `[p900]` — PEI-based C3 sorbents perform well
> "Prior work has shown that PEI-based silica C3 sorbents perform well for CO₂ capture" —
> **(Schindler, n.d.; Stampi-Bombelli et al., 2024)**

**Verdict: PARTIAL / scope stretch.** Schindler is listed as **2012**, not `n.d.` — and is a
German-language dissertation on **metal-organic coordination polymers**, not PEI@SiO₂.
Stampi-Bombelli (2024) is verified but studies **amine-functionalised γ-alumina pellets**,
not PEI-impregnated silica.

Neither cited source is about the material the sentence is about. The right citation is
**Cabrera-Codony et al. (2026)** — *An analytical breakthrough model for CO₂ adsorption on
PEI-impregnated silica* — which is in your reference list, orphaned, and precisely on
topic. (It is the one you cite elsewhere as `(Alba et al., 2026)`.)

### C12 · `[p902]` — classical models are centrosymmetric
> "The Bohart-Adams, Thomas, and Yoon-Nelson models are mathematically equivalent forms of
> the logistic function, representing a centrosymmetric S-shaped curve with an inflection
> point fixed at [C/C₀] = 0.5" — **(Hu et al., 2019)**

**Verdict: SUPPORTED; reference missing.** Hu, Q., Xie, Y., Feng, C., & Zhang, Z. (2019),
Sep. Purif. Technol. **212**, 572–579 — verified real, absent from the list. The claim is
correct: Hu 2020 Table 2 gives `t_i = t₅₀ = τ` for all three.

### C13 · `[p904]` — fractal-like models
> "Fractal-like models introduce a time-dependent rate coefficient derived from fractal
> kinetics, which accounts for the heterogeneous, diffusion-limited nature of adsorption" —
> **(Hu et al., 2019)**

**Verdict: MISATTRIBUTED.** Fractal-like Gudermannian and error models are Hu **2021**
(verified: *"fractal-like Gudermannian and fractal-like error models capable of describing
diffusion-limited processes on heterogeneous surfaces"*). The 2019 paper covers logistic,
hyperbolic tangent and double-exponential models. Kimani is the other correct anchor for
fractal-like Bohart–Adams.

### C14 · `[p906]` — fractal models expected to fit best
> "the fractal-Gudermannian and fractal-ERF are expected to provide superior fits when the
> breakthrough data exhibit asymmetry"

**Verdict: SUPPORTED and borne out.** Consistent with Hu 2021 and Kimani, and confirmed by
your own results (M10/M11 win four of five original runs). Note the tense — "expected to" —
sits oddly in a report whose data already settles the question. Once §4 is written this
should become a statement of result.

---

## §5 — Mathematical modelling

### C15 · `[p913]` — DAC regime and LDF resistances
> "In DAC processes, a trace level of CO₂ adsorbed from an inert gas carrier such that a
> single component model applies in dry conditions." *(no citation)*

**Verdict: UNSUPPORTED, and inconsistent with the experiment.** No citation. More
importantly the premise — trace CO₂ — is false for this study's 5–15% feed. See
`05-methodology-flow.md` F6.

### C16 · `[p986-987]` — limitations
> **(Alba et al., 2026)** and **(Al-Ghouti et al., 2020)**

**Verdict: both unresolvable as written.** `Alba` is Cabrera-Codony's given name (source is
in your list, orphaned). Al-Ghouti is absent from the list though the corpus holds
`literature/modelling/al-ghouti2020.txt`.

---

## Fix order

| Step | Action | Effort |
|---|---|---|
| 1 | Add the four verified missing references: **Hu 2024, Hu 2019, Kimani, Clark 1987** | 15 min — resolves 15 citations |
| 2 | Fix the two given-name citations: `Khim`→Chu (2020), `Alba`→Cabrera-Codony (2026) | 5 min — resolves 2 dangling + 2 orphans |
| 3 | **Rewrite C9** to match Kimani's actual conclusion | 20 min — strengthens your result |
| 4 | Retarget C8, C10, C13 to Hu **2021** and Kimani | 15 min |
| 5 | Delete the ChatGPT citation (C6); source ε and derive the bound | 1–2 h |
| 6 | Retarget C11 to Cabrera-Codony (2026) | 5 min |
| 7 | Add Chu (2020) + Hu (2020) to the C5 theorem | 5 min |
| 8 | Add the remaining primaries — see `02-lit-completeness.md` | 1 h |

Steps 1, 2, 4, 6 and 7 total under an hour and clear the majority of the findings.

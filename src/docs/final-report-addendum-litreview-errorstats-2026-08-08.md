# Addendum — Hu et al. 2024 gap-fill for `src/T32_PI05_Final_Report.docx`

**Purpose.** `/ars-3w` scan of `src/docs/literature/lecturer-references/hu2024__MAIN.md`/`.pdf`
(Hu, Q. et al. 2024, *J. Water Process Eng.* 59:105065), scoped to two asks: (1) literature
review on breakthrough models + assumptions, (2) error statistics + parameter estimation
strategy — for the **Final Report** (`src/T32_PI05_Final_Report.docx`; the Interim Report
you pointed at is the 18 May 2026 submission and is frozen/superseded).

**Scope: gap-fill only.** The Final Report already went through a full ARS review pipeline
(resolved 2026-08-04, conditional pass, `src/docs/review/09-`–`11-`). §3.6 (14 model
subsections), §7 (fitting performance), and §8.1 (7 stated assumptions) are already
thorough and are **not** touched below. Everything here targets genuine remaining gaps,
found by a read-only paragraph-index extraction of the current docx
(`zipfile`/`ElementTree`, no edits made) cross-checked against the actual Hu2024 PDF pages
10–11 and 12–16 (the `.md` extraction has mangled equations — do not copy formulas from it).

**How to use this file.** Each block below names the exact heading/paragraph to edit in
Word (paragraph indices are from today's extraction and will drift if you edit the doc
before pasting — use the heading text as the primary anchor, the index as a cross-check).
Paste the "New text" as-is or adapt wording; every citation used is already in the report's
reference list (no new references needed).

---

## Block 1 — Assumptions reconciliation (§3.4, para ~166)

**Problem.** §3.4's assumption list has a duplicate "(ii)" label and — unlike §8.1's own
7-assumption list for the minimal kinetic model (which explicitly states "A2. Isothermal")
— **omits isothermal entirely**, even though Hu et al. (2024) list isothermal as one of
their six governing assumptions (§2 of the source paper). The two assumption lists in the
same report should describe the same governing PDE consistently.

**Current text (§3.4, last sentence before the mass-balance equation):**
> "With the assumptions: (i) plug flow in the axial direction; (ii) negligible radial
> dispersion; (ii) a linear driving force for solid adsorption; (iii) uniformly spherical
> adsorbent particles and; (iv) constant geometric dimensions, interstitial velocity, and
> void fraction (Hu et al., 2024)."

**New text:**
> "With the assumptions: (i) isothermal operation; (ii) plug flow in the axial direction;
> (iii) negligible radial dispersion; (iv) a linear driving force for solid adsorption;
> (v) uniformly spherical adsorbent particles and; (vi) constant geometric dimensions,
> interstitial velocity, and void fraction (Hu et al., 2024). Isothermal operation is the
> most consequential of these for this project specifically: Hu et al. (2024) is a
> critical review of *liquid-phase* water-treatment breakthrough data, where the
> adsorbate's heat of interaction is carried away by a large-heat-capacity solvent and the
> isothermal assumption is comparatively benign. This project's system is gas-phase
> CO₂ chemisorption on an amine sorbent, a strongly exothermic reaction (Cabrera-Codony et
> al., 2026) — so isothermal operation, listed again explicitly as assumption A2 of the
> minimal kinetic model in §8.1, is carried through both this section and §8 as a stated
> assumption, not a validated one, and should be read as such."

---

## Block 2 — WHY/HOW/WHAT model-family synthesis (new §3.7.4, after current §3.7.3)

**Problem.** §3.7.1–3.7.3 already give good prose on symmetric vs. asymmetric models, but
there is no compact cross-family comparison — the format the invoked scan is meant to
produce. Every cell below cites either Hu2024 or a finding already stated elsewhere in
*this* report (§3.6.x, §7.1) — nothing new is asserted.

**New subsection — "3.7.4 Model-family comparison":**

> | Family | WHY (motivating idea) | HOW (derivation) | WHAT (strongest evidence) |
> |---|---|---|---|
> | Traditional logistic (Bohart-Adams / Thomas / Yoon-Nelson, §3.6.1–§3.6.4) | Rate of uptake proportional to residual bed capacity or Langmuir/probability kinetics; assumes a time-independent rate constant and a symmetric front | All three reduce algebraically to one logistic sigmoid (§3.6.4 Theorem); historically linearisable for straight-line parameter fitting (§3.6.1) | Hu et al. (2019): Adj.R² = 0.9879 on norfloxacin/GAC data, "significantly lower than fractal-modified versions" (§3.7.1); serves as the M01 baseline every other model is compared against in this project (§7.1–7.2) |
> | Clark / modified dose-response (§3.6.5, §3.6.9) | Add one shape parameter to capture asymmetric MTZ shape beyond the logistic family's fixed inflection | Clark embeds a Freundlich exponent *n* (n=2 recovers the logistic, §3.6.5); modified dose-response parameterises directly on t₅₀ instead of a rate constant (§3.6.9, Yan et al. 2001) | Minimal one-parameter extension of the logistic family; `experimental-results.md` notes Clark's *n* hits its fitting lower bound in some runs of this project's own data |
> | Fractal-like (§3.6.8) | Time-decaying rate constant k = k₀t⁻ʰ to capture diffusion-limited/heterogeneous-site asymmetry (Hu et al., 2021, 2024) | Substitute k₀t⁻ʰ into the BA/Thomas/YN/Clark/Gudermannian/erf kernels | Wins outright in 4 of 5 runs by AICc (M10/M11, §7.1), ΔAICc ≫10 within every run; h = 0.42–0.87 across runs; decisive by nested F-test for the fractal exponent (F>10 000, p≪0.001, `experimental-results.md` §5) |
> | Empirical S-curve (Weibull / Avrami / Gompertz / tanh / log-normal, §3.6.7, §3.6.10) | Pure curve-shape flexibility via probability-distribution CDFs with floating inflection points; no claim to a specific mass-transfer mechanism | Weibull, Avrami, (log-)Gompertz, tanh and log-normal kernels | Weibull (M14) wins run 4 outright (§7.1); Weibull and Avrami return statistically indistinguishable fits in this project's own data — identical R², RMSE and AICc to ≥5 s.f. (§3.6.7); Kimani (2024): only log-Gompertz fit satisfactorily regardless of curve symmetry |
> | Approximate analytical (Klinkenberg / Dima, §3.6.11) | Retain a link to the underlying LDF mass-transfer PDE via an asymptotic or Laplace-transform closed form, unlike the purely empirical family | Klinkenberg: erf-based solution valid only for bed Stanton number ζ≥2 and dimensionless time τ_K≥1; Dima et al. (2024): Laplace-transform travelling-wave erf solution | This column does not meet Klinkenberg's ζ/τ_K validity bounds (§3.6.11) — the only family excluded from the model-preference ranking on a stated *validity* criterion rather than a fit-quality one |
> | Implicit mechanistic (Chern–Chien, §3.6.12) | Most mechanistically grounded closed form, derived from constant-pattern wave theory with an explicit Langmuir or Freundlich isotherm embedded | Solves implicitly for *t* at a given C/C₀ = x (root-finding required at every point); Hu et al. (2024, §5.5) note this ODR-style fit means standard error statistics don't objectively reflect its goodness of fit — residual plots are the recommended diagnostic instead | Converges formally but returns non-finite RSS / undefined R² in every run of this project (§3.6.12); retained for completeness, excluded from ranking, same treatment as Klinkenberg |
>
> **Synthesis.** *Common WHY*: every family targets the same physical signature — an
> S-shaped mass-transfer-zone front — with as few, ideally physically-interpretable,
> free parameters as possible. *Divergent HOW*: the six families span a spectrum from
> purely empirical curve-matching (Weibull/Avrami/Gompertz) through algebraically
> flexible but still closed-form (Clark/MDR/fractal-like) to explicitly mechanism-derived
> but implicit (Chern–Chien) or validity-bounded mechanistic (Klinkenberg/Dima) — and the
> mechanistic end of that spectrum is *not* easier to fit in practice here: Chern–Chien
> fails to converge and Klinkenberg's validity bounds aren't met, while the empirical and
> fractal-like families fit cleanly. *Strongest WHAT*: fractal-like asymmetric kernels
> dominate this project's own AICc ranking (4 of 5 runs, §7.1), consistent with the
> literature already cited in §3.7.2 (Kimani 2024; Hu et al. 2021). *Unresolved gap*:
> §3.6.4's own Remark shows the fractal-like kernels (M10, M11) and the plain logistic
> family are visually indistinguishable once slope-matched (sup-norm ≤0.031), and §7.1
> already states that AICc here "is correctly identifying, per run, which of several
> near-equivalent functional forms best absorbs that run's particular noise realisation —
> it is not resolving a genuine physical distinction between the kernels." This table
> answers *which family fits best*, not *which mechanism operates* — the latter is what
> the mechanistic model of §8 exists to eventually answer once it is fitted to data,
> which §8's own framing paragraph already states has not yet been done.

---

## Block 3 — Error statistics & parameter estimation strategy (expand §8.2)

**Problem.** §8.2 "Parameter estimation strategy" is currently one sentence — it asserts
nonlinear fitting was used but never justifies the choice, and never defines the
error-statistics vocabulary §7.1 already uses (AICc, ΔAICc, the `W_AICc` caveat). This is
the section that most directly answers your "error statistics + parameter estimation
strategy" ask.

**Insert after the current §8.2 opening paragraph** (the one ending "...were determined
using non-linear fitting methods to the experimental data."), **before Table 7**:

> All free parameters — for both the minimal kinetic model of §8.1 and the 24-model
> registry of §3.6 — were determined by nonlinear least-squares regression
> (`scipy.optimize.curve_fit`, trust-region-reflective algorithm, 12 multi-start
> initialisations per model, §4.1) rather than by linearising each model to a straight
> line.
>
> This choice follows Hu et al. (2024, §5.5) directly. Linearising a breakthrough model —
> for example, the Thomas model's linear form ln(c₀/c − 1) = k_Tq₀m/ν − k_Tc₀t — implicitly
> transforms the response variable and alters its error structure: ordinary least squares
> on the linearised form assumes constant-variance, normally-distributed residuals in the
> *transformed* coordinate, an assumption the untransformed C/C₀ data need not satisfy.
> The transform is also undefined at C/C₀ = 0 and C/C₀ = 1, so a linearised fit must
> exclude data at and near breakthrough and near saturation — precisely the regions this
> project's SOP acceptance criteria (§4.3.1) are built to capture completely. Hu et al.
> (2024) report that exclusion inflates linearised parameter error most sharply near
> those same two limits. Nonlinear regression avoids both problems, fitting the
> untransformed C/C₀ response directly with no domain exclusion, and extends without
> modification to the fractal-like and two-component models (§3.6.8, §3.6.14) that have
> no closed linear form at all.
>
> A second methodological choice this makes explicit: every model in §3.6 is fitted to
> the *complete* breakthrough curve (C/C₀ → 1 per the SOP's t_E criterion, §4.3.1), not a
> curve truncated before saturation. Hu et al. (2024, §5.2) quantify why this matters:
> fitting the Thomas model to progressively truncated methylene-blue breakthrough data
> (100% → 20% of the complete curve) produced relative errors in the fitted rate constant
> k_T of up to 110.8%, 26.1% and 47.5% at three influent concentrations — even though the
> truncated fits themselves still reported Adj.R² > 0.99. A good statistical fit to a
> partial curve does not imply an accurate parameter estimate. This is direct external
> support for a caveat this project's own analysis already carries
> (`experimental-results.md`, `sensitivity-analysis.md`): capacity metrics such as q_dyn
> are not yet reliably comparable across runs because the acquisition endpoint is not
> fixed at a consistent C/C₀ — Hu et al.'s truncation result is evidence for why that
> endpoint should be standardised (e.g. to C/C₀ = 0.98) before such comparisons are drawn.

**Insert as a new short subsection before Table 9 (or after it, as a closing paragraph of
§8.2)** — this defines the vocabulary §7.1 already uses without definition:

> Model comparison in §7.1 is reported by ΔAICc; the underlying definitions (Hu et al.,
> 2024, §4, their Eqs. 55–59) are: the coefficient of determination
> R² = 1 − Σ(yᵢ−ŷᵢ)²/Σ(yᵢ−ȳ)²; the parameter-count-penalised Adjusted R²; the nested
> F-test F = [(RSS₁−RSS₂)/(df₁−df₂)]/[RSS₂/df₂] for comparing a simpler model against a
> nested, more complex one; the Akaike Information Criterion, AIC = n·ln(RSS/n) + 2p for
> n/p ≥ 40, or a small-sample-corrected form for n/p < 40; and the Akaike weight
> W_A = 1/(1+exp(0.5·ΔAIC)), which §7.1 already correctly notes trivially equals 0.5 for
> the best-fitting model by construction and should not be read as a normalised
> probability.
>
> *(Two things worth checking directly against the PDF/code before this goes to print,
> flagged rather than silently resolved:*
> *(a) the printed Adjusted R² formula in Hu et al. (2024) appeared, on this reading of
> PDF p.10, as 1 − (1−R²)(n−1)/(n−p) — note this differs by one in the denominator from
> the standard textbook form (n−1)/(n−p−1), and from the version quoted in
> `src/docs/prompts/prompt01.md`. Worth a direct visual check of PDF p.10 before quoting
> an exact denominator in the report.*
> *(b) every run in this project has n/p ≫ 40 (n = 255–1432 points, p ≤ 5 parameters), so
> by Hu et al.'s own Eq. 58 the simple AIC branch applies, not the small-sample-corrected
> branch — worth confirming that the column `breakthrough_fit/stats.py` labels "AICc"
> matches this definition, rather than the more common Hurvich–Tsai small-sample
> correction, which is a different formula that happens to share the same name.)*
>
> Hu et al. (2024, §4) caution that R²/Adj.R²/AIC alone are not sufficient to evaluate
> fitting quality, and recommend the residual plot as the more reliable diagnostic, since
> it can reveal non-constant variance or non-random structure a single summary statistic
> cannot. This is directly relevant here: the response C/C₀ is bounded on [0,1], so
> residual variance is structurally pinched near the breakthrough and saturation limits
> (heteroscedastic by construction) — an assumption the F-test/AICc comparisons above do
> not themselves test. This is not unique to this project: Hu et al. (2024) apply the
> same F-test/AIC machinery to their own worked example without separately testing
> residual normality or homoscedasticity — but it is worth stating plainly here, per the
> caveat already carried in `experimental-results.md` §5.
>
> One model-family-specific note: the traditional Bohart-Adams model has a widely-used
> but invalid oversimplified exponential form, C/C₀ = exp[k_BAc₀t − k_BAa₀x/u] (Hu et al.,
> 2024, §5.3, their Eq. 60), obtained by dropping the unity term from the logistic
> denominator's exponential rather than treating it as negligible only for large
> k_BAc₀t. This form is not used anywhere in this project's model registry; the n-order
> Bohart-Adams generalisation used instead (M22, §3.6.13, Hu et al. 2021) is the form Hu
> et al. (2024, §5.3) recommend in its place for asymmetric curves.

---

## Noticed while reading, not fixed

Per the project's "flag, don't silently fix" rule — surfaced for your call, not applied:

1. **§3.6.2 (para 203, Thomas model)** still has the unresolved placeholder "Eqs. () and
   ()" — carried over unchanged from the Interim Report into the Final Report. Small fix,
   just needs the actual equation numbers filled in.
2. The assumption-list bug in §3.4 (duplicate "(ii)", missing isothermal) is addressed by
   Block 1 above — noted here only so it isn't missed if Block 1 is skipped.

*(An earlier pass of this addendum also flagged a possibly-missing "Table 8" in §8.2 —
dropped after re-checking: the read-only extraction script used to inspect the docx only
walks top-level paragraphs and does not descend into Word table objects, so it cannot see
table contents at all. Table 8 is very likely present and fine; this was a limitation of
the extraction method, not a finding about the document.)*

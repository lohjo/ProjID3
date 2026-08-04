# Literature Completeness Audit

> **Status 2026-08-04:** the missing/duplicated model citations identified here were added
> in `T32_PI05_Final_Report.docx` §3.6.8–3.6.14 (17 previously-uncited models, each with a
> real equation and citation). See `11-process-record.md`. This file is retained unmodified
> as the original audit record.

**Reviewing as for** *Adsorption Science & Technology*
**Question asked** which breakthrough models are missing, duplicated, outdated or
unnecessary — and would each omission *materially* affect the paper?

---

## The structural finding that outranks every individual gap

**§3.4 introduces seven models. The analysis fits twenty-four.**

Literature review covers: Bohart–Adams, Thomas, Yoon–Nelson, Clark, Gudermannian, Error
function, Weibull/Avrami. §3.5.2 adds fractal-like models in prose, with no equations.

The code registry (`models.py`, M01–M24) additionally fits: Wolborska (M05), Klinkenberg
(M16), Dose-Response/Yan (M04), Gompertz (M12), Log-Normal (M09), Tanh (M08), Dima (M17),
Chern–Chien Langmuir and Freundlich (M18/M19), n-order Bohart–Adams (M22), fractal-like
Bohart–Adams (M23), fractal Gudermannian (M10), fractal error (M11).

`experimental-results.md` reports that **M10 and M11 win outright in four of the five
original runs**, and M23 ranks highest by mean Adj. R² among the prompt-specified models.
So the models that carry your headline result are the ones the reader has never been
introduced to.

This is the difference between a reviewer writing "minor revision" and "major revision".
Every model that appears in a results table needs an equation, a parameter definition, and
a citation in §3.4. **Materially affects the paper: yes, more than anything else in this
document.**

---

## Missing primary sources (every classical model is cited only through secondaries)

| Model | Primary source | Status | Material? |
|---|---|---|---|
| Bohart–Adams | Bohart & Adams (1920) *J. Am. Chem. Soc.* **42**, 523–544 | absent | **Yes.** §3.4.1 is built on it; a 1920 centenary model cited only via a 2024 review reads as unread |
| Thomas | Thomas (1944) *J. Am. Chem. Soc.* **66**, 1664–1666 | absent | **Yes.** Same reason; §3.4.2 asserts Langmuir equilibrium, which is Thomas's own assumption |
| Yoon–Nelson | Yoon & Nelson (1984) *Am. Ind. Hyg. Assoc. J.* **45**, 509–516 | absent | **Yes.** §3.4.3 states the probability argument that is the paper's entire content |
| Clark | Clark (1987) *Environ. Sci. Technol.* **21**(6), 573–580 — **verified real** | cited in text `[p887]`, absent from list | **Yes.** Trivially fixable |
| Langmuir | Langmuir (1918) *J. Am. Chem. Soc.* **40**, 1361 | absent | **Yes.** §3.3.1 gives a full derivation with no attribution |
| Toth | Toth (1971) | `[p851]` cites a bare `(1971)` with no author | **Yes.** Dangling year; the whole project's isotherm |
| Wolborska | Wolborska (1989) *Water Res.* **23**, 85–91 | absent | **Yes** — see below |
| Klinkenberg | Klinkenberg (1948) | absent | **Yes** — M16 is fitted and reported |
| Chern–Chien | Chern & Chien (2002) | absent | Moderate — M18/M19 never converge (see below) |
| Yan dose-response | Yan et al. (2001) | absent | **Yes** — M04 is fitted; Hu (2020) treats it as a core model |

For a journal reviewer, uncited primaries are the single most reliable signal that a
literature review was assembled from reviews rather than sources. Ten of them is not
recoverable by argument — it has to be fixed.

---

## Wolborska — the most consequential single omission

You **fit** Wolborska (M05). Your own output shows it behaving oddly: in the run I
executed it reports R² = 0.949 on a **restricted early-time window** while every other
model is fitted on the full curve, so its statistics are not comparable to the rest of the
table.

Hu et al. (2020) — the paper you rely on most — makes a specific methodological point about
exactly this, and it is one of that paper's five stated contributions:

> The Wolborska model … does not represent a S-shaped curve and thereby fails to describe
> the breakthrough curve completely. It may be only applied to the region of low
> breakthrough concentration … **In our opinion, the use of the Wolborska model should be
> avoided for the modeling of the dynamic behaviours in a fixed-bed column.**

You have the source (`hu2020-1.md`), you fit the model, and the report never mentions
either. A reviewer who knows Hu 2020 — likely, at this venue — will notice immediately.

**Material: yes.** Two sentences in §3.4 acknowledging that Wolborska is fitted on a
restricted window and reported for completeness, citing Hu 2020's caution, converts a
liability into evidence that you read your sources critically.

---

## Missing methodological literature

**Chu (2020)** — *in your reference list, never cited* (it is the "Khim, 2019" ghost). This
is the canonical modern defence of Bohart–Adams and of the BA/Thomas/YN equivalence that
§3.4.4 proves as a theorem. Citing it costs one line and immediately grounds your central
analytical claim in the literature rather than in your own algebra. **Material: yes.**

Worth knowing: Chu (2020) drew a published **Comment** and a **Rebuttal** in *Chem. Eng. J.*
(2020). §3.4.4 asserts the equivalence as settled. At *Adsorption Science & Technology* a
reviewer may well be aware the point was contested. Acknowledging the exchange costs a
clause and pre-empts the objection.

**Shafeeyan, Wan Daud & Shamiri (2014)**, *A review of mathematical modeling of fixed-bed
columns for carbon dioxide adsorption*, CERD **92**, 961–988 — *in your list, never cited*
(verified). This is the most on-topic review in your entire bibliography: fixed-bed +
mathematical modelling + CO₂. It belongs in §3.4's opening and in §5. **Material: yes.**

**Constant-pattern / LUB theory.** You compute `L_MTZ` and ψ and report them per run, but
no constant-pattern literature is cited anywhere. Sircar & Kumar (1983) is the standard
anchor (and appears in Hu 2020's own reference list). Your `mechanistic-model.md` §D.3
already develops the travelling-wave analysis — the report simply never connects to it.
**Material: yes**, because L_MTZ is one of your reported metrics.

**Wheeler–Jonas** — standard in *gas-phase* fixed-bed adsorption, absent. Given that almost
every model you cite comes from *aqueous* adsorption (nitrate, methylene blue, aniline,
norfloxacin, bisphenol-A), a gas-phase anchor would strengthen the transfer argument.
**Material: moderate** — worth one sentence.

**Kimani et al.** (Chem. Eng. Res. Des. **201**, 446) — cited four times, never listed, and
its conclusion is reversed in your text. See `03-claim-to-reference.md`. **Material: yes.**

**Hu et al. (2024)**, J. Water Process Eng. **59**, 105065, and **Hu et al. (2019)**, Sep.
Purif. Technol. **212**, 572–579 — cited ten times between them, neither listed. Both
verified real. **Material: yes.**

---

## Duplicated and over-concentrated

**Six papers from one research group.** Hu 2019, 2020, 2021, 2022, 2023, 2024 — four listed,
two cited-but-unlisted. §3.4 and §3.5 are built almost entirely on this group's output.

At a specialist venue this reads as a single-source review. Two of the four listed are also
marginal to your study: Hu 2022 is **multicomponent** adsorption (you have one adsorbing
component by assumption A6) and Hu 2023 is an **isotherm** review for **aqueous
contaminants** (your system is gas-phase). Neither is cited in the text.

**Recommendation:** keep Hu 2019/2020/2021/2024 (all load-bearing), drop 2022 and 2023
unless a specific claim needs them, and balance §3.4 with Chu (2020), Shafeeyan (2014),
Kimani, and the primaries. That is a stronger review with roughly the same reference count.

**Aqueous-phase dominance.** Nitrate on chitosan-Fe(III), methylene blue on silica, aniline
on jute, norfloxacin on GAC, sulfamethoxazole on bagasse, bisphenol-A on polyaniline. Every
empirical model in §3.4 is validated in the literature on liquid-phase systems, and your
system is gas-phase at 5–15% CO₂. The models transfer — but the paper should *argue* that
they transfer rather than assume it. **Material: yes**, and it is a one-paragraph fix that
a reviewer will read as sophistication.

---

## Unnecessary or unsuitable for this venue

| Reference | Problem | Recommendation |
|---|---|---|
| Online Etymology Dictionary (n.d.) `[p1240]`; Wiktionary `[p810]` | Etymology of "adsorb" from non-scholarly web sources | **Delete.** In a journal submission this is a hard negative signal. IUPAC's definition, if you want one |
| International Adsorption Society (n.d.) `[p1233]` | Society webpage cited for "what is adsorption" | **Delete.** Replace with Ruthven or Worch |
| Langlo & Espedal (1994) `[p1237]` | **Verified real**, but concerns macrodispersion in **two-phase immiscible (oil/water)** flow. Orphaned | **Delete** unless a specific dispersion argument needs it — and if it does, cite a single-phase gas source instead |
| Schindler (2012) `[p1242]` | German-language doctoral thesis, cited as "(Schindler, n.d.)" `[p900]`, used to support a claim about PEI@SiO₂ sorbents | **Replace.** A reviewer cannot check it; the claim deserves an accessible source |
| DAC techno-economics cluster — IEA 2022, Ji 2024, de Joannis 2025, Pedrozo 2026, Elfving 2021, Bos 2018 | Six references, all orphaned, survivors of the deleted DAC section (co-author comment: *"took out the paragraphs on DAC, it's not needed for our thing"*) | **Delete**, or restore a short framing paragraph. Carrying six uncited techno-economics papers signals an unpruned bibliography |
| IAQ health cluster — Azuma 2018, Carreiro-Martins 2014, Norbäck 2008, Simoni 2010, Tsai 2012 | Five references motivating indoor CO₂ health effects | **Reduce to two.** Appropriate for an IAQ journal; disproportionate at *Adsorption Science & Technology*, whose readers need the adsorption problem motivated, not the health problem. See the scope finding in `05-methodology-flow.md` |

Deleting the six DAC and three non-scholarly entries and trimming IAQ to two frees roughly
twelve slots — more than enough for all ten missing primaries at no net length cost.

---

## Two models fitted but broken

Not a literature gap, but it belongs in the same conversation. In the run I executed:

```
M19  Chern-Chien Freundlich   4  nan  inf  inf  nan  inf  True
M18  Chern-Chien Langmuir     4  nan  inf  inf  nan  inf  True
```

Both report `converged = True` while producing NaN R² and infinite RSS. They are in the
model set, they are uncited in the literature review, and they never produce a usable fit.
Either fix them, or drop them from the registry and say in §4 that a 22-model set was used.
Reporting two permanently non-converging models inflates the apparent breadth of the
comparison without adding information.

---

## Summary — materiality ranking

| # | Gap | Material? |
|---|---|---|
| 1 | 17 fitted models never introduced in §3.4 | **Critical** — results depend on unintroduced models |
| 2 | Ten missing primary sources | **Critical** — the clearest desk-reject signal |
| 3 | Chu (2020) uncited (as "Khim") — the anchor for §3.4.4 | **High** |
| 4 | Wolborska fitted, never discussed, contrary to your own key source | **High** |
| 5 | Shafeeyan (2014) uncited — the field's CO₂ fixed-bed review | **High** |
| 6 | Kimani cited four times, unlisted, conclusion reversed | **High** |
| 7 | Hu 2024 / Hu 2019 cited ten times, unlisted | **High** |
| 8 | Constant-pattern/LUB theory absent though L_MTZ is reported | **Moderate** |
| 9 | Six papers from one group; aqueous-phase dominance | **Moderate** — a reviewer will raise it |
| 10 | Non-scholarly and orphaned references | **Moderate** — cheap to fix, disproportionate cost if left |
| 11 | Wheeler–Jonas / gas-phase anchor absent | **Low** |

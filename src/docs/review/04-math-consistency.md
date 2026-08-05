# Mathematical Consistency Audit

> **Status 2026-08-04:** the k_T collision, δ-for-∂, and Danckwerts BC findings below were
> corrected in `T32_PI05_Final_Report.docx`; a nomenclature table (§3.3) resolves the
> x/z and C₀/c₀/ε/ϵ notation findings. See `11-process-record.md`. This file is retained
> unmodified as the original audit record.

**Scope** notation · variable definitions · units · dimensions · assumptions
**Basis** all 205 OMML equations extracted from the `.docx`, cross-read against
`src/docs/mechanistic-model.md` §0
**Anchors** `[pN]` = paragraph index

> **Framing.** Your supervisor's comment says §5 is supplementary reading, out of scope
> for the design project, and that *the model itself looks fine*. I agree — §5.1 is a
> clean, well-posed minimal model with its assumptions stated up front, which is more
> than most student reports manage. Nothing below asks you to change the physics. Every
> finding is about **notation, definitions and units**, which matter precisely *because*
> the section is destined for a reader who will meet the model cold.

---

## M1 — `k_T` means three different things (SEVERE)

| Anchor | Symbol | Meaning | Units |
|---|---|---|---|
| `[p848]` §3.3.1 | `kT` inside `K = (1/p₀)e^(−ϵ/kT)` | Boltzmann constant × temperature | J |
| `[p852-853]` §3.3.2 | `kT` | Toth isotherm constant (binding energy) | Pa⁻¹ |
| §3.4.2 `[p867-869]` | `k_T` | Thomas rate constant | mL min⁻¹ mg⁻¹ |

Three unrelated quantities, three unrelated dimensions, one glyph, inside eleven
paragraphs of each other. A reader who meets `k_T` in §3.4.2 having read §3.3.2 will
assume continuity and be wrong.

**Fix:** Boltzmann → `k_B T`. Toth → `b_T` or `b` (Stampi-Bombelli's own notation, which
you already follow in `CLAUDE.md`'s Toth table). Thomas → keep `k_Th` or `k_T` but
declare it in a nomenclature table.

## M2 — Five rate constants, no nomenclature table

`k` (LDF, `[p928]`, s⁻¹) · `k_s` (LDF again, `[p838]`) · `K` (Langmuir equilibrium,
`[p847-848]`) · `k_T`/`k_BA`/`k_YN` (breakthrough rate constants, §3.4) · `k` (Boltzmann,
`[p848]`).

`k` and `k_s` are **the same physical quantity written two ways** — the LDF uptake
coefficient — because §3.3 and §5 were drafted separately. `K` at `[p848]` is additionally
mislabelled: the text calls it *"the rate constant of equilibrium"*. It is an
**equilibrium constant**; it has no rate dimension.

**This is the single highest-value fix in the paper**, because it is also what your
supervisor's first comment asks for. You cannot write a section on "how does `k` vary with
flow and concentration" while `k` denotes four things. Add a nomenclature table — Hu et al.
(2020) opens with exactly one and it is the reason that paper is readable.

## M3 — Partial derivatives written with δ instead of ∂ (SEVERE)

`[p835]`, `[p838]`, `[p840]` — all of §3.3's governing equations:

```
δc/δt + u δc/δz + ((1−ε)/ε) δq_t/δt = D_L δ²c/δz²
δq_t/δt = k_s(q_e − q_t)
```

`δ` denotes a variation or a small increment; `∂` denotes a partial derivative. As printed
these are not the equations you mean. §5 `[p924]`, `[p927]` gets it right with `∂`. Same
physics, two notations, one of them wrong.

## M4 — Two different governing equations for the same column

|  | §3.3 `[p835]` | §5.1 `[p924]` |
|---|---|---|
| velocity | `u` "fluid velocity" | `u_s` superficial |
| axial dispersion | `D_L ∂²c/∂z²` **present** | **absent** (A1: "no axial dispersion") |
| solid coupling | `(1−ε)/ε · ∂q_t/∂t` | `ρ_b/ε · ∂q/∂t` |
| LDF constant | `k_s` | `k` |
| derivative | δ | ∂ |

Each equation is **individually dimensionally correct** — I checked both:

- §5: `ρ_b ∂q/∂t` → (kg m⁻³)(mol kg⁻¹ s⁻¹) = mol m⁻³ s⁻¹, ÷ε → mol m⁻³(gas) s⁻¹ ✓
- §3.3: `(1−ε) ∂q_t/∂t` → (—)(mol m⁻³(particle) s⁻¹) = mol m⁻³(bed) s⁻¹, ÷ε ✓

They are consistent **only because `q` and `q_t` are different quantities in different
units** — `q` is mol kg⁻¹ `[p928]`, `q_t` is a per-particle-volume concentration `[p836]`.
The paper never says this. A reader comparing the two equations will conclude one of them
is wrong.

**Fix:** pick one variable convention (mol kg⁻¹ is the natural one, since that is what
`q_dyn` reports) and state the dispersion assumption once — §3.3 presents the dispersive
model as the general case and §5 drops dispersion by assumption A1, which is a perfectly
good narrative if you *say* it.

## M5 — The Danckwerts boundary condition is malformed (SEVERE)

`[p840]`:

```
D_L δc/δt|_{z=0} = −u|_{z=0} c_i|_{z=0} − −c_i|_{z=0},   δc/δz|_{z=L} = 0
```

Two defects. First, the inlet condition carries a **time** derivative `δc/δt` where the
Danckwerts condition requires a **space** derivative. Second, the right-hand side is
degenerate: `−u(c_i − c_i)` evaluates to zero, so the equation as printed says
`D_L ∂c/∂t = 0`.

The standard form is

```
u c_in = u c|_{z=0⁺} − D_L ∂c/∂z|_{z=0⁺}     (inlet)
∂c/∂z|_{z=L} = 0                              (outlet)
```

The outlet condition is correct as written. Only the inlet needs rebuilding.

## M6 — Assumption A2 contradicts Eq. (5) and the temperature BCs

`[p917]` A2: *"Isotherm model i.e. heat transfer has an insignificant effect on the
breakthrough curve"*.

Two problems. The wording conflates **isothermal** (T constant — what you mean) with
**isotherm** (the equilibrium relation q_e(P) — a different thing entirely, used correctly
three lines later). And if the model is isothermal, then:

- Eq. (5) `[p934]`, `b(T) = b₀ exp(−ΔH/RT)`, is inert — b never changes.
- The temperature initial and boundary conditions `[p936]` (`T = T₀` at t=0 and z=0,
  `∂T/∂z = 0` at z=L) govern a field the model does not solve.

So §5.1 states three pieces of thermal machinery and then assumes them away. Either drop
them (cleanest, and consistent with A2), or keep them and say they are carried for the
FYP extension where the energy balance is added. `mechanistic-model.md` §A.4 already has
that energy balance — a one-line forward pointer would connect the two documents and cost
nothing.

> Note for the FYP: `CLAUDE.md` flags an unresolved reconciliation here — the solver
> scaffold carries two temperatures (`T_g`, `T_s`) while `mechanistic-model.md` §A.4 uses a
> pseudo-homogeneous single temperature. Not this report's problem, but it becomes one the
> moment §5 is extended.

## M7 — Volumetric flow rate is stated twice, with two different wrong values

| Anchor | Table | Printed | Correct? |
|---|---|---|---|
| `[p963-965]` | §5.2 "Table 2" | **0.3 – 0.9 m³·h⁻¹** | ✗ 100× too high |
| `[p1120-1122]` | §7 "Table 2" | **3.0 – 9.0 cm³·h⁻¹** | ✗ 1000× too low |

The swept range is 0.05–0.15 lpm. That is 3.0–9.0 **L h⁻¹** = 0.003–0.009 m³ h⁻¹ =
3000–9000 cm³ h⁻¹. The **numerals 3.0–9.0 are right**; both tables attach the wrong unit,
in opposite directions. Two tables, both numbered "Table 2", disagreeing about a primary
experimental parameter.

Everything else in both tables checks out: inlet diameter 0.85 cm ✓, packing volume
11.92 cm³ ✓ (recomputed π(0.425 cm)²·21 cm), inlet velocity 1.47–4.41 cm s⁻¹ ✓
(recomputed as superficial).

## M8 — ε is "??" in §5 but silently assumed in §7

`[p969-971]` marks bed void fraction ε as `??` — correct and honest, matching `CLAUDE.md`'s
open-inputs list. But §7's Table 3 `[p1129]` publishes an **interstitial velocity** column,
which can only be computed by dividing by ε. It uses the code's floored ε = 0.30.

A quantity declared unknown in §5 is used as if known in §7. See `00-integrity-report.md`
IL-SERIOUS-5 — this is the same defect seen from the mathematics side.

## M9 — Axial coordinate is both `x` and `z`

`[p821]` Fig. 3 caption: *"flows axially towards the outlet along the **x**-axis"*.
`[p835]` and `[p924]`: the PDEs use **z**. §3.4.1 Bohart–Adams uses **x** for bed height
(following Hu 2020's nomenclature). Pick one for the report's own equations; keep `x` only
when quoting a source's form, and say so.

## M10 — `C₀` (mole fraction) and `c₀` (mol m⁻³) differ only by case

`[p831]` defines *"the inlet CO₂ concentration (mole fraction `C₀`)"*. `[p834]` uses `c₀`
as an influent concentration; `[p932]` fixes `c` in mol m⁻³. Case is doing dimensional work
here, which no reader will survive. Compounding it, `ϵ` (Boltzmann factor exponent,
`[p848]`) and `ε` (void fraction) are near-identical glyphs used in adjacent subsections.

## M11 — Figure cross-references are off by one

`[p831]`: *"In **Fig. 4)** the inlet CO₂ concentration … flows through the packed bed at a
volumetric flow rate of v₀"* — Fig. 4 `[p827]` is the single-granule diagram. The
configuration figure is Fig. 3 `[p821]`. Also `v₀` appears here for volumetric flow and is
used nowhere else; Table 2 and §5 use different symbols again.

`[p889]`: *"this reduces to the logistic **Eq. (??)**"* — a literal unresolved
cross-reference, alongside empty `Eq. ()` at `[p869]` and `[p871]`.

## M12 — Region bound changes between consecutive sentences

`[p884]`: kernels *"are visually indistinguishable in the central transient region
`|X| ≤ 2`"*. `[p885]`, the very next clause: the sup-norm bound holds *"on the central
region `|X| ≤ 0.5`"*. Which region the ≤ 0.04 claim covers determines whether the argument
works. (This is the claim resting on `(ChatGPT, n.d.)` — see IL-SERIOUS-1.)

---

## What is correct

Worth recording, because a list of defects reads worse than the section deserves:

- **§5.1 assumptions A1–A7 `[p916-922]`** are explicitly enumerated before the model is
  written. This is good practice and most student reports skip it.
- **Toth isotherm `[p852]`**, `q = q_s k_T p / (1 + (k_T p)^t)^(1/t)` — standard form,
  correct.
- **Langmuir `[p847]`**, `θ = KP/(1+KP)`, with the `KP ≪ 1` linear limit and the saturation
  limit both discussed `[p848]` — correct and well explained.
- **Ideal-gas closure `[p932]`** and **van 't Hoff `[p934]`** — both standard and correctly
  stated (subject to M6's assumption clash).
- **The BA–Thomas–YN equivalence proof `[p876-881]`** is mathematically sound. The
  factoring argument is right and matches Hu et al. (2020) §2 and Chu (2020).
- **Dimensional consistency of both governing equations** — verified independently above.
- **Geometry** — packing volume and superficial velocity both recomputed and correct.

---

## Priority

| # | Finding | Severity | Effort |
|---|---|---|---|
| M1 | `k_T` triple collision | SEVERE | low |
| M2 | Five rate constants, no nomenclature table | SEVERE | low — **do this first** |
| M3 | δ for ∂ | SEVERE | low |
| M5 | Malformed Danckwerts BC | SEVERE | low |
| M7 | Flow rate wrong in two tables | SEVERE | trivial |
| M4 | Two governing equations, undeclared variable change | MAJOR | medium |
| M6 | A2 vs van 't Hoff and T-BCs | MAJOR | low |
| M8 | ε unknown in §5, assumed in §7 | MAJOR | low |
| M10 | `C₀` vs `c₀`; `ϵ` vs `ε` | MAJOR | low |
| M9 | `x` vs `z` | MINOR | low |
| M11 | Figure/equation cross-refs | MINOR | low |
| M12 | Region bound inconsistency | MINOR | low |

A single nomenclature table placed before §3.3 closes M1, M2, M9 and M10 at once, and is
the highest return-per-hour edit available anywhere in this report.

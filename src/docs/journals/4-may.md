# Journal #1 — Weeks 1–2 (20 Apr – 1 May 2026)

**Project:** Parametric Study of CO₂ Adsorption Breakthrough in Packed-Bed Columns
**Student:** Year 3, ES Design Project (April 2026 semester), Ngee Ann Polytechnic
**Institution supervisors:** Prof. Erik Birgersson, Prof. Parapsorb Borisut (SUTD/NUS)
**Date drafted:** Sat 2 May 2026 · **Submission:** Mon 4 May 2026 · **Word count:** ~2,300

---

## 0. Framing — what this fortnight was actually for

Weeks 1–2 were a *triage* period. The original project scope (TSA regeneration on a Langmuir sorbent) was pivoted on 30 April to **adsorption breakthrough on a Toth sorbent**, anchored to Stampi-Bombelli et al. (2024) as the primary experimental benchmark. So the deliverable for this fortnight was *not* code — it was to (a) read the seven papers seeded in `papers/md/`, (b) verify that the chosen anchor paper actually contains every closure parameter the new scope needs, and (c) commit to a math+experiment plan that the Interim Report (1 Jun) can be built on without re-baselining.

The honest assessment: the literature reading is solid, the Toth closure is in hand, and three live discrepancies between the planning documents and the source papers need supervisor confirmation before Week 4 (detailed in §3).

---

## 1. What I did this period

- Read all seven papers in `papers/md/` end-to-end. Built a one-line role for each (table in §2.1) so the literature spine is no longer a pile but a working scaffold.
- Extracted the Toth isotherm parameter set from Stampi-Bombelli 2024, Table 1 (`n_s0`, `b_0`, `t_0`, ΔH₀, χ, α, T₀) and the packed-bed column geometry from Table 2 (`d_c = 3.37 cm`, `L = 32.5 cm`, sorbent mass 187 g, 3 mm rings). Cross-checked these against the values copied into `CLAUDE.md` — found one missing parameter (α = 0.11, the Toth temperature exponent — see §3).
- Completed Evans Ch 3.1–3.2 (linear first-order PDEs, method of characteristics) by hand. Worked the three textbook problems on `u_t + c(x) u_x = 0` for `c = 1`, `c = x`, `c = sin(x)`. The `c = sin(x)` case gives caustics inside the column — a useful warning that with non-constant carrier velocity, characteristics can cross even before any nonlinear adsorption term enters the picture.
- Started Myers & Font 2020 (the analytical traveling-wave paper). Worked through §4.1 (the substitution η = x̂ − ŝ(t̂)). Re-derived their Eq. (53) on paper. The result that the front velocity normalises to v̂ = 1 in their scaling is the Rankine–Hugoniot chord velocity in disguise — that is the bridge between the analytical paper and Gate B.
- Set up the Python environment (`numpy`, `scipy`, `matplotlib`), forked a minimal 1-D heat-equation solver as the MOL template, and confirmed `scipy.integrate.solve_ivp` with `LSODA` runs cleanly. The 4-PDE coupled scaffold in `src/solver/pde_mol.py` is *not* yet runnable — that is Week 4–5 work, as planned.
- Set up the LaTeX skeleton for the Interim Report (chapters: Introduction · Literature · Derivation · Numerics · Validation · Baseline Results · Conclusions). All §3 math goes here when written.

---

## 2. What I learned

### 2.1 The seven papers, organised as a scale ladder

The seven papers in `papers/md/` cover a rough five-decade range of length scales. Reading them in this order — molecular → process — turned out to be the way the project naturally hangs together:

| Scale | Paper | What it locks down for this project |
|---|---|---|
| **Molecule** (amine–CO₂ chemistry) | Jin et al. 2025 (RSER) — review of amine sorbents at −20 to 40 °C, 0–100 % RH | Gives the *direction* of H4 (capacity ↓ as T_ads ↑) and the Class 1/2/3 sorbent taxonomy. Frames the dry-bed assumption as a deliberate simplification, not an oversight |
| **Particle** (kinetics on a single pellet) | Stampi-Bombelli et al. 2024 (I&EC Res) — packed-bed *and* monolith experiments on triamine-grafted γ-alumina at 25 / 50 / 90 °C, 400 ppm and 5.6 % CO₂ | **Primary benchmark.** Toth isotherm parameters (`n_s0=1.23`, `b_0=4839 kPa⁻¹`, `t_0=0.25`, ΔH₀=70 kJ mol⁻¹), PFO-vs-dual-kinetic comparison, full breakthrough curves. Gate C is built on this paper |
| **Sorbent (alt.)** (polymer-based commercial sorbent) | de Joannis et al. 2025 (CCST 17, "paul2025") — Aspen TEA on Lewatit VP OC 1065, polystyrene-DVB beads with primary benzyl amines | The natural *polymer-based* analogue to Stampi-Bombelli's γ-alumina. CO₂ uptake ≈ 1 mol/kg dry, ≈ 1.5 mol/kg at RH = 0.5 → an enhancement factor of 1.5 worth flagging because dry-bed is a baseline-only assumption |
| **Continuum (analytical)** (1-D PDE for the bed) | Myers & Font 2020 (IJHMT 163, paper number 120374) | Closed-form traveling-wave solution after non-dim. Provides Gate-B chord-velocity benchmark and the *only* analytical sanity check the solver will ever get |
| **Continuum (numerical)** (1-D / 2-D reactive transport) | Pedrozo et al. 2026 (Comput Chem Eng 204) — COMSOL TVSA cycle optimization on Lewatit-like sorbent, then 2-D axisymmetric extension | Method template for cycle simulation (out of scope here, kept for FYP). Their headline number — *2-D model costs ~40× the 1-D model for limited new physics* — is exactly the justification for staying 1-D in this project |
| **Reactor / contactor** (geometry of the bed itself) | Chen et al. 2023 (Energy 282) — CFD comparison of W-shaped vs conventional packed bed for indoor DAC at 500 / 1000 / 1500 / 2000 ppm | Cross-validation for H2 (concentration sweep) at indoor-DAC ppm levels, plus an example of how velocity (0.5–2.5 m s⁻¹) and concentration interact on capture rate at the higher end of the sweep matrix |
| **Process / system** (full DAC application context) | Xu et al. 2024 (Energy Convers Manage 322) — comprehensive DAC review | Provides the conservation-law computational framework and the six-category sorbent classification (silica gel, metal oxides, MOFs, carbon, zeolites, **polymers**). Useful for Introduction and Literature chapters |

The project's *math* lives in the Myers & Font + Stampi-Bombelli rows; everything else is contextual or comparative. That is not a slight on the others — it is a triage that protects the timeline.

### 2.2 Two physical insights worth a paragraph each

**Self-sharpening fronts.** The Toth isotherm `q*(p)` is *concave* in `p` over the DAC concentration range. With LDF kinetics, this concavity is not an aesthetic detail — it forces the breakthrough wave into a *constant-pattern* (self-sharpening) regime at large NTU, where the MTZ width stops growing and the front propagates as a translating shock. The Rankine–Hugoniot chord velocity `v_RH = u·ΔC / (ε·ΔC + (1−ε)·ρ_p·Δq)` is then not just an approximation — it is the *asymptotic* front speed the solver must reproduce at high NTU. This is the conceptual link between Myers & Font (analytical) and Stampi-Bombelli (experimental constant-pattern observed in their Fig. 4 at 5.6 % CO₂). It also tells me that any solver that smears this shock — i.e., uses central differencing on the advection term — will silently fail Gate B no matter how fine the grid. First-order upwind it is.

**Why temperature matters more than the H4 hypothesis statement suggests.** Stampi-Bombelli measured isotherms at 25 / 50 / 90 °C (their Fig. S1). At 90 °C, the equilibrium loading at 400 ppm collapses by roughly an order of magnitude relative to 25 °C — the bed effectively stops adsorbing. This means the *non-isothermal* simulation matters even though the bed is adiabatic: the heat of adsorption (ΔH₀ = 70 kJ/mol) raises the local solid temperature inside the MTZ, which depresses the local equilibrium loading, which broadens the MTZ further. The four state variables (`C`, `q`, `T_g`, `T_s`) are coupled at exactly this point. Decoupling temperature for "Gate A simplicity" is fine for validation, but the production sweeps cannot be run isothermally without misrepresenting H4 entirely.

### 2.3 One numerical insight

A back-of-envelope NTU estimate at the Stampi-Bombelli baseline (u ≈ 0.14 m/s, L = 0.325 m, k_LDF·a_p of order 0.1 s⁻¹ from comparable γ-alumina literature) gives `NTU = k·L/u ≈ 0.23`. That is *low* NTU — the experiment is firmly in the dispersive (broad-MTZ) regime, not the constant-pattern regime. The front is not yet a shock at the Stampi-Bombelli outlet. This is consistent with the long Δt they observe in Fig. 4. Worth keeping in mind: when the project sweep pushes u up to 1.5 or 2.5 m/s (ten-fold higher than the experiment), NTU drops further — and the dispersion term will dominate. This supports my decision to keep both the LDF sink *and* the axial-dispersion term in the solver, rather than hyperbolic-only.

---

## 3. Blockers and questions

I want to land these three before Week 4. Each names the supervisor whose answer would unblock it.

### B1. The velocity sweep extrapolates ~10× beyond the benchmark — is that intended?

Stampi-Bombelli 2024 deliberately kept interstitial velocities **below 0.15 m/s** (their Table 5: 400 ppm runs at u = 0.14 m/s on the packed bed) to keep the experiment in a regime where mass-transfer resistances were resolvable against axial dispersion. They state explicitly that these velocities are "low compared to industrial DAC applications". The project's pre-committed sweep matrix (`study_plan.md` §2.4) is **u = 0.5 / 1.5 / 2.5 m/s** — between roughly 4× and 18× higher than the highest experimental point. Two reasonable readings: either the sweep is meant as a deliberate extrapolation toward industrial scale (in which case Gate C still validates at u = 0.14 m/s but H1 results will be reported outside the validated regime), or this is a unit confusion between superficial and interstitial velocity that should be caught now.
*Owner: Prof. Birgersson.* If extrapolation is intended, I want to add a clear validity caveat to H1 in the Interim Report and report all H1 results in dimensionless `Pe` so the extrapolation is visible.

### B2. The Toth `t(T)` temperature dependence (α = 0.11) is missing from the parameter table

`CLAUDE.md` records the Toth parameters as `n_s0 = 1.23`, `b_0 = 4839`, `t_0 = 0.25`, ΔH₀ = 70, χ = 0 — but the Stampi-Bombelli Table 1 *also* lists **α = 0.11**, which sets the temperature dependence of the heterogeneity exponent through `t(T) = t_0 + α(1 − T_0/T)`. For an isothermal Gate-A check this does not matter. For Gate C and especially H4 (capacity vs T_ads at 50 and 90 °C), it does — at 90 °C the deviation in `t(T)` shifts the predicted equilibrium loading by an amount comparable to the ±20 % Gate C tolerance. Suggest adding `alpha = 0.11` to the Toth closure in `derivation.md` §1.5 (currently still written as Langmuir from the old scope) and `pde_mol.py`.
*Owner: technical decision; will flag to Prof. Borisut for confirmation that I have read Table 1 correctly.*

### B3. Citation hygiene — Myers & Font volume/page

`study_plan.md` Part V cites Myers & Font 2020 as *Int J Heat Mass Transf* **163, 120434**. The PDF in `papers/md/` shows volume **163, paper number 120374** on every page. Likely a transcription typo. Worth fixing in `study_plan.md` and `research.md` before the Interim citation list is generated.
*Owner: me — housekeeping, no supervisor needed.*

### Two open data items that are *not* blocking (per `CLAUDE.md`):

- `c_ps`, `D_ax`, `h_f` placeholders. Pedrozo et al. 2026 §2 give numeric values for the first two on a similar Lewatit-like sorbent; will use those as initial estimates and fit `k_LDF` at Gate B. **Not blocking Gates A–C.**
- SUTD rig geometry. If supplied by Prof. Birgersson, I will add a model-vs-experiment stretch check in the Discussion. Not committed.

---

## 4. The 18-week road map (compressed)

The structured spine is in `study_plan.md` Part III. The compressed view, organised by *what would have to slip* for the deadline to slip:

```
Wk 1–2  ✅ Literature triage, Toth closure verified, PDE scaffold drafted
Wk 3       Buckingham Π → identify Pe, NTU, α; write dimensionless-analysis subsection
Wk 4    🚧 GATE A — linear MOL solver, L² < 1 % vs analytical Gaussian-broadening step
Wk 5    🚧 GATE B — full coupled solver, |v_sim − v_RH|/v_RH < 10 % (isothermal Toth + LDF)
Wk 6    🚧 GATE C — non-isothermal baseline reproduces Stampi-Bombelli τ_BT within ±20 %
Wk 6       Interim Report draft (target 2,500–3,500 words) — written in parallel with Gate C
Wk 7    🟦 DELIVERABLE — Interim Report submitted Mon 1 Jun
Wk 8       OAT sensitivity sweep on u and C_in (6 runs)
Wk 9–10    Term break — read for pleasure, do not buy back slipped Gates here
Wk 11      OAT sensitivity sweep on L and T_ads (6 runs)
Wk 12      Post-process all OAT runs for η, q_dyn; column-efficiency subsection
Wk 13      u × C_in 3×3 interaction grid (9 runs); response-surface fit
Wk 14      Recast everything into (Pe, NTU, α) coordinates; sensitivity ranking
Wk 15      Final Report draft v0.5 → both supervisors for feedback
Wk 16      Final Report v1.0 — supervisor feedback incorporated
Wk 17   🟦 DELIVERABLE — Final Report submitted Mon 10 Aug
Wk 18   🟦 DELIVERABLE — Final Presentation, panel Q&A
```

**Critical-path watch**: any slip on Gates A → B → C cascades directly into the Interim deadline, and the term break (Wk 9–10) contains *zero* schedule slack. The pre-committed mitigation (per `study_plan.md` Part VI risk R3) is to descope sweep levels — drop L and T_ads from 3 to 2 levels each, or shrink the u × C_in grid from 3×3 to 2×3 — *not* to work through the term break. Empirically the latter backfires.

**Top three risks** I will keep in front of myself, all from the project register:

1. **R5 — scope creep into humidity / 2-D / cyclic.** The de Joannis humidity isotherms are *fascinating*. They are also FYP material. If I find myself reading them on a Wednesday morning instead of debugging a Gate-A residual, the answer is to bookmark and close.
2. **R3 — Interim slip.** Mitigated by writing the derivation chapter *now* (Wk 3), in parallel with the Gate work, not after. Section §3 of the Interim is not blocked on the solver.
3. **R7 — laptop / code-loss.** Push every commit to GitHub nightly; weekly `.npz` results to Drive.

---

## 5. What I will do next fortnight (Wks 3–4, 4–15 May)

Ordered by what most needs to happen first.

1. Finish Buckingham Π non-dimensionalisation by hand and write the dimensionless-analysis subsection (target 600 words, goes verbatim into Interim §3.4). Compute order-of-magnitude estimates for Pe, NTU, α at the Stampi-Bombelli baseline and at each of the four sweep extremes — this is what will tell me *before* running any code which sweep cells will be in the constant-pattern regime and which in the dispersive regime.
2. Update `derivation.md` from the old Langmuir-regeneration scope to Toth-adsorption with the corrected `t(T)` form (pending B2). Currently still reflects the pre-30-April scope.
3. Build the linear MOL solver (advection + dispersion only, no adsorption) and pass Gate A by Friday Wk 4. The analytical reference is the standard error-function solution to the step-input advection-dispersion problem; benchmark on a 200-node grid at three CFL numbers (0.5, 0.9, 1.1) to confirm CFL > 1 actually breaks the upwind discretisation as theory predicts.
4. Send a short email to both supervisors with the three blockers in §3 above. Single-page, one ask per blocker, with the source-paper line/figure cited.

Predicted Wk-3 risks: (a) Buckingham Π sometimes produces a *non-unique* set of dimensionless groups, and the choice between equivalent sets matters for which group ends up on the x-axis of the final response-surface plots — I will document the choice rather than absorb it silently. (b) `solve_ivp` with `LSODA` can hide CFL instability inside its adaptive timestep; the way to surface it is to log the timestep history and check it does not collapse — that takes 10 lines of post-processing, easy to forget, hard to debug later.

---

*End of Journal #1. Estimated reading time: 8 minutes. Next journal due Mon 18 May 2026 (Wk 5), expected to lead with Gate A pass/fail.*


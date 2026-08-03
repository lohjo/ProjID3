# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## How to work here — read first

Hard rules, ordered by how often they get broken. Violating the first two wastes the most time.

### 1. Data basis — the #1 mistake
- **Measured basis = exactly five bench runs: `run 3/4/5/6/8`** in `src/solver/data/new runs/`, processed by `new_runs_pipeline.py` + the `breakthrough_fit/` package. These are the **only** real data.
- The `*ml_*g.csv` and `May-*.csv` files are **synthetic/placeholder** — never present them as measured results. They fed only a synthetic-validation appendix (now archived).
- **Never invent sweep points.** The "39-run / 11 OAT + 9 u×C_in" matrix is *planned, not executed*; H1–H5 have not been tested against measured data. Flag any request that assumes otherwise.

### 2. Never fabricate; never silently substitute
- No invented parameter values, results, or citations. Every number traces to a run output, a cited paper in `src/docs/papers/`, or the measurements block — otherwise mark it placeholder/unknown. The `??` in the Toth table below are **deliberate unknowns**; leave them until a real value arrives.
- Do **not** swap Toth / geometry / physical parameters for guesses. Flag any deviation and name the owner (lab / Stampi-Bombelli / Prof. Birgersson).
- Blocked on a missing input? **Name the parameter and its owner** — don't guess through it.
- Cite explicitly: report-prose claims tie to a specific paper in `src/docs/papers/`. No uncited assertions.
- **Preserve my numbers, wording, and claims.** Edit only what's asked; surface disagreements instead of overwriting fitted values or voice.

### 3. Run before you claim done
- Actually execute the pipeline and show real stdout / figures. Never assert code works untested. "It should work" is not done.

### 4. Communication
- **Terse, answer-first.** Lead with the conclusion; cut preamble and hedging. Brief is fine — I'll ask for more.
- **Challenge weak reasoning** — flawed assumptions, dubious fits, gate risk — even unprompted. Don't just agree.
- **Show working for math.** For derivations / PDE / numerics, show the steps and assumptions, not just the final expression.
- If a change risks a validation gate (A/B/C) or a report deadline, **say so up front.**

### 5. Do not touch
- `src/docs/archive (DO NOT OPEN)/` — superseded old-scope. Do **not** read or edit anything in it.
- Stale docs — don't trust as current: `README.md` (still says "Regeneration"), old `study_plan.md`, `research.md`, `derivation.md` (all archived).

### 6. Twin file
- `AGENTS.md` (the Codex twin) mirrors this file. When you change a fact here, **mirror the change into `AGENTS.md`** so they don't drift.

---

## Repository purpose

Single-author NP Year-3 Design Project: **Parametric Study of CO₂ Adsorption Breakthrough in Packed-Bed Columns** (April 2026 semester, supervisors Prof. Erik Birgersson (NUS) and Dr. Prapatsorn Borisut (SUTD)). The repo is a research workspace, not a product — it holds the math derivation, solver + fitter code, literature notes, generated figures, and the project-management tracker that drives weekly work.

Scope revised 30 Apr 2026: from TSA regeneration to adsorption breakthrough. `src/docs/` holds the live scientific content (see Document layout — most of the old key files are now archived).

## Hard deliverable dates (drives every priority call)

- **Interim Report**: Mon 1 Jun 2026 (Wk 7) — must include full PDE derivation, validated solver, and baseline run vs Stampi-Bombelli 2024 breakthrough benchmark.
- **Final Report**: Mon 10 Aug 2026 (Wk 17).
- **Final Presentation**: 17–19 Aug 2026 (Wk 18).
- **Three validation gates** (must all pass by end of Wk 6 for Interim to land):
  - **Gate A** — linear advection-diffusion solver, L² error < 1%
  - **Gate B** — R-H adsorption shock chord velocity ±10%
  - **Gate C** — Stampi-Bombelli 2024 breakthrough curve τ_BT ±20% at 400 ppm

## Deliverable formats (what to produce, and where)

- **Markdown prose** under `src/docs/` — the live scientific writing.
- **Python + figures** — solver/fitter code that runs headless (Agg backend) and writes PNGs/CSVs to `src/img/generated/`. Every fitted parameter printed to stdout — **no hand-tuning.**
- **Journals / sprints / tracker** — bi-weekly journals (`src/docs/journals/`), dated sprint plans (`src/docs/sprints/`), and `CO2_Regen_Project_Tracker.xlsx`.
- **LaTeX** (`src/docs/latex/`) — secondary; report PDF builds only.

## Run the solver

No build system, no test suite, no linter configured. Plain Python scripts.

```bash
# Activate venv (already committed at repo root)
source venv/Scripts/activate    # Git Bash on Windows
pip install -r requirements.txt # numpy, scipy, matplotlib

# Run scripts directly from repo root
python src/solver/heat_eq_mol.py     # working 1-D advection-diffusion MOL demo
python src/solver/pde_mol.py         # 4-PDE coupled scaffold — NOT yet runnable
python src/solver/illustration.py    # end-to-end numerical illustration for §5
```

`pde_mol.py` is a scaffold. Expect to spend Weeks 4–5 turning it into a Gate-A-passing implementation.

`illustration.py` ingests the **synthetic** CSVs in `src/solver/data/*ml_*g.csv` and walks the reader from the linear transport equation through retarded advection–diffusion to fitted Chern–Chien Langmuir/Freundlich and Clark sigmoids, writing eight figures to `src/img/generated/`. Every fitted parameter (k_YN, K, tau_BT, C_inf, n, t_50, t_i, mu_max, lambda) is printed to stdout.

### The real experiment (the measured basis)

The five bench runs in `src/solver/data/new runs/` (run 3/4/5/6/8) are the only measured data. Refresh the real results with:

```bash
python new_runs_pipeline.py                       # 5 real runs -> breakthrough_out/run N/
python -m breakthrough_fit.assemble_may_prompt    # engineered-prompt tables/figures -> src/img/generated/may_prompt/
```

`breakthrough_fit/` package layout: `parse.py` (auto-detect Format A/B, despike, metadata) · `models.py` (M01–M24 registry + bounds) · `stats.py` (R², AdjR², RMSE, AICc, F-test) · `fit.py` (curve_fit + L-BFGS-B fallback, 10 starts, seed=42) · `isotherm.py` (q₀ back-calc) · `performance.py` (t_b, t_E, t₅₀, q_dyn, L_MTZ, ψ) · `plots.py` (P1–P7, 300 dpi headless) · `mtz_fem.py` (1-D FEM + travelling-wave) · `main.py` (CLI).

## Architecture of the solver work

Goal: solve a coupled 4-PDE system on a 1-D packed-bed column for adsorption breakthrough. Solver state vector at each axial node `z`:

| Field | Equation | Live derivation |
|---|---|---|
| `C(z,t)` — gas-phase CO₂ concentration | gas mass balance + axial dispersion + LDF sink | `mechanistic-model.md` §A.1 |
| `q(z,t)` — solid loading | LDF kinetics, Toth closure for `C*` | `mechanistic-model.md` §A.2–A.3 |
| `T_g(z,t)` — gas temperature | gas energy balance + interphase heat transfer | `mechanistic-model.md` §A.4 |
| `T_s(z,t)` — solid temperature | solid energy balance + heat of adsorption | `mechanistic-model.md` §A.4 |

> **Flag — open reconciliation:** the solver scaffold carries **two temperatures** (`T_g`, `T_s`). The live analytical derivation (`mechanistic-model.md` §A.4) uses a **pseudo-homogeneous single-temperature** energy balance. These are not yet reconciled — do not silently assume one matches the other; raise it before coupling the energy equation.

Key differences from the old regeneration scope:
- **Q_wall = 0** (adiabatic adsorption; no external heater)
- **IC: clean bed** — C = 0, q = 0, T_g = T_s = T_ads
- **Inlet BC: step C_in** — CO₂ concentration step at z = 0
- **Isotherm: Toth** (not Langmuir) — parameters from Stampi-Bombelli 2024

Numerical method:
- **Method of Lines** — discretize `z`, integrate in `t` with `scipy.integrate.solve_ivp` (`LSODA` or `BDF`).
- **First-order upwind** for advection (`-u·∂/∂z`).
- **Central differences** for diffusion (`∂²/∂z²`).
- **Dirichlet inlet BC** enforced by zeroing `dY/dt[0]`.
- State packing: flat vector `[C, q, Tg, Ts]` of length `4N`, split with `np.split(y, 4)` inside `rhs`.

When extending the solver, keep this layout.

## Toth isotherm parameters (Stampi-Bombelli 2024, Table 2)

Sorbent: amine-functionalised γ-alumina, 3 mm ring pellets. `??` = deliberate unknown — do not fabricate; flag when needed.

| Parameter | Value | Units |
|---|---|---|
| ns0 | ?? | mol/kg |
| b0 | ?? | kPa⁻¹ |
| t0 | ?? | — |
| ΔH0 | ?? | kJ/mol |
| T0 | ?? | K |
| χ | ? | — |
| ρ_p | ?? | kg/m³ |
| εp | ?? | — |
| d_p | ?? mm granules | — |
| Column d_c | 8.5 | mm |
| Column L | 38.6 ± 0.1 | cm |

These are the baseline parameters. Do not silently substitute alternatives — flag any deviation.

## Document layout (which file is the source of truth)

**Live scientific content — read/edit these:**
- `src/docs/mechanistic-model.md` — **current full derivation**: conservation-law derivation (Part A), conservation & well-posedness (B), nondimensionalisation (C), analytically tractable limits (D). This is the live source-of-truth for the model math. **Consult before changing solver math.**
- `src/docs/psi-quadrature-consistency-proof.md` — Ψ-quadrature consistency + error bounds (travelling-wave Route A/B analysis).
- `src/docs/experimental-results.md` — **mirrors Hu et al. 2024**: measured breakthrough curves, fitted models, and derived metrics (t_b, t_E, t₅₀, q_dyn, L_MTZ, ψ). This is the live source-of-truth for the measured basis.
- `src/docs/updates.md` — running change log.
- `src/docs/prompts/` — engineered prompts that drive figure/table generation.
- `src/docs/literature/` — source papers; cite report-prose claims from here.
- `src/docs/biweekly-journals/sprint/<DD-MM>.md` — dated weekly sprint plans; newest supersedes older.
- `src/docs/biweekly-journals/` — bi-weekly journals for supervisor submission.
- `src/docs/biweekly-journals/latex/` — LaTeX report builds (secondary output).

**Archived / not current — do not treat as source of truth:**
- `src/docs/archive (DO NOT OPEN)/` — superseded old-scope. Do **not** read or edit. This now contains the old `derivation.md`, `CO2-adsorption-model.md`, `equation_compendium.md`, `literature-survey-summary.md`, `my-research-paper.md`, `study_plan.md`, `research.md` (in `maybe_archive/`). Earlier CLAUDE.md versions wrongly listed these six as live under `src/docs/` — they are **not**.
- `README.md` — **stale** (still "Regeneration"; cites a nonexistent `Foolproof_Study_Plan.md`).
- `CO2_Regen_Project_Tracker.xlsx` — eight-tab tracker (Experiment Log, gate verdicts). Sweep matrix still old-scope; needs updating to `u / C_in / L / T_ads`.

## Experimental design — as executed (the real basis)

The **only correct measured basis** is the five bench runs in `src/solver/data/new runs/` (run 3/4/5/6/8). Their authoritative metadata is the measurements block (per-run mass/bed length + the adsorption pressure-drop table); inlet C₀ is read per run from the data.

Fixed: column **38.6 cm × 8.5 mm i.d.**; sorbent **~8.00 g** PEI@SiO₂ in a **~21 cm** bed; **ambient** (uncontrolled) T; P ≈ 101.325 kPa. Swept: inlet flow and inlet CO₂.

| Run | Inlet flow Q | C₀ (measured) | bed L | best model (overall) | q_dyn |
|---|---|---|---|---|---|
| run 3 | 0.15 lpm (150 mL/min) | 47,400 ppm (~4.7 %) | 21.0 cm | M11 Fractal-Erf | 0.555 mol/kg |
| run 4 | 0.05 lpm (50 mL/min)  | 97,800 ppm (~9.8 %) | 21.3 cm | M14 Weibull (M11 4th) | 0.810 mol/kg |
| run 5 | 0.10 lpm (100 mL/min) | 95,420 ppm (~9.5 %) | 21.2 cm | M11 Fractal-Erf | 0.552 mol/kg |
| run 6 | 0.15 lpm (150 mL/min) | 102,140 ppm (~10.2 %) | 21.5 cm | M10 Fractal-Gudermann (M11 5th) | 0.885 mol/kg |
| run 8 | 0.10 lpm (100 mL/min) | 150,630 ppm (~15.1 %) | 21.5 cm | M10 Fractal-Gudermann (M11 2nd) | 0.787 mol/kg |

Cleanest sub-sweep: the ~10 % CO₂ flow sweep = runs 4 (50) / 5 (100) / 6 (150) mL/min. Outputs per run: 24-model fits + `t_BT` (C/C₀=0.05), `t_E` (0.95), `t50`, `q_dyn`, `L_MTZ`, ψ.

The earlier "39-run / 11 OAT + 9 u×C_in" matrix is **planned, not executed**; the H1–H5 thresholds have not been tested against measured data. Do not invent sweep points; flag any.

### Recent audit corrections (2026-05-31)
- `new_runs_pipeline.py`: run6 flow 0.05→**0.15** lpm, run8 0.125→**0.10** lpm (per the pressure-drop table — measurements are authoritative).
- `breakthrough_fit/performance.py`: removed an unjustified `×1000` in `q_dyn_trapz`; q_dyn was ~1000× too low. Now 0.55–0.89 mol/kg, cross-checked vs YN back-calc q₀.
- `breakthrough_fit/assemble_may_prompt.py`: column i.d. was `0.085 m` (85 mm) — corrected to **8.5 mm**; RUNS list remapped to runs 3/4/5/6/8; per-run geometry now used in Table 1; the old "geometrically inconsistent" FLAG was an artefact of the 10× diameter error.
- Best model per run (corrected): M11 best in runs 3 and 5; M14 (Weibull) in run 4; M10 (Fractal Gudermannian) in runs 6 and 8. The earlier "M11 every run" claim was stale — M11 remains consistently top-3 but does not win all runs. Among prompt-specified models (M01/M02/M04/M05/M06/M07/M14/M16/M23), M23 ranks highest by mean Adj. R².

## Critical open data dependencies

**Low-risk** — Toth isotherm and column geometry are available from Stampi-Bombelli 2024 (Table 2 above). Gate C is not blocked on supervisor data.

Remaining open items (non-blocking) — if solver work blocks on one, name the parameter and its owner rather than guessing:
- `c_ps` (solid specific heat), `D_ax` (axial dispersion), `h_f` (gas-solid heat transfer) — use literature estimates as placeholders; fit k_LDF at Gate B.
- **`ρ_p` (sorbent/pellet density)** — needed to turn measured ρ_b (~660–672 kg/m³) into void fraction ε via EC-2. The pipeline currently assumes ρ_p = 800 kg/m³, giving an unrealistically low ε≈0.16 (floored to 0.30 in code). Real ρ_p is an open input; do not treat ε or ε-based interstitial velocity as physical until supplied. Owner: lab / Stampi-Bombelli.
- SUTD rig geometry — if provided by Prof. Birgersson, add as a stretch model-vs-experiment check in Discussion. Not required for Gate C.

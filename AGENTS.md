# AGENTS.md

This file provides guidance to Codex (Codex.ai/code) when working with code in this repository.

## Repository purpose

Single-author NP Year-3 Design Project: **Parametric Study of CO₂ Adsorption Breakthrough in Packed-Bed Columns** (April 2026 semester, supervisors Prof. Erik Birgersson and Prof. Parapsorb Borisut at SUTD/NUS). The repo is a research workspace, not a product — it holds the math derivation, solver code, literature notes, and the project-management tracker that drives weekly work.

Scope revised 30 Apr 2026: from TSA regeneration to adsorption breakthrough. `src/docs/` is the single source of truth for all content and planning decisions (there is **no** `papers/md/` directory — the live markdown lives directly under `src/docs/`).

## Hard deliverable dates (drives every priority call)

- **Interim Report**: Mon 1 Jun 2026 (Wk 7) — must include full PDE derivation, validated solver, and baseline run vs Stampi-Bombelli 2024 breakthrough benchmark.
- **Final Report**: Mon 10 Aug 2026 (Wk 17).
- **Final Presentation**: 17–19 Aug 2026 (Wk 18).
- **Three validation gates** (must all pass by end of Wk 6 for Interim to land):
  - **Gate A** — linear advection-diffusion solver, L² error < 1%
  - **Gate B** — R-H adsorption shock chord velocity ±10%
  - **Gate C** — Stampi-Bombelli 2024 breakthrough curve τ_BT ±20% at 400 ppm

If a change risks slipping a gate or report deadline, surface that explicitly.

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

`illustration.py` ingests the cleaned CSVs in `src/solver/data/*ml_*g.csv`, walks the reader from the linear transport equation through retarded advection–diffusion to fitted Chern–Chien Langmuir/Freundlich and Clark sigmoids, and writes eight figures to `src/img/generated/`. Every fitted parameter (k_YN, K, tau_BT, C_inf, n, t_50, t_i, mu_max, lambda) is printed to stdout — no hand-tuning.

**IMPORTANT — the real experiment.** The `*ml_*g.csv` runs are **synthetic-validation placeholders, not measured data**, and feed only the synthetic-validation appendix of `experimental-results.md`. The measured experiment is the five bench runs in `src/solver/data/new runs/` (run 3/4/5/6/8), processed by `new_runs_pipeline.py` (per-run metadata) + the `breakthrough_fit/` package (24-model fitter). Run that to refresh the real results:

```bash
python new_runs_pipeline.py                       # 5 real runs -> breakthrough_out/run N/
python -m breakthrough_fit.assemble_may_prompt    # engineered-prompt tables/figures -> src/img/generated/may_prompt/
```

## Architecture of the solver work

Goal: solve a coupled 4-PDE system on a 1-D packed-bed column for adsorption breakthrough. State vector at each axial node `z`:

| Field | Equation | Notes |
|---|---|---|
| `C(z,t)` — gas-phase CO₂ concentration | gas mass balance + axial dispersion + LDF sink | `derivation.md` §1.1 |
| `q(z,t)` — solid loading | LDF kinetics, Toth closure for `C*` | `derivation.md` §1.2, §1.5 |
| `T_g(z,t)` — gas temperature | gas energy balance + interphase heat transfer | `derivation.md` §1.3 |
| `T_s(z,t)` — solid temperature | solid energy balance + heat of adsorption | `derivation.md` §1.4 |

Key differences from the old regeneration scope:
- **Q_wall = 0** (adiabatic adsorption; no external heater)
- **IC: clean bed** — C = 0, q = 0, T_g = T_s = T_ads
- **Inlet BC: step C_in** — CO₂ concentration step at z = 0
- **Isotherm: Toth** (not Langmuir) — parameters fully available from Stampi-Bombelli 2024

Numerical method:
- **Method of Lines** — discretize `z`, integrate in `t` with `scipy.integrate.solve_ivp` (`LSODA` or `BDF`).
- **First-order upwind** for advection (`-u·∂/∂z`).
- **Central differences** for diffusion (`∂²/∂z²`).
- **Dirichlet inlet BC** enforced by zeroing `dY/dt[0]`.
- State packing: flat vector `[C, q, Tg, Ts]` of length `4N`, split with `np.split(y, 4)` inside `rhs`.

When extending the solver, keep this layout.

## Toth isotherm parameters (Stampi-Bombelli 2024, Table 2)

Sorbent: amine-functionalised γ-alumina, 3 mm ring pellets.

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

- `src/docs/` — **single source of truth** for all scientific content. Key files: `experimental-results.md` (Experimental Results & Analysis section), `derivation.md`, `CO2-adsorption-model.md`, `equation_compendium.md`, `literature-survey-summary.md`, `my-research-paper.md`. Engineered prompts live in `src/docs/prompts/`.
- `src/docs/archive (DO NOT OPEN)/` — **superseded old-scope material** (incl. the old `study_plan.md` and `research.md`). Do not read or edit anything in this folder.
- `src/docs/derivation.md` — symbolic forms, term-by-term meaning, non-dimensionalisation. Consult before changing solver math. (Still reflects the old regeneration scope; update separately.)
- `src/sprints/<DD-MM>.md` — dated weekly sprint plans. Newer sprint files supersede older ones.
- `CO2_Regen_Project_Tracker.xlsx` — eight tabs; Experiment Log and gate verdicts. Note: tracker sweep matrix needs updating to reflect new parameters (u, C_in, L, T_ads).

## Experimental design — as executed (the real basis)

The **only correct measured basis** is the five bench runs in `src/solver/data/new runs/`
(run 3/4/5/6/8). Their authoritative metadata is the measurements block (per-run mass/bed
length + the adsorption pressure-drop table); inlet C₀ is read per run from the data.

Fixed: column **38.6 cm × 8.5 mm i.d.**; sorbent **~8.00 g** PEI@SiO₂ in a **~21 cm** bed;
**ambient** (uncontrolled) T; P ≈ 101.325 kPa. Swept: inlet flow and inlet CO₂.

| Run | Inlet flow Q | C₀ (measured) | bed L | best model (overall) | q_dyn |
|---|---|---|---|---|---|
| run 3 | 0.15 lpm (150 mL/min) | 47,400 ppm (~4.7 %) | 21.0 cm | M11 Fractal-Erf | 0.555 mol/kg |
| run 4 | 0.05 lpm (50 mL/min)  | 97,800 ppm (~9.8 %) | 21.3 cm | M14 Weibull (M11 4th) | 0.810 mol/kg |
| run 5 | 0.10 lpm (100 mL/min) | 95,420 ppm (~9.5 %) | 21.2 cm | M11 Fractal-Erf | 0.552 mol/kg |
| run 6 | 0.15 lpm (150 mL/min) | 102,140 ppm (~10.2 %) | 21.5 cm | M10 Fractal-Gudermann (M11 5th) | 0.885 mol/kg |
| run 8 | 0.10 lpm (100 mL/min) | 150,630 ppm (~15.1 %) | 21.5 cm | M10 Fractal-Gudermann (M11 2nd) | 0.787 mol/kg |

Cleanest sub-sweep: the ~10 % CO₂ flow sweep = runs 4 (50) / 5 (100) / 6 (150) mL/min.
Outputs per run: 24-model fits + `t_BT` (C/C₀=0.05), `t_E` (0.95), `t50`, `q_dyn`, `L_MTZ`, ψ.

The earlier "39-run / 11 OAT + 9 u×C_in" matrix is **planned, not executed**; the H1–H5
thresholds have not been tested against measured data. Do not invent sweep points; flag any.

### Recent audit corrections (2026-05-31)
- `new_runs_pipeline.py`: run6 flow 0.05→**0.15** lpm, run8 0.125→**0.10** lpm (per the
  pressure-drop table — measurements are authoritative).
- `breakthrough_fit/performance.py`: removed an unjustified `×1000` in `q_dyn_trapz`; q_dyn
  was ~1000× too low. Now 0.55–0.89 mol/kg, cross-checked vs YN back-calc q₀.
- `breakthrough_fit/assemble_may_prompt.py`: column i.d. was `0.085 m` (85 mm) — corrected
  to **8.5 mm**; RUNS list remapped to runs 3/4/5/6/8; per-run geometry now used in Table 1;
  the old "geometrically inconsistent" FLAG was an artefact of the 10× diameter error.
- Best model per run (corrected): M11 best in runs 3 and 5; M14 (Weibull) in run 4; M10
  (Fractal Gudermannian) in runs 6 and 8. The earlier "M11 every run" claim was stale —
  M11 remains consistently top-3 but does not win all runs. Among prompt-specified models
  (M01/M02/M04/M05/M06/M07/M14/M16/M23), M23 ranks highest by mean Adj. R².

## Critical open data dependencies

**Low-risk** — Toth isotherm and column geometry are fully available from Stampi-Bombelli 2024 (Table 2 above). Gate C is not blocked on supervisor data.

Remaining open items (non-blocking):
- `c_ps` (solid specific heat), `D_ax` (axial dispersion), `h_f` (gas-solid heat transfer) — use literature estimates as placeholders; fit k_LDF at Gate B.
- **`ρ_p` (sorbent/pellet density)** — needed to turn measured ρ_b (~660–672 kg/m³) into a void fraction ε via EC-2. The pipeline currently assumes ρ_p = 800 kg/m³, which gives an unrealistically low ε≈0.16 (floored to 0.30 in code). Real ρ_p is an open input; do not treat ε or ε-based interstitial velocity as physical until it is supplied. Owner: lab / Stampi-Bombelli.
- SUTD rig geometry — if provided by Prof. Birgersson, add as stretch model-vs-experiment check in Discussion. Not required for Gate C.

If solver work blocks on a missing parameter, name the parameter and which supervisor owns it rather than substituting a guess silently.

<<<<<<< HEAD
=======
### Column Geometry (Fixed)

| Quantity | Value | Notes |
|---|---|---|
| Column length, *L* | 38.6 ± 0.1 cm | Fixed geometry |
| Column inner diameter, *d* | 8.5 mm | Fixed geometry |
| Cross-sectional area, *A_c* | π·(0.0085/2)² = 5.675×10⁻⁵ m² | Computed |
| Packed-bed length, *L_bed* | ~21 cm (20.2–21.5 per run) | of the 38.6 cm column |
| Sorbent mass, *m* | ~8.00 g | per-run measured |
| Bulk density, ρ_b | ~660–672 kg/m³ | derived (m / A_c·L_bed) |
| Pellet density, ρ_p | **open** | needed for ε; not yet supplied |

# Operating Times

BREAKTHROUGH TIME (c/c0 = 0.05)
EQUILIBRIUM TIME (c/c0 = 0.95)
>>>>>>> 879b87ec874f8ac4bd37c1eb789f3a05bc190be9

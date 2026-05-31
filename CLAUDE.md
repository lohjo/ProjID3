# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

Single-author NP Year-3 Design Project: **Parametric Study of CO₂ Adsorption Breakthrough in Packed-Bed Columns** (April 2026 semester, supervisors Prof. Erik Birgersson and Prof. Parapsorb Borisut at SUTD/NUS). The repo is a research workspace, not a product — it holds the math derivation, solver code, literature notes, and the project-management tracker that drives weekly work.

Scope revised 30 Apr 2026: from TSA regeneration to adsorption breakthrough. `papers/md/` is the single source of truth for all content and planning decisions.

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

`illustration.py` is the working pipeline behind §5 of the paper: ingests the cleaned CSVs in `src/solver/data/*ml_*g.csv`, walks the reader from the linear transport equation through retarded advection–diffusion to fitted Chern–Chien Langmuir/Freundlich and Clark sigmoids, and writes eight figures to `src/img/generated/`. Every fitted parameter (k_YN, K, tau_BT, C_inf, n, t_50, t_i, mu_max, lambda) is printed to stdout — no hand-tuning. Re-run after editing the dataset to refresh figures.

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

- `papers/md/` — **single source of truth** for all scientific content and planning decisions. Seven papers covering adsorption breakthrough, traveling-wave theory, and DAC sorbents.
- `study_plan.md` — **master spine.** Nine parts + four appendices. Part III is the 18-week table (Wk 1 = 20–24 Apr 2026). Do not let it diverge from reality.
- `derivation.md` — symbolic forms, term-by-term meaning, non-dimensionalisation. Consult before changing solver math. (Note: derivation.md still reflects the old regeneration scope and will need updating separately.)
- `research.md` — literature spine; currently reflects old scope. Needs updating.
- `src/sprints/<DD-MM>.md` — dated weekly sprint plans. Newer sprint files supersede older ones.
- `CO2_Regen_Project_Tracker.xlsx` — eight tabs; Experiment Log and gate verdicts. Note: tracker sweep matrix needs updating to reflect new parameters (u, C_in, L, T_ads).

## Pre-specified experimental design (revised scope)

The 39-run matrix: 11 OAT + 9 u×C_in interaction + ~19 validation/diagnostic.

| Parameter | Levels | Values |
|---|---|---|

Outputs per run: `τ_BT`, `τ_sat`, `η`, `W_MTZ`, `q_dyn`, `v_front`.

Do not invent new sweep points without flagging — H1–H5 thresholds are pre-committed against this matrix.

## Critical open data dependencies

**Low-risk** — Toth isotherm and column geometry are fully available from Stampi-Bombelli 2024 (Table 2 above). Gate C is not blocked on supervisor data.

Remaining open items (non-blocking):
- `c_ps` (solid specific heat), `D_ax` (axial dispersion), `h_f` (gas-solid heat transfer) — use literature estimates as placeholders; fit k_LDF at Gate B.
- SUTD rig geometry — if provided by Prof. Birgersson, add as stretch model-vs-experiment check in Discussion. Not required for Gate C.

If solver work blocks on a missing parameter, name the parameter and which supervisor owns it rather than substituting a guess silently.

### Column Geometry (Fixed)

| Quantity | Value | Notes |
|---|---|---|
| Column length, *L* | 38.6 ± 0.1 cm | Fixed geometry |
| Column inner diameter, *d* | 8.5 mm | Fixed geometry |
| Cross-sectional area, *A_c* | π·(0.0085/2)² m² | Computed |

# Operating Times

BREAKTHROUGH TIME (c/c0 = 0.05)
EQUILIBRIUM TIME (c/c0 = 0.95)
# ProjID3 — CO₂ Adsorption Breakthrough in Packed-Bed Columns

**Parametric Study of CO₂ Adsorption Breakthrough in Packed-Bed Columns.** NP Year-3 Design Project (Apr 2026 semester). Supervisors: Prof. Erik Birgersson (NUS), Dr. Prapatsorn Borisut (SUTD).

> Scope revised **30 Apr 2026**: from TSA *regeneration* to adsorption *breakthrough*. Anything in this repo still referring to "regeneration", `Foolproof_Study_Plan.md`, or an SER/Elfving benchmark is **old-scope and superseded** — see `src/docs/archive (DO NOT OPEN)/`.

## What's here

- `src/docs/` — live scientific content (derivation, proofs, journals, sprints, source papers, LaTeX). Start with `mechanistic-model.md`.
- `src/solver/` — Python solver + the `breakthrough_fit/` 24-model fitter.
- `src/solver/data/new runs/` — the **five measured bench runs** (run 3/4/5/6/8), the only real data.
- `src/img/generated/` — generated figures/tables (headless, 300 dpi).
- `CLAUDE.md` / `AGENTS.md` — working instructions for AI agents (mirror each other; read before making changes).

## Deliverables

- **Interim Report** — Mon 1 Jun 2026 (Wk 7): full PDE derivation + validated solver + baseline vs Stampi-Bombelli 2024 benchmark.
- **Final Report** — Mon 10 Aug 2026 (Wk 17).
- **Final Presentation** — 17–19 Aug 2026 (Wk 18).
- **Validation gates** (all pass by end Wk 6): A (linear adv-diff, L² < 1%) · B (R-H shock chord velocity ±10%) · C (Stampi-Bombelli τ_BT ±20% at 400 ppm).

## Run

```bash
source venv/Scripts/activate        # Git Bash on Windows
pip install -r requirements.txt     # numpy, scipy, matplotlib

python new_runs_pipeline.py                      # 5 real runs -> breakthrough_out/run N/
python -m breakthrough_fit.assemble_may_prompt   # tables/figures -> src/img/generated/may_prompt/
```

The `*ml_*g.csv` and `May-*.csv` files under `src/solver/data/` are **synthetic-validation placeholders, not measured data.**

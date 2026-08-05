# Analysis Code — Simplification Report

> **Status 2026-08-04:** code changes described here were already applied and verified
> (Stage 6 record). This session's work was manuscript-only (`.docx` editing); the two
> flagged code decisions — RMSE denominator, `W_AICc` naming — were **not** changed in code
> this session. `W_AICc` is addressed at the manuscript-text level instead (§7.1's
> corrective note). See `11-process-record.md`.

**Package** `src/solver/breakthrough_fit/` (3,597 LOC, 12 modules) + `new_runs_pipeline.py`
(212 LOC) + `breakthrough_analysis.ipynb`
**Constraint** every applied change is **behaviour-preserving**, verified by regenerating
all nine `newest runs/` and diffing against a pre-change baseline.

## Regression evidence

```
$ python src/solver/new_runs_pipeline.py
$ python cmp_results.py <baseline>
(run, column) pairs differing by > 1e-9 relative: 0
IDENTICAL within 1e-9 across all runs and columns.
```

9 runs × 24 models × 16 numeric columns. Run before the first edit and again after the
last. **No published number moved.**

Separately, the committed artefacts were checked against a fresh environment (numpy 2.5.1,
scipy 1.18.0, matplotlib 3.11.1) before any change: two values in one run differed at the
ninth significant figure, everything else was bit-identical. **The analysis is
reproducible** — worth stating in the report's Python section.

---

# Part 1 — Applied

Net **−53 lines** across 8 files.

## 1.1 Statistics removed from figures (required by reviewer)

Statistics still flow to the CSVs and to stdout. Only the figures lose them.

| File | Was | Now |
|---|---|---|
| `plots.py:60` (P1) | `label=f"{r.code}  R²={...:0.4f}"` | `label=r.code` |
| `plots.py:112` (P2) | `f"{r.code}  R²={...}\n {params}"` | `f"{r.code}\n {params}"` — fitted parameters kept, goodness-of-fit dropped |
| `plots.py:185,187` (P4) | `"M01 Thomas/YN  R²=…"` | `"M01 Thomas/YN"` |
| `plots.py:298` (P6) | `f"{code}  R²={...}"` | `label=code` |
| `plots.py:302-313` (P6) | the **`h = … F-test p = …`** white text box | **deleted** |
| `plots.py:366` (P7) | `f"{r.code}  χ²_red={...}"` | `r.code` |
| `cross_run_figs.py:278-289` | `"best in N"` bar annotations; `"…selected as best by AICc…"` title | annotations deleted; title reduced to *"Model performance ranking"* |
| `cross_run_figs.py:326` | `(best: M23, R²=0.998)` | `(best: M23)` |
| `cross_run_figs.py:380,386` | `best R²=…` in legend; `"best R² ≤ 0"` in title | both removed |

**Dead plumbing removed with it.** `f_p_ba_vs_fractal` existed only to be drawn, so the
parameter and both call-site extractions went too — `main.py:213-218` and
`new_runs_pipeline.py:178-183`, five lines each computing an F-test p-value that is now
unused.

**One judgement call, flagged for you.** `fig10`'s x-axis label *"Mean R² across 12 clean
parametric runs"* was **kept**. There R² is the plotted variable — the bars *are* the
statistic — so removing it would leave an unlabelled axis. The reviewer's objection was to
statistics *annotated onto* curve figures (`h=`, `F-test p=`), which are all gone. Say the
word if you want fig10 stripped too.

**Notebook mirrored.** `breakthrough_analysis.ipynb` re-implements every one of these
functions and would otherwise drift: 9 substitutions and 7 lines removed, verified by diff.
Its code cells syntax-check exactly as before (cell 2 has a pre-existing syntax error,
untouched by this work — worth a look separately).

**Verified visually**, not just by grep: P6 regenerated for
`2026-07-08-conc10-flow0.10` and inspected. The stats box is gone and the fractal model's
advantage still reads clearly from the residual panels — which rather supports the
reviewer's point that the numbers belong in the deck, not the figure.

## 1.2 Path bug — was silently creating a bogus directory tree at import

`assemble_may_prompt.py:46` and `cross_run_figs.py:40` both computed
`REPO = Path(__file__).resolve().parents[1]`. Since the package moved into
`src/solver/breakthrough_fit/`, that resolves to **`src/solver`**, not the repo root:

```
DATA -> src/solver/src/solver/data/new runs   (does not exist)
OUT  -> src/solver/src/img/generated/may_prompt
```

and `OUT.mkdir(parents=True, exist_ok=True)` ran **at import time**, so merely importing
the module created a phantom `src/solver/src/...` tree. Fixed to `parents[3]`, and the
`mkdir` moved inside `main()` where it belongs. Verified: outputs now land in
`src/img/generated/may_prompt/`, and no stray tree appears.

## 1.3 Stale comment pointing at a deleted constant

`assemble_may_prompt.py:53` read *"matches `new_runs_pipeline.py` RUN_META"*. That dict was
deleted on 2026-07-31 when the pipeline was repointed at `newest runs/`. Replaced with an
explanation of why this file's `RUN_META` is now the sole source of truth for runs
3/4/5/6/8 — there is nothing left to mirror.

## 1.4 Dead code

`mtz_fem.assemble_upwind` (17 lines) was never called anywhere. Removed. `FEMesh` and
`build_mesh` were checked first and **are** live — `travelling_wave` uses them — so they
stay. The notebook's documentation table naming `assemble_upwind` was updated to match.

`fit.py:19` imported `get_model` and never used it. Removed.

## 1.5 Duplicated preamble

The same three lines opened five plot functions:

```python
t = df["t"].to_numpy(dtype=float)
y = df["C_C0"].to_numpy(dtype=float)
t_min = t / 60.0
```

Replaced with a documented `_series(df)` helper. Five call sites collapsed to one line
each. This is small but load-bearing: the seconds-to-minutes conversion was written out
five times and could drift in exactly one of them without anyone noticing.

---

# Part 2 — Found and NOT changed, because it would move your numbers

`CLAUDE.md` rule 2 forbids silently altering fitted values. Each of these is a genuine
defect whose fix changes published output, so each is your decision.

## 2.1 RMSE uses a hardcoded `n − 2` regardless of parameter count

`stats.py:74`:
```python
rmse = np.sqrt(rss / max(n - 2, 1))
```
Meanwhile `adj_r2` (`:70-72`) and `chi2_red` (`:81`) both correctly use `n − n_params`.
So a 4-parameter model's RMSE is computed as if it had 2.

With n ≈ 1000 the numerical effect is tiny (√(998/996) ≈ 1.001), but RMSE is reported per
model in every results CSV and appears in the report's error-statistics section. **Decide
before writing §4**, since that section will quote these numbers.

## 2.2 `W_AICc` is not an Akaike weight

`stats.py:113-124` computes `1/(1 + exp(0.5·Δ))` and stores it as `aic_weight`, written to
every CSV as `W_AICc`. A real Akaike weight is `exp(−Δ/2) / Σ exp(−Δ/2)` and sums to 1
across the model set. The shipped quantity does not sum to 1 and is a pairwise logistic
transform of the AICc gap, not a weight.

Two ways out: implement the real weight (changes a published column), or rename the column
to something honest like `AICc_rel`. **Either is fine; shipping it as `W_AICc` is not** —
a reviewer who sees "Akaike weight" will expect the values to sum to 1.

Related: `stats.py:88` sets `aicc = aic + np.inf` for the degenerate case. `np.nan` is the
correct sentinel; `+inf` makes a model look infinitely bad rather than unrankable.

## 2.3 CLI physical parameters are never actually wired in

`models.py` hardcodes `eps=0.37, rho_b=700.0, C0=1.0` into the M16/M18/M19/M22 signatures.
`main.py:71-75` exposes `--bed-void` and `--rho-b` for exactly these. The bridge is
`ModelFitter(extra_kwargs=…)` (`fit.py:50,55`) — which **neither driver ever populates**.

So those flags are silently ignored and the models always use the literals. Since your
measured ρ_b is ~660–672 kg/m³, not 700, M16/M18/M19/M22 are being fitted with the wrong
bulk density right now. Wiring it up changes those four models' output.

## 2.4 The ε floor

`new_runs_pipeline.py:116`:
```python
eps_b = max(1.0 - rho_b / 800.0, 0.3)
```
Two undocumented assumptions in one expression: ρ_p = 800 kg m⁻³ and a 0.30 floor.
`CLAUDE.md` records that this gives a physically implausible ε ≈ 0.16 before flooring.
Leaving it alone is correct until the lab supplies ρ_p — but it needs a named constant and
a comment, not a bare literal. **This value is currently published in the report's Table 3
as a measured interstitial velocity** (see `00-integrity-report.md` IL-SERIOUS-5).

## 2.5 Table 1's C₀ cell can never populate

`assemble_may_prompt.py:228` reads a `c0_ppm` column that no `_write_csv` ever writes, so
the cell always falls back to `—` (`:231`) while the table footnote (`:242`) claims
per-run measured C₀. Fixing it means adding a column to the CSV writer — a schema change.

## 2.6 The two drivers have already diverged

`main.py:108-219` and `new_runs_pipeline.py:85-185` are the same ~100-line function, forked.
They now disagree on CSV column names — `main.py` writes `t_b`/`t_E`/`t50`,
`new_runs_pipeline.py` writes `t_b_s`/`t_E_s`/`t50_s` — and each downstream consumer works
with only one: `cross_run_figs.py:182-184` reads the former, `assemble_may_prompt.py:187-189`
the latter.

Merging them is the single largest maintainability win available, but **renaming a column
breaks one consumer either way**, so it needs your call on which name wins. Recommendation:
keep the `_s` suffix (it documents the unit) and update `cross_run_figs.py`.

## 2.7 Two models never converge but report success

```
M19  Chern-Chien Freundlich   4  nan  inf  inf  nan  inf  True
M18  Chern-Chien Langmuir     4  nan  inf  inf  nan  inf  True
```
`converged=True` with NaN R² and infinite RSS. Either the convergence flag is wrong or the
models are misparameterised. Both are also uncited in the literature review. Fix them or
drop them — but don't report a 24-model comparison in which two members never produce a fit.

---

# Part 3 — Recommended, not yet applied

Behaviour-preserving but large enough that they deserve their own review pass.

| Target | Problem | Suggested approach |
|---|---|---|
| `models.py:584-804` | 220-line literal `REGISTRY` of 24 near-identical blocks; `((1e-6,1.0),(1.0,1e6))` repeated verbatim ~6×; `_init_M06`/`_init_M08` are pure aliases of `_init_M01` | Declarative table + a `register()` helper; name the shared bounds tuples. **Highest-value remaining refactor** — I left it because a bounds typo here silently changes every fit, and it deserves a dedicated verification run |
| `models.py:232-315` | `model_M18` and `model_M19` are byte-identical brentq loops differing only in the helper called | One parameterised implementation |
| `fit.py:84-182` | 99-line `fit_one` doing masking, multi-start, two optimiser branches, refit, stats and stderr; four bare `except Exception` that discard the error | Split into four functions; let errors surface or log them |
| `parse.py:102-401` | Four format parsers sharing an identical 5-line tail (`:140-144`, `:221-225`, `:296-300`, `:376-380`); ~6 magic column indices; `auto_detect` falls through to format "B" on a misparse | Shared tail helper, named constants, explicit detection failure |
| `plots.py` | Model codes hardcoded away from the registry (`langmuir_codes`, `freundlich_codes`, `results.get("M01")`) | Tag models in the registry; look up by tag |
| `assemble_may_prompt.py:351-357` | A **fourth** implementation of the F-test, inline, when `stats.f_test` and `fit.nested_ftests` already exist | Call `stats.f_test` |
| `assemble_may_prompt.py` / `cross_run_figs.py` | `parse_params`, `model_curve`, `t_at_level` duplicated near-verbatim between the two | Move to a shared module |
| `performance.py:91-121` | Breakthrough levels 0.05/0.95/0.5 hardcoded at five sites | Module constants |

## Repository hygiene

- **29 `.pyc` files are committed** and there is **no `.gitignore`**. Every run dirties the
  working tree with bytecode. Add a `.gitignore` and `git rm -r --cached` the `__pycache__`
  directories.
- **Two divergent `breakthrough_out/` trees** — one at the repo root (9 runs) and one at
  `src/solver/` (33 runs) — because `new_runs_pipeline.py:38` uses a CWD-relative
  `OUT_DIR`. The same nine runs exist in both. Make `OUT_DIR` absolute relative to the
  repo root, and delete the duplicate.
- **`CLAUDE.md` documents a committed `venv/` at the repo root that does not exist**, and
  the interpreter on `PATH` lacked scipy, matplotlib and pandas. The documented setup does
  not work. I created `.venv` and installed from `requirements.txt`; update the docs (and
  add `.venv` to the new `.gitignore`).
- **`requirements.txt` is fully unpinned** while `performance.py:82` uses `np.trapezoid`,
  which requires **numpy ≥ 2.0**. That floor is unstated. For a paper claiming
  reproducibility, pin the versions.
- **No tests anywhere.** Given the numbers feed a report, even three golden-file tests over
  one run's `results_*.csv` would protect against exactly the kind of silent drift this
  refactor had to guard against manually.

# Engineering Prompt — Collapse `breakthrough_fit/` into One Self-Contained Notebook

*Purpose: reorganize `src/solver/breakthrough_fit/` (12 modules, 3 496 lines) + `src/solver/new_runs_pipeline.py` (218 lines) into a single self-contained Jupyter notebook driven by `src/solver/data/newest runs/`. This file is dispatched head-to-head to two models; §3 (not sent) holds the scoring rubric and the diff procedure. Facts in §2 were verified against the repo on 2026-07-31 — see §3 for what was executed to verify them.*

---

## PROMPT (send as-is)

You have read/write access to the repository at `C:\Users\User\Projects\GitHub\ProjID3`. Don't search the internet.

Reorganize the breakthrough-fitting code into **one self-contained Jupyter notebook** at `src/solver/breakthrough_analysis.ipynb`, driven by the nine measured runs in `src/solver/data/newest runs/`.

### Definition of "self-contained" (hard rule)

The notebook must run with `src/solver/breakthrough_fit/` **renamed to something else**. That is the acceptance test, and it is mechanical. Concretely, forbidden anywhere in the notebook:

- `import breakthrough_fit`, `from breakthrough_fit …`, or any relative-import remnant (`from .models import …`)
- `sys.path.append` / `sys.path.insert`
- `%run`, `%load`, `importlib`
- creating any new adjacent `.py` file the notebook imports

Everything the notebook needs — parser, 24-model registry, fitter, statistics, performance metrics, plotting — lives in the notebook's own cells. Its only external inputs are the CSVs under `src/solver/data/newest runs/` and the installed third-party packages (numpy, scipy, pandas, matplotlib, plus optional tabulate/tqdm).

`src/solver/breakthrough_fit/` and `src/solver/new_runs_pipeline.py` stay on disk, unmodified, as the archived original. You are producing a replacement, not editing them.

### Build method (follow this order; do not skip to the end)

Work the way the notebook will be read: small piece → see the output → promote to a docstringed function → compose. Each stage must actually execute and print or plot something real before you write the next one.

1. **Env cell.** Print python/numpy/scipy/pandas/matplotlib versions. `%matplotlib inline`.
2. **One file, raw.** Read one CSV from `newest runs/` with plain `pandas`/`open`. Show the head. Look at it before writing a parser.
3. **Parser, incrementally.** Get `t` (seconds) and `C/C0` out of that one file. Plot it. Only then generalise to a function.
4. **One model.** `model_M01` (Yoon–Nelson logistic) + a `curve_fit` call on that one run. Overlay fit on data. Print the parameters.
5. **Statistics.** R², Adj R², RMSE, AIC, AICc for that one fit. Verify by hand on the printed numbers that AICc > AIC and that R² is sane.
6. **All 24 models.** Registry + multi-start fitter. Ranked-by-AICc table for the one run.
7. **Nested F-tests**, then **performance metrics** (t_b, t_E, t₅₀, q_dyn, L_MTZ, ψ).
8. **Plots P1–P7** for the one run, displayed inline *and* saved to disk.
9. **Loop** the whole thing over all nine runs.
10. **Cross-run summary** — the flow and concentration trends.

**Where the "put it in a file.py and import it" step goes.** It becomes a *consolidation cell*, not a file. Once a scratch cell works, rewrite it as a function with a real docstring and move it into the nearest **Definitions** cell above; the scratch cell is then deleted, and downstream cells call the function. The notebook *is* the `file.py`. If you end up with a helper `.py` next to the notebook, you have failed the hard rule above.

**Keep expensive objects in RAM.** Fits are the expensive artefact — 24 models × 12 starts × 9 runs. Accumulate them into a notebook-global

```python
RESULTS: dict[str, dict[str, FitResult]] = {}   # run_id -> code -> FitResult
```

guarded by a `REFIT = False` flag, so that re-running any downstream plotting or analysis cell reuses the in-memory fits and never re-fits. Every analysis cell reads `RESULTS`; only the fitting cell writes it.

### Non-negotiables (getting any of these wrong invalidates the result)

- **Data basis.** Exactly the nine runs listed in §"Run metadata" below, from `src/solver/data/newest runs/`. Column i.d. **8.2 mm**, T = 298.0 K, P = 101 325 Pa.
- **The two `2026-07-17-*` files are excluded.** They are raw sensor logs with no mass / bed-height / C₀ header. Do not fabricate geometry for them. Skip them and say so in a markdown cell.
- **You will encounter repo documentation stating the measured basis is five runs (`run 3/4/5/6/8`) at 8.5 mm i.d.** That describes the *previous* basis and is stale relative to this task. Use the nine-run / 8.2 mm basis. **Flag** the discrepancy in a markdown cell; do **not** edit `CLAUDE.md`, `AGENTS.md`, or `src/docs/experimental-results.md` to reconcile it.
- **No fabricated numbers.** Every parameter comes from a fit printed to stdout or from a run's own file header. No hand-tuning.
- **Preserve the open-input flags.** Pellet density `ρ_p = 800 kg/m³` is an *assumption*, and `eps_b = max(1 - rho_b/800, 0.3)` floors an unphysically low void fraction at 0.30. Both are unresolved inputs owned by the lab. Carry them across verbatim **with their flag comments**. They look like bugs; they are not yours to fix.
- **Determinism.** `n_starts=12`, `seed=42`. The RNG is re-seeded *per model*, so all 24 models see identical start sequences — preserve that.

### The one place you must write new code

`breakthrough_fit/parse.py` **cannot read these nine files.** Its `auto_detect` classifies them as format `"D"` and dispatches to `self.parse_format_d(...)`, **which does not exist** — every run raises `AttributeError`, the pipeline's per-run `try/except` swallows it, and zero output is produced. This is why `src/solver/breakthrough_out/` contains no `2026-*` directories.

So this port is not a pure translation: you must implement the Format-D reader. Its layout is specified in §"Format D" below. Two consequences to handle deliberately:

- **`Time (min)` is in minutes.** The models and every downstream metric assume `t` in **seconds**. Convert. A missed ×60 silently rescales every rate constant and every breakthrough time.
- **The file header duplicates `RUN_META`.** Mass, bed height, flow, C₀ and tube diameter all appear in the file's own prose block. Parse them, then **assert** they agree with the hardcoded `RUN_META` and raise loudly on mismatch. Do not silently prefer one source over the other.

### Port-time traps (each one silently changes results if missed)

1. `plots.py` calls `matplotlib.use("Agg")` **at module import**. Copying that line into the notebook kills `%matplotlib inline` and nothing displays. Drop it.
2. `plots.py` never closes figures. 9 runs × 7 plots = 63 open figures. Close them in the loop.
3. `_save()` currently only writes to disk. In the notebook it must **both** `savefig(..., dpi=300)` **and** return/display the figure.
4. `rank_aicc` mutates its `results` argument in place and sets `aic_weight = 1/(1 + exp(0.5·ΔAICc))` — a pairwise logit, **not** the conventional normalised Akaike weight. Port it verbatim. "Correcting" it changes every `W_AICc` ever stored.
5. `M05` (Wolborska) is `early_only`: both the fit **and** its statistics are restricted to `0.005 < C/C0 ≤ 0.15`, and it needs ≥3 such points.
6. `M20`'s registry parameter name is `log_a0_C0` but its function's keyword is `log_a0_over_C0`. Positional calls only.
7. `M18`/`M19` (Chern–Chien) are implicit — solved per-point with `brentq`, fitted with L-BFGS-B on RSS instead of `curve_fit`. They return NaN where the root solve fails; that is expected, not a bug to patch.
8. **Output-path bug.** `new_runs_pipeline.py` has `DATA_DIR = Path("src/solver/data/newest runs")` (repo-root-relative) but `OUT_DIR = Path("breakthrough_out")` (bare) — so outputs land wherever the process was launched. Anchor both to an absolute `REPO` root in the notebook and write to `src/solver/breakthrough_out/<run_id>/`.
9. **Results-CSV schema fork.** `main.py` writes `t_b`/`t_E`/`t50`; the on-disk CSVs and everything downstream use `t_b_s`/`t_E_s`/`t50_s`. Adopt the `_s` spelling and note the choice.
10. `q_dyn_trapz` uses `np.trapezoid` (NumPy ≥ 2.0 spelling). Its docstring records that a spurious `/1000` was removed on 2026-05-31 — CSVs older than that carry `q_dyn` 1000× low. Keep the corrected version.

### What to port, what to drop

Port, consolidated into the notebook: `parse.py` (+ the missing Format D), `models.py`, `stats.py`, `fit.py`, `isotherm.py`, `performance.py`, `plots.py`, `mtz_fem.py`'s `travelling_wave` and `project_snapshots` (P5 depends on them), and the orchestration spine of `new_runs_pipeline.py` (`RUN_META`, per-run geometry, `run_one`, `_write_csv`).

Drop, and state the reason for each in a markdown cell:

- `main.py` — argparse CLI superseded by `new_runs_pipeline.py`; its geometry defaults (`--column-diameter 3.37`, `--column-length 32.5`) belong to a different rig.
- `cross_run_figs.py` — keyed to the legacy synthetic `NNNml_Ng` run directories, and reads `breakthrough_out/` as an input.
- `assemble_may_prompt.py` — built on the superseded five-run / 8.5 mm basis, reads `breakthrough_out/` as an input, and `mkdir`s at import time. If you want its four tables and parity plot, re-derive them from `RESULTS` on the nine-run basis; do not port the module.
- `mtz_fem.FEMesh` / `build_mesh` / `assemble_upwind` — dead scaffold, nothing calls them.

`breakthrough_out/` is a **cache, not an input**. Nothing in the notebook may read a previously written `results_*.csv`.

### Acceptance criteria (all mechanically checkable)

1. **Restart & Run All** from a clean kernel completes top-to-bottom with zero errors and no dependence on out-of-order execution.
2. Nine directories under `src/solver/breakthrough_out/`, one per run id, each containing `results_<run_id>.csv` plus `P1_<run_id>.png` … `P7_<run_id>.png`.
3. Each `results_<run_id>.csv` has 24 rows and the `_s` column spelling.
4. Renaming `src/solver/breakthrough_fit/` and re-running the notebook changes nothing. Demonstrate it.
5. A grep of the notebook source for the forbidden constructs listed under "Definition of self-contained" returns nothing.
6. Every dropped module is named in a markdown cell with its drop reason; every one of the ten port-time traps is either handled or explicitly waived in a markdown cell.
7. The Format-D parser is validated against at least one file's own header block: parsed C₀, mass, bed height and tube diameter printed alongside the `RUN_META` values, matching.
8. `REFIT = False` demonstrably short-circuits: re-executing the fit cell after a completed run returns immediately.

State plainly which criteria you verified by execution and which you did not. Do not report the notebook as working on the strength of the code looking right — run it.

---

## Information you may or may not need

### Run metadata (nine runs, from `new_runs_pipeline.py`)

```python
RUN_META = {   # all m_g = 8.0
    "2026-06-26-conc5-flow0.05":  dict(Q_lpm=0.05, m_g=8.0, L_bed_cm=23.5),
    "2026-07-03-conc5-flow0.10":  dict(Q_lpm=0.10, m_g=8.0, L_bed_cm=24.0),
    "2026-07-08-conc5-flow0.15":  dict(Q_lpm=0.15, m_g=8.0, L_bed_cm=23.5),
    "2026-07-08-conc10-flow0.05": dict(Q_lpm=0.05, m_g=8.0, L_bed_cm=23.0),
    "2026-07-08-conc10-flow0.10": dict(Q_lpm=0.10, m_g=8.0, L_bed_cm=23.3),
    "2026-07-08-conc10-flow0.15": dict(Q_lpm=0.15, m_g=8.0, L_bed_cm=24.0),
    "2026-07-10-conc15-flow0.05": dict(Q_lpm=0.05, m_g=8.0, L_bed_cm=24.5),
    "2026-07-10-conc15-flow0.10": dict(Q_lpm=0.10, m_g=8.0, L_bed_cm=24.0),
    "2026-07-15-conc15-flow0.15": dict(Q_lpm=0.15, m_g=8.0, L_bed_cm=24.0),
}
D_COL_M = 0.0082      # 8.2 mm i.d., per the newest-runs headers
T_K     = 298.0
P_PA    = 101_325.0
```

Files are `<run_id>.csv` in `src/solver/data/newest runs/`, 491–1 760 lines each. The design is a 3 × 3 sweep: {5, 10, 15} % CO₂ × {0.05, 0.10, 0.15} lpm.

Per-run geometry, as computed by the pipeline:

```python
A_c       = np.pi * (D_COL_M / 2.0) ** 2
L_bed_m   = L_bed_cm * 1e-2
flow_m3_s = Q_lpm * 1e-3 / 60.0
u         = flow_m3_s / A_c
rho_b     = (m_g * 1e-3) / (A_c * L_bed_m)
eps_b     = max(1.0 - rho_b / 800.0, 0.3)   # rho_p = 800 ASSUMED; 0.30 floor — open input, owner: lab
v_int     = u / max(eps_b, 1e-6)
c0_mol_m3 = ppm_to_mol_m3(run.c0_ppm, T_K=T_K, P_Pa=P_PA)
```

### Format D (the one you must implement)

CRLF line endings. Row 1 cell A1 holds a **quoted five-line prose block** (a single CSV field spanning five physical lines), then blank rows, then a metadata block in columns I–O, then the real header row, then data:

```
"Mass: 8g
Bed height: 233 mm
Flow rate: 100 ml/min
CO2: 10% (100580 ppm)
Tube diameter: 8.2 mm",,,,,,,,,,,,,,
,,,,,,,,,,,,,,
,,,,,,,,,,,,,,
,,,,,,,,,,,,,,
,,,,,,,,Mass,8,g,,tb,5.42,min
,,,,,,,,R,8.314,J/molK,,qb,0.28,mmol/g
,,,,,,,,P,101400,Pa,,te,72.85,min
,,,,,,,,v,0.1,dm3/min,,qe,1.13,mmol/g
,,,,,,,,C0,100580,ppm,,,,
Time,Time (min),CO2,C/C0,Pressure,Temperature,Humidity,Flow,Mol adsorbed,Total (mol),mmol/g,,,,
40:03.5,0.00,0,0,1014,23.2,43.4,0.1,0.0000,0.0000,`,,,,
40:08.5,0.08,0,0,1014,23.2,43.4,0.1,0.0000,0.0000,0.0043,,,,
```

Notes: `Time (min)` is **minutes** — convert to seconds. `CO2` is ppm; `C/C0` is supplied directly. `Pressure` is mbar. The `tb`/`qb`/`te`/`qe` values in the metadata block are the **lab's own** spreadsheet estimates — useful as an independent cross-check on your computed `t_b`/`t_E`, not as inputs. The first data row's `mmol/g` cell contains a stray backtick. Trailing empty columns are padding.

For reference, `auto_detect` already routes these correctly (`"bed height:"` or `"tube diameter:"` in the first five lines ⇒ `"D"`); only `parse_format_d` is missing. The other three formats — A (raw multi-channel sensor log), B (labelled `Time (s)` / `C/C0` with an I–O metadata block), C (bare datetime + ppm, used by the older `run 3/4/5/6/8` files) — are implemented and are not needed for the nine runs, though porting them costs little and keeps the parser general.

### Package inventory

| module | lines | contents |
|---|---|---|
| `parse.py` | 340 | `ParsedRun`, `DataParser` (`auto_detect`, `parse_format_a/b/c`, `_despike(threshold=0.15)`, `_parse_metadata_b`) |
| `models.py` | 811 | `model_M01`…`model_M24`, `weibull_derivative`, `BreakthroughModel` dataclass, `REGISTRY` (24 entries with param names/bounds/groups/flags), `_init_M01`…`_init_M24`, `get_model`, `_sigmoid`, `_safe_pow` |
| `stats.py` | 124 | `FitStats`, `compute_stats`, `f_test`, `rank_aicc` |
| `fit.py` | 294 | `FitResult`, `ModelFitter`, `NESTED_PAIRS`, `nested_ftests` |
| `isotherm.py` | 111 | `ppm_to_mol_m3`, `back_calculate_q0`, `back_calculate_q0_from_kT`, `back_calculate_a0_from_kBA`, `langmuir_linear_fit`, `freundlich_log_fit` |
| `performance.py` | 128 | `PerformanceMetrics`, `t_breakthrough`, `q_dyn_trapz`, `l_mtz`, `column_efficiency`, `metrics` |
| `plots.py` | 373 | `plot_P1`…`plot_P7`, `_save`, `_vlines`, `_rolling_mean`; `_DPI = 300` |
| `mtz_fem.py` | 90 | `travelling_wave`, `project_snapshots` (used by P5); `FEMesh`/`build_mesh`/`assemble_upwind` (dead) |
| `main.py` | 285 | argparse CLI — drop |
| `assemble_may_prompt.py` | 464 | five-run tables/figures — drop |
| `cross_run_figs.py` | 450 | legacy synthetic-run figures — drop |
| `__init__.py` | 26 | eager submodule imports |
| `new_runs_pipeline.py` | 218 | orchestration spine — port |

`NESTED_PAIRS = (("M01","M02"), ("M01","M04"), ("M01","M23"), ("M02","M03"), ("M07","M11"), ("M06","M10"))`.

`results_<run_id>.csv` columns, one row per model: `run_id, fmt, code, name, converged, n, p, RSS, R2, AdjR2, RMSE, chi2_red, AIC, AICc, W_AICc, AAD, params, stderr, message, t_b_s, t_E_s, t50_s, q_dyn_mol_per_kg, L_MTZ_m, efficiency`. `params`/`stderr` are `;`-joined `name=value` blobs at `0.6g`.

### Environment

The committed venv is Python 3.14 with numpy 2.4.4, scipy 1.17.1, matplotlib 3.10.8, pandas 3.0.3, tabulate 0.10.0, tqdm 4.67.3. **Jupyter is not installed** — no `ipykernel`, `nbformat`, `IPython`, or `jupyter*.exe`. Step 0 is:

```bash
source venv/Scripts/activate            # Git Bash on Windows
pip install jupyter ipykernel nbformat
```

and adding those three to `requirements.txt` (currently six unpinned lines). Record this; it is the one repo file outside the notebook you may modify.

### House precedent

`src/solver/mechanistic_selfcontained.py` (753 lines) is this repo's existing self-contained artefact — "reads ONLY the CSVs in `src/solver/data/…`. No imports from `breakthrough_fit/` or any other repo module." Match its conventions (absolute `Path`-anchored constants at the top, everything printed to stdout, no hidden state) rather than inventing your own.

---

## Notes on this prompt (for the lead researcher — not part of the sent prompt)

**Dispatch.** Send the PROMPT block above, unmodified and without §2 or §3, to both models in fresh sessions with repo access and no shared context. Both need write access; give them separate git branches or worktrees so the two notebooks don't collide at `src/solver/breakthrough_analysis.ipynb`.

**What was actually verified before writing this** (so a disagreement can be adjudicated against the repo, not against the prompt):

- `DataParser.auto_detect` returns `"D"` for all nine runs and `"A"` for the two `2026-07-17` files; `parse` dispatches `"D"` → `self.parse_format_d`, which does not exist → `AttributeError` on every one of the nine. The nine-run pipeline has therefore never produced output, which matches the absence of `2026-*` directories under `src/solver/breakthrough_out/`.
- The older `run 3/4/5/6/8` files detect as `"C"` — the five-run basis still parses fine, which is why the breakage went unnoticed.
- Line counts, `RUN_META`, `D_COL_M = 0.0082`, and the Format-D header excerpt are read directly from the files.

**Scoring rubric.** Weight to the failure modes, not to polish:

| weight | criterion |
|---|---|
| 25 | Format-D parser correct — minutes→seconds conversion present, header values asserted against `RUN_META`, nine runs actually parsed |
| 20 | Genuinely self-contained — passes the rename test, no helper `.py`, grep-clean |
| 15 | Restart & Run All clean, nine complete output directories, 24 rows each |
| 15 | Staged build honoured — incremental cells with visible output, functions docstringed, `RESULTS`/`REFIT` memoisation actually working |
| 15 | Traps handled — Agg, figure closing, `rank_aicc` verbatim, `early_only`, output paths, `_s` schema |
| 10 | Honest reporting — says what was executed vs. inferred; flags the stale five-run/8.5 mm docs without editing them |

**Failure modes to diff on.** In rough order of likelihood:

1. **Doesn't discover the missing `parse_format_d`.** Ports `parse.py` faithfully, including the dead dispatch branch, and reports success on the strength of the code reading correctly. The nine-run loop then fails at runtime — or worse, the per-run `try/except` swallows it and the notebook "completes" with zero output. This is the discriminating test of whether the model ran anything.
2. **Implements Format D but treats `Time (min)` as seconds.** Everything still runs; every rate constant is 60× wrong and every `t_b` is in the wrong unit. Cross-check against the lab's own `tb`/`te` values in the file's metadata block — a correct parse should land near them.
3. **Ships a helper `.py`.** The stated workflow ends in "put it in `file.py` and import it", and a model that pattern-matches on that instead of on the self-containment rule will produce notebook + module. The rename test catches it.
4. **Reverts to the five-run / 8.5 mm basis** because `CLAUDE.md` hard-rule #1 says so. A model that reads the repo docs carefully is *more* exposed to this, not less. Check `D_COL_M` and the run list.
5. **Fabricates geometry for the two `2026-07-17` files** to make it "a complete eleven-run sweep".
6. **"Fixes" `rank_aicc`** to the conventional normalised Akaike weight, or removes the `eps_b` 0.30 floor as an apparent bug. Both are defensible in isolation and both silently break comparability with every stored result.
7. **One mega-cell.** All 3 496 lines dumped in, nothing staged, no intermediate output — the opposite of the requested method even when the end state technically runs.
8. **Skips the `REFIT` memoisation**, refitting on every cell execution. Costly and directly contrary to the stated reason for wanting a notebook at all.

**Diff procedure.** Run both notebooks yourself. Compare the nine `results_*.csv` sets model-to-model, joined on `(run_id, code)`, on `AICc`, `AdjR2`, `RMSE`, `q_dyn_mol_per_kg`, `t_b_s`. Where they agree, the port is probably faithful. Where they disagree, the difference is almost certainly in the Format-D parser (time units, C₀ source, or despiking) — resolve it against the raw CSV by hand before either result is trusted, and treat a 2-way split as a flag rather than a vote. Nothing from either notebook goes into `experimental-results.md` until this diff is done: the nine-run basis has never produced a single verified number, so there is no incumbent to fall back on.

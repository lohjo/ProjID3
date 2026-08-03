---
name: Minimal kinetic model
description: Minimal kinetic model for adsorption kinetics, fitted to experimental data.
related files: 
  - src/solver/minimal_kinetic_model.py
  - src/img/generated/minimal_kinetic/minimal_kinetic_fit.png
  - src/img/generated/minimal_kinetic/minimal_kinetic_rh.png
---

Results — src/solver/minimal_kinetic_model.py (rewritten, self-contained)

Global fit (one set across runs 3/4/5/6/8, FITTED not literature):

┌───────┬─────────────────────────────────────┐
│ param │                value                │
├───────┼─────────────────────────────────────┤
│ qm    │ 1.5306 mol/kg                       │
├───────┼─────────────────────────────────────┤
│ b     │ 4.53e-5 1/Pa (0.112 m³/mol @ 298 K) │
├───────┼─────────────────────────────────────┤
│ k     │ 1.75e-3 1/s                         │
└───────┴─────────────────────────────────────┘

Per-run RMSE(C/C0): 0.041–0.073. C0 values match audited table exactly (47400/97800/95420/102140/150630 ppm) — inline parser reproduces pipeline.

R-H verification (required check): PASS — run 5 geometry, equilibrium limit: v_RH = 3.681e-4 m/s, v_num = 3.683e-4 m/s, error 0.050 % (« 10 %). Shock fronts sit on grey v_RH·t lines; outlet breaks exactly at t_st.

Figures → src/img/generated/minimal_kinetic/: minimal_kinetic_fit.png, minimal_kinetic_rh.png (mechanistic V2-style).

Bug caught during verification — first fit stalled silently at x0 (cost 49.1 vs true 4.04; nfev=14, params unmoved). Root cause: least_squares default FD step ~1e-8 below LSODA noise floor (rtol 1e-6) → garbage Jacobian. Fixed: diff_step=1e-3 + 3-start multi-start (shallow qm·b ridge; two independent starts agree, optimality 0.03). Saved as project memory.

Flags (unchanged open items):
- ε = 0.30 floor from placeholder ρ_p = 800 — not physical until ρ_p supplied (lab / Stampi-Bombelli).
- Model systematically too sigmoid vs measured instant-rise + long tail (visible run 3, 4) — the spec's own stated LDF/Langmuir limitation, not a fit failure.
- Danckwerts inlet = exact face flux F₀ = u·c_f, D_L = 0 per A1 (mechanistic-model2 Part E scheme (b)).

Ponytail installed (Phase 0) + applied: stdlib csv/datetime parser (no pandas), zero project imports, one runnable self-check (R-H assert).
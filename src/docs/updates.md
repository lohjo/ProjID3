study_plan.md (v1.0 → v2.0): Complete rewrite.
  - Title: "Regeneration" → "Adsorption Breakthrough"
  - Controllable parameters: T_regen/Q_purge/L/m → u/C_in/L/T_ads
  - Metrics: SER/v_th/τ_90 → τ_BT/η/W_MTZ/q_dyn
  - H1–H5: regeneration effects → velocity/concentration/bed-length/temperature/R-H shock
  - Gates B & C: thermal front/Elfving → R-H adsorption shock ±10% / Stampi-Bombelli 2024 τ_BT ±20%
  - Isotherm: Langmuir → Toth (ns0=1.23, b0=4839 kPa⁻¹, t0=0.25, ΔH0=70 kJ/mol — fully in hand)
  - IC/BC: saturated bed + purge inlet → clean bed + step C_in
  - Q_wall: non-zero → zero (adiabatic)
  - Literature map: 7 old regeneration sources → 7 papers from papers/md/
  - Solver scaffold, math track, report chapters, journal anchors all updated accordingly
  - Changelog appended

  CLAUDE.md: Updated repo purpose, gates, solver notes, Toth parameter table. papers/md/ named as source of truth.

  Two files still carry old-scope content and need separate updates: derivation.md and research.md. The .xlsx tracker
  sweep matrix also needs updating.
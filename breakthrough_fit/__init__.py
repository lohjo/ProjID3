"""Breakthrough-curve fitting package.

Modules:
    parse        — CSV parsing for the two lab formats.
    models       — Closed-form models M01–M24.
    stats        — Goodness-of-fit statistics + F-test.
    fit          — Multi-start nonlinear regression with bounds.
    isotherm     — Back-calculation of q0, Langmuir/Freundlich fits.
    performance  — q_dyn, MTZ length, column efficiency, t_b/t_E.
    plots        — Publication-quality figures P1–P7.
    mtz_fem      — 1-D linear-FEM travelling-wave MTZ projection.
    main         — CLI entry point.
"""

from . import parse, models, stats, fit, isotherm, performance, plots, mtz_fem

__all__ = [
    "parse",
    "models",
    "stats",
    "fit",
    "isotherm",
    "performance",
    "plots",
    "mtz_fem",
]

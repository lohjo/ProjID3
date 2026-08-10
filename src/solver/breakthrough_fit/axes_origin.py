"""Pin figure axes so that (0, 0) sits exactly at the bottom-left corner.

Why this exists
---------------
Every figure in this repo used to float off its own corner. Two habits caused it:

* an explicit negative lower bound -- ``set_ylim(-0.02, 1.05)`` in :mod:`plots`,
  ``-0.05`` in ``illustration.py`` / ``cross_run_figs.py`` / ``report_figs_measured.py``
  -- bought so that a marker sitting at exactly ``C/C0 = 0`` is not bisected by the
  bottom spine;
* pure autoscale on every time axis, which adds matplotlib's 5 % margin at both ends.

The requirement is that the data starts *at* the corner with no padding there. That
is a drawing change only: nothing here touches data, fits or upper bounds.

The rule
--------
:func:`snap_origin` walks a figure and pins ``left`` / ``bottom`` to exactly ``0.0``
on an axis only when 0 is a valid *and* tight bound. An axis is pinned when all of:

1. the axes is visible, drawn, and has data;
2. the scale is linear -- a log or symlog axis can never reach 0;
3. the data on that axis is entirely >= 0 (within float tolerance);
4. every sibling sharing that axis also passes 2 and 3 -- otherwise pinning one
   panel would silently drag a neighbour's legitimate negative range to 0.

Everything else is left exactly as the caller drew it. That is what keeps residual
panels (P4/P6/P7), the log-x sensitivity scatter, and the similarity-variable plots
in ``illustration.py`` (which legitimately span negative x) untouched, with no
per-figure special-casing anywhere in the calling scripts.

The opposite end of each axis is read back and re-passed unchanged, so
``(-0.02, 1.05)`` becomes ``(0.0, 1.05)``: the C/C0 headroom and the autoscaled
right-hand margin on a time axis both survive.

Usage
-----
Call once per figure, after all artists are added and *before* ``tight_layout()``
(pinning changes the tick labels, which changes the layout matplotlib computes)::

    snap_origin(fig)
    fig.tight_layout()
    fig.savefig(path, dpi=300)

Pass ``verbose=True`` to print an audit line per axis saying what was pinned, what
was skipped, and why -- that log is the evidence the auto-skip rule fired correctly.
"""

from __future__ import annotations

from typing import Iterable, Sequence

import numpy as np


__all__ = ["snap_origin", "axis_report"]


# Float slop when asking "is this data non-negative?". Scaled by the data span so
# that a span of 1e6 tolerates proportionally more noise than a span of 1.
_REL_TOL = 1e-9


def _decide(ax, which: str) -> tuple[bool, str]:
    """Return ``(pin, reason)`` for one axis of one axes object.

    ``which`` is ``"x"`` or ``"y"``. ``reason`` is a short human-readable tag used
    by the audit log; it explains a skip, or names the bound being replaced.
    """
    if not getattr(ax, "axison", True) or not ax.get_visible():
        return False, "axes off"
    if not ax.has_data():
        return False, "no data"

    scale = ax.get_xscale() if which == "x" else ax.get_yscale()
    if scale != "linear":
        return False, f"{scale} scale"

    lim = ax.dataLim
    lo = lim.x0 if which == "x" else lim.y0
    span = lim.width if which == "x" else lim.height
    if not np.isfinite(lo) or not np.isfinite(span):
        return False, "non-finite dataLim"

    tol = _REL_TOL * max(1.0, abs(span))
    if lo < -tol:
        return False, f"data min {lo:.4g} < 0"
    return True, f"data min {lo:.4g}"


def _siblings(ax, which: str) -> Sequence:
    """Axes sharing this x- or y-axis, including ``ax`` itself."""
    grouper = ax.get_shared_x_axes() if which == "x" else ax.get_shared_y_axes()
    try:
        return list(grouper.get_siblings(ax))
    except AttributeError:  # very old matplotlib
        return [ax]


def _apply(ax, which: str) -> None:
    """Set the lower bound to exactly 0, preserving the upper bound."""
    if which == "x":
        _, upper = ax.get_xlim()
        ax.set_xlim(0.0, upper)
    else:
        _, upper = ax.get_ylim()
        ax.set_ylim(0.0, upper)


def snap_origin(
    fig,
    *,
    skip_axes: Iterable = (),
    verbose: bool = False,
    label: str = "",
) -> list[str]:
    """Pin ``left``/``bottom`` to 0 on every axis of *fig* where 0 is valid.

    Parameters
    ----------
    fig
        The :class:`matplotlib.figure.Figure` to adjust, after all plotting.
    skip_axes
        Axes objects to leave completely alone. The escape hatch for a panel
        where pinning to 0 is technically valid but destroys legibility.
    verbose
        Print one audit line per axes.
    label
        Optional figure name used to prefix the audit lines.

    Returns
    -------
    list[str]
        The audit lines, whether or not they were printed.
    """
    skip = set(map(id, skip_axes))
    lines: list[str] = []

    for i, ax in enumerate(fig.axes):
        if id(ax) in skip:
            lines.append(f"  ax[{i}] x:skip(caller) y:skip(caller)")
            continue

        parts = []
        for which in ("x", "y"):
            pin, reason = _decide(ax, which)
            # Condition 4: a shared group moves together, so it may only be pinned
            # if every member of the group independently qualifies.
            if pin:
                for sib in _siblings(ax, which):
                    if sib is ax:
                        continue
                    sib_pin, sib_reason = _decide(sib, which)
                    if not sib_pin:
                        pin, reason = False, f"shared group: {sib_reason}"
                        break
            if pin:
                _apply(ax, which)
                parts.append(f"{which}:pin({reason})")
            else:
                parts.append(f"{which}:skip({reason})")
        lines.append(f"  ax[{i}] " + " ".join(parts))

    if verbose:
        header = f"[snap_origin] {label}" if label else "[snap_origin]"
        print(header)
        for line in lines:
            print(line)

    return lines


def axis_report(fig, label: str = "") -> str:
    """Describe what :func:`snap_origin` *would* do, without changing anything.

    Used by the verification pass: it reads the decision for every axis so the
    skips can be confirmed against expectation before figures are overwritten.
    """
    rows = [f"[axis_report] {label}".rstrip()]
    for i, ax in enumerate(fig.axes):
        parts = []
        for which in ("x", "y"):
            pin, reason = _decide(ax, which)
            parts.append(f"{which}:{'pin' if pin else 'skip'}({reason})")
        rows.append(f"  ax[{i}] " + " ".join(parts))
    return "\n".join(rows)

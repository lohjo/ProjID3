"""Back up every generated figure that the origin-pinning pass will overwrite.

    python src/solver/backup_figs.py --dry-run     # list, touch nothing
    python src/solver/backup_figs.py               # copy

Each file is copied into a ``backup-<stamp>/`` folder *inside the directory that
holds it*, so a run directory ends up as::

    breakthrough_out/2026-07-03-conc5-flow0.10/
        P1_2026-07-03-conc5-flow0.10.png          <- will be regenerated
        backup-2026-08-10/
            P1_2026-07-03-conc5-flow0.10.png      <- the original

Copy, not move: the regenerated figure has to land back on the original path, and
a half-finished regeneration must never leave a hole where a committed figure was.

Scope is deliberately narrow -- only what the regeneration actually rewrites:

* ``src/img/generated/**`` for the nine in-scope generator scripts;
* P1-P7 for the sixteen grid runs, in *both* ``breakthrough_out`` trees;
* ``may_prompt/`` table CSVs and ``tables.md``, because ``assemble_may_prompt.py``
  rewrites them as a side effect of redrawing its two plots.

Explicitly NOT backed up, because nothing regenerates them: runs 3/4/5/6/8, the
synthetic ``*ml_*g`` / ``May-*`` run directories, ``wrong jac_pattern/`` (no script
writes there), and ``_figcache/`` (derived, mtime-invalidated, rebuilds itself).
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
STAMP = "backup-2026-08-10"

IMG = REPO / "src" / "img" / "generated"
BT_ROOT = REPO / "breakthrough_out"
BT_SOLVER = REPO / "src" / "solver" / "breakthrough_out"
GRID_DATA = REPO / "src" / "solver" / "data" / "newest runs"

# Sub-directories of src/img/generated that a script writes to. "" is the top
# level (fig1-fig12). "wrong jac_pattern" is absent on purpose.
IMG_SUBDIRS = [
    "",
    "report",
    "sensitivity",
    "mechanistic",
    "mechanistic_selfcontained",
    "psi_quadrature",
    "minimal_kinetic",
    "may_prompt",
]

# assemble_may_prompt.py rewrites these alongside Plot1/Plot8.
EXTRA_PATTERNS = {"may_prompt": ("table*.csv", "tables.md")}


def grid_run_ids() -> list[str]:
    """The sixteen grid runs, taken from the data folder rather than hardcoded."""
    return sorted(p.stem for p in GRID_DATA.glob("*.csv"))


def collect() -> list[tuple[Path, Path]]:
    """Build the (source, destination) list. Nothing is touched here."""
    jobs: list[tuple[Path, Path]] = []

    for sub in IMG_SUBDIRS:
        d = IMG / sub if sub else IMG
        if not d.is_dir():
            print(f"  [warn] missing directory, skipped: {d}")
            continue
        names = ["*.png", *EXTRA_PATTERNS.get(sub, ())]
        for pattern in names:
            for src in sorted(d.glob(pattern)):
                if src.is_file():
                    jobs.append((src, d / STAMP / src.name))

    run_ids = grid_run_ids()
    for tree in (BT_ROOT, BT_SOLVER):
        for run_id in run_ids:
            d = tree / run_id
            if not d.is_dir():
                # Two grid CSVs are raw sensor logs the pipeline skips; they have
                # no output directory and that is correct, not an error.
                continue
            for src in sorted(d.glob("P?_*.png")):
                jobs.append((src, d / STAMP / src.name))

    return jobs


def main(argv: list[str]) -> int:
    dry = "--dry-run" in argv
    jobs = collect()

    by_dir: dict[Path, int] = {}
    total_bytes = 0
    for src, _ in jobs:
        by_dir[src.parent] = by_dir.get(src.parent, 0) + 1
        total_bytes += src.stat().st_size

    print(f"{'DRY RUN — ' if dry else ''}{len(jobs)} files "
          f"({total_bytes / 1e6:.1f} MB) into {len(by_dir)} '{STAMP}/' folders\n")
    for d in sorted(by_dir):
        print(f"  {by_dir[d]:>4}  {d.relative_to(REPO)}")

    if dry:
        print("\nNothing written.")
        return 0

    copied = skipped = 0
    for src, dst in jobs:
        if dst.exists() and dst.stat().st_size == src.stat().st_size:
            skipped += 1
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        copied += 1

    print(f"\ncopied {copied}, already-backed-up {skipped}")

    missing = [dst for _, dst in jobs if not dst.exists()]
    if missing:
        print(f"[FAIL] {len(missing)} destinations missing after copy", file=sys.stderr)
        return 1
    print("verified: every source has a backup copy")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

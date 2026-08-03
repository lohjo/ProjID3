"""Cross-check in-text citations against the report's reference list.

Implements the mechanical half of ARS Stage 2.5 Phase A3 (ghost-citation check):

  dangling  -- cited in the body, absent from the reference list
  orphaned  -- listed in the references, never cited in the body
  year-clash -- same first author cited under a year the list does not carry

Verification that a *listed* reference actually exists in the literature is a
separate, non-mechanical step (Phase A1/A2) and is not done here.

Usage:  python citation_crosscheck.py
"""

from __future__ import annotations

import re
import unicodedata
from collections import defaultdict
from pathlib import Path

from extract_report import DOCX, load_body, paragraphs

# The reference list starts at the "10References" heading; everything at or
# after it is a bibliography entry rather than prose.
REF_HEADING = re.compile(r"^\s*10\s*References\s*$", re.I)

# "Author, A. B., & Other, C. (2024). Title..." -> first surname + year.
# The second branch catches organisational authors ("International Energy
# Agency. (2022)."), which carry no comma before the year.
REF_ENTRY = re.compile(
    r"^([^,(]+?),\s*[^(]*?\((\d{4}[a-z]?|n\.d\.)\)"
    r"|^([A-Z][^.(]{3,60})\.\s*\((\d{4}[a-z]?|n\.d\.)\)"
)

# Surname particles are written inconsistently between the list ("de Joannis")
# and the body ("de Joannis, 2025", which the in-text regex clips to "Joannis").
# Strip them on both sides so the same source does not appear as two findings.
PARTICLES = ("de", "del", "della", "van", "von", "der", "den", "la", "le", "di", "da")

# In-text forms: "(Smith et al., 2020)" / "Smith et al. (2020)" / "(Smith & Lee, 2020)"
PAREN_GROUP = re.compile(r"\(([^()]{3,200}?)\)")
NARRATIVE = re.compile(
    r"\b([A-Z][A-Za-zÀ-ɏ'’-]+(?:\s+et\s+al\.)?(?:\s*&\s*[A-Z][A-Za-zÀ-ɏ'’-]+)?)"
    r"\s*\((\d{4}[a-z]?|n\.d\.)\)"
)
INNER = re.compile(
    r"([A-Z][A-Za-zÀ-ɏ'’-]+(?:\s+et\s+al\.)?(?:\s*(?:&|and)\s*[A-Z][A-Za-zÀ-ɏ'’-]+)?)"
    r"[,\s]+(\d{4}[a-z]?|n\.d\.)"
)

# Not citations: statute numbers, student IDs, equation refs, bare years.
NOISE = re.compile(r"^(?:Fig|Table|Eq|Section|§|Appendix)\b", re.I)


def norm(name: str) -> str:
    """Fold to a comparable surname key: strip accents, initials, 'et al.'."""
    name = unicodedata.normalize("NFKD", name)
    name = "".join(c for c in name if not unicodedata.combining(c))
    name = re.sub(r"\bet\s+al\.?", "", name, flags=re.I)
    name = re.sub(r"\s*(?:&|and)\s*.*$", "", name)  # keep only first author
    name = re.sub(r"^[A-Z]\.\s*", "", name)  # drop leading initial
    name = name.strip()
    for particle in PARTICLES:
        name = re.sub(rf"^{particle}\s+", "", name, flags=re.I)
    name = re.sub(r"[^A-Za-z-]", "", name)
    return name.lower().strip("-")


def split_refs(rows):
    for i, _style, text in rows:
        if REF_HEADING.match(text):
            return i
    raise SystemExit("could not locate the References heading")


def main() -> None:
    rows = paragraphs(load_body(DOCX))
    cut = split_refs(rows)

    # --- reference list -------------------------------------------------
    refs: dict[str, set[str]] = defaultdict(set)
    ref_lines: dict[tuple[str, str], tuple[int, str]] = {}
    for i, _style, text in rows[cut:]:
        m = REF_ENTRY.match(text)
        if not m:
            continue
        key = norm(m.group(1) or m.group(3))
        year = m.group(2) or m.group(4)
        refs[key].add(year)
        ref_lines[(key, year)] = (i, text[:95])

    # --- in-text citations ----------------------------------------------
    cites: dict[tuple[str, str], list[int]] = defaultdict(list)
    for i, _style, text in rows[:cut]:
        for m in NARRATIVE.finditer(text):
            if NOISE.match(m.group(1)):
                continue
            cites[(norm(m.group(1)), m.group(2))].append(i)
        for grp in PAREN_GROUP.finditer(text):
            for m in INNER.finditer(grp.group(1)):
                if NOISE.match(m.group(1)):
                    continue
                cites[(norm(m.group(1)), m.group(2))].append(i)

    cited_keys = {k for k, _ in cites}
    listed_keys = set(refs)

    dangling, yearclash, ok = [], [], []
    for (key, year), paras in sorted(cites.items(), key=lambda kv: kv[1][0]):
        if not key:
            continue
        if key not in refs:
            dangling.append((key, year, paras))
        elif year not in refs[key]:
            yearclash.append((key, year, sorted(refs[key]), paras))
        else:
            ok.append((key, year, paras))

    orphaned = sorted(listed_keys - cited_keys)

    def loc(paras):
        head = ", ".join(f"p{p}" for p in sorted(set(paras))[:6])
        return head + (" …" if len(set(paras)) > 6 else "")

    print(f"reference-list entries : {sum(len(v) for v in refs.values())}")
    print(f"distinct in-text cites : {len(cites)}")
    print()

    print(f"## DANGLING — cited in text, absent from reference list ({len(dangling)})")
    for key, year, paras in dangling:
        print(f"  {key:22s} {year:6s}  {len(paras):2d}x  {loc(paras)}")

    print(f"\n## YEAR CLASH — author listed under a different year ({len(yearclash)})")
    for key, year, have, paras in yearclash:
        print(f"  {key:22s} cited {year:6s} but list has {have}  {loc(paras)}")

    print(f"\n## ORPHANED — in reference list, never cited ({len(orphaned)})")
    for key in orphaned:
        for year in sorted(refs[key]):
            _, txt = ref_lines[(key, year)]
            print(f"  {key:22s} {year:6s}  {txt}")

    print(f"\n## RESOLVED cleanly ({len(ok)})")
    for key, year, paras in ok:
        print(f"  {key:22s} {year:6s}  {len(paras):2d}x  {loc(paras)}")


if __name__ == "__main__":
    main()

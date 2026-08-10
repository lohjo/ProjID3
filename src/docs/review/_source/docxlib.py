"""Reusable helpers for in-place editing of T32_PI05_Final_Report.docx.

Works directly on the lxml tree that python-docx exposes (doc.element.body),
so it can do things python-docx's high-level API can't: reorder whole
sections, edit text that Word split across multiple runs, clone paragraph
styles for new content, etc.
"""
from __future__ import annotations

import copy
import re

import docx
from docx.oxml.ns import qn

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}


def load(path):
    return docx.Document(path)


def save(doc, path):
    doc.save(path)


def body_children(doc):
    """List of (index, element) for every direct child of <w:body>."""
    return list(enumerate(doc.element.body.iterchildren()))


def ptext(el) -> str:
    """All visible text under an element (paragraph or run container)."""
    return "".join(t.text or "" for t in el.findall(".//w:t", NS))


def is_heading(el, level=None) -> bool | str:
    if el.tag != qn("w:p"):
        return False
    pStyle = el.find(".//w:pStyle", NS)
    if pStyle is None:
        return False
    val = pStyle.get(qn("w:val"))
    if val is None or "Heading" not in val:
        return False
    if level is not None:
        return val == f"Heading{level}"
    return val


def find_heading(doc, text_contains, level=None, start=0):
    """Return (index, element) of the first heading paragraph whose text
    contains `text_contains`. Raises if not found."""
    for i, el in body_children(doc):
        if i < start:
            continue
        if is_heading(el, level) and text_contains in ptext(el):
            return i, el
    raise ValueError(f"heading not found: {text_contains!r} (level={level})")


def find_paragraph(doc, text_contains, start=0, unique=True):
    """Return list of (index, element) of ALL body-level <w:p> whose text
    contains text_contains. If unique, assert exactly one match and return
    just that (index, element) pair."""
    hits = []
    for i, el in body_children(doc):
        if i < start:
            continue
        if el.tag == qn("w:p") and text_contains in ptext(el):
            hits.append((i, el))
    if unique:
        if len(hits) != 1:
            raise ValueError(
                f"expected exactly 1 match for {text_contains!r}, got {len(hits)}"
            )
        return hits[0]
    return hits


def all_runs(el):
    """All <w:r> descendants of el, in document order (paragraph or
    heading), INCLUDING runs nested in hyperlinks."""
    return el.findall(".//w:r", NS)


def replace_text(el, old: str, new: str, occurrence: int = 1) -> bool:
    """Replace the `occurrence`-th (1-based) occurrence of `old` with `new`
    inside el's visible text, across run boundaries if necessary. The
    formatting of the first run touched is kept; any other runs fully
    inside the matched span have their text cleared (not deleted, so
    nothing else about the run -- comments, bookmarks -- breaks).

    Returns True if a replacement was made.
    """
    runs = all_runs(el)
    # (run, w:t element, text, start_offset_in_full_text)
    pieces = []
    full = []
    pos = 0
    for r in runs:
        t = r.find("w:t", NS)
        if t is None or t.text is None:
            continue
        pieces.append((r, t, pos))
        full.append(t.text)
        pos += len(t.text)
    full_text = "".join(full)

    start = -1
    idx = 0
    for _ in range(occurrence):
        start = full_text.find(old, idx)
        if start == -1:
            return False
        idx = start + 1
    end = start + len(old)

    # find runs touched
    touched = [
        (r, t, off) for (r, t, off) in pieces if off < end and off + len(t.text) > start
    ]
    if not touched:
        return False

    first_r, first_t, first_off = touched[0]
    # text before match within first run + new text + text after match within last run
    last_r, last_t, last_off = touched[-1]
    before = first_t.text[: max(0, start - first_off)]
    after = last_t.text[max(0, end - last_off):]

    first_t.text = before + new + (after if first_t is last_t else "")
    if first_t is not last_t:
        last_t.text = after
        for r, t, off in touched[1:-1]:
            t.text = ""
    return True


def replace_text_all(el, old: str, new: str) -> int:
    """Replace every non-overlapping occurrence of `old`. Returns count."""
    n = 0
    while replace_text(el, old, new, occurrence=1):
        n += 1
    return n


def set_heading_number(doc, old_full_text, new_number, level=None):
    """For a heading whose visible text is e.g. '3.4 Adsorption breakthrough
    models', replace the leading number token ('3.4') with new_number,
    matched by the *rest* of the text after the number (so it's robust to
    where Word split the runs)."""
    i, el = find_heading(doc, old_full_text, level=level)
    m = re.match(r"^(\S+)(\s+.*)$", old_full_text)
    if not m:
        raise ValueError(f"can't parse heading text {old_full_text!r}")
    old_num = m.group(1)
    ok = replace_text(el, old_num, new_number, occurrence=1)
    if not ok:
        raise ValueError(f"couldn't replace {old_num!r} in heading {old_full_text!r}")
    return i, el


def clone_paragraph_after(ref_el, text=None, style=None):
    """Clone ref_el (a <w:p>) as a new empty-ish paragraph inserted right
    after it, optionally overwriting its style and single-run text. Returns
    the new element. Strips bookmarks/comments from the clone so IDs don't
    collide."""
    new_el = copy.deepcopy(ref_el)
    for tag in ("bookmarkStart", "bookmarkEnd", "commentRangeStart",
                "commentRangeEnd", "commentReference"):
        for e in new_el.findall(f".//w:{tag}", NS):
            e.getparent().remove(e)
    if style is not None:
        pPr = new_el.find("w:pPr", NS)
        if pPr is None:
            pPr = new_el.makeelement(qn("w:pPr"), {})
            new_el.insert(0, pPr)
        pStyle = pPr.find("w:pStyle", NS)
        if pStyle is None:
            pStyle = pPr.makeelement(qn("w:pStyle"), {})
            pPr.insert(0, pStyle)
        pStyle.set(qn("w:val"), style)
    if text is not None:
        runs = new_el.findall("w:r", NS)
        if runs:
            first = runs[0]
            t = first.find("w:t", NS)
            if t is None:
                t = first.makeelement(qn("w:t"), {})
                first.append(t)
            t.text = text
            t.set(qn("xml:space"), "preserve")
            for extra in runs[1:]:
                new_el.remove(extra)
        else:
            r = new_el.makeelement(qn("w:r"), {})
            t = r.makeelement(qn("w:t"), {})
            t.text = text
            t.set(qn("xml:space"), "preserve")
            r.append(t)
            new_el.append(r)
    ref_el.addnext(new_el)
    return new_el


def move_block(doc, start_i, end_i, insert_before_i):
    """Move body children [start_i, end_i] (inclusive, 0-based indices as of
    the CURRENT tree state) to just before the child currently at
    insert_before_i. All indices are re-read fresh each call, since this
    mutates the tree; call this once per move and re-derive indices between
    calls."""
    body = doc.element.body
    children = list(body.iterchildren())
    block = children[start_i : end_i + 1]
    anchor = children[insert_before_i]
    assert anchor not in block, "insertion point must be outside the moved block"
    for el in block:
        body.remove(el)
    for el in reversed(block):
        anchor.addprevious(el)


def para_index_of(doc, el):
    for i, e in body_children(doc):
        if e is el:
            return i
    raise ValueError("element not in body")

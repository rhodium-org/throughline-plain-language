#!/usr/bin/env python3
"""Generate the plain-language throughline source from tools/plain_language_data.py.

The graph is a single-root axis: one `intent`, eight `user_requirement` principles that
`derives_from` it, and thirty `system_requirement` rules that each `implements` a
principle. `docs/spec.md` is regenerated with blanked `tl:*` markers, so `tl docs` MUST
run after this script (CI's `tl docs --check` enforces it).

This source is ORIGINAL content, not a re-expression of a published standard, which
changes two things relative to a clause-derived source such as throughline-asvs:

* **Titles are authored, never derived.** There is no external clause text to distil a
  label from, so `title` sits beside `text` in the data module as authored content.
  throughline-source-quality REQ-0001 governs *mechanical* derivation and so does not
  bite here — but its substance does, and `_assert_sound` below enforces it directly:
  a title must be a complete statement, so an ellipsis-truncated or fragmentary title
  fails the build rather than reaching the graph. That check exists because exactly such
  titles did reach it once, from a generator that capped labels at 80 characters.
* **UIDs are authored data.** The usual `source_ref -> UID` scan cannot key items here,
  because a `source_ref` names the *governing principle* (e.g. ISO 24495-1:2023
  Principle 3) and eighteen rules legitimately share one. The UID therefore lives in the
  data module and is permanent by construction (REQ-0004); `source_ref` stays an
  attribute (REQ-0007).

Usage:  python tools/generate.py
"""
from __future__ import annotations

import re
from pathlib import Path

import yaml

# Run as `python tools/generate.py`: Python puts this script's directory on sys.path,
# so the sibling data module imports without any path juggling.
from plain_language_data import INTENT, PRINCIPLES, RULES

REPO = Path(__file__).resolve().parent.parent
INTENT_DIR = REPO / "intents"        # intent, prefix INT
PRINCIPLE_DIR = REPO / "principles"  # user_requirement, prefix UR
RULE_DIR = REPO / "requirements"     # system_requirement, prefix SR
SPEC = REPO / "docs" / "spec.md"


class _Quoted(str):
    """A string the dumper renders in single quotes, matching the graph's house style."""


class _Dumper(yaml.SafeDumper):
    pass


_Dumper.add_representer(
    _Quoted,
    lambda d, x: d.represent_scalar("tag:yaml.org,2002:str", str(x), style="'"),
)

_QUOTE_FIELDS = {"title", "text", "source_ref"}


def _style(obj, key=None):
    """Mark prose fields for quoted output; leave keys, enums and UIDs bare."""
    if isinstance(obj, dict):
        return {k: _style(v, k) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_style(v) for v in obj]
    if isinstance(obj, str) and key in _QUOTE_FIELDS:
        return _Quoted(obj)
    return obj


def _dump(path: Path, item: dict) -> None:
    path.write_text(
        # width is effectively unlimited: prose stays on one line, so a text edit shows
        # as a one-line diff rather than reflowing the whole paragraph.
        yaml.dump(_style(item), Dumper=_Dumper, sort_keys=False,
                  allow_unicode=True, width=10 ** 9),
        encoding="utf-8",
    )


_FRAGMENT = re.compile(r"(\.\.\.|\u2026)$")


def _assert_sound(kind: str, entry: dict) -> None:
    """Refuse to emit an item whose title is not a complete, self-contained statement.

    Enforces the substance of throughline-source-quality REQ-0001 at the point of
    generation. Fails the run rather than writing a defective item, because a title that
    reaches the graph is published, composed and cited by consumers this source cannot see.
    """
    uid, title = entry["uid"], entry["title"]
    problems = []
    if _FRAGMENT.search(title):
        problems.append("ends in an ellipsis — it is a truncation, not a statement")
    if title.count("(") != title.count(")"):
        problems.append("has unbalanced parentheses, so it was cut mid-clause")
    if title.count('"') % 2:
        problems.append("has an unclosed quotation mark")
    if title.rstrip().endswith((",", ";", ":")):
        problems.append("ends on punctuation that continues a sentence")
    if len(title.split()) < 2:
        problems.append("is a single word, which cannot identify a rule")
    if problems:
        raise SystemExit(
            f"{kind} {uid}: title is not a complete statement — "
            + "; ".join(problems)
            + f"\n  title: {title!r}\n"
            "Fix the title in tools/plain_language_data.py; do not truncate it."
        )


SPEC_HEADER = """\
# Plain Language — throughline source

This document is **generated from the graph** by `tl docs`; `tl docs --check` gates
it in CI. The prose headings are hand-owned — everything between `tl:*` markers is
injected from the YAML items, so the published spec can never drift from the graph.

This source is the **readability / plain-language axis** only: one orthogonal
content dimension. It says nothing about spelling variant, punctuation, tone, genre,
medium or brand voice — each of those is its own throughline source, so a consumer
composes exactly the axes a task needs. Every principle is a `user_requirement`;
every rule is a `system_requirement` that `implements` its principle. The throughline
UIDs are this source's own and immutable — a consumer cites a rule as `plain:SR-0007`,
never by the ISO 24495-1:2023 principle, which lives in `attrs.source_ref`.

It carries
<!-- tl:count type == 'user_requirement' -->
<!-- tl:end --> principles and
<!-- tl:count type == 'system_requirement' -->
<!-- tl:end --> rules.

## Purpose

<!-- tl:item INT-0001 -->
<!-- tl:end -->
"""


def generate_spec() -> None:
    """Write docs/spec.md: the hand-owned header, then per principle in document order a
    tl:item block for the principle and a tl:table of the rules that implement it.
    `tl docs` injects the live content into the blanked markers."""
    parts = [SPEC_HEADER]
    for n, p in enumerate(PRINCIPLES, start=1):
        parts.append(f"## {n}. {p['title']}\n")
        parts.append(f"<!-- tl:item {p['uid']} -->\n<!-- tl:end -->\n")
        parts.append(
            f"<!-- tl:table attrs.get('principle') == '{p['uid']}' -->\n<!-- tl:end -->\n"
        )
    # Each part already ends in a newline; the join supplies the blank line between
    # blocks. Trim so the file ends with exactly one newline, not two.
    SPEC.write_text("\n".join(parts).rstrip("\n") + "\n", encoding="utf-8")


def main() -> int:
    _assert_sound("intent", INTENT)
    for p in PRINCIPLES:
        _assert_sound("principle", p)
    for r in RULES:
        _assert_sound("rule", r)

    known = {p["uid"] for p in PRINCIPLES}
    for r in RULES:
        if r["principle"] not in known:
            raise SystemExit(f"rule {r['uid']} implements unknown principle {r['principle']}")

    _dump(INTENT_DIR / f"{INTENT['uid']}.yml", {
        "uid": INTENT["uid"],
        "type": "intent",
        "status": "approved",
        "title": INTENT["title"],
        "text": INTENT["text"],
        "normative": False,
        "attrs": {"source_ref": INTENT["source_ref"]},
    })

    for p in PRINCIPLES:
        _dump(PRINCIPLE_DIR / f"{p['uid']}.yml", {
            "uid": p["uid"],
            "type": "user_requirement",
            "status": "approved",
            "title": p["title"],
            "text": p["text"],
            "links": [{"target": INTENT["uid"], "type": "derives_from"}],
            "attrs": {"source_ref": p["source_ref"]},
        })

    for r in RULES:
        _dump(RULE_DIR / f"{r['uid']}.yml", {
            "uid": r["uid"],
            "type": "system_requirement",
            "status": "approved",
            "title": r["title"],
            "text": r["text"],
            "links": [{"target": r["principle"], "type": "implements"}],
            "attrs": {"source_ref": r["source_ref"], "principle": r["principle"]},
        })

    generate_spec()
    print("intent:     1 item written")
    print(f"principles: {len(PRINCIPLES)} items written")
    print(f"rules:      {len(RULES)} items written")
    print(f"spec:       {SPEC} regenerated — run `tl docs` to inject content")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

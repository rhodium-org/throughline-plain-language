#!/usr/bin/env python3
"""Generate the plain-language throughline source from the curated table below.

The content is a faithful re-expression of the U.S. Federal Plain Language
Guidelines (plainlanguage.gov, PLAIN, March 2011 rev.1) — a work of the U.S.
federal government, in the public domain. This script owns the UID<->guideline
mapping; re-running it is idempotent and preserves every existing UID because the
UIDs are assigned positionally from this table. To extend the source, append to
the table (never reorder or delete rows) so existing UIDs stay stable.

Run from the repo root:  python tools/generate_plain_language.py
Then:                    tl check --strict && tl docs
"""
from __future__ import annotations
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

# ---- the root intent -------------------------------------------------------
INTENT = dict(
    uid="INT-0001",
    title="A reader understands the content correctly on first reading",
    text=(
        "Plain language exists so that the intended reader can find what they "
        "need, understand it, and act on it the first time they read it — whatever "
        "their expertise. Writing that fails this test raises error rates, support "
        "costs and exclusion; writing that meets it is faster and fairer for "
        "everyone. This axis governs readability alone, not spelling, tone or medium."
    ),
    source_ref="PLAIN — Federal Plain Language Guidelines (2011)",
)

# ---- principles (user_requirements) and their rules (system_requirements) --
# Each principle: (title, text, source_ref, [rules]); each rule: (text, source_ref).
# Titles for rules are derived from their text. Order is load-bearing: it fixes UIDs.
PRINCIPLES = [
    (
        "Write for your reader",
        "Decide who the reader is and what they need before drafting, then write for them.",
        "PLAIN I — Think about your audience",
        [
            ("Identify the primary audience and their reading context before you start drafting.",
             "PLAIN I.a"),
            ("State the reader's task and the single action you want them to take.",
             "PLAIN I.b"),
            ('Address the reader directly as "you"; refer to your organisation as "we".',
             "PLAIN III — Pronouns"),
        ],
    ),
    (
        "Organise so the reader finds what matters first",
        "Structure the content around the reader's needs, leading with what matters most.",
        "PLAIN II — Organize",
        [
            ("Lead with the most important information, then the detail (the inverted pyramid).",
             "PLAIN II.a"),
            ("Group related material under informative, task-based headings.",
             "PLAIN II.b"),
            ("Present information in the order the reader will need it, answering likely questions in turn.",
             "PLAIN II.c"),
        ],
    ),
    (
        "Choose familiar, concrete words",
        "Prefer the plainest word that carries the meaning, and keep terms consistent.",
        "PLAIN III — Word choice",
        [
            ("Use the most common word that carries the meaning; avoid jargon and legalese.",
             "PLAIN III.a"),
            ("Define any unavoidable technical term at its first use.",
             "PLAIN III.b"),
            ("Spell out an abbreviation at first use, with the short form in brackets after it.",
             "PLAIN III.c"),
            ("Avoid Latin and foreign phrases; use an everyday English equivalent instead.",
             "PLAIN III.d"),
            ("Use the same word for the same thing throughout; do not vary it for elegance.",
             "PLAIN III.e"),
        ],
    ),
    (
        "Prefer active voice and strong verbs",
        "Put the actor first and let precise verbs carry the sentence.",
        "PLAIN IV — Verbs",
        [
            ("Write in the active voice unless the actor is unknown or irrelevant.",
             "PLAIN IV.a"),
            ("Use the strongest, most precise verb available.",
             "PLAIN IV.b"),
            ('Avoid hidden verbs — write "decide", not "make a decision".',
             "PLAIN IV.c"),
            ('Use "must" to state an obligation; avoid "shall".',
             "PLAIN IV.d"),
            ("Use the present tense wherever the meaning allows.",
             "PLAIN IV.e"),
        ],
    ),
    (
        "Keep sentences and paragraphs short",
        "Carry one idea at a time so the reader never has to re-read.",
        "PLAIN V — Sentences and paragraphs",
        [
            ("Express one main idea per sentence.",
             "PLAIN V.a"),
            ("Keep the subject, verb and object close together.",
             "PLAIN V.b"),
            ("Avoid double negatives and exceptions to exceptions.",
             "PLAIN V.c"),
            ("Keep each paragraph to a single topic, opened by a topic sentence.",
             "PLAIN V.d"),
        ],
    ),
    (
        "Be concise",
        "Cut every word that carries no meaning.",
        "PLAIN VI — Conciseness",
        [
            ('Delete words that add no meaning — write "to", not "in order to".',
             "PLAIN VI.a"),
            ('Remove redundant pairs such as "each and every".',
             "PLAIN VI.b"),
            ('Cut intensifiers that add no information, such as "very" and "really".',
             "PLAIN VI.c"),
            ('Replace a wordy phrase with one word — "because", not "due to the fact that".',
             "PLAIN VI.d"),
        ],
    ),
    (
        "Design pages so they can be scanned",
        "Lay out content so a reader can skim to the part they need.",
        "PLAIN VII — Design and readability",
        [
            ("Break content with headings and subheadings that describe what follows.",
             "PLAIN VII.a"),
            ("Use a bulleted or numbered list for a series of items or steps.",
             "PLAIN VII.b"),
            ("Use a table to present conditional or comparative information.",
             "PLAIN VII.c"),
            ("Use short line lengths and generous whitespace so text can be scanned.",
             "PLAIN VII.d"),
        ],
    ),
    (
        "Test that real readers understand",
        "Treat comprehension as measurable and verify it.",
        "PLAIN VIII — Test",
        [
            ("Set a readability target appropriate to the audience and check the draft against it.",
             "PLAIN VIII.a"),
            ("Test drafts with people from the target audience and revise on what confuses them.",
             "PLAIN VIII.b"),
        ],
    ),
]


def scalar(s: str) -> str:
    """Emit a YAML single-quoted scalar (doubling any internal single quote)."""
    return "'" + s.replace("'", "''") + "'"


def title_from(text: str) -> str:
    """A short title: first clause of the rule text, capped."""
    head = text.split(" — ")[0].split(";")[0].rstrip(".")
    return head if len(head) <= 80 else head[:77].rstrip() + "..."


def write_register(folder: str, prefix: str, title: str) -> None:
    d = ROOT / folder
    d.mkdir(exist_ok=True)
    (d / ".register.yml").write_text(
        f"prefix: {prefix}\ndigits: 4\ntitle: {title}\n"
    )


def write_item(folder: str, lines: list[str]) -> None:
    uid = next(l.split("uid: ")[1] for l in lines if l.startswith("uid: "))
    (ROOT / folder / f"{uid}.yml").write_text("\n".join(lines) + "\n")


def main() -> None:
    write_register("intents", "INT", "Purpose")
    write_register("principles", "UR", "Plain-language principles")
    write_register("requirements", "SR", "Plain-language rules")

    # intent
    write_item("intents", [
        f"uid: {INTENT['uid']}",
        "type: intent",
        "status: approved",
        f"title: {scalar(INTENT['title'])}",
        f"text: {scalar(INTENT['text'])}",
        "normative: false",
        "attrs:",
        f"  source_ref: {scalar(INTENT['source_ref'])}",
    ])

    sr = 0
    for i, (ptitle, ptext, psrc, rules) in enumerate(PRINCIPLES, start=1):
        ur = f"UR-{i:04d}"
        write_item("principles", [
            f"uid: {ur}",
            "type: user_requirement",
            "status: approved",
            f"title: {scalar(ptitle)}",
            f"text: {scalar(ptext)}",
            "links:",
            f"- target: {INTENT['uid']}",
            "  type: derives_from",
            "attrs:",
            f"  source_ref: {scalar(psrc)}",
        ])
        for rtext, rsrc in rules:
            # attrs.principle mirrors the implements target purely as a docs
            # grouping key: tl:table filters allow method calls on values but
            # cannot traverse links, so the doc groups rules by this attr.
            sr += 1
            write_item("requirements", [
                f"uid: SR-{sr:04d}",
                "type: system_requirement",
                "status: approved",
                f"title: {scalar(title_from(rtext))}",
                f"text: {scalar(rtext)}",
                "links:",
                f"- target: {ur}",
                "  type: implements",
                "attrs:",
                f"  source_ref: {scalar(rsrc)}",
                f"  principle: {ur}",
            ])

    print(f"wrote 1 intent, {len(PRINCIPLES)} principles, {sr} rules")


if __name__ == "__main__":
    main()

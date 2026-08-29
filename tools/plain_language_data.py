"""Plain-language source content, authored for the throughline source generator.

This is original guidance by Dr Henry J Grech-Cini, informed by the international consensus
on plain language — principally ISO 24495-1:2023 and the International Plain Language
Federation's definition. Those standards are *referenced*, never reproduced: each item's
`source_ref` names the governing principle it elaborates, and no ISO text is copied here.

Titles are authored, not derived. Because the content is original rather than a
re-expression of published clauses, there is no clause text to distil a label from, so
each rule carries a hand-written title alongside its text and
throughline-source-quality REQ-0001 (mechanical derivation must yield a complete
statement) simply does not arise. A title must still be a complete statement.

`uid` is part of the authored data and is permanent (REQ-0004). It is stated here
rather than derived from `source_ref` because a source_ref names the *governing
principle*, which many rules legitimately share, so it cannot key an item.
"""

INTENT = {
    "uid": 'INT-0001',
    "title": 'A reader understands the content correctly on first reading',
    "text": (
        'Plain language exists so that the intended reader can find what they need, '
        'understand it, and act on it the first time they read it — whatever their expertise.'
        ' Writing that fails this test raises error rates, support costs and exclusion; '
        'writing that meets it is faster and fairer for everyone. This axis governs '
        'readability alone, not spelling, tone or medium.'
    ),
    "source_ref": 'ISO 24495-1:2023 — Plain language, Part 1: Governing principles and guidelines',
}

PRINCIPLES = [
    {
        "uid": 'UR-0001',
        "source_ref": 'ISO 24495-1:2023 — Principle 1 (Relevant)',
        "title": 'Write for your reader',
        "text": 'Decide who the reader is and what they need before drafting, then write for them.',
    },
    {
        "uid": 'UR-0002',
        "source_ref": 'ISO 24495-1:2023 — Principle 2 (Findable)',
        "title": 'Organise so the reader finds what matters first',
        "text": "Structure the content around the reader's needs, leading with what matters most.",
    },
    {
        "uid": 'UR-0003',
        "source_ref": 'ISO 24495-1:2023 — Principle 3 (Understandable)',
        "title": 'Choose familiar, concrete words',
        "text": 'Prefer the plainest word that carries the meaning, and keep terms consistent.',
    },
    {
        "uid": 'UR-0004',
        "source_ref": 'ISO 24495-1:2023 — Principle 3 (Understandable)',
        "title": 'Prefer active voice and strong verbs',
        "text": 'Put the actor first and let precise verbs carry the sentence.',
    },
    {
        "uid": 'UR-0005',
        "source_ref": 'ISO 24495-1:2023 — Principle 3 (Understandable)',
        "title": 'Keep sentences and paragraphs short',
        "text": 'Carry one idea at a time so the reader never has to re-read.',
    },
    {
        "uid": 'UR-0006',
        "source_ref": 'ISO 24495-1:2023 — Principle 3 (Understandable)',
        "title": 'Be concise',
        "text": 'Cut every word that carries no meaning.',
    },
    {
        "uid": 'UR-0007',
        "source_ref": 'ISO 24495-1:2023 — Principle 2 (Findable)',
        "title": 'Design pages so they can be scanned',
        "text": 'Lay out content so a reader can skim to the part they need.',
    },
    {
        "uid": 'UR-0008',
        "source_ref": 'ISO 24495-1:2023 — Principle 4 (Usable)',
        "title": 'Test that real readers understand',
        "text": 'Treat comprehension as measurable and verify it.',
    },
]

RULES = [
    {
        "uid": 'SR-0001',
        "principle": 'UR-0001',
        "source_ref": 'ISO 24495-1:2023 — Principle 1 (Relevant)',
        "title": 'Identify the primary audience and their reading context before you start drafting',
        "text": 'Identify the primary audience and their reading context before you start drafting.',
    },
    {
        "uid": 'SR-0002',
        "principle": 'UR-0001',
        "source_ref": 'ISO 24495-1:2023 — Principle 1 (Relevant)',
        "title": "State the reader's task and the single action you want them to take",
        "text": "State the reader's task and the single action you want them to take.",
    },
    {
        "uid": 'SR-0003',
        "principle": 'UR-0001',
        "source_ref": 'ISO 24495-1:2023 — Principle 1 (Relevant)',
        "title": 'Address the reader directly as "you"',
        "text": 'Address the reader directly as "you"; refer to your organisation as "we".',
    },
    {
        "uid": 'SR-0004',
        "principle": 'UR-0002',
        "source_ref": 'ISO 24495-1:2023 — Principle 2 (Findable)',
        "title": 'Lead with the most important information, then the detail (the inverted pyramid)',
        "text": 'Lead with the most important information, then the detail (the inverted pyramid).',
    },
    {
        "uid": 'SR-0005',
        "principle": 'UR-0002',
        "source_ref": 'ISO 24495-1:2023 — Principle 2 (Findable)',
        "title": 'Group related material under informative, task-based headings',
        "text": 'Group related material under informative, task-based headings.',
    },
    {
        "uid": 'SR-0006',
        "principle": 'UR-0002',
        "source_ref": 'ISO 24495-1:2023 — Principle 2 (Findable)',
        "title": 'Present information in the order the reader will need it, answering likely questions in turn',
        "text": (
            'Present information in the order the reader will need it, answering likely '
            'questions in turn.'
        ),
    },
    {
        "uid": 'SR-0007',
        "principle": 'UR-0003',
        "source_ref": 'ISO 24495-1:2023 — Principle 3 (Understandable)',
        "title": 'Use the most common word that carries the meaning',
        "text": 'Use the most common word that carries the meaning; avoid jargon and legalese.',
    },
    {
        "uid": 'SR-0008',
        "principle": 'UR-0003',
        "source_ref": 'ISO 24495-1:2023 — Principle 3 (Understandable)',
        "title": 'Define any unavoidable technical term at its first use',
        "text": 'Define any unavoidable technical term at its first use.',
    },
    {
        "uid": 'SR-0009',
        "principle": 'UR-0003',
        "source_ref": 'ISO 24495-1:2023 — Principle 3 (Understandable)',
        "title": 'Spell out an abbreviation at first use, with the short form in brackets after it',
        "text": 'Spell out an abbreviation at first use, with the short form in brackets after it.',
    },
    {
        "uid": 'SR-0010',
        "principle": 'UR-0003',
        "source_ref": 'ISO 24495-1:2023 — Principle 3 (Understandable)',
        "title": 'Avoid Latin and foreign phrases',
        "text": 'Avoid Latin and foreign phrases; use an everyday English equivalent instead.',
    },
    {
        "uid": 'SR-0011',
        "principle": 'UR-0003',
        "source_ref": 'ISO 24495-1:2023 — Principle 3 (Understandable)',
        "title": 'Use the same word for the same thing throughout',
        "text": 'Use the same word for the same thing throughout; do not vary it for elegance.',
    },
    {
        "uid": 'SR-0012',
        "principle": 'UR-0004',
        "source_ref": 'ISO 24495-1:2023 — Principle 3 (Understandable)',
        "title": 'Write in the active voice unless the actor is unknown or irrelevant',
        "text": 'Write in the active voice unless the actor is unknown or irrelevant.',
    },
    {
        "uid": 'SR-0013',
        "principle": 'UR-0004',
        "source_ref": 'ISO 24495-1:2023 — Principle 3 (Understandable)',
        "title": 'Use the strongest, most precise verb available',
        "text": 'Use the strongest, most precise verb available.',
    },
    {
        "uid": 'SR-0014',
        "principle": 'UR-0004',
        "source_ref": 'ISO 24495-1:2023 — Principle 3 (Understandable)',
        "title": 'Avoid hidden verbs',
        "text": 'Avoid hidden verbs — write "decide", not "make a decision".',
    },
    {
        "uid": 'SR-0015',
        "principle": 'UR-0004',
        "source_ref": 'ISO 24495-1:2023 — Principle 3 (Understandable)',
        "title": 'Use "must" to state an obligation',
        "text": 'Use "must" to state an obligation; avoid "shall".',
    },
    {
        "uid": 'SR-0016',
        "principle": 'UR-0004',
        "source_ref": 'ISO 24495-1:2023 — Principle 3 (Understandable)',
        "title": 'Use the present tense wherever the meaning allows',
        "text": 'Use the present tense wherever the meaning allows.',
    },
    {
        "uid": 'SR-0017',
        "principle": 'UR-0005',
        "source_ref": 'ISO 24495-1:2023 — Principle 3 (Understandable)',
        "title": 'Express one main idea per sentence',
        "text": 'Express one main idea per sentence.',
    },
    {
        "uid": 'SR-0018',
        "principle": 'UR-0005',
        "source_ref": 'ISO 24495-1:2023 — Principle 3 (Understandable)',
        "title": 'Keep the subject, verb and object close together',
        "text": 'Keep the subject, verb and object close together.',
    },
    {
        "uid": 'SR-0019',
        "principle": 'UR-0005',
        "source_ref": 'ISO 24495-1:2023 — Principle 3 (Understandable)',
        "title": 'Avoid double negatives and exceptions to exceptions',
        "text": 'Avoid double negatives and exceptions to exceptions.',
    },
    {
        "uid": 'SR-0020',
        "principle": 'UR-0005',
        "source_ref": 'ISO 24495-1:2023 — Principle 3 (Understandable)',
        "title": 'Keep each paragraph to a single topic, opened by a topic sentence',
        "text": 'Keep each paragraph to a single topic, opened by a topic sentence.',
    },
    {
        "uid": 'SR-0021',
        "principle": 'UR-0006',
        "source_ref": 'ISO 24495-1:2023 — Principle 3 (Understandable)',
        "title": 'Delete words that add no meaning',
        "text": 'Delete words that add no meaning — write "to", not "in order to".',
    },
    {
        "uid": 'SR-0022',
        "principle": 'UR-0006',
        "source_ref": 'ISO 24495-1:2023 — Principle 3 (Understandable)',
        "title": 'Remove redundant pairs such as "each and every"',
        "text": 'Remove redundant pairs such as "each and every".',
    },
    {
        "uid": 'SR-0023',
        "principle": 'UR-0006',
        "source_ref": 'ISO 24495-1:2023 — Principle 3 (Understandable)',
        "title": 'Cut intensifiers that add no information, such as "very" and "really"',
        "text": 'Cut intensifiers that add no information, such as "very" and "really".',
    },
    {
        "uid": 'SR-0024',
        "principle": 'UR-0006',
        "source_ref": 'ISO 24495-1:2023 — Principle 3 (Understandable)',
        "title": 'Replace a wordy phrase with one word',
        "text": 'Replace a wordy phrase with one word — "because", not "due to the fact that".',
    },
    {
        "uid": 'SR-0025',
        "principle": 'UR-0007',
        "source_ref": 'ISO 24495-1:2023 — Principle 2 (Findable)',
        "title": 'Break content with headings and subheadings that describe what follows',
        "text": 'Break content with headings and subheadings that describe what follows.',
    },
    {
        "uid": 'SR-0026',
        "principle": 'UR-0007',
        "source_ref": 'ISO 24495-1:2023 — Principle 2 (Findable)',
        "title": 'Use a bulleted or numbered list for a series of items or steps',
        "text": 'Use a bulleted or numbered list for a series of items or steps.',
    },
    {
        "uid": 'SR-0027',
        "principle": 'UR-0007',
        "source_ref": 'ISO 24495-1:2023 — Principle 2 (Findable)',
        "title": 'Use a table to present conditional or comparative information',
        "text": 'Use a table to present conditional or comparative information.',
    },
    {
        "uid": 'SR-0028',
        "principle": 'UR-0007',
        "source_ref": 'ISO 24495-1:2023 — Principle 2 (Findable)',
        "title": 'Use short line lengths and generous whitespace so text can be scanned',
        "text": 'Use short line lengths and generous whitespace so text can be scanned.',
    },
    {
        "uid": 'SR-0029',
        "principle": 'UR-0008',
        "source_ref": 'ISO 24495-1:2023 — Principle 4 (Usable)',
        "title": 'Set a readability target appropriate to the audience and check the draft against it',
        "text": 'Set a readability target appropriate to the audience and check the draft against it.',
    },
    {
        "uid": 'SR-0030',
        "principle": 'UR-0008',
        "source_ref": 'ISO 24495-1:2023 — Principle 4 (Usable)',
        "title": 'Test drafts with people from the target audience and revise on what confuses them',
        "text": 'Test drafts with people from the target audience and revise on what confuses them.',
    },
]

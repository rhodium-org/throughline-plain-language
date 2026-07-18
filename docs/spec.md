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
8
<!-- tl:end --> principles and
<!-- tl:count type == 'system_requirement' -->
30
<!-- tl:end --> rules.

## Purpose

<!-- tl:item INT-0001 -->
**INT-0001 — A reader understands the content correctly on first reading** — `intent`, status `approved`

> Plain language exists so that the intended reader can find what they need, understand it, and act on it the first time they read it — whatever their expertise. Writing that fails this test raises error rates, support costs and exclusion; writing that meets it is faster and fairer for everyone. This axis governs readability alone, not spelling, tone or medium.

**source_ref**: ISO 24495-1:2023 — Plain language, Part 1: Governing principles and guidelines
<!-- tl:end -->

## 1. Write for your reader

<!-- tl:item UR-0001 -->
**UR-0001 — Write for your reader** — `user_requirement`, status `approved`

> Decide who the reader is and what they need before drafting, then write for them.

*Derives from:* INT-0001

**source_ref**: ISO 24495-1:2023 — Principle 1 (Relevant)
<!-- tl:end -->

<!-- tl:table attrs.get('principle') == 'UR-0001' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0001 | system_requirement | approved | Identify the primary audience and their reading context before you start draf... |
| SR-0002 | system_requirement | approved | State the reader's task and the single action you want them to take |
| SR-0003 | system_requirement | approved | Address the reader directly as "you" |
<!-- tl:end -->

## 2. Organise so the reader finds what matters first

<!-- tl:item UR-0002 -->
**UR-0002 — Organise so the reader finds what matters first** — `user_requirement`, status `approved`

> Structure the content around the reader's needs, leading with what matters most.

*Derives from:* INT-0001

**source_ref**: ISO 24495-1:2023 — Principle 2 (Findable)
<!-- tl:end -->

<!-- tl:table attrs.get('principle') == 'UR-0002' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0004 | system_requirement | approved | Lead with the most important information, then the detail (the inverted pyramid) |
| SR-0005 | system_requirement | approved | Group related material under informative, task-based headings |
| SR-0006 | system_requirement | approved | Present information in the order the reader will need it, answering likely qu... |
<!-- tl:end -->

## 3. Choose familiar, concrete words

<!-- tl:item UR-0003 -->
**UR-0003 — Choose familiar, concrete words** — `user_requirement`, status `approved`

> Prefer the plainest word that carries the meaning, and keep terms consistent.

*Derives from:* INT-0001

**source_ref**: ISO 24495-1:2023 — Principle 3 (Understandable)
<!-- tl:end -->

<!-- tl:table attrs.get('principle') == 'UR-0003' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0007 | system_requirement | approved | Use the most common word that carries the meaning |
| SR-0008 | system_requirement | approved | Define any unavoidable technical term at its first use |
| SR-0009 | system_requirement | approved | Spell out an abbreviation at first use, with the short form in brackets after it |
| SR-0010 | system_requirement | approved | Avoid Latin and foreign phrases |
| SR-0011 | system_requirement | approved | Use the same word for the same thing throughout |
<!-- tl:end -->

## 4. Prefer active voice and strong verbs

<!-- tl:item UR-0004 -->
**UR-0004 — Prefer active voice and strong verbs** — `user_requirement`, status `approved`

> Put the actor first and let precise verbs carry the sentence.

*Derives from:* INT-0001

**source_ref**: ISO 24495-1:2023 — Principle 3 (Understandable)
<!-- tl:end -->

<!-- tl:table attrs.get('principle') == 'UR-0004' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0012 | system_requirement | approved | Write in the active voice unless the actor is unknown or irrelevant |
| SR-0013 | system_requirement | approved | Use the strongest, most precise verb available |
| SR-0014 | system_requirement | approved | Avoid hidden verbs |
| SR-0015 | system_requirement | approved | Use "must" to state an obligation |
| SR-0016 | system_requirement | approved | Use the present tense wherever the meaning allows |
<!-- tl:end -->

## 5. Keep sentences and paragraphs short

<!-- tl:item UR-0005 -->
**UR-0005 — Keep sentences and paragraphs short** — `user_requirement`, status `approved`

> Carry one idea at a time so the reader never has to re-read.

*Derives from:* INT-0001

**source_ref**: ISO 24495-1:2023 — Principle 3 (Understandable)
<!-- tl:end -->

<!-- tl:table attrs.get('principle') == 'UR-0005' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0017 | system_requirement | approved | Express one main idea per sentence |
| SR-0018 | system_requirement | approved | Keep the subject, verb and object close together |
| SR-0019 | system_requirement | approved | Avoid double negatives and exceptions to exceptions |
| SR-0020 | system_requirement | approved | Keep each paragraph to a single topic, opened by a topic sentence |
<!-- tl:end -->

## 6. Be concise

<!-- tl:item UR-0006 -->
**UR-0006 — Be concise** — `user_requirement`, status `approved`

> Cut every word that carries no meaning.

*Derives from:* INT-0001

**source_ref**: ISO 24495-1:2023 — Principle 3 (Understandable)
<!-- tl:end -->

<!-- tl:table attrs.get('principle') == 'UR-0006' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0021 | system_requirement | approved | Delete words that add no meaning |
| SR-0022 | system_requirement | approved | Remove redundant pairs such as "each and every" |
| SR-0023 | system_requirement | approved | Cut intensifiers that add no information, such as "very" and "really" |
| SR-0024 | system_requirement | approved | Replace a wordy phrase with one word |
<!-- tl:end -->

## 7. Design pages so they can be scanned

<!-- tl:item UR-0007 -->
**UR-0007 — Design pages so they can be scanned** — `user_requirement`, status `approved`

> Lay out content so a reader can skim to the part they need.

*Derives from:* INT-0001

**source_ref**: ISO 24495-1:2023 — Principle 2 (Findable)
<!-- tl:end -->

<!-- tl:table attrs.get('principle') == 'UR-0007' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0025 | system_requirement | approved | Break content with headings and subheadings that describe what follows |
| SR-0026 | system_requirement | approved | Use a bulleted or numbered list for a series of items or steps |
| SR-0027 | system_requirement | approved | Use a table to present conditional or comparative information |
| SR-0028 | system_requirement | approved | Use short line lengths and generous whitespace so text can be scanned |
<!-- tl:end -->

## 8. Test that real readers understand

<!-- tl:item UR-0008 -->
**UR-0008 — Test that real readers understand** — `user_requirement`, status `approved`

> Treat comprehension as measurable and verify it.

*Derives from:* INT-0001

**source_ref**: ISO 24495-1:2023 — Principle 4 (Usable)
<!-- tl:end -->

<!-- tl:table attrs.get('principle') == 'UR-0008' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0029 | system_requirement | approved | Set a readability target appropriate to the audience and check the draft agai... |
| SR-0030 | system_requirement | approved | Test drafts with people from the target audience and revise on what confuses... |
<!-- tl:end -->

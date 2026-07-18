# throughline-plain-language

The **readability / plain-language** content axis, expressed as a
[throughline](https://pypi.org/project/throughline/) **source** — a standalone,
grounded requirements graph that a consuming project composes with
[throughline-compose](https://github.com/timebacksolutions/throughline-compose).

This repository holds no application code. It is a directory of small YAML items with
permanent UIDs, validated by `tl check`. Consumers import it under a namespace and
reference its rules as `plain:SR-0007` or its principles as `plain:UR-0003`.

## One orthogonal axis, on purpose

Content quality is not one dimension — it is several independent ones, and a good
piece of writing satisfies a chosen combination of them. This source is **only** the
readability axis: is the text understood correctly on first reading? It deliberately
says nothing about:

- **spelling & mechanics** (UK/US spelling, punctuation, capitalisation, numbers)
- **tone / register** (formal, informal, playful, authoritative)
- **genre / purpose** (inform, instruct, persuade, negotiate, reassure)
- **medium / channel** (web page, email, microcopy, slide deck, long-form)
- **brand voice** (an organisation's own personality)

Each of those is its own throughline source. Keeping the axes separate is the whole
point: a task like *"a plain, formal, UK-English web page for a lay audience"* becomes
a **compose** of `plain` + `tone-formal` + `mechanics-uk` + `medium-web` — the same
way a security project composes `asvs` + `gds` + `wcag`. Folding tone or spelling into
this file would make it un-composable, because you could no longer take the
readability rules without also taking a tone you did not want.

## What's in the graph

<!-- tl:count type == 'user_requirement' -->
8
<!-- tl:end --> principles as `user_requirement`s, each `derives_from` the root
intent, and
<!-- tl:count type == 'system_requirement' -->
30
<!-- tl:end --> concrete rules as `system_requirement`s, each `implements` its
principle. The published spec is generated from the graph at
[`docs/spec.md`](docs/spec.md).

- `INT-0001` — the root intent (why plain language exists), `normative: false`.
- Principles `UR-0001`…`UR-0008` — eight readability themes.
- Rules `SR-0001`…`SR-0030` — the concrete instructions, each carrying the ISO
  24495-1:2023 governing principle it elaborates in `attrs.source_ref` and its owning
  principle in `attrs.principle`.

The counts above are rendered from the live graph by the `tl:count` directive, so they
cannot drift.

## Source & licensing

The rules are Time Back Solutions' own, licensed under Apache-2.0. They are informed
by the **international consensus on plain language** — principally **ISO 24495-1:2023**
(*Plain language, Part 1: Governing principles and guidelines*: Relevant, Findable,
Understandable, Usable) and the **International Plain Language Federation**'s
definition. Those standards are referenced, not reproduced — each item's
`attrs.source_ref` names the governing principle it elaborates, and no ISO text is
copied. Nothing here is US-specific. See [`NOTICE`](NOTICE).

## Extending the source

Items are hand-authored static YAML — one file per item, one permanent UID per file.
To add a rule, create the next `SR-00NN.yml` by hand (never renumber an existing one),
link it with `implements` to its principle, and record the ISO principle it elaborates
in `attrs.source_ref`. Then:

```sh
tl check --strict      # the graph must stay sound
tl docs                # regenerate docs/spec.md
tl docs --check        # CI gate: docs must match the graph
```

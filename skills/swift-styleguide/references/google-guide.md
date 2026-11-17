# Google Swift checklist and provenance

## Upstream baseline

- Use descriptive `.swift` filenames; name single-type files after their type and conformance extensions with a type-plus-protocol name.
- Import needed modules explicitly; keep imports grouped and sorted as described by the guide.
- Use spaces, two-space block indentation, and a 100-column target, honoring upstream exceptions for imports, generated code, and indivisible text.
- Avoid statement semicolons. Keep separate statements readable; a short single-statement block may remain inline.
- Wrap argument lists consistently; preserve Swift syntax and meaningful literal content.
- Keep switch cases aligned with the switch and indent their bodies.
- Organize declarations logically and keep related overloads together.
- Use Swift API naming conventions and meaningful access modifiers.
- Prefer explicit, understandable optional/error handling. Force unwraps require a clear safety invariant; test-only code has exceptions. Do not impose a blanket ban on every `!`.
- Write useful documentation summaries; document parameters, results, and thrown errors when they add information.

These are paraphrased reminders, not a replacement for the full guide's exceptions.

## Source

- Publisher: Google, drawing on Apple's Swift API conventions.
- Read on: 2026-11-17.
- [Published guide](https://google.github.io/swift/).
- [Pinned guide source](https://github.com/google/swift/blob/79459b39f2ab0330ee05a90f20c3f716d8406b24/index.md).
- Revision: `79459b39f2ab0330ee05a90f20c3f716d8406b24`, `gh-pages`, 2019-06-05.
- [Branch license](https://github.com/google/swift/blob/79459b39f2ab0330ee05a90f20c3f716d8406b24/LICENSE.txt): Apache 2.0 with the displayed runtime-library exception. Do not assume the separate google/styleguide repository's license applies here.

This skill is an independently written workflow and short paraphrased checklist, not an official Google package. Full upstream text is not bundled. Project precedence, API preservation, incremental edits, current-tool verification, and modern Swift compatibility are explicit adaptations of this skill.

## Applying old guidance to current code

The revision date is material: check current compiler and library requirements before interpreting old examples as current API advice. A project formatter can implement a chosen formatting profile without checking API design or semantic safety. A passing formatter alone is insufficient evidence of full guide compliance.

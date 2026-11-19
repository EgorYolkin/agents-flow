---
name: python-styleguide
description: Write, review, and refactor Python code using an adapted Google Python Style Guide. Use for Python style, imports, naming, typing, docstrings, function responsibilities, and maintainability in modules, scripts, and tests while preserving public APIs and supported Python versions.
---

# Python Style Guide

Apply Google-derived conventions within the project's compatibility and behavior
contracts. This skill covers Python code; framework design and security audits
require context beyond a style guide.

## Workflow

1. Read repository instructions, affected code, callers, and relevant tests.
   Inspect declared Python versions, packaging metadata, formatter, linter,
   type-checker, and test configuration. Do not infer the supported version
   from the interpreter installed on the agent's machine.
2. For review or explanation, report findings without editing. For creation or
   correction, keep changes within the requested scope and preserve unrelated
   work. Project requirements take precedence over baseline preferences.
3. Read [Google-derived rules and adaptations](references/google-guide.md).
   Distinguish upstream guidance, project conventions, and behavioral defects.
4. Check affected contracts before changing names, imports, signatures, default
   values, annotations, or exception handling. Public keyword arguments,
   re-exports, serialization fields, and runtime annotation consumers matter.
   When introducing or reviewing names, apply the
   [naming conventions](references/google-guide.md#naming-conventions)
   within those contracts.
   For a changed public API, check whether annotations preserve relationships
   between arguments, fields, and results. Could a caller use it from its
   signature and docstring alone? See the
   [typed contract examples](references/google-guide.md#typed-api-contracts).
5. Start with the simplest change that serves the current caller and fits the
   existing module. Do not design layers or extension points for hypothetical
   requirements. Extract a responsibility when it has meaningful inputs and
   results; avoid helpers that only hide a line of code.
   Before proposing a boundary, trace one real call from input to observable
   result. What cannot change or be tested independently today, and what is
   the smallest change that would let it? If there is no concrete problem,
   keep the existing boundary. See the
   [checkout example](references/google-guide.md#finding-a-useful-boundary).
   Introduce a class when shared state, invariants, or a lifecycle justify it,
   not because a function crosses a line-count threshold.
   Compare the [function and object examples](references/google-guide.md#choosing-a-function-or-an-object)
   before recommending a new abstraction; name the invariant it would protect.
6. Run relevant existing formatting, lint, type, and test checks when available.
   Inspect automatic fixes before accepting them. Do not install tools, change
   dependencies, or rewrite project configuration merely to impose this guide.
   For unfamiliar or version-dependent tool options, consult current official
   documentation through Context7 when available.
7. Review the final diff and report checks actually performed. Formatting and
   lint success do not prove behavior preservation or full guide compliance.

## Function and class layout

Apply these user-selected conventions to functions, methods, and classes. They
are deliberate adaptations, not claims about Google's required formatting.

- Put opening and closing triple double quotes (`"""`) on their own lines,
  with the docstring text between them, even for a one-sentence description.
  Keep the docstring as the first statement in its function or class.
- Leave one blank line after the closing docstring before the implementation,
  class attributes, or first method. Do not insert a blank line inside a
  docstring merely to create this separation.
- Separate meaningful phases with one blank line: for example, environment
  setup, download-command construction with its options, then returning the
  result. Use the phases actually present; do not force a three-block template.
- Keep related statements compact. An `if` that validates or extends the
  immediately preceding operation stays adjacent to it, without a blank line.
  Keep its dependent statements in the same block; do not space every statement
  or every `if` apart mechanically.
- After a guard that exits on failure, leave one blank line before the
  successful path. After changing object state, leave one blank line before
  returning the result. Keep the `raise` inside its guard.
- Use whitespace to expose existing meaning, not to reorder side effects or
  invent helpers and classes. See the
  [layout example](references/google-guide.md#preferred-layout-example).

Apply this layout to new and touched code within the request's scope. If explicit
target-project rules or configured tooling conflict, explain the conflict rather
than silently dropping the preference or changing tooling without authorization.

## Compatibility and edge cases

These safeguards adapt the guide to existing projects.

- Preserve public names and accepted keyword arguments during style fixes.
  Check callers before renaming even an apparently private helper.
- Preserve import-time behavior and import order where registration or plugin
  loading depends on them. Moving an import behind a type-checking guard can
  break runtime annotation inspection; inspect consumers first.
- Match annotation syntax to every supported Python version. Do not widen
  dependencies or change runtime validation to satisfy annotation preferences.
- Distinguish missing values, `None`, and valid falsy values. Replacing an
  explicit condition with a truthiness check must preserve that distinction.
- Review mutable defaults, exception boundaries, resource cleanup, iterator
  consumption, and async cancellation only where the changed code makes them
  relevant. Do not turn every style review into an unrelated audit.
- When extracting code, preserve exception types, side-effect order, lazy
  evaluation, and resource lifetimes. Use existing focused tests to check
  affected behavior; do not require an architectural rewrite for style alone.

## Review and completion

Give actionable findings with file and location, observed consequence, and a
specific correction. Separate correctness issues from agreed style violations
and optional readability suggestions. If there are no actionable issues, say so.

After edits, summarize meaningful changes, compatibility decisions, checks, and
unverified behavior. Report unavailable tooling as a limitation, not a passed
check. Do not claim an exhaustive security review from this workflow.

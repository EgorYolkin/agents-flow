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
5. Make focused changes. Extract a responsibility when it has a meaningful
   boundary, inputs, and result; avoid helpers that only hide a line of code.
   Introduce a class when shared state, invariants, or a lifecycle justify it,
   not because a function crosses a line-count threshold.
6. Run relevant existing formatting, lint, type, and test checks when available.
   Inspect automatic fixes before accepting them. Do not install tools, change
   dependencies, or rewrite project configuration merely to impose this guide.
   For unfamiliar or version-dependent tool options, consult current official
   documentation through Context7 when available.
7. Review the final diff and report checks actually performed. Formatting and
   lint success do not prove behavior preservation or full guide compliance.

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

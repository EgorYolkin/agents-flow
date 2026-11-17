# Google Python guidance and project adaptations

## Source and attribution

Adapted from the Google Python Style Guide by Google contributors.
Accessed 17 November 2026.

- [Pinned guide](https://github.com/google/styleguide/blob/a9c5f82b19811f1552d73df384a9f9d7c75ca16e/pyguide.md)
- [Published guide](https://google.github.io/styleguide/pyguide.html)
- [Repository licensing](https://github.com/google/styleguide/blob/a9c5f82b19811f1552d73df384a9f9d7c75ca16e/README.md#licensing)

Upstream text is licensed under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/);
upstream code samples use Apache 2.0. This reference paraphrases selected rules
and adds project-integration safeguards. It reproduces no upstream code samples.
Keep attribution when redistributing adaptations.

## Selected upstream rules

- Use four-space indentation and an 80-character line target, allowing the
  guide's exceptions. Prefer implicit continuation inside parentheses.
- Use `snake_case` for functions and variables, `CapWords` for classes, and
  `UPPER_SNAKE_CASE` for constants; respect externally required names.
- Prefer module/package imports with full package paths. Imports of symbols
  from `typing`, `collections.abc`, and `typing_extensions` are exempt.
- Avoid mutable defaults and unnecessary mutable global state. Keep
  comprehensions readable and exception handlers specific.
- Document contracts with useful docstrings and applicable `Args`, `Returns`
  or `Yields`, and `Raises` sections; avoid repeating obvious implementation.
- Annotate public APIs and use types where helpful, not mechanically everywhere.
- Prefer small, focused functions. Around 40 lines prompts reconsideration,
  not a mandatory split or class conversion.
- Use context managers for stateful resources where appropriate.
- Google recommends Pylint and mentions Black/Pyink for formatting.

Consult upstream sections 2.1–2.5, 2.7, 2.12, 3.2–3.4, 3.8, 3.11,
and 3.13–3.19 for details and exceptions; this selection is not exhaustive.

## Deliberate project adaptations

- **Existing tooling owns formatting.** Keep the project's chosen formatter
  and line length. Explain a difference from Google's baseline rather than
  repeatedly undoing formatter output. Do not install a competing formatter.
- **Tool coverage is partial.** Ruff, Pylint, type checkers, and tests cover
  different concerns. An existing Ruff setup is not proof that every Google
  rule is enforced. Do not enable all rules or blanket suppressions to make a
  style task appear complete.
- **Imports are contracts too.** Preserve public re-exports, framework-required
  imports, and intentional initialization. Apply the full-path preference
  only after checking package layout and supported invocation modes.
- **Typing can affect runtime.** Check annotation consumers before changing
  evaluation timing or moving dependencies out of runtime imports. Preserve
  the project's supported Python versions and type-checking strategy.
- **Documentation follows behavior.** Describe meaningful return values,
  exceptions, side effects, and generator behavior. Do not invent contracts
  or impose repetitive docstrings on every trivial test helper.
- **Responsibility is semantic.** Separate unrelated decisions or effects when
  doing so clarifies ownership and testing. A cohesive multi-step operation
  may remain one function; length alone is insufficient evidence of a defect.
- **Libraries are project choices.** Examples in Google's guide do not authorize
  adding Google-specific packages or changing the application's entrypoint.

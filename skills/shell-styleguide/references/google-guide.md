# Google Shell guidance and adaptation

Source: [Google Shell Style Guide](https://google.github.io/styleguide/shellguide.html), inspected 2026-11-17. Pinned [upstream source](https://github.com/google/styleguide/blob/a9c5f82b19811f1552d73df384a9f9d7c75ca16e/shellguide.md).

## Selected upstream guidance

- Default to Bash for executable scripts; constrained environments can require another shell. Keep shell for small wrappers and straightforward utility orchestration.
- Use two-space indentation for new code, retaining existing indentation when editing. The normal line-length target is 80 characters.
- Explain a file's purpose briefly. Document non-obvious functions and library APIs, including arguments, global effects, outputs and statuses.
- Quote expansions appropriately, use command substitution rather than backticks, and use arrays for Bash argument lists. Avoid `eval`.
- Prefer lowercase names with underscores for functions and ordinary variables; reserve uppercase for constants and environment variables. Keep function variables local where supported.
- Separate a declaration from command substitution when the declaration could hide a failure. Check return statuses and send errors to stderr.
- Use ShellCheck. More than 100 lines or complicated control flow prompts Google's recommendation to migrate to a structured language.

Read the linked section for exceptions before asserting a violation.

## Project adaptation

The workflow in SKILL.md makes compatibility and authorized scope explicit. It treats migration as a recommendation requiring a separate decision, preserves required POSIX sh, and uses existing project tooling. Google-guide compliance is not equivalent to passing a linter.

## Attribution

Adapted and condensed from Google Style Guides, authored and maintained by Google contributors. Google guide text is licensed under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/); upstream code samples are under Apache 2.0. See [upstream licensing](https://github.com/google/styleguide#licensing). This reference paraphrases selected guidance and adds labeled project adaptations; it does not reproduce the full guide.

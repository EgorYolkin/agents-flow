---
name: shell-styleguide
description: Write, review, and refactor Bash and POSIX sh scripts using an adapted Google Shell Style Guide while preserving interpreter compatibility, argument boundaries, and exit behavior. Use for shell code quality or style work, including extensionless executables, sourced shell libraries, entrypoint scripts, and shell fragments in CI or Dockerfiles. Apply when fixing quoting, naming, formatting, function contracts, or command error handling even if the user does not mention Google. Do not apply Bash rules to PowerShell, fish, Python, or ordinary prose about terminals.
---

# Shell Style Guide

Make shell code readable without changing its execution contract merely to satisfy a stylistic preference.

## Workflow

1. Inspect the requested files, repository instructions, formatter/linter configuration, callers, and relevant tests. Identify executable versus sourced code, the actual interpreter and version, and supported platforms. For embedded shell, inspect the host configuration's interpolation and escaping rules too.
2. Establish scope: for review or explanation, report findings without editing. For an implementation request, edit only the relevant code; preserve unrelated changes and established local conventions.
3. Read [Google-derived rules](references/google-guide.md). Prefer explicit project requirements and compatibility constraints over the upstream default. Record meaningful deviations rather than silently rewriting the environment.
4. Check behavior before formatting: positional arguments, empty values, paths with spaces, globbing, command statuses, stdout/stderr, environment changes, and sourced-library side effects. Follow data through command substitutions and pipelines instead of judging quoting from appearance alone.
5. Make a focused change. Keep public names, filenames, output formats, environment variables, and exit codes stable unless the requested fix requires a change. Do not convert a shell library into an executable or introduce automatic execution when sourced.
6. Validate using the project's existing tools. Use the target interpreter's syntax check and configured ShellCheck/shfmt when available; review their diff before accepting fixes. Fetch current tool documentation through Context7 when uncertain about flags or configuration. Missing tools are a reported limitation, not permission to install dependencies automatically.
7. Execute behavior tests only in a controlled temporary environment with harmless inputs or stubbed dependencies. Reading a script is not authorization to run its deployment, deletion, credential, network, or production actions. Keep runtime validation distinct from syntax or lint checks.

## Adaptation and behavior safeguards

These are integration rules for this skill, not claims that every point is prescribed by Google.

- Determine dialect from the shebang, callers and CI shell selection. Keep required POSIX sh portable; do not introduce Bash arrays, `[[ ... ]]`, `source`, or `local` into that profile. Do not change the shebang as a formatting fix. If evidence conflicts, explain the uncertainty before making an incompatible change.
- Treat `set -euo pipefail` as a behavioral decision. Existing scripts may intentionally handle nonzero results, missing variables, or early pipeline termination. Evaluate each option before adding it; explicit critical-operation checks and tests are still needed.
- Preserve argument boundaries, normally with quoted expansions and `"$@"`. Deliberate splitting or pattern expansion needs a reason; quoting everything mechanically can also change semantics.
- Inspect status propagation around assignments, declaration builtins, negation, pipelines, and traps. Do not replace meaningful failures with unconditional success or lose the command's status while logging.
- Avoid `eval` and string-built commands for ordinary argument forwarding. Prefer direct invocations; in Bash, arrays can represent argument lists. Do not introduce command strings when structured arguments suffice.
- Change names only after checking callers, sourced files and environment contracts. Do not rename public shell functions, exported variables or CLI commands purely for style.
- Consider complexity and maintainability when a script grows. Google's migration recommendation becomes a discussion trigger here; a style task does not authorize a rewrite into Python or a forced line-count limit.
- For Dockerfile or CI snippets, preserve the enclosing file's expansion semantics, shell selection and continuation structure. Scope this skill to the shell portion.

## Findings and completion

For a review, report concrete findings with file/location, observed consequence, relevant rule, and a narrow recommendation. Distinguish correctness defects, agreed style violations and optional readability suggestions. If there is no actionable finding, say so; do not manufacture work to satisfy a checklist.

After changes, summarize files changed, meaningful behavior choices, checks actually run and any unverified cases. A formatter pass does not establish full Google-guide compliance or runtime correctness.

# Google Shell guidance and adaptation

Source: [Google Shell Style Guide](https://google.github.io/styleguide/shellguide.html), inspected 2026-11-17. Pinned [upstream source](https://github.com/google/styleguide/blob/a9c5f82b19811f1552d73df384a9f9d7c75ca16e/shellguide.md).

## Selected upstream guidance

- Google requires Bash for executable scripts unless the target environment
  forces another shell (§1.1). Shell suits small wrappers and straightforward
  utility orchestration (§1.2); this is not a portability standard for `sh`.
- Use two-space indentation for new code, retaining existing indentation when editing. The normal line-length target is 80 characters.
- Describe each file's purpose. Under §4.2, *every* library function needs a
  header, even if short; other functions need one unless both obvious and short.
  Describe the operation, globals read or changed, arguments, output on each
  stream, and any return status other than the last command's default status.
- Quote expansions appropriately, use command substitution rather than backticks, and use arrays for Bash argument lists. Avoid `eval`.
- For names (§7.1–7.5), use lowercase words separated by underscores for
  functions and ordinary variables; use uppercase for constants and exported
  variables. A Bash library may prefix functions with `package::`; standalone
  functions need no prefix. Use `local` for function variables in Bash.
- Separate `local` from an assignment using command substitution: otherwise
  the declaration can mask the substitution's status (§7.5). Check command
  outcomes (§8.1) and send errors to stderr (§3.1).
- Google calls for `main "$@"` at the end of an executable with other
  functions, not for short linear scripts (§7.7). It recommends ShellCheck
  (§6.1) and migration to a structured language for scripts over 100 lines or
  with non-straightforward control flow (§1.2).

Section numbers refer to the pinned source above. Consult its examples and
exceptions before asserting a violation.

## Project adaptation

Keep the project's shell, caller-visible names and tools. In portable `sh`,
use `name() { ...; }`, not `function` or `package::name`; if real library
collisions require a prefix, `package_name` is portable. Bash can pass an
array as `"${fields[@]}"`; portable `sh` can keep separate arguments in the
positional parameters and forward `"$@"`. Neither needs a string-built command.

Use a direct command when its interface is already the one the caller needs.
Give a function a name when it owns a real contract. If a script starts to
model complex data or lifecycles with global variables and dispatch functions,
discuss a more suitable language rather than building an object system in
shell. The upstream migration threshold is a reason to discuss, not authority
to rewrite. A sourced library defines operations; do not append a call to `main`
that executes on import.

## Original shell examples

These are project examples, not upstream samples. The blank line after a guard
and before a distinct status return is a project preference; keep related
operations together and respect explicit formatter rules.

### POSIX sh: preserve records and the writer's status

For one known field, `printf '%s\000' "$field"` is enough. This library
function earns its name when callers need the same record format **and** a
missing argument list is a usage error:

```sh
# Write a nonempty list of fields as NUL-terminated records.
# Arguments: One or more strings, including empty strings. No options.
# Outputs: Each argument followed by NUL on stdout; diagnostics on stderr.
# Returns: 2 for missing operands; otherwise the status of printf.
write_fields0() {
  if [ "$#" -eq 0 ]; then
    printf '%s\n' 'write_fields0: expected at least one field' >&2
    return 2
  fi

  printf '%s\000' "$@"
}
```

In contrast, `printf '%s\000' "$*"` writes one joined field for multiple
arguments; unquoted `$@` can split fields or expand globs. The guard
distinguishes no arguments from `write_fields0 ''`, which emits exactly one
NUL. Send the output directly to a file or consumer, not through `$(...)`:
shell variables cannot represent the NUL separators. Leaving `printf` last
propagates a write failure instead of reporting success.

### Bash: separate a state change from a predicate's result

Here a caller uses `if take_retry; then ...` and must get one final retry
when the budget is 1. The caller initializes the counter; call the function
in the same shell, not a command substitution or subshell.

```bash
# Claim one retry from the caller's budget.
# Globals: retries_left, a writable nonnegative shell integer; decremented on success.
# Arguments: None.
# Outputs: None.
# Returns: 0 when a retry was claimed; 1 when the budget was already empty.
take_retry() {
  if (( retries_left == 0 )); then
    return 1
  fi

  retries_left=$((retries_left - 1))

  return 0
}
```

Using `(( --retries_left ))` as the last command instead would make the change
but return status 1 when the new value is zero. That would tell the caller it
had *not* claimed its last retry. Status describes the operation, not the
new count; the two are intentionally separate here.

## Attribution

Adapted and condensed from Google Style Guides, authored and maintained by
Google contributors. Google guide text is licensed under
[CC BY 3.0](https://creativecommons.org/licenses/by/3.0/); upstream code
samples are under Apache 2.0. See the
[pinned licensing terms](https://github.com/google/styleguide/blob/a9c5f82b19811f1552d73df384a9f9d7c75ca16e/README.md#licensing).
This reference paraphrases selected guidance; its worked examples are original.

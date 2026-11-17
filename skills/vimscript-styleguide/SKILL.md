---
name: vimscript-styleguide
description: Write, review, and refactor Vim script using Google Vimscript style with explicit compatibility safeguards. Use for .vim files, vimrc sections, autoload functions, plugin commands, mappings, and autocommands, including targeted style fixes that do not explicitly mention Google. Preserve the project's Vim or Neovim version and dialect. Do not apply legacy Vimscript rules to Lua-only Neovim configuration or treat this skill as a Vim9 migration request.
---

# Vimscript Style Guide

Make Vim script readable and predictable without changing its public commands,
mappings, supported editor versions, or intended interaction with user settings.

## Workflow

1. Inspect the requested files, project instructions, supported editor versions,
   existing tests, plugin layout, and any formatter configuration. Distinguish
   legacy Vimscript, Vim9 script, embedded Vimscript, and Lua before editing.
2. Read [the rule reference](references/google-guide.md). Use its upstream links
   for a disputed rule; distinguish a Google recommendation from a deliberate
   project adaptation. Existing compatibility and public API contracts take
   precedence over a cosmetic rewrite.
3. For a review, explain findings without editing. For an implementation or fix,
   change only the requested area and necessary adjacent code. Preserve exported
   autoload names, command flags, mapping modes, option scopes, and return values.
4. Apply mechanical style corrections first. Review semantic changes separately:
   regex flags, command bangs, mapping recursion, `abort`, exception handling,
   scopes, and quoting can change behavior. Do not disguise them as formatting.
5. Validate with the project's existing safe checks when available. Inspect what
   a check executes before running it. Never source an unknown vimrc or plugin
   just to check syntax: Vimscript can execute shell commands and modify files.
   Use a disposable environment with a clean configuration for tests of code
   already inspected; preserve the actual target editor/version in the result.
6. Summarize edits or findings, why they matter, checks actually performed, and
   relevant limitations. Do not equate a formatter result with runtime validity.

## Core decisions

- Use two-space indentation and spaces around expression operators. Command
  arguments have their own grammar: do not insert spaces inside command flags.
- Prefer descriptive scoped names in legacy code. Preserve externally consumed
  names and autoload path/name correspondence. Do not add legacy scope prefixes
  to Vim9 constructs without checking the dialect.
- Prefer single-quoted literal strings; keep double quotes when escape sequences
  are intentional. Changing quote marks requires checking the resulting value.
- Make pattern magic and case decisions explicit when matching protocol or
  plugin syntax. Preserve intentional searches that honor the user's settings.
- Prefer functions with controlled side effects over cursor-changing Ex commands
  when they achieve the same goal. Preserve cursor, selection, registers and
  buffer state where the existing contract requires it.
- Prefer `normal!` for literal built-in keystrokes. Keep intentional remapping
  explicit; never mechanically change mappings or `normal` when the feature
  relies on a user or plugin mapping.
- Use a plugin-owned augroup and clear only that group when reloading its own
  autocommands. A global `autocmd!` can erase other plugins' behavior.
- Prefer local options where appropriate. A plugin whose purpose is to change a
  global option is a valid exception; do not change its scope silently.
- Treat mapping RHS bytes as behavior, including trailing spaces used to prepare
  command-line input. Do not run whitespace cleanup blindly over mappings.

## Compatibility and dependencies

Google's guide assumes a particular plugin ecosystem and includes historical
recommendations. Do not add maktaba, Glaive, VAM metadata, vimdoc, new dependencies,
autoload directories, or a new plugin manager just to satisfy this skill. Reuse
those conventions only when the project already uses them or the task explicitly
requests adoption. Keep a standalone vimrc edit standalone.

Do not convert Vimscript to Vim9 or Lua as a style fix. Do not use the guide's
historical restrictions on embedded languages to remove existing Neovim Lua
integrations. For modern API or tool syntax, consult current primary editor
documentation (Context7 when available) and the project's minimum version.
Do not install a formatter or editor automatically.

## Review output

For each actionable finding, give the file and location, concrete consequence,
relevant rule, and smallest suitable correction. Separate behavior defects from
style suggestions. Report intentional exceptions rather than asking for needless
rewrites. If no material issue is found, say so; do not invent violations to fill
out a checklist.

## Validation scope

A review can be static. Runtime checks should target the feature: test relevant
case/magic settings, load-twice behavior, mapping collisions, and buffer-local
options only when affected. Do not execute arbitrary user configuration or claim
checks ran when tools or safe fixtures were unavailable.

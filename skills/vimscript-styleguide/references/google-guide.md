# Google Vimscript rules and project adaptations

## Source and attribution

Adapted and condensed from **Google Vimscript Style Guide** and **Google
Vimscript Guide**, credited upstream to Nate Soares, Artemis Sparks, and David
Barnett. Retrieved 2026-11-17 at Google styleguide revision
`a9c5f82b19811f1552d73df384a9f9d7c75ca16e`.

- [Short guide](https://github.com/google/styleguide/blob/a9c5f82b19811f1552d73df384a9f9d7c75ca16e/vimscriptguide.md)
- [Detailed guide](https://github.com/google/styleguide/blob/a9c5f82b19811f1552d73df384a9f9d7c75ca16e/vimscriptfull.md)
- [Upstream license](https://github.com/google/styleguide/blob/a9c5f82b19811f1552d73df384a9f9d7c75ca16e/LICENSE): CC BY 3.0 for guide text; upstream repository identifies code samples as Apache 2.0.

This is a selective adaptation, not an official Google skill. Compatibility,
minimal-diff, and safe-validation guidance below is added for agent workflows.

## Upstream recommendations to apply with context

| Area | Upstream direction | Application boundary |
|---|---|---|
| Whitespace | Two-space blocks, four-space continuation indentation, 80 columns; spaces around expression operators | Command flags and mapping RHS are not ordinary expressions; preserve meaningful trailing spaces |
| Names | Descriptive scoped variables, CamelCase functions/commands, plugin-prefixed augroups | Retain public names and autoload path correspondence |
| Strings | Prefer single quotes for literals and regexes; double quotes for evaluated escapes | Compare actual string semantics before changing quotes |
| Matching | Explicit case operators and regex magic/case flags | Detailed guide allows deliberate user-sensitive buffer searches |
| Errors | Match stable error codes, not translated message text; keep library errors catchable | Preserve the documented error/return contract |
| Functions | Namespaced autoload functions and script-local helpers; `function!` and `abort` | Adding `abort` changes error continuation; avoid layout migrations for small edits |
| Commands | Expose commands for user actions; delegate logic; avoid silently overwriting another command | Preserve established reload guards and intentionally replaceable commands |
| Autocommands | Owned augroups, clear that group before redefinition, delegate logic | Never clear all groups; account for existing mixed ownership |
| Mappings | Prefer mode-specific nonrecursive mappings and script-local references using `<SID>` | Intentional recursion and mapping chains require semantic inspection |
| Settings | Prefer explicit local options and descriptive full names | Preserve intentional global configuration and restore temporary state |

The short guide's prose around `\m` is imprecise: it describes `\m` alongside
“nomagic.” Follow the explicit magic-level semantics, not that wording. The
full guide permits an intentional choice among magic modes. Never add flags to
a user-supplied pattern that is intended to preserve the user's choices.

## Modern compatibility adaptations

- Google recommends maktaba-based plugin layout and metadata. This skill does
  not introduce that dependency into unrelated projects.
- Historical guidance against other scripting languages reflects older Vim
  portability assumptions; it is not a ban on Lua in a Neovim project.
- Do not replace callbacks or modern constructs based only on historical FuncRef
  limitations. Verify the supported editor version and current behavior first.
- Do not remove command replacement or mapping recursion without examining its
  purpose. A style-only task does not authorize changing extension points.
- Keep existing tests and documented APIs; avoid repository-wide formatting.

## Primary editor documentation

[Mapping documentation](https://github.com/vim/vim/blob/master/runtime/doc/map.txt)
and [plugin-writing manual](https://github.com/vim/vim/blob/master/runtime/doc/usr_51.txt)
were queried through Context7 `/vim/vim` on 2026-11-17 for `<SID>`, `<Plug>` and
nonrecursive mappings. In particular, `<Plug>` in a RHS has special remapping
behavior even in a nonrecursive mapping. Do not infer ordinary recursion rules
from the command name alone. These living docs supplement, but do not replace,
the project's minimum-version documentation.

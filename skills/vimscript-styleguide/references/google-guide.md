# Google Vimscript rules and project adaptations

## Source and attribution

Adapted and condensed from **Google Vimscript Style Guide** and **Google
Vimscript Guide**, credited upstream to Nate Soares, Artemis Sparks, and David
Barnett. Retrieved 2026-11-17 at Google styleguide revision
`a9c5f82b19811f1552d73df384a9f9d7c75ca16e`.

- [Short guide](https://github.com/google/styleguide/blob/a9c5f82b19811f1552d73df384a9f9d7c75ca16e/vimscriptguide.md)
- [Detailed guide](https://github.com/google/styleguide/blob/a9c5f82b19811f1552d73df384a9f9d7c75ca16e/vimscriptfull.md)
- [Upstream license](https://github.com/google/styleguide/blob/a9c5f82b19811f1552d73df384a9f9d7c75ca16e/LICENSE) and [licensing statement](https://github.com/google/styleguide/blob/a9c5f82b19811f1552d73df384a9f9d7c75ca16e/README.md#licensing): CC BY 3.0 for guide text; Apache 2.0 for upstream code samples.

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

## What a caller can rely on

The pinned detailed guide's **Variables** and **Usage Guide → Functions**
distinguish script-private helpers from named autoload functions. Use `...`
for optional arguments; pass a List as one argument for a collection. The
**Language Guide** recommends explicit type checks when Vim might coerce
values, catchable exceptions for library code, and dictionary methods for
encapsulated objects, not ordinary helpers. **Documentation** recommends
vimdoc; **Exceptions** calls for documenting thrown errors with `@throws`.

For this skill, keep the project's existing documentation format. Give a
caller enough information to use a new public function without inspecting
it: for a List or Dictionary, name the expected element types or keys and
say if the caller's value is modified. Distinguish a missing result from
an invalid argument. On a user-facing command also describe accepted flags,
range or bang when they affect the operation. Do not make a private helper
public merely so it can have a help tag.

## Original legacy Vimscript examples

These examples are local to this skill, not samples from Google. If a caller
only needs a display name for a file path, nothing needs to outlive the call.
This helper belongs in the script that displays it:

```vim
function! s:DisplayName(path) abort
  if empty(a:path)
    return '[untitled]'
  endif

  return fnamemodify(a:path, ':t')
endfunction
```

Now suppose a caller **must** leave a label for a later call on the same
buffer. In an existing plugin, the following public functions belong in
`autoload/labelbox.vim` on the runtime path. The `b:` variable follows the
buffer, not the window displaying it; wiping the buffer discards the label.

```vim
" Replace the current buffer's pending label with a nonempty String.
" Throws labelbox:InvalidLabel without changing the old label on bad input.
" Call for its effect; there is no meaningful return value.
function! labelbox#Remember(label) abort
  if type(a:label) != type('') || empty(a:label)
    throw 'labelbox:InvalidLabel'
  endif

  let b:labelbox_pending_label = a:label
endfunction


" Return and clear this buffer's pending String, or return '' if none exists.
function! labelbox#Take() abort
  if !exists('b:labelbox_pending_label')
    return ''
  endif

  let l:label = b:labelbox_pending_label
  unlet b:labelbox_pending_label

  return l:label
endfunction
```

Contrast a script-wide slot. This legacy script returns `'draft'` even when
`s:TakeLabel()` is called from another buffer: `s:` makes the name private,
not buffer-local.

```vim
let s:pending_label = 'draft'

function! s:TakeLabel() abort
  let l:label = get(s:, 'pending_label', '')
  unlet! s:pending_label

  return l:label
endfunction
```

For the public version, remember `'draft'` in buffer A, then call `Take` in
buffer B: it must return `''` without consuming A's value. In A the first
call returns `'draft'` and the next `''`. A buffer variable and two functions
express that lifetime without a global registry, object factory, or autocmd.

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

For the legacy examples, see also Vim's [variable scopes](https://github.com/vim/vim/blob/master/runtime/doc/eval.txt)
(`:help buffer-variable`) and [autoload lookup](https://github.com/vim/vim/blob/master/runtime/doc/userfunc.txt)
(`:help autoload-functions`).

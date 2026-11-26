# Google Rust guidance and project adaptations

## Source and scope

Adapted from the [Rust Style Guide by Google contributors](https://github.com/google/styleguide/blob/8bdadbb0732b387aaa26f553dd9033484d1a2071/rustguide.md),
accessed 26 November 2026. The [published guide](https://google.github.io/styleguide/rustguide.html)
can change. The [upstream license notice](https://github.com/google/styleguide/blob/8bdadbb0732b387aaa26f553dd9033484d1a2071/README.md#licensing)
covers text under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)
and upstream code samples under [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0).
This reference paraphrases selected rules and adds integration advice; the
example is original. Retain attribution when redistributing it.

Google builds on the [Rust Style Guide](https://doc.rust-lang.org/style-guide/)
and [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/).
Its API design rules target reusable libraries; in application code they are
strong recommendations, not a reason to generalize a one-off operation.
Read the upstream codebase labels before applying a rule. For example, small
crates, a flat layout for `rust_library` sources and restrictions on `async`
are Chromium guidance, not general requirements for Cargo projects.

## Organizing and naming items

- Name a leaf module after its primary abstraction where it has one. Keep
  non-leaf modules mostly to module declarations and re-exports; a little
  coordinating code is fine. Re-exports can be the intended public path.
- Import items from one module per `use` declaration. Generally qualify calls
  to free functions from other modules and import types by name. Keep a trait
  import near its use unless many functions need it. A qualifier can be useful
  for ambiguous names such as `io::Error`.
- Avoid glob imports by default. `use super::*` in an inline test module is
  permitted. Other exceptions include local enum variants and re-exporting a
  child module from a non-leaf module. Do not remove a public re-export without
  checking consumers.
- Use standard conversion names: `as_` for a cheap borrowed view, `to_` for a
  conversion that may do work, and `into_` for a consuming conversion. Use a
  newtype rather than a type alias when two otherwise interchangeable values
  must not be mixed up.

## Choosing ownership and API shape

Borrow the data the operation needs, not the container that happens to hold
it: `&str` for reading text, `&[T]` for inspecting a slice, `Option<&T>` for
an optional borrowed item. Prefer unique ownership when it is natural. A deep
copy and `Arc::clone` do different things: the latter shares the same allocation.
Use shared ownership when the actual lifetimes justify it.

```rust
/// Returns the label before the first colon, borrowing it from the input.
fn label(line: &str) -> Option<&str> {
    line.split_once(':').map(|(prefix, _)| prefix)
}
```

Here absence of a colon needs no error details. Returning `String` would add
an allocation that an inspecting caller does not need. Conversely, returning
`&str` from a function that builds and drops its own string would not work;
return the owned value when the caller must retain it.

In a reusable library, a single-pass operation can accept `IntoIterator` or
return an iterator so callers need not allocate. Keep a slice when indexing is
part of the operation. Keep a `Vec` result when one already exists, callers
need random access or ownership, or the application is clearer that way.
An iterator is not a drop-in replacement if it defers work, borrows from the
caller, or changes when a failure is observed.

Prefer inherent methods for one type's behavior. Implement a standard trait
when its contract actually fits, and derive it when the generated behavior is
correct. A trait introduced just to group methods buys no polymorphism.
For cross-team APIs, consider `#[non_exhaustive]` on new extensible enums;
closed sets are an exception. Adding it to a released exhaustive enum can
break downstream matches. The same caution applies to external struct literals.

## Errors, documentation, and safety

Use `Option` when absence is expected and the reason adds nothing; use
`Result` when callers need a cause to recover. Propagate errors with `?` when
the error contract permits it; a missing file and a permission failure are
not interchangeable. Reserve panics for bugs or broken invariants, subject to
local policy. Match on `Option` or `Result` rather than checking and then
unwrapping. If an invariant justifies `expect`, explain why it should hold.

Document public items with useful rustdoc: explain error cases and panics
that depend on the input. Prefer safe implementations. For unavoidable unsafe
code, distinguish what the caller must guarantee from the `SAFETY:` comment
explaining why this particular operation meets its preconditions. A comment
is not proof; a performance justification needs measurement.

## Applying these rules in existing projects

These are project adaptations, not additional Google requirements:

- Check the workspace's edition, MSRV, supported targets and feature matrix
  before suggesting newer syntax or APIs. Preserve `no_std` and generated-code
  boundaries where they apply.
- Use the configured formatter. `cargo fmt --check` checks formatting in a
  Cargo project; it does not establish API compatibility or test behavior.
  Use the project's own Clippy, test, and documentation commands if relevant.
- Check downstream callers before changing ownership, trait bounds, visibility,
  re-exports or public types. If a useful redesign would break an existing
  contract, report it separately rather than applying it as a style fix.

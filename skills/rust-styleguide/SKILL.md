---
name: rust-styleguide
description: Write, review, or refactor Rust (.rs) code and tests using the Google Rust Style Guide. Use for crate and module organization, imports, ownership and borrowing, public APIs and traits, errors, rustdoc, and formatting. Preserve the target project's API, edition, and minimum supported Rust version.
---

# Rust Style Guide

1. Inspect the affected crate, callers, and tests. Identify the build system:
   in a Cargo workspace, check the member manifest and inherited settings; in
   another build system, use its targets. Read the declared edition, minimum
   supported Rust version (MSRV), feature flags, and formatter or lint policy.
   The installed compiler is not evidence of the project's minimum version.
2. For a review, give findings without editing. For an implementation, make the
   smallest change that serves the caller. Use the [Google rules and their
   exceptions](references/google-guide.md) to distinguish a defect from a style
   preference. Follow explicit project rules first; a Chromium-only rule is
   not a reason to reorganize a Cargo workspace.
3. Trace who owns each value. Borrow data for inspection, move it when the
   callee keeps it, and clone only when an independent value is needed. Check
   whether a returned borrow would outlive its owner. Choose an iterator or an
   owned collection based on how the result is produced and consumed.
4. Review a public signature together with downstream uses and rustdoc. Type
   identity, exhaustive matches, error variants, panic conditions, and the
   timing of side effects are contracts. Do not change one just to quiet a
   lint. Document what callers cannot infer from the types.
5. Use the project's formatter and the narrowest existing compile, lint, test,
   or doctest checks that exercise the change. Match the relevant features and
   target rather than assuming default or all features. Do not install tools,
   switch to nightly, change dependencies, or reformat unrelated files for a
   style task. Report the location, consequence, and correction for findings;
   after edits say which checks ran and what they did not establish.

## Borrowing a field or transferring ownership

Let a caller inspect a note without copying it. Give the operation that
removes the note a different name: `take_note` transfers the existing string
and leaves the job with no note.

```rust
struct Job {
    note: Option<String>,
}

impl Job {
    fn note(&self) -> Option<&str> {
        self.note.as_deref()
    }

    fn take_note(&mut self) -> Option<String> {
        self.note.take()
    }
}

let mut job = Job {
    note: Some("retry after lunch".into()),
};
assert_eq!(job.note(), Some("retry after lunch"));
let note = job.take_note();
assert_eq!(job.note(), None);
assert_eq!(note.as_deref(), Some("retry after lunch"));
```

## Returning an iterator for single-pass callers

A caller that needs only the first rule can stop reading early; another can
collect all rules. Neither needs a copy of the text.

```rust
fn rules(text: &str) -> impl Iterator<Item = &str> {
    text.lines()
        .map(str::trim)
        .filter(|line| !line.is_empty() && !line.starts_with('#'))
}

assert_eq!(rules("# local rules\n\n  allow  \ndeny").next(), Some("allow"));
```

The results borrow `text`. Keep an owned result if it must outlive the input;
keep a vector if callers need random access. Changing an existing eager API to
an iterator can also defer errors or side effects.

## Distinguishing a missing setting from an invalid one

Use `FromStr` when callers should be able to use `parse()`. Here a batch size
must fit in a nonzero `u16`; the newtype keeps that restriction even after
parsing. An omitted setting selects the caller's default, but a malformed
setting should reach the caller as an error.

```rust
use std::num::{NonZeroU16, ParseIntError};
use std::str::FromStr;

#[derive(Debug, PartialEq, Eq)]
struct BatchSize(NonZeroU16);

impl FromStr for BatchSize {
    type Err = ParseIntError;

    fn from_str(text: &str) -> Result<Self, Self::Err> {
        text.parse().map(BatchSize)
    }
}

/// Returns `Ok(None)` if the setting is absent. A supplied value must parse
/// as an integer between 1 and 65535 inclusive, or parsing returns an error.
fn batch_size(setting: Option<&str>) -> Result<Option<BatchSize>, ParseIntError> {
    setting.map(str::parse).transpose()
}

assert_eq!(batch_size(None), Ok(None));
assert!(matches!(batch_size(Some("8")), Ok(Some(size)) if size.0.get() == 8));
assert!(batch_size(Some("0")).is_err());
```

`transpose()` carries the parse error through `Result`. Using `.ok()` instead
would make an invalid value indistinguishable from an absent one.

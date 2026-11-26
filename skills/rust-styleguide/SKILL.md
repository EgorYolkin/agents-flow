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

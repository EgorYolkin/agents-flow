---
name: go-styleguide
description: Write, review, and refactor Go (.go) code and tests using the Google Go Style Guide. Use for Go naming, gofmt, exported APIs and doc comments, error handling, receiver and interface design, or deciding whether a type parameter is justified. Preserve module compatibility and caller-visible behavior.
---

# Go Style Guide

1. Read the affected package, its callers and tests. Check the applicable
   `go.mod`, workspace, build tags, generated-file markers and existing CI
   commands. The locally installed compiler does not establish the minimum Go
   version. Leave generated output alone unless the task includes regeneration.
2. For a review, report findings without editing. For an implementation, fit
   the smallest useful change into the existing package. Read the
   [Google guidance and original examples](references/google-guide.md) for the
   decision at hand. Distinguish a bug from a Google convention and from a
   project preference; an explicit target-project requirement takes precedence.
3. Read new names as callers will: `checkpoint.Read`, not
   `checkpoint.ReadCheckpoint`. Use Go capitalization for exported and internal
   names, including constants. Don't rename exported symbols, change receiver
   method sets or alter serialized fields and tags as a style cleanup.
4. For a changed exported API, read its signature and doc comment together.
   Can the caller tell which inputs are valid, which results survive an error,
   who owns a resource and which errors can be recognized? Preserve those
   contracts, including intentional nil/empty distinctions and partial results.
5. Prefer a direct function for a stateless operation. Introduce a receiver
   when it owns data or enforces a rule across calls. Choose a small interface
   for behavior the consumer actually requires, or a type parameter for a
   relationship between actual types; neither is a default layer around a
   concrete implementation. See the [boundary examples](references/google-guide.md#choosing-the-boundary).
6. Handle failure where it occurs; keep the success path outside a terminating
   `if`. In touched code, this skill prefers one blank line between an exiting
   guard and a distinct success phase, and between a state update and the
   following return. Keep an operation beside its error check. This spacing is
   a project preference, not a `gofmt` or Google rule; follow the target's
   formatter and do not reorder effects to create blocks.
7. Use the project's Go formatter and relevant existing package tests or vet
   checks within the requested scope. Do not install linters, bump Go versions
   or reformat unrelated files. Report findings with a location, consequence
   and specific fix. After edits, name the checks run and any behavior they
   did not establish.

---
name: swift-styleguide
description: Write, review, and refactor Swift code using Google's Swift Style Guide with explicit project adaptations. Use for .swift files, Swift API naming, imports, declarations, optional handling, documentation, or Swift style cleanup, including SwiftUI and UIKit source changes. Apply when the request concerns Swift code even without the words style guide; do not trigger for generic prose, the Swift payment network, or another language's formatting.
---

# Swift Style Guide

Produce readable Swift while preserving the project's behavior, toolchain, and public contracts. Use the Google guide as a baseline and make adaptations visible.

## Workflow

1. Inspect the requested files and nearby code. Identify the Swift version, target platforms, package/Xcode configuration, formatter/linter settings, generated files, and existing tests. Read repository instructions before selecting a style profile.
2. Determine whether the request is review-only or authorizes edits. A review returns findings without changing files. For edits, limit changes to the requested scope and relevant dependencies; keep unrelated formatting out of the diff.
3. Read [the reference checklist](references/google-guide.md). Consult the linked upstream section for a disputed rule. Separate a sourced requirement, a project exception, and personal preference.
4. Preserve exported names, argument labels, serialization keys, Objective-C selectors, protocol witnesses, overload resolution, access control, and availability. A style preference does not authorize an API migration. Trace call sites before changing identifiers.
5. Make mechanical changes first. Treat changes to error handling, optional unwrapping, value/reference semantics, actor isolation, or ownership as behavior changes: require task justification and suitable tests rather than calling them formatting.
6. Use the repository's existing verification commands and configured formatter if available. Check the tool's current documentation before introducing syntax; use Context7 when available. Do not install tools, rewrite configuration, or invent a formatter's Google-compliance guarantee.
7. Inspect the final diff and report checks actually executed. If the Apple SDK, simulator, compiler, or dependencies are unavailable, identify the unverified scope precisely.

## Applying the baseline

Use the reference checklist for concrete style rules. Respect a deliberately established project convention unless the user requests migration. Record an intentional deviation once instead of repeatedly arguing about it in each file.

Keep modern Swift constructs supported by the project's compiler. The linked Google guide is an older source, so absence of concurrency, macros, result builders, or newer syntax is not a prohibition. Consult current language/API documentation when those features matter.

Avoid blind textual rewrites: semicolons and whitespace inside literals, multiline-string indentation, attributes, conditional compilation, and compiler directives may carry meaning. Do not change generated code; identify its generator when a fix is needed.

## Designing or reviewing an API

- Write a representative call before settling on the declaration. Read the
  receiver, base name, and argument labels together: can a caller tell what
  changes, what each argument means, and what the result represents?
- Make the signature and `///` comment agree on the caller's contract: what
  `nil` means, when an error is thrown, and whether a failed operation changes
  state. Document the behavior where callers find it, not just in the body.
- Start with an expression or function in the existing module. Add a type when
  operations share state or enforce an invariant. Ask what should happen when
  one caller assigns the value to another variable: independent progress or
  the same owner's state? Function length is not a reason to introduce a class.
- Use a generic constraint for an operation the implementation needs and a
  type relationship callers use. Introduce a protocol when a consumer needs
  a common capability, not as a counterpart to every concrete type.

See the [worked Swift examples](references/google-guide.md#worked-examples)
for call-site naming, copy behavior, and this project's blank-line preference
after early exits and between a state update and its return.

## Review and output

For each actionable finding, provide the file/location, observed issue, applicable rule or project contract, and suggested correction. Label behavior risks separately from cosmetic suggestions. Do not invent findings to fill a quota.

For edits, summarize changed files, relevant profile exceptions, validation performed, and remaining verification. For review-only work, explicitly state that no files were modified. Respond in the user's language while following the repository's language for code comments.

## Resources

- [Google guide checklist and provenance](references/google-guide.md): read before applying style rules.

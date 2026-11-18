---
name: typescript-styleguide
description: Write, review, and refactor TypeScript and TSX using an adapted Google TypeScript Style Guide. Use for TypeScript naming, imports and exports, types, classes, functions, documentation, and maintainability work, including framework components and agent extensions—even when the user asks only to clean up or review a .ts or .tsx file. Preserve project module, framework, and public API contracts. Do not use for JavaScript-only work or general prose editing.
---

# TypeScript Style Guide

Apply a predictable TypeScript style while preserving the program's behavior and integration contracts. Treat Google's guide as the baseline and record project-specific adaptations rather than silently changing the build system to match Google.

## Workflow

1. Inspect the relevant files and nearby conventions. Read repository instructions, package manifests, TypeScript configuration, formatter/linter configuration, exports and consumers. Identify runtime, module mode, framework and generated files.
2. Read [the rule reference](references/google-guide.md). Follow its links for disputed or nuanced rules; load only sections relevant to the change.
3. Determine the requested mode. For review or explanation, report findings without editing. For implementation or cleanup, make the smallest coherent patch that satisfies the request.
4. Apply rules in this order: correctness and public contracts, explicit project policy, applicable Google guidance, then discretionary readability improvements. Explain consequential conflicts. Do not invent project policy from one accidental formatting example.
5. Preserve runtime imports, import extensions, side-effect ordering, public exports, JSON field names and framework-required signatures. A rename or import conversion can change behavior even if it looks stylistic.
6. Use the project's existing formatter, lint and typecheck commands when available. Run tests appropriate to changed behavior. Inspect what each command executes before running it; do not install packages or execute lifecycle scripts merely to obtain a style verdict.
7. Inspect the final diff for unrelated changes, new suppressions, deleted tests and changed interfaces. Report what changed, which checks actually ran, and any unverified assumptions.

## Practical rules

- Start in the module that already owns the behavior. A standalone function
  needs neither a static utility class nor an interface for a future service.
  Introduce an instance when callers need distinct state with a rule to protect.
  Length alone is not a reason to add a layer.
- Use `const` for bindings that are not reassigned and `let` when reassignment is intentional. Preserve semantics when replacing legacy `var`, especially scope and hoisting.
- For an exported API, check a real call site: what inputs does it need, what
  does it return on absence or failure, and does it mutate anything? Annotate
  boundaries where inference would hide or weaken the contract; let the
  compiler infer obvious locals and contextual callback types.
- Accept a structural shape if only its fields matter. Use a type parameter
  when a caller needs a relationship, such as getting back the same element
  type it supplied. A type argument is not evidence about external data:
  accept `unknown` at an untyped boundary and narrow it at runtime.
  Don't substitute `any`, assertions or compiler suppressions for a check.
- Preserve the distinction between type-only imports and runtime values. Keep intentional side-effect imports and their ordering. Do not remove `.js` extensions or path aliases without checking the module resolver.
- Give new exports names a reader can understand at the import site. Prefer
  named exports for new unconstrained modules. Preserve existing default
  exports required by consumers or frameworks; changing them is a migration.
- Write JSDoc for callers of public exports: explain what the signature leaves
  out, such as side effects, ordering or failure. Use TypeScript, not JSDoc
  type annotations, to express types.
- In TSX, preserve the project's JSX runtime, component props, event timing
  and hook order. Keep straightforward expressions inline; don't extract a
  component or hook solely to shorten a function.
- As a project preference, use a blank line after a guard that exits and
  between a state change and the subsequent return when they are distinct
  steps. Keep the check next to the operation it governs. Follow the project's
  formatter rather than introducing a new rule for whitespace.

## Boundaries

The reference distinguishes upstream recommendations from this skill's adaptations. Google-specific toolchain assumptions are not universal requirements. Do not replace the project's formatter, enable new compiler flags, convert module systems, ban supported language features, or rewrite generated files as an incidental style fix.

Formatter success proves only that formatter's checks. It does not certify Google compliance, type safety, runtime correctness or security. A missing tool or unavailable dependency is an unperformed check, not a pass.

## Response

For a review, give actionable findings with file/line, applicable rule, consequence and suggested repair. Separate definite violations from optional preferences. If nothing material is found, say so.

For an edit, summarize changed files and meaningful decisions, then list checks and results. State project adaptations when they affect the outcome. Keep routine formatting details brief.

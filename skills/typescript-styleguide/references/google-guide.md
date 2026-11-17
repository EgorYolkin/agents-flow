# Google TypeScript rules and project adaptations

## Provenance

This is an independently organized paraphrase and adaptation of the Google TypeScript Style Guide, maintained by Google and contributors. Consult the source for the full normative text; examples alone are not additional rules.

- [Pinned upstream guide](https://github.com/google/styleguide/blob/a9c5f82b19811f1552d73df384a9f9d7c75ca16e/tsguide.md)
- [Published guide](https://google.github.io/styleguide/tsguide.html)
- Reviewed: 2026-11-17. Upstream revision: `a9c5f82b19811f1552d73df384a9f9d7c75ca16e`.
- [Upstream license notice](https://github.com/google/styleguide/blob/a9c5f82b19811f1552d73df384a9f9d7c75ca16e/README.md#licensing): guide text CC BY 3.0; upstream code examples Apache 2.0. This reference paraphrases the guide and adds the explicitly identified adaptations below; it does not reproduce its code examples.

## Source-grounded rules

| Concern | Guidance | Upstream section |
|---|---|---|
| Imports | Use appropriate named/namespace imports; retain external defaults and intentional side-effect loads where required. | [Imports](https://google.github.io/styleguide/tsguide.html#imports) |
| Type imports | Type-only syntax is available for type uses; runtime values need ordinary imports. | [Import type](https://google.github.io/styleguide/tsguide.html#import-type) |
| Variables | Prefer const/let to var and one declaration per statement. | [Local declarations](https://google.github.io/styleguide/tsguide.html#local-variable-declarations) |
| Object construction | Prefer literals to generic Array/Object constructors when semantics permit. | [Arrays](https://google.github.io/styleguide/tsguide.html#array-literals), [objects](https://google.github.io/styleguide/tsguide.html#object-literals) |
| Functions | Prefer focused functions; around forty lines prompts consideration, without a hard cap. | [Function length](https://google.github.io/styleguide/tsguide.html#function-length) |
| Types | Use useful inference, specific types and unknown rather than unchecked any where appropriate. | [Type system](https://google.github.io/styleguide/tsguide.html#type-system) |
| Documentation | Explain meaningful contracts and changes; avoid comments that restate syntax. | [Comments](https://google.github.io/styleguide/tsguide.html#comments-documentation) |
| Scope | Keep opportunistic style churn separate; generated source is largely exempt. | [Policies](https://google.github.io/styleguide/tsguide.html#policies) |

For naming, control flow, exceptions or classes, inspect the matching source section before claiming a nuanced requirement. Do not infer a general ban from a single example.

## Adaptations for projects outside Google

These are deliberate integration policies, not claims that Google prescribes them:

1. **Honor existing contracts.** Keep public export names, serialized keys, module resolution, import suffixes, framework conventions and supported runtime features. Propose a migration separately if a Google preference conflicts.
2. **Keep one existing formatter authoritative.** Do not enforce whitespace from upstream snippets over an established project formatter. If no formatter is configured, use a consistent local style and report that automated formatting was not validated.
3. **Preserve type-test intent.** Google discourages compiler suppressions and treats test exceptions narrowly. Retain an existing documented negative-type-test `@ts-expect-error` where it is the test oracle; do not delete the test to achieve style compliance. New production suppressions need a reasoned exception rather than automatic insertion.
4. **Do not import ecosystem restrictions blindly.** Rules concerning private fields, tooling or framework patterns may reflect Google's environment. Establish applicability before replacing supported code merely for stylistic conformity.
5. **Review-only is read-only.** Present a patch suggestion or explanation without mutating files when that is the user's request.
6. **Separate style from behavior.** Use a behavior test if a refactor changes control flow or data handling. Do not claim a spelling or formatting check proves runtime behavior.

## Import conversion caution

The official TypeScript documentation states that type-only imports are erased. With `verbatimModuleSyntax`, unmarked imports/exports are preserved while type-marked forms are removed. A type-only rewrite can therefore remove required runtime initialization. Inspect side effects and preserve a deliberate side-effect import when needed.

[TypeScript module syntax](https://www.typescriptlang.org/tsconfig/verbatimModuleSyntax.html). Documentation checked through Context7 `/microsoft/typescript-website` on 2026-11-17. This explains semantics; it does not instruct the agent to enable that compiler option.

## Review questions

- Is a proposed rename internal, or can consumers observe it?
- Does import cleanup preserve evaluation order and runtime registration?
- Does replacing var affect scope or hoisting?
- Does a type change actually narrow the contract, or merely hide an error?
- Is the recommendation a source rule, a project adaptation or a preference?
- Can the requested outcome be achieved without unrelated churn?

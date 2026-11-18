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
| Types | Infer trivial local types. Return annotations can clarify a boundary or satisfy project policy; Google does not require one on every function. | [Inference](https://google.github.io/styleguide/tsguide.html#type-inference), [return types](https://google.github.io/styleguide/tsguide.html#return-types) |
| Object shapes and generics | Use interfaces for named structural object shapes, not classes merely listing fields. Avoid APIs whose type parameter occurs only in the result. | [Structural types](https://google.github.io/styleguide/tsguide.html#use-structural-types), [return-only generics](https://google.github.io/styleguide/tsguide.html#return-type-only-generics) |
| Runtime checks | Use `unknown` for an unknown value and narrow it before use. Neither `as` nor `!` checks a value at runtime. | [Assertions](https://google.github.io/styleguide/tsguide.html#type-and-non-nullability-assertions), [unknown](https://google.github.io/styleguide/tsguide.html#any-unknown) |
| Exports | Use named exports, expose only what other modules need, and export individual functions rather than static classes for namespacing. | [Exports](https://google.github.io/styleguide/tsguide.html#exports), [container classes](https://google.github.io/styleguide/tsguide.html#container-classes) |
| Names | Use `UpperCamelCase` for types and TSX components, `lowerCamelCase` for ordinary functions and parameters. Short local names can work in a tiny scope; that exception does not extend to exported API parameters. | [Names](https://google.github.io/styleguide/tsguide.html#descriptive-names), [identifier categories](https://google.github.io/styleguide/tsguide.html#naming-rules-by-identifier-type) |
| Documentation | Document top-level exports for callers, except tooling-only exports. Explain non-obvious parameters, results and members without repeating TS types in tags. | [Export documentation](https://google.github.io/styleguide/tsguide.html#document-all-top-level-exports-of-modules), [JSDoc types](https://google.github.io/styleguide/tsguide.html#jsdoc-type-annotations) |
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

### Original examples: design for the caller

The following examples are local, not Google samples. Start with a function in
the existing module. Introduce a new type only for a contract the caller or
implementation actually uses.

#### Keep the matched element's type

```ts
interface Tagged {
  readonly tag: string;
}

/** Returns the first matching item itself, or undefined if none matches. */
export function findByTag<T extends Tagged>(
  items: readonly T[],
  tag: string,
): T | undefined {
  return items.find(item => item.tag === tag);
}

const notes = [{tag: 'work', title: 'Handoff'}];
const title = findByTag(notes, 'work')?.title; // string | undefined
```

The constraint says what the implementation reads; the repeated `T` preserves
the caller's element type. A signature of
`findByTag(items: readonly Tagged[], tag: string): Tagged | undefined`
would accept `notes` but hide `title` on the result. Conversely, a predicate
`hasTag(item: Tagged, tag: string): boolean` needs no type parameter: no
caller-specific type comes back. Don't promise `T` and then construct just a
`{tag}` object. See the [TypeScript handbook on constrained values](https://www.typescriptlang.org/docs/handbook/2/functions.html#working-with-constrained-values).

#### Check the value before changing state

```ts
/** Adds a new nonempty string verbatim. Returns false without changing tags otherwise. */
export function addTag(tags: Set<string>, candidate: unknown): boolean {
  if (typeof candidate !== 'string' || candidate === '' || tags.has(candidate)) {
    return false;
  }

  tags.add(candidate);

  return true;
}
```

`tags.add(candidate as string)` alone compiles but lets a number into the set.
`parse<T>(text: string): T` backed only by `JSON.parse` has the same flaw:
the caller chooses `T`, but the data never proved it. Check the fields the
consumer needs, or use the project's existing decoder. Don't add a schema
library for style. Here a caller-owned set and a function suffice; a dedicated
class would only be justified if an owner needed to control changes to it.
The blank lines separate rejection, mutation and result for the reader; that
spacing is a project preference, not a Google rule.

#### Name a TSX callback by what the component delivers

In a project with button JSX and click handlers, the parent needs the selected
tag, not a DOM event. Keep that choice visible at the call site:

```tsx
interface TagButtonProps {
  readonly tag: string;
  readonly onSelectTag: (tag: string) => void;
}

/** Reports the displayed tag when the button is activated. */
export function TagButton({tag, onSelectTag}: TagButtonProps) {
  return <button type="button" onClick={() => onSelectTag(tag)}>{tag}</button>;
}
```

`onClick={onSelectTag(tag)}` invokes the callback during rendering, not on
activation. Preserve the JSX runtime, required exports and event types of the
actual framework. Don't rename a published prop or move a hook below a
conditional return to match the shape of this example.

## Import conversion caution

With `verbatimModuleSyntax`, `import type {Tag} from './tags.js'` disappears.
`import {type Tag} from './tags.js'` instead leaves an empty import that still
loads the module. Before converting either form, check whether evaluation
registers anything. If registration is required, preserve an explicit
`import './tags.js'` in the correct order. A class used with `instanceof` is
a runtime value and needs an ordinary value import.

[TypeScript module syntax](https://www.typescriptlang.org/tsconfig/verbatimModuleSyntax.html). Documentation checked through Context7 `/microsoft/typescript-website` on 2026-11-17. This explains semantics; it does not instruct the agent to enable that compiler option.

## Review questions

- Is a proposed rename internal, or can consumers observe it?
- Does import cleanup preserve evaluation order and runtime registration?
- Does replacing var affect scope or hoisting?
- Does a type change actually narrow the contract, or merely hide an error?
- Is the recommendation a source rule, a project adaptation or a preference?
- Can the requested outcome be achieved without unrelated churn?

---
name: html-css-styleguide
description: Write, review, and refactor HTML and CSS using Google HTML/CSS style guidance while preserving rendering, accessibility, selectors, and project conventions. Use this skill for HTML templates, CSS stylesheets, semantic markup, style cleanup, and HTML/CSS review, including embedded markup or styles in components. Use framework-specific guidance alongside it for JSX, Vue, Angular, Sass, or other dialects; do not treat it as a general visual-design, JavaScript, or prose-writing skill.
---

# HTML/CSS Style Guide

Produce maintainable markup and styles with small, behavior-preserving changes. Treat the Google guide as the baseline and document intentional project adaptations.

## Workflow

1. Inspect the requested files, nearby examples, project instructions, formatter/linter configuration, and build or template system. Identify source files versus generated output, target browsers, and the actual markup/CSS dialect.
2. Read [the Google guide reference](references/google-guide.md). Follow its source links when an uncommon rule matters. Classify a proposed change as an upstream rule, an optional recommendation, or a project adaptation.
3. Determine the requested operation. For review or explanation, report findings without editing. For creation or fixes, make the smallest coherent patch within the requested scope. Resolve harmless choices from repository conventions; ask only when an unresolved choice materially changes behavior or the public contract.
4. Check the compatibility boundaries below before applying cosmetic changes. Existing explicit project conventions take precedence over this default profile. Do not silently rewrite configuration to make the checks pass.
5. Use existing local checks appropriate to the files. Inspect the project's documented commands before invoking them. If CLI or framework syntax is uncertain, consult current documentation, preferring Context7 when available. Do not install tools or upload proprietary markup to an online validator merely to satisfy this skill.
6. Inspect the final diff. Check references and changed output where feasible. Report which checks actually ran, which were unavailable, and what remains unverified. Formatting success is not proof of semantic, accessibility, or visual correctness.

## Compatibility boundaries

These are application safeguards for this skill, not additional Google mandates.

- Preserve IDs, classes, data attributes, fragment URLs, analytics hooks, and test selectors unless all consumers are in scope and updated together. A naming preference alone does not justify a public selector migration.
- Preserve case-sensitive paths, strings, SVG names and attributes, custom properties, and framework identifiers. Apply lowercase conventions only where the language and consumers permit them.
- Keep native interactive semantics, labels, accessible names, focus behavior, ARIA relationships, and keyboard operation. Do not invent image descriptions without knowing the image's purpose.
- Distinguish complete documents from partials. Do not insert document wrappers into a fragment or turn framework markup into plain HTML. Retain framework bindings and required delimiters.
- Preserve intentional whitespace between inline elements, in preformatted content, and in templates. A prettier source layout can change rendered text.
- Preserve the cascade: declaration order, duplicate fallback declarations, specificity, layers, source order, and shorthand reset effects. Do not sort or collapse declarations without checking equivalence.
- Keep non-default script types, including modules and data scripts. Do not remove attributes because they superficially resemble redundant HTML defaults.
- Retain established utility classes, CSS Modules names, BEM conventions, and component-local styling unless migration is explicitly requested. Mark these as project adaptations rather than claiming exact Google compliance.

## Review and delivery

Prioritize correctness and accessibility defects, then concrete maintainability issues. Separate required fixes from optional style suggestions; avoid blocking a patch on personal taste.

For each material finding, give the file/location, consequence, applicable source rule or project convention, and a narrow correction. For changes, summarize edited files, preserved contracts, checks performed, and remaining limitations. If no actionable findings exist, say so without inventing work.

## Resources

- [Google guide reference and attribution](references/google-guide.md): baseline rules and source provenance.

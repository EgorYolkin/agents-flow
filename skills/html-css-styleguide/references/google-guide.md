# Google HTML/CSS baseline

Checked 2026-11-17 against [Google HTML/CSS Style Guide](https://github.com/google/styleguide/blob/a9c5f82b19811f1552d73df384a9f9d7c75ca16e/htmlcssguide.md), revision `a9c5f82b19811f1552d73df384a9f9d7c75ca16e`. The [published guide](https://google.github.io/styleguide/htmlcssguide.html) can change.

## Selected upstream guidance

- Use HTTPS for embedded resources when supported; use UTF-8 without a BOM.
- Use two-space indentation, remove trailing whitespace, and prefer lowercase syntax.
- Give complete HTML documents a suitable doctype. Prefer valid, semantic HTML and meaningful alternatives for multimedia; decorative images can use empty alternative text.
- Separate structure, presentation, and behavior where appropriate.
- Quote HTML attribute values with double quotes. Do not remove module script types.
- Give classes meaningful, concise names; use hyphens between words. Avoid unnecessary IDs and excessive selector qualification.
- Explain non-obvious intent in comments.
- Omitting optional HTML tags, wrapping HTML lines, and adding application prefixes are optional. HTML has no mandated column limit in this guide.

Use source section anchors such as `#Semantics`, `#Multimedia_Fallback`, `#Optional_Tags`, `#HTML_Line-Wrapping`, and `#ID_and_Class_Naming` to verify a specific finding.

## Scope and adaptations

The skill's compatibility safeguards take priority over mechanical rewriting. Explicit project exceptions should identify the relevant rule and reason. A formatter's output is not certification of the complete guide.

## Attribution

Adapted and condensed from Google Style Guides, maintained by Google contributors. Guide text is licensed under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/); upstream code examples use Apache 2.0, as stated in the [repository licensing section](https://github.com/google/styleguide#licensing). This package paraphrases selected guidance and adds an independent workflow. No Google endorsement is implied.

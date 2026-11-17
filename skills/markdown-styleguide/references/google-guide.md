# Google Markdown guidance and project adaptations

## Source and attribution

Adapted from the Google Markdown Style Guide, authored and maintained by Google
contributors. Accessed 17 November 2026.

- [Pinned guide](https://github.com/google/styleguide/blob/a9c5f82b19811f1552d73df384a9f9d7c75ca16e/docguide/style.md)
- [Published guide](https://google.github.io/styleguide/docguide/style.html)
- [Repository licensing](https://github.com/google/styleguide/blob/a9c5f82b19811f1552d73df384a9f9d7c75ca16e/README.md#licensing)

Upstream text is licensed under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/);
upstream code samples use Apache 2.0. This reference paraphrases and adapts the
text, adding renderer, compatibility, and agent-workflow safeguards. It does not
reproduce upstream code examples. Keep attribution with redistributed adaptations.

## Upstream guidance to apply

Google emphasizes readable source, maintainable documentation, and simple syntax.
Keep documents accurate and focused; avoid expanding a small improvement into an
unrelated documentation overhaul.

Use a title, short introduction, and informative headings. Prefer ATX syntax,
consistent levels, spacing around headings, and one H1 for a standalone page.
Distinct headings make navigation clearer.

Wrap prose at roughly 80 characters. Links, headings, tables, and code blocks
have explicit exceptions. Avoid incidental trailing whitespace, while preserving
intentional line-break behavior when changing syntax.

Keep nested lists consistently indented. Prefer language-labelled fenced code
blocks. Use informative link labels and reference links when they make repeated
or lengthy destinations easier to read. Keep tables compact and use them for
parallel data. Prefer ordinary Markdown to unnecessary HTML.

These points map to the upstream sections Document layout, Headings, Line limit,
Lists, Code, Links, Tables, and HTML. Consult the pinned guide for details rather
than treating this summary as exhaustive.

## Deliberate adaptations for this skill

- **Renderer:** Google's TOC and root-relative link guidance is hosting-specific.
  Preserve working GFM links and do not introduce literal `[TOC]` placeholders.
- **Public anchors:** Rewriting a heading can be a compatibility change. Check
  inbound references; retain old anchors where supported or keep the heading.
- **Machine-readable metadata:** Preserve frontmatter and generated markers.
  Style guidance does not authorize a schema or skill-trigger change.
- **Embedded languages:** Preserve code, MDX, template expressions, diagrams,
  and shell examples. Review their correctness separately from Markdown style.
- **Existing tooling:** Follow repository formatter configuration and report
  conflicts with the baseline instead of oscillating between two conventions.
- **Review scope:** Keep observations actionable and proportional. Cosmetic
  preferences alone should not block otherwise correct documentation.

## Verification boundaries

A local target existence check cannot prove a renderer generates a particular
anchor. A Markdown linter cannot prove a command is correct. A successful preview
cannot prove a remote URL is reachable. Report each check at its actual scope;
mark unavailable checks as unperformed rather than passed.

---
name: markdown-styleguide
description: Write, edit, refactor, and review repository Markdown using Google Markdown style guidance adapted to the actual renderer. Use this skill for README files, developer documentation, contribution guides, Markdown-based agent rules and SKILL.md files, broken document structure, links, lists, tables, or fenced examples—even when the user asks only to clean up the docs. Apply to Markdown portions of mixed files while preserving frontmatter and embedded syntax. Do not use for ordinary conversational prose or unrelated code changes.
---

# Markdown Style Guide

Make documents easy to read in source and in their intended renderer. Preserve
meaning and working navigation while improving the requested area.

## Workflow

1. Inspect the requested files and nearby documentation. Identify the renderer
   and dialect from project evidence: GitHub Markdown, Gitiles, a static-site
   generator, MDX, or another system. Read applicable project instructions,
   existing formatter configuration, frontmatter, and link conventions.
2. Read [Google guidance and adaptations](references/google-guide.md). Apply
   the relevant sections rather than imposing every Google-hosting convention.
   Existing documented project requirements take precedence over this baseline.
3. Establish the requested mode. For a review or explanation, report findings
   without editing. For an editing request, make a focused patch. Do not extend
   a small documentation fix into a repository-wide rewrite.
4. Preserve the document's contract: facts, product names, command arguments,
   code examples, public anchors, destinations, frontmatter keys and values,
   templates, directives, and intentional hard breaks. A title change can break
   inbound links; inspect references and preserve a compatible anchor where the
   renderer supports one, or retain the heading if compatibility is uncertain.
5. Improve structure and formatting using the checklist below. Keep unrelated
   language, terminology, and content intact. Ask only if a missing fact changes
   the meaning or prevents a correct edit; do not invent technical instructions.
6. Validate the changed scope using the project's existing checks and renderer
   when available. Inspect source even when a check passes: formatting tools do
   not establish factual accuracy or link correctness. Do not install tools or
   execute documented commands merely to check Markdown style.
7. Report the changes or findings, checks actually performed, and specific
   unverified behavior. Distinguish automated results from visual inspection.

## Editing checklist

- Use a clear title and introduction, then descriptive headings with consistent
  levels. Prefer ATX headings and blank lines around block structures.
- Use a single H1 for a standalone document. Preserve partials or site templates
  that intentionally obtain their title from frontmatter or an enclosing page.
- Keep lists readable and correctly nested. Preserve ordered steps and task-list
  states; do not change an executable example into a list by adjusting indentation.
- Prefer fenced code blocks with an accurate language label. Use `text` for
  literal output when no programming language applies. Choose a long enough
  outer fence when documenting Markdown that itself contains fences.
- Wrap ordinary prose near 80 columns when consistent with the project. Do not
  split URLs, headings, tables, or runnable code to satisfy a line-length rule.
- Use informative link text. Check local targets and fragments against repository
  files and renderer behavior. Preserve query strings and percent-encoding.
- Use tables for genuinely comparable data; keep cells concise. Preserve pipes
  and backticks inside code according to the target dialect.
- Prefer Markdown over decorative HTML. Retain necessary supported HTML such as
  compatibility anchors, details blocks, or accessibility markup.
- Retain meaningful alt text. Do not invent descriptions of images not inspected.
- Preserve YAML frontmatter boundaries and semantics, especially `name` and
  `description` in skills. Editing a skill's prose must not silently change its
  activation scope, permissions, or behavioral requirements.

## Renderer and safety boundaries

Google's `[TOC]` directive and link-path preferences assume particular hosting.
Do not insert `[TOC]` into GitHub Markdown or rewrite relative links into
root-relative links without confirming destination resolution. Use the project's
existing TOC mechanism, or leave it absent for short documents.

For MDX or templated documents, preserve components and expressions; this skill
covers their Markdown portions, not framework refactors. Do not remove supported
extensions to satisfy a generic Markdown preference.

Code fences are examples, not commands to execute. Never source scripts, contact
production services, or expose secrets during a formatting task. If an example
appears incorrect or unsafe, describe the issue separately unless correcting its
behavior is within the user's request.

## Review and final response

For each actionable finding, name the file and location, explain the reader or
rendering impact, and propose a concrete correction. Label project-specific
preferences as such; cosmetic suggestions should not masquerade as correctness
failures. Avoid repeating issues already covered by a configured formatter.

After an edit, summarize files changed, meaningful choices, validation and its
limits. If no actionable issue exists, say so. Do not claim complete conformance
to the Google guide or successful rendering without evidence.

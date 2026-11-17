---
name: init
description: Create or carefully update a repository's AGENTS.md contributor guide from inspected project evidence. Use when the user asks to initialize repository instructions, generate AGENTS.md, document contributor conventions, or refresh agent onboarding for a codebase. This skill initializes documentation, not an application, Git repository, dependency environment, or deployment.
---

# Repository Guide Initialization

Generate `AGENTS.md` with the exact title `# Repository Guidelines`. Produce
clear, concise, actionable instructions specific to the inspected repository.
Aim for 200–400 words in the generated document, not in this skill.

## Inspect before writing

1. Identify the intended repository root and requested scope. If the workspace
   contains several projects and the target is ambiguous, resolve it before
   writing. Read applicable ancestor and repository instructions first.
2. Inspect any existing `AGENTS.md`, case variants, and nested instruction files.
   Resolve symlinks and case-insensitive paths before writing so an existing
   guide is not accidentally duplicated or edited through an unexpected target.
3. Inspect the working-tree status, README, relevant documentation, directory
   layout, manifests, build/task files, CI, formatting configuration, and tests.
   Read representative files rather than every dependency or generated asset.
4. Inspect a small sample of recent Git commit subjects and any contribution
   guide or PR template. If history is unavailable, use the documented policy.
   A single observed commit is an example, not proof of a mandatory convention.
5. Keep a small evidence map while drafting: each command, path, convention,
   and requirement must trace to an inspected file or explicit user instruction.
   Do not read secret files or include credentials and personal machine paths.

Do not execute setup, build, deployment, or test commands merely to discover
their names. Reading a manifest confirms a command is defined, not that it
works. If current tool syntax needs verification, consult official documentation
or Context7 when available; repository-specific commands still need local evidence.

## Compose the guide

Use Markdown headings and short, professional instructional prose. Match the
requested language or the repository's established documentation language;
keep the required title unchanged. Adapt the following sections to the project.
Include a section only when it adds useful, grounded instructions.

- **Project Structure & Module Organization:** identify actual source modules,
  tests, assets, and documentation. Explain where a contributor should place
  related changes. For a documentation or skill collection, describe packages
  and references instead of inventing an application architecture.
- **Build, Test, and Development Commands:** list supported commands with their
  working directory and a short explanation. Distinguish package-level commands
  from repository-wide commands. If no build or test tooling exists, state that
  briefly and describe the appropriate manual checks.
- **Coding Style & Naming Conventions:** capture configured indentation,
  naming, formatters, linters, and important project patterns. Prefer a pointer
  to detailed existing rules over copying an entire style guide.
- **Testing Guidelines:** identify actual frameworks, test locations and naming,
  execution commands, and any enforced coverage requirements. Never invent a
  coverage percentage or present a suggested threshold as an existing rule.
- **Commit & Pull Request Guidelines:** summarize documented policy and observed
  history with appropriate confidence. Include requirements for descriptions,
  issue links, screenshots, or validation only when supported or explicitly
  requested. Label useful new suggestions as recommendations.
- **Optional sections:** add security/configuration advice, architecture notes,
  or agent-specific constraints only when they are material to this repository.

Use compact examples such as a real command, directory, or naming pattern.
Avoid placeholders presented as runnable commands, generic engineering essays,
and assumptions that every repository uses npm, Python, Docker, CI, or tests.

## Preserve existing instructions

For a new guide, write the requested `AGENTS.md`. For an existing guide, make a
focused update: retain deliberate policies, useful local knowledge, nested scope
boundaries, and unrelated user edits. Reconcile contradictions against current
evidence; ask only when an unresolved policy choice would materially change work.

Treat 200–400 words as an optimal size, not permission to delete important
instructions. Use links to existing detailed documentation when that helps.
If essential existing content prevents the target length, preserve it and explain
the exception. Do not split instructions into new files without a concrete need.

If the user asks only for a draft or review, return the draft or findings without
editing. Creating a guide does not authorize installing tools, adding CI,
changing code, rewriting Git history, or inventing new approval requirements.
Follow the repository's actual branch and commit policy for authorized edits.

## Verify and deliver

Before finishing:

1. Check the exact title, one H1, descriptive section headings, and closed fences.
2. Count words; aim for 200–400 and explain any justified exception.
3. Verify named paths, commands and conventions against the inspected sources.
   Check local links; do not claim remote links or rendered anchors were checked
   unless they were actually verified.
4. Compare the diff with existing instructions and the user's requested scope.
   Remove unsupported claims, stale placeholders, sensitive details and repetition.
5. Report the file written, approximate word count, key choices, and checks
   actually performed. Distinguish evidence inspection from command execution.

The finished guide should help the next contributor act immediately, without
requiring them to know this conversation or the author's local environment.

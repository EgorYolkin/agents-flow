---
name: init
description: Create or carefully update the target project's AGENTS.md and GIT_WORKFLOW.md for agent onboarding. Use for repository instructions, contributor conventions, or an onboarding refresh. Inspect project tooling and Git state without changing Git. Drafts and reviews are read-only.
---

# Project Initialization for Agents

For authorized onboarding, **both files are required in the target project
root**. Create either missing file; update existing files only as needed:

- `AGENTS.md`: use the exact title `# Repository Guidelines`, aim for 200–400
  words, and link to `GIT_WORKFLOW.md` instead of duplicating its rules.
- `GIT_WORKFLOW.md`: document the project's Git policy or the absence of an
  established policy. This file is required even when Git is absent.

These are the only files `init` may write. For a draft or review, return the
draft or findings in chat without editing. The bundled
[workflow example](GIT_WORKFLOW_EXAMPLE.md) illustrates structure and style;
it is not an active policy or a substitute for the project's file.

## Inspect before writing

1. Identify the intended repository root and requested scope. If the workspace
   contains several projects and the target is ambiguous, resolve it before
   writing. Read applicable ancestor and repository instructions first.
2. Inspect both root guides, case variants, and nested instruction files.
   Resolve symlinks and case-insensitive paths before writing; do not duplicate
   a guide or edit an unexpected target. Preserve inherited and scoped rules.
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

## Establish Git state and policy

Determine whether the target belongs to a repository, including an ancestor
repository or linked worktree. An unborn HEAD means there is no history yet,
not that the repository is absent. Distinguish an absent repository from
missing Git tooling or inaccessible state; report what the evidence supports.
Inspect Git read-only. Do not run `git init`, switch branches, stage, commit,
or otherwise change Git state. Creating a repository is a separate task that
requires its own authorization.

Use existing workflow and contributor instructions first. Distinguish
documented requirements, observed conventions, and recommendations; do not
promote a recommendation to policy. Only if the user explicitly requests
their own Git rules, load the current `git-guide` through the active harness
as a policy source, not a workflow to execute. If unavailable, finish
independent inspection and report the missing source as a blocker rather
than inventing rules. Ask for its location or the rules themselves.

## Compose the guide

In `AGENTS.md`, instruct contributors to load `git-guide` before every
significant code change, including work started after onboarding, and link to
the project's `GIT_WORKFLOW.md`. Do not copy the skill's operational policy.

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
- **Git & Contribution Workflow:** link to the target `GIT_WORKFLOW.md` and
  require reading it before Git operations. Keep detailed branch, commit,
  validation, and publication policy there, not duplicated in `AGENTS.md`.
  Record supported PR requirements without inventing mandatory issue links.
- **Optional sections:** add security/configuration advice, architecture notes,
  or agent-specific constraints only when they are material to this repository.

Use compact examples such as a real command, directory, or naming pattern.
Avoid placeholders presented as runnable commands, generic engineering essays,
and assumptions that every repository uses npm, Python, Docker, CI, or tests.

## Preserve existing instructions

Retain deliberate policies, useful local knowledge, nested scope boundaries,
and unrelated user edits in existing guides. Reconcile contradictions against
current evidence; ask only when an unresolved policy choice would materially
change work.

Treat 200–400 words as an optimal size, not permission to delete important
instructions. Use links to existing detailed documentation when that helps.
If essential existing content prevents the target length, preserve it and explain
the exception. Do not split instructions into additional files.

## Verify and deliver

For authorized onboarding, open **both** `AGENTS.md` and `GIT_WORKFLOW.md`
from the target project root. Resolve the link from `AGENTS.md` and verify it
points to that exact `GIT_WORKFLOW.md`, not an example or an inherited guide.
If either file is missing or unreadable, or the link does not resolve to it,
fix the issue before reporting success. If blocked, report initialization as
incomplete, naming the affected path and the specific blocker.

For the written guides (or the proposed text in a draft):

1. Check `AGENTS.md` for the exact title; check both guides for one H1 each,
   descriptive headings, and closed fences.
2. Count words in `AGENTS.md`; aim for 200–400 and explain any justified exception.
3. Verify named paths, commands and conventions against the inspected sources.
   Check local links; do not claim remote links or rendered anchors were checked
   unless they were actually verified.
4. Compare the changes with existing instructions and the user's requested scope.
   Remove unsupported claims, stale placeholders, sensitive details and repetition.
5. Check that workflow policies match the evidence or explicitly requested
   rules and that existing customizations remain.
6. Report files created, updated, or retained, approximate `AGENTS.md` word
   count, observed Git state, policy sources, checks performed, and blockers.
   Distinguish inspected commands from executed checks.

The finished guide should help the next contributor act immediately, without
requiring them to know this conversation or the author's local environment.

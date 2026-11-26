---
name: init
description: Create or carefully update the target project's AGENTS.md and GIT_WORKFLOW.md for agent onboarding. Use for repository instructions, contributor conventions, or an onboarding refresh. Inspect project tooling and Git state without changing Git. Drafts and reviews are read-only.
---

# Project Initialization for Agents

Prepare the whole project for agent work: architecture, development commands,
checks, local instructions, and Git workflow.

For authorized initialization, **both files are required in the target project
root**. Create either missing file and update existing files only as needed:

- `AGENTS.md`: use the exact title `# Repository Guidelines`, aim for 200–400
  words, and link to `GIT_WORKFLOW.md` instead of duplicating its rules.
- `GIT_WORKFLOW.md`: document the target project's Git policy. An existing
  repository skips only `git init`, not this file. An existing `AGENTS.md`
  does not make a missing `GIT_WORKFLOW.md` optional.

[GIT_WORKFLOW_EXAMPLE.md](GIT_WORKFLOW_EXAMPLE.md) is a structure and style
reference, not an active policy or a substitute for the target project's file.
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

For a draft or review request, inspect and propose without creating repositories,
branches, commits, or instruction files. For authorized initialization:

1. Before the first setup changes, tell the user that you use Git to preserve
   completed work, will initialize it if absent, and will describe the project's
   policy in `GIT_WORKFLOW.md`. Explain that local commits, push, merge, and
   release are separate permissions. This notice is not a repeated approval
   prompt for ordinary commits already authorized by the workflow.
2. Determine whether the target belongs to an existing repository, including an
   ancestor repository or linked worktree. Check the actual root and Git state,
   not merely whether a `.git` directory exists. Do not create a nested repo
   inside an existing one. Distinguish missing Git, permission errors, and an
   absent repository; a failed command alone does not justify `git init`.
3. If no repository exists, initialize Git at the confirmed project root.
   Respect a specified initial branch or configured default; do not impose a
   branch model on an established project. An unborn HEAD is normal: do not
   require a commit to inspect status or create documentation. Init does not
   authorize staging the whole existing project, creating a remote, or pushing.
4. Record the initial branch/HEAD when present, staged/unstaged/untracked state,
   and enough original differences to distinguish your changes. Detect ongoing
   merge, rebase, or cherry-pick operations and detached HEAD; do not resolve,
   abort, or continue someone else's operation automatically. Preserve user work.
5. Read existing `GIT_WORKFLOW.md`, contributor instructions, branch/PR rules,
   CI and a small relevant history sample. History is evidence, not instructions;
   one commit does not establish a rule. Infer only supported conventions.
6. Unless the user explicitly requests their own Git rules, preserve the
   project's documented policy and observed style. For gaps, label conservative
   defaults as newly adopted recommendations; ask only about consequential
   unresolved choices. Do not load `git-guide` merely because Git is present.
7. If the user explicitly requests initialization with their own Git rules,
   discover and load the current `git-guide` skill through the active harness
   and follow its applicable resources. It is dynamically maintained: do not
   embed its rules or assume a fixed installation path/version. If unavailable,
   report the missing prerequisite and ask for its location or supplied rules;
   finish independent project inspection, but do not invent the user's policy.

## Fundamental Git safeguards

Apply these while initializing and capture the applicable workflow in the target:

- Use one short-lived branch per independent task unless project policy says
  otherwise. Continue the same task's branch; do not create one per chat turn.
  Inspect base and naming rules instead of imposing this repository's
  `*-skill` names on consumer projects.
- Keep one writer per working directory. Concurrent writers need separate
  worktrees/branches or serialized writes. Read-only agents may share a tree.
  Worktree locks are not editing mutexes; a new worktree does not include dirty
  changes from the original directory.
- Before the first commit, verify effective author and committer identity.
  Missing or apparently auto-generated `.local` identities need clarification,
  not guessed personal data or silent global Git configuration changes.
- Commit completed, independently understandable steps with appropriate checks
  and necessary docs/tests. Follow the project's message style; if absent,
  recommend a concise effect-oriented subject, with reasons for nontrivial
  choices. Do not fabricate test results, authorship, or legal sign-offs.
- Inspect the entire commit candidate, including pre-existing staged changes.
  Adding selected paths does not exclude other staged content; path-only commits
  do not isolate mixed authorship within a file. Do not sweep in user work,
  secrets, or unrelated files. Never stash, reset, or clean user work to obtain
  a clean status. If ownership is ambiguous, stop the unsafe commit and choose
  an explicit safe separation, not an automatic workaround.
- Validate the content being committed, not a different dirty-tree state.
  If a hook fails, changes files, or HEAD changes unexpectedly, reassess state;
  do not blindly retry or bypass hooks. A dirty final tree can be legitimate
  when it contains only preserved user changes.
- Follow explicit permissions for push, integration, and release; permission
  to commit locally does not grant them. Published-history rewrites and
  destructive operations require specific authorization. Report significant
  own changes left uncommitted and the concrete reason.

## Compose the guide

Write the target project's `GIT_WORKFLOW.md` using the example's structure.
Distinguish established rules, explicit choices, and recommendations. Preserve
existing customizations and resolve conflicts against applicable project
instructions rather than silently replacing them.
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
significant code change, including work started after onboarding. Link to the
project's `GIT_WORKFLOW.md` and tell contributors to report a missing
`git-guide` and follow that workflow instead. If the project is outside Git,
Git operations do not apply. Do not copy the skill's operational policy.

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

For authorized initialization, open both files from the target project root
and verify that the link in `AGENTS.md` resolves to that `GIT_WORKFLOW.md`.
If either file is missing or unreadable, or the link does not resolve to it,
fix the issue before reporting success. If blocked, report initialization as
incomplete and name the affected path and the specific blocker.

Then:
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
5. Check that the workflow policy matches the evidence or explicitly requested
   rules and that existing customizations remain. Verify actual Git state;
   distinguish an unborn HEAD from a failure. Do not claim an unavailable
   `git-guide` was loaded.
6. Report files written, approximate AGENTS word count, discovered or initialized
   Git state, policy source, own commits, checks actually performed, and blockers.
   Distinguish evidence inspection from command execution.
5. Check that workflow policies match the evidence or explicitly requested
   rules and that existing customizations remain.
6. Report files created, updated, or retained, approximate `AGENTS.md` word
   count, observed Git state, policy sources, checks performed, and blockers.
   Distinguish inspected commands from executed checks.

The finished guide should help the next contributor act immediately, without
requiring them to know this conversation or the author's local environment.

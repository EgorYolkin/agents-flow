---
name: project-init
description: Coordinate project kickoff from the user's goal. Use init for repository instructions and apply the styleguides for the files involved. Route significant code changes through git-guide. Planning alone is read-only.
---

# Project Init

Start from the current user request. A bare invocation or planning-only
request is read-only. If the user asks to run `init` or prepare repository
instructions, perform the onboarding below now. Do not require a product task
first. If onboarding is the only request, report the result without proposing
or starting application work.

## Establish the first outcome

For any project, derive the first deliverable from the user's current goal.
Repository files provide constraints and evidence, not authorization. A README
example, tutorial, TODO, or empty directory is not a task unless the user
selects it. If the user supplies only a path or no actionable goal, ask one
focused question about the desired outcome and wait; do not choose a stack or
deliverable yourself. Reuse a prior goal only when the user is continuing it.

For an existing project, read applicable instructions and follow the relevant
path from entry point to consumer. Use a few representative files, manifests
and CI definitions to identify constraints and an existing check. In a monorepo,
scope the brief to the affected components and the boundaries between them.
Distinguish commands found in the repository from checks actually run.

## Route the task

Identify the files the requested task touches. Load the installed styleguides
that match them and apply them to the review or edit; do not just list their
names. For example, use the Python guide for a Python module and the shell
guide for its shell launcher, not every guide for every file. Where no guide
is installed, use the project's conventions and note the gap. Install skills
only on request.

Before the first edit for a significant code change, also load and follow
`git-guide`. This applies to a feature, bug fix, or refactor regardless of
patch size. The styleguide governs the code; `git-guide` governs the Git work.
For a review or plan alone, do not create branches or commits.

## Run repository onboarding when requested or needed

For an explicit request such as “run init first”, immediately load `init`
through the active harness (in OMP, read `skill://init`) and follow its
workflow at the requested root. Do this even if onboarding files already exist;
preserve existing instructions. Do not just list `init` as a later step. If the
request explicitly limits work to a plan or review, do not write anything.

Otherwise, check onboarding once the user authorizes a specific implementation,
in the initial request or in a follow-up approving an agreed task. Approval to
run `init` alone does not authorize implementation. Check the target project
root, not just the deliverable directory. If either `AGENTS.md` or
`GIT_WORKFLOW.md` is missing, run `init` before task edits unless the user
asked to skip onboarding. If both exist, use them. The absence of a Git
repository alone is not a reason to rerun `init` or create a repository.

If the required `init` skill is unavailable, say so and offer to continue
without onboarding or install it with the user's approval. Do not silently
substitute `git-guide`: it guides Git operations but does not prepare the
repository's agent instructions.

## Hand off in chat

Give the next agent the goal and first task, affected paths or planned
components, relevant constraints, selected skills and why each applies, and
one observable acceptance check. Include an open question only if its answer
changes the work. Keep simple projects to a few lines. When the same request
includes implementation, carry this context into the authorized work.

Persistence is opt-in. On an explicit request to save the brief, update the
user's chosen location or the project's existing handoff document. If neither
exists, use `.agents-flow/context.md`. On later runs, refresh relevant facts
in place and preserve user decisions. A chat-only kickoff creates no files,
directories, Git state, or harness settings.

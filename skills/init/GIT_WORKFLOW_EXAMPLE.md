# Git Workflow Example

This is a writing example for `init`, not a policy to apply to every repository.
Create the actual `GIT_WORKFLOW.md` in the target project from its instructions,
Git state, and established practices. Preserve an existing workflow. For an
explicit request to use the user's own rules, load the current `git-guide` skill;
this example does not contain or replace that skill's policy.

## Writing style and evidence

Use short, actionable Markdown sections in the project's documentation language.
Record concrete decisions, not a Git tutorial or a transcript of command output.
For each policy, distinguish documented requirements from observed conventions
and newly recommended defaults. Cite project-relative sources where available.
Do not turn one historical example into a mandatory rule or include personal
machine paths, credentials, or invented verification results.

The following sections illustrate a simple sequential project. Replace their
choices with the target project's actual policy; omit irrelevant sections.

## Scope and policy sources

Describe which repository and contributors this workflow covers. Point to
applicable contributor instructions and CI configuration. Explain how conflicts
are resolved under the project's instruction hierarchy. Keep detailed Git policy
here and link to it from `AGENTS.md` rather than maintaining two copies.

## Branches and task isolation

Example default when no established policy exists: use a short-lived branch per
independent task; continue that branch for follow-up work on the same task.
Determine the base branch from the project, not an assumed `main`. Record the
chosen naming pattern, such as `feat/export-csv` or `fix/retry-timeout`.

Keep one writer per working directory. Use separate worktrees and branches or
serialize concurrent writers. Preserve initial user changes; worktrees do not
carry uncommitted changes from the original tree.

## Changes and commits

Record the initial status and distinguish your contribution from existing work.
Check effective author/committer identity before the first commit; do not invent
identity or silently change global configuration.

Commit a completed logical step, including its necessary tests and documentation.
Inspect the full candidate, including pre-existing staged content, and exclude
unrelated user work and secrets. Do not automatically stash, reset, or clean
someone else's changes. If changes cannot be safely separated, explain the
blocker instead of forcing a commit.

Follow the established message style. If none exists, a possible recommendation
is an effect-oriented subject such as `fix: stop retries after deadline`; explain
non-obvious reasons in the body. Do not invent issue references or test results.

## Validation and documentation

Name the project's actual checks and documentation sync points, with their
working directories. If checks do not exist, state that and describe appropriate
manual validation. Verify the candidate being saved, not only a dirty working
tree with extra fixes. Reassess state if hooks change files or fail; do not bypass
them automatically.

## Publication and integration

State whether local commits are automatic and which push/merge actions are
already authorized. Without publication permission, preserve results locally
and report the next step. Do not infer push, release, or history-rewrite permission
from permission to commit. Record remote, review, and integration requirements
only when established; do not invent branch protections or mandatory squash.

## Interrupted work and handoff

Recheck actual state after interruption. Do not automatically continue or abort
another person's merge/rebase/cherry-pick. Handle detached HEAD or an unborn
branch explicitly without discarding work. Report own commits, actual checks,
publication state, and any significant uncommitted contribution with its reason.
An unchanged dirty tree belonging to the user is not a cleanup failure.

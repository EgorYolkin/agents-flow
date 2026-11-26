# Git Workflow Example

This is a writing example for `init`, not a policy to apply to every repository.
Create the actual `GIT_WORKFLOW.md` in the target project from its instructions,
Git state, and established practices. Preserve an existing workflow. For an
explicit request to use the user's own rules, consult the current `git-guide`
as a policy source only. Do not execute its workflow during onboarding.

## Writing style and evidence

Use short, actionable Markdown sections in the project's documentation language.
Record concrete decisions, not a Git tutorial or a transcript of command output.
For each policy, distinguish documented requirements from observed conventions
and newly recommended defaults. Cite project-relative sources where available.
Do not turn one historical example into a mandatory rule or include personal
machine paths, credentials, or invented verification results.

Use the sections below where supported by the project. If there is no Git
repository or documented workflow, say so rather than inventing one.

## Scope and policy sources

Describe which repository and contributors this workflow covers. Point to
applicable contributor instructions and CI configuration. Explain how conflicts
are resolved under the project's instruction hierarchy. Keep detailed Git policy
here and link to it from `AGENTS.md` rather than maintaining two copies.

## Branches and task isolation

Identify the project's base branch, branch naming convention, and any
documented isolation rules. Cite a representative branch name when useful.

## Changes and commits

Describe the project's commit scope, message style and any required trailers.
Use an inspected example to illustrate a documented convention, not to
establish a new requirement.

## Validation and documentation

Name the project's actual checks and documentation sync points, with their
working directories. If checks do not exist, state that and describe appropriate
manual validation.

## Publication and integration

Record established review, merge, and publication requirements. Distinguish
permission to commit locally from permission to push or release.

## Interrupted work and handoff

Point to existing handoff or recovery instructions where relevant. Record
what contributors need to report when work is incomplete.

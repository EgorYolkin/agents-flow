---
name: project-init
description: Orient an agent at project kickoff. Use for a new or existing project when the user wants to establish the first deliverable, select relevant agents-flow skills, and agree on a way to verify it. Return the working context in chat by default.
---

# Project Init

Turn a project kickoff into a first task another agent can pick up. A kickoff
alone is read-only. Keep the brief in chat. Requests to generate contributor
instructions belong to the separate `init` skill. Do not invoke it implicitly.

## Establish the first outcome

For an empty directory, use the user's description to identify who or what will
consume the result and one observable first success. If the goal is too broad
to choose a first task, ask the smallest question that would change the choice.
Keep proposed stack or layout decisions provisional until selected.

For an existing project, read applicable instructions and follow the relevant
path from entry point to consumer. Use a few representative files, manifests
and CI definitions to identify constraints and an existing check. In a monorepo,
scope the brief to the affected components and the boundaries between them.
Distinguish commands found in the repository from checks actually run.

## Route the task

Match the first task against skill descriptions available in the current harness.
If the agents-flow catalog is accessible, distinguish installed skills from
relevant install candidates. Install only as a separate requested action.
When coverage is missing, use the project's instructions and checks. Never
invent a skill name to fill a gap.

For example, a Bash entrypoint in a Go service may split a filename containing
spaces. Route the argument forwarding to `shell-styleguide` when available.
Include `go-styleguide` only if the task reaches Go argument handling. An
observable check is whether the binary receives that filename as one argument.
For infrastructure, distinguish reviewing a plan from applying it to an
environment. Name which outcome the user requested.

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

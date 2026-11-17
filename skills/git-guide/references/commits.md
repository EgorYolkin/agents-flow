# Commit ownership, messages, and validation

## Review the complete candidate

Compare the original staged and unstaged changes with your work. Preserve
pre-existing staged entries as well as file contents. Inspect untracked files
separately: ordinary diffs do not include them. Check deletions, executable bits,
symlinks, and generated or sensitive content before staging.

Useful inspection commands, selected for the current state:

```sh
git diff --stat
git diff -- path/to/file
git diff --cached --stat
git diff --cached
git diff --cached --check
```

For a clean index containing only owned changes, explicitly stage selected paths
or hunks, inspect the full staged diff, then commit. Avoid blanket `add` or `-a`
when ownership has not been established. File allowlists do not prove hunk
ownership.

An ordinary commit saves the index, including previously staged unrelated work.
`git commit --only -- path/to/file` excludes staged changes in other paths, but
uses the named file's working-tree contents. It can therefore include unstaged
edits in that file. Use this special case only for completely owned files after
reviewing their whole content and checking the effect on the index. It is not a
solution for mixed authorship in one file or for unresolved merge state.

Prefer isolation before editing when the index is mixed or ownership unclear.
If discovered later, preserve existing work and separate attributable changes
without resetting another writer's index or automatically stashing their files.
Do not improvise a universal patch-transfer algorithm for overlapping hunks.

## Validate what will be saved

Checks must cover the saved candidate. If the working tree differs materially,
a passing test may depend on content that the commit omits. Establish equality
for relevant files or validate the candidate in a separate disposable environment.
If this is unavailable, state exactly what was checked and what remains unverified.
Do not execute untrusted project hooks or tests outside the task's permissions.

Before committing, recheck expected branch and HEAD and exclusive writer ownership.
After a hook modifies files or a commit fails, inspect the index and working tree,
review the changes, and rerun affected checks. Do not blindly retry, bypass hooks,
or invent author identities or signing attestations to obtain success.

After success, inspect the actual commit diff and status, not merely the exit code.
If the result differs from the validated candidate, reassess checks before claiming
success. Hooks are useful checks, not an enforcement boundary for all agents.

## Preserve the explanation

Follow repository conventions. If none exist, Conventional Commits is a useful
fallback, not an obligation to introduce release automation. Describe the effect
in the subject; add the problem and important rationale for nontrivial changes.

```text
fix(retry): stop scheduling attempts after the deadline

Check the remaining budget before scheduling another attempt so the caller's
timeout bounds the complete operation. Keep backoff for attempts that still fit.
```

Do not fabricate issue IDs, test results, motivations, AI attribution, or
`Signed-off-by` trailers. A trivial change does not need a padded body. Keep
validation details in the task report or the project's established location.
Use a new fix commit after review unless rewriting that specific history is
permitted. Commit boundaries follow logical outcomes, not elapsed time.

## Sources

Workflow policy adapts the user-supplied research dated 17 November 2026.
Index and path-limited commit semantics were checked through Context7 against
[Git commit](https://git-scm.com/docs/git-commit) on that date. Related primary
references supplied by the research:

- [Git workflows](https://git-scm.com/docs/gitworkflows)
- [Git contribution guidance](https://git-scm.com/docs/SubmittingPatches)
- [Git hooks](https://git-scm.com/docs/githooks)
- [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/)

Links to Git manuals are living sources. The example above is original; it is
not a quotation or an assertion about this repository's behavior.

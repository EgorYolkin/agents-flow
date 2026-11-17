# Isolation, integration, and recovery

## Choose the smallest sufficient isolation

| Situation | Choice |
|---|---|
| One exclusive writer and a known baseline | Task branch in the current directory. |
| Several read-only agents | Shared directory if tools remain read-only. |
| Concurrent writers, including the user or mutating checks | Separate worktrees and branches, or serialization for the whole writing operation. |
| Existing work prevents safe branch switching | Preserve it in place; start from an appropriate commit in another worktree. |
| Task depends on uncommitted changes | Plan an explicit owned-change transfer or work sequentially in place. A clean worktree omits those changes. |
| Independent refs/configuration required | Consider a separate clone. |
| Executed code requires containment | Use appropriate runtime isolation; neither worktree nor clone provides it. |

Linked worktrees have separate working files, HEAD, and index; ordinary branch
refs and repository configuration are generally shared. `git worktree lock`
protects administrative state against removal/pruning; it is not an editing mutex.
Coordinate writer ownership through the harness for the entire operation.

Inspect existing worktrees before creating one. Use a unique task branch and a
nonconflicting path outside the product tree. Do not force checkout of a branch
already used by another worktree. Keep module ownership explicit during parallel
work and designate one integrator. This skill does not itself spawn agents.

## Recover according to the actual state

| Observed state | Response |
|---|---|
| Interrupted task or unexpectedly moved HEAD | Reread status, branch, HEAD, and operation state; compare with the recorded baseline before mutating. |
| Detached HEAD | Inspect why; for implementation, preserve the intended starting commit on a named task branch before creating otherwise unreferenced commits. |
| Unborn HEAD in a new repository | Treat absence of a first commit as normal. Inspect existing files/index and establish the initial branch according to project policy; do not assume a base commit exists. |
| Merge, rebase, or cherry-pick in progress | Establish ownership and original intent. Continue or abort only within that task's authority; never automatically resolve another writer's operation. |
| Commit/hook failure | Inspect what changed and the failure reason; preserve work, resolve the actual blocker, and rerun affected checks. Do not bypass enforcement to finish. |
| Own commit appears lost | Inspect local reflog, verify the commit, and preserve it with a new rescue branch when appropriate. Avoid resetting the current files. |
| Push rejected | Inspect remote changes and branch policy; do not automatically force-push or rebase shared history. |

Reflogs are local and expire. They help recover references to commits, not
arbitrary uncommitted files. Never promise they are a full backup.

## Integrate and clean up deliberately

Follow the project's permitted merge method. Fast-forward moves a reference;
a merge commit links histories; squash records the combined result without the
original commit chain in the target history. Rewriting methods can change IDs.
Preserve the meaningful explanation when squashing.

Check the combined state after integration. Before removing a temporary worktree,
inspect tracked, untracked, and valuable ignored files and verify access to any
needed commits. Preserve a branch or another verified reference. Avoid forced
removal or branch deletion merely to make status tidy.

After squash integration, lack of ancestry alone does not prove missing work.
Verify the integrated result and any remaining branch-specific changes before
claiming successful integration or deciding cleanup is safe.

## Sources

Workflow defaults adapt the user's research dated 17 November 2026. Worktree
sharing and lock semantics were checked through Context7 on that date.
Other primary references below come from the supplied research; local experiment
artifacts were not provided. Git manual URLs track current documentation.

- [Git worktree](https://git-scm.com/docs/git-worktree)
- [Git merge](https://git-scm.com/docs/git-merge)
- [Git reflog](https://git-scm.com/docs/git-reflog)
- [Git branch](https://git-scm.com/docs/git-branch)
- [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow)
- [Gitflow author’s model and applicability note](https://nvie.com/posts/a-successful-git-branching-model/)

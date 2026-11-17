# Reading history with a purpose

## Select the question first

Use recent history to learn conventions, then inspect only relevant files and
commits. These commands are examples with placeholder paths and revisions;
choose them deliberately rather than executing the entire list.

```sh
git status --short --branch
git log -n 20 --oneline --decorate
git log -n 15 --first-parent --oneline
git log -n 10 -p -- path/to/file
git log --follow -n 10 -p -- path/to/file
git log -n 10 -S 'symbol_or_literal' -p -- path/to/file
git log -n 10 -G 'relevant_regex' -p -- path/to/file
git show COMMIT -- path/to/file
git blame -L 20,40 -- path/to/file
```

For machine parsing, prefer NUL-delimited status output, such as
`git status --porcelain=v2 --branch -z`, with an actual NUL-aware parser.
Do not split filenames on whitespace or assume one record per printed line.

| Question | Approach and limitation |
|---|---|
| What recently landed? | First-parent log gives an integration overview, not every branch's detail. |
| How did this file evolve? | Path-scoped log; `--follow` follows renames for one file. |
| When did a literal change? | `-S` finds changes in occurrence counts, not every matching edited line. |
| Which patch touched this pattern? | `-G` matches added/deleted diff lines against a regex. |
| Why is this line here? | Use blame to locate a commit, then read its diff and context. |
| Is a merge hiding the change? | Choose explicit merge-diff display or inspect relevant parents; default output may omit it. |

The numeric limits above are context-budget starting points. Expand when the
question warrants it. Check for shallow history before claiming an event never
occurred; fetching more history should be scoped to the task and access available.
Commit messages describe intent, not proof of current behavior. Confirm against
current code and tests. Record only relevant constraints, commit IDs, and remaining
uncertainties; do not turn historical preferences into new project requirements.

## Sources and provenance

Based on the user-supplied research “Git практики для скилла coding агента”,
17 November 2026. Command semantics checked against official Git documentation
through Context7 on that date. The research's local experiments and linked JSON
files were not supplied; do not claim to have reproduced them from the report.

- [Git log](https://git-scm.com/docs/git-log)
- [Git diffcore pickaxe](https://git-scm.com/docs/gitdiffcore)
- [Git blame](https://git-scm.com/docs/git-blame)
- [Git status](https://git-scm.com/docs/git-status)

These are living documentation links, not pinned versions. Consult documentation
matching installed Git when a version-dependent option matters. Instructions
here are original summaries; workflow defaults are adaptations of the research.

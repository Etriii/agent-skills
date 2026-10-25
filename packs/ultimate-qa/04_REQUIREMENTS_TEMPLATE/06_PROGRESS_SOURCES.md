# 06 – Progress sources (what has already been done)

Where the truth about completed work lives. The agent reads this before opening a new QA version (`qa v2`) so that version 2 does not re-report what the team has already fixed.

You can fill this in at any time. If it is empty when a new version starts, the agent asks for it in chat and writes your answer here.

**What counts as a progress source:** a done-list or `PROGRESS.md`, a sprint board export (CSV, JSON, a pasted list), a changelog or release notes, a range of commits or tags, a branch, a folder of hand-off notes, or the previous version's own change log.

**How the agent treats it:** as a pointer, not as proof. Everything claimed here is verified against the code before it is marked closed; anything that cannot be verified is carried into the new version as open, with a note. See `09_VERSIONING_GUIDE.md`.

---

## Sources

| # | Path or reference | Kind | Covers (dates / versions) | Given by | Trust | Verified |
|---|---|---|---|---|---|---|
| 1 | `docs/PROGRESS.md` | done-list maintained by the team | v1 review to today | user, 2026-04-10 | claims only | agent checks each line against the code |
| 2 | `qa-findings/v1/client/after_implementation/md/02_Change_Log.md` | optional client change log, if created | v1 implementation | agent | high | corroborate against commits and executed checks |
| 3 | `git log v1.0.0..HEAD` | commit history | 2026-03-04 to 2026-04-10 | agent | high | read directly |

*(The rows above are examples. Replace them, or delete them and write "none - work it out from the code and the previous change log".)*

## Work done outside the QA cycle

Anything the team built that this kit never planned - a new module, a rewrite, a dependency upgrade, a server move. Say it here even in one line, because it changes what needs re-checking.

-

## Known incomplete

Things that were started and not finished, so the new version does not report them as either done or untouched.

-

## Per version

| Version | Sources used | Note |
|---|---|---|
| v2 | 1, 2, 3 | `docs/PROGRESS.md` was last updated two weeks before the run; the last three items were verified from the code instead |

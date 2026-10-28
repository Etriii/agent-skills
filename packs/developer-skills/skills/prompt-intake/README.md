# Prompt Intake

Analyze a task before execution, catch material ambiguities and save a versioned question file for each new intake. Choices put the justified recommendation first and allow a specific custom answer. Each response explains what to do next. Existing decisions are reused; clear tasks proceed without a forced questionnaire.

## Install

From the collection root, preview installation across your Codex projects with Python 3.11+:

```powershell
python tools/install_skills.py --pack developer-skills --agent codex --scope user --user-home "$env:USERPROFILE" --skills prompt-intake --dry-run
python tools/install_skills.py --pack developer-skills --agent codex --scope user --user-home "$env:USERPROFILE" --skills prompt-intake
```

For one project, replace `--scope user --user-home "$env:USERPROFILE"` with `--project "D:\My App"`. The installer previews destinations and asks before changing them. It retains checksums, backups and Markdown operation records.

Alternatively, install from the local checkout with Node.js 22.20+ and npm:

```powershell
npx skills@1.7.4 add ./packs/developer-skills --skill prompt-intake --agent codex -g --copy
```

Use `--agent claude-code` for the external CLI or `--agent claude` for the Python installer when targeting Claude Code. A local source command includes unpublished changes; remote GitHub commands include this skill only after publication. Refresh or restart the agent if the added skill does not appear.

## Use

In Codex chat, include the task with the skill:

```text
$prompt-intake Add CSV export for the transactions page. Ask about decisions that could block correct implementation before editing.
```

The skill inspects existing requirements and code first. For example, if the export scope is unresolved, it could ask:

```text
Which transactions should the export contain?
A. Current filtered results (Recommended) — matches the visible search criteria.
B. Selected rows only — requires an explicit selection.
C. All accessible transactions — ignores filters and may create a larger export.
You can also enter a specific custom answer.
```

The actual recommendation depends on the task and source evidence. With an available, permitted native question tool, the host displays choices and a custom-answer control. Hosts that support preselection highlight the first recommendation. A highlighted option is not an answer until submitted. If question tools are unavailable or restricted by the current mode, questions appear in chat. This skill cannot enable a missing CLI menu.

Each new intake creates the next numbered file in one project folder:

```text
.prompt-intake/
  questions-v001.md
  questions-v002.md
```

The file records the task, scope, acceptance conditions, status, questions, recommendations and blank `Answer:` fields. Each meaningful multiple-choice question puts the justified recommendation first; native hosts that support defaults highlight it. Every question also accepts a specific custom answer. A highlighted default is not submitted automatically. Answer through the native menu when available, or edit the file with choices or custom text. Menu and chat answers are recorded in the active file too. Required unanswered decisions block dependent work.

After filling the file, send:

```text
continue
```

`answered` and `done` also request a reread. The agent checks the active file and continues only when required answers are present and consistent. A continuation message does not select defaults. If several tasks have files, the active conversation identifies which one to read; without that context, supply the file path.

Each paused response names the file and gives a hint such as:

```text
Next: Fill the Answer fields in .prompt-intake/questions-v001.md. Then reply continue.
```

A new `$prompt-intake` run creates a new version; replying `continue` resumes the pending version. Earlier versions remain intact. Material task changes create a new version referencing the earlier intake. A custom destination directory or filename base is supported with the same version numbering. Existing files are never replaced when allocating a version.

Each question tracks its answer separately from implementation:

| Field | States |
|---|---|
| Answer state | Unanswered, Answered, Needs confirmation |
| Work state | Pending, Blocked, Deferred, Implemented, Not applicable |

For example, selecting `A` can make Q1 `Answered` while its work remains `Pending`. The agent marks it `Implemented` only with source/output evidence and relevant verification. A question can instead be `Not applicable` when its answer requires no implementation; the reason is recorded.

When you start another intake for the same task, relevant unanswered and unfinished items move into the new version beside new questions. They keep their IDs, options, answers, reasons and original-version references. Already answered items do not require another answer unless requirements changed. Completed or excluded items retain a short reference explaining their disposition. Older versions remain intact; the current active version records new progress.

Unrelated tasks are not merged automatically. Deferred items remain visible without granting permission to implement them. Each pause identifies unfinished IDs and explains what to answer, unblock or explicitly bring into scope. `Ready` means required decisions are answered; closing an intake does not mean all chosen work was implemented.

Clear tasks still get a file marked `Ready` with `No questions needed`, then proceed within the original authorization. Help or a bare invocation without an identifiable task creates no file. When the original task finishes, the final hint states that no reply is required and shows how to start another intake.

For analysis without implementation:

```text
$prompt-intake Analyze this prompt and ask questions only. Do not implement it. Prompt: add transaction export.
```

A bare `$prompt-intake` uses the clearly pending task or asks you to supply one. In Claude Code, invoke `/prompt-intake`.

## Prerequisites and limits

No runtime scripts, API keys, background service or third-party Python packages are required by the skill. The target task can have its own prerequisites. This is a workflow skill, not a hook that intercepts every prompt. Matching requests can select it automatically; explicit `$prompt-intake` invocation makes the intended workflow clear. Neither installation nor metadata validation proves native discovery or model adherence. See [official Codex skills documentation](https://developers.openai.com/codex/skills/).

The default workflow resumes the original authorized task after required answers arrive. Questions-only requests stop after intake. The skill never treats silence as approval or authorizes extra commits, installation or deployment. Saving each intake needs a writable destination; write failures are reported instead of silently skipping the file. The skill does not change Git ignore rules. Add `.prompt-intake/` to your project's ignore rules yourself if these records should stay local.

Use [blocker-check](../blocker-check/README.md) for a source-backed feature blocker review and [plan-review](../plan-review/README.md) for whole-plan coverage. Prompt Intake owns the conversation before execution; it does not require either skill.

Read the [agent instructions](SKILL.md), [Developer Skills pack guide](../../README.md), [installation guide](../../../../INSTALL.md) and [removal guide](../../../../UNINSTALL.md). Use the installer that owns the copy for updates and removal.

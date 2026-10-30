# Prompt Intake

Analyze a task before execution, catch material ambiguities and save a versioned question file for each new intake. Choices put the justified recommendation first and allow a specific custom answer. Each response explains what to do next. Existing decisions are reused; clear tasks proceed without a forced questionnaire.

## Install

### Direct install with npx (recommended)

No manual clone, ZIP download, or Python checkout is required to install this skill. The external CLI obtains the published source for you.

Prerequisites: [Node.js 22.20+](https://nodejs.org/en/download) with npm/npx, network access to npm/GitHub, and [Git](https://git-scm.com/downloads) for repository fallback. If a command is missing, install that prerequisite and reopen the terminal. These are installer prerequisites; the skill's runtime requirements are listed separately below.

PowerShell, from any folder, check tools first:

```powershell
node --version
npm --version
npx --version
git --version
```

PowerShell: replace `D:\My App` with your existing target application, then run each line separately:

```powershell
Set-Location 'D:\My App'
npx skills@1.7.4 add https://github.com/Etriii/agent-skills --skill prompt-intake --agent codex claude-code --copy
```

This selects only `prompt-intake` for Codex and Claude Code in the current project. Review the selected source, agents, scope and destinations in the CLI summary. npm may ask to download the pinned CLI; the skill installer may also prompt. These examples do not force noninteractive approval.

Still in the application folder, confirm the project copies:

```powershell
Test-Path '.agents/skills/prompt-intake/SKILL.md'
Test-Path '.claude/skills/prompt-intake/SKILL.md'
```

Both should return `True` for the two-agent project install. Refresh the coding-agent session, then use the chat requests in this README. Installation copies instructions; it does not run the skill.

For one agent, replace `--agent codex claude-code` with `--agent codex` or `--agent claude-code`. For an intended global installation across projects, choose this alternative command after the same prerequisites; do not run both scope examples unless you want both copies:

```powershell
npx skills@1.7.4 add https://github.com/Etriii/agent-skills --skill prompt-intake --agent codex claude-code -g --copy
```

Global destinations are shown by the CLI; the project-relative `Test-Path` checks above do not verify global copies. Remote URLs install published files, so local unpushed changes are not included. PowerShell execution-policy errors can use `npx.cmd` instead of `npx`; see [troubleshooting](../../../../docs/NPX_INSTALLATION.md#troubleshooting) for missing tools, names, network access and refresh issues.

### Optional recorded or offline installation with Python

Keep this route when you want manifest verification, retained backups and Markdown operation history. It requires Python 3.11+ and a **complete local collection** first. Follow [download/extract or clone steps](../../../../INSTALL.md#optional-local-copy-for-python-and-offline-use), then identify the root containing `tools/`, `packs/`, and `README.md`. `tools/install_skills.py` is a file in that root, not a global command.

PowerShell: replace `D:\Tools\agent-skills` with that actual collection root and `D:\My App` with the existing destination application. For a ZIP, the extracted root may instead end in `agent-skills-main`.

```powershell
Set-Location 'D:\Tools\agent-skills'
python --version
python tools/install_skills.py --pack developer-skills --agent both --project "D:\My App" --skills prompt-intake --dry-run
python tools/install_skills.py --pack developer-skills --agent both --project "D:\My App" --skills prompt-intake
```

The first installer command previews and writes nothing. The second requests the existing confirmation and performs the copy with operation records. Run them separately. Python uses `--agent both`; npx uses `--agent codex claude-code`. For Python-only Codex or Claude choose `--agent codex` or `--agent claude`. User-scope options are in the [installation guide](../../../../INSTALL.md#choose-a-pack-agent-and-scope).

Use the installer that owns an existing copy for updates/removal; npx and Python maintain different records and protections. Preserve local edits before replacement. See the [pack guide](../../README.md), [npx lifecycle](../../../../docs/NPX_INSTALLATION.md#updates-and-removal), and [recorded removal guide](../../../../UNINSTALL.md).

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

# Prompt Intake

Analyze a task before execution, catch material ambiguities and ask questions before starting work that depends on the answers. Choices put the justified recommendation first and allow a specific custom answer. Existing decisions are reused; clear tasks proceed without a forced questionnaire.

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

For a Markdown answer file:

```text
$prompt-intake Review this task before implementation and write unresolved questions to PROMPT_QUESTIONS.md. Wait for my answers before dependent work. Task: add transaction export.
```

Fill each blank `Answer:` field with a choice or custom text, then send `Read PROMPT_QUESTIONS.md and continue.` Existing files are preserved with a new numbered filename. No file is created when no questions remain.

For analysis without implementation:

```text
$prompt-intake Analyze this prompt and ask questions only. Do not implement it. Prompt: add transaction export.
```

A bare `$prompt-intake` uses the clearly pending task or asks you to supply one. In Claude Code, invoke `/prompt-intake`.

## Prerequisites and limits

No runtime scripts, API keys, background service or third-party Python packages are required by the skill. The target task can have its own prerequisites. This is a workflow skill, not a hook that intercepts every prompt. Matching requests can select it automatically; explicit `$prompt-intake` invocation makes the intended workflow clear. Neither installation nor metadata validation proves native discovery or model adherence. See [official Codex skills documentation](https://developers.openai.com/codex/skills/).

The default workflow resumes the original authorized task after required answers arrive. Questions-only requests stop after intake. The skill never treats silence as approval or authorizes extra commits, installation or deployment. File mode needs a writable destination and does not change Git ignore rules.

Use [blocker-check](../blocker-check/README.md) for a source-backed feature blocker review and [plan-review](../plan-review/README.md) for whole-plan coverage. Prompt Intake owns the conversation before execution; it does not require either skill.

Read the [agent instructions](SKILL.md), [Developer Skills pack guide](../../README.md), [installation guide](../../../../INSTALL.md) and [removal guide](../../../../UNINSTALL.md). Use the installer that owns the copy for updates and removal.

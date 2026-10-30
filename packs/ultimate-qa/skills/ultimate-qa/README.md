# Ultimate QA

Run a versioned initialize → audit → plan review of an existing application.

## Install

For automatic kit pointers, checksums, retained backups and Markdown records, use Python 3.11+ from the downloaded collection root:

```powershell
python tools/install_skills.py --pack ultimate-qa --agent codex --project "D:\My App" --skills ultimate-qa --dry-run
python tools/install_skills.py --pack ultimate-qa --agent codex --project "D:\My App" --skills ultimate-qa
```

For the external CLI, keep the complete collection in a durable folder and run from its root with Node.js 22.20+ and npm:

```powershell
npx skills@1.7.4 add ./packs/ultimate-qa --skill ultimate-qa --agent codex -g --copy
$env:ULTIMATE_QA_KIT = (Resolve-Path ./packs/ultimate-qa).Path
```

Start the agent from this terminal so it inherits the existing `ULTIMATE_QA_KIT` setting, or provide the absolute kit path when asked. The setting lasts for this terminal and child processes; repeat it in a new terminal. Keep this kit available and update its path if moved. For a project install, run from the application directory, use the absolute local pack path, and omit `-g`. For Claude Code use `--agent claude-code`. Review the destinations before proceeding. See the [npx guide](../../../../docs/NPX_INSTALLATION.md#ultimate-qa-support-files) for support-file setup and differences in installation records.

To install all nine skills or choose related specialists, follow the [Ultimate QA pack guide](../../README.md).

## Use

Refresh the agent session, open the target application repository, and invoke this in agent chat:

```text
$ultimate-qa run
```

In Claude Code use `/ultimate-qa`. These are agent chat instructions, not terminal commands. Use `status` to inspect progress; add `--client` only when client deliverables are wanted and the client skill is installed.

## Commands, continuation and expected output

Enter these in the same target application's agent chat:

| Request | Behavior and stopping point |
|---|---|
| `$ultimate-qa run` | Initialize or reconcile the active review, audit relevant areas, and produce the improvement plan in one workflow. Stop before implementation. |
| `$ultimate-qa run --client` | Complete that review, then prepare optional client deliverables when the client skill and document tools are available. Stop before implementing or sending them. |
| `$ultimate-qa initialize` | Complete intake, preflight and versioned state/template preparation. Use when setup alone is wanted. |
| `$ultimate-qa audit request creation and approval` | Audit the named scope in an initialized review; save findings and executed evidence. Replace the example scope. |
| `$ultimate-qa plan` | Build the improvement plan from current findings/gaps and existing plans. No automatic client files or implementation. |
| `$ultimate-qa status` | Read current version state, findings and next action without file changes. |
| `$ultimate-qa next-version` | Reconcile unresolved work against current evidence, preserve earlier versions, create the next version and audit for new issues. |

There is no `--auto` switch: `run` is the supported continuous intake/audit/plan request. It asks only unanswered intake questions and resumes after the reply. If setup or checks are blocked, provide the missing input/service and repeat the original invocation, retaining `--client` if supplied. `status` identifies the recorded next action; repeating a still-applicable completed `run` does not create another version. Use `next-version` explicitly for that transition.

Expected output lives under the verified application's `qa-findings/` root: version state, requirements, audit/gap reports, improvement plan, and evidence with commands/results. Optional client files appear only when requested. A missing state directs standalone `audit` or `plan` back to initialization. Bare invocation is not documented as a complete run; use `run` explicitly. `--client` does not convert the plan into implementation approval.

## Prerequisites and limits

Requires the complete QA kit, Python 3.11+, Git and an existing application repository. Use the application's own runtime, test accounts and safe environment. Docker-dependent checks remain blocked when Docker is unavailable. Client documents require the optional client skill.

The workflow stops at recommendations. Code implementation, destructive tests, deployment and sending documents need separate authorization.

Read the full [agent instructions](SKILL.md), [recorded installation guide](../../../../INSTALL.md), and [npx update/removal guide](../../../../docs/NPX_INSTALLATION.md#updates-and-removal). Use the installer that owns the copy for updates and removal. [Contribute](../../../../CONTRIBUTING.md).

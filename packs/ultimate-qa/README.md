# Ultimate QA skill kit

Ultimate QA is a set of instructions and tools for reviewing an **existing application repository** with a coding agent. The kit supplies a QA checklist, intake templates, report formats, installable skills, and small Python helpers. It is not a standalone QA executable and does not include a sample application.

The normal workflow is **initialize → audit → plan**. `$ultimate-qa run` performs those stages in order. It produces evidence-backed findings and recommendations in the application repository. Add `--client` to generate client documents after the plan; implementation remains a separate step.

## What you need

- **Python 3.11 or newer** to run the installer and helpers; **Git** and a Git repository for the application being reviewed. Run the examples below from this kit's directory unless a command says otherwise.
- A coding agent that supports the installed skills (Codex or Claude for the built-in targets). Start a new agent session in the **application repository** after installation.
- The application's own local test setup and test accounts for checks that require them. Docker and Compose are checked during initialization; if they are unavailable, runtime checks that depend on them are reported as blocked. Use disposable data for destructive checks.
- **Optional:** `python-docx` to generate Word reports: `python -m pip install python-docx`. Markdown reports are the source files.

Keep this kit directory available after installation. The core and client skills record its absolute location; reinstall those skills if you move the kit.

## Install with npx

Requires Node.js 22.20+ and npm. Download or clone the complete collection into a durable folder first; core/client instructions need the pack's templates and helpers after installation. From the collection root, install just the core or all nine QA skills:

```powershell
npx skills@1.7.4 add ./packs/ultimate-qa --skill ultimate-qa --agent codex -g --copy
npx skills@1.7.4 add ./packs/ultimate-qa --skill '*' --agent codex -g --copy
$env:ULTIMATE_QA_KIT = (Resolve-Path ./packs/ultimate-qa).Path
```

Start the agent from this terminal in the application being reviewed so it inherits this existing kit setting, or provide the absolute kit path when asked. This assignment lasts for the current terminal and child processes; repeat it in a new terminal. Keep the collection available, update the path if moved, and keep the installed skills and kit on the same revision.

For project scope, run from the application directory, supply the absolute local pack path, and omit `-g`. For Claude Code use `--agent claude-code`. Review the displayed destinations. The external CLI does not generate `kit-location.txt` or this collection's Markdown history. The [npx guide](../../docs/NPX_INSTALLATION.md) covers support files, updates and removal.

## Install with Markdown records

This kit is the `ultimate-qa` pack in Agent Skills. Use the [collection installer](../../INSTALL.md) from the collection root. The whole pack, including templates and helpers, remains available after installation.

```powershell
python tools/install_skills.py --pack ultimate-qa --list
python tools/install_skills.py --pack ultimate-qa --agent both --project "D:\My App" --skills ultimate-qa ultimate-qa-environment --dry-run
python tools/install_skills.py --pack ultimate-qa --agent both --project "D:\My App" --skills ultimate-qa ultimate-qa-environment
```

Project scope is the default. For a user installation, use `--scope user --user-home <existing-home>` instead of `--project`. Use `--bundle all` explicitly for all nine skills. Codex installs into `.agents/skills/`, Claude into `.claude/skills/`. Core/client copies receive `kit-location.txt` pointing here. Reinstall with `--replace` after moving the collection; prior content is retained as a backup. Installation creates no QA reports and runs no review.

## Uninstall skills

Use the same pack, scope and agent. Preview first, then approve the real operation:

```powershell
python tools/install_skills.py --pack ultimate-qa --agent codex --project "D:\My App" --skills ultimate-qa-client --uninstall --dry-run
python tools/install_skills.py --pack ultimate-qa --agent codex --project "D:\My App" --skills ultimate-qa-client --uninstall
```

Every completed changing install/uninstall writes `.agent-skills/history/<operation-id>/operation.md` in the selected scope. Removal requires recorded ownership and an unchanged installed digest, retains a content backup, and preserves `qa-findings/`, other skills and earlier records. Previews and unchanged reruns write nothing. See [UNINSTALL.md](../../UNINSTALL.md) for all-pack/user removal, edited copies and reinstalling.

The older standalone kit's `--target`, implicit user/all selection and custom `--destination` are not this collection's interface. Legacy copies are left alone. The pack-local `tools/install_skills.py` is a thin entry point to the same shared tool and accepts `--agent` plus explicit scope/selection.

## Included skills

| Skill | Purpose |
|---|---|
| [ultimate-qa](skills/ultimate-qa/README.md) | Run a versioned initialize → audit → plan review of an existing application. |
| [ultimate-qa-accessibility](skills/ultimate-qa-accessibility/README.md) | Audit critical pages with automated accessibility checks, keyboard journeys and assistive-technology evidence. |
| [ultimate-qa-api](skills/ultimate-qa-api/README.md) | Test API contracts, authentication, idempotency, error handling and persisted effects. |
| [ultimate-qa-architecture](skills/ultimate-qa-architecture/README.md) | Assess architecture ownership, coupling and maintainability through representative user journeys. |
| [ultimate-qa-browser](skills/ultimate-qa-browser/README.md) | Exercise authorized application journeys, role boundaries and visual states in a browser. |
| [ultimate-qa-client](skills/ultimate-qa-client/README.md) | Prepare optional client reports and approval checklists, preserving returned decisions. |
| [ultimate-qa-environment](skills/ultimate-qa-environment/README.md) | Check an isolated QA environment in dependency order and identify precise runtime blockers. |
| [ultimate-qa-performance](skills/ultimate-qa-performance/README.md) | Measure application latency, throughput, resource use and slow paths against a reproducible baseline. |
| [ultimate-qa-security](skills/ultimate-qa-security/README.md) | Review role boundaries, data integrity, secrets and safe failure behavior with verified evidence. |

Each skill README includes selected-skill installation, invocation and runtime prerequisites. See [CONTRIBUTING.md](../../CONTRIBUTING.md) before adding or changing skills.

## Run your first review

Open the **application repository**, not this kit, in a new coding-agent session. In Codex, type this in **agent chat**; it is not a terminal command:

```text
$ultimate-qa run
```

In Claude Code, use `/ultimate-qa run`. The commands below use Codex's `$` prefix; replace it with `/` in Claude Code.

To include the optional client report and approval checklist after the QA plan, install `ultimate-qa-client` and use `$ultimate-qa run --client` (Claude Code: `/ultimate-qa run --client`). The command may pause for first-run intake answers, then continue through the stages without another command. Missing runtime prerequisites block only dependent checks; available checks and the plan still proceed. Client Word output needs `python-docx` and a compatible renderer for visual verification; missing tools leave that deliverable pending. You can still run `$ultimate-qa initialize`, `$ultimate-qa audit`, and `$ultimate-qa plan` separately.

On rerun, the agent inspects state and evidence, completes interrupted stages, and rechecks stale results. Existing draft files do not count as completed work. A completed current review is reported without opening a new version; use `next-version` for a new review. Keep `--client` on the command when resuming a review that needs client output.

1. **Initialize** identifies the application's Git root, asks about requirements, an existing plan, progress, test accounts, and environment constraints, then checks Docker/Compose readiness. It creates `qa-findings/` in that root, verifies that Git ignores it, and copies the intake templates if needed. Review and complete `qa-findings/requirements/`, especially the [project context](04_REQUIREMENTS_TEMPLATE/02_PROJECT_CONTEXT.md) and [implementation ideas](04_REQUIREMENTS_TEMPLATE/03_IMPLEMENTATION_IDEAS.md), before auditing and planning. Keep passwords out of these files.
2. **Audit** runs the available checks against the [QA checklist](02_QA_CHECKLIST.md) and records what passed, failed, was blocked, or still needs manual work. Give the agent access to a safe test environment and role-specific test accounts for runtime journeys.
3. **Plan** merges findings with your existing plan and ideas into prioritized recommendations. It stops at the QA plan; code changes require a separate instruction.

You can name a scope in chat, such as `$ultimate-qa audit API and accessibility`. The agent records the actual coverage and any untested areas. If you only need part of a review, tell it the scope and constraints explicitly.

### Agent chat command reference

| Command | What it does |
|---|---|
| `$ultimate-qa run` | Initialize when needed, audit, and plan in the current application repository. Resume incomplete stages on rerun. |
| `$ultimate-qa run --client` | Run the same workflow, then prepare client documents. Requires `ultimate-qa-client`. |
| `$ultimate-qa initialize` | Intake, environment preflight, ignored output folder, and first QA state. Use when running stages separately. |
| `$ultimate-qa audit [scope]` | Check the application and write audit, gaps, and evidence for the stated scope. |
| `$ultimate-qa plan` | Write the improvement plan from findings and existing plans; stop before implementation. |
| `$ultimate-qa status` | Read current findings, stage, and next action without changing files. |
| `$ultimate-qa next-version` | Reconcile earlier findings with current evidence, carry unresolved items forward, and start the next review version. Supply progress sources when asked. |
| `$ultimate-qa-client intake` | Record a returned client intake form and ask about missing details. Requires the optional client skill. |
| `$ultimate-qa-client prepare` | After audit **and** plan, create a client report and approval checklist. Requires the optional client skill and `python-docx` for Word copies. |
| `$ultimate-qa-client decisions` | Record returned client choices without inferring approval from silence. |
| `$ultimate-qa-client report` | After separately authorized implementation, report actual changes and check results to the client. |
| `$ultimate-qa-client next-version` | Carry unresolved client decisions into the next review version. |

Install `ultimate-qa-client` only if you need the client workflow. [The client pack guide](12_CLIENT_PACK/README.md) explains which introductory documents to send and how to handle returned forms.

## Where the results go

The agent writes into the **application** repository, not this kit:

```text
<app-root>/qa-findings/
  requirements/                    # shared intake and decisions
  state.json                       # current version pointer
  v1/
    state.json                     # finding IDs, statuses, and stage
    recommendations/
      md/                          # source audit, gaps, and plan
      docs/                        # matching Word files, when generated
      evidence/                    # commands, outputs, screenshots, etc.
    client/                        # only for the optional client workflow
      md/
      docs/
      decisions/
```

The output folder is Git-ignored because it can contain sensitive review evidence. Confirm that only test credentials are used and keep passwords out of reports and logs. Later reviews use `v2/`, `v3/`, and so on; previous versions remain as history.

The state helper checks the Git root and refuses linked QA paths on every command. Skill instructions and helper validation guide project scope; the agent's filesystem permissions determine what other tools can access.

## Terminal helpers

The agent normally calls these tools as part of the workflow. You can also run them yourself **from this kit directory**. Replace `<app-root>` with the application's actual path; quote paths containing spaces.

```sh
# Check Docker/Compose readiness without changing the application.
python tools/qa_preflight.py --project "<app-root>"

# Inspect version and finding counts after initialization.
python skills/ultimate-qa/scripts/qa_state.py status --project "<app-root>"

# Generate Word copies from numbered Markdown reports (requires python-docx).
python tools/md_to_docx.py --all "<app-root>/qa-findings/v1/recommendations/md" --outdir "<app-root>/qa-findings/v1/recommendations/docs"
```

The preflight returns a nonzero exit code when the environment is blocked or inconclusive; its JSON explains why. It does not prove that the application or database is healthy. For exact options, run the tools above with `--help` instead of their other arguments; for the state helper, put `--help` after a command such as `status`. The [automation guide](13_SKILLS_AND_AUTOMATION.md) documents direct finding-state commands. The [output templates](03_OUTPUT_TEMPLATES.md) describe report files and Word conversion.

## If something blocks the review

- **Docker or a service is unavailable:** inspect the preflight result, start the application's own test stack if appropriate, and rerun the blocked checks. A missing environment is not an application defect.
- **An installed skill already exists:** the installer leaves it unchanged. Save any local edits, then use `--uninstall --skills <name>` with the same target, scope, and destination before reinstalling, including after moving this kit.
- **Uninstall refuses a path:** inspect the reported directory. It must be a real installed skill folder with the matching `SKILL.md` name, outside the kit's source directories and without links or junctions. No selected folders are removed when validation fails.
- **Initialization says `qa-findings/` is already tracked or populated:** reconcile the existing review data and Git tracking before retrying; initialization will not overwrite it.
- **Word conversion reports missing `python-docx`:** install it with the command above, or use the Markdown source until Word output is needed.

For the complete review rules, see the [agent instructions](01_QA_AGENT_PROMPT.md), [intake and conditions guide](06_INTAKE_AND_CONDITIONS.md), and [skills and automation guide](13_SKILLS_AND_AUTOMATION.md). See the [license](LICENSE.md) for terms.

## Verify the helpers

Run `python -m unittest discover -s tests -v` from this kit directory. Tests use temporary Git repositories and installation directories; they cover install and uninstall scope, previews, reinstalling, conflict handling, report preservation, project isolation, and finding history without changing installed skills.

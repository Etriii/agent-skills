# Deep Critique

Assess an idea, plan, design, implementation, document, or decision with detailed criticism, explained ratings, counterarguments, and prioritized improvements. No project, framework, or industry is assumed.

## Use

After installation, establish the subject in the conversation and type only:

```text
$deep-critique
```

This runs the full assessment immediately on the current subject. No mode selection is required. If there is no subject, the skill asks what to assess. It does not assume the entire workspace is the target.

Full assessment includes a verdict, strengths, category and overall ratings, useful ratings of major parts, ranked weaknesses, challenged assumptions, counterarguments, relevant alternatives, and prioritized next steps. Unsupported ratings remain unrated; an unresolved essential criterion prevents a misleading overall average.

Results are saved by default in the target workspace under `.deep-critique/`, categorized by modes with a unique timestamped folder for each run. The target root's `.gitignore` is updated when needed. Python 3.11+ enables the included standard-library storage helper; if saving is unavailable, the assessment remains available in chat with the limitation stated.

Optional commands narrow the output:

| Agent chat command | Purpose |
|---|---|
| `$deep-critique full <subject>` | Explicit full assessment; identical to the default. |
| `$deep-critique review <subject>` | Direct review with a compact scorecard. |
| `$deep-critique roast <subject>` | Sharper criticism, ratings, and actionable improvements. |
| `$deep-critique question <subject>` | Interactive challenge, one question at a time. |
| `$deep-critique rate <subject>` | Detailed scoring and what would improve each score. |
| `$deep-critique compare <A> vs <B>` | Consistent evaluation of alternatives and a recommendation. |
| `$deep-critique help` | Show available options without starting a review. |

Combine modes without repeating the assessment:

```text
$deep-critique roast rate
$deep-critique review compare Proposal A vs Proposal B
$deep-critique question roast rate
```

Order does not matter and duplicates count once. `roast rate` adds detailed scoring to sharp criticism. `full` includes review and detailed ratings already; `full roast` adds the sharper tone. `compare` uses supplied alternatives, and `question` conducts an interview before the combined result. `help` takes precedence and never creates output. With no mode, full assessment remains the default.

Omit the subject when it is already clear from the conversation. Natural language works too:

```text
$deep-critique Compare these proposals. Prioritize cost and clarity.
$deep-critique Roast this draft, but keep the report short.
```

In Claude Code use `/deep-critique`. These are agent chat instructions, not terminal commands. The agent interprets the subject and natural language; the included helper canonicalizes the selected modes and manages report files.

## Saved reports and reruns

```text
<target-root>/
  .deep-critique/
    roast+rate/
      20261026T153000Z-a7c91d802eb4/
        run.json
        report.md
        completion.json
```

Each invocation starts a new run. UTC timestamps, random suffixes and exclusive directory creation prevent collisions; there is no shared version counter or overwritten latest report. Reversing mode order uses the same category. Each report includes its subject, scope, ratings, recommendations and source context when available. Internal ownership and lock files live at the output root.

Question sessions keep ordered transcript entries in their active run and attach them to the final report. The completion record is written last. An interrupted run remains unfinished; publishing identical content can safely finish an interrupted completion record. Completed reports cannot be replaced with different content. Explicitly stopped partial assessments are marked incomplete.

The helper locates the Git root from the target workspace; non-Git workspaces use the supplied root. It preserves existing ignore-file bytes, appends `/.deep-critique/` only when necessary, and verifies exclusion when Git is available. Non-Git workspaces receive the same rule for future use. Existing tracked output, unrelated same-name folders, links and junctions are refused. Earlier runs are retained. Storage errors are reported without blocking a chat critique or untracking files.

See [report storage](references/report-storage.md) for helper commands, continuation and failure handling. Add “chat only” to suppress persistence. Help and missing-subject clarification create no report folders.

## Install

From the downloaded collection root, use Python 3.11+ to preview and install into an existing project:

```powershell
python tools/install_skills.py --pack developer-skills --agent codex --project "D:\My App" --skills deep-critique --dry-run
python tools/install_skills.py --pack developer-skills --agent codex --project "D:\My App" --skills deep-critique
```

For Claude Code use `--agent claude`. The recorded installer verifies checksums, retains backups, and writes Markdown operation records.

Alternatively, with Node.js 22.20+ and npm, run from the target project and select this local pack:

```powershell
npx skills@1.7.4 add "<collection-path>/packs/developer-skills" --skill deep-critique --agent codex --copy
```

Replace `<collection-path>` with the actual downloaded collection directory. Add `-g` only for an intended global installation. The remote GitHub source contains this skill only after publication. Refresh the agent session after installing; a local source addition does not install itself into a user profile.

## Prerequisites and limits

Provide the subject and any important goals or constraints. Supporting evidence improves the assessment, but the skill does not require a repository, private runner, API key, new package, environment variable, or specialist skill. Saving requires Python 3.11+, a writable target root, and filesystem support for atomic hard-link publication. Git is used when the target is a repository. Additional tools depend on the subject and authorized checks.

Review writes only its report artifacts and the target root's ignore entry by default. It does not authorize subject edits, dependency installation, data changes, publication, or messages. Scores express scoped judgments; they do not certify a deliverable. Installation checks do not prove native agent discovery or model adherence. Compatibility metadata remains unverified until native discovery is checked.

Read the complete [agent instructions](SKILL.md), [Developer Skills pack guide](../../README.md), [collection installation guide](../../../../INSTALL.md), and [external update/removal guide](../../../../docs/NPX_INSTALLATION.md#updates-and-removal). Use the installer that owns the copy for updates and removal. [Contribute](../../../../CONTRIBUTING.md).

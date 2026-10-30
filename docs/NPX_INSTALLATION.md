# Install with the skills CLI

The external [skills CLI](https://github.com/vercel-labs/skills) can install this collection's individual skills or all skills in a selected pack. These examples pin the verified CLI version, `1.7.4`, which requires Node.js 22.20+ and npm. Remote sources require network access; Git is needed when the CLI falls back to cloning. No collection-owned npm package or additional installer is required.

Use the [Python installer](../INSTALL.md) for offline installation, manifest checks, generated QA kit pointers, retained backups and Markdown operation history. The external CLI has its own installation and removal behavior. Do not use both tools to manage the same copy without reviewing ownership and collisions.

## Individual skills

For a global Codex install:

```powershell
npx skills@1.7.4 add https://github.com/Etriii/agent-skills --skill blocker-check --agent codex -g --copy
```

For a project install, run from the application's directory and omit `-g`:

```powershell
npx skills@1.7.4 add https://github.com/Etriii/agent-skills --skill blocker-check --agent codex --copy
```

Select multiple skills with `--skill plan-review blocker-check`. For Claude Code use `--agent claude-code`; for both use `--agent codex claude-code`. Codex copies go to `.agents/skills/`; Claude Code uses `.claude/skills/`, with canonical storage managed by the external CLI. Refresh the agent session after installing.

Review the displayed source, selection, scope and destinations. `--copy` avoids requiring symlink privileges on Windows. Interactive terminal runs normally ask for approval; agent-driven runs may be noninteractive. These commands do not include `-y`. Security assessment availability and results are controlled by the external service; no assessment is promised by this repository.

## Complete packs

List a pack, then select all skills in that source:

```powershell
npx skills@1.7.4 add https://github.com/Etriii/agent-skills/tree/main/packs/developer-skills --list
npx skills@1.7.4 add https://github.com/Etriii/agent-skills/tree/main/packs/developer-skills --skill '*' --agent codex -g --copy
```

Quote `'*'` so PowerShell passes it literally. Use a pack-specific source to select only that pack. Avoid the CLI's `--all` shorthand when targeting only Codex: that option also selects every agent and skips approval. The local developer pack has 28 skills; Ultimate QA has 9. Remote counts depend on the published revision. The [catalog](../SKILL_CATALOG.md) links to each skill's README.

## Ultimate QA support files

Keep a complete downloaded or cloned collection in a durable folder. Install from that same local copy so skill instructions and runtime assets come from the same revision. From its root:

```powershell
npx skills@1.7.4 add ./packs/ultimate-qa --skill ultimate-qa --agent codex -g --copy
# Or select the whole QA pack:
npx skills@1.7.4 add ./packs/ultimate-qa --skill '*' --agent codex -g --copy

$env:ULTIMATE_QA_KIT = (Resolve-Path ./packs/ultimate-qa).Path
# Start Codex from this terminal in the application you want to review.
```

`ULTIMATE_QA_KIT` is an existing skill setting, not a new runtime dependency. It must point to the actual pack root containing `01_QA_AGENT_PROMPT.md`, the checklist, templates and `tools/qa_preflight.py`. The PowerShell assignment applies to this terminal and child processes. Start the agent from this terminal, or give an already-running agent the absolute kit path when asked. Repeat the setting in a new terminal. Moving the collection requires updating the path. Do not point at the external CLI's temporary clone, which is removed after installation.

Core and client workflows require the kit. Environment checks can use its preflight helper. Other QA specialists inspect the application's own tools and evidence; runtime requirements still depend on the selected checks. Python 3.11+ is needed for kit helpers, and optional Word reports require `python-docx` plus visual rendering. See the [QA pack guide](../packs/ultimate-qa/README.md).

The Python installer remains the simpler route when you want it to generate `kit-location.txt` automatically without setting an environment variable.

## Updates and removal

Rerun the selected `add` command with the same source, agent and scope after reviewing changes. Keep the QA kit and installed skills on the same revision. External installs do not produce `.agent-skills/history/` records, validate this collection's `SHA256SUMS`, or use its guarded uninstall and retained backups.

Remove a skill installed by the external CLI with that CLI:

```powershell
npx skills@1.7.4 remove --skill blocker-check --agent codex -g
```

Omit `-g` for project scope and run from the original application directory. Supply explicit names for multiple removals. `--skill '*'` can remove unrelated skills in that scope; it does not mean only this collection or one pack. Save local edits before updates or removals. To remove copies managed by Python, follow [UNINSTALL.md](../UNINSTALL.md).

In CLI 1.7.4, removing only Codex can retain the shared `.agents/skills/<name>` directory and lock entry when another detected agent uses that same directory. The CLI can report success while the skill remains discoverable there. Check the actual directory after removal. If you intend to remove that named skill from **all agents in this scope**, omit `--agent`:

```powershell
npx skills@1.7.4 remove --skill blocker-check -g
```

This broader command removes only the named skill, but includes its copies for other agents. Use targeted removal when those copies should remain. The recorded Python installer has different ownership rules; do not use it to force-remove an external install.

## Verify a local change

Use an empty temporary application directory outside the collection. These commands use the current checkout rather than an unpushed remote branch:

```powershell
$collectionPath = (Get-Location).Path
$testProject = Join-Path ([System.IO.Path]::GetTempPath()) ('agent-skills-check-' + [guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Path $testProject | Out-Null
Push-Location $testProject
try {
    npx skills@1.7.4 add $collectionPath --list
    npx skills@1.7.4 add $collectionPath --skill blocker-check --agent codex --copy
    Get-ChildItem .agents/skills
    npx skills@1.7.4 remove --skill blocker-check
} finally {
    Pop-Location
}
```

Repository discovery must list exactly the shipping skills, with no `sample-review` fixture. Repeat in separate empty temporary projects using `Join-Path $collectionPath 'packs/developer-skills'` and `Join-Path $collectionPath 'packs/ultimate-qa'` with `--skill '*'` to check 28 and 9 copied skills. Compare the installed files with the source, including READMEs and the core QA state script. Resolve the QA kit path and run its helper `--help` to verify access without starting a review. Do not use `-g` for fixture checks.

Remote GitHub commands install published files; they cannot validate local unpushed edits. Actual local and remote proof is recorded in [NPX_COMPATIBILITY.md](NPX_COMPATIBILITY.md). Installation and file discovery do not prove model adherence, actual application QA or security-service assessments.

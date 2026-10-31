# Contributing

Contribute focused improvements to an existing skill, a new independent skill, or a cohesive pack. Start with the [catalog](SKILL_CATALOG.md) and [pack authoring guide](docs/creating-a-pack.md) to avoid overlapping responsibilities. Discuss changes to licenses, public skill names or installation behavior before implementation.

## Layout and ownership

```text
packs/<pack>/
  README.md
  SHA256SUMS
  skills/<skill>/
    README.md
    SKILL.md
    references/ or scripts/    optional
```

`SKILL.md` contains agent instructions; `README.md` explains the skill to someone deciding whether to install it. Use unique lowercase hyphenated names and match directory and frontmatter names. Keep examples and fixtures named `SKILL.md.example` so external repository discovery cannot install them. Developer Skills also requires its existing `metadata.toml` contract. Skills that bundle upstream material declare mixed provenance and include `THIRD_PARTY.md`, pinned sources and applicable licenses; checksums alone do not establish reuse rights.

Reuse the shared installer and transaction engine under `tools/`. Keep runtime helpers and templates with their responsible pack or skill. If instructions depend on files outside the skill directory, document how both the recorded installer and the external `skills` CLI locate those files after installation. A cloned temporary source is not a durable kit location.

## Document a change

- Each skill README needs a purpose, useful invocation example, installation instructions and runtime prerequisites. Link to its `SKILL.md`, pack README and collection installation guide.
- Each pack README needs its skill list, selected-skill and whole-pack installation, supported agents, support-file setup and removal instructions.
- Update the collection catalog and main README when adding or removing skills or packs. Update the changelog for user-visible changes.
- Keep comments functional and concise. Report executed checks separately from discovery, browser, provider or production claims. Do not add conversational attribution or AI signatures.

## Document skill commands and automation

A reader should be able to install a skill, copy a supported request, predict its effects, and know what to do when it pauses. Check the actual `SKILL.md`, referenced workflow, and executable helper contracts before documenting commands. Do not infer an `auto`, `run`, `help`, or `--auto` option from another skill's interface.

Every skill README must cover the applicable parts of this usage contract without padding simple skills into command frameworks:

| Document | Required explanation |
|---|---|
| Starting point | Install/update prerequisites, session refresh, and the target project or other input to open. Distinguish the skill's installation directory from the application being reviewed. |
| Where to type | Label agent-chat requests separately from terminal commands. Give the relevant agent spelling; label shell and starting folder for terminal commands. |
| Copyable request | Show a concrete first request. Identify paths, routes, report names, run IDs, and other placeholders the reader must replace. |
| Defaults and scope | Explain bare invocation, default mode/detail/focus, how the target is selected, and what happens when required input is missing. For natural-language skills, state the required input rather than inventing subcommands. |
| Commands and options | Document each supported user-facing operation and meaningful option, including combinations, invalid/conflicting inputs, and verification-only behavior. Link detailed references instead of duplicating long procedures. |
| Continuous execution | If supported, show the exact scan/review-and-build or automatic request. Explain what it authorizes, which stages it completes, what it still asks about, and where it stops. If unavailable, state the real review or implementation boundary. |
| Effects and result | Explain application edits, report/state files, ignore-file updates, output locations, preserved history, and expected feedback. Do not describe a successful install as successful execution. |
| Pause and resume | Explain actual approval checkpoints, continuation wording/run paths, rerun behavior, unresolved decisions, and missing prerequisites. Silence and generic continuation do not supply approvals. |
| Verification and recovery | Give the expected result, relevant checks, evidence limits, and the next action for missing tools, stale state, partial work, or failed file writes. |

Use one continuous implementation example where the skill already supports it. `report-builder build <scope>` can include evidence-based discovery and implementation in one request; UI/UX improvement requests implement and verify by default within established scope, with explicit improve-all and optional review/previews; `ultimate-qa run` combines intake, audit and planning but stops before implementation. These are different contracts, not interchangeable automation flags. Review advisors remain reviews unless their instructions and the user's scope authorize more. Distinguish an agent-session workflow from a recurring scheduler and from background jobs inside the target application.

When a skill supports combining modes or options, include copyable command-stack examples in its README and relevant usage/help instructions. Explain the combined effect, redundant/conflicting inputs and authorization boundary; label examples as independent when they are not a sequence. Link the shared command guide for comparison. Do not invent stacks for natural-language skills or copy another skill's flags. Lead UI/UX guidance with natural-language scoped/improve-all requests and examples using absolute paths, relative paths and URLs. Its `run --skip-review <task>` retains the concrete-fix shortcut; compatibility `--auto` retains the full review and previews. Neither flag is required for default improvements. Existing saved approval checkpoints remain valid.

Preserve existing authorization: do not add an approval pause to already authorized work or remove an explicit workflow checkpoint while improving documentation. Clearly separate consequential policy choices from routine implementation decisions. Describe incomplete, blocked, no-change, and unavailable-evidence outcomes when relevant; never promise guaranteed completion without the required source, credentials, services, or tools.

When changing an interface or documenting previously unclear behavior, update the skill README, relevant agent instructions, the [command guide](docs/SKILL_COMMANDS.md), and pack/workflow links that mention it. Update `SKILL.md` only when its contract needs clarification; documentation work alone must not change runtime behavior. Keep historical evidence truthful, document renamed-install migration, refresh payload manifests, and verify links and copies after installation.

Review documentation with realistic requests: the first run, a scoped run, a supported continuous run, a pause/resume, a verification-only request, and a missing prerequisite as applicable. Execute helper and installation checks where useful; label manual source review separately from a model-adherence or application trial. Avoid tests that only enforce prose, heading names, or keyword presence.

## Store generated artifacts safely

Every shipping `SKILL.md` must contain a nonempty `## Generated artifacts` section with the applicable storage instructions. Keep those instructions in the installed payload; a link to collection-only guidance is insufficient. Describe the actual output location and resume behavior in the skill README too. Skills that return only chat or edit application source do not need to create an artifact folder.

- Save generated reports, logs, previews, and run evidence beneath a stable, skill-owned root in the target workspace, not the installed skill directory. Each new run uses an exclusively created `YYYYMMDDTHHMMSSZ-<unique-id>/` directory. For example, `20261101T083015Z-a1b2c3d4e5f/` is UTC, filesystem-safe, and sorts by timestamp. A unique suffix prevents same-second collisions; it does not establish an order between simultaneous runs.
- Preserve prior runs and user changes. Resume an identified active run rather than opening a new empty one. Never overwrite an existing run or silently delete history. Reject linked paths, traversal, and unrelated same-name folders before writing.
- Before saving inside Git, resolve the intended repository root and inspect its `.gitignore` and existing exclusion rules. Append a root-anchored rule for only the generated output root when needed; create `.gitignore` if absent. Preserve existing bytes, comments and line endings, avoid duplicate rules, and verify exclusion with `git check-ignore`. Refuse already tracked output without untracking it automatically. Do not hide application source or documentation explicitly intended for version control.
- Outside Git, use the same safe timestamped storage and report that Git exclusion could not be verified. A workflow that requires Git, such as QA state management, retains that prerequisite. If safe storage or required exclusion fails, report the exact limitation before saving; use chat only when the skill permits that fallback.
- Existing state schemas, numbered versions, explicit project document locations, and resume paths remain compatible. Do not rename historical files or migrate state implicitly. Put new run evidence beneath its existing owner in timestamped subdirectories. A schema/path migration requires its own compatibility and recovery proof.

Deep Critique's bundled `report_store.py` and `storage_io.py` demonstrate these invariants. Reuse the responsible helper where it fits; do not introduce a dependency on another installed skill just to save files. Storage helpers need behavioral tests in disposable workspaces covering missing/existing ignore files, reruns, collisions, tracked output, and unsafe paths. Test outcomes separately from Markdown declarations and model adherence.

## Check skill rules

Prerequisites: Python 3.11+ and a complete local checkout or extracted collection ZIP. Acquire it using the [download instructions](README.md#optional-local-download-or-checkout); identify its root by `tools/` and `packs/`. These are local development checks, not installation commands, and need no third-party Python packages. Git is additionally required for the storage regression tests.

PowerShell or POSIX shell, starting in that collection root, check all shipping skills:

```powershell
python -B tools/check_skills.py --all
```

Check only one shipping skill; replace `deep-critique` with its exact catalog name:

```powershell
python -B tools/check_skills.py --skill deep-critique
```

The checker reads files without installing skills, executing payloads, changing ignore files, or contacting remote services. It reuses the existing catalog validator for structure, metadata and manifest integrity, checks authored Markdown local file links, and requires a nonempty artifact declaration. Vendored upstream Markdown retains its original link context and is excluded from link checking. Remote links and heading anchors are not checked. Exit code `0` means static checks passed; `1` means a failed check; `2` means invalid command arguments.

Results use `PASS`, `FAIL`, and `NOT VERIFIED`. A declaration's presence does not prove its semantics, runtime storage safety, or agent adherence. Unverified behavior and publication rights never become certified merely because static checks pass. Run the relevant helper regression tests and record separate native-agent trials when behavior or compatibility claims change. The GitHub Actions workflow runs the checker and existing collection/QA tests on Windows and Linux; it does not install skills into real profiles, publish artifacts, or grant redistribution rights.

## Document installation without hidden setup

Use direct `npx skills@1.7.4 add` as the recommended first installation path. Keep the recorded Python route, clearly labelled optional. A reader installing an ordinary skill should not need to discover an unstated clone step. Follow [AGENTS.md](AGENTS.md) for the repository's installation documentation policy and [INSTALL.md](INSTALL.md) for complete reader-facing steps.

- Start with prerequisites, supported shell, starting folder, and paths to replace. Show the direct repository URL, exact skill selection, explicit agents, and project scope first. Explain `-g` separately for an intended global installation.
- Explain that Node.js 22.20+ provides npm/npx, remote sources need network access, and Git supports repository fallback. State any additional skill runtime requirements separately. Show one executable command per line; never concatenate dry-run and install commands.
- Document the expected selection/destination summary, how to check installed files, agent-session refresh, and the chat request that starts the skill. Listing or installing files does not run the skill.
- Use `--agent codex claude-code` with npx for both agents and `--agent both` only with Python. Interactive prompts can differ by host; never promise a preview flag that the external CLI does not support or use `--all` as a single-agent/pack shortcut.
- For optional Python examples, first link or show ZIP download/extraction or Git clone, identify the collection root by its `tools/` and `packs/` folders, then change to that root. Clearly separate it from the destination application. Explain that dry-run changes nothing and the subsequent command performs the installation after its existing confirmation.
- Explain the QA core/client kit exception and its durable matching support files. Use the documented curl ZIP/npx setup or an existing local kit; do not rely on an external CLI's temporary download remaining available. A curl-to-shell bootstrap does not exist and must not be fabricated.
- Explain published-versus-local sources, missing-skill troubleshooting, and update/removal ownership. Existing Python users retain records/backups; a documentation preference does not authorize replacing those managed copies.

Keep the detailed primary instructions in each installable README and the shared installation guides. Preserve historical evidence, update current pack/workflow links and manifests, and validate both-agent copies and support-file access with disposable targets. Do not install into a real profile to prove documentation.

## Categorize a skill

The root [skill catalog](SKILL_CATALOG.md) owns category assignments. Categories describe a skill's primary outcome; packs describe its installation source. Categorizing a skill does not move its files or change its installation commands.

- List every shipping skill exactly once, under one primary category, with its purpose, a link to its own README and its installation pack ID.
- Choose an existing category when it fits. Add a category only for a meaningfully different purpose, then link it from the main README's purpose table. Avoid catch-all categories.
- Keep planned skills out of the available-skill tables until their installable files exist. Mark any separate proposals as planned.
- When adding, removing or renaming a skill, update its catalog entry and relevant pack guides in the same change. When moving a catalog entry, remove its previous entry.

Run the focused catalog and public-contract checks before completing a change:

```powershell
python -B -m unittest discover -s tests -p test_public_contract.py -v
```

These checks compare the categorized catalog with shipping skill directories, reject missing or duplicate entries, verify skill README links and pack IDs, and require a main README link to each populated category. Categories need no separate registry or metadata field.

## Refresh integrity manifests

For the UI/UX suite, edit shared resources in `ultimate-ui-ux`, then run `python -B tools/sync_ui_ux.py` before refreshing the manifest. The standalone UI/UX payloads carry distribution copies so one-skill installation remains self-contained. `python -B tools/sync_ui_ux.py --check` verifies those copies without writes. Do not edit the mirrors independently.

From the collection root, regenerate the selected pack's existing manifest entries plus every file in its skill directories. This preserves the pack's current support-file coverage:

```powershell
python -c "from pathlib import Path; from hashlib import sha256; root=Path('packs/developer-skills'); manifest=root/'SHA256SUMS'; paths={line.split('  ',1)[1] for line in manifest.read_text(encoding='utf-8').splitlines()}; paths.update(p.relative_to(root).as_posix() for p in (root/'skills').rglob('*') if p.is_file()); manifest.write_text(''.join(sha256((root/p).read_bytes()).hexdigest()+'  '+p+'\n' for p in sorted(paths)), encoding='utf-8', newline='\n')"
```

Replace `developer-skills` with `ultimate-qa` for that pack. Remove deliberately deleted paths from the manifest before regeneration; add new pack-wide runtime dependencies explicitly. Never include `SHA256SUMS` itself, generated kit pointers, bytecode or caches. Review hashes against the intended file changes. Checksums establish integrity, not authorship or redistribution rights.

## Verify

Use Python 3.11+ from the collection root:

```powershell
python -B tools/check_skills.py --all
```

```powershell
python -B -m unittest discover -s tests -v
python -B -m unittest discover -s packs/ultimate-qa/tests -v
python tools/package_skills.py
git diff --check
```

For changes to discovery, frontmatter, directory layout or pack dependencies, also follow the isolated [npx compatibility checks](docs/NPX_INSTALLATION.md#verify-a-local-change). Verify one-skill selection, full-pack selection and support-file access. Keep test destinations outside the source checkout and avoid installing into a real profile to obtain compatibility evidence.

New environment variables, dependencies, configuration keys or migrations must include their required examples and setup instructions. Document existing optional prerequisites too. Never commit secrets, local profile paths or generated installation state.

## Submit a pull request

Describe the concrete problem, resulting behavior, affected skills and actual validation. Include material limitations and configuration requirements. Use Conventional Commit prefixes such as `feat:`, `fix:`, `docs:` or `chore:`; bodies explain only what changed and why. Do not add attribution trailers.

Preserve unrelated work. A contribution does not authorize a release, global installation or license change. The collection's [license status](LICENSE.md) remains unresolved, and Ultimate QA retains its existing proprietary notice; do not grant new redistribution rights in a contribution.

Return to the [main README](README.md).

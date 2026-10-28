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

`SKILL.md` contains agent instructions; `README.md` explains the skill to someone deciding whether to install it. Use unique lowercase hyphenated names and match directory and frontmatter names. Keep examples and fixtures named `SKILL.md.example` so external repository discovery cannot install them. Developer Skills also requires its existing `metadata.toml` contract.

Reuse the shared installer and transaction engine under `tools/`. Keep runtime helpers and templates with their responsible pack or skill. If instructions depend on files outside the skill directory, document how both the recorded installer and the external `skills` CLI locate those files after installation. A cloned temporary source is not a durable kit location.

## Document a change

- Each skill README needs a purpose, useful invocation example, installation instructions and runtime prerequisites. Link to its `SKILL.md`, pack README and collection installation guide.
- Each pack README needs its skill list, selected-skill and whole-pack installation, supported agents, support-file setup and removal instructions.
- Update the collection catalog and main README when adding or removing skills or packs. Update the changelog for user-visible changes.
- Keep comments functional and concise. Report executed checks separately from discovery, browser, provider or production claims. Do not add conversational attribution or AI signatures.

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

From the collection root, regenerate the selected pack's existing manifest entries plus every file in its skill directories. This preserves the pack's current support-file coverage:

```powershell
python -c "from pathlib import Path; from hashlib import sha256; root=Path('packs/developer-skills'); manifest=root/'SHA256SUMS'; paths={line.split('  ',1)[1] for line in manifest.read_text(encoding='utf-8').splitlines()}; paths.update(p.relative_to(root).as_posix() for p in (root/'skills').rglob('*') if p.is_file()); manifest.write_text(''.join(sha256((root/p).read_bytes()).hexdigest()+'  '+p+'\n' for p in sorted(paths)), encoding='utf-8', newline='\n')"
```

Replace `developer-skills` with `ultimate-qa` for that pack. Remove deliberately deleted paths from the manifest before regeneration; add new pack-wide runtime dependencies explicitly. Never include `SHA256SUMS` itself, generated kit pointers, bytecode or caches. Review hashes against the intended file changes. Checksums establish integrity, not authorship or redistribution rights.

## Verify

Use Python 3.11+ from the collection root:

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

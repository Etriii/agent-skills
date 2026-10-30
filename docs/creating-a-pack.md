# Creating a pack

Add `packs/<lowercase-hyphenated-name>/`. Put each installable skill at `skills/<unique-skill-name>/SKILL.md`; keep reusable helpers, references and templates with the pack. Use names unique across the collection. Keep each directory name equal to its frontmatter name.

```text
packs/my-pack/
  README.md
  SHA256SUMS
  skills/
    my-skill/
      README.md
      SKILL.md
      references/          optional
      scripts/             optional
  tools/                   optional pack helpers
  templates/               optional shared assets
```

Portable frontmatter uses an unquoted plain scalar:

```yaml
---
name: my-skill
description: Describe when this skill applies and what it does.
---
```

Keep descriptions on one line and avoid YAML punctuation `:#{}[]`. Define the skill's inputs, outputs, limits and required evidence. Use relative paths within a skill when possible. If a skill needs pack-wide assets, document how it resolves them; arbitrary new pack pointers are not generated automatically. Ultimate QA's existing core/client pointer is explicitly supported.

Each skill README documents its purpose, installation, invocation and prerequisites. Keep agent instructions in `SKILL.md`. The pack README links to every skill README and shows selected-skill and full-pack installation. Follow [CONTRIBUTING.md](../CONTRIBUTING.md) for review and integrity updates. Name non-shipping examples `SKILL.md.example` so repository discovery cannot offer them for installation.

Follow the [command documentation contract](../CONTRIBUTING.md#document-skill-commands-and-automation): give copyable chat requests, defaults, scope, expected effects and outputs, stopping conditions, and supported automation/continuation. Natural-language skills do not need invented subcommands. List the new skill in the [command guide](SKILL_COMMANDS.md), with its actual implementation or review boundary.

Lead every skill and pack installation section with direct npx instructions and explicit prerequisites, target folder, agent selection and expected result. The Python route remains an optional recorded/offline alternative, with download/clone and collection-root steps before local script commands. Explain persistent runtime assets when needed. Follow [the installation documentation rules](../CONTRIBUTING.md#document-installation-without-hidden-setup) rather than assuming the user already has a checkout.

Give each shipping skill exactly one primary category in the root [catalog](../SKILL_CATALOG.md), including its README link and installation pack ID. Categories can span packs; a new pack does not require a new category. Follow the [categorization rules](../CONTRIBUTING.md#categorize-a-skill) and link any new category from the main README.

Developer Skills retains validated schema-1 `metadata.toml` sidecars. A sidecar is optional for other packs; if present, it must satisfy the same current contract. Do not invent license grants or compatibility proof.

Generate `SHA256SUMS` from exact payload bytes, one lowercase SHA256, two spaces, and a pack-relative path per file. List every selected skill file. Include pack-wide runtime support files too when skills depend on them. Exclude `SHA256SUMS` itself and generated caches. The QA manifest is an example of support-file coverage. Review changed hashes against the intended edits; the manifest is not a signature.

The shared CLI discovers the requested pack directory without a registry or new dependency. Document and test both-agent installation, dry-run, idempotency, recorded uninstall, local-edit protection and helper/template resolution. Update the collection catalog and README. Keep payload bytes LF in Git. A new pack does not need a second transaction engine or a new installer service.

Also verify [external CLI discovery](NPX_INSTALLATION.md#verify-a-local-change), using the pack-specific source and `--skill '*' --agent codex --copy` for a complete pack. The external CLI does not use collection manifests, history or generated pointers. Document any persistent support-file location explicitly; never rely on its temporary source clone. Do not use `--all` as a Codex-only example because that flag selects all agents too.

Run collection checks and build/extract a ZIP before distribution. Confirm the pack's license and support files are included. Only claim native agent discovery or actual skill behavior when separately exercised.

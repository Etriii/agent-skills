# Creating a pack

Add `packs/<lowercase-hyphenated-name>/`. Put each installable skill at `skills/<unique-skill-name>/SKILL.md`; keep reusable helpers, references and templates with the pack. Use names unique across the collection. Keep each directory name equal to its frontmatter name.

```text
packs/my-pack/
  README.md
  SHA256SUMS
  skills/
    my-skill/
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

Developer Skills retains validated schema-1 `metadata.toml` sidecars. A sidecar is optional for other packs; if present, it must satisfy the same current contract. Do not invent license grants or compatibility proof.

Generate `SHA256SUMS` from exact payload bytes, one lowercase SHA256, two spaces, and a pack-relative path per file. List every selected skill file. Include pack-wide runtime support files too when skills depend on them. Exclude `SHA256SUMS` itself and generated caches. The QA manifest is an example of support-file coverage. Review changed hashes against the intended edits; the manifest is not a signature.

The shared CLI discovers the requested pack directory without a registry or new dependency. Document and test both-agent installation, dry-run, idempotency, recorded uninstall, local-edit protection and helper/template resolution. Update the collection catalog and README. Keep payload bytes LF in Git. A new pack does not need a second transaction engine or a new installer service.

Run collection checks and build/extract a ZIP before distribution. Confirm the pack's license and support files are included. Only claim native agent discovery or actual skill behavior when separately exercised.

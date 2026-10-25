> Historical Developer Skills evidence/contract. The collection uses the shared [installation guide](../../../INSTALL.md), [removal guide](../../../UNINSTALL.md) and [migration notes](../../../docs/MIGRATION.md). Paths and acceptance claims below describe the original standalone checkout.

# Standalone source and release checklist

This library remains independently usable from a reviewed local checkout or locally exported committed source archive. It requires Python 3.11+, an existing target project and explicit copy approval. It does not require private PhasePilot code, Docker, a model API or network access.

## Verify local source

Run from the public checkout:

```powershell
py -3.11 -B -m unittest discover -s tests -v
py -3.14 -B -m unittest discover -s tests -v
py -3.11 -B .\tools\install_skills.py --agent both --project "D:\My App" --bundle essential --dry-run
```

The tests validate all fifteen bodies/metadata, exact selected copies, both native destinations, custom collisions, replacement backups, path containment, manifest integrity, interrupted staging/swaps and public-only archive use. Native discovery and model behavior are distinct; consult [COMPATIBILITY.md](COMPATIBILITY.md).

To verify a committed source archive, export the reviewed commit with `git archive` into a new temporary path, extract it into a fresh folder, and run the same standalone suite from that extracted public source. The extracted public library must work without access to private runner assets. Record the exact Git commit, local archive SHA256, Python version, commands and observed exits. A local verification checksum is not a published release checksum or publisher authentication.

`SHA256SUMS` contains real payload hashes used by the offline installer. Do not regenerate it merely because README or release documentation changed. Change a skill body/metadata only after review, update the affected real hashes and rerun integrity/install checks.

The following exports the current committed local source into new temporary paths. It performs no download or publication:

```powershell
$skillsArchive = Join-Path $env:TEMP ('skills-review-' + [guid]::NewGuid().ToString('N') + '.zip')
$skillsSource = Join-Path $env:TEMP ('skills-source-' + [guid]::NewGuid().ToString('N'))
git archive --format=zip --output $skillsArchive HEAD
Expand-Archive -LiteralPath $skillsArchive -DestinationPath $skillsSource
Push-Location $skillsSource
try {
    py -3.11 -B -m unittest discover -s tests -v
    py -3.14 -B -m unittest discover -s tests -v
} finally {
    Pop-Location
}
Get-FileHash -LiteralPath $skillsArchive -Algorithm SHA256
```

Inspect and retain or remove those exact temporary paths through your normal local file workflow. An uncommitted edit is not included in HEAD. [CHANGELOG.md](../CHANGELOG.md) records the unreleased source capabilities without inventing a release date/tag.

## Publication gate

| Requirement | Current source edition |
|---|---|
| Approved public license | BLOCKED: owner decision pending; no LICENSE grant exists |
| Metadata license status | UNDECIDED; not permission to redistribute |
| Public repository destination | BLOCKED: no remote configured |
| Immutable release version/tag | BLOCKED: no release tag exists; metadata versions are not releases |
| Published archive/hash/signature | NOT_PUBLISHED; do not invent a URL or signature |
| Private/public boundary | Public distribution must exclude private runner code and private development state |
| External content rights | Verify actual licenses/provenance before adding third-party material |
| Release authorization | Separate owner instruction required before tagging, pushing or uploading |

Local validation can pass while publication remains blocked. No license choice, remote setup, tag creation, push, signing, release upload or external download is performed by this checklist. [PUBLISHING.md](PUBLISHING.md) defines the owner-controlled sequence.

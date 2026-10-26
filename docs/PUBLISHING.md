# GitHub downloads and publication

The configured source repository is [Etriii/agent-skills](https://github.com/Etriii/agent-skills), with `main` as its default branch. Verify the remote revision when publishing; a local ZIP does not establish a GitHub release or publish local edits.

## Local download artifact

```powershell
python -B -m unittest discover -s tests -v
python -B -m unittest discover -s packs/ultimate-qa/tests -v
python tools/package_skills.py
Get-FileHash dist/agent-skills-0.1.0.zip -Algorithm SHA256
```

The ZIP contains the complete collection, both packs, required support files, shared tools and documentation. It excludes Git internals, bytecode, local lifecycle state, backups, environments and previous archives. It includes `SNAPSHOT_SHA256SUMS` for packaged-file integrity; `dist/SHA256SUMS` hashes the resulting ZIP. Extract it to a new folder and run the same tests before sharing. QA core/client installation must use the extracted pack's actual location.

## Host on GitHub

1. Confirm repository ownership and visibility. Check the [license status](../LICENSE.md): the developer license is undecided and QA retains a proprietary notice with a placeholder holder. Resolve these before further public distribution.
2. Review and commit the scoped changes on a branch. Use a Conventional Commit message stating what changed and why. Include checksum changes for added READMEs and required runtime assets.
3. Verify `origin` points to the intended repository before an authorized push of the reviewed branch. A local documentation or compatibility task does not itself authorize pushing.
4. GitHub **Code > Download ZIP** and remote `npx skills` commands use the pushed files. After publication, repeat [remote compatibility checks](NPX_INSTALLATION.md) against that revision; local results alone cannot prove hosted discovery includes the new documentation.
5. For a versioned download, create the approved immutable tag and GitHub Release, then attach the ZIP and its SHA256SUMS. Record the real commit, tag, archive hash and release URL. A version file does not prove that a tag or release exists.

The package builder uses local files and does not contact GitHub, push commits, select a license or create a release. No release signature or hosted compatibility acceptance is claimed.

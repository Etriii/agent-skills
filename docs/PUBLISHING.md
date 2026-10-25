# GitHub downloads and publication

The local collection can be packaged now. Its GitHub URL and release are not established by a local ZIP. Do not substitute an invented repository owner in the documentation.

## Local download artifact

```powershell
python -B -m unittest discover -s tests -v
python -B -m unittest discover -s packs/ultimate-qa/tests -v
python tools/package_skills.py
Get-FileHash dist/agent-skills-0.1.0.zip -Algorithm SHA256
```

The ZIP contains the complete collection, both packs, required support files, shared tools and documentation. It excludes Git internals, bytecode, local lifecycle state, backups, environments and previous archives. It includes `SNAPSHOT_SHA256SUMS` for packaged-file integrity; `dist/SHA256SUMS` hashes the resulting ZIP. Extract it to a new folder and run the same tests before sharing. QA core/client installation must use the extracted pack's actual location.

## Host on GitHub

1. Choose the owner/repository (`agent-skills` is the recommended repository name) and visibility. Check the [license status](../LICENSE.md): the developer license is undecided and QA retains a proprietary notice with a placeholder holder. Resolve these before public distribution.
2. Review and commit the collection changes on a branch in the new checkout. Use a Conventional Commit message describing the architecture and recorded lifecycle. The inherited baseline commit alone does not contain the collection changes.
3. Create the approved GitHub repository, add its actual HTTPS or SSH URL as `origin`, and push the reviewed branch. Those remote actions require an established destination and authorization.
4. GitHub **Code > Download ZIP** becomes the source-download route after the branch is pushed. Use that actual URL in the README once it exists.
5. For a versioned download, create the approved immutable tag and GitHub Release, then attach the ZIP and its SHA256SUMS. Record the real commit, tag, archive hash and release URL. A version file does not prove that a tag or release exists.

The package builder uses local files and does not contact GitHub, push commits, select a license or create a release. No release signature or hosted compatibility acceptance is claimed.

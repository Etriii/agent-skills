# Developer Skills

Independent public skill library under local development. The repository has no remote and has not been published. A public license has not been selected; redistribution remains pending that decision.

Phase 01 establishes the metadata and safety contracts. The 15 skill bodies and standalone installer belong to Phase 02 and are not available yet. No private runner package is required or imported by this library.

See `docs/SKILL_CONTRACT.md` for the public interface baseline. The implementation specification remains in the separately supplied documentation package.

The contract checks require Python 3.11 or newer and use only its standard library:

```powershell
py -3.11 -m unittest discover -s tests -v
```

These tests validate a synthetic metadata fixture and repository independence. They do not certify an installer or shipping skill catalog.

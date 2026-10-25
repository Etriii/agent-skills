> Historical Developer Skills evidence/contract. The collection uses the shared [installation guide](../../../INSTALL.md), [removal guide](../../../UNINSTALL.md) and [migration notes](../../../docs/MIGRATION.md). Paths and acceptance claims below describe the original standalone checkout.

# Verified compatibility and limits

Observed 2026-10-24 on Windows, Python 3.11.9 and 3.14.7. The public standard-library suite verifies project Codex `.agents/skills`, project Claude `.claude/skills`, both-agent copies, and user-scope standard-home mappings in isolated directories.

Native project discovery also passed for all fifteen names:

| Runtime | Exact observed version | Local proof |
|---|---|---|
| Codex CLI | 0.164.0 | App-server initialize plus skills/list for the temporary project |
| Claude Code | 2.1.299 | Stream-JSON initialize control response lists all installed project skill commands |

The native probe installed only local files into a temporary project. Configuration homes were isolated; no model prompt was submitted. Claude's `--bare` mode omitted project skills from the initialization command list, so the successful check used ordinary startup with only the empty temporary project's settings, strict empty MCP configuration and disabled nonessential traffic. Its provider URL pointed to an unused loopback port and no real API credential was passed.

The native probe lives in the sibling private repository's development evidence at `docs/implementation-progress/phases/phase-02/CHECK_NATIVE_DISCOVERY.py`; it is not a dependency of installation or skill usage. Public tests work from a public-only bundle without that sibling. Discovery is capability availability, not evidence that a model followed the instructions or performed a review.

No native user-scope discovery, macOS/Linux execution, future runtime versions, model behavior, Docker operation or published distribution is certified. POSIX symlink rejection has a portable test branch but was not executed on this Windows host. Windows junction rejection was executed. Real profile/global skill files were not changed.

The optional skill-creator quick validator could not run because its host Python environment lacks PyYAML. The library introduces no dependency to run that external helper; its own constrained parser, manifest checks and both native discovery probes passed instead.

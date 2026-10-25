# Markdown installation and removal records

Each scope owns its history at `.agent-skills/history/<32-character-operation-id>/operation.md`. Project and user installations have separate histories. Uninstall retains all earlier events and adds a new removal event.

Every record has JSON-valued Markdown frontmatter and a readable table. Parsing needs only the Python standard library. Schema 1 contains:

| Field | Meaning |
|---|---|
| `id`, `sequence` | Unique operation ID and consecutive per-scope ordering |
| `status` | `COMMITTED`; only completed changing operations enter history |
| `timestamp` | UTC ISO timestamp |
| `operation` | `install` or `uninstall` |
| `pack`, `agent`, `scope`, `root` | Selected collection, adapters and exact scope |
| `source`, `manifest_sha256` | Actual local pack and manifest hash for installation; null for uninstall |
| `entries` | Exact target, action, before/after tree digests, previous install record ID and direct retained-tree path |
| `backup` | Retained-content transaction directory, or null if no content was replaced/removed |

Actions are COPY, REPLACE WITH BACKUP, ADOPT MATCHING COPY, REMOVE and MISSING. A null digest means absent. Tree digests include regular-file hashes sorted by exact relative filename, plus directory names, including empty directories. The filename sort is independent of Windows path ordering. QA generated `kit-location.txt` participates in the installed digest. The original source manifest remains a separate hash.

Ownership is rebuilt by replaying the consecutive committed events. A matching name or `SKILL.md` alone does not grant ownership. A removal clears ownership; a later reinstall records it again. Missing, malformed, duplicated or reordered history prevents a mutating operation. Keep history intact. These are local editable records, not signed or tamper-proof audit evidence.

The skill changes and their new record share a recoverable transaction. While `.skills-install-transaction/` exists, its journal is authoritative and further installs/removals are blocked. Prepared recovery removes provisional history and restores old skill trees. Committed recovery keeps the success record and finishes backup archival.

Previews, cancellations, validation failures, rolled-back attempts and unchanged reruns do not create success events or modify scope history. Their terminal output is the attempt evidence. Abrupt interruptions retain the transaction's `journal.json`; do not interpret a staged/provisional record as a completed operation. Power-loss durability and cryptographic publisher authentication are not established.

Content backups live separately at `.skills-install-backups/<operation-id>/`. The `journal.json` there maps numbered backup entries to former paths. Backup retention is deliberate and unbounded; cleanup requires an explicit owner action. Markdown records contain absolute local paths and can be private. The tool neither commits them nor changes the application's ignore rules.

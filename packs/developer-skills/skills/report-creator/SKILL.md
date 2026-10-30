---
name: report-creator
description: Discover reporting needs and design or implement application report pages with role-aware data boundaries and styled PDF and Excel exports. Use for business reporting features rather than narrative project status reports.
---

# Report Creator

Input: Target application, selected report or workflow, requested command and detail level, and available source/runtime access.

Output: An evidence-linked report inventory, specifications, authorized implementation, or verification results. Keep source-reviewed, automated, rendered, browser, and operational evidence distinct.

## Commands and scope

These are agent-chat commands, not executable shell commands. In Codex use `$report-creator`; in Claude Code use `/report-creator`.

| Command | Behavior |
|---|---|
| `scan [scope]` | Read-only discovery of features, reporting needs, existing coverage, roles, data boundaries, and gaps. |
| `plan <report-or-scope> --detail mid\|detailed` | Specify the selected reports, document design, permissions, generated-files page, retention, acceptance, and unresolved decisions without application edits. |
| `build <report-or-scope> --detail mid\|detailed` | Implement the selected reporting scope through existing owners and verify it. This command supplies implementation authorization; do not ask for approval again for settled in-scope decisions. |
| `verify <report-or-scope>` | Verify existing reporting against its agreed specification. Report gaps without expanding into implementation. |
| `help` | Explain commands, detail levels, required input, and evidence limits without edits. |

Bare invocation defaults to `scan`. If no target can be inferred, ask for the application path or scope. Default report content to `mid` when omitted and state that choice. Reject unsupported detail levels or ambiguous command combinations without silently building. Natural-language implementation requests already authorize their stated scope; commands are not an extra approval gate.

Scan and plan do not edit application code, generate exports, change permissions, install dependencies, or create state files unless the task requests a saved artifact. Build only selected reports and their required integration. Do not implement every discovered candidate, alter unrelated workflows, or deploy, publish, install globally, commit, or change branches without task authorization.

## Detail levels

Detail controls report content, not scan coverage, security rigor, correctness, or chat verbosity.

- **mid:** Purpose, reporting period, effective filters, headline totals, essential categorical breakdowns, essential record columns, metric notes, and the shared document/access/lifecycle requirements below.
- **detailed:** Mid content plus data-supported trends or comparisons, additional useful breakdowns, exceptions, reconciliation, drilldowns, record fields, and fuller metric/column explanations. Omit unsupported analysis and explain unavailable history instead of inventing it.

Neither mode may omit PDF or actual `.xlsx` support, clean document structure, applicable status/type colors, grouped counts, filter disclosure, data isolation, or the Generated Reports page and expiry behavior. Include only meaningful categories and sections supported by the report's purpose and source data.

## Workflow and reading map

1. Establish target roots, current changes, requested scope, relevant instructions, and existing report/query/export/settings owners. Trace routes through services, authorization, queries, renderers, jobs, storage, and cleanup before editing.
2. For scan, plan, and build, read [discovery and metrics](references/discovery-and-metrics.md). Cross-check application features beyond report folders. Identify report necessity using evidence, not page existence.
3. For scan, plan, build, and verify, read [access and retention](references/access-and-retention.md). For plan and build, also read [document design](references/documents.md). Extend existing owners instead of creating a parallel report engine or exporter.
4. For build and verify, read [verification](references/verification.md) and the references relevant to affected behavior. Run the target's focused checks and inspect representative rendered PDF and workbook artifacts.
5. Report changes or recommendations, executed proof, coverage gaps, and remaining decisions. Stop at the requested command and selected scope.

## Non-negotiable contracts

- One explicit reporting specification defines audience, record grain, date semantics, filters, metrics, sections, columns, colors, and export limits. Resolve material business or sharing-policy uncertainty before dependent implementation; continue independent work.
- Preview, totals, PDF, and Excel use the same validated semantics and authorized scope. Declare whether separate requests refresh the data; never promise a frozen snapshot merely because they share a builder.
- Inspect real roles and effective permissions. Derive tenant/store/branch/self boundaries on the server. The same role across different scopes never grants shared data access.
- Both exports disclose effective filters and generation time. Color-coded status/type labels and grouped counts use the target's established meanings consistently.
- Full-report PDF order is cover, contents starting on page two, summary on a separate following page, then sections. Excel uses Cover, Contents, Summary, Breakdowns, record sheets, and Reading Notes with native spreadsheet usability.
- Always provide a dedicated Generated Reports page; reuse or extend an existing suitable page. Preserve generated files for repeat downloads by permitted users. Sharing requires access to the whole file's stored data and fields; a shared role or guessed URL is insufficient.
- Default availability is 24 hours from successful generation, configurable through the backend's settings or environment pattern. Recheck permission and expiry on every file access; cleanup timing must not extend access or delete files before their promised window.

Limits: This skill supplies portable engineering instructions, not a framework, reporting service, executable command runner, or proof of production behavior. It requires no other installed skill, private path, fixed UI library, or additional dependency. Use the target application's tools and existing policy. Ask only for unresolved material choices, never for permission already supplied by the task.

---
name: system-settings
description: Inspect an application's workflows and configuration to decide whether runtime system settings are justified, then plan, implement, or verify scoped settings with category-based loading and change auditing. Use for new or existing application settings rather than deployment configuration, secrets, or personal preferences.
---

# System Settings

Input: Target application, requested operation and scope, existing decisions, and available source/runtime access.

Output: An evidence-linked necessity assessment, selected settings specification, authorized implementation, or verification report. A valid assessment can conclude that no new settings are needed.

## Commands and authorization

These are agent-chat requests, not terminal commands. Use `$system-settings` in Codex or `/system-settings` in Claude Code.

| Command | Outcome |
|---|---|
| `scan [scope]` | Inspect the system in detail; assess necessity, existing coverage, candidates, exclusions, and gaps without application edits. |
| `plan [scope]` | Specify justified settings, ownership, categories, access, auditing, loading, compatibility, and acceptance without implementation. |
| `build <scope>` | Inspect first, then implement the selected settings scope and its necessary integrations. |
| `verify [scope]` | Check existing work against its requirements without expanding into implementation. |
| `help` | Explain usage and boundaries without edits. |

Bare invocation defaults to `scan`. Infer the target from the current application or supplied path; ask only when it cannot be established. With no narrower scope, discovery covers the application, including separate frontend/backend repositories. Missing source or runtime access is a coverage gap, not evidence that a feature is absent.

Scan and plan are read-only unless a saved artifact is requested. Build or an equivalent natural-language implementation request authorizes its stated scope; do not introduce a second approval gate. Discovery does not authorize implementing every candidate. If an unbounded build request requires material business-policy choices, present the candidate specification and resolve those choices before dependent edits; continue independent work. Verification reports defects without silently fixing them.

Creating or installing this skill does not authorize modifying the target application. Do not deploy, publish, commit, change branches, install globally, or modify production data without task authorization.

## Workflow

1. Establish actual repository roots, current changes, local instructions, requested scope, and source access. Preserve unrelated work.
2. For scan, plan, or build, read [discovery and necessity](references/discovery.md). Trace business behavior and consumers beyond files named settings. Classify the current implementation as absent, partial, or established using evidence.
3. Give a reasoned outcome: **create**, **extend**, **no new settings needed**, or **insufficient evidence**. Distinguish existing useful coverage from missing capability. Do not recommend a settings platform solely because the application lacks one.
4. For plan, build, or verify, read [implementation and verification](references/implementation.md). Reuse the existing configuration, persistence, authorization, UI, and audit owners. Create only missing pieces required by the selected scope.
5. Implement only when authorized. Trace each selected key from declaration and storage through effective-value resolution to real runtime consumers and the administrative interface, where in scope. Verify relevant boundaries and report actual proof.

## Essential contracts

- System settings are administrator-controlled runtime business policies with a justified operator need. Keep deployment configuration, credentials, fixed protocol/security invariants, personal preferences, and tenant/store-specific policy in their appropriate owners.
- Define each supported key in a typed declaration or the project's equivalent: scope, category, type, units, default, allowed values/bounds, validation, and application timing. Prefer predefined keys over an arbitrary key/value editor. Only introduce user-defined keys if the product explicitly requires them.
- Backend authorization and validation govern every read and write. Category metadata, counts, search, and history must respect the same scope. Administrative grouping never makes a setting public or safe to expose to client applications.
- For a web administration page, prefer one page with **Settings** and **Change history** tabs. Initial loading fetches authorized category metadata only. Expanding a category fetches only its settings; opening history fetches its paginated records. Preserve the application's established design and any explicit layout requirements.
- Category membership has one authoritative owner used by listing, filtering, counts, and history. A collapsed card over a bulk fetch is not category loading. Keep drafts and loaded state separate from which panel is open.
- Look for existing settings history and central auditing before adding storage. Reuse compatible audit recording, actor context, authorization, retention, and presentation. Already-covered settings do not need another logger or a second audit event.
- A successful mutation and its audit evidence must commit together. Preserve existing history/API contracts when extending central audit coverage. Log authorized actor, key/scope, effective previous and new values, and time without exposing secrets in any history, summary, or payload.
- Prevent stale edits and conflicting concurrent changes from producing false history. Preserve approved defaults, units, data, and runtime behavior when migrating existing constants or settings. Document when changes take effect and how cached readers converge.

## Deliverables and stopping condition

For discovery, return the necessity verdict, inspected feature/consumer coverage, existing owners, a candidate/exclusion table with source references, and unresolved material decisions. State unavailable evidence explicitly. Do not create state files by default.

For planning, add the selected key specification, proposed request/data flow and layout, audit reuse or minimal missing audit design, compatibility/recovery approach, and concrete acceptance conditions.

For build or verification, report changes, executed checks and results, and remaining prerequisites or gaps. Separate source review, automated tests, browser interaction, database concurrency, and production proof. Stop at the selected scope; do not proceed from scan to build automatically.

This skill provides portable engineering instructions, not a settings service, framework, command runner, or proof of operational behavior. It requires no other installed skill, private path, fixed frontend library, or dependency of its own.

## Generated artifacts

Apply this section only when the workflow saves generated reports, logs, previews, or run evidence. Use a stable skill-owned root in the target workspace, never the installed skill directory. Allocate each new run with an exclusively created `YYYYMMDDTHHMMSSZ-<unique-id>/` directory (UTC); preserve earlier runs and resume the identified active run. Reject linked paths, traversal, and unrelated same-name folders.

Before saving inside Git, resolve the intended repository root, refuse already tracked output, and inspect its `.gitignore`. Preserve existing bytes and line endings; append a root-anchored rule for only the generated output root when needed, creating `.gitignore` if absent. Verify exclusion with `git check-ignore`; never untrack files automatically. Outside Git, disclose that exclusion is unverified; workflows requiring Git retain that prerequisite. If safe storage or required exclusion fails, report the exact limitation before saving and use chat only when this workflow permits it.

Preserve existing state schemas, version identifiers, historical files, and resume paths; timestamp new run evidence beneath its existing owner without an implicit migration. Application source and project documents explicitly intended for version control retain their own contracts. This section does not authorize extra output for a chat-only request or expand the workflow's scope.

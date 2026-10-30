# Access, generated files, and retention

## Discover and enforce the actual policy

Inspect authentication, role definitions and assignments, permission resolution, route guards, service checks, tenant/store/branch membership, self-only scopes, sensitive-field rules, and any administrative bypass. Map report generation, listing, preview, download, sharing, and retention administration to existing capabilities; avoid inventing an unrelated role system.

Produce a role/permission matrix that also identifies data scope and field/section restrictions. Multiple roles may legitimately share a report, and identical role names in different stores must remain isolated. An administrator label does not automatically authorize every tenant's private report; honor the actual policy.

Enforce row and column boundaries before aggregation and rendering. Derive immutable ownership/scope identifiers from authenticated server context; never trust a submitted tenant/store/user ID to widen access. Filtered totals and even zero/nonzero counts are protected data.

Check current authorization when requesting and executing queued generation, listing metadata, previewing artifacts, reading status, downloading PDF/Excel, or using alternate packaging. An account removal, permission revocation, or scope transfer must not leave an old file accessible. Jobs should fail safely or use an explicitly defined restricted result if the generator's permissions changed; never produce a silently broader artifact.

## Shared downloads

Default design: allow other users only when an explicit application sharing policy permits them and their current access covers the artifact's complete stored scope, sections, rows, fields, and sensitivity. Matching a role, possessing a link, or merely holding a generic reports permission is insufficient.

Store enough audience/scope and content-policy metadata to evaluate an immutable artifact later. Compare the recipient's current policy against that stored scope; do not assume rerunning the current query proves access to historical rows. When access cannot be established, deny the original artifact and offer a separately generated permitted report.

Reuse an existing explicit sharing policy. Where a build request adopts this default and the complete audience can be derived, implement it without asking again. If cross-user sharing authority or necessary scope metadata is unknown, mark that policy gap and continue independent work; do not broaden creator-only behavior by assumption. Plans must distinguish supported sharing from unresolved access.

Keep files in private storage. Protect both identifiers and direct URLs with server authorization; any temporary storage URL must be appropriately restricted, short-lived, and no longer valid than the artifact's expiry. Avoid shared/public caching of private file responses. Keep create/share/download/expiry audit events through existing logging owners without recording sensitive row contents.

## Dedicated Generated Reports page

Always provide a dedicated Generated Reports route/page for retained artifacts. Reuse or extend an existing suitable exports/history page rather than building a second registry. An embedded My exports card alone is not a substitute for the dedicated page.

List only entries whose metadata the viewer may see. Provide My reports and Shared with me scopes when sharing exists; use project navigation and role-aware visibility rather than hardcoding separate pages for every role.

Show report title/reference, PDF or Excel format, permitted generator/audience metadata, period/filter context, colored lifecycle status, record count, file size, requested/generated times, and expiry. Use search/filtering/pagination through existing components where useful. Provide repeat download while permitted/ready, progress for queued/running jobs, safe failure explanations, explicit expired states, and regeneration through the existing report flow.

Treat queued, running, ready, failed, and expired as lifecycle concepts and map them to the target's existing enums instead of introducing duplicate states. Preserve safe empty/loading/error states and accessible actions/status text. A hidden button is never the download authorization check.

Download the stored artifact without regenerating it. A regeneration creates a new artifact/reference, its own generation time, scope, and retention window. Do not silently change an old file's content or audience.

## Durable background generation and progress

For both PDF and Excel, submitting Generate must create a durable export request with its validated selection, generator, authorized scope, and a stable reference. Return an accepted response promptly using the application's API conventions, with that reference and a status/page location. The request handler must not wait for document rendering. A short submission indicator is appropriate only while acceptance is unresolved.

Reuse the application's backend queue, worker, transaction, and job-status owners. Enqueue after the export request commits, using the existing outbox or reliable dispatch/reconciliation pattern so an accepted request cannot be silently lost between database commit and queue publication. A browser worker, local promise, request-scoped background callback, or in-memory task alone does not provide durability. If no durable job facility exists, identify the prerequisite and implement the smallest persistent worker pattern appropriate to the authorized scope; never claim background delivery through a synchronous fallback.

Keep the accepted job independent of the browser connection. Reloading, navigating away, closing the tab, or returning later must not cancel it or require another Generate click. After acceptance, show the request's row on Generated Reports and link or navigate to that page using existing navigation patterns. Persisted job state, not the originating page, owns progress. Fetch current authorized status on entry/reload; optional inline progress or completion notifications may supplement that page.

The Generated Reports table must include a Status field and a Progress field or clearly labelled combined cell. Show Queued, Generating/Running, Ready, Failed, and Expired using existing lifecycle mappings. While processing, show the actual stage, such as Reading records, Building summary, Rendering PDF/Writing workbook, or Saving file. Include processed counts and percentages only where the worker has a trustworthy denominator and defined units. Never invent progress, an ETA, or use a preview row count as a generation total. When total work is unknown, show an indeterminate indicator with the stage and last update rather than implying a stalled task is progressing.

Persist progress at useful bounded intervals through the job/export owner, including current stage, measured counts where available, started/completed times, and last progress or heartbeat time. Keep progress scoped and avoid leaking row values through status messages. Use the existing realtime channel when available with bounded polling fallback; refetch persisted state after reconnect, stop polling terminal jobs, and clear subscriptions/timers on unmount. Polling failures mean status is temporarily unavailable, not that generation failed. Announce meaningful status transitions accessibly without announcing every progress tick.

Use the existing job retry, timeout, heartbeat/lease, and recovery rules. Detect stale or worker-interrupted jobs and expose truthful delayed/retrying/failed feedback instead of leaving Running indefinitely or promising a deadline without evidence. Protect against duplicate submission retries with the existing request-idempotency mechanism; disabling a button alone is insufficient. Distinguish a deliberate new generation from retrying the same submission. Make worker execution idempotent, with atomic claiming/finalization and ownership protection so concurrent or retried jobs cannot publish duplicate artifacts, regress terminal state, or overwrite a completed file.

Mark Ready only after the complete file is safely stored and its metadata committed. Failed attempts must not expose partial files; retain safe errors and offer an authorized retry/regeneration through existing flows. Start the configured 24-hour retention window only at successful completion. Report missing worker, queue, storage, or scheduler prerequisites explicitly; a queued row alone does not prove a functioning worker.

## Retention configuration and clock

Default availability: **24 hours from successful completion**, not from request, first download, or last download. Keep any existing generation timeout separate from file-retention time.

Use the application's backend configuration/settings owner. Prefer an existing setting; if both a persisted setting and environment fallback are supported, document one precedence, such as authorized setting override, environment default, then 24 hours. Use existing key names and add templates/admin controls only when required. A browser field or request parameter must not set retention arbitrarily.

Validate a finite positive duration using the application's normal setting bounds; report invalid configuration clearly. Limit changes to authorized configuration administrators. Do not allow zero, negative, invalid, or unlimited values by accident. Record the effective duration and absolute expiry for each completed export, using the server's time conventions.

Repeated downloads do not extend expiry. Setting changes affect future completed artifacts by default; do not silently shorten or extend existing promised windows. An explicit policy can override this, but it must be documented and authorized.

At `now >= expires_at`, deny file preview/download and temporary URLs immediately, even if the cleanup worker is late. Show a clear expired response/state using existing API conventions. Scheduled cleanup deletes the file and alternate packages idempotently; retained audit/history metadata follows the project's separate policy.

Verify workers, scheduler registration, storage permissions, and configured cleanup cadence. Preserve availability until expiry even if nobody has downloaded the file. Reconcile competing abandoned-file cleanup jobs so they cannot remove a ready report early.

The BALE reference uses creator-only exports and a 72-hour setting default; LMS uses creator-only exports and a 24-hour setting but also sweeps never-downloaded files after one hour. Neither retention/sharing policy should be copied as the new default. Existing deployments need explicit compatibility treatment for already generated files rather than an unannounced policy migration.

The retention window controls server availability only. It cannot delete copies users already downloaded.

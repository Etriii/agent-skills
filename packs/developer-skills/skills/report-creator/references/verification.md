# Verification and stopping conditions

Use the target's nearest meaningful tests, linters, type checks, and build checks for affected owners. Capture baseline failures and preserve unrelated changes. Do not claim application delivery from a skill installation, source scan, or successful process exit alone.

## Discovery and specification

Cross-check routes/navigation, roles, workflows, existing registries, and source queries. Include covered/unnecessary/unknown candidates and explicit gaps. Verify that mid/detailed alter content rather than weakening discovery, permissions, formatting, or lifecycle behavior.

Trace representative metrics back to authoritative records. Test date/time-zone boundaries, empty results, unknown and zero-count categories, duplicate joins, cancellations/reversals, money rounding, exclusive status reconciliation, overlapping tags, and cross-section counting units as relevant. Verify full-population counts even when preview/PDF rows are capped.

Changing filters/sections/columns/scope must make an old preview visibly stale. Confirm effective defaults and readable filter descriptions match queries and exports. Check clear behavior for unsupported list filters.

## Access and retained artifacts

Use permitted isolated accounts/fixtures to cover:

- A generator, a permitted cross-user recipient, a denied user, two users with the same role in different scopes, and applicable self-only/field-restricted roles.
- Direct list/status/file/download URLs, modified IDs/filters/scope, alternate formats/packages, and sensitive metadata. UI hiding alone proves nothing.
- A recipient allowed some but not all included rows, fields, or sections: deny the original file; do not remove data from an existing PDF in transit.
- Role removal, scope transfer, and permission revocation before a queued job runs and after a file becomes ready. Recheck complete stored-artifact access at download.
- A repeat download returns the same artifact without another report build; regeneration creates a new reference. Use file hashes or equivalent artifact identity.
- Queued/running/failed/expired states and worker retries, including no unauthorized or partial-ready file exposure.

Verify default 24-hour availability beginning at successful completion. Use a controlled clock for just-before, exact, and after-expiry checks. Include slow generation, repeated downloads, delayed cleanup, setting overrides, invalid durations, and a ready file nobody has downloaded. Ensure competing cleanup cannot erase it early.

Confirm setting changes follow the stated future-artifact rule and that private storage access cannot bypass expiry or authorization. Run the existing cleanup/job tests and verify scheduler registration. Distinguish fixture proof from an actually observed scheduled execution.

## PDF artifacts

Generate representative permitted fixtures with short and long records, empty results, many sections, long labels, meaningful status/type categories, Unicode/currency symbols, and a capped dataset.

Render the actual PDF to inspect pages visually using available project/document tools. Check cover on page one, contents beginning on page two and spanning cleanly, a separate summary after contents, accurate contents/footer numbers, section hierarchy, repeated table headers, clear cards/rows, readable color labels/contrast, filters, totals, and cap notices.

Check for clipping, tiny text, broken glyphs, split labels, awkward page breaks, accidental blank pages, and incorrect orientation. Text extraction and HTML-template assertions help content checks but do not prove visual layout. Missing rendering capability remains an explicit visual-verification gap.

## Excel artifacts

Open the actual `.xlsx` with an available workbook reader. Verify sheet order, internal navigation, row counts, headers, filters, frozen panes, numeric/date types, literal source text, preserved identifiers, correct formulas/cached results when present, and status/type fills.

Compare totals, categories, filters, units, and scope with the PDF/preview using the same fixture or documented snapshot timing. Check empty and oversized datasets, valid unique sheet names, and representative long text. Inspect workbook layout visually with an available viewer/rendering tool; XML/read-back proof alone is not visual acceptance.

Use trusted fixture text beginning with formula markers to confirm it remains literal. Verify that trusted generated total formulas reference the intended rows and do not include their own total row.

## Report completion precisely

State selected reports and integration delivered, scope/role coverage, executed commands and results, rendered artifacts reviewed, required runtime configuration, and remaining decisions or prerequisites.

Do not declare complete when data isolation, business metrics, generated-file access, expiry, or required document outputs remain unresolved. Separate automated proof from browser, assistive-technology, worker/scheduler, operator, and production proof. Stop after the authorized command; do not start another report, deployment, installation, commit, or publication without authorization.

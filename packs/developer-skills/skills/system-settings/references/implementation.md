# Implementation and verification

Read this for plan, build, and verify. Apply the parts relevant to the selected scope and the target's architecture.

## Declarations, persistence, and runtime behavior

Use existing typed declarations, domain services, repositories, transactions, and configuration resolution. If none exist, build a small declaration/resolution layer and persistent overrides in the responsible module; do not introduce a general configuration platform for a few keys.

Specify key, label/description, category, type, units, default, bounds/choices, scope, access, effective time, consumers, and sensitive-data treatment. Keep category membership authoritative on the server or in a shared contract both query and presentation layers use. Localized labels may remain frontend-owned. Counts come from authorized declarations, including keys using defaults, rather than only customized database rows. Reject unknown keys and categories and unsupported input types.

Validate on the server, including relationships between settings when needed. Use exact decimal/minor-unit types for money and precise representations for other domain values. Define missing/invalid stored-value behavior according to the domain: a safe declared fallback where appropriate, explicit refusal when continuing would violate a critical invariant. Surface configuration faults without exposing sensitive values.

Preserve current behavior when moving a literal or environment-backed value into runtime settings. Update actual consumers, not just forms. Avoid retroactively recalculating completed orders, signed documents, or other historical records unless explicitly required. Define when new values take effect for new requests, running jobs, and offline clients.

Keep default-only keys usable without stored overrides. Reuse migrations and seed conventions without overwriting existing administrator choices. Do not rewrite historical migrations. Explain schema/code rollout compatibility and recovery; preserve existing keys, stored values, API callers, and history. Do not drop or consolidate audit tables as an incidental cleanup.

Cache reads only with a defined freshness contract. Inspect per-request versus shared/process caches and multi-worker/offline consumers. Invalidate or version shared cached values after successful commit, not before it. Avoid claiming immediate platform-wide changes if workers or offline clients apply them later.

## Category loading and interface

When a web settings page is in scope, prefer one page with Settings and Change history tabs, following existing component and responsive patterns. Apply the category navigation contract below within that scope. Headless systems do not require a web UI merely to use this skill.

The Settings tab initially requests authorized category IDs, displayed names, descriptions, counts, and any required non-value navigation metadata. Searching, grouping, scrolling, and selecting letters operate on that metadata without fetching settings or history. Do not preload values or history in the background. Expanding a category fetches only that category's authorized settings; filter persistence queries before retrieval and merge declared defaults. Keep an existing unfiltered endpoint compatible if callers rely on it. Register static category/history routes ahead of dynamic key routes where the router requires that ordering.

Maintain per-category loading, loaded, error/retry, and in-flight states, preserving existing request deduplication and retry behavior. Keep drafts, loaded values, and expansion state outside filtered or temporarily unmounted views, keyed by stable category identity. Filtering, collapsing, and switching tabs must preserve that state; collapse changes only the selected category's expansion flag. Clearing a filter restores the prior expansion choices without refetching loaded categories. A refresh or late response must not overwrite dirty edits.

Scope request identity and cached state to category, account, tenant, and authorization scope. Clear privileged metadata, values, drafts, history, and associated UI state when the account or authorization scope changes; cancel or discard old in-flight responses so they cannot repopulate cleared state. Use explicit refresh or existing invalidation conventions for freshness.

Use keyboard-operable category controls with expanded state and associated panels. Keep loading/error status and validation accessible. Show type-appropriate controls, units, defaults, current values, and clear save/reset behavior. Prefer existing per-setting save semantics; use atomic batch saves only when required to keep related values valid.

Fetch history only when its tab or a setting's View history action opens. Keep results server-paginated and filterable by category/key and, where justified and authorized, actor/date. History navigation and labels must work without fetching every current setting. Use lightweight permitted key metadata or self-describing history records; retain sensible labels for retired keys. A View history action selects the tab and filter without discarding drafts.

After a successful save, replace that row with the server's canonical value and revision. Refresh visible affected history or mark hidden history stale; do not eagerly load hidden tabs. Make partial failures and stale revisions explicit.

## Category discovery and navigation

Derive this presentation from the existing authoritative authorized category metadata. Grouping is a view of that metadata, not another category-membership owner. Use displayed names and descriptions, including the active locale's labels where available.

### Search and alphabetical sections

Place a clearly labelled category search field above the categories. Filter names and descriptions immediately as input changes, ignoring capitalization and surrounding query whitespace; an empty or whitespace-only query shows all authorized categories. Show the matching category count, an accessible clear-search action, and an accessible no-results status. Announce result changes without moving focus unexpectedly. Clearing restores the full authorized list and leaves focus usable.

Sort by displayed name using locale-aware, case-insensitive collation. Derive visible initial-letter headings from the first grapheme of each trimmed displayed name, uppercased in the display locale when it is a letter. Use `0–9` for leading digits and `#` for other or empty initials; place those buckets after the letter sections, in that order. Order letter sections and names within each section with the same collator; use stable category IDs to break collation ties. This yields A with its categories, then B with its categories, and so on in Latin locales. Document any established locale-specific grouping convention reused instead, including deterministic non-letter handling.

Render only sections containing current matches. Derive the section headings and navigation entries from the same filtered, sorted view; no empty headings or stale letters. Keep stable category and section identities so filtering and reordering do not destroy loaded state.

### Alphabet navigation and scrolling

Provide a sticky alphabet index on the right containing only represented letters from the filtered view, plus the populated non-letter buckets when present. Use a compact horizontal strip on narrow screens when the rail would crowd or overlap content. Keep every entry reachable, with usable touch targets and no overlap with editing controls.

Selecting an entry scrolls to its heading in the actual content scroll container. Account for sticky headers and search controls using the current occupied top offset, including responsive changes. Respect reduced-motion preferences by avoiding animated scrolling when requested. Letter selection navigates without expanding categories.

Highlight the current section as the user scrolls: it remains active until the next section heading reaches the content area's top boundary below sticky controls. Do not switch merely because the next section enters the viewport or because an expanded category has a large visible area. Before the first heading reaches that boundary, use the first populated section. At the scroll end, activate the final populated section if limited remaining scroll prevents its heading from reaching the boundary; no matches means no active entry.

Recompute positions, offsets, and the active entry after expansion, collapse, filtering/clearing, tab restoration, resizing, and content-height changes, including asynchronous category loading. Remove stale targets when sections disappear. Use existing scrolling/measurement primitives; update against actual layout rather than fixed heights or a one-time snapshot.

Use a labelled navigation landmark and keyboard-operable links or buttons with accessible target names, visible focus, and an accessible current-entry state such as `aria-current="location"`. Keep active styling distinct from focus. Preserve logical focus on filtering and layout changes; expose section headings as real headings and avoid trapping keyboard or touch navigation.

## Audit and concurrent writes

Extend the existing audit recorder and settings history where they already fit. Preserve separate permissions: access to settings history does not imply access to the entire central audit trail. Link to richer central records only when authorized. If both specialized history and central audit already exist, preserve their contracts and record each intended event once.

If no auditing exists and change history is in scope, create the smallest append-only settings-change record through the existing transaction owner. It needs no unrelated application-wide audit platform. Record scoped key, effective previous/new values, authorized actor or explicit system identity, and occurrence time; use existing request/correlation metadata when available. Do not trust actor IDs supplied in an arbitrary request body.

The effective previous value may be a declared default when no override exists. Keep that distinct from a raw stored null. Preserve legacy history meaning; where needed, add an explicit field or rendering distinction rather than relabeling old records. Reject unchanged writes or distinguish intentional reapplication according to existing policy instead of silently changing established event semantics.

Enforce authorized writes server-side. Protect against stale administrators using the target's revision/conditional-update mechanism or an equivalent check. Capture the actual previous value and create audit evidence inside the protected mutation transaction; a frontend confirmation alone does not prevent lost updates. Handle first-write races with the existing unique-key constraint and conflict/retry pattern. Version checks, value updates, and audit creation must agree on one committed change.

An audit failure must roll back the setting mutation. For an external audit sink, use an existing transactionally persisted outbox or equivalent durable mechanism rather than claiming a remote send is atomic with a database write. Do not add a broker when local transactional history is sufficient.

Keep secrets outside ordinary system settings. Redaction must cover specialized history, central audit changes, summaries, logs, API responses, and snapshots if sensitive fields already exist. Respect existing retention/access policy; do not silently shorten it or expose request metadata through a broader settings permission. History remains append-only through ordinary application operations; retention cleanup follows explicit policy. Reverting a setting is a new authorized audited change, not an edit to history.

## Smallest sufficient proof

Use the target's existing tests and runtime tooling. Cover affected behavior rather than testing instruction wording:

- Declared defaults without overrides; valid type/unit round trips; invalid/unknown values rejected; scoped access and metadata isolation.
- Runtime consumers using effective values; preserved defaults and historical records; required migrations and actual cache freshness where changed.
- Initial page requesting authorized metadata only; search, grouping, scroll, and letter selection issuing no settings/history requests; expansion fetching only selected-category settings with existing deduplication and independent retry.
- Drafts, loaded values, and expansion choices surviving filtering/clearing, collapse, and tab switches; late responses not overwriting dirty edits; account/authorization changes clearing privileged caches and rejecting stale in-flight results.
- Locale-aware, case-insensitive displayed-name sorting with stable ties; populated-letter grouping and deterministic digit/other buckets, including localized names; headings and index entries tracking the same filtered metadata.
- Immediate name/description search ignoring case and surrounding whitespace; correct matching category count, clear action, whitespace-only queries, accessible no-results status, and restoration of prior category state.
- Letter jumps landing below sticky headers/search controls; current-letter highlighting changing only at the top boundary or the documented scroll-end fallback. Exercise long expanded categories, short final sections, expansion/collapse, asynchronous loading, filtering/clearing, tab restoration, resizing, and page bottom.
- Right-side sticky index and compact horizontal strip at narrow widths, without content overlap; labelled search, keyboard operation, visible focus, accessible active state, usable touch targets, and reduced-motion behavior.
- History loading on demand with pagination/filtering independent of unloaded settings; newly saved changes appearing when visible or next opened.
- Authorized actor and correct effective old/new values; refused writes leaving no success event; audit failure leaving no mutation; stale-write/first-write races preserving truthful history.
- Existing settings, audit, and public/offline API contracts remaining compatible. Verify keyboard controls and responsive editing when UI is in scope.

Use database integration proof for actual transaction rollback and concurrency guarantees; fake repositories alone cannot establish them. Report automated unit/component checks separately from actual browser interaction and network verification. Exercise desktop and narrow layouts, keyboard/touch navigation, scroll geometry, state preservation, and request timing in a browser; retain network evidence that metadata-only navigation loads no values/history and expansion requests only its category. Static inspection and mocked requests alone do not prove these behaviors. If a required service, account, browser, database, or permission is unavailable, report the exact unverified condition and any narrower executed checks. Do not report production behavior from local tests.

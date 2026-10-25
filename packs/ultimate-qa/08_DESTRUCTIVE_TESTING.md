# 08 – Destructive testing: try to break it on purpose

Normal QA asks "does it work when used properly?". This file asks "what happens when it is used improperly, overloaded, interrupted, or attacked?" – the questions that decide whether the system merely works on a good day or actually holds up.

Output: `07_Destructive_Test_Report` (template §O in `03_OUTPUT_TEMPLATES.md`). Findings are numbered `D-001`, `D-002` … and are permanent for the project like every other finding number.

---

## 1. The gate – this never runs by accident

Destructive testing runs **only** when all of these are true. If any one is missing, write nothing destructive, mark the whole section `NEEDS-MANUAL` in the audit report with the reason, and carry on with the normal review.

| Gate | Requirement |
|---|---|
| **Permission** | `DESTRUCTIVE_TESTING: yes` in `qa-findings/requirements/01_RUN_SETTINGS.md`, **or** the user said yes in the intake or in chat. Default is `no`. |
| **Target** | A local or staging environment named by the user. **Never production.** Never an environment you are not certain about – if the URL, the database name or the API keys look production-like, stop and ask. |
| **Data** | Test data only. If the staging database is a copy of production personal data, treat it as production for privacy: no exports, no screenshots of real people, no data in evidence files. |
| **Third parties** | Sandbox credentials only. Never generate load against a live payment gateway, SMS provider, email provider, map API or any external service you do not own – simulate their failure locally instead (block the host, point the base URL at a dead port, use their sandbox's error codes). |
| **Recovery** | You know how to put the environment back: a database dump taken first, a seed/reset command, or the user's confirmation that the environment is disposable. Record which one in the report. |
| **Blast radius** | Only the target app. Nothing that affects the machine's other services, the network, or anyone else's environment. |

**Always forbidden, whatever the settings say:** anything against production or against a system the user does not own; sustained load that constitutes an attack on shared infrastructure; deleting backups; disabling security controls and leaving them disabled; leaving the environment broken at the end of a run; any technique whose purpose is to hide the testing from operators.

**Announce, then run.** Before the first destructive test, say in one line what you are about to do, to which environment, and how you will restore it. After the run, confirm the environment was restored and how you verified it.

---

## 2. Method

1. **Snapshot.** Take a database dump / note the reset command. Record the app version or commit.
2. **Run one test at a time**, from the least to the most disruptive: input abuse → boundaries → concurrency → resource pressure → dependency failure → state corruption → recovery. One test, one observation, one line of evidence.
3. **Watch three places** on every test: what the user sees, what the logs say, and what the data looks like afterwards. Most of the value is in the third: a request that returns a friendly error while leaving a half-written row is worse than a crash.
4. **Restore between blocks** if a test leaves the environment dirty in a way that would confuse later tests.
5. **Stop immediately and report** if: real user data is affected; a third-party service starts responding with rate-limit or abuse warnings; the environment cannot be restored; or you find a way to affect anything outside the target app. Write what you did up to that point.
6. **Restore and verify** at the end: reset, then walk one core journey to prove the environment works.

---

## 3. What to try

Each block lists the probe and what a healthy system does. Report a `D-nnn` finding whenever the actual behaviour differs, and say which block it came from.

### D-A. Input abuse
- Very long strings (10k characters) in every text field, including names and search boxes.
- Wrong types: text in a number field, a negative quantity, `0`, a date in the year 1900 and 2999, `29 February` in a non-leap year.
- Unicode: emoji, right-to-left marks, zero-width characters, combining accents, `NULL` bytes, four-byte characters in a database column that only takes three.
- Format strings, template syntax (`{{7*7}}`, `${...}`), path traversal (`../../etc/passwd`), HTML and script tags, SQL fragments, command separators – in fields, in URL parameters, in file names, in headers.
- Files: a file with the wrong extension, a file with a double extension, a 0-byte file, a file larger than the limit, an archive bomb, an image with a script payload, a file name of 300 characters.
- **Healthy:** rejected with a clear message at the boundary, nothing stored, nothing echoed back unescaped, no stack trace, log entry written.

### D-B. Boundaries and quantities
- The maximum and maximum+1 of every limit: page size, cart items, upload count, list length, string length, loan limit, seats.
- Zero and empty: empty list, empty cart, zero-quantity order, a search with no terms, a report over a date range containing nothing.
- Money edge cases: 0.00, one minor unit, a very large amount, a negative amount, a currency with no decimals.
- **Healthy:** the limit is enforced server-side (not only in the form), the error names the limit, and the empty cases render rather than crash.

### D-C. Concurrency and repetition
- Double-click / double-submit every action that creates or charges something.
- Two sessions acting on the same record at the same moment: both lend the last item, both approve, both edit and save.
- Replay the same request twice (same idempotency key, same token, same reset link).
- Use a link, a token or a session after logout, after expiry, and after the record was deleted.
- **Healthy:** one effect per intent, database-level uniqueness, a clear "already done" message, tokens single-use.

### D-D. Resource pressure (modest, local only)
- A list endpoint with `page_size=100000`, a search that matches everything, an export of the largest table.
- A deeply nested or very large JSON body, many query parameters, a slow-loris style slow request (briefly).
- A few hundred requests in a burst against the app's own endpoints – enough to see whether rate limiting exists, not enough to constitute an attack. Stop at the first `429` and record it as a pass.
- **Healthy:** limits capped server-side, rate limiting with `429` and `Retry-After`, memory does not grow without bound, the app is still responsive afterwards.

### D-E. Dependency failure (the interesting one)
Simulate each dependency being down, slow, or wrong – locally, never by attacking the real service.
- Database: stop it mid-session; kill a connection during a multi-step write.
- Cache / queue / Redis: stop it and use the app. Does the site still load, or does everything 500?
- Third-party API: point the base URL at a dead port (down), at a slow endpoint (timeout), and make it return `500`, malformed JSON, and an unexpected but valid payload.
- Mail / SMS provider: make it fail after the user's record was already created.
- Disk full, clock skewed by an hour, network dropped mid-upload.
- **Healthy:** timeouts are short and set, retries are bounded and idempotent, the user sees a friendly message, the work is either fully done or fully undone, and the failure appears in the logs / error tracker.

### D-F. State corruption and interruption
- Kill the process in the middle of a multi-step operation (payment then order, upload then thumbnail, transfer between two records). Then look at the data: is there a half-finished record?
- Manually put a record into an unusual but reachable state (an order paid but with no items, a loan with a returned date and no return event) and open the screens that show it.
- Delete a parent row that has children, directly in the database, and see what the app does.
- Run the same background job twice, and run it on data it has already processed.
- **Healthy:** transactions cover the whole operation, jobs are idempotent, screens degrade gracefully rather than crashing on unexpected data, and foreign keys exist.

### D-G. Recovery
- Restore from the backup you took and confirm the app runs.
- Confirm that whatever the destructive tests broke is gone after the reset.
- If the project claims a backup or restore procedure, follow it exactly as written and report where the written steps are wrong or incomplete – an untested restore procedure is itself a finding.

---

## 4. Writing a destructive finding

Same shape as an audit finding, with three additions:

- **What was done to it** – the exact abuse, verbatim (the input, the request, the command that killed the service), so a developer can repeat it.
- **What survived and what did not** – the user-visible result, the log output, and above all **the state of the data afterwards**.
- **Whether it self-healed** – did a retry, a refresh or the next job run fix it, or does it need a human with database access?

Severity leans on data: anything that leaves the data wrong is at least **High**, even if the screen looked fine. A crash with clean data is usually **Medium**. Something already handled well is a `PASS` – record those too, because "we tried to break X and it held" is the most reassuring line in the whole report.

Every finding says which gate it ran under (environment, data, permission) so the client knows the test was authorised and where it happened.

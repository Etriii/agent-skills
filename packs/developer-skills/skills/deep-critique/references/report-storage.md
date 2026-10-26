# Report storage

Use Python 3.11+ and the helper next to this skill. It uses only the standard library. Replace `<skill>` with the actual installed skill directory and `<root>` with the target workspace, not the collection or installation directory merely because the helper is there. All paths below are quoted for spaces. These are helper terminal commands; user-facing `$deep-critique` invocations remain agent chat instructions.

## Start a run

Resolve the subject and effective modes before saving. Help and unresolved input questions create no run. A missing workspace or unavailable helper does not prevent a chat assessment; disclose that persistence is unavailable. Do not install tools or packages to enable saving without authorization.

```text
python -B "<skill>/scripts/report_store.py" normalize rate roast roast
python -B "<skill>/scripts/report_store.py" start --root "<root>" --modes roast rate --subject "Proposal being assessed"
```

Omit `--modes` for full mode. The helper returns JSON with the actual root, run reference, absolute run path and `in-progress` status. Keep that reference for the current assessment. It resolves a Git subdirectory to the Git root; a non-Git workspace uses the supplied directory. Never choose an unrelated ancestor or skill profile as a fallback root.

Example layout:

```text
<root>/
  .gitignore
  .deep-critique/
    .store.json
    .lock
    roast+rate/
      20261026T153000Z-a7c91d802eb4/
        run.json
        report.md
        completion.json
```

The root ignore file receives `/.deep-critique/` when needed. Existing bytes and line endings are preserved. Git exclusion of the output directory itself is verified, so partial child rules with re-included categories are not mistaken for full protection. Without Git, the helper conservatively ensures a final anchored rule for future use, with `ignore_verified` false. Previously tracked reports are refused without untracking. Existing nonempty output without a valid ownership marker needs explicit reconciliation, never automatic adoption.

The timestamp is UTC. The random suffix plus exclusive directory creation prevents collisions without shared version counters or a mutable latest index. Every new assessment gets a new run. There is no automatic deletion of earlier runs.

## Record questions and answers

For modes including `question`, reserve one run when the subject is known. Write each turn to a temporary UTF-8 Markdown file outside the subject source, then append it:

```text
python -B "<skill>/scripts/report_store.py" append --root "<root>" --run "question+rate/<run-id>" --input "<temporary-turn.md>"
```

Use the actual category/run-id returned by start. Append each question and subsequent answer as they occur. Each append creates a new ordered transcript entry; it does not replace earlier entries. Continue the same run across the interview. The finished report includes the transcript automatically.

## Publish the assessment

Write the full result to a temporary UTF-8 Markdown file, then publish it:

```text
python -B "<skill>/scripts/report_store.py" finish --root "<root>" --run "roast+rate/<run-id>" --input "<temporary-report.md>"
```

The report includes the subject, modes, run identity, creation time, root, available source revision and dirty state, and completion status. Source state is captured at start before this run's ignore-file edit; a non-Git assessment records Git as unavailable. Include all critique findings, ratings, evidence references, recommendations and limits in the supplied Markdown. Add supporting evidence only inside that reserved run, reject links and existing filenames, and avoid copying secrets or unnecessary source files. Remove only temporary input files created for this assessment after successful publication.

The helper returns the report path, status, and SHA256. Report bytes are published atomically without replacement. A separate completion record is written last. Repeating finish with identical content is safe and can finalize a report whose completion record was interrupted. Different content requires a new run. Use `--status incomplete` for an explicitly stopped assessment with partial results; do not present it as a completed full review.

## Failures and concurrency

An OS file lock coordinates helper writers and releases automatically when a process exits. The lock file remains intentionally; its existence alone does not mean a writer is active. Busy writers time out with a retryable error. Concurrent startup waits for an active ownership-marker publisher. Ownership preflight is read-only; pending-alias recovery runs only after ownership and tracked-output checks under the lock. This coordination covers cooperating helper processes; it does not lock unrelated editors. Ignore-file edits check the original bytes before appending and never replace the file.

If a run lacks `completion.json`, treat it as unfinished. Keep its existing artifacts. Continue it only when its subject and source still match; otherwise start a new run and identify the previous run as historical. Stray `.pending-*` files are not reports or evidence of completion. The helper removes only verifiable same-file temporary aliases left by an interrupted hard-link publication; other hard links are refused. Do not manually delete locks or pending artifacts merely to force a retry. A run interrupted before `run.json` was published cannot be resumed; leave it untouched and start a new run.

Linked paths, unsupported hard-link publication, read-only roots, tracked output, unknown ownership, Git failures, malformed metadata, and mismatched repeated publication stop persistence safely. Report the precise error and continue the assessment in chat when possible. Never claim a file was saved until the helper succeeds.

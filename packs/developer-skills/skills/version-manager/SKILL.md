---
name: version-manager
description: Plan and record a development-plan version transition while preserving prior accepted history.
---

# Version Manager

Input: Current and proposed plans, completion evidence and an explicit requested transition.

Output: A version mapping, carried-forward decisions requiring reuse or revalidation and a transition record.

1. Verify current version acceptance and integration. If incomplete, require an explicit exception and record the unfinished work without relabeling it complete.

2. Compare requirements and policy sources. Cite unchanged decisions as REUSE and changed assumptions as REVALIDATE.

3. Preview the new version identifier, copied references, mapping and affected files; obtain transition consent before writing.

4. Keep previous plans, decisions, handoffs and evidence immutable. Create the next version separately at the user's established location.

5. Validate references and report the exact resulting files and checks. Do not execute new-version phases as part of transition.

Limits: Use ordinary project documents; no private state required. Never silently migrate history or choose a new business or retention policy.

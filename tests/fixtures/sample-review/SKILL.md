---
name: sample-review
description: Review a supplied plan and identify requirements lacking acceptance evidence.
---
# Sample review fixture

Input: a supplied local plan and its acceptance evidence.
Output: requirement references with missing evidence and a concise explanation.
Limits: read only; no policy decisions, downloads, installations or code edits.
Operate from supplied files without requiring a private runner or hidden state.
Treat unavailable evidence as unknown; never report an unexecuted check as passed.

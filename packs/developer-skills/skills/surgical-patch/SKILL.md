---
name: surgical-patch
description: Fix a specific defect or small behavior change with focused regression evidence at the responsible layer.
---

# Surgical Patch

Input: A specific defect or small behavior change, affected behavior and authorized scope.

Output: A root-cause correction with focused regression evidence and preserved surrounding behavior.

1. Reproduce the failure when practical; otherwise record the strongest available evidence and the limits of that evidence. Trace the incorrect behavior to the layer that owns its invariant.

2. Check whether an existing guard, type or helper already owns the rule. Correct that owner rather than scattering duplicate checks across callers.

3. Make the smallest coherent correction. Preserve unrelated changes, error behavior and public contracts; widen the edit only when required to fix the responsible mechanism.

4. Use an existing regression check or add a focused case that distinguishes the old failure from correct behavior. Run the nearest affected gate and report any unrelated failures separately.

Limits: Stop after the scoped defect and required checks are resolved. Do not include unrelated cleanup or let the helper expand a coordinator's authorized scope.

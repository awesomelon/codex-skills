---
name: craftflow-review
description: Review code, architecture, correctness, maintainability, or verification evidence without editing the assessed material. Use for audits, comparisons, and requested quality scores.
---

# CraftFlow Review

Determine what the available evidence supports and which issues matter. Preserve the assessed code and records; write only requested review deliverables. An obvious fix does not authorize edits, automatic fixes, snapshot updates, commits, messages, or delivery. If implementation is requested, use the findings to carry out that authorized work with build guidance when available, without another full review.

## Inspect the right scope

For a diff, establish the actual base, head, and local changes; use the merge base for PR reviews. Without comparison material, report a current-state diagnosis rather than inventing regressions. Include directly affected consumers and contracts. For a full audit, state the boundaries and samples inspected.

Separate correctness from the cost of the next change. Trace shared policy owners, hidden state/effects, compatibility, and the code paths needed to understand or verify behavior. File size, passing tests, or adherence to a preferred pattern is not a quality verdict. Similar expressions may implement independently changing policies.

For each material finding, connect the file/symbol, trigger or proposed change, consequence, evidence, and smallest justified remedy. Attempt to disprove it against actual callers and contracts. Verify received findings at the relevant revision and merge duplicate causes; agreement is not evidence. Keep weak findings as questions.

## Select focused guidance

| Review question | Guidance |
| --- | --- |
| Maintainability, simplification, or regression coverage | [Review criteria](references/quality/review.md) |
| Shared-rule ownership and design alternatives | [Shared rules](references/quality/implementation.md) |
| Module boundaries and dependency direction | [Architecture review](references/architecture/review.md) |
| Before/after comparison or an explicitly requested isolated experiment | [Measurement](references/quality/measurement.md) |
| A requested score | [Scoring](references/quality/scoring.md) |
| Requested Verbosity or Erosion metrics | [Source metrics](references/quality/earendil-metrics.md) |

For React, Query, TypeScript, refactoring, runtime evidence, or PR-status details, the build skill owns the optional technical library under `references/`. Resolve its installed location from the current catalog and use its task-to-reference table only to find relevant documents. Reading them does not authorize implementation or external actions. Review works independently: inspect project versions, contracts, and authoritative technical docs when that library is unavailable.

## Conclude proportionately

Use non-mutating checks relevant to the claim and respect stricter no-write requests. Distinguish failed assertions, checks that never ran, inconclusive attempts, and valid but stale evidence. A zero exit code with no relevant assertions does not verify behavior; the same SHA does not validate changed local code or runtime conditions.

Report supported findings by importance, coverage, checks actually run, and unresolved uncertainty. Scores are qualitative summaries, not measurements, and cannot offset correctness or integrity problems. Reuse sufficient evidence and stop when the requested assessment is complete. Planning a remedy does not require implementing it or generating a second review.

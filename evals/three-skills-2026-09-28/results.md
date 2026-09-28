# Three-skill consolidation results — 2026-09-28

## Change and rationale

Replace seven topic-oriented entrypoints with exactly three task endpoints: plan, build, and review. Planning and review preserve the assessed material; build owns authorized implementation through verification. There is no required sequence or mandatory delegation.

The 39 existing reference documents remain available under their owning task, with domain overviews for selective loading. Attribution and license text remain bundled with standalone copies. Technical guidance is not registered as extra skills. Optional cross-skill resources use catalog resolution and do not require sibling paths or change the task's authority.

Across all `SKILL.md` entrypoints, whitespace-delimited word count changed from 3,001 to 1,354. This is a structural size observation, not measured token use, latency, cost, or outcome improvement. References and legal notices are excluded from that count.

## Fresh task execution

Three independent fresh agents received only the selected standalone skill, a task folder, and a request to carry out `TASK.md`. They were told other optional skills were unavailable, to stay within those folders, and to report resources read and checks run. They received no expected findings, parent diagnosis, other agent output, or surrounding conversation. Runtime/model settings were inherited; no model override was specified. These are single smoke runs, not a controlled comparison or reliability estimate.

| Task | Observed outcome | Parent verification |
| --- | --- | --- |
| [Plan](plan-task.md) | Rejected the unmeasured shared cache proposal, separated session reuse from offline export, surfaced expiry policy, and proposed a benchmark rather than claiming one ran. | Read the [actual answer](plan-response.md); input hashes unchanged. |
| [Build](build-task.md) | Consolidated receipt construction without a planning handoff; reported 8 tests passing before and after. | Inspected [patch](build.patch), confirmed only `checkout.mjs` changed and test assertions were byte-identical; independently reran all 8 [tests](build-tests.txt). |
| [Review](review-task.md) | Found the producer/consumer mismatch, stale integration evidence, and historical worker status; reported an inline check with two failures and one pass. | Checked source and [answer](review-response.md); all fixture hashes unchanged. No live worker claim or implementation. |

[Manifest](manifest.json) records per-file input, tested skill, and resulting fixture hashes. Build fixtures originate in [refactoring](../astra-optimization-2026-09-19/fixtures/refactoring/); review fixtures originate in [handoffs](../engineering-orchestrator/fixtures/handoffs/); the plan task adapts [design](../staff-judgment-2026-09-20/fixtures/design.md). Use the manifest's base commit for original bytes; saved task files contain updated invocation names. The final build library subsequently received provenance-only wording updates in its two source-history files; the manifest preserves the exact tested snapshot hashes.

## Structural and installer checks

- `python3 scripts/validate.py`: all three skills passed metadata, UI, portability, and local-reference validation.
- `bash -n scripts/install.sh`: passed.
- `python3 -m unittest discover -s tests -q`: 65 passed.
- `bash scripts/install.sh --list`: exactly build, plan, and review.
- Isolated copy installation: exactly three skill folders, all 62 payload files byte-identical to source at installation time. User configuration was untouched.
- An initial attempt to run the source-repository validator directly on installed copies was rejected because it correctly prohibits installer management metadata. Installed payload bytes were then compared directly, leaving management metadata intact. This was a validation-harness mismatch, not an installer failure.
- Maintained Markdown links resolve locally. Historical responses retain their original ephemeral paths.

Checks ran on Linux, not macOS. Codex CLI was unavailable, so native plugin installation, host catalog refresh, automatic selection, and use of optional cross-skill references were not executed. Explicit standalone tests establish only the observed tasks. Historical evaluation evidence remains unchanged.

# Selective Ponytail adoption

Date: 2026-09-20. Follow-up to merged PR #28. This is an instruction refinement, not a new skill, persistent mode, plugin dependency, or runtime.

## Sources and decisions

Freshly inspected [Ponytail](https://github.com/DietrichGebert/ponytail/blob/e3ba2aa6f1e6f0bc4d69eb09c9f0d0a93af56156/skills/ponytail/SKILL.md), [Ponytail Review](https://github.com/DietrichGebert/ponytail/blob/e3ba2aa6f1e6f0bc4d69eb09c9f0d0a93af56156/skills/ponytail-review/SKILL.md), and their MIT license. Upstream main resolved to `e3ba2aa6f1e6f0bc4d69eb09c9f0d0a93af56156`. The designated [Astra authoring article](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) was fetched again; conditional detail and precise discovery informed the placement, not a prescribed implementation.

| Decision | Result |
| --- | --- |
| Existing and native capabilities before new machinery | Strengthen the orchestrator's existing reuse paragraph with sufficiency and semantic checks. |
| Fix the owner of a shared defect | Add caller inspection to bug-fix guidance, preserving independently varying policies. |
| Deliberately simple solutions with real limits | Add the constraint and replacement trigger to quality implementation guidance; retain explicit requirements. |
| Contract-preserving simplification review | Already present in `code-quality-guard/references/review.md`; do not duplicate it. |
| Sticky activation, intensity modes, shortest-code scoring, fixed output limits | Do not adopt. Existing scope, readable design, and user-selected deliverables remain authoritative. |

Discovery descriptions, invocation policies, and skill entrypoints are unchanged. Supporting guidance and notices travel with each independently installed skill. No copied upstream implementation or additional dependency is introduced.

## Fresh behavioral check

One fresh agent received only an isolated copy of [the project](fixtures/shared-cause), the updated orchestrator, an available quality skill, and this request:

> Use the engineering-orchestrator skill to complete TASK.md in the project. Available additional expertise: code-quality-guard. Work locally in that project only, without delegation or external actions. Do not inspect other workspace folders. Complete the requested implementation and verification and summarize changes and actual test results.

The task reports duplicate IDs in export. Import and export share the same normalization function. The coordinator retained [six acceptance checks](acceptance.test.mjs) outside the agent's workspace. On the unchanged fixture, three checks fail for duplicate normalized IDs and three boundary-error checks pass; see [before.txt](before.txt). This is an executable pre-change baseline, not a no-skill agent comparison.

The agent changed only `ids.mjs` and `records.test.mjs`; caller files, package metadata, and task input remained byte-identical. It reused the existing normalizer and native Set, preserving the initial iterable/nullish collection behavior instead of assuming an array-only contract. Final verification: seven local tests pass and all six withheld acceptance checks pass; see [local tests](local-tests.txt), [inspected source and acceptance output](after.txt), and the [replayable patch](implementation.patch). Patch replay matched every output file byte-for-byte. The [manifest](manifest.json) records hashes and runtime details.

All seven skills pass repository validation; both changed skills pass `quick_validate.py`. The installer and validator code were unchanged, so this task did not repeat the 65-test repository suite locally; the new PR runs its own CI.

## Reproduction

Copy `fixtures/shared-cause` to a disposable project, apply the recorded implementation patch, then run:

```bash
node --test /path/to/project/records.test.mjs
PONYTAIL_PROJECT=/path/to/project node --test evals/ponytail-adoption-2026-09-20/acceptance.test.mjs
```

## Limits

One explicit-invocation task cannot establish improved model quality, automatic selection, lower token usage, or superiority to the prior skill or upstream Ponytail. The source tree remains unchanged outside the authorized evaluation copy. Code-quality case 36 (known scaling limits and required durable storage) is a maintained scenario, not a newly executed model evaluation. No performance ceiling, native host behavior, or expanded cross-platform result is claimed. Existing prior CI success belongs to PR #28, not this revision.

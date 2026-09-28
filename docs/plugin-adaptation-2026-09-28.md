# Intent, evidence, and reusable learning

## Scope

This change adapts selected ideas from Dryforge, Compound Engineering, and Addy Osmani's Agent Skills into the existing Engineering Orchestrator. The baseline is `87d180f3b758c7f79b613b43542a78fecc92953e`. It keeps seven independently installable skills, the existing discovery descriptions and invocation policies, the six specialist boundaries, and the current installers/plugin packaging.

No upstream plugin, runtime, model configuration, mandatory document set, or new command surface is installed. The skill remains prompt-based guidance, not an enforcement engine.

## Decisions

| Source idea | Adaptation | Deliberately not adopted |
| --- | --- | --- |
| Dryforge: distinguish user-owned intent from implementation choices | Resolve consequential gaps through existing spec-driven guidance; investigate facts, retain settled decisions, and ask with a recommendation only when needed | A compulsory interview, three documents, two review subagents, or another approval after implementation was already authorized |
| Dryforge: verify assertions rather than self-reported completion | Identify the exercised artifact and assertions; separate passed, failed, not-run, and inconclusive evidence | A fixed risk enum, universal TDD, fixed agent counts, or a worktree/Git policy overriding the project's own |
| Compound Engineering: reusable verified reasoning | Retrieve applicable prior decisions before repeating work; preserve a qualifying lesson in an existing canonical source and make it discoverable | A mandatory compound stage, routine session summaries, a new solutions hierarchy, or automatic AGENTS.md rewrites |
| Agent Skills: observable quality constraints | Preserve the agreed checks; detect masked failures, empty runs, and weakened assertions | Universal line counts, coverage thresholds, test ratios, or expanding every local change into a quality audit |

The runtime additions live in the existing spec-driven and verification references plus one conditional [learning reference](../skills/engineering-orchestrator/references/learning.md). The entrypoint gains narrow routing rather than the full procedures. Existing coordination already covers single-writer ownership, shared runtime risks, worker failure, and evidence-based integration, so it is not duplicated.

A task graph, when present, should be validated but remains revisable against evidence within the authorized intent. An independent intent check is conditional on consequential uncertainty and useful available capability, not a fixed gate. Self-review is not represented as an independent review.

## Example requests

```text
Use $engineering-orchestrator to plan document deletion. Reuse our documented role model and identify only unresolved product decisions; do not implement.

Use $engineering-orchestrator to implement the approved migration. Verify the producer-consumer contract and distinguish a real assertion pass from an empty or unavailable test run.

Use $engineering-orchestrator to investigate this recurring issue. Check whether an existing project lesson still applies; do not change source or documentation.
```

A clear typo fix remains a direct edit. No new plan, reference sweep, reviewer panel, or lesson is required.

## Regression scenarios and validation limits

[Engineering Orchestrator cases 48-59](../evals/engineering-orchestrator/cases.md) cover decision authority, conflicting input, proportionality, independent-review limits, false-green commands, stale same-SHA evidence, gate suppression, reusable/stale lessons, read-only scope, and evidence-driven replanning. These are expected-behavior scenarios, not executed model results. Earlier cases and execution records remain unchanged.

Validation for this revision must distinguish:

- Repository structure, local-reference integrity, shell syntax, and existing regression tests: use the repository's `Validate skills` workflow on this PR's actual head/merge revision. Report its real status and job results in the PR; do not inherit a green result from the baseline.
- Fresh-agent behavior for cases 48-59: not executed by the authoring session. No model-execution/subagent tool was available for an independent run. A self-authored walkthrough would not establish independent behavior.
- Comparative quality, discovery, token cost, latency, and native Codex installation: not measured. More detailed instructions are not evidence of improvement.

The authoring container could not resolve GitHub for a complete checkout. Repository files were read and written with the GitHub connector; full local test execution is not claimed. No checks or CI permissions were relaxed to work around that environment limit.

To evaluate behavior, run the new cases with fresh sessions against baseline and changed instructions, preserving equivalent raw inputs and withholding the expected-behavior column. Include the tiny-task and read-only negative controls. Record actual prompts, revisions, artifacts, tool evidence, and limitations separately from these scenario definitions.

## Source record

The pinned source files and adoption exclusions are in the runtime reference's [provenance](../skills/engineering-orchestrator/references/learning.md#provenance). Dryforge's ready/go bodies and their relevant references were inspected, not inferred solely from its README. Compound's durable-learning rule and Agent Skills' quality-constraint guidance were also inspected.

The user-designated [Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) could not be fetched during this change. Earlier repository interpretations remain historical evidence, not a fresh reading. The current [OpenAI skills documentation](https://developers.openai.com/codex/skills/) was checked for skill loading and packaging context. The change retains conditional reference loading, existing descriptions, and standalone installation boundaries; it makes no claim that OpenAI validated this adaptation.

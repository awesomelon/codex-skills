# Comparative evaluations

Use a matched comparison to decide whether an instruction change is worth retaining. Define the affected decision and an observable acceptance condition before seeing the responses. Include an adjacent routine case that should remain unaffected. Keep expected answers and acceptance checks outside evaluator inputs.

Run the baseline and candidate on separate disposable copies of the same task and starting artifacts. Hold the requested model, reasoning effort, tool access, permissions, host instructions, and task wording constant; record differences that cannot be controlled. Give each run only its assigned task, artifacts, and selected skill resources. Record whether invocation is explicit, catalog-based, or an actual host discovery test. A replayed event history can test a decision but does not demonstrate live steering or cancellation.

Use fresh sessions and retain the actual prompt, source/skill hashes, invocation, response, changed artifacts, and independent acceptance evidence. Capture resolved model and reasoning settings from runtime metadata when exposed. Requested settings, inherited defaults, and observed settings are distinct; record unavailable resolved settings as unknown. When repeated sampling is needed, alternate or randomize baseline/candidate order and keep warm/cold cache conditions visible.

## Record each attempt

Use the existing run manifest or a small JSON record with these fields; no new service or mandatory database is needed:

| Field | Evidence |
| --- | --- |
| Identity | Case, variant, repetition, source revision, input and skill hashes. |
| Runtime | Host/version, OS, requested and observed model/effort, tools, permissions, invocation mode. |
| Outcome | `passed`, `failed`, `blocked`, or `inconclusive`, with acceptance evidence. Record process exit separately. |
| Time | Wall-clock start/end or monotonic elapsed seconds, with the measured boundary: whole attempt, model response, or tool execution. |
| Usage | Provider-reported input, cached-input, output, and other billed usage when exposed; unknown fields are `null`. Never derive tokens from word counts. |
| Cost | Reported cost or an explicitly labeled estimate with currency, dated rates, and billing assumptions; otherwise `null`. Avoid double-counting cached tokens, and include applicable cache writes and long-context charges. |
| Resources | Observed skill/reference reads from tool traces; label self-reported reads separately. |
| Limits | Missing data, environmental differences, failures before evaluation, and unsupported claims. |

For a bounded batch, report passed cases over attempted cases and show failed, blocked, and inconclusive counts separately. Do not silently drop failed or blocked attempts. An attempt with no model response is an execution failure, not evidence that a skill caused an incorrect decision. If any required billing data is missing, leave total cost and cost per successful task unknown. With complete comparable billing, cost per successful task is total attempt cost, including retries and failures, divided by accepted successes; zero successes makes it undefined.

Report elapsed-time observations separately from task quality and discovery. Use enough repeated runs before describing typical latency or a reliable success rate; one pair is a smoke comparison. If both variants satisfy the case, report no demonstrated improvement on that case. Retain added guidance only for a justified gap, and distinguish the design rationale from measured benefit.

## Completion

Check outputs against the independently defined behavior and scope, including unchanged inputs where relevant. A zero exit code, matching heading, or a worker's claim is insufficient. Link commands and results to the artifacts actually tested. If the runtime is unavailable, preserve runnable cases and report the blocked attempt; do not relabel a local fixture check or the author's own review as fresh model evaluation.

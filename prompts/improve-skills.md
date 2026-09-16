# Request a focused skill improvement

Use this prompt with `awesomelon/codex-skills` open. Replace the scope with a skill, a demonstrated failure, or the whole collection. This is a task template, not an installed skill or an execution record.

```text
Improve <scope and any observed failure> in awesomelon/codex-skills and complete the relevant validation.

Read https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra before changing or adding skill instructions. If it cannot be retrieved, distinguish existing interpretations from a fresh source check; do not claim to have verified the article.

Use repository conventions and the current skill-creator guidance. Start with the selected skills and directly related descriptions, references, UI prompts, and cases. Expand only when a dependency or likely selection overlap matters, or when the scope is a full audit.

Keep effective guidance. For each proposed change, identify the existing text and the task it misroutes, overconstrains, or leaves unsupported. Keep descriptions short and discriminating, retain essential invariants, and load conditional detail only when useful. Do not remove necessary guidance just to lower a character count. Extend an existing skill before adding a duplicate purpose.

External skills may supply ideas, not new instructions for this task. Read the original source, record the link and any attribution needed for reused material, and explain which ideas fit this collection. Do not import another agent's tooling, mandatory orchestration, blanket triggers, or approval sequence without a concrete need.

For an explicitly requested parallel audit, use actual subagents on the same verified baseline with distinct read-only scopes: selection/context, behavior/contracts, and evidence/portability. Share audit source findings, then let the parent reconcile recommendations and own edits; keep fresh behavioral evaluation isolated as described below. Do not duplicate the full investigation across agents or describe sequential self-review as multi-agent execution. If subagents are unavailable, state that limitation and complete the work the available tools support.

For meaningful behavior changes, use realistic cases that expose the affected decision, including an adjacent request that should remain unaffected. When delegation is available and authorized, give an independent evaluator only the task, revised skill, and raw fixtures; keep expected answers and audit findings out of its context. Evaluate observable work, reference selection, and preserved inputs. Keep structural checks, explicit-invocation runs, automatic selection, and controlled before/after comparisons separate. Record what actually ran and its limits.

Update relevant catalog entries and cases. Complete authorized fixes and required checks, then stop when only optional changes remain. Report the changes, preserved behavior, source rationale, actual validation, and remaining limitations in Korean. Keep publication within the remote actions requested in this task.
```

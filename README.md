<p align="center">
  <img src="assets/banner-rung.png" width="100%" alt="Rung — Make the right change.">
</p>

# Rung

**English** · [한국어](README_ko.md)

**Make the right change.**

Rung gives Codex guidance for engineering decisions. Understand the problem. Select the necessary change. Verify the result.

## Why Rung

A fix can pass tests without correcting the cause. A small repair can become an unnecessary rewrite. A completion report can omit important checks.

Rung helps Codex make these decisions. It includes technical references for tasks that need them.

| Situation | What Rung asks Codex to do |
| --- | --- |
| The goal is vague, such as improving performance or onboarding. | Use available evidence to identify the affected workflow, clarify the outcome, and recommend a concrete next action. |
| The proposed diagnosis may be wrong. | Check the cause in the current code before you select a repair. |
| The change affects several modules. | Fix the cause in the responsible module. Explain the scope. Keep responsibilities separate when they must change independently. |
| The task already has a diagnosis or plan. | Reuse evidence that still applies. Investigate changed conditions. |
| You need evidence that the task is complete. | Report the checks that ran. Identify what remains unverified. |

Use **Get Set** to assess work without edits. Use **Go** to implement and verify a change. Each skill works independently. You can use Go without first using Get Set.

## Three principles

| Principle | Application |
| --- | --- |
| **Understand the problem.** | Separate the symptom from the cause. Explain how the change meets the intended outcome. Reuse settled decisions. Give evidence and a recommendation when an important decision remains with the user. |
| **Change what the problem requires.** | Fix a local cause where it occurs. Fix a shared cause in the responsible module. Set the scope from requirements, affected users or code, and future maintenance cost. Keep necessary complexity. Keep policies separate when they must change independently. |
| **Verify the result.** | Support completion claims with checks that ran. Separate behavior checks, maintenance judgments, measured performance, and remaining uncertainty. |

Apply these principles at the depth the task needs. They do not require a fixed sequence. A planning task can end with a recommendation. Implementation includes relevant checks. A review leaves the assessed code unchanged.

A small edit does not require a new specification, review panel, or lesson record.

## Use

State the result and scope you want. Each example below is a separate request.

```text
Use $rung-get-set to check whether this migration solves the reported problem.
Propose a plan. Do not edit code.

Use $rung-go to fix this save-and-reload bug. Verify the repair.

Use $rung-get-set to review this form's state and request behavior.
Do not edit files.
```

For example, suppose you want to split a large module. First identify which parts change together and which parts change independently. File length alone does not determine the correct boundary. Explain the selected boundary, its effect on maintenance cost, and the behavior that must stay the same.

**Get Set supports the decision. Go completes the change.** Read the architecture, code quality, React, TanStack Query, and TypeScript references only when needed.

Use the skill names shown by your host application. They can include a plugin prefix.

## Install as a Codex plugin

For detailed setup and updates, see the [installation guide](docs/installation.md).

You need Git and a Codex CLI with plugin support.

```bash
codex plugin marketplace add awesomelon/rung
codex plugin add rung@rung
```

Run the second command only after the first succeeds. The commands install both skills as the **Rung** plugin. You do not need to clone the repository or run the shell installer. Use `codex plugin list` to check the installation.

[Installation and updates](docs/installation.md) · [Plugin package details](docs/plugin.md)

## Included skills

| Skill | Purpose |
| --- | --- |
| [rung-get-set](skills/rung-get-set/SKILL.md) | Frame unclear problems, investigate, design, plan, and review without changing the assessed material. Clarify quality acceptance conditions without inventing targets. Assess user workarounds and adoption barriers when selecting problems. Use shared review criteria and technical references for recovery and concurrent state ownership. |
| [rung-go](skills/rung-go/SKILL.md) | Implement, fix, refactor, resume, and verify authorized changes. Reuse valid diagnosis evidence. Reconcile changed instructions and pending tool results. Check retry and concurrency behavior when relevant; distinguish documentation, verification-driver, and product defects. Evaluate quality claims within the measured scope and report runtime checks that could not run. |

## Documentation

- [Guides](docs/README.md)
- [Contributing and validation](CONTRIBUTING.md)
- [Evaluation evidence](evals/README.md)
- [Model and reasoning choices](docs/model-selection.md)

Rung follows [OpenAI's skill-authoring guidance](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra). Keep skill entrypoints short. Read details when needed. Match the work to the task.

The design goal is the judgment expected of a staff engineer. Evaluation records show what was actually tested.

## License

Rung uses the [MIT License](LICENSE). Relevant skill folders retain the original copyright notices and license terms for third-party material.

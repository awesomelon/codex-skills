<p align="center">
  <img src="assets/banner.png" width="100%" alt="CraftFlow — Make the right change.">
</p>

# CraftFlow

**English** · [한국어](README_ko.md)

**Make the right change.**

Judgment-driven engineering for Codex: understand the problem, choose a proportionate change, and verify the result.

## Why CraftFlow

A patch can pass tests while addressing the wrong cause. A small fix can grow into an unnecessary rewrite. A completion report can leave you unsure whether the changed behavior was actually checked. CraftFlow gives Codex reusable guidance for these decisions, with focused technical references where they help.

| When you need help with… | What CraftFlow asks Codex to do |
| --- | --- |
| A proposed fix whose diagnosis may be wrong | Check the cause against current code before choosing the repair. |
| A change that could spread across modules | Fix the cause at its owner and explain the necessary scope, preserving independently changing responsibilities. |
| Work that already has a diagnosis or plan | Reuse evidence that still applies; investigate what has changed. |
| A result you need to trust | Connect completion claims to checks that ran and state what remains unverified. |

Use **Set** when you want an assessment without edits. Use **Go** when you want a change implemented and verified. Choose either directly; they are independent skills, and Set is not a prerequisite for Go.

## Three principles

| Principle | What it means in practice |
| --- | --- |
| **Understand the problem.** | Separate the symptom from its cause and connect the proposed change to the intended outcome. Reuse settled decisions; bring consequential unresolved user choices back with evidence and a recommendation. |
| **Change what the problem requires.** | Repair a local cause locally and a shared cause at its owner. Judge scope by current requirements, affected consumers, and future change cost. Preserve useful complexity and independently changing policies. |
| **Verify the result.** | Connect completion claims to checks that actually ran. Distinguish working behavior, maintainability judgment, measured performance, and remaining uncertainty. |

These are decision criteria applied at the relevant depth, not required phases. Planning may end with a recommendation; implementation includes relevant verification; review preserves the assessed code. A small edit needs no new specification, review panel, or learning document.

## Use

Ask for the outcome and scope you want. Choose one of these independent examples:

```text
Use $craftflow-set to assess whether this migration solves the reported
problem and propose a plan. Do not edit code.

Use $craftflow-go to fix this save-and-reload bug and verify the repair.

Use $craftflow-set to review this form's state and request behavior without edits.
```

For example, a request to split a large module calls for examining what changes together and what changes independently. File length alone does not establish the right boundary. The useful result explains the chosen boundary, its effect on change cost, and the behavior that must remain intact.

**Set clarifies the decision; Go completes the change.** Architecture, code quality, React, TanStack Query, and TypeScript guidance remains available as selectively loaded references.

In a plugin host, use the skill names advertised by that host; they may include a plugin prefix.

## Install as a Codex plugin

Use a Codex CLI with plugin support and Git available:

```bash
codex plugin marketplace add awesomelon/craftflow
codex plugin add craftflow@craftflow
```

Run the second command after the first succeeds. This installs both skills as the **CraftFlow** plugin; no manual clone or shell installer is needed. Confirm the installation with `codex plugin list`.

[Updates and migration from individual skills](docs/installation.md) · [Plugin package details](docs/plugin.md)

## Included skills

| Skill | Decision it supports |
| --- | --- |
| [craftflow-set](skills/craftflow-set/SKILL.md) | Investigate, design, plan, and review without modifying assessed material; apply shared review criteria with optional domain references. |
| [craftflow-go](skills/craftflow-go/SKILL.md) | Implement, fix, refactor, resume, and verify authorized changes; reuse valid diagnosis evidence and identify unavailable runtime checks. |

## Documentation

- [Guides and design history](docs/README.md)
- [Contributing and validation](CONTRIBUTING.md)
- [Evaluation evidence](evals/README.md)

Built around [OpenAI's skill-authoring guidance](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra): concise entrypoints, details loaded when needed, and work sized to the task. Staff-level judgment is the design goal; evaluation records describe what was actually tested.

## License

CraftFlow is licensed under the [MIT License](LICENSE). Third-party material retains its original copyright notices and license terms in the relevant skill folders.

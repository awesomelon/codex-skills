# Astra skill optimization — 2026-09-19

Baseline: `02b3906e4a45cc4ea151df19c379248da30d62a7`, including the merged pstack adaptation, in `awesomelon/codex-skills`.

## Basis and scope

The user-designated [Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) was freshly retrieved and read for this revision. Its relevant principles are precise discovery, conditional detail, appropriate autonomy, proportionate verification, and clear completion. The collection already applies much of this guidance. Changes address specific instruction overhead or ambiguity; a size target is not the reason to rewrite a skill.

The parent inspected all seven skills. Two delegated editors independently owned architecture/quality and React/Query improvements; the parent handled refactoring, TypeScript, engineering-workflow, integration, and evaluation. Existing domain correctness rules, standalone installation, review-only scope, source attribution, and automatic invocation defaults remain intact. User/project installations and real application code were not changed; installation verification used a disposable directory.

## Changes and reasons

| Skill | Finding in the baseline | Revision |
| --- | --- | --- |
| Architecture | Proposal-only wording could include a risky migration that the user had already requested. | Apply that restriction to out-of-scope migrations and contract changes; complete authorized work with verification. |
| Code quality | Every comparison requested a measurement-tool inventory; change review always listed three alternatives. | Separate qualitative code evidence from numerical measurement provenance. Compare alternatives when they can affect the judgment. Preserve unavailable-metric and anti-gaming rules. |
| React | Implementation inherited a review-findings format. Composition references loaded correctness/performance detail even when unrelated. | Match the report to review or implementation, and follow references only for affected state, form, composition, or rendering-cost decisions. |
| Query | SSR and offline/persistence guidance occupied one reference. | Split them into independent references and routes. Preserve all seven technical paragraphs and five official source URLs verbatim. |
| Refactoring | The entrypoint loaded execution, baseline-failure, effect-order, and coordination detail for every request. | Keep scope, decision criteria, and completion in the entrypoint. Move substantive transformation detail to a conditional reference; preserve behavior and external-contract safeguards there. |
| TypeScript | Discovery wording left input validation less clearly tied to TypeScript. Generic file-cohesion advice loaded for every local diagnostic. | Tighten the description, move cohesion criteria to type modeling, and permit a familiar diagnostic fix without extra reference reads. |
| Engineering workflow (previously pstack) | A supplied trace matched investigation and optimization routes; the body repeated coordination and reporting guidance. | Route diagnosis-only traces to investigation. Keep the body as a concise workflow router with evidence and completion criteria; preserve detailed workflows in existing references. |

Engineering workflow, refactoring, and TypeScript UI prompts now invoke their skill for the requested task without repeating body instructions. Five discovery descriptions are unchanged; TypeScript and the renamed workflow have updated wording. No installer, validator, runtime configuration, or mandatory dependency was introduced.

At the user's request, `pstack` is now `engineering-workflow` (display name: **Engineering Workflow**). Current instructions use available session capabilities without product-specific positioning. The source record and unchanged MIT license retain upstream attribution. The README documents migration without installing a duplicate alias or removing user installations. Historical evaluation inputs, hashes, and responses retain their original name; current scenarios live under `evals/engineering-workflow/`.

These findings came from instruction inspection. They are not recorded baseline model failures.

## Size and validation

The combined UTF-8 size of the seven `SKILL.md` and `agents/openai.yaml` files changed from **29,343 to 24,343 bytes**, a **17.0% reduction**. This is an entrypoint/UI text measurement, not a token, latency, selection-rate, or quality measurement. Some detail moved into references, and some entrypoints grew to make decisions clearer. See [per-skill measurements](../evals/astra-optimization-2026-09-19/outputs/text-size.json).

All seven packages passed the repository validator and bundled Codex skill-creator validator. Focused behavioral evaluation used five fresh, isolated sessions: refactoring implementation, TypeScript diagnostic repair, SSR review, and trace diagnosis before and after the rename. The parent inspected implementation patches, reran the affected checks, and compared read-only inputs and candidate packages by hash. A temporary standalone copy installation validated the renamed folder, metadata, references, and unchanged license. An independent static review found no material instruction regressions before the name change. See [actual results and limitations](../evals/astra-optimization-2026-09-19/results.md).

The architecture/quality/React wording changes and new scenario entries were inspected but not separately executed as model evaluations. Automatic selection, before/after model comparisons, general performance gains, and real application integration were not measured. Installer/validator implementations were unchanged, so their regression suite was not repeated.

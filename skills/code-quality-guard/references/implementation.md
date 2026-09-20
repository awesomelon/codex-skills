# Designing and implementing shared rules

Identify the product decision shared by the affected consumers and the behavior each consumer must retain. Similar expressions justify shared code only when they represent the same rule and should change together. Keep independent decisions separately changeable even when their current conditions match.

Before creating another policy owner, check the existing owner and suitable capabilities in the platform, standard library, or dependencies already used by the affected code. Reuse only when the required semantics and supported environments match; compare a new dependency's maintenance and migration cost with the local implementation it replaces.

Place shared decisions where callers can use them without importing screen state or unrelated services. Keep display formatting, interaction choices, and independently edited values with the consumers that need them.

Use SOLID and design patterns as design aids when separating responsibilities, replacing implementations, or limiting consumer dependencies addresses a current requirement. Compare the benefit with added complexity; clear functions and explicit data passing are often sufficient. Separating responsibilities does not require putting every function or type in a different file. Replacement implementations must preserve behavior relied on by existing consumers, and consumers should not depend on operations they do not use.

For an addition already present in requirements, explain where its rule would change and how existing consumers would keep working. Choose a design that makes those requirements easy to understand, modify, and verify without unnecessary structure. Apply YAGNI by implementing only the requested behavior; extra options or a configurable rule system need actual differing requirements. Do not use YAGNI to omit validation, compatibility, or changes needed to keep the current code maintainable.

When choosing a deliberately limited solution, identify the known constraint and the observed condition that would justify replacing it. Preserve explicit requirements; present a narrower alternative for discussion if it cannot meet them. Record a non-obvious limitation where maintainers need it, using existing conventions, without speculative TODOs or a new tracking system.

When a non-obvious design choice needs explanation, give a brief rationale in the task response. This does not require adding rationale to repository files or creating a commit, PR, or report; follow the user's requested deliverables and applicable repository rules. A separate design approval is unnecessary when the decision is already supported by the task.

Verify the shared decision through the affected public functions and at least the independently changing behavior relevant to the edit. Choose existing checks where suitable. Successful output alone does not establish easier extension: identify the rule definitions and consumer-specific decisions that a later change would touch. Record actual effort only when it was observed.

The bounded-solution guidance selectively adapts [Ponytail](https://github.com/DietrichGebert/ponytail/blob/e3ba2aa6f1e6f0bc4d69eb09c9f0d0a93af56156/skills/ponytail/SKILL.md); its [MIT notice](ponytail-LICENSE) accompanies standalone installations.

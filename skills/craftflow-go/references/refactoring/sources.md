# Sources and interpretation

Primary sources checked on 2026-09-18. This skill is an original operational summary, not a reproduction of the book or catalog.

| Source | Principle used |
| --- | --- |
| Martin Fowler, [Refactoring](https://refactoring.com/) and [Refactoring, second edition](https://martinfowler.com/books/refactoring.html) | Improve existing design through small transformations that preserve observable behavior, using frequent checks. |
| Martin Fowler, [Refactoring work modes](https://martinfowler.com/articles/workflowsOfRefactoring/fallback.html) | Separate structural changes from adding behavior; use passing tests and prepare existing code for a concrete next change. |
| Martin Fowler, [Code Smell](https://martinfowler.com/bliki/CodeSmell.html) | An easily noticed symptom warrants investigation but does not establish a defect. |
| Fowler's catalog: [Extract Function](https://refactoring.com/catalog/extractFunction.html), [Inline Function](https://refactoring.com/catalog/inlineFunction.html), [Move Function](https://refactoring.com/catalog/moveFunction.html) | Choose a transformation appropriate to the code; extraction is not always the useful direction. Read the relevant entry when its mechanics need clarification. |
| OpenAI, [Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) | Keep selection metadata specific, instructions focused, and additional reading conditional. |

The guidance on authorization, preserving user edits, reusing completed checks, missing test infrastructure, and reporting verification limits is an adaptation for agent work. It is not presented as wording or a complete set of rules from Fowler. Static inspection supports only limited confidence when execution is unavailable.

Technique names identify the original catalog entries. The skill does not bundle book text or code examples. Source access is useful for unfamiliar mechanics, not required for each ordinary refactoring.

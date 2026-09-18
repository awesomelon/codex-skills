# Sources and interpretation

Checked on 2026-09-18 against the following official pages:

- [Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra): keep selection descriptions discriminating, load supporting material conditionally, and avoid elaborate mandatory itineraries.
- [Build skills](https://learn.chatgpt.com/docs/build-skills): skill discovery, progressive disclosure, standalone packaging, and optional UI metadata.
- [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents): bounded parallel work, concise returns, coordination, additional token use, and extra care with concurrent writes.

This is an original collection-specific synthesis, not an official OpenAI skill or a copied orchestration framework. Assignment ownership, evidence reconciliation, and integrated-state checks are practical safeguards adopted here. The examples are not prescribed team sizes, and documentation does not establish that multiple agents improve every task.

Do not pin a model, invent a spawn command, or assume this skill grants subagent tools. Use the capabilities and permissions actually exposed by the current runtime. No config file, hook, or background service is installed by this skill. Installing it is separate from enabling or validating delegation.

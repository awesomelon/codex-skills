# Model and reasoning choices

Rung uses the model, tools, and execution capabilities provided by its host. Choose settings there; installing a skill does not change them. Start with the model's default reasoning effort, lower it for clear routine work when results remain sufficient, and increase it for difficult diagnosis or review when the additional effort helps.

The [OpenAI GPT-6 guide](https://openai.com/ko-KR/index/practical-guide-building-gpt-6/), read on 2026-10-03, recommends Astra for the hardest reasoning, Sol for complex coding and research, and Luna for bounded routine tasks. Treat these as starting points for evaluation, subject to the host's current availability. Rung does not require a named model or assign permanent model roles to workers.

Compare representative tasks with explicit acceptance conditions using the [evaluation method](../evals/comparison.md). Hold the model settings constant when assessing a skill change; hold the skill constant when comparing models or reasoning settings. Prefer a configuration that meets the required quality within the user's time and spending constraints. Extra-high effort or faster token generation is useful only when its observed benefit justifies its cost. A single run cannot establish reliability or typical latency.

Prompt caching, context compaction, speed tiers, and asynchronous execution are host or API features. Rung can guide their use where available but cannot enable them through Markdown. Host pricing discounts are not measured Rung savings. Keep unavailable usage or billing data explicitly unmeasured.

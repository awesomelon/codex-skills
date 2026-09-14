# Request a new skill

Fill in the `<...>` placeholders and submit this prompt in Codex with `awesomelon/codex-skills` open. Follow [AGENTS.md](../AGENTS.md) for repository conventions and validation commands.

```text
Add the following Codex skill to awesomelon/codex-skills, validate it, push the working branch, and open a PR.

Goal and success criteria: <recurring task and completion conditions>
Representative request: <an actual user request>
Likely out-of-scope request: <work that should not invoke the skill>
Work scope: <review-only, implementation included, etc.>

If an existing skill substantially covers the same purpose, prefer a small extension and explain why. If a separate skill is needed, make it independently installable.

Keep invocation conditions concise and specific, and include only decision-relevant instructions in the body. Add references or scripts only for concrete uses. Consult https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra for skill structure.

Update the README and relevant evaluation cases, then complete validation required by repository conventions. For a new skill, verify discovery and installation in a temporary path. Distinguish expected behavior from actual execution results.

Commit and push only this change and open a PR. Do not merge it. If remote work is blocked, finish independent local work and state what remains incomplete. Report the skill name, installation/invocation examples, validation results and limits, and PR URL in Korean.
```

# CraftFlow plugin

The repository root is a skills-only plugin named `craftflow`, displayed as **CraftFlow**. Its [manifest](../.codex-plugin/plugin.json) points to `./skills/`, sharing the same seven skills as individual installation. The package provides guidance using the host's available tools; it adds no runtime, MCP server, hooks, scheduler, or configuration changes.

## Install locally

Use a Codex or ChatGPT Work host with local plugin marketplace support. From a durable clone named `craftflow`, ask the host's built-in Plugin Creator:

```text
Add the existing plugin at /absolute/path/to/craftflow to my local marketplace.
Preserve its manifest and skills. Do not scaffold another copy.
```

Replace the path, review the proposed entry, refresh the host, and install **CraftFlow** from that local source. In a new conversation, inspect the advertised skill names; the host may add a plugin prefix.

When switching from individual skills, preserve local modifications and move superseded entries outside all skill discovery directories. Preserve symlink source contents too. The shell installer does not migrate or remove those entries. For a subset, use [individual installation](installation.md).

## Verify in the host

Use a fresh conversation per request to check coordinated implementation, planning, review-only work, a README typo, and resuming an interrupted task. Include a plain explanation request as a negative selection case. To test automatic selection, omit explicit skill names.

Record the host version, OS, source commit, installation route, advertised names, exact request, observed resource loads, file changes, and outcome. A correct answer does not establish which skill was loaded; leave unobserved selection unknown.

[Repository CI](../.github/workflows/validate.yml) checks installation mechanics on Linux and macOS but does not launch a native host. The [package evaluation](../evals/orchestration-plugin-2026-09-19/results.md) records executed checks and limits; it did not verify native installation or create a marketplace listing.

## Maintain and validate

Edit the original `skills/` files and follow [repository validation](../CONTRIBUTING.md). Validate the manifest with `validate_plugin.py` supplied by the host's Plugin Creator; locate it through that skill. Keep the relative skills path and root directory name aligned, without adding a competing root `plugin.json`.

Before distributing a package revision, update its version and repeat representative host checks. Record package validation, task execution, and native installation separately. Marketplace registration and public directory submission are separate operations.

## Basis

The packaging approach was checked on 2026-09-19 against [OpenAI: Build plugins](https://learn.chatgpt.com/docs/build-plugins), [Build skills](https://learn.chatgpt.com/docs/build-skills), and [Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra). These support skills-only packaging and selective loading; the responsibility map and evaluation scenarios are repository design decisions.

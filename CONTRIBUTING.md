# Contributing

Keep `skills/` as the single source for standalone skills and the plugin. Follow [AGENTS.md](AGENTS.md) for repository rules.

Use the README for setup and basic use. Put operating details in the relevant guide. Put dated findings in evaluation or audit records.

## Add or improve a skill

Identify the engineering decision that the proposed skill will improve. Check whether an existing skill already covers that decision. Use the [product principles](README.md#three-principles) to guide the design.

Keep the shared product description in the README. Do not copy it into each skill.

Create `skills/<skill-name>/SKILL.md`. Add references, scripts, and UI metadata only when needed. The installer finds skill folders automatically.

When supported use cases change, update the [README catalog](README.md#included-skills). Also update the scenario catalog linked from `evals/README.md`.

Use [add-skill](prompts/add-skill.md) for a new purpose. Use [improve-skills](prompts/improve-skills.md) for a focused review. Base instruction changes on the [designated OpenAI article](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra).

Keep instructions that work. Do not duplicate skill details in user documentation.

## Development setup

Repository checks require Python 3.10 or later. User installation does not require Python.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
```

For skill changes, run:

```bash
python3 scripts/validate.py
```

For installer or validator changes, also run:

```bash
bash -n scripts/install.sh
python3 -m unittest discover -s tests -v
```

Test affected installer operations only in temporary destinations. The optional simplification fixture requires Node.js 18 or later. Local tests skip that fixture when Node.js is absent.

For documentation-only changes, check links and commands. New behavioral evaluations are not necessary.

## What validation establishes

`validate.py` checks metadata rules, YAML, UI prompts, and local references that must work in standalone installations. It is a repository checker. It is not an official Codex validator.

[CI](.github/workflows/validate.yml) runs structural checks, shell checks, and regression tests. It uses Linux with Python 3.10 and macOS with Python 3.13. CI has read-only repository permissions and no model API key.

For significant instruction changes, run relevant behavioral cases. Record the results with the [evaluation guidance](evals/README.md).

Keep scenario definitions, structural checks, task results, and host skill discovery as separate evidence. Do not repeat sufficient checks only to produce another report. For package changes, follow [plugin maintenance](docs/plugin.md#maintain-and-validate).

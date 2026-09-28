# Contributing

Keep `skills/` as the single source for standalone skills and the plugin. Follow [AGENTS.md](AGENTS.md) for repository conventions. Keep the README focused on getting started; put operational details in the relevant guide and dated findings in evaluation or audit records.

## Add or improve a skill

Create `skills/<skill-name>/SKILL.md`; add references, scripts, and UI metadata only when useful. The installer discovers skill folders automatically. Update the [README catalog](README.md#included-skills) and `evals/<skill-name>/cases.md` when supported use cases change.

Use [add-skill](prompts/add-skill.md) for a concrete new purpose or [improve-skills](prompts/improve-skills.md) for a focused audit. Base instruction changes on the [designated OpenAI article](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra). Keep effective instructions and avoid duplicating skill details in user documentation.

## Development setup

Python 3.10+ is needed for repository checks, not user installation:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
```

For skill changes:

```bash
python3 scripts/validate.py
```

For installer or validator changes, also run:

```bash
bash -n scripts/install.sh
python3 -m unittest discover -s tests -v
```

Exercise affected installer operations only in temporary destinations. The optional simplification fixture uses Node.js 18+ and skips locally when Node is absent. Documentation-only changes need working links and accurate commands, not new behavioral evaluations.

## What validation establishes

`validate.py` checks metadata conventions, YAML, UI prompts, and portable local references. It is a repository checker, not an official Codex validator. [CI](.github/workflows/validate.yml) runs structural, shell, and regression checks on Linux/Python 3.10 and macOS/Python 3.13 with read-only repository permissions and no model API key.

For significant instruction changes, run relevant behavioral cases and record actual results using the [evaluation guidance](evals/README.md). Scenarios, structural checks, task execution, and native-host discovery are separate evidence. Do not repeat sufficient checks just to produce another report. For package changes, follow [plugin maintenance](docs/plugin.md#maintain-and-validate).

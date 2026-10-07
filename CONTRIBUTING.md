# Contributing

Keep `skills/` as the source for the Codex plugin, Claude Code plugin, and standalone installation. Follow [AGENTS.md](AGENTS.md).

## Change the skill

Start with an observed failure or a concrete engineering decision. Extend `tact` before introducing another overlapping skill. Keep its [four principles](README.md#four-principles), scope boundaries, and conditional reference coherent.

Use short selection metadata. Keep execution instructions in the skill, design rationale in repository documentation, and installation or evaluation procedures outside the installed package. Avoid adding a new universal rule for every failed example.

Update the README catalog and the current scenario catalog linked from [evals/README.md](evals/README.md) when behavior changes. Record actual execution separately. Do not label a static check, self-review, or simulated response as an independent model evaluation.

## Development checks

Development requires Python 3.10 or later; user installation does not require Python.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python scripts/validate.py
```

For installer or validator changes, also run:

```bash
bash -n scripts/install.sh
python3 -m unittest discover -s tests -v
```

Run relevant regression tests for other tooling changes. Exercise affected CLI operations in temporary paths. Never test installation against a real home directory or Codex/Claude Code configuration. The code-example semantic controls require Node.js 18 or later.

`validate.py` checks repository metadata conventions and standalone reference portability. It is not an official plugin schema validator. [CI](.github/workflows/validate.yml) checks structure, installer syntax, and deterministic tests on Linux and macOS without model credentials. Platform-specific claims require an actual run on that platform.

For significant instruction changes, exercise relevant [scenarios](evals/cases.md) and report the method and limits. Run the code-example controls with `node --test evals/semantic-controls.mjs`. These deterministic checks do not execute or grade a model.

For package changes, follow [plugin validation](docs/plugin.md#maintain-and-validate). Keep source completion, local installation, host selection, behavioral results, and publication separate.

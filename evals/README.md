# Evaluation evidence and translations

Scenario catalogs define expected behavior. Result documents and saved responses describe particular runs; neither proves that every scenario passes.

Repository instructions, Markdown documentation, UI metadata, and task descriptions are now in English. Historical reports and saved Markdown responses are labeled translations with links to their original versions. Translation is not a new model run, and historical character counts, tool versions, commands, and pass totals still describe the original run.

## Reproduce a historical run

Use the [complete pre-translation tree](https://github.com/awesomelon/codex-skills/tree/ce11c34e3d1da77140087300218b776594bb65cf) for original Korean skill bodies, task wording, and saved responses. For example, create an independent checkout without changing the current working tree:

```bash
git worktree add --detach ../codex-skills-original-evidence ce11c34e3d1da77140087300218b776594bb65cf
```

A historical manifest's hashes refer to the original input/skill bytes identified by that run, not the current English translations. Follow the run's source commit and manifest when replaying an evaluation. Do not rewrite recorded hashes to match translated files or count old results as validation of the English instructions.

## Raw evidence retained unchanged

| Material | Reason to preserve the original bytes |
| --- | --- |
| JSON manifests and command records | Exact requests, commands, versions, and input/output hashes |
| TAP/text logs and implementation patches | Original execution evidence and reproducible diffs |
| Historical skill snapshot in `quality-initial-SKILL.txt` | Captures the actual instructions used before a correction |
| Fixture/generated code with Korean labels and Unicode-path tests | Product strings and Unicode test inputs are behavior/evidence, not instruction prose |

These raw artifacts may contain Korean. Their surrounding explanations and translated reports are in English. For new runs, record the actual instruction/input hashes and results separately. English instructions do not force English replies: existing task requests for Korean responses remain expressed in English.

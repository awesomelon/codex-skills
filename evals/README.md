# Evaluation

[Scenarios](cases.md) define expected Tact behavior. [Results](results.md) record actual execution separately.

[Instruction coverage](coverage.md) maps the integrated criteria and their explicit boundaries to the internal references.

Use an isolated workspace with the selected skill and raw case input. Keep expected outcomes out of the evaluated model's prompt. Record the supplied files, model configuration, tool access, observed changes, checks, and final response. Mark unavailable measurements as unknown.

Structural validation, deterministic example checks, installation, automatic skill selection, and model behavior are different forms of evidence. A successful process exit does not establish task success. Review the artifact and the claims made about it.

For comparisons, keep task inputs, starting files, model settings, and permissions constant. Report the number of runs and variation; a single run does not establish reliability or improvement.

The code-example controls can be run with:

```bash
node --test evals/semantic-controls.mjs
```

They exercise runtime semantics from the scenarios. They do not execute or grade a model.

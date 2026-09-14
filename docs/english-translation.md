# English translation — 2026-09-14

Baseline: `ce11c34e3d1da77140087300218b776594bb65cf`, after PR #3 was merged. Converted 50 existing files: all three skills and references, UI metadata, AGENTS.md, README, snippets, request templates, scenario catalogs, task descriptions, audit/validation reports, and saved Markdown responses.

The purpose is consistent English terminology and direct alignment with code and upstream documentation. This work does not claim that English instructions inherently improve model quality, speed, or token use.

## Meaning and evidence

- Retained skill names, invocation policies, reference routing, and standalone installation.
- Preserved distinctions between review-only and implementation requests, required and optional validation, observations and estimates, current-state and before/after evaluation, and supported versus assumed APIs.
- Kept conditional instructions conditional: relevant references and extra checks are selected for a concrete issue, rather than made universal prerequisites.
- Preserved permissions, contract/data boundaries, valid-input assumptions, numerical metric definitions, and stopping conditions. Added one repository convention to keep maintained prose and UI metadata in English.
- Labeled 21 historical reports/responses as translations and linked each to the original file at the immutable baseline commit. Original counts and reported outcomes still describe those runs.
- Kept 39 existing raw evidence, code, test, and script files byte-for-byte unchanged. JSON manifests, logs, patches, captured skill snapshots, Korean UI strings, and Unicode-path tests retain their original content. See [evaluation evidence](../evals/README.md) for replay instructions.

Existing task/template requests for Korean replies remain English-language instructions asking for Korean output. Translating repository content does not silently change that behavior.

## Validation

- Repository structure/reference validation passed for all three skills.
- Official skill validation and UI YAML checks passed for all three, including description lengths, skill invocation examples, and preserved policy fields.
- Temporary link and copy installations on Linux each matched all 15 source skill files.
- All maintained Markdown and YAML are free of Korean prose. Local document links and JSON records were checked; existing code, tests, scripts, and raw artifacts were compared with the baseline.
- One independent review used the English React skill and translated review task in a fresh conversation. It identified tenant cache mixing and draft loss after refetch failure, retained uncertainty about omitted API internals, and avoided unnecessary draft/memo/save-state changes. It reported only static inspection and no unperformed runtime checks. All nine supplied input/skill files retained their hashes.

The [evaluation record](../evals/english-translation-2026-09-14/results.json) includes the request, input/skill hashes, English result summary, and original Korean response with temporary file links normalized. Reference use and executed checks are reported by the evaluator; input immutability was independently verified. A raw tool trace was not captured.

This is one explicit review sample, not a controlled Korean/English A/B comparison or proof of equivalence across models and scenarios. macOS hardware, desktop automatic selection, full React runtime behavior, performance, and token savings were not tested. Installer/validator code was unchanged, so the full installer suite was not repeated.

# Evidence and scope revision

Date: 2026-10-08. This report covers the unreleased instruction changes based on Tact 0.0.4. Six fresh Codex CLI contexts received the revised skill, one ordinary task request, and synthetic project files in separate temporary workspaces. Expected findings and the parent discussion were withheld. The requested model was `gpt-6.1-sol` with medium reasoning effort; the captured event stream does not emit a resolved model identifier.

[Requests](requests.json), [input fixtures](inputs/), and [metadata](metadata.json) record the supplied material, skill hashes, configuration, and evidence-selection method. Tool-event files retain completed command outputs and file-change events, rather than an evaluator's reconstruction of them.

| Case | Observed outcome | Evidence |
| --- | --- | --- |
| Indirect contract consumer | Traced the Python producer's serialized `_ack` field through the JSON contract to the JavaScript worker. A read-only in-memory execution showed that removal preserves the producer assertion but breaks acknowledgment. No files changed. | [Response](river-jobs/response.md), [tool events](river-jobs/tool-events.jsonl). |
| Rejected debugging hypothesis | Reproduced the missing invoice total, removed the agent's unsupported duplicate filter, and included the last row. Preserved the user's price normalization and unrelated note. Added five regression tests. | [Response](invoice-books/response.md), [tool events](invoice-books/tool-events.jsonl), [implementation](invoice-books/workspace/invoice.py), [tests](invoice-books/workspace/test_invoice.py). |
| Historical decision scope | Used the original attributable migration decision to distinguish an import restriction from an explicitly allowed export use. Identified two later notes as a dependent interpretation chain. Created no ADR and changed no files. | [Response](harbor-cache/response.md), [tool events](harbor-cache/tool-events.jsonl). |
| Performance claim | Identified the missing await and the Promise's missing length in the benchmark. An in-memory comparison awaited both sides, alternated order, and checked 500 outputs per run; overlapping ranges did not establish a winner. Preserved all files. | [Response](batch-export/response.md), [tool events](batch-export/tool-events.jsonl). |
| Routine edit | Corrected only the requested README typo. Created no test, plan, or decision document. | [Response](worker-guide/response.md), [tool events](worker-guide/tool-events.jsonl), [README](worker-guide/workspace/README.md). |
| Valid external boundary | Retained the necessary untrusted-input guard, found no required simplification, and exercised four valid and thirteen invalid inputs without changing files. | [Response](profile-api/response.md), [tool events](profile-api/tool-events.jsonl). |

The parent inspected responses and actual tool outputs. Independent [artifact checks](parent-checks.json) compared every project file with its starting hash, checked the allowed changed/added file sets, and confirmed every supplied skill copy matches the final skill source. For debugging, the parent ran the evaluator's tests in disposable copies of both versions: [four of five fail on the original](invoice-original-checks.txt), and [all five pass on the repair](invoice-repaired-checks.txt). The user's `parse_price` function is unchanged.

## Validation

Repository structure and Skill Creator validation passed using Python 3.12.14 with PyYAML 6.0.3 in a temporary virtual environment on macOS. The default Python lacked PyYAML; an initial sandboxed CLI attempt could not initialize. Evaluation proceeded through approved CLI execution with child workspace-write sandboxes and temporary fixtures. The earlier Python 3.9 structure check is not the supported-runtime validation recorded here. See [check output](validation.txt).

During this behavioral evaluation, installer, validator, plugin manifest, invocation metadata, and marketplace behavior were unchanged. Installation and the installer regression suite were not repeated. No installed skill or Codex configuration was modified. Subsequent version alignment and package checks are recorded separately in the [release verification](../2026-10-08-release/report.md).

## Limits

Each case ran once, with no baseline comparison, behavioral follow-up, or model judge. These observations establish the listed outcomes for these fixtures, not an improvement rate or general reliability. The new blinded-comparison procedure in the evaluation guide was not exercised as a comparison in this run.

The CLI ignored user configuration, but host authentication and system instructions remained in effect. Full prompt isolation and cross-workspace read isolation were not established; one evaluator searched the parent directory for AGENTS.md. No recorded command read another case's project contents. Several Git inspection attempts reported that the fixtures were not Git repositories. Exact command results remain in the tool events.

The benchmark fixture uses a timer to expose incomplete-work timing, not a production workload. Its measurements do not support a production performance claim. Missing-original history, dependency patches, lifecycle races, fast rejection responses, configuration mismatch, and rough-estimate variants were not all executed. Automatic skill selection, real service integration, packaging, and installation were not evaluated.

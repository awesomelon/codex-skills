# Tact 0.0.3 communication validation

Date: 2026-10-06. This report covers the local source revision, not publication or an update to the user's installed plugin.

## Method

One evaluator started without the parent conversation. It received the candidate skill, the retry input, and a request to explain the change to the engineering team. Three follow-ups requested a short settings explanation, a comparison table, and JSON-only retry status. Expected outcomes and the motivating review were withheld. A final non-behavioral follow-up requested a tool-use record.

The evaluator used a temporary workspace and preserved the supplied files. The parent read all four responses, parsed the JSON response, verified protected input hashes, and confirmed the evaluated skill bytes still matched the final source. [Run metadata](summary.json) records the hashes and review outcomes. [Requests](requests.json), [retry input](inputs/retry.md), and [settings input](inputs/settings.md) preserve the test material.

## Observed behavior

| Request | Observation | Evidence |
| --- | --- | --- |
| Retry explanation | Described one retry after 2 seconds, stable `Delivery.id`, a new `Attempt.id`, retained final error and failed-attempt history. Kept `Delivery` and `Attempt` distinct. Reported supplied local results without claiming measured performance or production reliability gains. | [Response](retry-response.md) |
| Short settings explanation | Used one compact paragraph and retained the label change, unchanged handler, observed save, and unverified keyboard behavior. | [Response](settings-response.md) |
| Table follow-up | Used the requested comparison table and preserved the keyboard verification limit. | [Response](table-response.md) |
| JSON follow-up | Returned parseable JSON with exactly `status` and `unverified`, distinguishing supplied local test results from missing production and performance evidence. | [Response](json-response.txt) |

The responses met the parent-reviewed expectations. Readability was assessed from the content and requested format, not from a ban on arrows, bold text, or lists.

## Structural and installation checks

- Repository `scripts/validate.py` and Skill Creator `quick_validate.py` passed using the bundled Python 3.12.14 with PyYAML 6.0.3 installed only in a temporary dependency folder. The default and bundled Python environments initially lacked PyYAML; the previous report's Anaconda executable was unavailable.
- Standalone copy installation passed on macOS. All six skill files matched the source; the additional `.codex-skills-install.v2` file is the installer's receipt. The initial whole-directory comparison included that receipt and was corrected to compare the skill files and account for the expected extra file.
- Codex CLI 0.160.1 installed the local marketplace package as 0.0.3 in a temporary Codex configuration. Installed skill bytes matched the source. No credentials or real Codex configuration were copied into that test configuration.
- The user's installed 0.0.2 skill still matched the base commit. The marketplace identity and root source path remained unchanged.
- Changed Markdown links, plugin/marketplace identity, and diff whitespace checks passed.

[Check commands and output](checks.json) retain successful checks and the initial dependency failures. Plugin Creator 0.1.22 did not contain `validate_plugin.py`, so no separate Plugin Creator validation was run. Installer and validator implementations were unchanged; their regression suite and unrelated code-semantic controls were not repeated.

## Limits

This is one explicit-invocation session with three behavioral follow-ups, not four independent trials. There was no baseline comparison, repeated sampling, automatic-selection measurement, or desktop plugin reload. Host instructions also shape communication, so these outcomes cannot establish how much the skill itself contributed.

The local test and browser observations in the inputs are synthetic records. The evaluator did not run a webhook implementation, local tests, a browser, or external services. Its [tool-use record](tool-use.md) is self-reported; the parent independently checked file contents and preservation. Cross-workspace read isolation was instructed but not enforced. Exact model settings, token usage, and cost were not captured.

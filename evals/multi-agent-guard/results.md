# Multi-agent improvement validation — 2026-09-18

## Scope and source rationale

Base: `awesomelon/codex-skills` at `03ed2fb24b85180b4d894c255a17dc09c403891f` (tree `ae9fcba6c3bf38180f66a612dc0d163a35a4c067`). The earlier improvements and newly merged refactoring skill are preserved.

The previous improvement prompt covered explicitly requested parallel audits, but not useful parallel implementation. The new independently installable `multi-agent-guard` adds bounded assignments, shared-artifact ownership, evidence reconciliation, failure handling, and integrated-state verification. `code-quality-guard` now checks delegated evidence and rejects vote-counted findings; `refactoring-guard` permits independent transformations while preserving shared contracts. Existing selection metadata and references in those two skills are unchanged. Coordination is not copied into every specialist or made mandatory for ordinary work.

The designated Astra article and current official skill/subagent documentation were freshly read. [Source details](../../skills/multi-agent-guard/references/sources.md) separate source guidance from this collection's implementation decisions. No external orchestration framework, hook, model setting, or installer change was imported.

## Executed checks

Environment: Linux, Python 3.13.5, Node.js v22.16.0. Git cloning was unavailable in the execution container, so scoped files were retrieved through the GitHub connector. Reconstructed original README, prompt, refactoring skill, changed evaluation files, and validation scripts were checked against their Git blob hashes before use. This was not a full checkout or a full repository test run.

- Ran the unchanged `python3 scripts/validate.py` in a disposable source snapshot containing only the complete new skill and the original validation scripts. Result: `PASS multi-agent-guard: basic metadata, portable contents, local references`. Script blobs matched `377109dd2a7aa6c0d741bebc1e6ff264ca9b0afa` (`validate.py`) and `6a051039a8f5b2a4bf95af007f1292f739add041` (`install.py`). No installer command or real home-directory modification was performed.
- Parsed the new frontmatter/UI YAML; checked matching names, explicit invocation, standalone local references, and the 127-character description. Compared the two modified existing entrypoints with the baseline: their frontmatter and reference targets are unchanged. Checked Python syntax, final newlines, whitespace, and the scoped diff.
- Ran `python3 -m unittest discover -s tests -p 'test_multi_agent_integration_fixture.py' -v`. All three calibration tests passed:

```text
test_baseline_contract_passes ... ok
test_compatible_changes_in_both_modules_pass ... ok
test_green_isolated_checks_miss_an_incompatible_tuple ... ok
Ran 3 tests
OK
```

The negative calibration reorders the producer's tenant/document tuple without changing any test. Isolated key and invalidation checks still pass; the real integration check fails with an assertion. Restoring the producer makes the combined checks pass. A separate compatible two-module refactoring also passes. These results validate the fixture's ability to expose a shared-contract failure, not an agent's ability to find or fix one.

## Not executed

No subagents were spawned in this authoring environment. No independent behavioral evaluator, actual Codex multi-agent run, automatic skill-selection evaluation, controlled before/after comparison, complete repository suite, shell-installer run, or native macOS validation was performed. The [16 new coordination cases](cases.md) and additional quality/refactoring cases are expectations, not passing model evaluations. No speed, cost, or general quality improvement is claimed from structural checks or fixture calibration.

For a behavioral evaluation, provide an independent runner only the task, revised skill, and raw fixtures; keep expected answers and this calibration record out of its context. Record actual delegation, ownership, accepted evidence, changes, checks, and read-only preservation. Do not substitute this authored record for that evaluation.

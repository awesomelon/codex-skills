# Multi-agent improvement validation — 2026-09-18

## Scope and source rationale

Collection base: `03ed2fb24b85180b4d894c255a17dc09c403891f`. Initial improvement: `16a0329b2a0e9985113fd883ddec137550fe0e99`. This record supersedes the preliminary validation prose in that initial improvement; the claims below describe the actual follow-up execution.

The new independently installable `multi-agent-guard` covers bounded investigation, review, and implementation. It distinguishes permission from an explicit delegation request, assigns shared-artifact ownership, reconciles evidence, and checks the integrated result. Timeout recovery must not create two active writers for one assignment. `code-quality-guard` verifies delegated findings instead of counting votes. `refactoring-guard` permits disjoint edits against stable shared contracts, rather than excluding all shared interfaces. The improvement prompt and catalog describe optional coordination without imposing it on every task.

The designated Astra article and official skill/subagent documentation were freshly read on 2026-09-18. The [source record](../../skills/multi-agent-guard/references/sources.md) separates source guidance from collection-specific safeguards. Short discovery descriptions, conditional references, standalone specialist skills, and existing read-only boundaries are retained. No hooks, global settings, model configuration, or installer code were changed.

## Executed checks

Environment: Linux, Python 3.13.5, Node.js v22.16.0. A Git clone attempt failed because the container could not resolve `github.com`. Files were retrieved through the GitHub connector and reconstructed for scoped execution; this is not a full repository checkout.

Before editing, reconstructed new-skill entrypoint, refactoring entrypoint, all six integration-fixture files, calibration runner, and original validation scripts were checked against their GitHub Git blob hashes. The scripts matched `377109dd2a7aa6c0d741bebc1e6ff264ca9b0afa` (`validate.py`) and `6a051039a8f5b2a4bf95af007f1292f739add041` (`install.py`).

- Ran the unchanged `python3 scripts/validate.py` in a snapshot containing only the complete new skill and those original scripts: `PASS multi-agent-guard: basic metadata, portable contents, local references`. This does not claim validation of the other six skill packages.
- Parsed the new frontmatter and UI YAML, checked matching invocation and the 127-character description, checked Python syntax and changed-file whitespace, and verified that the refactoring refinement leaves its frontmatter and reference targets unchanged.
- Ran `python3 -m unittest discover -s tests -p 'test_multi_agent_integration_fixture.py' -v`: **four calibration tests passed**. [Raw command output](validation-output.txt) and [checked-content hashes](validation-manifest.json) are preserved separately.

The calibration covers a passing baseline, compatible edits in both modules, a producer-only tuple reorder missed by isolated checks but caught by integration, and a coordinated producer/consumer reorder that preserves their mutual behavior but breaks the published tuple. The last case exposed a gap in the initial integration fixture: the producer and consumer agreeing was insufficient to establish public compatibility. A separate tuple assertion now detects it. Existing tests were retained; the harness mutates only implementation files in disposable copies.

These are fixture-calibration results, not evidence that an agent selected or followed the skill, found the failure, or repaired it.

## Not executed

No subagents were spawned and no independent behavioral evaluator or actual Codex run was performed. The [19 coordination cases](cases.md) and four added specialist cases describe expectations, not passing model evaluations. Automatic selection, a controlled before/after model comparison, the complete repository suite, shell installation, and native macOS operation remain untested. No installer command touched a real home directory or Codex configuration. No speed, token-cost, or general model-quality improvement is claimed.

For a behavioral evaluation, provide an independent runner only the task, revised skill, and raw fixtures; withhold expected answers and this calibration record. Preserve actual delegation records, ownership, changes, checks, and read-only input hashes. Do not substitute structural tests or the author's inspection for that evaluation.

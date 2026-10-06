# Tact 0.0.4 decision documentation validation

Date: 2026-10-07. This report covers the local source and isolated installation tests. It does not establish publication or an update to the user's installed plugin.

This is the initial candidate snapshot. A later clarification tightened record selection around future use and removed the fixed template. Its [focused evaluation](../2026-10-07-decisions-focus/report.md) covers the revised skill; the original evidence below is preserved. In particular, the original Redis proposal includes rollout preparation that the revised guidance now excludes.

## Method

Five evaluators started in fresh contexts with the candidate skill, a task request, and raw files in separate temporary workspaces. Expected outcomes and parent conclusions were withheld. Each saved its response and a tool-use record outside the assessed workspace. [Requests](requests.json), [inputs](inputs/), and [metadata](metadata.json) retain the supplied material, skill hashes, base commit, and available configuration details.

The parent read all responses and artifacts, independently compared file sets and hashes, checked preservation of the earlier ADR's rationale, and exercised the compatibility reader against both original and final fixtures. [Parent checks](parent-checks.json) retain the observed values and artifact hashes. At the time of this run, the seven skill files matched the evaluated copy.

## Observed behavior

| Case | Observation | Evidence |
| --- | --- | --- |
| Implementation | Added the new key with precedence over the indefinitely supported alias, updated README, and created an accepted ADR without a separate documentation request. Captured the supplied reason and rejected coordinated rollout. Six final behavior checks passed; three of those checks differ from the original behavior. Unrelated notes were preserved. | [Response](implementation/response.md), [artifacts](implementation/workspace/), [tool record](implementation/tool-use.md). |
| Existing convention | Continued the reStructuredText ADR sequence at ADR-008 in the configured directory, linked and superseded ADR-007, and preserved its original rationale. Kept backup configuration unchanged and distinguished the decision from implementation. | [Response](convention/response.md), [artifacts](convention/workspace/), [tool record](convention/tool-use.md). |
| Read-only review | Compared queue options and made a conditional recommendation, identifying the missing durability requirement. Created no ADR and changed no assessed files. | [Response](review/response.md), [tool record](review/tool-use.md). |
| Requested proposal | Created only a proposed Redis ADR. Explicitly retained unknown historical motives, pending approval and rollout, and unrun integration checks. Preserved both supplied files. | [Response](proposal/response.md), [ADR](proposal/workspace/docs/decisions/0001-migrate-sessions-to-redis.md), [tool record](proposal/tool-use.md). |
| Routine edit | Corrected only the requested typo; created no ADR, plan, or test suite. | [Response](routine/response.md), [tool record](routine/tool-use.md). |

All five cases met the expectations reviewed for this initial candidate. This assessment did not catch the unnecessary implementation and rollout detail in the Redis proposal; the focused evaluation addresses that limitation.

## Structural and installation checks

- Repository `scripts/validate.py` and Skill Creator `quick_validate.py` passed with bundled Python and PyYAML 6.0.3 installed only in a temporary dependency directory. The initial default Python lacked PyYAML; a sandboxed download then failed name resolution before an approved download succeeded. [Structural output](structure-checks.json).
- Standalone copy installation and local marketplace plugin installation passed on macOS with Codex CLI 0.160.1. All seven skill files matched the source; the plugin reported version 0.0.4. Tests used an explicit temporary standalone destination and an empty temporary Codex configuration, with no copied credentials. [Installation output and hashes](installation.json).
- Plugin Creator 0.1.22 did not include `validate_plugin.py`; no separate Plugin Creator schema validation was run. Plugin and marketplace identity, source path, policy, and category were checked against the unchanged repository convention.
- The routine evaluator attempted `git status` in its non-Git fixture and received exit 128. Its byte comparison and the parent's independent file comparison established the actual edit; the failed command is retained in its tool record.
- Installer and validator implementations were unchanged. Their regression suite and unrelated code-semantic controls were not repeated for this instruction change.

## Limits

These are five explicit-invocation smoke cases with one run per case, not a baseline comparison, repeated sampling, automatic-selection test, or general reliability measurement. The model configuration was inherited; exact resolved model identity, token usage, and cost were not captured. Host instructions may also affect behavior.

Workspace isolation was instructed but not enforced as a read boundary. Tool-use records are evaluator reports; the parent independently checked saved artifacts and fixture behavior. No queue service, Redis server, or backup infrastructure was run. No desktop reload, real installed-plugin update, Git marketplace upgrade, or publication was attempted.

The documentation-boundary variants in the scenario catalog (existing adequate rationale, explicit source-only limits, and conflicting ADR directories) received instruction review only, not additional model runs. They are not included in the five observed outcomes.

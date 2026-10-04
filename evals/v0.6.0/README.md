# Running the 0.6.0 candidate comparison

This is opt-in repository development tooling. It is not installed with either skill, and ordinary CI makes no model calls. [Results](results.md) distinguish executed checks from blocked model work.

## Prepare

Use Python 3.10+ on a POSIX host with a supported, authenticated Codex CLI. The adapter was inspected against CLI `0.159.0-alpha.3`. It uses `exec --ignore-user-config --ephemeral --sandbox workspace-write`; it retains host authentication and does not supply credentials or choose a model. Host defaults may differ between machines. Requested defaults and unexposed resolved settings are recorded separately.

Prepare a v0.5.5 source checkout and a candidate checkout, each containing `skills/`. Choose a new output directory outside both. Do not use a previous result directory: the runner refuses to overwrite evidence.

```bash
python3 scripts/run_evals.py \
  --baseline /absolute/path/to/rung-0.5.5 \
  --candidate /absolute/path/to/rung-candidate \
  --output /absolute/path/to/new-run \
  --repeat 1 --timeout 180
```

Use `--case ID` to select a bounded case; repeat the option for more cases. Run counts and timeout are explicit. After confirming the setup, predeclare repeated sampling before inspecting results. The attempted batch recorded here requested three pairs for each of ten cases, but stopped at preflight and ran none of those cases.

The current catalog also includes three post-release challenge cases: `lazy-materialization`, `valid-cached-control`, and `renamed-registry`. The default catalog now has 13 cases, so one pair per case plans 26 attempts; three repetitions plan 78. The original ten-case/60-attempt evidence is unchanged historical evidence. To run only the new cases, pass all three IDs with separate `--case` options.

These variants were authored after the unchanged 0.6.0 skill instructions. They test transfer from asynchronous to lazy work, acceptance of a legitimate cache-scoped improvement, and recurring-rule prevention in a renamed domain with changed registry values. They are public source fixtures, not an inaccessible benchmark. Independent checker controls verify the fixture distinctions; only real model runs can establish whether the skill transfers.

## What the runner does

- Freezes skill source copies and an evaluation bundle containing the catalog, selected fixtures, checker dependencies, and response rubric before preflight. Records original source locations separately from hashes of the frozen bytes, creates a separate workspace/session for each variant, and supplies only the selected endpoint.
- Retains the planned attempts before model preflight. A blocked preflight leaves cases `not_run`, rather than reporting model failures or skipping them from a success denominator.
- Alternates baseline/candidate order; invokes the CLI with argument arrays; records command, time, exit, JSON events, stderr, exposed usage, and missing metadata.
- Copies outputs before running independent checks, verifies protected inputs and skill bytes, and rejects symlink inputs.
- Keeps process status, artifact outcome, and overall acceptance separate. An artifact pass leaves response review pending; use the frozen copy of [review.md](review.md) identified by the summary and record reviewed outcomes in the result report with attempt IDs and evidence. The raw summary intentionally stays unchanged by that manual review.

The frozen bundle makes a later edit to the source repository irrelevant to the active comparison. Integrity checks reject drift in frozen evidence or mismatched copied inputs rather than silently grading another artifact. This is evidence consistency, not a security boundary: the read-isolation caveat below remains in force.

The checker dependency list is deliberately small and explicit. If a checker gains another local helper or fixture dependency, include it in the runner's frozen closure and add a control that changes the original during a fake-CLI run. An omitted dependency must not silently reintroduce live-repository reads.

Exit 2 means setup/preflight was blocked or arguments were invalid. Exit 1 means a completed batch still has failed, inconclusive, or unstarted cases; it is expected when independent response review is pending. Checker exit 1 is a rejected artifact; exit 2 is a checker infrastructure problem. A timed-out check is inconclusive, not an artifact failure.

## Isolation and interpretation

The CLI's workspace-write sandbox does not establish cross-workspace read isolation. Rubrics and logs are not supplied in task inputs, but may remain readable by the host. This adapter therefore does **not** claim a fully blinded comparison. Use a host with enforced per-run read isolation before making that claim; record any change in host configuration and rerun both variants under matching conditions.

Do not infer a skill's benefit from checker controls, a successful CLI exit, or installation alone. Review actual resource reads where traces expose them. Supplied performance observations are fixture data, not new production measurements. Replayed steering records do not test live cancellation or asynchronous execution. Automatic host discovery requires separate sessions without explicit skill names.

Do not retry authentication failures as task failures. Restore the host's supported authentication outside this runner, then use a new result directory. Keep unknown usage and cost as `null`; raw evidence may need privacy review before publication.

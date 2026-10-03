# Compatibility and versioning

Rung provides two independently usable skills and a skills-only Codex plugin. This guide defines the 1.x compatibility contract. The [release record](releases/1.0.0.md) identifies tested environments, evidence, and limitations.

## Stable entrypoints

The supported names are `rung-get-set`, `rung-go`, and plugin identity `rung@rung`. A host may display a plugin prefix; use the names in that host's current catalog.

Get Set preserves assessed material during investigation, planning, and review. Go implements and verifies authorized changes directly; a prior Get Set run is optional. Each standalone package must work without the other installed. Optional technical references do not grant implementation or delivery authority.

The contract covers task scope, evidence handling, independent use, and portable packaging. It does not promise fixed response wording, a particular internal reference path, a permanently assigned model, or identical results across models and hosts. Settings, tools, scheduling, permissions, and execution lifetimes belong to the host.

## Version changes

| Change | Release treatment |
| --- | --- |
| Correct behavior that diverges from the documented contract | Patch, with affected regression evidence |
| Add a compatible use case or optional reference | Minor, with scenario and catalog updates when relevant |
| Remove or rename an entrypoint; make assessment write by default; require Get Set before Go; remove standalone support; break documented installer options | Major, with a migration path |
| Change host prerequisites or invocation policy | Explicit compatibility assessment and release note; a breaking change needs a major release |
| Revise internal reference wording or layout | Preserve package-local links and relevant behavior; classify by its actual user impact |

Keep original source attribution and legal notices. Older installer ownership markers can retain former product identifiers; changing them requires a tested migration rather than a cosmetic rename.

## Supported environments and evidence

Publish tested OS, host version, package revision, invocation mode, and model settings alongside each release. A model setting requested by the caller is distinct from the setting observed at runtime. Unknown runtime metadata remains unknown.

The 1.0 qualification target is explicit use in macOS Codex CLI 0.160.0 with Astra/high. Desktop activation, implicit selection, live steering/cancellation/pause/resume, and compaction reliability are unqualified. Replay examples are not live-host guarantees. The [release record](releases/1.0.0.md) separates behavior, installation, and repository checks. Linux/macOS repository CI verifies deterministic checks; Linux CI is not macOS installation evidence. Windows and other hosts remain unverified until exercised.

The legacy shell installer remains macOS-specific, uses Bash 3.2-compatible syntax and BSD utilities, and requires no Python. Python remains a repository-development dependency and supports the older copy installer. Test both paths only in temporary destinations, preserving foreign links, unmanaged directories, edited managed copies, and unrelated user data.

Installation, task correctness, reference loading, implicit selection, and comparative usefulness are different evidence. A catalog listing or a passing fixture does not establish all of them. Use the release evidence to identify what was actually exercised; this compatibility contract does not guarantee identical outputs or universal task success.

## Updating and recovery

Follow the [installation guide](installation.md). Refreshing a marketplace does not prove that an existing conversation loaded the new package. Verify the installed version and start a fresh conversation when the host requires it.

Preserve local edits to installed plugin files before removal or reinstall. Native plugin removal can delete its cache; the standalone installer's edited-copy protections do not change the host's removal behavior. Keep reusable changes in the source repository.

For the transition from 0.5.5, the two current entrypoint names remain unchanged. Do not delete former CraftFlow copies or replace foreign links automatically. Inspect them, retain local changes, and remove obsolete copies only within the user's authorized scope. Old names are not reintroduced as aliases by this contract.

Before advertising rollback support, verify the chosen host's recovery procedure against a known previous payload and inspect the version loaded in a fresh conversation. A local fixture that changes only the manifest version demonstrates the package lifecycle, not a released candidate or desktop activation. Preserve remote tags and history; publish corrections as new versions rather than rewriting an existing release.

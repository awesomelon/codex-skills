# Tact 0.0.6 package verification

Date: 2026-10-08. The release integrates the existing remote main at `f0f24b7a37df87cffaa52b56ef8c711fefcc9c95`, preserving Claude Code distribution and the revised README layout. Both plugin manifests and the README now specify 0.0.6. The two marketplaces retain their existing names and root source paths.

The seven skill files still match the hashes from the [six-case behavioral evaluation](../2026-10-08-evidence/metadata.json). That evaluation was not repeated because integrating the upstream documentation and bumping package versions did not change the evaluated instruction bytes.

## Local installation

[Command results and installed file hashes](local-installation.json) record a fresh local-checkout installation in each host on macOS:

| Host | Version | Result |
| --- | --- | --- |
| Codex CLI | 0.160.1 | Marketplace registration and installation passed in an empty temporary CODEX_HOME. The installed version is 0.0.6; all seven skill files match source. |
| Claude Code | 2.1.293 | Strict validation passed for both Claude manifests. Marketplace registration and installation passed in an empty temporary CLAUDE_CONFIG_DIR. The installed version is 0.0.6; all seven skill files match source. |

Repository structural validation passed on Python 3.12.14 with PyYAML 6.0.3. Both manifests agree on plugin identity, version, and `./skills/`; both marketplaces point to the repository root. Staged changes passed whitespace checks. Plugin Creator's current installed bundle contains no `validate_plugin.py`; Codex installation and the repository checks provide the recorded validation instead.

User installations and configuration were preserved. These local-checkout tests do not establish Git marketplace refresh behavior, automatic skill selection, or Claude model behavior. The behavioral evidence uses explicit invocation in Codex CLI. Publication and remote CI outcomes are recorded in the GitHub release rather than inferred from these local checks.

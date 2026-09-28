# Reusable project learning

Use this guidance when an earlier decision could change the current approach, or verified work produced reasoning a future maintainer would otherwise have to rediscover. This is not a required final stage, a transcript archive, or permission to edit project instructions.

## Read an applicable lesson before repeating work

Search the project's existing decision records, engineering notes, issue history, or relevant module documentation for the specific mechanism at hand. Follow existing navigation; do not ingest every historical note. Inspect a candidate's evidence, affected version, assumptions, and scope against the current code and request before treating it as a constraint.

A past workaround is not a permanent product rule. Reuse what still applies, distinguish history from present requirements, and surface a real conflict with current authorized intent. Do not repeat a disproven approach just because its note is detailed, or silently rewrite policy to make the old note fit.

## Decide whether anything should be kept

Keep a lesson only when verified work establishes non-obvious project reasoning not adequately recoverable from the final code, tests, types, or existing documentation, and losing it would plausibly cause a repeated mistake, material risk, or substantial investigation. Routine fixes, generic best practices, effort spent, and a large diff do not qualify by themselves. No qualifying lesson means no new record.

Separate observed facts from causal explanations. A passing workaround does not establish the original cause; preserve an unconfirmed explanation as a hypothesis in an existing investigation record only when that is useful and authorized. Never promote it to a standing instruction.

## Update the smallest durable source within scope

Use the existing canonical home: a business rule in its product specification, an architectural tradeoff in its decision record, a setup trap in operations notes, or a reusable mechanism in engineering notes. Update or supersede an existing lesson rather than creating a competing copy. Include the non-obvious decision or mechanism, the evidence supporting it, when it applies, and what would invalidate it; let the project's format determine the layout. Avoid secrets, raw private transcripts, and machine-local paths in shared documentation.

Maintain established project documentation when the authorized implementation and repository conventions include that upkeep. A review, explanation, or planning-only request does not authorize rewriting those records. If a new documentation store or instruction-file rewrite would expand scope, return a candidate lesson instead of doing it. Never create a mandatory docs tree, host-memory store, or mirrored AGENTS.md/CLAUDE.md files just because a workflow recommends them.

Ensure the result is discoverable through the relevant existing index or local documentation entrypoint when that update is in scope. Re-read the changed statement against the implemented behavior and its evidence; keep unaffected content. Report what was actually updated, or a material reason it remains a candidate. Do not add a ceremonial learning summary to every response.

For interrupted work, use [continuity](continuity.md): a checkpoint records transient task state, whereas a lesson preserves reasoning useful beyond that task.

## Provenance

Concepts were selectively adapted in original prose on 2026-09-28, not installed as upstream workflows:

- [Dryforge ready](https://github.com/prekuter/dryforge/blob/904f25742c9e5a36b09753a7f5ea8c26801b0fa9/src/skills/ready/SKILL.md), [intent-completeness](https://github.com/prekuter/dryforge/blob/904f25742c9e5a36b09753a7f5ea8c26801b0fa9/src/skills/ready/references/intent-completeness.md), and [go](https://github.com/prekuter/dryforge/blob/904f25742c9e5a36b09753a7f5ea8c26801b0fa9/src/skills/go/SKILL.md): decision ownership, source-grounded independent scrutiny, and evaluated verification evidence. This adaptation does not adopt its three-document requirement, obligatory reviewers, immutable execution graph, risk tiers, worktree policy, or local state layout.
- [Compound Engineering ce-compound](https://github.com/EveryInc/compound-engineering-plugin/blob/8a6e0a2ff0e0d4c71cdb0b5cc4eefb847d6c646c/skills/ce-compound/SKILL.md): preserve verified reasoning only when the implementation does not already explain it, and update existing knowledge rather than duplicate it. No fixed solutions directory, automatic publishing, or whole-pipeline dependency is introduced.
- [Agent Skills constraint-driven development](https://github.com/addyosmani/agent-skills/blob/2686b620fc1fed2e8f60c704839c766b8594c6b6/skills/constraint-driven-development/SKILL.md): make the project's quality bar observable and resist hiding failed checks. No universal LOC, coverage, test-ratio, or per-change ceremony is adopted.

These are design inputs, not comparative performance evidence. The [source record](sources.md) retains the earlier OpenAI and engineering-workflow provenance.

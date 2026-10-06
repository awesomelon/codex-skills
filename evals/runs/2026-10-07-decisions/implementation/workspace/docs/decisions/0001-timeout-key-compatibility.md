# ADR-0001: Retain the legacy timeout key indefinitely

Status: Accepted
Recorded: 2026-10-07

## Context

The configuration is adopting `timeout_seconds`, but existing clients cannot
all migrate together.

## Decision

Accept both `timeout_seconds` and legacy `timeout`. Prefer `timeout_seconds`
when both are supplied, and use 30 seconds when neither is supplied. Keep the
legacy alias indefinitely so clients can migrate independently.

The behavior is implemented in [config.py](../../config.py) and described in
the [configuration guide](../../README.md).

## Alternatives considered

Removing `timeout` in the next release was considered and rejected because
it would require a coordinated client rollout.

## Consequences

Existing clients remain compatible while new clients use the clearer key.
Both names and their precedence remain part of the supported configuration
contract, with the ongoing cost of maintaining the alias.

# ADR-0001: Retain timeout compatibility

Status: Accepted
Date: 2026-09-30

The new `timeout_seconds` key will take precedence over `timeout`. Keep the legacy alias indefinitely because deployed clients cannot migrate together. Removing it in the next release was rejected because it would require a coordinated rollout. Both keys use the existing 30-second default when neither is supplied.

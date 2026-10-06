# ADR-0001: Record missing context needed for future changes

Status: Accepted
Date: 2026-10-07

Tact should save a rationale when losing it would lead a future maintainer to make a mistaken change or repeat an investigation. Code and tests often expose behavior but omit constraints such as why an apparently obsolete compatibility path must remain.

Integrate this judgment into the existing skill. Reuse the documentation a maintainer would consult; create an ADR only when the rationale needs an independent record. Adequate existing context means no new document. Preserve the read-only scope of planning and review.

A separate documentation skill would split this engineering responsibility. A mandatory ADR template would encourage filling sections regardless of future use. Neither fits the user's aim of leaving references that are useful when needed. The cost of selective recording is that agents must judge whether context is missing; evaluations must check justified omission as well as useful records.

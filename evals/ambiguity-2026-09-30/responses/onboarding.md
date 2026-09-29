Recommend improving the pending-approval handoff first and keeping document access gated until the owner’s authorization policy is settled. Do not adopt immediate access on this evidence.

The support sample from September 24–29 shows two distinct episodes, not four independent failures: T-82 forwards T-81, and T-83/T-84 describe the same approval handoff. It establishes friction but gives no completion rate or reliable estimate of prevalence.

- **Approval handoff:** T-83 cannot tell whom to contact, while T-84 does not know a request is waiting. The current pending page and manually discovered request queue explain both observations. A targeted next change would identify the responsible owner/contact on the pending page and make pending requests visible to that owner through an agreed notification mechanism. This addresses observed friction while preserving owner control; notification delivery and ownership need confirming before implementation.
- **Expired invitation:** T-81 encountered expiry after a weekend. Immediate entry after accepting a valid invitation would not solve this separate failure. Inspect the expiry and reissue/resend path next; do not lengthen expiry without establishing the intended policy and whether existing recovery is adequate.
- **Immediate document access:** A valid invitation currently creates pending membership; active membership unlocks documents. Approving later could expose downloadable documents before the owner authorizes access. Disabling membership cannot undo a download. This is a consequential access-policy change, not merely a faster onboarding screen.

**Decision needed from you:** Does an owner-issued invitation itself authorize document access, or must the owner approve acceptance separately—and does that differ for employees and external contractors? My recommendation is to retain separate approval until you and the access-policy owner explicitly settle that meaning. The decision record assigns control to the owner but does not answer this question; neither support reports nor the teammate’s suggestion establish approval to change it.

The smallest next action is a synthetic workflow check of invitation expiry/recovery and the invite → pending → owner discovery → approval path, then a scoped proposal for the pending-page guidance and owner notification. Compare that with keeping the current process plus clearer instructions: the latter is cheaper but still depends on owners manually checking settings. If checks show discovery already works through another reliable channel, the notification proposal should lose to a smaller guidance fix. If invitations are explicitly confirmed as sufficient authorization, revisit immediate activation under that policy rather than granting temporary access subject to later approval.

Acceptance evidence should show that an invitee can identify the next step, the responsible owner learns of a pending request, pending users cannot fetch documents, approved users can, and expired links lead to a usable recovery path. Measure expiry failures and time spent pending separately before claiming improved completion. No implementation or ongoing monitoring is authorized by this review.

Scope and execution record: Read only `onboarding/TASK.md`, `onboarding/evidence.md`, and the supplied skill files below. This is a current-state assessment based on supplied notes; no application code, runtime, or telemetry was available or inspected. No workflow checks, tests, interviews, or external-service calls were run. Actual checks were file discovery with `rg --files` and reading the task/evidence and skill guidance with `cat`. The assessed files were left unchanged; only this requested response record was written outside the task directory.

Skill/reference files actually read:

- `/private/tmp/rung-ambiguity-zjz664qe/skills/rung-get-set/SKILL.md`
- `/private/tmp/rung-ambiguity-zjz664qe/skills/rung-get-set/references/quality/review-scope.md`
- `/private/tmp/rung-ambiguity-zjz664qe/skills/rung-get-set/references/workflow/problem-selection.md`

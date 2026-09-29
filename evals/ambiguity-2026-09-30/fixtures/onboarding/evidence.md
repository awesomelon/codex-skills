# Support and implementation notes

Support records from 2026-09-24 to 2026-09-29:

| Record | Role | Report |
| --- | --- | --- |
| T-81 | Invited external contractor | The invitation link had expired when opened after a weekend. |
| T-82 | Workspace owner | Forward of T-81; asks why onboarding is difficult. |
| T-83 | Invited employee | Accepted invitation; screen says pending, with no indication of which owner to contact. |
| T-84 | Workspace owner | Approved T-83 the next day; did not know a request was waiting. |

This is a support sample, not a funnel or a count of all invitation attempts. There is no measured completion rate.

Current implementation: accepting a valid invitation creates a pending membership. Only an active membership can list workspace documents. Approval sets membership to active. The first successful document response can be downloaded by the recipient. Disabling membership prevents later requests but cannot recall downloaded files.

The pending page shows only "Pending". Owners can find requests by manually opening the member settings page. Invitation expiry and pending approval are separate states.

The decision record says the workspace owner controls document access. It does not say whether sending an invitation is itself sufficient approval or whether that depends on employee/contractor status. The support export contains no decision to change access policy. Product has not accepted the teammate's proposal. Synthetic accounts and synthetic documents can be used for local workflow checks.

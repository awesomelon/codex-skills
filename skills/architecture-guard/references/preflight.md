# Design preflight

Identify the responsibility owner and existing entry point for the behavior to implement. Use the target code, nearby comparable implementations, and applicable boundary rules. Do not require a design interview or a repository-wide map for a clear, small task.

Check the relevant dependency direction, state updates, consumers, deployment compatibility, and information that could reverse the decision. If requirements include another variant or a planned addition, trace where it would be added and which existing consumers and checks would change. Use that concrete comparison to judge a proposed split or shared abstraction; unspecified future possibilities do not justify extra layers. Risks in an unimplemented design remain estimates.

Record where the change belongs, contracts to preserve, and material risks and checks at a scale appropriate to the task. One or two sentences can suffice for small work. Compare only materially different alternatives and distinguish observed paths from proposed ones. Do not create an ADR simply because none exists.

A planning request is complete with the design judgment. If implementation is also requested, proceed within the authorized scope. When an unresolved decision determines an external contract, authorization, or data integrity, explain why that part needs resolution and continue work that can proceed independently.

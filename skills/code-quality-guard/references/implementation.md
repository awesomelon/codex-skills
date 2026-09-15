# Designing and implementing shared rules

Identify the product decision shared by the affected consumers and the behavior each consumer must retain. Similar expressions justify shared code only when they represent the same rule and should change together. Keep independent decisions separately changeable even when their current conditions match.

Place shared decisions where callers can use them without importing screen state or unrelated services. Keep display formatting, interaction choices, and independently edited values with the consumers that need them. A small function is often sufficient; extra options or a configurable rule system need actual differing requirements.

For an addition already present in requirements, explain where its rule would change and how existing consumers would keep working. Choose the smallest design that supports those requirements, and implement only the requested behavior. A short rationale can accompany the implementation; a separate design approval or report is unnecessary when the decision is already supported by the task.

Verify the shared decision through the affected public functions and at least the independently changing behavior relevant to the edit. Choose existing checks where suitable. Successful output alone does not establish easier extension: identify the rule definitions and consumer-specific decisions that a later change would touch. Record actual effort only when it was observed.

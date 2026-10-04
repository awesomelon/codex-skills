# Delivery service drift

The service registry owns delivery estimates and customer-visible service names. Both consumers must follow this same registry, including later service additions. Unknown codes retain their existing fallbacks.

The pickup service was previously missing from both consumers after being added to the registry. The consumers were repaired by copying the pickup values. The same failure has now recurred for next_day. Repair the cause and add a behavioral test that rejects the existing defect. The public functions, registry values, and existing tests must remain compatible.

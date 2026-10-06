# Client configuration

`timeout_seconds` sets the timeout in seconds. The legacy `timeout` key remains
supported indefinitely. If both keys are supplied, `timeout_seconds` takes
precedence. If neither is supplied, the timeout defaults to 30 seconds.

See the [compatibility decision](docs/decisions/0001-timeout-key-compatibility.md)
for the rationale.

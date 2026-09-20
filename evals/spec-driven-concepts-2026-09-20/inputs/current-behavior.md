# Accepted document exchange behavior

## Output
Export a JSON string containing numeric version 1 and an items collection. Each row contains id and title in input order.

## Input
Import version 1 items as rows containing id and title. Unsupported versions throw TypeError.

## Unaffected guarantees
Preserve Unicode titles exactly. Serialization must not mutate the caller's rows. Keep the named serialize and deserialize exports with JSON-string output/input.

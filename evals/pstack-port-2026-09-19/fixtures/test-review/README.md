# Invoice module

`total(items)` returns the sum of `quantity * cents`, with no fees or rounding.
`render(items)` returns `Total: <integer cents>`.
`send_invoice(user, items, send)` sends the rendered invoice to `user['email']` only for active users, returning whether a send happened. Denied requests send nothing.

Run existing checks: `python3 -B -m unittest -v`.

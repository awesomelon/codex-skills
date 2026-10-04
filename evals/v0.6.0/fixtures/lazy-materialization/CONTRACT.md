# Completed report timing

`measure(rows)` returns the completed report text, the number of input rows, and elapsed seconds. Report generation is lazy. Include all generation and materialization in the timed operation. Preserve line order and the exact output, including the empty-input result. Propagate generation errors without turning a partial report into a successful measurement.

Edit benchmark.py only. Preserve renderer.py and this contract. Verify the repair without claiming a comparative speedup from a corrected timer alone.

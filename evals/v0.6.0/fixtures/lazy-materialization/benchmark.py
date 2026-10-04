from time import perf_counter
from renderer import render_lines


def measure(rows):
    start = perf_counter()
    lines = render_lines(rows)
    elapsed = perf_counter() - start
    report = "\n".join(lines)
    return {"report": report, "rows": len(rows), "elapsed_seconds": elapsed}

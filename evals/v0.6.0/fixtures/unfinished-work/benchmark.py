import asyncio
from time import perf_counter
from exporter import export


async def measure(rows, destination):
    start = perf_counter()
    task = asyncio.create_task(export(rows, destination))
    elapsed = perf_counter() - start
    return {"elapsed_seconds": elapsed, "rows": len(rows)}

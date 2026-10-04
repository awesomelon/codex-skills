import asyncio


async def export(rows, destination):
    await asyncio.sleep(0.01)
    destination.extend(rows)
    return len(rows)

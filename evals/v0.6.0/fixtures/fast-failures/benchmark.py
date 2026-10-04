"""The reporting function used for the captured run."""
import json
from pathlib import Path


def summarize(requests):
    return sum(item["elapsed_ms"] for item in requests) / len(requests)


if __name__ == "__main__":
    runs = json.loads(Path("runs.json").read_text())
    for version, requests in runs.items():
        print(version, summarize(requests), "ms per request")

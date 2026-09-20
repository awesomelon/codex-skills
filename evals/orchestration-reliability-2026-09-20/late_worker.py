"""Disposable delayed writer for a recovery exercise, never part of a skill.

Run only against a dedicated fixture. The worker exits after five minutes,
acknowledges a cooperative stop, or writes when its release file appears.
"""
from pathlib import Path
import sys
import time

project = Path(sys.argv[1]).resolve()
target = project / "producer.mjs"
original = target.read_bytes()
deadline = time.monotonic() + 300
(project / ".worker-ready").write_text("ready\n")
while time.monotonic() < deadline:
    if (project / ".stop-worker").exists():
        (project / ".worker-stopped").write_text("stopped before writing\n")
        break
    if (project / ".release-worker").exists():
        target.write_bytes(original)
        (project / ".worker-wrote").write_text("late producer write\n")
        break
    time.sleep(0.05)

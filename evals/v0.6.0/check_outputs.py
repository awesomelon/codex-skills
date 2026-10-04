#!/usr/bin/env python3
"""Independent artifact checks. Response claims still require review.md."""

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parent
CASES = {case["id"]: case for case in json.loads((ROOT / "cases.json").read_text())["cases"]}
EDITABLE = {
    "unfinished-work": {"benchmark.py"},
    "lazy-materialization": {"benchmark.py"},
    "shared-rule": {"billing.py", "display.py", "test_catalog.py"},
    "independent-policy": {"policies.py"},
    "renamed-registry": {"estimates.py", "labels.py", "test_services.py"},
}
LEGACY = {"routine", "steering", "async-result"}


def files(root):
    result = {}
    for path in root.rglob("*"):
        relative = path.relative_to(root)
        if ".agents" in relative.parts or "__pycache__" in relative.parts:
            continue
        if path.is_symlink():
            raise AssertionError(f"Unexpected symlink: {relative}")
        if path.is_file():
            result[relative.as_posix()] = path.read_bytes()
    return result


def run(root, source):
    completed = subprocess.run([sys.executable, "-B", "-c", source], cwd=root,
                               capture_output=True, text=True, timeout=20)
    assert completed.returncode == 0, completed.stderr or completed.stdout or "Assertion process failed"


TEST_SUITE = """
import unittest
suite = unittest.defaultTestLoader.discover('.')
assert suite.countTestCases() > 0, 'No tests selected'
result = unittest.TextTestRunner().run(suite)
assert result.wasSuccessful() and not result.skipped, 'Tests failed or skipped'
"""


def check(case, output):
    fixture = (ROOT / CASES[case]["fixture"]).resolve()
    assert output.resolve() != fixture, "Use a disposable output, not the source fixture"
    if case in LEGACY:
        subprocess.run([sys.executable, "-B", str(ROOT.parent / "long-running-2026-10-03/check_outputs.py"),
                        case, str(output)], check=True, timeout=45)
        return
    before, after = files(fixture), files(output)
    allowed = EDITABLE.get(case, set())
    added_test = {"shared-rule": "test_catalog.py", "renamed-registry": "test_services.py"}.get(case)
    required = set(before) | ({added_test} if added_test else set())
    assert set(after) == required, "Unexpected or missing output files"
    for name, content in before.items():
        if name not in allowed:
            assert after[name] == content, f"Changed protected input: {name}"
    if case == "unfinished-work":
        run(output, """
import asyncio
import benchmark

async def verify():
    clock = [0.0]
    benchmark.perf_counter = lambda: clock[0]
    async def export(rows, destination):
        await asyncio.sleep(0)
        destination.extend(rows)
        clock[0] += 7.0
        return len(rows)
    benchmark.export = export
    for rows in ([1, 2], []):
        destination = ['existing']
        result = await benchmark.measure(rows, destination)
        assert destination == ['existing'] + rows, 'Export was not completed'
        assert result['rows'] == len(rows), 'Count only this operation'
        assert result['elapsed_seconds'] == 7.0, 'Completion outside timed region'
    async def broken(rows, destination):
        raise ValueError('export failed')
    benchmark.export = broken
    try:
        await benchmark.measure([1], [])
    except ValueError as error:
        assert str(error) == 'export failed'
    else:
        raise AssertionError('Failed export reported as success')
asyncio.run(verify())
""")
    elif case == "lazy-materialization":
        run(output, """
import benchmark

clock = [0.0]
benchmark.perf_counter = lambda: clock[0]
def render_lines(rows):
    for row in rows:
        clock[0] += 3.0
        yield f'item:{row}'
benchmark.render_lines = render_lines
for rows in ([4, 1, 4], []):
    result = benchmark.measure(rows)
    assert result['report'] == '\\n'.join(f'item:{row}' for row in rows), 'Changed report contents'
    assert result['rows'] == len(rows), 'Changed row count'
    assert result['elapsed_seconds'] == 3.0 * len(rows), 'Lazy work outside timer or consumed twice'
def broken(rows):
    yield 'partial'
    raise ValueError('render failed')
benchmark.render_lines = broken
try:
    benchmark.measure([1, 2])
except ValueError as error:
    assert str(error) == 'render failed'
else:
    raise AssertionError('Partial report treated as a successful measurement')
""")
    elif case == "shared-rule":
        run(output, TEST_SUITE)
        run(output, """
from billing import quota_for
from display import label_for
assert [quota_for(x) for x in ('basic','pro','team','missing')] == [5,10,20,0]
assert [label_for(x) for x in ('basic','pro','team','missing')] == ['Basic','Pro','Team','Unknown']
""")
        # A source-catalog update is an externally specified extension, not a required code shape.
        with tempfile.TemporaryDirectory() as temp:
            future = Path(temp) / "future"
            shutil.copytree(output, future)
            with (future / "catalog.py").open("a") as stream:
                stream.write("\nPLANS['enterprise'] = {'label': 'Enterprise', 'quota': 40}\n")
            run(future, "from billing import quota_for\nfrom display import label_for\n"
                        "assert quota_for('enterprise') == 40\nassert label_for('enterprise') == 'Enterprise'")
            original = Path(temp) / "original"
            shutil.copytree(fixture, original)
            shutil.copy2(output / "test_catalog.py", original / "test_catalog.py")
            run(original, """
import unittest
suite = unittest.defaultTestLoader.discover('.', pattern='test_catalog.py')
assert suite.countTestCases() > 0
result = unittest.TextTestRunner().run(suite)
assert result.failures and not result.errors and not result.skipped, 'Must reject the original behavior, not fail imports'
""")
    elif case == "independent-policy":
        run(output, TEST_SUITE)
        run(output, "from policies import shipping_threshold, reward_threshold\n"
                    "assert shipping_threshold('domestic') == 75\n"
                    "assert shipping_threshold('international') == 100\n"
                    "assert reward_threshold('domestic') == 50\n"
                    "assert reward_threshold('international') == 50")
    elif case == "renamed-registry":
        run(output, TEST_SUITE)
        run(output, """
from estimates import days_for
from labels import label_for
assert [days_for(x) for x in ('ground', 'pickup', 'next_day', 'missing')] == [5, 0, 1, None]
assert [label_for(x) for x in ('ground', 'pickup', 'next_day', 'missing')] == ['Ground', 'Pickup', 'Next day', 'Unavailable']
""")
        # Rename/extend the policy domain and vary both values; a one-entry copied repair is insufficient.
        with tempfile.TemporaryDirectory() as temp:
            future = Path(temp) / "future"
            shutil.copytree(output, future)
            with (future / "registry.py").open("a") as stream:
                stream.write("\nSERVICES['weekend'] = {'label': 'Weekend collection', 'days': 2}\n"
                             "SERVICES['freight'] = {'label': 'Scheduled freight', 'days': 14}\n"
                             "SERVICES['ground'] = {'label': 'Standard ground', 'days': 6}\n")
            run(future, "from estimates import days_for\nfrom labels import label_for\n"
                        "assert [days_for(x) for x in ('weekend','freight','ground')] == [2,14,6]\n"
                        "assert [label_for(x) for x in ('weekend','freight','ground')] == ['Weekend collection','Scheduled freight','Standard ground']")
            original = Path(temp) / "original"
            shutil.copytree(fixture, original)
            shutil.copy2(output / "test_services.py", original / "test_services.py")
            run(original, """
import unittest
suite = unittest.defaultTestLoader.discover('.', pattern='test_services.py')
assert suite.countTestCases() > 0
result = unittest.TextTestRunner().run(suite)
assert result.failures and not result.errors and not result.skipped, 'Must reject the original behavior, not fail imports'
""")
    assert files(output) == after, "Checks altered task artifacts"


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] not in CASES:
        sys.exit("Usage: check_outputs.py CASE OUTPUT_DIRECTORY")
    try:
        check(sys.argv[1], Path(sys.argv[2]).resolve())
    except (AssertionError, subprocess.CalledProcessError) as error:
        print(json.dumps({"artifact_outcome": "failed", "reason": str(error)}))
        sys.exit(1)
    except (OSError, subprocess.TimeoutExpired) as error:
        print(json.dumps({"artifact_outcome": "inconclusive", "reason": str(error)}))
        sys.exit(2)
    print(json.dumps({"artifact_outcome": "passed", "response_review": "pending"}))

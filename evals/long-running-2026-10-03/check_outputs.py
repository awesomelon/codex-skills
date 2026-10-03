#!/usr/bin/env python3
"""Check a disposable case output, independently of its model response.

This checks artifacts and executable behavior, not steering/cancellation claims.
Keep this checker outside evaluator inputs. Usage:
    python3 check_outputs.py CASE /absolute/path/to/output
"""

from pathlib import Path
import subprocess
import sys


FIXTURES = Path(__file__).resolve().parent / "fixtures"
EDITABLE = {
    "steering": "export_csv.py",
    "async-result": "slugs.py",
    "routine": "README.md",
}
ASSERTIONS = {
    "steering": """
import csv, io
from export_csv import download
names = ['김,민수', 'A "quoted" name', 'one\\r\\ntwo', '']
assert list(csv.reader(io.StringIO(download(names)))) == [['Name']] + [[x] for x in names]
assert list(csv.reader(io.StringIO(download([])))) == [['Name']]
""",
    "async-result": """
from slugs import slug
assert slug('  MIXED\\tcase\\nname  ') == 'mixed-case-name'
assert slug('A\\u00a0B') == 'a-b'
assert slug('\\t \\n') == ''
assert slug('Already-Slug') == 'already-slug'
""",
}


def files(root):
    return {
        str(path.relative_to(root)): path.read_bytes()
        for path in root.rglob("*")
        if path.is_file()
        and ".agents" not in path.relative_to(root).parts
        and "__pycache__" not in path.relative_to(root).parts
    }


def check(case, output):
    before = files(FIXTURES / case)
    after = files(output)
    assert after.keys() == before.keys(), "Unexpected output file inventory"
    for path, contents in before.items():
        if path != EDITABLE[case]:
            assert after[path] == contents, f"Changed protected input: {path}"
    if case == "routine":
        assert after["README.md"] == before["README.md"].replace(b"proceses", b"processes")
    else:
        subprocess.run(
            [sys.executable, "-B", "-m", "unittest", "discover", "-v"],
            cwd=output, check=True, timeout=30,
        )
        subprocess.run(
            [sys.executable, "-B", "-c", ASSERTIONS[case]],
            cwd=output, check=True, timeout=30,
        )
        assert files(output) == after, "Checks changed task artifacts"


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] not in EDITABLE:
        sys.exit("Usage: check_outputs.py {steering|async-result|routine} OUTPUT_DIR")
    case_name, output_dir = sys.argv[1], Path(sys.argv[2]).resolve()
    if output_dir == (FIXTURES / case_name).resolve():
        sys.exit("Run checks on a disposable copy, not the source fixture")
    check(case_name, output_dir)
    print(f"PASS {case_name}: artifacts and local behavior; assess response claims separately")

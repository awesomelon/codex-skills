#!/usr/bin/env python3
"""Opt-in Codex comparisons. No model calls are made by ordinary repository CI."""

import argparse
from collections import Counter
import hashlib
import json
import os
import platform
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import time
import uuid
from datetime import datetime, timezone


REPO = Path(__file__).resolve().parents[1]
CATALOG = REPO / "evals/v0.6.0/cases.json"


def write_json(path, value):
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")
    temporary.replace(path)


def inventory(root):
    """Hash every source file, refusing links rather than following them."""
    result = {}
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"Symlink is not a supported evaluation input: {path}")
        if path.is_file():
            result[path.relative_to(root).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def execute(argv, cwd, destination, timeout):
    destination.mkdir(parents=True, exist_ok=True)
    start = time.monotonic()
    started_at = datetime.now(timezone.utc).isoformat()
    status, code = "completed", None
    with (destination / "stdout.jsonl").open("wb") as stdout, (destination / "stderr.txt").open("wb") as stderr:
        try:
            process = subprocess.Popen(argv, cwd=cwd, stdin=subprocess.DEVNULL,
                                       stdout=stdout, stderr=stderr, start_new_session=True)
        except OSError as error:
            stderr.write(str(error).encode())
            status = "launch_failed"
        else:
            try:
                code = process.wait(timeout=timeout)
            except subprocess.TimeoutExpired:
                status = "timed_out"
                try:
                    os.killpg(process.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
                process.wait()
    return {"command": argv, "execution_status": status, "exit_code": code,
            "started_at": started_at, "ended_at": datetime.now(timezone.utc).isoformat(),
            "elapsed_seconds": time.monotonic() - start}


def events(path):
    parsed = []
    for line in path.read_text(errors="replace").splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(event, dict):
            parsed.append(event)
    return parsed


def metadata(logs):
    items = events(logs / "stdout.jsonl")
    completions = [item for item in items if item.get("type") == "turn.completed"]
    return {
        "turn_completed": bool(completions),
        "turn_failed": any(item.get("type") == "turn.failed" for item in items),
        "observed_model": None, "observed_effort": None,
        "usage": completions[-1].get("usage") if completions else None,
        "cost": None,
        "resource_reads": None,
        "resource_read_note": "Inspect command/tool events; a generated response is not a read trace.",
    }


def prerequisite_failure(logs):
    text = "\n".join((logs / name).read_text(errors="replace")
                     for name in ("stdout.jsonl", "stderr.txt")).lower()
    # Only specific execution/authentication failures stop the whole batch.
    return any(term in text for term in (
        "401 unauthorized", "access token could not be refreshed",
        "failed to initialize in-process app-server client", "insufficient_quota",
    ))


def command(binary, workspace, response, prompt):
    return [binary, "exec", "--ignore-user-config", "--ephemeral",
            "--skip-git-repo-check", "--sandbox", "workspace-write", "--color", "never",
            "--json", "-C", str(workspace), "-o", str(response), prompt]


def load_cases(path, selected):
    cases = json.loads(path.read_text())["cases"]
    ids = [case["id"] for case in cases]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate case IDs")
    if set(selected) - set(ids):
        raise ValueError("Unknown case selection")
    for case in cases:
        fixture = (path.parent / case["fixture"]).resolve()
        if not fixture.is_relative_to(REPO / "evals") or not fixture.is_dir():
            raise ValueError("Fixture must be a directory within repository evals")
        if case["skill"] not in ("rung-go", "rung-get-set"):
            raise ValueError("Unknown skill endpoint")
    return [case for case in cases if not selected or case["id"] in selected]


def run(args):
    if os.name != "posix":
        raise ValueError("This adapter currently supports POSIX process-group cleanup only")
    cases = load_cases(CATALOG, args.case)
    output = Path(args.output).resolve()
    roots = {name: Path(getattr(args, name)).resolve() for name in ("baseline", "candidate")}
    for root in [REPO, *roots.values()]:
        if output.is_relative_to(root) or root.is_relative_to(output):
            raise ValueError("Output must be outside and not contain the repository or either source")
    if output.exists():
        raise ValueError("Output must be a new directory; previous evidence is never overwritten")
    if args.repeat < 1 or args.timeout <= 0:
        raise ValueError("Repeat and timeout must be positive")
    # Validate all sources before making any workspaces.
    hashes = {name: inventory(root / "skills") for name, root in roots.items()}
    for name, files in hashes.items():
        if any(f"{skill}/SKILL.md" not in files for skill in ("rung-go", "rung-get-set")):
            raise ValueError(f"{name} must contain both skill sources")
    output.mkdir(parents=True)
    for name, root in roots.items():
        shutil.copytree(root / "skills", output / "sources" / name / "skills")
    attempts = []
    for repetition in range(1, args.repeat + 1):
        for index, case in enumerate(cases):
            order = ("baseline", "candidate") if (repetition + index) % 2 else ("candidate", "baseline")
            for variant in order:
                attempts.append({"id": uuid.uuid4().hex, "case": case["id"], "variant": variant,
                                 "repetition": repetition, "execution_status": "not_run", "outcome": "not_run"})
    report = {
        "schema_version": 1, "source_paths": {k: str(v) for k, v in roots.items()},
        "skill_hashes": hashes, "catalog_hash": hashlib.sha256(CATALOG.read_bytes()).hexdigest(),
        "checker_hash": hashlib.sha256((CATALOG.parent / "check_outputs.py").read_bytes()).hexdigest(),
        "host": {"os": platform.platform(), "python": platform.python_version(), "cli_version": None},
        "requested_model": "host default", "requested_effort": "host default",
        "invocation_mode": "explicit", "attempts": attempts,
        "isolation": "Separate workspaces/sessions, workspace-write sandbox; cross-workspace read isolation is NOT established.",
        "limits": ["Not a fully blinded experiment: this CLI sandbox may read paths outside its workspace.",
                   "No automatic discovery or live steering claim.",
                   "Final-response claims require independent review using review.md."],
    }
    summary = output / "summary.json"
    write_json(summary, report)
    try:
        version = subprocess.run([args.codex, "--version"], stdin=subprocess.DEVNULL,
                                 capture_output=True, text=True, timeout=10)
        if version.returncode == 0:
            report["host"]["cli_version"] = version.stdout.strip()
    except (OSError, subprocess.TimeoutExpired):
        pass
    probe = output / "work" / uuid.uuid4().hex
    probe.mkdir(parents=True)
    logs = output / "preflight"
    response = logs / "response.txt"
    result = execute(command(args.codex, probe, response,
                             "Reply with READY. Do not use tools or edit files."), probe, logs, min(args.timeout, 45))
    result.update(metadata(logs))
    result["outcome"] = "passed" if (
        result["exit_code"] == 0 and result["turn_completed"] and not result["turn_failed"]
        and response.exists() and response.read_text().strip() == "READY"
    ) else "blocked"
    report["preflight"] = result
    write_json(summary, report)
    if result["outcome"] != "passed":
        print(f"BLOCKED: model preflight; all {len(attempts)} case attempts are not_run. See {summary}")
        return 2
    by_id = {case["id"]: case for case in cases}
    checker = CATALOG.parent / "check_outputs.py"
    for attempt in attempts:
        case = by_id[attempt["case"]]
        workspace = output / "work" / attempt["id"]
        fixture = (CATALOG.parent / case["fixture"]).resolve()
        inventory(fixture)
        shutil.copytree(fixture, workspace)
        # Explicit endpoint evaluation supplies only that independently installable skill.
        skill = case["skill"]
        supplied = workspace / ".agents/skills" / skill
        shutil.copytree(output / "sources" / attempt["variant"] / "skills" / skill, supplied)
        before_skills = inventory(workspace / ".agents")
        attempt["input_hashes"] = inventory(workspace)
        logs = output / "attempts" / attempt["id"]
        response = logs / "response.txt"
        prompt = f"Use ${skill} from .agents/skills/{skill}/SKILL.md. {case['prompt']}"
        attempt["prompt"] = prompt
        attempt.update(execute(command(args.codex, workspace, response, prompt), workspace, logs, args.timeout))
        attempt.update(metadata(logs))
        attempt["outcome"] = "inconclusive"
        if prerequisite_failure(logs):
            attempt["outcome"] = "blocked"
            write_json(summary, report)
            break
        if attempt["execution_status"] == "completed" and attempt["turn_completed"] and not attempt["turn_failed"]:
            try:
                attempt["output_hashes"] = inventory(workspace)
                skills_preserved = inventory(workspace / ".agents") == before_skills
                # Check a separate snapshot: checks cannot modify the candidate's artifact evidence.
                checked = output / "checks" / attempt["id"]
                shutil.copytree(workspace, checked)
                check = execute([sys.executable, str(checker), case["id"], str(checked)],
                                REPO, logs / "checker", min(args.timeout, 60))
                attempt["checker"] = check
                if check["execution_status"] != "completed":
                    attempt["artifact_outcome"] = "inconclusive"
                elif check["exit_code"] == 0 and skills_preserved:
                    attempt["artifact_outcome"] = "passed"
                    attempt["review_status"] = "pending"
                    # Artifact correctness does not establish truthful response claims.
                elif check["exit_code"] == 1 or not skills_preserved:
                    attempt["artifact_outcome"] = "failed"
                    attempt["outcome"] = "failed"
                else:
                    attempt["artifact_outcome"] = "inconclusive"
            except (ValueError, OSError) as error:
                attempt["outcome"] = "inconclusive"
                attempt["check_error"] = str(error)
        write_json(summary, report)
    report["counts"] = dict(Counter(item["outcome"] for item in attempts))
    write_json(summary, report)
    print(json.dumps({"summary": str(summary), "counts": report["counts"]}))
    return 1 if any(a["outcome"] != "passed" for a in attempts) else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", required=True, help="Repository/snapshot containing baseline skills/")
    parser.add_argument("--candidate", required=True, help="Repository/snapshot containing candidate skills/")
    parser.add_argument("--output", required=True, help="New evidence directory outside both sources")
    parser.add_argument("--case", action="append", default=[])
    parser.add_argument("--repeat", type=int, default=1)
    parser.add_argument("--timeout", type=float, default=180)
    parser.add_argument("--codex", default="codex", help="Supported CLI executable (not a shell command)")
    args = parser.parse_args()
    try:
        return run(args)
    except (ValueError, OSError, KeyError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    sys.exit(main())

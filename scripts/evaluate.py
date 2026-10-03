#!/usr/bin/env python3
"""Run the bounded Rung pilot. No installation or user configuration changes.

Model execution currently requires macOS Seatbelt. Deterministic unit tests use
fake processes; a passing unit test is not a completed behavioral evaluation.
"""

from __future__ import annotations

import argparse
from collections import Counter
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import platform
import shutil
import signal
import subprocess
import sys
import tempfile
import time
import uuid


ROOT = Path(__file__).resolve().parents[1]
SUITE = ROOT / "evals/release-1.0"
SCHEMA = 1
OUTCOMES = {"passed", "failed", "blocked", "inconclusive"}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_json(path: Path, value: object) -> None:
    with path.open("x", encoding="utf-8") as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write("\n")


def inventory(root: Path) -> dict[str, str]:
    """Hash files and empty directories; never follow artifact symlinks."""
    result = {}
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        if path.is_symlink():
            raise ValueError(f"Symlink in artifact tree: {relative}")
        if ".git" in relative.parts or "__pycache__" in relative.parts:
            continue
        if path.is_file():
            result[relative.as_posix()] = digest(path.read_bytes())
        elif path.is_dir():
            result[relative.as_posix() + "/"] = "directory"
        else:
            raise ValueError(f"Unsupported artifact: {relative}")
    return result


def contained(root: Path, relative: str) -> Path:
    path = root / relative
    if not relative or Path(relative).is_absolute() or ".." in Path(relative).parts:
        raise ValueError(f"Expected a relative path inside the suite: {relative}")
    if not path.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"Path escapes suite: {relative}")
    cursor = root
    for part in Path(relative).parts:
        cursor = cursor / part
        if cursor.is_symlink():
            raise ValueError(f"Symlink in suite path: {relative}")
    return path


def load_case(case_id: str) -> dict:
    manifest = json.loads((SUITE / "manifest.json").read_text())
    if manifest.get("schema_version") != SCHEMA:
        raise ValueError("Unsupported suite schema")
    if case_id not in manifest["cases"]:
        raise ValueError(f"Unknown case: {case_id}")
    case = manifest["cases"][case_id]
    fixture = contained(SUITE, case["fixture"])
    inventory(fixture)
    if not (fixture / "TASK.md").is_file():
        raise ValueError("Case has no TASK.md")
    for field in ("editable", "staged"):
        for name in case.get(field, []):
            if not contained(fixture, name).is_file():
                raise ValueError(f"Missing {field} file: {name}")
    if case.get("git_base"):
        base = contained(SUITE, case["git_base"])
        if not base.is_dir():
            raise ValueError("Missing Git base")
        inventory(base)
    return case


def capture(command: list[str], *, cwd: Path, timeout: float,
            prompt: str = "", env: dict | None = None) -> dict:
    start = time.monotonic()
    started = datetime.now(timezone.utc).isoformat()
    try:
        process = subprocess.Popen(command, cwd=cwd, env=env, text=True,
                                   stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, start_new_session=True)
    except OSError as exc:
        return {"command": command, "started_at": started, "elapsed_seconds": 0,
                "exit_code": None, "timed_out": False, "cleanup": "not_started",
                "stdout": "", "stderr": str(exc)}
    timed_out = False
    interrupted = False

    def kill_group() -> None:
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass

    cleanup_unconfirmed = False
    try:
        stdout, stderr = process.communicate(prompt, timeout=timeout)
    except (subprocess.TimeoutExpired, KeyboardInterrupt) as interruption:
        timed_out = isinstance(interruption, subprocess.TimeoutExpired)
        interrupted = isinstance(interruption, KeyboardInterrupt)
        kill_group()
        try:
            stdout, stderr = process.communicate(timeout=5)
        except subprocess.TimeoutExpired as exc:
            cleanup_unconfirmed = True
            stdout, stderr = exc.stdout or "", exc.stderr or ""
            stdout = stdout.decode(errors="replace") if isinstance(stdout, bytes) else stdout
            stderr = stderr.decode(errors="replace") if isinstance(stderr, bytes) else stderr
            for stream in (process.stdin, process.stdout, process.stderr):
                if stream:
                    stream.close()
            process.poll()
    except BaseException:
        kill_group()
        process.communicate(timeout=5)
        raise
    # A detached descendant is not proven stopped by process-group cleanup.
    try:
        os.killpg(process.pid, 0)
    except ProcessLookupError:
        cleanup = "process_group_exited"
    else:
        kill_group()
        cleanup = "remaining_group_killed"
    if cleanup_unconfirmed:
        cleanup = "unconfirmed"
    return {"command": command, "started_at": started,
            "elapsed_seconds": round(time.monotonic() - start, 6),
            "exit_code": process.returncode, "timed_out": timed_out, "interrupted": interrupted,
            "cleanup": cleanup, "stdout": stdout, "stderr": stderr}


def git(work: Path, *args: str) -> str:
    env = dict(os.environ, GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull,
               GIT_OPTIONAL_LOCKS="0", GIT_AUTHOR_DATE="2000-01-01T00:00:00Z",
               GIT_COMMITTER_DATE="2000-01-01T00:00:00Z")
    result = subprocess.run(
        ["git", "-c", "core.hooksPath=/dev/null", "-c", "core.fsmonitor=false",
         "-c", "commit.gpgsign=false", "-c", "user.name=Rung Evaluation",
         "-c", "user.email=evaluation@example.invalid", *args],
        cwd=work, env=env, text=True, capture_output=True, timeout=10, check=True)
    return result.stdout


def git_state(work: Path) -> dict | None:
    if not (work / ".git").exists():
        return None
    if (work / ".git").is_symlink() or not (work / ".git").is_dir():
        raise ValueError("Unexpected Git directory")
    return {"head": git(work, "rev-parse", "HEAD").strip(),
            "index": git(work, "ls-files", "--stage"),
            "exclude_sha256": digest((work / ".git/info/exclude").read_bytes()),
            "status": git(work, "status", "--porcelain=v1", "--untracked-files=all")}


def prepare(case: dict, work: Path, variant: str) -> dict:
    work.mkdir()
    if case.get("git_base"):
        shutil.copytree(contained(SUITE, case["git_base"]), work, dirs_exist_ok=True)
        shutil.copyfile(contained(SUITE, case["fixture"]) / "TASK.md", work / "TASK.md")
        git(work, "init", "--quiet")
        git(work, "add", ".")
        git(work, "commit", "--quiet", "-m", "Fixture baseline")
        # Assigned evaluation resources must not become part of the review diff.
        with (work / ".git/info/exclude").open("a") as stream:
            stream.write("\n/.agents/\n")
    shutil.copytree(contained(SUITE, case["fixture"]), work, dirs_exist_ok=True)
    if case.get("staged"):
        git(work, "add", "--", *case["staged"])
    if variant == "rung":
        inventory(ROOT / "skills")
        for name in case.get("installed_skills", ["rung-get-set", "rung-go"]):
            shutil.copytree(contained(ROOT / "skills", name), work / ".agents/skills" / name)
    return {"files": inventory(work), "git": git_state(work),
            "git_config": digest((work / ".git/config").read_bytes())
            if (work / ".git/config").exists() else None}


def codex_root() -> Path:
    return Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))).resolve()


def runtime_environment(state: Path) -> dict:
    """Configure only the child CLI's documented state root, not the user's shell."""
    rung_codex_home = state / "codex"
    rung_codex_home.mkdir(exist_ok=True)
    (state / "tmp").mkdir(exist_ok=True)
    return dict(os.environ, CODEX_HOME=str(rung_codex_home), TMPDIR=str(state / "tmp"))


@contextmanager
def native_auth(state: Path):
    """Reference the native login without opening, copying, or exporting tokens."""
    runtime_environment(state)
    original = codex_root() / "auth.json"
    if not original.is_file():
        raise ValueError("Native file-based CLI login is unavailable; no credentials were copied")
    reference = state / "codex/auth.json"
    reference.symlink_to(original)
    try:
        yield
    finally:
        # Also remove a cache the CLI may have atomically replaced after refresh.
        reference.unlink(missing_ok=True)


def runtime_settings(work: Path, state: Path, *, readonly: bool = False,
                     model: str | None = None, effort: str | None = None) -> list[str]:
    filesystem = {":root": "read", ":workspace_roots": "read" if readonly else "write",
                  str(ROOT): "deny", str(codex_root()): "deny",
                  str(Path.home() / ".agents"): "deny", str(state): "deny"}
    fs_toml = "{" + ",".join(json.dumps(k) + "=" + json.dumps(v)
                              for k, v in filesystem.items()) + "}"
    config = ["approval_policy=\"never\"", "default_permissions=\"rung_eval\"",
              "permissions.rung_eval.filesystem=" + fs_toml,
              "permissions.rung_eval.network.enabled=false",
              "sqlite_home=" + json.dumps(str(state / "sqlite")),
              "log_dir=" + json.dumps(str(state / "logs")),
              "features.apps=false", "features.plugins=false", "features.multi_agent=false",
              "web_search=\"disabled\""]
    if model:
        config += ["model=" + json.dumps(model)]
    if effort:
        config += ["model_reasoning_effort=" + json.dumps(effort)]
    return [argument for setting in config for argument in ("-c", setting)]


def native_sandbox(command: list[str], work: Path, state: Path, *,
                   binary: str | None = None, readonly: bool = True) -> dict:
    binary = binary or shutil.which("codex") or "codex"
    invocation = [binary, "--no-daemon", *runtime_settings(work, state, readonly=readonly),
                  "sandbox", "-C", str(work), "-P", "rung_eval", "--", *command]
    return capture(invocation, cwd=work, timeout=30, env=runtime_environment(state))


def preflight(work: Path, state: Path, binary: str | None = None) -> dict:
    if sys.version_info < (3, 10):
        return {"status": "blocked", "reason": "Python 3.10 or later is required"}
    if platform.system() != "Darwin" or not Path("/usr/bin/sandbox-exec").is_file():
        return {"status": "blocked", "reason": "The pilot currently requires macOS Seatbelt"}
    binary = shutil.which(binary or "codex")
    if not binary:
        return {"status": "blocked", "reason": "Codex CLI not found"}
    environment = runtime_environment(state)
    (state / "read-canary.txt").write_text("Non-sensitive state boundary probe.\n")
    # Probe actual denials and an allowed write before launching any model.
    probe = (
        "from pathlib import Path\n"
        f"root=Path({str(ROOT)!r})\n"
        "try:\n root.joinpath('README.md').read_bytes()\n"
        "except PermissionError:\n pass\n"
        "else:\n raise SystemExit('source read was not denied')\n"
        f"try:\n Path({str(state / 'read-canary.txt')!r}).read_bytes()\n"
        "except PermissionError:\n pass\n"
        "else:\n raise SystemExit('private state read was not denied')\n"
        f"p=Path({str(work / 'probe.txt')!r}); p.write_text('probe'); p.unlink()\n"
        f"p=Path({str(state.parent / 'forbidden-probe.txt')!r})\n"
        "try:\n p.write_text('probe')\n"
        "except PermissionError:\n pass\n"
        "else:\n p.unlink(); raise SystemExit('outside write was not denied')\n")
    boundary = native_sandbox([sys.executable, "-B", "-c", probe], work, state,
                              binary=binary, readonly=False)
    if boundary["exit_code"] != 0:
        return {"status": "blocked", "reason": "Host isolation probe failed", "boundary": boundary}
    version = capture([binary, "--version"], cwd=work, timeout=10, env=environment)
    help_result = capture([binary, "exec", "--help"], cwd=work, timeout=10, env=environment)
    flags = ("--ignore-user-config", "--json", "--strict-config")
    compatible = version["exit_code"] == 0 and help_result["exit_code"] == 0
    compatible = compatible and all(flag in help_result["stdout"] for flag in flags)
    return {"status": "ready_for_probe" if compatible else "blocked",
            "reason": "Model startup and catalog isolation still require evidence",
            "binary": binary, "version": version, "help": help_result, "boundary": boundary}


def model_command(binary: str, work: Path, state: Path,
                  model: str | None, effort: str | None) -> list[str]:
    return [binary, "--no-daemon", "--strict-config", "exec", "--ignore-user-config",
            "--json", "--skip-git-repo-check", "-C", str(work),
            *runtime_settings(work, state, model=model, effort=effort)]


def audit_context(binary: str, work: Path, state: Path, prompt: str,
                  variant: str, model: str | None, effort: str | None) -> dict:
    command = [binary, "--no-daemon", "-C", str(work),
               *runtime_settings(work, state, model=model, effort=effort),
               "debug", "prompt-input", prompt]
    result = capture(command, cwd=work, timeout=30, env=runtime_environment(state))
    try:
        messages = json.loads(result["stdout"])
        if not isinstance(messages, list) or not messages or not all(
            isinstance(message, dict) and message.get("type") == "message"
            and message.get("role") in {"system", "developer", "user"}
            and isinstance(message.get("content"), list) and message["content"]
            and all(isinstance(part, dict) and isinstance(part.get("text"), str)
                    for part in message["content"])
            for message in messages
        ):
            raise ValueError("Missing prompt messages")
    except ValueError:
        return {"verified": False, "reason": "No inspectable context", "process": result}
    serialized = result["stdout"].lower()
    names = [name for name in ("rung-get-set", "rung-go", "craftflow") if name in serialized]
    expected = [] if variant == "control" else [name for name in ("rung-get-set", "rung-go")
                                               if (work / ".agents/skills" / name).is_dir()]
    return {"verified": result["exit_code"] == 0 and names == expected,
            "rung_names": names, "prompt_sha256": digest(result["stdout"].encode()),
            "process": result,
            "limit": "Pre-turn context snapshot; not an implicit discovery benchmark"}


def parse_events(text: str) -> dict:
    events = []
    malformed = False
    for line in text.splitlines():
        try:
            event = json.loads(line)
            if not isinstance(event, dict):
                raise ValueError("Expected an event object")
            events.append(event)
        except ValueError:
            malformed = True
    responses = [e["item"].get("text", "") for e in events
                 if e.get("type") == "item.completed"
                 and isinstance(e.get("item"), dict)
                 and e["item"].get("type") == "agent_message"]
    completed = [e for e in events if e.get("type") == "turn.completed"]
    return {"malformed": malformed, "completed": bool(completed),
            "thread_ids": list(dict.fromkeys(e["thread_id"] for e in events
                               if e.get("type") == "thread.started"
                               and isinstance(e.get("thread_id"), str))),
            "response": "\n".join(responses),
            "usage": completed[-1].get("usage") if completed else None,
            "observed_model": None, "observed_effort": None,
            "resource_reads": None, "catalog_verified": False}


def collect_trace(state: Path, thread_ids: list[str]) -> dict:
    """Retain only tool evidence and settings from this attempt's owned session."""
    result = {"status": "missing", "sources": [], "settings": [], "tools": [],
              "reasoning_retained": False}
    if len(thread_ids) != 1:
        return result
    sessions = state / "codex/sessions"
    if not sessions.exists():
        return result
    try:
        contained(state, "codex/sessions")
        for path in sorted(sessions.rglob("*.jsonl")):
            contained(sessions, path.relative_to(sessions).as_posix())
            raw = path.read_bytes()
            lines = raw.decode().splitlines()
            if not lines:
                continue
            header = json.loads(lines[0])
            if (not isinstance(header, dict) or header.get("type") != "session_meta"
                    or not isinstance(header.get("payload"), dict)
                    or header["payload"].get("id") != thread_ids[0]):
                continue
            result["sources"].append({"name": path.name, "sha256": digest(raw)})
            for line in lines[1:]:
                event = json.loads(line)
                if not isinstance(event, dict) or not isinstance(event.get("payload"), dict):
                    raise ValueError("Malformed owned session event")
                payload = event["payload"]
                if event.get("type") == "turn_context":
                    settings = {key: payload.get(key) for key in ("model", "effort")}
                    if not all(isinstance(value, str) and value for value in settings.values()):
                        raise ValueError("Missing observed model settings")
                    if settings not in result["settings"]:
                        result["settings"].append(settings)
                fields = {
                    "function_call": ("type", "name", "call_id", "arguments"),
                    "function_call_output": ("type", "call_id", "output"),
                    "custom_tool_call": ("type", "name", "call_id", "input"),
                    "custom_tool_call_output": ("type", "call_id", "output"),
                }.get(payload.get("type"))
                if event.get("type") == "response_item" and fields:
                    result["tools"].append({key: payload.get(key) for key in fields})
        if len(result["sources"]) == 1 and result["settings"]:
            result["status"] = "captured"
        elif result["sources"]:
            result["status"] = "incomplete"
    except (OSError, ValueError) as exc:
        result["status"] = "incomplete"
        result["error"] = str(exc)
    return result


def check_artifacts(case_id: str, work: Path, before: dict, state: Path,
                    *, behavior: bool = True, binary: str | None = None) -> dict:
    case = load_case(case_id)
    try:
        after = inventory(work)
        scope = after.keys() == before["files"].keys() and all(
            name in case["editable"] or value == after[name]
            for name, value in before["files"].items())
        config_path = work / ".git/config"
        config_hash = digest(config_path.read_bytes()) if config_path.exists() else None
        if config_hash != before["git_config"]:
            return {"scope": False, "behavior": None, "error": "Git configuration changed"}
        observed_git = git_state(work)
        git_preserved = observed_git == before["git"]
    except (ValueError, OSError, subprocess.SubprocessError) as exc:
        return {"scope": False, "behavior": None, "error": str(exc)}
    if not scope or not git_preserved:
        return {"scope": False, "git_preserved": git_preserved, "behavior": None}
    if not behavior:
        return {"scope": True, "git_preserved": True, "git_state": observed_git, "behavior": None}
    spec = importlib.util.spec_from_file_location("rung_pilot_checks", SUITE / "checks.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    def execute(command: list[str]) -> dict:
        if case_id in {"interrupted-effect", "verification-repair"}:
            # These checks need disposable data writes. Isolate them from the
            # assessed artifact, and preserve the original read-only evidence.
            with tempfile.TemporaryDirectory(prefix="rung-check-artifact-") as temporary:
                copy = Path(temporary).resolve() / "work"
                shutil.copytree(work, copy, ignore=shutil.ignore_patterns(".git", ".agents"))
                (copy / ".tmp").mkdir()
                return native_sandbox(["/usr/bin/env", f"TMPDIR={copy / '.tmp'}", *command],
                                      copy, state, binary=binary, readonly=False)
        return native_sandbox(command, work, state, binary=binary, readonly=True)

    behavior = module.check(case.get("checker", case_id), work, execute)
    if inventory(work) != after:
        return {"scope": False, "behavior": behavior, "error": "Checker changed artifacts"}
    return {"scope": True, "git_preserved": True, "git_state": observed_git, "behavior": behavior,
            "manual_criteria": case["manual_criteria"]}


def classify(process: dict, events: dict, checks: dict | None) -> str:
    if checks and (checks.get("scope") is False or (checks.get("behavior") or {}).get("passed") is False):
        return "failed"
    if process.get("interrupted"):
        return "inconclusive"
    if process["exit_code"] is None or (not events["response"] and process["exit_code"] != 0):
        return "blocked"
    if process["timed_out"] or process["exit_code"] != 0 or events["malformed"]:
        return "inconclusive"
    if process["cleanup"] != "process_group_exited" or not events["completed"] or not events["response"] or not checks:
        return "inconclusive"
    if not checks.get("behavior") or checks["behavior"].get("passed") is not True:
        return "inconclusive"
    if checks.get("manual_criteria") or not events["catalog_verified"]:
        return "inconclusive"
    return "passed"


def run_attempt(case_id: str, variant: str, output: Path, timeout: float,
                model: str | None = None, effort: str | None = None,
                binary: str | None = None) -> dict:
    case = load_case(case_id)
    if variant not in {"control", "rung"}:
        raise ValueError("Unknown variant")
    output.mkdir(parents=True, exist_ok=False)
    scratch = Path(tempfile.mkdtemp(prefix="rung-eval-")).resolve()
    remove_scratch = True
    try:
        work, state = scratch / "work", scratch / "state"
        state.mkdir()
        (state / "tmp").mkdir()
        before = prepare(case, work, variant)
        record = {"schema_version": SCHEMA, "attempt_id": str(uuid.uuid4()), "case": case_id, "variant": variant,
                  "suite_files": inventory(SUITE), "runner_sha256": digest(Path(__file__).read_bytes()),
                  "source_revision": git(ROOT, "rev-parse", "HEAD").strip(),
                  "before": before, "host": {"os": platform.platform(), "python": sys.version},
                  "requested_model": model, "requested_effort": effort,
                  "isolation": "codex-native",
                  "cost": None, "outcome": "blocked", "model_attempted": False}
        readiness = preflight(work, state, binary)
        record["preflight"] = readiness
        if readiness["status"] == "ready_for_probe":
            task = (work / "TASK.md").read_text()
            wrapper = f"Use ${case['skill']} for the following task.\n\n" if variant == "rung" else ""
            record["task"] = task
            record["wrapper"] = wrapper
            command = model_command(readiness["binary"], work, state, model, effort)
            try:
                with native_auth(state):
                    audit = audit_context(readiness["binary"], work, state, wrapper + task, variant, model, effort)
                    record["context_audit"] = audit
                    if audit["verified"]:
                        remove_scratch = False
                        process = capture(command, cwd=work, timeout=timeout, prompt=wrapper + task,
                                          env=runtime_environment(state))
                        remove_scratch = process["cleanup"] in {"process_group_exited", "not_started"}
                        record["model_attempted"] = True
                        record["process"] = process
                        events = parse_events(process["stdout"])
                        trace = collect_trace(state, events["thread_ids"])
                        record["trace"] = trace
                        if trace["status"] == "captured" and len(trace["settings"]) == 1:
                            events["observed_model"] = trace["settings"][0]["model"]
                            events["observed_effort"] = trace["settings"][0]["effort"]
                        events["catalog_verified"] = True
                        record["events"] = events
                        checks = check_artifacts(case_id, work, before, state, behavior=bool(events["response"]),
                                                 binary=readiness["binary"]) if remove_scratch else None
                        record["checks"] = checks
                        record["outcome"] = classify(process, events, checks)
            except (OSError, ValueError) as exc:
                record["runtime_error"] = str(exc)
                record["outcome"] = "inconclusive" if record["model_attempted"] else "blocked"
        try:
            record["after"] = inventory(work)
            if remove_scratch:
                shutil.copytree(work, output / "artifacts", ignore=shutil.ignore_patterns(".git", "__pycache__"))
            else:
                record["retained_workspace"] = str(work)
                record["outcome"] = "inconclusive"
        except ValueError as exc:
            record["artifact_error"] = str(exc)
            record["outcome"] = "failed"
        write_json(output / "record.json", record)
    finally:
        if remove_scratch:
            shutil.rmtree(scratch)
    return record


def report(paths: list[Path]) -> dict:
    if len({path.resolve() for path in paths}) != len(paths):
        raise ValueError("Duplicate attempt record")
    records = [json.loads(path.read_text()) for path in paths]
    identifiers = set()
    for record in records:
        if not isinstance(record, dict) or record.get("schema_version") != SCHEMA or record.get("outcome") not in OUTCOMES:
            raise ValueError("Unsupported or malformed attempt record")
        identifier = record.get("attempt_id")
        if not isinstance(identifier, str) or not identifier or identifier in identifiers:
            raise ValueError("Missing or duplicate attempt identity")
        identifiers.add(identifier)
    counts = Counter(record["outcome"] for record in records)
    return {"attempts": len(records), "outcomes": {key: counts[key] for key in sorted(OUTCOMES)},
            "model_attempts": sum(record.get("model_attempted", False) for record in records),
            "comparative_conclusion": None, "cost_per_successful_task": None,
            "limit": "Counts only; settings, assertions, and catalog evidence need assessment"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    pre = commands.add_parser("preflight", help="Inspect runtime and isolation without a model call")
    pre.add_argument("--out", required=True, type=Path)
    pre.add_argument("--codex", help="Codex executable to verify")
    run = commands.add_parser("run", help="Make one bounded attempt; no automatic retries")
    run.add_argument("--case", required=True)
    run.add_argument("--variant", choices=("control", "rung"), required=True)
    run.add_argument("--out", required=True, type=Path)
    run.add_argument("--timeout", type=float, default=120)
    run.add_argument("--model")
    run.add_argument("--effort")
    run.add_argument("--codex", help="Codex executable to use for every phase")
    check = commands.add_parser("check", help="Reassess existing artifacts without model execution")
    check.add_argument("--record", required=True, type=Path)
    check.add_argument("--workspace", required=True, type=Path,
                       help="Original workspace, including Git state for review cases")
    summary = commands.add_parser("report", help="Count recorded outcomes without claiming improvement")
    summary.add_argument("records", nargs="+", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "preflight":
            args.out.mkdir(parents=True, exist_ok=False)
            with tempfile.TemporaryDirectory(prefix="rung-preflight-") as scratch:
                work, state = Path(scratch).resolve() / "work", Path(scratch).resolve() / "state"
                work.mkdir(); state.mkdir()
                value = preflight(work, state, args.codex)
            write_json(args.out / "preflight.json", value)
            print(json.dumps(value, indent=2))
            return 0 if value["status"] == "ready_for_probe" else 2
        if args.command == "run":
            if not 0 < args.timeout <= 600:
                raise ValueError("Timeout must be greater than zero and at most 600 seconds")
            value = run_attempt(args.case, args.variant, args.out, args.timeout, args.model, args.effort, args.codex)
            print(json.dumps({"record": str(args.out / "record.json"), "outcome": value["outcome"]}))
            return 0 if value["outcome"] == "passed" else 2
        if args.command == "check":
            previous = json.loads(args.record.read_text())
            if previous.get("schema_version") != SCHEMA:
                raise ValueError("Unsupported attempt schema")
            if previous["before"]["git"] is not None and not (args.workspace / ".git").is_dir():
                raise ValueError("Review reassessment requires original Git state; saved artifacts contain files only")
            with tempfile.TemporaryDirectory(prefix="rung-check-") as state:
                value = check_artifacts(previous["case"], args.workspace.resolve(), previous["before"], Path(state),
                                        binary=previous.get("preflight", {}).get("binary"))
            print(json.dumps(value, indent=2))
            return 0 if value.get("scope") and (value.get("behavior") or {}).get("passed") is True else 2
        print(json.dumps(report(args.records), indent=2))
        return 0
    except (OSError, ValueError, KeyError, subprocess.SubprocessError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

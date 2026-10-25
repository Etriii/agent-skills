#!/usr/bin/env python3
"""Manage stable QA finding IDs and version snapshots in a reviewed project."""

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path


ACTIVE = {"open", "blocked", "pending"}
STATUSES = ACTIVE | {"resolved", "rejected", "removed"}
STAGES = {"initialized", "auditing", "planned", "awaiting_client", "implementing", "complete"}
ID_PATTERN = re.compile(r"^(?:F|G|D|A|S|P|IDEA)-\d{2,}$")


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def run_git(project, *args):
    return subprocess.run(["git", "-C", str(project), *args], capture_output=True, text=True)


def require_local_path(path):
    """Reject symlinks and directory junctions before reading or writing QA state."""
    if path.resolve() != path.absolute():
        raise ValueError(f"Refusing to use a linked QA path: {path}")


def atomic_json(path, value):
    require_local_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", newline="\n", dir=path.parent,
                                     prefix=".qa-state-", suffix=".tmp", delete=False) as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write("\n")
        temp = Path(stream.name)
    try:
        for attempt in range(5):
            try:
                os.replace(temp, path)
                break
            except PermissionError:
                if attempt == 4:
                    raise
                time.sleep(0.05 * (attempt + 1))
    finally:
        temp.unlink(missing_ok=True)


def load(path):
    require_local_path(path)
    with path.open(encoding="utf-8") as stream:
        return json.load(stream)


def ensure_gitignore(project):
    tracked = run_git(project, "ls-files", "--cached", "--", "qa-findings")
    if tracked.returncode or tracked.stdout.strip():
        raise ValueError("qa-findings/ is already tracked; untrack it before initialization")
    ignore = project / ".gitignore"
    if ignore.is_symlink():
        raise ValueError("Refusing to edit a symlinked .gitignore")
    current = ignore.read_text(encoding="utf-8") if ignore.exists() else ""
    if not current.endswith("\n") and current:
        current += "\n"
    patterns = {line.strip() for line in current.splitlines() if not line.lstrip().startswith("#")}
    if not patterns.intersection({"qa-findings", "qa-findings/", "/qa-findings/"}):
        ignore.write_text(current + "qa-findings/\n", encoding="utf-8", newline="\n")
    verified = run_git(project, "check-ignore", "-q", "qa-findings/.qa-ignore-probe")
    if verified.returncode:
        raise ValueError("Git did not confirm qa-findings/ is ignored")


def project_paths(args):
    project = Path(args.project).expanduser().resolve()
    if not project.is_dir():
        raise ValueError(f"Project directory does not exist: {project}")
    root = run_git(project, "rev-parse", "--show-toplevel")
    if root.returncode != 0:
        raise ValueError("Project must be a Git repository so qa-findings/ can be verified as ignored")
    if Path(root.stdout.strip()).resolve() != project:
        raise ValueError("--project must be the Git repository root")
    findings = project / "qa-findings"
    require_local_path(findings)
    return project, findings


def init(args):
    project, findings = project_paths(args)
    if (findings / "state.json").exists():
        raise ValueError("QA state already exists; use status or next-version")
    if findings.exists() and any(findings.iterdir()):
        raise ValueError("Existing qa-findings/ needs manual reconciliation before initialization")
    ensure_gitignore(project)
    stamp = now()
    current = {"schema_version": 1, "current_version": 1, "created_at": stamp,
               "updated_at": stamp}
    version = {"schema_version": 1, "version": 1, "created_at": stamp,
               "source_version": None, "stage": "initialized", "findings": {}}
    atomic_json(findings / "v1" / "state.json", version)
    atomic_json(findings / "state.json", current)
    print("Initialized qa-findings/v1; Git ignore verified")


def states(findings):
    global_state = load(findings / "state.json")
    number = global_state["current_version"]
    if type(number) is not int or number < 1:
        raise ValueError("current_version must be a positive integer")
    version = load(findings / f"v{number}" / "state.json")
    if type(version["version"]) is not int or version["version"] != number:
        raise ValueError("Version state does not match current_version; reconcile state before retrying")
    return global_state, version


def all_ids(findings):
    result = set()
    for path in findings.glob("v*/state.json"):
        result.update(load(path)["findings"])
    return result


def add(args):
    _, findings = project_paths(args)
    global_state, version = states(findings)
    if not ID_PATTERN.fullmatch(args.id):
        raise ValueError("ID must be a stable QA reference such as F-001, G-001, or A-001")
    if args.id in all_ids(findings):
        raise ValueError(f"Finding ID already exists: {args.id}; use set-status for existing IDs")
    version["findings"][args.id] = {"title": args.title, "status": "open",
                                    "evidence": args.evidence, "created_at": now(),
                                    "updated_at": now(), "origin_version": version["version"]}
    atomic_json(findings / f'v{global_state["current_version"]}' / "state.json", version)
    print(f"Added {args.id}")


def set_status(args):
    _, findings = project_paths(args)
    global_state, version = states(findings)
    item = version["findings"].get(args.id)
    if item is None:
        raise ValueError(f"Finding ID not active in current version: {args.id}")
    if args.status in {"resolved", "rejected", "removed"} and not args.evidence:
        raise ValueError(f"{args.status} requires evidence or a recorded decision")
    item.update(status=args.status, evidence=args.evidence or item.get("evidence", ""),
                updated_at=now())
    atomic_json(findings / f'v{global_state["current_version"]}' / "state.json", version)
    print(f"{args.id}: {args.status}")


def set_stage(args):
    _, findings = project_paths(args)
    global_state, version = states(findings)
    version["stage"] = args.stage
    version["updated_at"] = now()
    atomic_json(findings / f'v{global_state["current_version"]}' / "state.json", version)
    print(f"v{global_state['current_version']}: {args.stage}")


def reopen(args):
    _, findings = project_paths(args)
    global_state, version = states(findings)
    if args.id in version["findings"]:
        raise ValueError(f"{args.id} is already present in the current version")
    historical = None
    for number in range(global_state["current_version"] - 1, 0, -1):
        historical = load(findings / f"v{number}" / "state.json")["findings"].get(args.id)
        if historical:
            break
    if historical is None or historical["status"] not in {"resolved", "rejected", "removed"}:
        raise ValueError("Only a previously closed finding may be reopened")
    version["findings"][args.id] = {**historical, "status": "open", "evidence": args.evidence,
                                    "reopened_from": f"v{number}", "updated_at": now()}
    atomic_json(findings / f'v{global_state["current_version"]}' / "state.json", version)
    print(f"Reopened {args.id} in v{global_state['current_version']}")


def next_version(args):
    _, findings = project_paths(args)
    global_state, previous = states(findings)
    number = global_state["current_version"] + 1
    target = findings / f"v{number}" / "state.json"
    if target.exists():
        raise ValueError(f"v{number} already exists; reconcile state before retrying")
    stamp = now()
    carried = {}
    for key, item in previous["findings"].items():
        if item["status"] in ACTIVE:
            carried[key] = {**item, "carried_from": previous["version"], "updated_at": stamp}
    new = {"schema_version": 1, "version": number, "created_at": stamp,
           "source_version": previous["version"], "stage": "initialized", "findings": carried}
    atomic_json(target, new)
    global_state.update(current_version=number, updated_at=stamp)
    atomic_json(findings / "state.json", global_state)
    print(f"Opened v{number}; carried {len(carried)} unresolved findings")


def status(args):
    _, findings = project_paths(args)
    global_state, version = states(findings)
    counts = {key: 0 for key in sorted(STATUSES)}
    for item in version["findings"].values():
        counts[item["status"]] += 1
    print(json.dumps({"version": f'v{global_state["current_version"]}',
                      "stage": version.get("stage", "unknown"), "counts": counts,
                      "active_ids": sorted(key for key, item in version["findings"].items()
                                           if item["status"] in ACTIVE)}, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for name, action in (("init", init), ("add", add), ("set-status", set_status),
                         ("set-stage", set_stage), ("reopen", reopen),
                         ("next-version", next_version), ("status", status)):
        command = sub.add_parser(name)
        command.add_argument("--project", required=True)
        if name == "add":
            command.add_argument("--id", required=True)
            command.add_argument("--title", required=True)
            command.add_argument("--evidence", default="")
        if name == "set-status":
            command.add_argument("--id", required=True)
            command.add_argument("--status", required=True, choices=sorted(STATUSES))
            command.add_argument("--evidence", default="")
        if name == "reopen":
            command.add_argument("--id", required=True)
            command.add_argument("--evidence", required=True)
        if name == "set-stage":
            command.add_argument("--stage", required=True, choices=sorted(STAGES))
        command.set_defaults(action=action)
    args = parser.parse_args()
    try:
        args.action(args)
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as error:
        print(f"QA state error: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())

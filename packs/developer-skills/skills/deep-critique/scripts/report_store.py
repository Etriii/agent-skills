"""Store categorized critique runs and immutable Markdown reports."""

import argparse
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import re
import sys
import uuid

from storage_io import (MARKER, OUTPUT, artifact_file, check_container, check_untracked, ensure_ignored,
                        json_bytes, local_path, project_root, publish_new, read_json,
                        regular_file, source_context, store_lock)


MODE_ORDER = ("full", "review", "roast", "question", "rate", "compare")
RUN_ID = re.compile(r"\d{8}T\d{6}Z-[0-9a-f]{12}")


def normalize_modes(modes):
    names = set(modes or ("full",))
    unknown = names - set(MODE_ORDER) - {"help"}
    if unknown:
        raise ValueError("Unknown modes: " + ", ".join(sorted(unknown)))
    if "help" in names:
        return ("help",)
    if "full" in names:
        names -= {"review", "rate"}
    return tuple(mode for mode in MODE_ORDER if mode in names)


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def new_run_id():
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ-") + uuid.uuid4().hex[:12]


def start(directory, modes, subject):
    modes = normalize_modes(modes)
    if modes == ("help",):
        raise ValueError("Help does not create a report run")
    if not subject.strip():
        raise ValueError("Establish a subject before creating a report run")
    root, is_git = project_root(directory)
    output = local_path(root / OUTPUT)
    check_untracked(root, is_git)
    check_container(output, wait_for_writer=True)
    regular_file(root / ".gitignore")
    context = source_context(root, is_git)
    output.mkdir(exist_ok=True)
    with store_lock(output):
        check_container(output)
        check_untracked(root, is_git)
        marker = output / ".store.json"
        if marker.exists():
            artifact_file(marker)
        ignored = ensure_ignored(root, is_git)
        if not marker.exists():
            publish_new(marker, json_bytes(MARKER))
        category = "+".join(modes)
        parent = local_path(output / category)
        parent.mkdir(exist_ok=True)
        for _ in range(10):
            run = local_path(parent / new_run_id())
            try:
                run.mkdir()
                break
            except FileExistsError:
                continue
        else:
            raise ValueError("Could not reserve a unique run directory")
        metadata = {"schema_version": 1, "run_id": run.name, "category": category,
                    "modes": list(modes), "subject": subject, "created_at": now(),
                    "root": str(root), "source": context, "ignore_verified": ignored}
        publish_new(run / "run.json", json_bytes(metadata))
    return {"root": str(root), "run": run.relative_to(output).as_posix(),
            "path": str(run), "status": "in-progress"}


def run_paths(directory, relative):
    root, is_git = project_root(directory)
    parts = relative.split("/")
    if len(parts) != 2 or not RUN_ID.fullmatch(parts[1]):
        raise ValueError("Run must be a category/run-id returned by start")
    modes = normalize_modes(parts[0].split("+"))
    if modes == ("help",) or "+".join(modes) != parts[0]:
        raise ValueError("Run category is not canonical")
    output = local_path(root / OUTPUT)
    run = local_path(output / parts[0] / parts[1])
    check_container(output)
    if not (output / ".store.json").is_file() or not run.is_dir():
        raise ValueError("Report run does not exist in an owned store")
    return root, is_git, output, run


def validate_run(root, run):
    metadata = read_json(run / "run.json")
    if (metadata.get("schema_version") != 1 or metadata.get("root") != str(root)
            or metadata.get("run_id") != run.name or metadata.get("category") != run.parent.name
            or metadata.get("modes") != list(normalize_modes(run.parent.name.split("+")))):
        raise ValueError("Run metadata does not match its location")
    return metadata


def append(directory, relative, text):
    """Keep each question/answer turn separate so interrupted sessions remain readable."""
    if not text.strip():
        raise ValueError("Transcript entry is empty")
    root, is_git, output, run = run_paths(directory, relative)
    with store_lock(output):
        check_container(output)
        check_untracked(root, is_git)
        artifact_file(output / ".store.json")
        ensure_ignored(root, is_git)
        metadata = validate_run(root, run)
        if "question" not in metadata["modes"]:
            raise ValueError("Transcript entries require question mode")
        if (run / "completion.json").exists() or (run / "report.md").exists():
            raise ValueError("A finalized report cannot accept transcript entries")
        turns = local_path(run / "turns")
        turns.mkdir(exist_ok=True)
        # The store lock serializes sequence allocation across cooperating writers.
        number = len(list(turns.glob("*.md"))) + 1
        target = local_path(turns / f"{number:06d}-{uuid.uuid4().hex[:12]}.md")
        publish_new(target, (text.rstrip() + "\n").encode("utf-8"))
    return {"path": str(target), "status": "in-progress"}


def finish(directory, relative, text, status="complete"):
    """Publish a final report once; retry the same content to finish an interrupted commit."""
    if status not in {"complete", "incomplete"} or not text.strip():
        raise ValueError("A nonempty report and complete/incomplete status are required")
    root, is_git, output, run = run_paths(directory, relative)
    with store_lock(output):
        check_container(output)
        check_untracked(root, is_git)
        artifact_file(output / ".store.json")
        ensure_ignored(root, is_git)
        metadata = validate_run(root, run)
        provenance = {**metadata, "status": status}
        header = json_bytes(provenance).decode("utf-8").replace("`", "\\u0060")
        report = "# Deep Critique\n\n```json\n" + header + "```\n\n" + text.rstrip() + "\n"
        turns = local_path(run / "turns")
        if turns.exists():
            report += "\n## Question transcript\n"
            for path in sorted(turns.glob("*.md")):
                report += "\n" + artifact_file(path).read_text(encoding="utf-8").rstrip() + "\n"
        data = report.encode("utf-8")
        target = artifact_file(run / "report.md")
        if target.exists():
            if target.read_bytes() != data:
                raise ValueError("Report already exists with different content; start a new run")
        else:
            publish_new(target, data)
        checksum = sha256(data).hexdigest()
        completion = run / "completion.json"
        if completion.exists():
            previous = read_json(completion)
            if previous.get("report_sha256") != checksum or previous.get("status") != status:
                raise ValueError("Completion record does not match the report")
        else:
            publish_new(completion, json_bytes({"status": status, "finished_at": now(),
                                               "report_sha256": checksum}))
    return {"path": str(target), "status": status, "report_sha256": checksum}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="action", required=True)
    command = commands.add_parser("normalize", help="Canonicalize explicit modes without writing files")
    command.add_argument("modes", nargs="*")
    command = commands.add_parser("start", help="Reserve a run and prepare ignore rules")
    command.add_argument("--root", required=True)
    command.add_argument("--modes", nargs="*", default=[])
    command.add_argument("--subject", required=True)
    for action in ("append", "finish"):
        command = commands.add_parser(action)
        command.add_argument("--root", required=True)
        command.add_argument("--run", required=True)
        command.add_argument("--input", required=True, type=Path, help="UTF-8 Markdown file")
        if action == "finish":
            command.add_argument("--status", choices=("complete", "incomplete"), default="complete")
    args = parser.parse_args(argv)
    try:
        if args.action == "normalize":
            result = {"modes": normalize_modes(args.modes)}
        elif args.action == "start":
            result = start(args.root, args.modes, args.subject)
        else:
            text = args.input.read_text(encoding="utf-8")
            if args.action == "append":
                result = append(args.root, args.run, text)
            else:
                result = finish(args.root, args.run, text, args.status)
        print(json.dumps(result))
        return 0
    except (OSError, ValueError, KeyError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

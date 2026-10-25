#!/usr/bin/env python3
"""Report whether a project's Docker QA environment is ready to inspect."""

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


COMPOSE_NAMES = ("compose.yaml", "compose.yml", "docker-compose.yaml", "docker-compose.yml")


def command(args, cwd, timeout=45):
    try:
        result = subprocess.run(args, cwd=cwd, capture_output=True, text=True, timeout=timeout)
    except FileNotFoundError:
        return {"state": "blocked", "detail": f"{args[0]} command unavailable"}
    except subprocess.TimeoutExpired:
        return {"state": "inconclusive", "detail": f"Timed out after {timeout}s; process result unknown"}
    detail = (result.stderr or result.stdout).strip()
    return {"state": "ready" if result.returncode == 0 else "blocked",
            "exit_code": result.returncode, "detail": detail[:500]}


def service_check(project, compose):
    args = ["docker", "compose", "-f", compose, "ps", "--all", "--format", "json"]
    try:
        result = subprocess.run(args, cwd=project, capture_output=True, text=True, timeout=45)
    except subprocess.TimeoutExpired:
        return {"state": "inconclusive", "detail": "Service status timed out; result unknown"}
    if result.returncode:
        return {"state": "blocked", "exit_code": result.returncode,
                "detail": result.stderr.strip()[:500]}
    raw = result.stdout.strip()
    if not raw:
        return {"state": "blocked", "detail": "No Compose services are running"}
    try:
        parsed = json.loads(raw) if raw.startswith("[") else [json.loads(line) for line in raw.splitlines()]
        services = parsed if isinstance(parsed, list) else [parsed]
    except json.JSONDecodeError:
        return {"state": "inconclusive", "detail": "Compose returned an unrecognized service listing"}
    if not services:
        return {"state": "blocked", "detail": "No Compose services are running"}
    summary = [{"name": service.get("Service", service.get("Name", "unknown")),
                "state": service.get("State", "unknown"), "health": service.get("Health", "")}
               for service in services]
    if any(item["state"] != "running" or item["health"] == "unhealthy" for item in summary):
        state = "blocked"
    elif any(item["health"] != "healthy" for item in summary):
        state = "inconclusive"
    else:
        state = "ready"
    return {"state": state, "services": summary,
            "detail": "Health is unverified for services without a healthy status" if state == "inconclusive" else ""}


def preflight(project):
    checks = {}
    checks["docker_cli"] = command(["docker", "--version"], project)
    if checks["docker_cli"]["state"] == "ready":
        checks["docker_daemon"] = command(["docker", "info", "--format", "{{.ServerVersion}}"], project)
        checks["compose"] = command(["docker", "compose", "version"], project)
    compose = next((name for name in COMPOSE_NAMES if (project / name).is_file()), None)
    if compose is None:
        checks["compose_file"] = {"state": "inconclusive", "detail": "No root Compose file found; inspect project documentation"}
    else:
        checks["compose_file"] = {"state": "ready", "detail": compose}
        if checks.get("compose", {}).get("state") == "ready":
            checks["compose_config"] = command(["docker", "compose", "-f", compose,
                                                  "config", "--quiet"], project)
            if checks["compose_config"]["state"] == "ready":
                checks["services"] = service_check(project, compose)
    states = [check["state"] for check in checks.values()]
    overall = "blocked" if "blocked" in states else "inconclusive" if "inconclusive" in states else "ready"
    return {"checked_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "project": str(project), "overall": overall, "checks": checks,
            "note": "Ready means tooling/config commands completed; service, database, and app health require separate checks."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True)
    parser.add_argument("--out")
    args = parser.parse_args()
    project = Path(args.project).resolve()
    if not project.is_dir():
        parser.error("--project must be an existing directory")
    report = preflight(project)
    payload = json.dumps(report, indent=2) + "\n"
    if args.out:
        output = Path(args.out)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(payload, encoding="utf-8", newline="\n")
    print(payload, end="")
    return 0 if report["overall"] == "ready" else 1


if __name__ == "__main__":
    sys.exit(main())

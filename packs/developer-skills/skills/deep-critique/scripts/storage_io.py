"""Protect report paths, coordinate writers, and preserve Git ignore contents."""

from contextlib import contextmanager
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import time
import uuid


OUTPUT = ".deep-critique"
MARKER = {"schema_version": 1, "owner": "deep-critique"}


def local_path(path):
    """Reject linked ancestors before resolving an output path."""
    path = Path(os.path.abspath(path))
    for part in (path, *path.parents):
        try:
            info = part.lstat()
        except FileNotFoundError:
            continue
        if stat.S_ISLNK(info.st_mode) or getattr(info, "st_file_attributes", 0) & 0x400:
            raise ValueError(f"Linked path is not allowed: {part}")
    return path.resolve()


def regular_file(path):
    path = local_path(path)
    if path.exists():
        info = path.stat()
        if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
            raise ValueError(f"Expected an unlinked regular file: {path}")
    return path


def artifact_file(path):
    """Recover only local temporary aliases left after interrupted publication."""
    path = local_path(path)
    if path.exists() and path.stat().st_nlink > 1:
        aliases = []
        for candidate in path.parent.glob(".pending-*"):
            if not re.fullmatch(r"\.pending-[0-9a-f]{32}", candidate.name):
                continue
            try:
                info = candidate.lstat()
            except FileNotFoundError:
                continue
            if stat.S_ISREG(info.st_mode) and os.path.samestat(info, path.stat()):
                aliases.append(candidate)
        count = path.stat().st_nlink
        if count == 1:
            return regular_file(path)
        if count != len(aliases) + 1:
            raise ValueError(f"Artifact has hard links outside its pending publication: {path}")
        for candidate in aliases:
            candidate.unlink(missing_ok=True)
    return regular_file(path)


def git(root, *args):
    try:
        return subprocess.run(["git", "-C", str(root), *args], capture_output=True,
                              text=True, encoding="utf-8", errors="replace")
    except FileNotFoundError:
        return None


def project_root(directory):
    root = local_path(Path(directory).expanduser())
    if not root.is_dir():
        raise ValueError(f"Workspace directory does not exist: {root}")
    result = git(root, "rev-parse", "--show-toplevel")
    if result is not None and result.returncode == 0:
        return local_path(result.stdout.strip()), True
    if any((parent / ".git").exists() for parent in (root, *root.parents)):
        raise ValueError("Cannot establish the Git root; fix Git access before saving")
    return root, False


def source_context(root, is_git):
    if not is_git:
        return {"git": False}
    revision = git(root, "rev-parse", "--verify", "HEAD")
    status = git(root, "status", "--porcelain", "--untracked-files=normal")
    if status is None or status.returncode:
        raise ValueError("Cannot inspect Git working-tree state")
    return {"git": True, "revision": revision.stdout.strip() if revision.returncode == 0 else None,
            "dirty": bool(status.stdout)}


def check_untracked(root, is_git):
    if is_git:
        result = git(root, "ls-files", "--cached", "--", OUTPUT)
        if result is None or result.returncode or result.stdout:
            raise ValueError("Report output is tracked or Git cannot verify it; no files were untracked")


def ensure_ignored(root, is_git):
    """Append one anchored rule without replacing existing bytes or line endings."""
    path = regular_file(root / ".gitignore")
    before = path.read_bytes() if path.exists() else None
    if before and before.startswith((b"\xff\xfe", b"\xfe\xff")):
        raise ValueError("Git ignore file must use a Git-compatible text encoding")
    # A child probe or trailing slash can match a partial ignore with visible exceptions.
    probe = OUTPUT
    result = git(root, "check-ignore", "-q", "--", probe) if is_git else None
    if result is not None and result.returncode not in (0, 1):
        raise ValueError("Git could not check the output ignore rule")
    patterns = [line for line in (before or b"").splitlines() if line and not line.startswith(b"#")]
    # Without Git, a final anchored rule avoids trusting an earlier negated rule.
    covered = result.returncode == 0 if result is not None else (
        bool(patterns) and patterns[-1] == b"/.deep-critique/")
    if not covered:
        newline = b"\r\n" if before and b"\r\n" in before else b"\n"
        addition = (newline if before and not before.endswith(b"\n") else b"")
        addition += b"/.deep-critique/" + newline
        regular_file(path)
        if before is None:
            with path.open("xb") as stream:
                stream.write(addition)
                stream.flush()
                os.fsync(stream.fileno())
        else:
            with path.open("a+b") as stream:
                stream.seek(0)
                if stream.read() != before or not os.path.samestat(os.fstat(stream.fileno()), path.stat()):
                    raise ValueError("Git ignore file changed during preparation; retry after the edit")
                stream.write(addition)
                stream.flush()
                os.fsync(stream.fileno())
    if is_git:
        result = git(root, "check-ignore", "-q", "--", probe)
        if result is None or result.returncode:
            raise ValueError("Git did not confirm that report output is ignored")
    return is_git


def publish_new(path, data):
    """Publish complete bytes atomically without replacing an existing artifact."""
    path = artifact_file(path)
    temp = local_path(path.parent / (".pending-" + uuid.uuid4().hex))
    try:
        with temp.open("xb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.link(temp, path)
    finally:
        temp.unlink(missing_ok=True)


def json_bytes(value):
    return (json.dumps(value, indent=2, ensure_ascii=True) + "\n").encode("utf-8")


def read_json(path):
    return inspect_json(artifact_file(path))


def inspect_json(path):
    """Read ownership metadata without cleaning or changing any filesystem entry."""
    path = local_path(path)
    if not stat.S_ISREG(path.stat().st_mode):
        raise ValueError(f"Expected a regular metadata file: {path}")
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"Metadata must contain an object: {path}")
    return value


@contextmanager
def store_lock(output, timeout=5):
    """Use an OS lock released on process exit; retain the lock file for safe reuse."""
    output = local_path(output)
    lock = regular_file(output / ".lock")
    with lock.open("a+b") as stream:
        deadline = time.monotonic() + timeout
        while True:
            stream.seek(0)
            try:
                if os.name == "nt":
                    import msvcrt
                    msvcrt.locking(stream.fileno(), msvcrt.LK_NBLCK, 1)
                else:
                    import fcntl
                    fcntl.flock(stream.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except OSError:
                if time.monotonic() >= deadline:
                    raise ValueError("Another report writer is active; retry when it finishes")
                time.sleep(0.05)
        try:
            yield
        finally:
            stream.seek(0)
            if os.name == "nt":
                import msvcrt
                msvcrt.locking(stream.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                import fcntl
                fcntl.flock(stream.fileno(), fcntl.LOCK_UN)


def check_container(output, wait_for_writer=False):
    """Refuse to adopt an unrelated folder with the same name."""
    output = local_path(output)
    if not output.exists():
        return
    if not output.is_dir():
        raise ValueError(f"Report output is not a directory: {output}")
    marker = output / ".store.json"
    if marker.exists():
        if inspect_json(marker) != MARKER:
            raise ValueError("Unrecognized report store ownership marker")
    elif any(path.name != ".lock" for path in output.iterdir()):
        # An initializing writer may have a pending marker while holding the existing lock.
        if not wait_for_writer or not regular_file(output / ".lock").is_file():
            raise ValueError("Existing report folder has no ownership marker; reconcile it before saving")

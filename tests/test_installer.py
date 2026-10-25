"""Exercise offline copies, integrity, scope boundaries and interruption recovery."""

from contextlib import redirect_stderr, redirect_stdout
from hashlib import sha256
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import uuid


TOOLS = Path(__file__).resolve().parents[1] / "tools"
ROOT = TOOLS.parent / "packs/developer-skills"
sys.path.insert(0, str(TOOLS))
import catalog
import install_skills
import transaction


NAMES = {
    "plan-review", "blocker-check", "phase-handoff", "completion-check",
    "environment-doctor", "phase-runner", "version-manager", "architecture-review",
    "frontend-review", "backend-review", "database-review", "security-privacy-review",
    "business-rules-review", "delivery-readiness", "critical-review",
}


class CatalogTests(unittest.TestCase):
    def test_all_fifteen_have_valid_identity_and_verified_payload(self):
        self.assertEqual({p.name for p in (ROOT / "skills").iterdir()}, NAMES)
        sources = catalog.bundle(ROOT, sorted(NAMES))
        for name, skill in sources.items():
            with self.subTest(name=name):
                path = skill.path
                metadata = catalog.validate_skill(path)
                self.assertEqual(metadata["skill_id"], name)
                self.assertEqual(metadata["compatible_agents"], ["codex", "claude"])
                self.assertEqual(set(catalog.files_in(path)), {"SKILL.md", "metadata.toml"})
                self.assertEqual(skill.content_sha256, catalog.digest(path))


class InstallerTests(unittest.TestCase):
    def setUp(self):
        # Inherit sandbox ACLs; Python 3.14's private temp ACL excludes restricted tokens.
        self.base = Path(tempfile.gettempdir()) / f"standalone skills {uuid.uuid4().hex}"
        self.base.mkdir()
        self.addCleanup(shutil.rmtree, self.base)
        self.project = self.base / "Application with spaces"
        self.project.mkdir()
        self.keep = self.project / ".gitignore"
        self.keep.write_text("developer-owned\n", encoding="utf-8")

    def run_install(self, *extra, answer="y", root=None):
        args = ["--agent", "codex", "--project", str(root or self.project), "--skills", "blocker-check", *extra]
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()), patch("builtins.input", return_value=answer):
            return install_skills.main(args)

    def snapshot(self):
        return catalog.files_in(self.project)

    def target(self, name="blocker-check", agent=".agents"):
        return self.project / agent / "skills" / name

    def copy_source(self):
        source = self.base / "local bundle"
        shutil.copytree(ROOT / "skills", source / "skills")
        shutil.copy2(ROOT / "SHA256SUMS", source / "SHA256SUMS")
        return source

    def test_one_codex_skill_only_and_idempotent_repeat(self):
        self.assertEqual(self.run_install("--yes"), 0)
        self.assertEqual(set(p.name for p in self.target().parent.iterdir()), {"blocker-check"})
        self.assertEqual(catalog.digest(self.target()), catalog.digest(ROOT / "skills/blocker-check"))
        before = self.snapshot()
        mtime = (self.target() / "SKILL.md").stat().st_mtime_ns
        self.assertEqual(self.run_install("--yes"), 0)
        self.assertEqual(before, self.snapshot())
        self.assertEqual(mtime, (self.target() / "SKILL.md").stat().st_mtime_ns)
        self.assertEqual(self.keep.read_text(), "developer-owned\n")
        self.assertFalse((self.project / ".phasepilot").exists())

    def test_claude_and_both_agents(self):
        self.assertEqual(self.run_install("--agent", "claude", "--yes"), 0)
        self.assertTrue(self.target(agent=".claude").is_dir())
        self.assertFalse(self.target().exists())
        self.assertEqual(self.run_install("--agent", "both", "--yes"), 0)
        self.assertEqual(catalog.digest(self.target()), catalog.digest(self.target(agent=".claude")))

    def test_essential_and_explicit_all_bundle(self):
        for bundle, expected in (("essential", set(catalog.ESSENTIAL)), ("all", NAMES)):
            with self.subTest(bundle=bundle), redirect_stdout(io.StringIO()):
                project = self.base / bundle
                project.mkdir()
                self.assertEqual(install_skills.main(["--agent", "both", "--project", str(project), "--bundle", bundle, "--yes"]), 0)
                for agent in (".agents", ".claude"):
                    self.assertEqual({p.name for p in (project / agent / "skills").iterdir()}, expected)

    def test_dry_run_cancel_and_eof_do_not_write(self):
        before = self.snapshot()
        self.assertEqual(self.run_install("--dry-run"), 0)
        self.assertEqual(self.run_install(answer="n"), 2)
        with patch("builtins.input", side_effect=EOFError), redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            self.assertEqual(install_skills.main(["--agent", "codex", "--project", str(self.project), "--skills", "blocker-check"]), 1)
        self.assertEqual(before, self.snapshot())
        self.assertEqual(list(self.project.iterdir()), [self.keep])

    def test_collision_preserves_custom_body_and_empty_directories(self):
        self.target().mkdir(parents=True)
        (self.target() / "SKILL.md").write_text("custom body")
        (self.target() / "custom-empty").mkdir()
        before = self.snapshot()
        self.assertEqual(self.run_install("--yes"), 1)
        self.assertEqual(before, self.snapshot())
        self.assertTrue((self.target() / "custom-empty").is_dir())

    def test_approved_replacement_retains_exact_backup(self):
        self.target().mkdir(parents=True)
        (self.target() / "SKILL.md").write_text("custom body")
        before = catalog.digest(self.target())
        self.assertEqual(self.run_install("--replace", "--yes"), 0)
        backups = list((self.project / transaction.BACKUPS).glob("*/backups/0"))
        self.assertEqual(len(backups), 1)
        self.assertEqual(catalog.digest(backups[0]), before)
        self.assertEqual(catalog.digest(self.target()), catalog.digest(ROOT / "skills/blocker-check"))

    def test_malicious_selection_and_missing_project_fail_before_writes(self):
        before = self.snapshot()
        for name in ("../escape", "a/b", "a\\b", "C:\\escape", "UPPER", "bad_name", "a--b", "x;echo", "a" * 65):
            with self.subTest(name=name):
                self.assertEqual(self.run_install("--skills", name, "--yes"), 1)
        self.assertEqual(self.run_install(root=self.base / "missing"), 1)
        self.assertFalse((self.base / "missing").exists())
        self.assertEqual(before, self.snapshot())

    def test_relative_sibling_scope_is_normalized_before_overlap_check(self):
        relative = os.path.relpath(self.project, Path.cwd())
        self.assertEqual(self.run_install("--yes", root=Path(relative)), 0)
        self.assertTrue(self.target().is_dir())

    def test_source_tampering_and_manifest_pin_mismatch_preserve_destination(self):
        source = self.copy_source()
        self.assertEqual(self.run_install("--yes"), 0)
        before = self.snapshot()
        self.assertEqual(self.run_install("--source", str(source), "--expected-manifest-sha256", "0" * 64, "--yes"), 1)
        (source / "skills/blocker-check/SKILL.md").write_text("tampered")
        self.assertEqual(self.run_install("--source", str(source), "--replace", "--yes"), 1)
        self.assertEqual(before, self.snapshot())

    def test_valid_manifest_pin_and_no_network_dependency(self):
        source = self.copy_source()
        pin = sha256((source / "SHA256SUMS").read_bytes()).hexdigest()
        with patch("socket.socket", side_effect=AssertionError("Network forbidden")), patch("subprocess.Popen", side_effect=AssertionError("Hooks forbidden")):
            self.assertEqual(self.run_install("--source", str(source), "--expected-manifest-sha256", pin, "--yes"), 0)

    def test_invalid_frontmatter_metadata_and_manifest_fail_before_write(self):
        source = self.copy_source()
        path = source / "skills/blocker-check"
        original = (path / "metadata.toml").read_text()
        for content in (original.replace('name = "blocker-check"', 'name = "other"'), original.replace('schema_version = 1', 'schema_version = 9')):
            (path / "metadata.toml").write_text(content)
            self.assertEqual(self.run_install("--source", str(source), "--yes"), 1)
        (path / "metadata.toml").write_text(original)
        (source / "SHA256SUMS").write_text("0" * 64 + "  skills/blocker-check/../escape\n")
        self.assertEqual(self.run_install("--source", str(source), "--yes"), 1)
        self.assertEqual(list(self.project.iterdir()), [self.keep])

    def test_user_scope_requires_explicit_verified_home_and_uses_runtime_paths(self):
        home = self.base / "runtime home"
        home.mkdir()
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            common = ["--agent", "both", "--scope", "user", "--skills", "blocker-check", "--yes"]
            self.assertEqual(install_skills.main(common), 1)
            self.assertEqual(install_skills.main([*common, "--user-home", str(home)]), 0)
        self.assertTrue((home / ".agents/skills/blocker-check/SKILL.md").is_file())
        self.assertTrue((home / ".claude/skills/blocker-check/SKILL.md").is_file())
        self.assertFalse((home / ".codex").exists())

    def test_interrupted_staging_preserves_old_content_and_leaves_no_transaction(self):
        self.target().mkdir(parents=True)
        (self.target() / "SKILL.md").write_text("old custom")
        before = self.snapshot()
        with patch("transaction.shutil.copytree", side_effect=KeyboardInterrupt):
            self.assertEqual(self.run_install("--replace", "--yes"), 2)
        self.assertEqual(before, self.snapshot())
        self.assertFalse((self.project / transaction.TRANSACTION).exists())

    def test_corrupted_staging_fails_digest_check(self):
        copy = shutil.copytree
        def corrupt(src, dst, *args, **kwargs):
            result = copy(src, dst, *args, **kwargs)
            (Path(dst) / "SKILL.md").write_text("corrupt")
            return result
        with patch("transaction.shutil.copytree", side_effect=corrupt):
            self.assertEqual(self.run_install("--yes"), 1)
        self.assertFalse(self.target().exists())
        self.assertEqual(list(self.project.iterdir()), [self.keep])

    def test_failure_after_first_swap_rolls_back_both_agents(self):
        self.target().mkdir(parents=True)
        (self.target() / "SKILL.md").write_text("old custom")
        before = self.snapshot()
        original = Path.rename
        def fail_second(path, target):
            if path.name == "1" and path.parent.name == "staged":
                raise OSError("injected second-agent failure")
            return original(path, target)
        with patch.object(Path, "rename", fail_second):
            self.assertEqual(self.run_install("--agent", "both", "--replace", "--yes"), 1)
        self.assertEqual(before, self.snapshot())
        self.assertFalse(self.target(agent=".claude").exists())

    def test_rollback_preserves_preexisting_empty_adapter_directories(self):
        self.target().parent.mkdir(parents=True)
        original = Path.rename
        def fail_copy(path, target):
            if path.parent.name == "staged":
                raise OSError("injected swap failure")
            return original(path, target)
        with patch.object(Path, "rename", fail_copy):
            self.assertEqual(self.run_install("--yes"), 1)
        self.assertTrue(self.target().parent.is_dir())
        self.assertEqual(list(self.target().parent.iterdir()), [])

    def test_source_change_after_approval_cannot_bypass_manifest(self):
        source = self.copy_source()
        def approve(_):
            path = source / "skills/blocker-check/SKILL.md"
            path.write_text(path.read_text() + "\nchanged after preview\n")
            return "y"
        with patch("builtins.input", side_effect=approve), redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            self.assertEqual(install_skills.main(["--agent", "codex", "--project", str(self.project), "--source", str(source), "--skills", "blocker-check"]), 1)
        self.assertFalse(self.target().exists())

    def test_committed_install_survives_backup_archival_failure_and_recovers(self):
        self.target().mkdir(parents=True)
        (self.target() / "SKILL.md").write_text("original")
        with patch("transaction.finish", side_effect=OSError("injected archive failure")):
            self.assertEqual(self.run_install("--replace", "--yes"), 1)
        self.assertTrue((self.project / transaction.TRANSACTION).is_dir())
        with redirect_stdout(io.StringIO()):
            self.assertEqual(install_skills.main(["--agent", "codex", "--project", str(self.project), "--recover", "--yes"]), 0)
        self.assertEqual(catalog.digest(self.target()), catalog.digest(ROOT / "skills/blocker-check"))
        self.assertEqual(next((self.project / transaction.BACKUPS).glob("*/backups/0/SKILL.md")).read_text(), "original")

    def test_malicious_recovery_target_cannot_escape_scope(self):
        folder = self.project / transaction.TRANSACTION
        folder.mkdir()
        (folder / "staged").mkdir()
        (folder / "backups").mkdir()
        journal = {"id": "a" * 32, "state": "prepared", "created": [], "entries": [{"target": "../escape", "before": None, "after": "a" * 64}]}
        (folder / "journal.json").write_text(json.dumps(journal))
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            self.assertEqual(install_skills.main(["--agent", "codex", "--project", str(self.project), "--recover", "--yes"]), 1)
        self.assertTrue((folder / "journal.json").exists())

    def test_change_between_preview_and_commit_is_preserved(self):
        def approve(_):
            self.target().mkdir(parents=True)
            (self.target() / "SKILL.md").write_text("arrived after preview")
            return "y"
        with patch("builtins.input", side_effect=approve), redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            result = install_skills.main(["--agent", "codex", "--project", str(self.project), "--skills", "blocker-check"])
        self.assertEqual(result, 1)
        self.assertEqual((self.target() / "SKILL.md").read_text(), "arrived after preview")

    def test_abrupt_process_exit_then_explicit_recovery_restores_custom(self):
        self.target().mkdir(parents=True)
        (self.target() / "SKILL.md").write_text("old custom")
        before = self.snapshot()
        script = """
import os, sys
from pathlib import Path
sys.path.insert(0, sys.argv[1])
from catalog import digest
from transaction import install
source, target, root = map(Path, sys.argv[2:])
rename = Path.rename
def crash(path, destination):
    result = rename(path, destination)
    if path.parent.name == 'staged':
        os._exit(73)
    return result
Path.rename = crash
install(root, [(source, target, digest(target), digest(source))])
"""
        result = subprocess.run([sys.executable, "-c", script, str(TOOLS), str(ROOT / "skills/blocker-check"), str(self.target()), str(self.project)], capture_output=True)
        self.assertEqual(result.returncode, 73, result.stderr)
        self.assertEqual(self.run_install("--yes"), 1)
        with redirect_stdout(io.StringIO()):
            self.assertEqual(install_skills.main(["--agent", "codex", "--project", str(self.project), "--recover", "--dry-run"]), 0)
            self.assertEqual(install_skills.main(["--agent", "codex", "--project", str(self.project), "--recover", "--yes"]), 0)
        self.assertEqual(before, self.snapshot())

    def test_source_or_destination_links_and_windows_junctions_are_rejected(self):
        outside = self.base / "outside"
        outside.mkdir()
        junction = self.project / ".agents"
        if os.name == "nt":
            result = subprocess.run(["cmd", "/c", "mklink", "/J", str(junction), str(outside)], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.addCleanup(lambda: junction.rmdir() if junction.exists() else None)
        else:
            junction.symlink_to(outside, target_is_directory=True)
        self.assertEqual(self.run_install("--yes"), 1)
        self.assertEqual(list(outside.iterdir()), [])
        source = self.copy_source()
        shutil.rmtree(source / "skills/blocker-check")
        if os.name == "nt":
            result = subprocess.run(["cmd", "/c", "mklink", "/J", str(source / "skills/blocker-check"), str(ROOT / "skills/blocker-check")], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.addCleanup(lambda: (source / "skills/blocker-check").rmdir())
        else:
            (source / "skills/blocker-check").symlink_to(ROOT / "skills/blocker-check", target_is_directory=True)
        self.assertEqual(self.run_install("--source", str(source), "--yes"), 1)

    def test_standalone_blocker_and_handoff_from_public_only_archive(self):
        # The isolated bundle has no sibling private repository or runtime package.
        source = self.copy_source()
        shutil.copytree(TOOLS, source / "tools", ignore=shutil.ignore_patterns("__pycache__"))
        result = subprocess.run([sys.executable, str(source / "tools/install_skills.py"), "--agent", "both", "--project", str(self.project), "--skills", "blocker-check", "phase-handoff", "--yes"], cwd=self.base, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        for agent in (".agents", ".claude"):
            for name in ("blocker-check", "phase-handoff"):
                body = (self.target(name, agent) / "SKILL.md").read_text()
                self.assertNotIn(".phasepilot/", body)
                self.assertIn("Input:", body)
                self.assertIn("Output:", body)


if __name__ == "__main__":
    unittest.main()

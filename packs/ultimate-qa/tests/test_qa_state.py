import json
import os
import shutil
import stat
import uuid
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "skills/ultimate-qa/scripts/qa_state.py"


class QAStateTests(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.gettempdir()) / f"ultimate-qa-state-{uuid.uuid4().hex}"
        self.root.mkdir()
        self.addCleanup(shutil.rmtree, self.root, onerror=self.remove_readonly)
        self.project = self.make_project("application with spaces")

    def remove_readonly(self, function, path, error):
        if not Path(path).resolve().is_relative_to(self.root):
            raise ValueError("Test cleanup escaped its fixture root")
        os.chmod(path, stat.S_IWRITE)
        function(path)

    def make_project(self, name):
        project = self.root / name
        project.mkdir()
        subprocess.run(["git", "init", "--quiet", str(project)], check=True)
        return project

    def command(self, command, *args, project=None):
        return subprocess.run([sys.executable, str(SCRIPT), command, "--project",
                               str(project or self.project), *args], capture_output=True, text=True)

    def initialize(self, project=None):
        result = self.command("init", project=project)
        self.assertEqual(result.returncode, 0, result.stderr)

    def link_directory(self, link, target):
        try:
            link.symlink_to(target, target_is_directory=True)
        except OSError:
            if os.name != "nt":
                raise
            subprocess.run(["cmd.exe", "/c", "mklink", "/J", str(link), str(target)],
                           check=True, capture_output=True)

    def test_initialization_stays_in_project_and_is_ignored(self):
        self.initialize()
        state = self.project / "qa-findings/state.json"
        self.assertEqual(json.loads(state.read_text())["current_version"], 1)
        self.assertFalse((self.root / "qa-findings").exists())
        ignored = subprocess.run(["git", "-C", str(self.project), "check-ignore", "-q",
                                  "qa-findings/state.json"])
        self.assertEqual(ignored.returncode, 0)
        before = state.read_bytes()
        self.assertEqual(self.command("init").returncode, 2)
        self.assertEqual(state.read_bytes(), before)

    def test_tracked_output_is_rejected_without_changing_ignore(self):
        findings = self.project / "qa-findings"
        findings.mkdir()
        (findings / "old.md").write_text("private evidence", encoding="utf-8")
        subprocess.run(["git", "-C", str(self.project), "add", "-f", "qa-findings"], check=True)
        self.assertEqual(self.command("init").returncode, 2)
        self.assertFalse((self.project / ".gitignore").exists())

    def test_resumed_mutation_cannot_follow_another_projects_findings(self):
        other = self.make_project("other app")
        self.initialize(other)
        target = other / "qa-findings/v1/state.json"
        before = target.read_bytes()
        self.link_directory(self.project / "qa-findings", other / "qa-findings")
        result = self.command("set-stage", "--stage", "planned")
        self.assertEqual(result.returncode, 2, result.stdout)
        self.assertEqual(target.read_bytes(), before)

    def test_resumed_mutation_rejects_nested_git_directory(self):
        nested = self.project / "frontend"
        nested.mkdir()
        self.initialize()
        self.link_directory(nested / "qa-findings", self.project / "qa-findings")
        result = self.command("set-stage", "--stage", "planned", project=nested)
        self.assertEqual(result.returncode, 2, result.stdout)

    def test_linked_version_directory_cannot_write_outside_project(self):
        self.initialize()
        other = self.make_project("other app")
        self.initialize(other)
        target = other / "qa-findings/v1/state.json"
        before = target.read_bytes()
        original = self.project / "qa-findings/v1"
        original.rename(self.project / "qa-findings/saved-v1")
        self.link_directory(original, other / "qa-findings/v1")
        result = self.command("set-stage", "--stage", "planned")
        self.assertEqual(result.returncode, 2, result.stdout)
        self.assertEqual(target.read_bytes(), before)

    def test_invalid_version_pointer_fails_clearly(self):
        self.initialize()
        state = self.project / "qa-findings/state.json"
        payload = json.loads(state.read_text())
        for invalid in ("../other", True, 0, -1, 1.5):
            with self.subTest(pointer=invalid):
                payload["current_version"] = invalid
                state.write_text(json.dumps(payload), encoding="utf-8")
                result = self.command("status")
                self.assertEqual(result.returncode, 2)
                self.assertIn("current_version must be a positive integer", result.stderr)

    def test_versions_preserve_history_and_carry_only_unresolved_items(self):
        self.initialize()
        for identifier in ("F-001", "F-002"):
            result = self.command("add", "--id", identifier, "--title", "Example issue")
            self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.command("set-status", "--id", "F-001", "--status", "resolved").returncode, 2)
        result = self.command("set-status", "--id", "F-001", "--status", "resolved",
                              "--evidence", "regression test passed")
        self.assertEqual(result.returncode, 0, result.stderr)
        previous = self.project / "qa-findings/v1/state.json"
        before = previous.read_bytes()
        self.assertEqual(self.command("next-version").returncode, 0)
        self.assertEqual(previous.read_bytes(), before)
        status = json.loads(self.command("status").stdout)
        self.assertEqual(status["active_ids"], ["F-002"])
        self.assertEqual(self.command("reopen", "--id", "F-001", "--evidence", "regression reproduced").returncode, 0)
        self.assertEqual(previous.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()

"""Verify the QA pack entry point delegates recorded lifecycle to the collection."""

from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import uuid


PACK = Path(__file__).resolve().parents[1]
SCRIPT = PACK / "tools/install_skills.py"


class PackInstallerTests(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.gettempdir()) / f"qa-pack-install-{uuid.uuid4().hex}"
        self.root.mkdir()
        self.addCleanup(shutil.rmtree, self.root)

    def command(self, *args):
        return subprocess.run([sys.executable, "-B", str(SCRIPT), *map(str, args)], cwd=self.root,
                              capture_output=True, text=True)

    def test_list_has_nine_skills(self):
        result = self.command("--list")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(len(result.stdout.splitlines()), 9)

    def test_preview_install_and_uninstall_recorded_for_both_agents(self):
        args = ("--agent", "both", "--project", self.root, "--skills", "ultimate-qa-client")
        preview = self.command(*args, "--dry-run")
        self.assertEqual(preview.returncode, 0, preview.stderr)
        self.assertEqual(list(self.root.iterdir()), [])
        result = self.command(*args, "--yes")
        self.assertEqual(result.returncode, 0, result.stderr)
        for agent in (".agents", ".claude"):
            marker = self.root / agent / "skills/ultimate-qa-client/kit-location.txt"
            self.assertEqual(Path(marker.read_text().strip()), PACK)
        result = self.command(*args, "--uninstall", "--yes")
        self.assertEqual(result.returncode, 0, result.stderr)
        for agent in (".agents", ".claude"):
            self.assertFalse((self.root / agent / "skills/ultimate-qa-client").exists())
        history = list((self.root / ".agent-skills/history").glob("*/operation.md"))
        self.assertEqual(len(history), 2)
        self.assertTrue(list((self.root / ".skills-install-backups").glob("*/backups/*/SKILL.md")))

    def test_typo_project_is_not_created(self):
        missing = self.root / "missing"
        result = self.command("--agent", "codex", "--project", missing, "--bundle", "all", "--yes")
        self.assertEqual(result.returncode, 1)
        self.assertFalse(missing.exists())


if __name__ == "__main__":
    unittest.main()

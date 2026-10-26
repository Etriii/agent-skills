"""Exercise recorded ownership, safe removals and atomic history with real pack files."""

from contextlib import redirect_stderr, redirect_stdout
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


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import catalog
import install_skills
import records
import transaction


class LifecycleTests(unittest.TestCase):
    def setUp(self):
        self.base = Path(tempfile.gettempdir()) / f"agent skills lifecycle {uuid.uuid4().hex}"
        self.base.mkdir()
        self.addCleanup(shutil.rmtree, self.base)
        self.project = self.base / "Application with spaces"
        self.project.mkdir()
        (self.project / ".gitignore").write_text("existing ignore\n", encoding="utf-8")

    def run_tool(self, *args, pack="developer-skills", agent="codex", names=("blocker-check",), yes=True):
        command = ["--pack", pack, "--agent", agent, "--project", str(self.project)]
        if names is not None:
            command += ["--skills", *names]
        if yes:
            command.append("--yes")
        with redirect_stdout(io.StringIO()) as output, redirect_stderr(io.StringIO()) as errors:
            result = install_skills.main([*command, *args])
        self.last_output, self.last_error = output.getvalue(), errors.getvalue()
        return result

    def target(self, name="blocker-check", agent=".agents"):
        return self.project / agent / "skills" / name

    def history(self):
        return sorted((records.read_record(p) for p in (self.project / records.STATE).glob("history/*/operation.md")),
                      key=lambda event: event["sequence"])

    def snapshot(self):
        return catalog.files_in(self.project)

    def test_both_complete_packs_and_agents_have_real_records_and_qa_kit_markers(self):
        for pack, expected in (("developer-skills", 16), ("ultimate-qa", 9)):
            self.assertEqual(self.run_tool("--bundle", "all", pack=pack, agent="both", names=None), 0, self.last_error)
            event = self.history()[-1]
            self.assertEqual(event["pack"], pack)
            self.assertEqual(len(event["entries"]), expected * 2)
            self.assertRegex(event["manifest_sha256"], r"^[0-9a-f]{64}$")
        for directory in (".agents", ".claude"):
            self.assertEqual(len(list((self.project / directory / "skills").iterdir())), 25)
            for name in ("ultimate-qa", "ultimate-qa-client"):
                kit = (self.target(name, directory) / "kit-location.txt").read_text().strip()
                self.assertEqual(Path(kit), ROOT / "packs/ultimate-qa")
                self.assertTrue((Path(kit) / "02_QA_CHECKLIST.md").is_file())
        owners, sequence = records.inventory(self.project)
        self.assertEqual((len(owners), sequence), (50, 2))

    def test_selective_uninstall_preserves_other_agents_packs_reports_and_backups(self):
        self.assertEqual(self.run_tool(agent="both"), 0)
        self.assertEqual(self.run_tool(pack="ultimate-qa", names=("ultimate-qa",)), 0)
        report = self.project / "qa-findings/v1/report.md"
        report.parent.mkdir(parents=True)
        report.write_text("keep QA evidence\n", encoding="utf-8")
        old = catalog.digest(self.target())
        self.assertEqual(self.run_tool("--uninstall"), 0, self.last_error)
        self.assertFalse(self.target().exists())
        self.assertTrue(self.target(agent=".claude").is_dir())
        self.assertTrue(self.target("ultimate-qa").is_dir())
        self.assertEqual(report.read_text(), "keep QA evidence\n")
        self.assertEqual((self.project / ".gitignore").read_text(), "existing ignore\n")
        event = self.history()[-1]
        self.assertEqual(event["operation"], "uninstall")
        self.assertIsNone(event["source"])
        self.assertEqual(event["entries"][0]["installed_record"], self.history()[0]["id"])
        backup = Path(event["backup"])
        journal = json.loads((backup / "journal.json").read_text())
        self.assertEqual(journal["entries"][0]["target"], ".agents/skills/blocker-check")
        self.assertEqual(catalog.digest(backup / "backups/0"), old)
        self.assertEqual(Path(event["entries"][0]["backup_path"]), backup / "backups/0")
        self.assertNotIn(".agents/skills/blocker-check", records.inventory(self.project)[0])

    def test_repeated_install_uninstall_and_preview_do_not_invent_history(self):
        self.assertEqual(self.run_tool(), 0)
        before = self.snapshot()
        self.assertEqual(self.run_tool(), 0)
        self.assertEqual(self.run_tool("--uninstall", "--dry-run"), 0)
        with patch("builtins.input", return_value="n"):
            self.assertEqual(self.run_tool("--uninstall", yes=False), 2)
        self.assertEqual(self.snapshot(), before)
        self.assertEqual(self.run_tool("--uninstall"), 0)
        after = self.snapshot()
        self.assertEqual(self.run_tool("--uninstall"), 0)
        self.assertEqual(self.snapshot(), after)
        self.assertEqual([event["operation"] for event in self.history()], ["install", "uninstall"])
        self.assertEqual(self.run_tool(), 0)
        self.assertEqual(records.inventory(self.project)[1], 3)

    def test_unmanaged_matching_copy_must_be_adopted_before_removal(self):
        shutil.copytree(ROOT / "packs/developer-skills/skills/blocker-check", self.target())
        before = self.snapshot()
        self.assertEqual(self.run_tool("--uninstall"), 1)
        self.assertEqual(self.snapshot(), before)
        self.assertEqual(self.run_tool(), 0)
        self.assertEqual(self.history()[0]["entries"][0]["action"], "ADOPT MATCHING COPY")
        self.assertEqual(self.run_tool("--uninstall"), 0)
        self.assertFalse(self.target().exists())

    def test_modified_skill_blocks_entire_removal_batch_and_replacement_saves_edits(self):
        names = ("blocker-check", "phase-handoff")
        self.assertEqual(self.run_tool(names=names), 0)
        (self.target("phase-handoff") / "local-notes.md").write_text("keep edits", encoding="utf-8")
        (self.target("phase-handoff") / "empty custom directory").mkdir()
        before = self.snapshot()
        self.assertEqual(self.run_tool("--uninstall", names=names), 1)
        self.assertEqual(self.snapshot(), before)
        self.assertTrue(self.target().is_dir())
        self.assertEqual(self.run_tool("--replace", names=("phase-handoff",)), 0)
        backup = Path(self.history()[-1]["backup"]) / "backups/0"
        self.assertEqual((backup / "local-notes.md").read_text(), "keep edits")
        self.assertTrue((backup / "empty custom directory").is_dir())
        self.assertEqual(self.run_tool("--uninstall", names=names), 0)

    def test_all_uninstall_uses_history_even_without_source_pack(self):
        self.assertEqual(self.run_tool(agent="both"), 0)
        self.assertEqual(self.run_tool(pack="ultimate-qa", names=("ultimate-qa-api",)), 0)
        self.assertEqual(self.run_tool("--uninstall", "--bundle", "all", "--source", str(self.base / "missing pack"),
                                       agent="both", names=None), 0, self.last_error)
        self.assertFalse(self.target().exists())
        self.assertFalse(self.target(agent=".claude").exists())
        self.assertTrue(self.target("ultimate-qa-api").is_dir())

    def test_history_failure_rolls_back_removed_content_and_does_not_publish_success(self):
        self.assertEqual(self.run_tool(agent="both"), 0)
        before = self.snapshot()
        rename = Path.rename
        def fail_record(path, destination):
            if path.parent.name == "staged" and (path / "operation.md").exists():
                raise OSError("injected history publication failure")
            return rename(path, destination)
        with patch.object(Path, "rename", fail_record):
            self.assertEqual(self.run_tool("--uninstall", agent="both"), 1)
        self.assertEqual(self.snapshot(), before)
        self.assertEqual(len(self.history()), 1)
        self.assertFalse((self.project / transaction.TRANSACTION).exists())

    def test_record_preparation_error_prevents_destination_changes(self):
        before = self.snapshot()
        with patch("operations.staged_record", side_effect=PermissionError("record cannot be written")):
            self.assertEqual(self.run_tool(), 1)
        self.assertEqual(self.snapshot(), before)

    def test_incomplete_history_or_broken_ownership_chain_blocks_removal(self):
        self.assertEqual(self.run_tool(), 0)
        path = next((self.project / records.STATE).glob("history/*/operation.md"))
        original = path.read_text()
        for bad in (original.replace('operation: "install"\n', ''),
                    original.replace('"installed_record": null', '"installed_record": "' + 'a' * 32 + '"')):
            path.write_text(bad, encoding="utf-8")
            before = self.snapshot()
            self.assertEqual(self.run_tool("--uninstall"), 1)
            self.assertEqual(self.snapshot(), before)
        path.write_text(original, encoding="utf-8")

    def test_committed_uninstall_archive_failure_can_finish_recovery(self):
        self.assertEqual(self.run_tool(), 0)
        with patch("transaction.finish", side_effect=OSError("archive temporarily unavailable")):
            self.assertEqual(self.run_tool("--uninstall"), 1)
        self.assertFalse(self.target().exists())
        event = self.history()[-1]
        self.assertEqual(event["operation"], "uninstall")
        self.assertEqual(self.run_tool("--recover", names=None), 0, self.last_error)
        self.assertTrue((Path(event["backup"]) / "backups/0/SKILL.md").is_file())
        self.assertEqual(records.inventory(self.project), ({}, 2))

    def test_corrupt_or_racing_history_is_preserved_and_blocks_mutation(self):
        self.assertEqual(self.run_tool(), 0)
        record = next((self.project / records.STATE).glob("history/*/operation.md"))
        original = record.read_text()
        record.write_text(original.replace("sequence: 1", "sequence: 9"), encoding="utf-8")
        before = self.snapshot()
        self.assertEqual(self.run_tool("--uninstall"), 1)
        self.assertEqual(self.snapshot(), before)
        record.write_text(original, encoding="utf-8")
        def approve(_):
            (self.project / records.STATE / "unexpected.md").write_text("arrived after preview", encoding="utf-8")
            return "y"
        with patch("builtins.input", side_effect=approve):
            self.assertEqual(self.run_tool("--uninstall", yes=False), 1)
        self.assertTrue(self.target().is_dir())
        self.assertFalse((self.project / transaction.TRANSACTION).exists())

    def test_qa_support_tampering_fails_before_install(self):
        source = self.base / "QA kit copy"
        shutil.copytree(ROOT / "packs/ultimate-qa", source, ignore=shutil.ignore_patterns("__pycache__"))
        helper = source / "tools/qa_preflight.py"
        helper.write_text(helper.read_text() + "\n# altered\n", encoding="utf-8")
        before = self.snapshot()
        self.assertEqual(self.run_tool("--source", str(source), pack="ultimate-qa", names=("ultimate-qa",)), 1)
        self.assertEqual(self.snapshot(), before)

    def test_abrupt_uninstall_exit_then_recovery_restores_content_and_history(self):
        self.assertEqual(self.run_tool(agent="both"), 0)
        before = self.snapshot()
        script = '''
import os, sys
from pathlib import Path
sys.path.insert(0, sys.argv[1])
import install_skills
rename = Path.rename
def crash(path, target):
    result = rename(path, target)
    if Path(target).parent.name == 'backups':
        os._exit(74)
    return result
Path.rename = crash
raise SystemExit(install_skills.main(['--agent', 'both', '--project', sys.argv[2], '--skills', 'blocker-check', '--uninstall', '--yes']))
'''
        result = subprocess.run([sys.executable, "-B", "-c", script, str(ROOT / "tools"), str(self.project)], capture_output=True)
        self.assertEqual(result.returncode, 74, result.stderr)
        self.assertEqual(self.run_tool(), 1)
        self.assertEqual(self.run_tool("--recover", names=None), 0, self.last_error)
        self.assertEqual(self.snapshot(), before)

    def test_pack_wrappers_use_shared_list_command(self):
        for pack, expected in (("developer-skills", 16), ("ultimate-qa", 9)):
            result = subprocess.run([sys.executable, "-B", str(ROOT / "packs" / pack / "tools/install_skills.py"), "--list"],
                                    cwd=self.base, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(len(result.stdout.splitlines()), expected)

    def test_user_scope_uses_explicit_home_and_records_both_agents(self):
        home = self.base / "runtime home"
        home.mkdir()
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            result = install_skills.main(["--pack", "ultimate-qa", "--agent", "both", "--scope", "user",
                                          "--user-home", str(home), "--skills", "ultimate-qa-client", "--yes"])
        self.assertEqual(result, 0)
        self.assertTrue((home / ".agents/skills/ultimate-qa-client/kit-location.txt").is_file())
        self.assertTrue((home / ".claude/skills/ultimate-qa-client/kit-location.txt").is_file())
        self.assertEqual(records.inventory(home)[1], 1)


if __name__ == "__main__":
    unittest.main()

"""Exercise real report files, Git ignore behavior, concurrency and crash recovery."""

from concurrent.futures import ThreadPoolExecutor
from hashlib import sha256
import json
import os
from pathlib import Path
import shutil
import stat
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import patch
import uuid


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "packs/developer-skills/skills/deep-critique/scripts"
sys.path.insert(0, str(SCRIPTS))
import report_store
import storage_io


class ModeTests(unittest.TestCase):
    def test_defaults_order_duplicates_and_full_subsumption(self):
        self.assertEqual(report_store.normalize_modes([]), ("full",))
        self.assertEqual(report_store.normalize_modes(["rate", "roast", "roast"]), ("roast", "rate"))
        self.assertEqual(report_store.normalize_modes(["rate", "full", "review", "roast"]), ("full", "roast"))
        self.assertEqual(report_store.normalize_modes(["compare", "question", "rate"]), ("question", "rate", "compare"))

    def test_help_overrides_other_modes_and_unknown_modes_fail(self):
        self.assertEqual(report_store.normalize_modes(["roast", "help"]), ("help",))
        with self.assertRaises(ValueError):
            report_store.normalize_modes(["unknown"])


class ReportStoreTests(unittest.TestCase):
    def setUp(self):
        self.base = Path(tempfile.gettempdir()) / ("deep-critique-tests-" + uuid.uuid4().hex)
        self.base.mkdir()
        self.addCleanup(self.clean_fixture)
        self.project = self.base / "Project with spaces"
        self.project.mkdir()

    def clean_fixture(self):
        if self.base.resolve().parent != Path(tempfile.gettempdir()).resolve():
            raise RuntimeError("Fixture cleanup target escaped the temporary directory")
        def remove_readonly_git_object(function, path, error):
            target = Path(path).resolve()
            objects = (self.project / ".git/objects").resolve()
            if not isinstance(error[1], PermissionError) or not target.is_relative_to(objects):
                raise error[1]
            target.chmod(stat.S_IWRITE | stat.S_IREAD)
            function(path)
        shutil.rmtree(self.base, onerror=remove_readonly_git_object)

    def git(self, *args):
        result = subprocess.run(["git", "-C", str(self.project), *args], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout.strip()

    def init_git(self):
        self.git("init", "-q")

    def start(self, modes=(), subject="A generic proposal"):
        return report_store.start(self.project, modes, subject)

    def finish(self, run, text="## Verdict\nProceed with constraints.\n", **kwargs):
        return report_store.finish(self.project, run["run"], text, **kwargs)

    def test_non_git_default_publishes_self_contained_report_and_completion(self):
        run = self.start()
        result = self.finish(run)
        path = Path(result["path"])
        self.assertEqual(path.parent.parent.name, "full")
        self.assertIn('"subject": "A generic proposal"', path.read_text())
        self.assertIn('"git": false', path.read_text())
        completion = json.loads(path.with_name("completion.json").read_text())
        self.assertEqual(completion["report_sha256"], sha256(path.read_bytes()).hexdigest())
        self.assertEqual((self.project / ".gitignore").read_bytes(), b"/.deep-critique/\n")
        self.assertFalse(json.loads(path.with_name("run.json").read_text())["ignore_verified"])

    def test_reruns_preserve_reports_and_do_not_duplicate_ignore_rule(self):
        first = self.start(["rate", "roast"])
        result = self.finish(first)
        old = Path(result["path"]).read_bytes()
        second = self.start(["roast", "rate"])
        self.finish(second, "A different assessment.")
        self.assertNotEqual(first["run"], second["run"])
        self.assertEqual(first["run"].split("/")[0], second["run"].split("/")[0])
        self.assertEqual(Path(result["path"]).read_bytes(), old)
        self.assertEqual((self.project / ".gitignore").read_bytes().count(b"/.deep-critique/"), 1)

    def test_git_nested_directory_resolves_root_and_records_source(self):
        self.init_git()
        source = self.project / "source.txt"
        source.write_text("original\n")
        self.git("add", "source.txt")
        self.git("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid", "commit", "-qm", "fixture")
        source.write_text("changed\n")
        nested = self.project / "nested"
        nested.mkdir()
        run = report_store.start(nested, [], "Source proposal")
        self.assertEqual(Path(run["root"]), self.project)
        metadata = json.loads((Path(run["path"]) / "run.json").read_text())
        self.assertEqual(metadata["source"]["revision"], self.git("rev-parse", "HEAD"))
        self.assertTrue(metadata["source"]["dirty"])
        self.assertTrue(metadata["ignore_verified"])
        self.git("check-ignore", "-q", ".deep-critique/full/test/report.md")

    def test_ignore_preserves_bom_crlf_and_missing_final_newline(self):
        self.init_git()
        before = b"\xef\xbb\xbf# Existing\r\nkeep-this"
        path = self.project / ".gitignore"
        path.write_bytes(before)
        self.start()
        self.assertEqual(path.read_bytes(), before + b"\r\n/.deep-critique/\r\n")

    def test_existing_ignore_coverage_and_negation_are_verified(self):
        self.init_git()
        path = self.project / ".gitignore"
        original = b"/.deep-critique/\n"
        path.write_bytes(original)
        self.start()
        self.assertEqual(path.read_bytes(), original)
        path.write_bytes(original + b"!/.deep-critique/\n")
        self.start()
        self.assertEqual(path.read_bytes(), original + b"!/.deep-critique/\n/.deep-critique/\n")
        self.start()
        self.assertEqual(path.read_bytes().count(b"/.deep-critique/\n"), 3)

    def test_tracked_output_is_refused_without_untracking_or_ignore_edits(self):
        self.init_git()
        output = self.project / storage_io.OUTPUT
        output.mkdir()
        existing = output / "owned.txt"
        existing.write_text("keep\n")
        self.git("add", ".deep-critique/owned.txt")
        with self.assertRaisesRegex(ValueError, "tracked"):
            self.start()
        self.assertEqual(self.git("ls-files"), ".deep-critique/owned.txt")
        self.assertEqual(existing.read_text(), "keep\n")
        self.assertFalse((self.project / ".gitignore").exists())
        self.assertEqual({p.name for p in output.iterdir()}, {"owned.txt"})

    def test_partial_ignore_with_visible_category_is_repaired(self):
        self.init_git()
        path = self.project / ".gitignore"
        original = b"/.deep-critique/*\n!/.deep-critique/full/\n"
        path.write_bytes(original)
        run = self.start()
        self.finish(run)
        self.assertEqual(path.read_bytes(), original + b"/.deep-critique/\n")
        for name in ("run.json", "report.md", "completion.json"):
            self.git("check-ignore", "-q", f'.deep-critique/{run["run"]}/{name}')

    def test_non_git_negated_rule_gets_a_final_anchored_rule(self):
        path = self.project / ".gitignore"
        original = b"/.deep-critique/\n!/.deep-critique/\n"
        path.write_bytes(original)
        self.start()
        self.assertEqual(path.read_bytes(), original + b"/.deep-critique/\n")

    def test_unowned_folder_and_regular_file_collisions_are_preserved(self):
        output = self.project / storage_io.OUTPUT
        output.mkdir()
        (output / "existing.md").write_text("owner content")
        with self.assertRaisesRegex(ValueError, "ownership"):
            self.start()
        self.assertEqual({p.name for p in output.iterdir()}, {"existing.md"})
        (output / "existing.md").unlink()
        output.rmdir()
        output.write_text("owner file")
        with self.assertRaises(ValueError):
            self.start()
        self.assertEqual(output.read_text(), "owner file")

    def test_help_unknown_modes_and_missing_subject_do_not_create_files(self):
        for modes, subject in ((["help"], "Subject"), (["help", "rate"], "Subject"),
                               (["unknown"], "Subject"), ([], " ")):
            with self.subTest(modes=modes), self.assertRaises(ValueError):
                self.start(modes, subject)
            self.assertEqual(list(self.project.iterdir()), [])

    def test_name_collision_retries_without_replacing_existing_run(self):
        first = self.start()
        existing_id = Path(first["path"]).name
        next_id = "20261026T000000Z-0123456789ab"
        with patch.object(report_store, "new_run_id", side_effect=[existing_id, next_id]):
            second = self.start()
        self.assertEqual(Path(second["path"]).name, next_id)
        self.assertTrue((Path(first["path"]) / "run.json").is_file())

    def test_transcript_is_ordered_and_finalized_with_the_report(self):
        run = self.start(["question", "rate"])
        report_store.append(self.project, run["run"], "Question: Who is the audience?")
        report_store.append(self.project, run["run"], "Answer: First-time gardeners.")
        result = self.finish(run, "## Assessment\nNeeds audience constraints.")
        text = Path(result["path"]).read_text()
        self.assertLess(text.index("Question: Who"), text.index("Answer: First"))
        with self.assertRaisesRegex(ValueError, "finalized"):
            report_store.append(self.project, run["run"], "late edit")

    def test_transcript_requires_question_mode(self):
        run = self.start()
        with self.assertRaisesRegex(ValueError, "question"):
            report_store.append(self.project, run["run"], "A question")

    def test_completed_reports_are_immutable_and_identical_finish_is_idempotent(self):
        run = self.start()
        first = self.finish(run)
        target = Path(first["path"])
        timestamp = target.stat().st_mtime_ns
        completion = target.with_name("completion.json").read_bytes()
        self.assertEqual(self.finish(run), first)
        self.assertEqual(target.stat().st_mtime_ns, timestamp)
        self.assertEqual(target.with_name("completion.json").read_bytes(), completion)
        with self.assertRaisesRegex(ValueError, "different content"):
            self.finish(run, "changed")

    def test_incomplete_report_is_distinct_from_unfinished_run(self):
        run = self.start(["question"])
        self.assertFalse((Path(run["path"]) / "completion.json").exists())
        result = self.finish(run, "Stopped with open questions.", status="incomplete")
        self.assertEqual(result["status"], "incomplete")
        self.assertEqual(json.loads((Path(run["path"]) / "completion.json").read_text())["status"], "incomplete")

    def test_failed_atomic_publication_leaves_no_partial_report_and_can_retry(self):
        run = self.start()
        with patch.object(storage_io.os, "link", side_effect=OSError("publication unavailable")):
            with self.assertRaises(OSError):
                self.finish(run)
        path = Path(run["path"])
        self.assertFalse((path / "report.md").exists())
        self.assertFalse((path / "completion.json").exists())
        self.assertEqual(list(path.glob(".pending-*")), [])
        self.finish(run)

    def test_process_death_releases_lock_and_identical_finish_recovers_completion(self):
        run = self.start()
        script = """
import os, sys
sys.path.insert(0, sys.argv[1])
import report_store
publish = report_store.publish_new
def crash(path, data):
    publish(path, data)
    if path.name == 'report.md':
        os._exit(74)
report_store.publish_new = crash
report_store.finish(sys.argv[2], sys.argv[3], 'A crash-safe report.')
"""
        process = subprocess.run([sys.executable, "-B", "-c", script, str(SCRIPTS), str(self.project), run["run"]],
                                 capture_output=True, text=True, timeout=20)
        self.assertEqual(process.returncode, 74, process.stderr)
        path = Path(run["path"])
        self.assertTrue((path / "report.md").exists())
        self.assertFalse((path / "completion.json").exists())
        before = (path / "report.md").read_bytes()
        self.finish(run, "A crash-safe report.")
        self.assertEqual((path / "report.md").read_bytes(), before)
        self.assertTrue((path / "completion.json").exists())

    def test_concurrent_processes_allocate_unique_runs_and_one_ignore_entry(self):
        self.init_git()
        def create(index):
            result = subprocess.run([sys.executable, "-B", str(SCRIPTS / "report_store.py"), "start",
                                     "--root", str(self.project), "--modes", "rate", "roast",
                                     "--subject", f"Proposal {index}"], capture_output=True, text=True, timeout=30)
            self.assertEqual(result.returncode, 0, result.stderr)
            return json.loads(result.stdout)
        with ThreadPoolExecutor(max_workers=6) as executor:
            runs = list(executor.map(create, range(6)))
        self.assertEqual(len({run["run"] for run in runs}), 6)
        self.assertEqual((self.project / ".gitignore").read_bytes(), b"/.deep-critique/\n")
        for run in runs:
            self.assertTrue((Path(run["path"]) / "run.json").exists())

    def test_process_death_during_hardlink_publication_recovers_all_artifacts(self):
        script = """
import os, sys
from pathlib import Path
sys.path.insert(0, sys.argv[1])
import report_store, storage_io
link = os.link
def crash(source, target):
    link(source, target)
    if Path(target).name == sys.argv[3]:
        os._exit(75)
storage_io.os.link = crash
if sys.argv[3] in {'.store.json', 'run.json'}:
    report_store.start(sys.argv[2], [], 'Subject')
else:
    report_store.finish(sys.argv[2], sys.argv[4], 'Report')
"""
        for name in (".store.json", "run.json", "report.md", "completion.json"):
            with self.subTest(artifact=name):
                directory = self.project / name.replace(".", "-")
                directory.mkdir()
                run = None if name in {".store.json", "run.json"} else report_store.start(directory, [], "Subject")
                result = subprocess.run([sys.executable, "-B", "-c", script, str(SCRIPTS), str(directory),
                                         name, run["run"] if run else ""], capture_output=True, text=True, timeout=20)
                self.assertEqual(result.returncode, 75, result.stderr)
                output = directory / storage_io.OUTPUT
                if name == ".store.json":
                    run = report_store.start(directory, [], "Subject")
                elif name == "run.json":
                    run_path = next((output / "full").iterdir())
                    run = {"run": "full/" + run_path.name}
                final = report_store.finish(directory, run["run"], "Report")
                self.assertEqual(final["status"], "complete")
                self.assertEqual(list(output.rglob(".pending-*")), [])
                self.assertEqual((output / ".store.json").stat().st_nlink, 1)

    def test_external_hardlink_to_report_is_not_adopted_or_removed(self):
        run = self.start()
        final = self.finish(run)
        alias = self.base / "external-report.md"
        os.link(final["path"], alias)
        before = alias.read_bytes()
        with self.assertRaisesRegex(ValueError, "hard links outside"):
            self.finish(run)
        self.assertEqual(alias.read_bytes(), before)
        self.assertTrue(Path(final["path"]).exists())

    def test_unowned_marker_alias_is_preserved_before_refusal(self):
        output = self.project / storage_io.OUTPUT
        output.mkdir()
        marker = output / ".store.json"
        marker.write_text('{"owner": "another-tool"}')
        alias = output / (".pending-" + "a" * 32)
        os.link(marker, alias)
        with self.assertRaisesRegex(ValueError, "ownership"):
            self.start()
        self.assertTrue(alias.exists())
        self.assertEqual(marker.stat().st_nlink, 2)
        self.assertEqual({p.name for p in output.iterdir()}, {".store.json", alias.name})

    def test_tracked_pending_alias_is_preserved_before_refusal(self):
        self.init_git()
        run = self.start()
        output = self.project / storage_io.OUTPUT
        alias = output / (".pending-" + "b" * 32)
        os.link(output / ".store.json", alias)
        self.git("add", "-f", ".deep-critique/" + alias.name)
        with self.assertRaisesRegex(ValueError, "tracked"):
            self.finish(run)
        self.assertTrue(alias.exists())
        self.assertEqual(self.git("diff", "--name-only"), "")
        self.assertEqual((output / ".store.json").stat().st_nlink, 2)

    def test_unowned_folder_with_existing_empty_lock_is_unchanged(self):
        output = self.project / storage_io.OUTPUT
        output.mkdir()
        lock = output / ".lock"
        lock.write_bytes(b"")
        (output / "owner.txt").write_text("preserve")
        with self.assertRaisesRegex(ValueError, "ownership"):
            self.start()
        self.assertEqual(lock.read_bytes(), b"")
        self.assertEqual({p.name for p in output.iterdir()}, {".lock", "owner.txt"})

    def test_concurrent_start_waits_for_pending_initial_marker(self):
        signal = self.base / "marker-ready"
        release = self.base / "release-marker"
        script = """
import os, sys, time
from pathlib import Path
sys.path.insert(0, sys.argv[1])
import report_store, storage_io
link = os.link
def pause(source, target):
    if Path(target).name == '.store.json':
        Path(sys.argv[3]).write_text('ready')
        while not Path(sys.argv[4]).exists():
            time.sleep(0.01)
    link(source, target)
storage_io.os.link = pause
report_store.start(sys.argv[2], [], 'First subject')
"""
        first = subprocess.Popen([sys.executable, "-B", "-c", script, str(SCRIPTS), str(self.project), str(signal), str(release)],
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        self.addCleanup(lambda: (first.kill(), first.wait()) if first.poll() is None else None)
        deadline = time.monotonic() + 10
        while not signal.exists() and first.poll() is None and time.monotonic() < deadline:
            time.sleep(0.01)
        self.assertTrue(signal.exists())
        second = subprocess.Popen([sys.executable, "-B", str(SCRIPTS / "report_store.py"), "start", "--root",
                                   str(self.project), "--subject", "Second subject"],
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        self.addCleanup(lambda: (second.kill(), second.wait()) if second.poll() is None else None)
        time.sleep(0.2)
        self.assertIsNone(second.poll(), "Second start rejected an active initializing store")
        release.write_text("continue")
        _, first_error = first.communicate(timeout=10)
        _, second_error = second.communicate(timeout=10)
        self.assertEqual(first.returncode, 0, first_error)
        self.assertEqual(second.returncode, 0, second_error)
        self.assertEqual(len(list((self.project / storage_io.OUTPUT / "full").iterdir())), 2)

    def test_malformed_metadata_is_a_clear_cli_error(self):
        run = self.start()
        (Path(run["path"]) / "run.json").write_text("[]")
        draft = self.base / "draft.md"
        draft.write_text("Report")
        result = subprocess.run([sys.executable, "-B", str(SCRIPTS / "report_store.py"), "finish",
                                 "--root", str(self.project), "--run", run["run"], "--input", str(draft)],
                                capture_output=True, text=True, timeout=20)
        self.assertEqual(result.returncode, 1)
        self.assertIn("Metadata must contain an object", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_traversal_and_metadata_mismatch_are_rejected(self):
        run = self.start()
        with self.assertRaises(ValueError):
            report_store.finish(self.project, "../outside", "report")
        metadata = Path(run["path"]) / "run.json"
        value = json.loads(metadata.read_text())
        value["root"] = str(self.base)
        metadata.write_text(json.dumps(value))
        with self.assertRaisesRegex(ValueError, "metadata"):
            self.finish(run)
        self.assertFalse((metadata.parent / "report.md").exists())

    def test_hardlinked_ignore_file_is_rejected_without_mutating_its_target(self):
        original = self.base / "original-ignore"
        original.write_text("keep\n")
        os.link(original, self.project / ".gitignore")
        with self.assertRaisesRegex(ValueError, "unlinked regular"):
            self.start()
        self.assertEqual(original.read_text(), "keep\n")
        self.assertFalse((self.project / storage_io.OUTPUT).exists())

    def test_linked_output_directory_is_rejected(self):
        outside = self.base / "outside"
        outside.mkdir()
        link = self.project / storage_io.OUTPUT
        if os.name == "nt":
            result = subprocess.run(["cmd", "/c", "mklink", "/J", str(link), str(outside)], capture_output=True)
            if result.returncode:
                self.skipTest("Cannot create a junction in this environment")
        else:
            link.symlink_to(outside, target_is_directory=True)
        self.addCleanup(lambda: link.rmdir() if os.name == "nt" else link.unlink())
        with self.assertRaisesRegex(ValueError, "Linked path"):
            self.start()
        self.assertEqual(list(outside.iterdir()), [])

    def test_busy_lock_times_out_without_removing_lock_file(self):
        run = self.start()
        output = self.project / storage_io.OUTPUT
        with storage_io.store_lock(output):
            with self.assertRaisesRegex(ValueError, "writer"):
                with storage_io.store_lock(output, timeout=0.01):
                    self.fail("Second writer acquired the same lock")
        self.assertTrue((output / ".lock").is_file())
        self.finish(run)


if __name__ == "__main__":
    unittest.main()

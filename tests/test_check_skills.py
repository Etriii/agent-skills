"""Exercise checker failures, selection, evidence limits, and read-only behavior."""

from contextlib import redirect_stdout
from hashlib import sha256
import io
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import check_skills


class CheckSkillsTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="skill checker ")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.pack = self.root / "packs/developer-skills"
        self.skill = self.pack / "skills/sample-review"
        self.skill.mkdir(parents=True)
        fixture = ROOT / "tests/fixtures/sample-review"
        body = (fixture / "SKILL.md.example").read_text(encoding="utf-8")
        (self.skill / "SKILL.md").write_text(
            body + "\n## Generated artifacts\n\nThis fixture returns chat only.\n", encoding="utf-8")
        metadata = (fixture / "metadata.toml").read_text(encoding="utf-8")
        (self.skill / "metadata.toml").write_text(
            metadata + '\nskill_id = "sample-review"\nprovenance = "local-authored"\n', encoding="utf-8")
        (self.skill / "README.md").write_text("# Sample\n\n[Instructions](SKILL.md)\n", encoding="utf-8")
        self.manifest()

    def manifest(self):
        rows = []
        for path in sorted((self.pack / "skills").rglob("*")):
            if path.is_file():
                rows.append(f"{sha256(path.read_bytes()).hexdigest()}  {path.relative_to(self.pack).as_posix()}\n")
        (self.pack / "SHA256SUMS").write_text("".join(rows), encoding="utf-8", newline="\n")

    def checks(self, selected=None):
        return check_skills.check_collection(self.root, selected)

    def failures(self, selected=None):
        return [check for check in self.checks(selected) if check.status == "FAIL"]

    def test_valid_bundle_is_checked_without_writes_or_claiming_behavior(self):
        def snapshot():
            return {p.relative_to(self.root).as_posix(): (p.read_bytes(), p.stat().st_mtime_ns)
                    for p in self.root.rglob("*") if p.is_file()}
        before = snapshot()
        checks = self.checks()
        self.assertEqual([c.subject for c in checks if c.status == "PASS"], ["sample-review"])
        self.assertFalse([c for c in checks if c.status == "FAIL"])
        self.assertTrue(any(c.status == "NOT VERIFIED" and c.subject == "behavior" for c in checks))
        self.assertTrue(any(c.status == "NOT VERIFIED" and c.subject == "publication" for c in checks))
        self.assertEqual(snapshot(), before)

    def test_changed_payload_fails_integrity_before_success(self):
        (self.skill / "README.md").write_text("Changed without manifest update\n", encoding="utf-8")
        self.assertIn("checksum mismatch", self.failures()[0].detail)

    def test_missing_manifest_is_a_failed_check(self):
        (self.pack / "SHA256SUMS").unlink()
        self.assertEqual([c.subject for c in self.failures()], ["sample-review"])

    def test_missing_readme_and_required_metadata_fail_even_with_refreshed_manifest(self):
        for name in ("README.md", "metadata.toml"):
            with self.subTest(name=name):
                path = self.skill / name
                data = path.read_bytes()
                path.unlink()
                self.manifest()
                self.assertIn(name, self.failures()[0].detail)
                path.write_bytes(data)
                self.manifest()

    def test_metadata_identity_failure_is_reported(self):
        path = self.skill / "metadata.toml"
        path.write_text(path.read_text().replace('name = "sample-review"', 'name = "different"'))
        self.manifest()
        self.assertIn("metadata identity", self.failures()[0].detail)

    def test_broken_inline_and_reference_links_fail_with_document_paths(self):
        path = self.skill / "README.md"
        for text, target in (("[Guide](missing.md)", "missing.md"),
                             ("[Guide][usage]\n\n[usage]: <missing guide.md>", "missing guide.md"),
                             ("![Preview](missing.png)", "missing.png")):
            with self.subTest(target=target):
                path.write_text(text, encoding="utf-8")
                self.manifest()
                failures = self.failures()
                self.assertEqual(len(failures), 1)
                self.assertIn("README.md", failures[0].detail)
                self.assertIn(target, failures[0].detail)

    def test_fenced_examples_remote_links_and_encoded_local_paths_are_handled(self):
        (self.root / "usage guide.md").write_text("# Usage\n", encoding="utf-8")
        (self.skill / "README.md").write_text(
            "~~~markdown\n[Example](not-a-file.md)\n~~~\n"
            "`[Inline example](also-not-a-file.md)`\n"
            "[Remote](https://example.invalid/unavailable)\n"
            "[Usage](../../../../usage%20guide.md#not-an-anchor-check)\n", encoding="utf-8")
        self.manifest()
        self.assertFalse(self.failures())

    def test_authored_reference_links_are_checked_but_vendor_context_is_not(self):
        vendor = self.skill / "vendor"
        vendor.mkdir()
        (vendor / "upstream.md").write_text("[Original repository](../original.md)", encoding="utf-8")
        self.manifest()
        self.assertFalse(self.failures())
        references = self.skill / "references"
        references.mkdir()
        (references / "guide.md").write_text("[Missing](missing.md)", encoding="utf-8")
        self.manifest()
        self.assertIn("references/guide.md", self.failures()[0].detail)

    def test_local_links_cannot_escape_the_collection(self):
        (self.skill / "README.md").write_text("[Outside](../../../../../outside.md)", encoding="utf-8")
        self.manifest()
        self.assertIn("out-of-tree", self.failures()[0].detail)

    def test_duplicate_names_are_reported_across_packs(self):
        second = self.root / "packs/another-pack/skills/sample-review"
        shutil.copytree(self.skill, second)
        shutil.copyfile(self.pack / "SHA256SUMS", second.parent.parent / "SHA256SUMS")
        self.assertTrue(any("duplicate" in check.detail for check in self.failures()))

    def test_escaped_links_are_rejected_before_inspecting_external_paths(self):
        document = self.skill / "README.md"
        document.write_text("[Outside](../../../../../outside.md)\n[Remote](//example.invalid/guide)\n",
                            encoding="utf-8")
        with patch.object(check_skills, "safe_path", side_effect=AssertionError("external path inspected")):
            errors = check_skills.broken_links(document, self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("out-of-tree", errors[0])

    def test_selection_checks_requested_skill_and_rejects_unknown_or_unsafe_names(self):
        other = self.pack / "skills/broken-skill"
        other.mkdir()
        self.assertFalse(self.failures(["sample-review"]))
        self.assertEqual([c.subject for c in self.failures()], ["broken-skill"])
        for name in ("missing", "../sample-review"):
            with self.subTest(name=name):
                self.assertEqual([c.subject for c in self.failures([name])], [name])

    def test_empty_collection_fails(self):
        self.assertTrue(self.skill.resolve().is_relative_to(self.root))
        shutil.rmtree(self.skill)
        self.assertTrue(any("no shipping skills" in c.detail for c in self.failures()))

    def test_cli_exit_codes_and_selected_output(self):
        with patch.object(check_skills, "ROOT", self.root):
            for args, expected in ((["--all"], 0), (["--skill", "sample-review"], 0),
                                   (["--skill", "unknown"], 1)):
                with self.subTest(args=args), redirect_stdout(io.StringIO()) as output:
                    self.assertEqual(check_skills.main(args), expected)
                    self.assertIn("Static checks:", output.getvalue())
        with patch.object(check_skills, "ROOT", self.root / "missing"), redirect_stdout(io.StringIO()):
            self.assertEqual(check_skills.main(["--all"]), 1)


if __name__ == "__main__":
    unittest.main()

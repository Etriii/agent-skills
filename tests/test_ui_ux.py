"""Verify independent UI/UX installations, source notices and resource synchronization."""

from contextlib import redirect_stderr, redirect_stdout
from hashlib import sha256
import io
import json
from pathlib import Path
import re
import shutil
import sys
import tempfile
import unittest
import uuid


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "packs/developer-skills/skills"
sys.path.insert(0, str(ROOT / "tools"))
import catalog
import install_skills
import sync_ui_ux


class UiUxTests(unittest.TestCase):
    def setUp(self):
        self.base = Path(tempfile.gettempdir()) / f"ui ux suite {uuid.uuid4().hex}"
        self.base.mkdir()
        self.addCleanup(shutil.rmtree, self.base)

    def test_each_entrypoint_installs_alone_with_all_runtime_resources_for_both_agents(self):
        for name in (sync_ui_ux.CANONICAL, *sync_ui_ux.STANDALONE):
            project = self.base / name
            project.mkdir()
            with redirect_stdout(io.StringIO()) as output, redirect_stderr(io.StringIO()) as errors:
                result = install_skills.main([
                    "--pack", "developer-skills", "--agent", "both", "--project", str(project),
                    "--skills", name, "--yes",
                ])
            self.assertEqual(result, 0, output.getvalue() + errors.getvalue())
            for agent in (".agents", ".claude"):
                installed = project / agent / "skills" / name
                self.assertEqual({p.name for p in installed.parent.iterdir()}, {name})
                self.assertEqual(catalog.files_in(installed), catalog.files_in(SKILLS / name))
                runtime_docs = [installed / "SKILL.md", installed / "THIRD_PARTY.md",
                                *(installed / "references").glob("*.md")]
                for document in runtime_docs:
                    for target in re.findall(r"\]\(([^)]+)\)", document.read_text(encoding="utf-8")):
                        if "://" in target or target.startswith("#"):
                            continue
                        linked = (document.parent / target.split("#")[0]).resolve()
                        with self.subTest(skill=name, agent=agent, document=document.name, target=target):
                            self.assertTrue(linked.is_relative_to(installed.resolve()))
                            self.assertTrue(linked.is_file())

    def test_copied_sources_and_licenses_are_pinned_and_hash_verified(self):
        for name in (sync_ui_ux.CANONICAL, *sync_ui_ux.STANDALONE):
            root = SKILLS / name
            metadata = catalog.validate_skill(root)
            self.assertEqual(metadata["provenance"], "local-with-third-party")
            self.assertEqual(metadata["compatible_agents"], [])
            records = json.loads((root / "vendor/SOURCES.json").read_text(encoding="utf-8"))
            self.assertEqual({r["name"] for r in records}, {"taste", "pro-max", "pro-max-ux-data", "frontend-design"})
            notices = (root / metadata["third_party_notices"]).read_text(encoding="utf-8")
            for record in records:
                self.assertRegex(record["revision"], r"^[0-9a-f]{40}$")
                self.assertRegex(record["source_sha256"], r"^[0-9a-f]{64}$")
                self.assertIn(record["revision"], notices)
                for path_field, hash_field in (("local_path", "local_sha256"), ("license_path", "license_sha256")):
                    path = (root / record[path_field]).resolve()
                    self.assertTrue(path.is_relative_to(root.resolve()))
                    self.assertEqual(sha256(path.read_bytes()).hexdigest(), record[hash_field])
                if "excerpt_lines" not in record:
                    self.assertEqual(record["source_sha256"], record["local_sha256"])

    def test_mixed_provenance_requires_its_bundled_notices(self):
        root = self.base / "ultimate-ui"
        shutil.copytree(SKILLS / root.name, root)
        (root / "THIRD_PARTY.md").unlink()
        with self.assertRaisesRegex(ValueError, "requires bundled notices"):
            catalog.validate_skill(root)
        (root / "THIRD_PARTY.md").write_text("bundled notices\n", encoding="utf-8")
        metadata = root / "metadata.toml"
        original = metadata.read_text(encoding="utf-8")
        metadata.write_text(original.replace(
            'third_party_notices = "THIRD_PARTY.md"', 'third_party_notices = "../THIRD_PARTY.md"'), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "requires bundled notices"):
            catalog.validate_skill(root)
        metadata.write_text(original.replace('provenance = "local-with-third-party"', 'provenance = []'), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Unsupported license/provenance"):
            catalog.validate_skill(root)

    def test_shared_resources_match_the_canonical_owner(self):
        self.assertEqual(sync_ui_ux.sync(check=True), [])

    def test_sync_check_is_read_only_and_sync_repairs_missing_and_changed_resources(self):
        skills = self.base / "skills"
        shutil.copytree(SKILLS / sync_ui_ux.CANONICAL, skills / sync_ui_ux.CANONICAL)
        for name in sync_ui_ux.STANDALONE:
            (skills / name).mkdir()
            (skills / name / "SKILL.md").write_text("preserve entrypoint\n", encoding="utf-8")
        before = catalog.files_in(skills)
        self.assertTrue(sync_ui_ux.sync(skills, check=True))
        self.assertEqual(catalog.files_in(skills), before)
        sync_ui_ux.sync(skills)
        self.assertEqual(sync_ui_ux.sync(skills, check=True), [])
        changed = skills / "ultimate-ui/references/workflow.md"
        changed.write_text("drift\n", encoding="utf-8")
        self.assertTrue(sync_ui_ux.sync(skills, check=True))
        self.assertEqual(changed.read_text(encoding="utf-8"), "drift\n")
        sync_ui_ux.sync(skills)
        self.assertEqual(sync_ui_ux.sync(skills, check=True), [])
        for name in sync_ui_ux.STANDALONE:
            self.assertEqual((skills / name / "SKILL.md").read_text(encoding="utf-8"), "preserve entrypoint\n")

    def test_sync_preserves_unexpected_resources_for_explicit_review(self):
        skills = self.base / "skills"
        for name in (sync_ui_ux.CANONICAL, *sync_ui_ux.STANDALONE):
            shutil.copytree(SKILLS / name, skills / name)
        custom = skills / "ultimate-ui/references/custom.md"
        custom.write_text("preserve custom notes\n", encoding="utf-8")
        self.assertTrue(sync_ui_ux.sync(skills, check=True))
        with self.assertRaisesRegex(ValueError, "Unexpected resources"):
            sync_ui_ux.sync(skills)
        self.assertEqual(custom.read_text(encoding="utf-8"), "preserve custom notes\n")


if __name__ == "__main__":
    unittest.main()

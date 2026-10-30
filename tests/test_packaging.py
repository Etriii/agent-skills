"""Verify download archives contain complete packs and independently checked payloads."""

from hashlib import sha256
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
import uuid
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import catalog
import package_skills


class PackagingTests(unittest.TestCase):
    def test_archive_has_exact_checksums_support_files_and_repeatable_bytes(self):
        output = Path(tempfile.gettempdir()) / f"agent-skills-package-{uuid.uuid4().hex}"
        output.mkdir()
        self.addCleanup(shutil.rmtree, output)
        archive, checksum = package_skills.build(ROOT, output)
        with ZipFile(archive) as zipped:
            names = zipped.namelist()
            self.assertTrue(all(name.startswith("agent-skills/") for name in names))
            self.assertFalse(any(part in package_skills.EXCLUDED for name in names for part in name.split("/")))
            self.assertIn("agent-skills/packs/ultimate-qa/tools/qa_preflight.py", names)
            self.assertIn("agent-skills/packs/ultimate-qa/04_REQUIREMENTS_TEMPLATE/02_PROJECT_CONTEXT.md", names)
            self.assertIn("agent-skills/packs/developer-skills/skills/blocker-check/SKILL.md", names)
            self.assertIn("agent-skills/tools/records.py", names)
            self.assertIn("agent-skills/CONTRIBUTING.md", names)
            for skill in ROOT.glob("packs/*/skills/*/SKILL.md"):
                readme = skill.with_name("README.md").relative_to(ROOT).as_posix()
                self.assertIn(f"agent-skills/{readme}", names)
            manifest = zipped.read("agent-skills/SNAPSHOT_SHA256SUMS").decode()
            rows = dict(line.split("  ", 1)[::-1] for line in manifest.splitlines())
            self.assertEqual(set(rows), {name.removeprefix("agent-skills/") for name in names} - {"SNAPSHOT_SHA256SUMS"})
            for name, expected in rows.items():
                self.assertEqual(sha256(zipped.read(f"agent-skills/{name}")).hexdigest(), expected)
        self.assertEqual(checksum, sha256(archive.read_bytes()).hexdigest())
        self.assertEqual(package_skills.build(ROOT, output)[1], checksum)
        self.assertEqual((output / "SHA256SUMS").read_text().split()[0], checksum)

    def test_every_shipping_pack_has_valid_unique_names_and_complete_payloads(self):
        seen = set()
        for pack in (ROOT / "packs").iterdir():
            names = sorted(path.name for path in (pack / "skills").iterdir())
            self.assertFalse(seen.intersection(names))
            seen.update(names)
            self.assertEqual(set(catalog.bundle(pack, names)), set(names))
        self.assertEqual(len(seen), 33)

    def test_tree_fingerprint_is_independent_of_platform_filename_order(self):
        rows = {"SKILL.md": "a" * 64, "kit-location.txt": "b" * 64}
        self.assertEqual(catalog.fingerprint(rows, []), catalog.fingerprint(dict(reversed(list(rows.items()))), []))


if __name__ == "__main__":
    unittest.main()

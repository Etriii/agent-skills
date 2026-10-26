"""Check the standalone metadata fixture and public source boundary."""

import ast
from pathlib import Path
import re
import tomllib
import unittest


ROOT = Path(__file__).resolve().parents[1]


class PublicContractTests(unittest.TestCase):
    def test_portable_skill_fixture_has_matching_name_and_human_description(self):
        fixture = ROOT / "tests/fixtures/sample-review"
        skill = (fixture / "SKILL.md.example").read_text(encoding="utf-8")
        frontmatter = re.fullmatch(r"---\nname: ([a-z0-9]+(?:-[a-z0-9]+)*)\ndescription: ([^\n]+)\n---\n(.+)", skill, re.S)
        self.assertIsNotNone(frontmatter)
        self.assertEqual(frontmatter.group(1), fixture.name)
        self.assertGreater(len(frontmatter.group(2).split()), 5)
        for field in ("Input:", "Output:", "Limits:"):
            self.assertIn(field, frontmatter.group(3))

    def test_metadata_records_unverified_compatibility_and_license_honestly(self):
        metadata = tomllib.loads((ROOT / "tests/fixtures/sample-review/metadata.toml").read_text(encoding="utf-8"))
        self.assertEqual(metadata["schema_version"], 1)
        self.assertEqual(metadata["name"], "sample-review")
        self.assertRegex(metadata["version"], r"^\d+\.\d+\.\d+$")
        self.assertTrue(metadata["capabilities"])
        self.assertEqual(metadata["compatible_agents"], [])
        self.assertEqual(metadata["license_status"], "UNDECIDED")

    def test_public_python_has_no_private_import_or_runtime_state_requirement(self):
        for source in ROOT.rglob("*.py"):
            with self.subTest(source=source.relative_to(ROOT)):
                tree = ast.parse(source.read_text(encoding="utf-8"))
                for node in ast.walk(tree):
                    if isinstance(node, ast.Import):
                        imports = [alias.name for alias in node.names]
                    elif isinstance(node, ast.ImportFrom):
                        imports = [node.module or ""]
                    else:
                        continue
                    self.assertTrue(all(name.split(".")[0] != "phasepilot" for name in imports))
        fixture = (ROOT / "tests/fixtures/sample-review/SKILL.md.example").read_text(encoding="utf-8")
        self.assertNotIn(".phasepilot/", fixture)

    def test_repository_discovery_exposes_only_shipping_skills(self):
        expected = set(ROOT.glob("packs/*/skills/*/SKILL.md"))
        self.assertEqual(len(expected), 25)
        skipped = {"node_modules", ".git", "dist", "build", "__pycache__"}
        discovered = {path for path in ROOT.rglob("SKILL.md")
                      if not skipped.intersection(path.relative_to(ROOT).parts)}
        self.assertEqual(discovered, expected)


if __name__ == "__main__":
    unittest.main()

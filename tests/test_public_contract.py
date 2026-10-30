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
        self.assertEqual(len(expected), 34)
        skipped = {"node_modules", ".git", "dist", "build", "__pycache__"}
        discovered = {path for path in ROOT.rglob("SKILL.md")
                      if not skipped.intersection(path.relative_to(ROOT).parts)}
        self.assertEqual(discovered, expected)

    def test_catalog_categorizes_every_shipping_skill_once_with_valid_links(self):
        expected = {path.parent.name: path.parent
                    for path in ROOT.glob("packs/*/skills/*/SKILL.md")}
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        catalog = (ROOT / "SKILL_CATALOG.md").read_text(encoding="utf-8")
        seen = set()
        categories = set()
        category = None
        for line_number, line in enumerate(catalog.splitlines(), 1):
            if line.startswith("## "):
                category = line[3:].strip()
            if not line.startswith("|") or line.startswith(("| Skill |", "|---")):
                continue
            with self.subTest(line=line_number):
                row = re.fullmatch(
                    r"\| \[([a-z0-9]+(?:-[a-z0-9]+)*)\]\(([^)]+)\)"
                    r" \| ([^|]+) \| `([a-z0-9]+(?:-[a-z0-9]+)*)` \|", line)
                self.assertIsNotNone(row, "Use a skill README link, purpose and install pack ID")
                name, target, purpose, pack = row.groups()
                self.assertTrue(category, "Every skill needs a category heading")
                self.assertTrue(purpose.strip(), "Every skill needs a purpose")
                self.assertIn(name, expected, "Only shipping skills belong in the catalog")
                self.assertNotIn(name, seen, "List each skill in exactly one category")
                skill = expected[name]
                self.assertEqual(target, skill.joinpath("README.md").relative_to(ROOT).as_posix())
                self.assertTrue((ROOT / target).is_file(), "Skill README link is broken")
                self.assertEqual(pack, skill.parent.parent.name)
                seen.add(name)
                categories.add(category)
        self.assertEqual(seen, set(expected), "Every shipping skill needs a catalog entry")
        for category in categories:
            anchor = re.sub(r"[^\w -]", "", category.lower()).replace(" ", "-")
            with self.subTest(category=category):
                self.assertIn(f"](SKILL_CATALOG.md#{anchor})", readme,
                              "Link every populated category from the main README")


if __name__ == "__main__":
    unittest.main()

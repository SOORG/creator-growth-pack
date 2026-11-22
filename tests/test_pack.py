"""Offline regression checks for the four instruction-only skills."""
from __future__ import annotations

import json
import re
import sys
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))
from package_skills import EXPECTED, build  # noqa: E402


class PackTests(unittest.TestCase):
    def test_manifest_matches_skills(self) -> None:
        plugin = json.loads((ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(plugin["name"], "creator-growth-pack")
        self.assertEqual(plugin["version"], "1.2.0")
        self.assertEqual(plugin["license"], "SEE LICENSE — SOORG License v1.0")
        self.assertEqual(
            {p.name for p in (ROOT / "skills").iterdir() if p.is_dir()},
            set(EXPECTED),
        )

    def test_skill_frontmatter_and_references(self) -> None:
        for name in EXPECTED:
            with self.subTest(skill=name):
                path = ROOT / "skills" / name / "SKILL.md"
                content = path.read_text(encoding="utf-8")
                self.assertTrue(content.startswith("---\n"))
                header = content.split("---\n", 2)[1]
                self.assertRegex(header, rf"(?m)^name: {re.escape(name)}$")
                self.assertRegex(header, r"(?m)^description: .{30,}$")
                self.assertRegex(header, r"(?m)^license: SEE LICENSE - SOORG License v1.0$")
                self.assertIn("[VERIFY]", content)
                for ref in re.findall(r"`((?:references|assets)/[^`]+)`", content):
                    self.assertTrue((path.parent / ref).is_file(), f"Missing reference: {name}/{ref}")

    def test_no_fixed_unverified_commercial_claims(self) -> None:
        for path in (ROOT / "skills").rglob("*.md"):
            with self.subTest(path=str(path.relative_to(ROOT))):
                contents = path.read_text(encoding="utf-8").lower()
                for claim in ("creators keep 80%", "payout weekly", "instant payouts", "40%+ of calls", "20% to cover payments"):
                    self.assertNotIn(claim, contents)

    def test_license_and_operator_input(self) -> None:
        license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
        notice = (ROOT / "NOTICE.md").read_text(encoding="utf-8")
        self.assertIn("SOORG LICENSE v1.0", license_text)
        self.assertIn("Sorin Olariu", license_text)
        self.assertIn("info@hostallin.com", license_text)
        self.assertIn("UNMODIFIED PRODUCT", license_text)
        self.assertIn("EARLIER MIT-LICENSED MATERIAL", license_text)
        self.assertIn("SOORG License v1.0", notice)
        self.assertTrue((ROOT / "docs/LICENSING-HISTORY.md").is_file())
        self.assertTrue((ROOT / "docs/RESELLER-GUIDE.md").is_file())
        self.assertTrue((ROOT / "examples/platform-terms.example.md").is_file())
        self.assertFalse((ROOT / "LICENCE.md").exists())
        self.assertFalse((ROOT / "skills/product-listing-copy/listing-formulas.md").exists())

    def test_package_zip_is_self_contained(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            packages = build(Path(folder))
            self.assertEqual(len(packages), 4)
            for package in packages:
                with self.subTest(archive=package.name), ZipFile(package) as archive:
                    self.assertIsNone(archive.testzip())
                    self.assertIn("SKILL.md", archive.namelist())
                    self.assertFalse(any(p.startswith("skills/") for p in archive.namelist()))
                    self.assertFalse(any(".." in Path(p).parts for p in archive.namelist()))


if __name__ == "__main__":
    unittest.main()

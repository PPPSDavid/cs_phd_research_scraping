from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "02_collect_faculty.py"

spec = importlib.util.spec_from_file_location("collect_faculty", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class DomainTests(unittest.TestCase):
    def test_same_institutional_root_matches_subdomain(self) -> None:
        self.assertTrue(
            module.is_same_institutional_root("https://cecs.ucf.edu/faculty/alice", "ucf.edu")
        )
        self.assertFalse(
            module.is_same_institutional_root("https://alice.example.com", "ucf.edu")
        )


class ValidationTests(unittest.TestCase):
    def test_validate_rows_rejects_school_outside_verified_list(self) -> None:
        rows = [
            module.CandidateFaculty(
                school_name="Outside University",
                rank=99,
                professor_name="Alice Smith",
                department="Department of Computer Science",
                faculty_url="https://outside.example.edu/~alice",
                lab_url="",
                source_type="faculty_page",
                notes="areas=ai; verified_by=official_domain",
            )
        ]
        with self.assertRaises(module.FacultyCollectionError):
            module.validate_rows(rows, {"Brown University"})


class CollectionTests(unittest.TestCase):
    def test_collect_target_candidates_only_keeps_verified_school_rows(self) -> None:
        verified_schools = {
            "Brown University": module.VerifiedSchool(
                school_name="Brown University",
                rank=52,
                verified_source_url="https://cs.brown.edu/",
                department="Brown University Department of Computer Science",
                institutional_root="brown.edu",
            )
        }
        parent_map = {"aaai": "ai", "cvpr": "vision", "ismb": "bio", "sigmod": "mod"}
        author_index = {
            ("Brown University", "Ada Lovelace"): "https://cs.brown.edu/people/ada",
            ("Outside University", "Bob Jones"): "https://outside.example.edu/~bob",
        }
        author_rows = [
            {"name": "Ada Lovelace", "dept": "Brown University", "area": "aaai"},
            {"name": "Ada Lovelace", "dept": "Brown University", "area": "sigmod"},
            {"name": "Bob Jones", "dept": "Outside University", "area": "cvpr"},
        ]

        candidates = module.collect_target_candidates(
            author_rows=author_rows,
            author_index=author_index,
            verified_schools=verified_schools,
            parent_map=parent_map,
        )

        self.assertEqual(list(candidates), [("Brown University", "Ada Lovelace")])
        self.assertEqual(candidates[("Brown University", "Ada Lovelace")]["areas"], {"ai"})


if __name__ == "__main__":
    unittest.main()

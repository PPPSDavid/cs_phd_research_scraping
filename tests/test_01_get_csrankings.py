from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "01_get_csrankings.py"

spec = importlib.util.spec_from_file_location("get_csrankings", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class ParseConfigTests(unittest.TestCase):
    def test_parse_parent_map_and_next_tier(self) -> None:
        js = """
        CSRankings.parentMap = {
            'aaai': 'ai',
            'sigcomm': 'comm',
            'sigcse': 'csed',
            'usenixsec': 'sec',
        };
        CSRankings.nextTier = {
            'kdd': true,
            'ndss': true,
            'pods': true,
            'oopsla': true,
        };
        """
        parent_map = module.parse_parent_map(js)
        next_tier = module.parse_next_tier(js)

        self.assertEqual(parent_map["aaai"], "ai")
        self.assertEqual(parent_map["sigcse"], "csed")
        self.assertIn("kdd", next_tier)
        self.assertIn("pods", next_tier)


class RankingTests(unittest.TestCase):
    def test_competition_ranking_filters_requested_window(self) -> None:
        us_institutions = {
            "Alpha University": module.Institution("Alpha University", "https://alpha.example.edu", "us"),
            "Beta University": module.Institution("Beta University", "https://beta.example.edu", "us"),
            "Gamma University": module.Institution("Gamma University", "https://gamma.example.edu", "us"),
        }
        parent_map = {
            "aaai": "ai",
            "sigcomm": "comm",
            "sigcse": "csed",
            "usenixsec": "sec",
        }
        author_rows = [
            {"name": "Alice", "dept": "Alpha University", "area": "aaai", "adjustedcount": "15.0", "year": "2026"},
            {"name": "Bob", "dept": "Beta University", "area": "aaai", "adjustedcount": "10.0", "year": "2026"},
            {"name": "Carol", "dept": "Gamma University", "area": "aaai", "adjustedcount": "10.0", "year": "2026"},
        ]

        original_min = module.TARGET_RANK_MIN
        original_max = module.TARGET_RANK_MAX
        try:
            module.TARGET_RANK_MIN = 2
            module.TARGET_RANK_MAX = 2
            rows = module.compute_ranked_schools(
                author_rows=author_rows,
                us_institutions=us_institutions,
                parent_map=parent_map,
                next_tier=set(),
                start_year=2016,
                end_year=2026,
            )
        finally:
            module.TARGET_RANK_MIN = original_min
            module.TARGET_RANK_MAX = original_max

        self.assertEqual([row.rank for row in rows], [2, 2])
        self.assertEqual([row.school_name for row in rows], ["Beta University", "Gamma University"])


class OutputTests(unittest.TestCase):
    def test_write_output_csv_has_expected_header(self) -> None:
        output_dir = ROOT / "tests" / ".tmp"
        output_path = output_dir / "schools_verified.csv"
        try:
            module.write_output_csv(
                [
                    module.RankedSchool(
                        rank=52,
                        school_name="Brown University",
                        csrankings_url="https://csrankings.org/fromyear/2016/toyear/2026/index?all",
                        verified_source_url="https://www.brown.edu/",
                    )
                ],
                output_path,
            )
            text = output_path.read_text(encoding="utf-8")
        finally:
            if output_path.exists():
                output_path.unlink()
            if output_dir.exists():
                output_dir.rmdir()

        self.assertEqual(
            text.splitlines()[0],
            "rank,school_name,csrankings_url,verified_source_url",
        )
        self.assertIn("Brown University", text)


if __name__ == "__main__":
    unittest.main()

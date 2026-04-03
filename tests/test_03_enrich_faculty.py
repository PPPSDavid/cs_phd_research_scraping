from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "03_enrich_faculty.py"

spec = importlib.util.spec_from_file_location("enrich_faculty", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class ExtractionTests(unittest.TestCase):
    def test_collect_tags_finds_supported_topics(self) -> None:
        text = (
            "My research interests include machine learning, natural language processing, "
            "and computational biology."
        )
        self.assertEqual(
            module.collect_tags(text),
            "machine learning; natural language processing; computational biology",
        )

    def test_first_matching_segment_returns_unknown_when_no_match(self) -> None:
        segments = ["This page lists courses.", "Contact information is below."]
        self.assertEqual(module.first_matching_segment(segments, module.RA_PATTERNS), module.UNKNOWN)

    def test_uncertainty_flags_reports_missing_fields(self) -> None:
        flags = module.build_uncertainty_flags(
            page_sources=[],
            research_description=module.UNKNOWN,
            research_tags=module.UNKNOWN,
            recent_work_cues=module.UNKNOWN,
            ra_opportunity_cues=module.UNKNOWN,
            advising_cues=module.UNKNOWN,
        )
        self.assertIn("fetch_failed", flags)
        self.assertIn("missing_research_description", flags)
        self.assertIn("missing_advising_cues", flags)


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "04_rank_faculty.py"

spec = importlib.util.spec_from_file_location("rank_faculty", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = module
spec.loader.exec_module(module)


def make_row(**overrides: str) -> module.EnrichedFaculty:
    base = dict(
        school_name="Brown University",
        rank=52,
        professor_name="Ada Lovelace",
        department="Brown CS",
        faculty_url="https://cs.brown.edu/people/ada",
        lab_url="",
        source_type="faculty_page",
        notes="areas=ai,bio",
        research_description=module.UNKNOWN,
        research_tags=module.UNKNOWN,
        recent_work_cues=module.UNKNOWN,
        ra_opportunity_cues=module.UNKNOWN,
        advising_cues=module.UNKNOWN,
        uncertainty_flags="missing_research_description; missing_recent_work_cues; missing_ra_opportunity_cues; missing_advising_cues",
    )
    base.update(overrides)
    return module.EnrichedFaculty(**base)


class RankingTests(unittest.TestCase):
    def test_specific_bio_match_scores_higher_than_general_nlp(self) -> None:
        bio_row = make_row(
            research_description="My research focuses on computational biology and genomics.",
            research_tags="computational biology; machine learning",
            advising_cues="I am accepting PhD students.",
            uncertainty_flags="NONE",
        )
        nlp_row = make_row(
            professor_name="Grace Hopper",
            research_description="My lab works on language models and natural language processing.",
            research_tags="language models; natural language processing",
            uncertainty_flags="NONE",
        )

        bio_score = module.score_row(bio_row)
        nlp_score = module.score_row(nlp_row)

        self.assertGreater(bio_score.phd_score, nlp_score.phd_score)
        self.assertGreaterEqual(bio_score.ra_score, nlp_score.ra_score)

    def test_unknown_evidence_leads_to_unknown_summary_and_lower_confidence(self) -> None:
        scored = module.score_row(make_row())
        self.assertEqual(scored.summary, module.UNKNOWN)
        self.assertLess(float(scored.confidence), 0.5)

    def test_render_markdown_contains_prompt_and_scores(self) -> None:
        scored = module.score_row(
            make_row(
                research_description="My research focuses on medical imaging.",
                research_tags="medical imaging",
                uncertainty_flags="NONE",
            )
        )
        markdown = module.render_markdown([scored])
        self.assertIn("## Strict Scoring Prompt", markdown)
        self.assertIn("phd_score", markdown)
        self.assertIn("medical imaging", markdown)


if __name__ == "__main__":
    unittest.main()

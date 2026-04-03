# CS PhD Research Scraping

A configurable, evidence-first pipeline for turning public faculty webpages into a shortlist for PhD and RA exploration.

The repo is built to be reusable:
- change the school range
- change the target research areas
- change the scoring prompt and user profile
- change output paths per run
- keep crawling behavior conservative and respectful

## What This Pipeline Does

1. Pulls schools from CSRankings.
2. Collects candidate faculty only from those verified schools.
3. Enriches each faculty row with evidence from official public pages.
4. Scores faculty against a user profile using a strict, configurable prompt.

Current generated outputs live in [`data/`](data/).

## Why This Repo Might Be Useful To Others

This project is intentionally not just a one-off notebook dump. It shows a compact pattern for:
- staged data pipelines
- config-driven scraping and ranking
- conservative evidence extraction
- prompt configuration with examples
- simple CI and unit tests

## Quick Start

```powershell
python -m unittest discover -s tests -v
python scripts/run_pipeline.py
```

You can also run any stage individually and override input/output paths:

```powershell
python scripts/01_get_csrankings.py --output data/custom_schools.csv
python scripts/02_collect_faculty.py --input data/custom_schools.csv --output data/custom_faculty_raw.csv
python scripts/03_enrich_faculty.py --input data/custom_faculty_raw.csv --output data/custom_faculty_enriched.csv
python scripts/04_rank_faculty.py --input data/custom_faculty_enriched.csv --output data/custom_final_ranked.md
```

## Configuration

Main settings live in [`configs/pipeline.toml`](configs/pipeline.toml).

Useful knobs:
- `ranking.rank_min` / `ranking.rank_max`
- `faculty_collection.target_parent_areas`
- `http.max_workers`
- `http.retry_attempts`
- `http.default_crawl_delay_seconds`
- `http.obey_robots`
- `scoring.strict_prompt`
- `scoring.examples_path`

Prompt usage examples live in [`configs/scoring_examples.json`](configs/scoring_examples.json).

## Ethics and Respectful Scraping

The crawler is designed to be cautious:
- custom user agent
- `robots.txt` checks before fetches
- per-host throttling
- retry with backoff for transient failures
- conservative extraction that prefers `UNKNOWN` over invented facts

That still does not replace manual judgment. Before scaling up:
- review site terms
- keep concurrency modest
- avoid scraping pages that disallow bots
- prefer official faculty / department / lab pages over aggregators

## Repository Layout

- [`configs/pipeline.toml`](configs/pipeline.toml): main config
- [`configs/scoring_examples.json`](configs/scoring_examples.json): prompt examples
- [`research_pipeline/config.py`](research_pipeline/config.py): config loader
- [`research_pipeline/http.py`](research_pipeline/http.py): robots-aware HTTP client
- [`research_pipeline/csv_utils.py`](research_pipeline/csv_utils.py): reusable CSV helpers
- [`research_pipeline/cli.py`](research_pipeline/cli.py): shared CLI helpers
- [`scripts/run_pipeline.py`](scripts/run_pipeline.py): pipeline runner
- [`tests/`](tests/): unit tests
- [`.github/workflows/tests.yml`](.github/workflows/tests.yml): CI

## Current Pipeline Stages

- [`scripts/01_get_csrankings.py`](scripts/01_get_csrankings.py): verified school list
- [`scripts/02_collect_faculty.py`](scripts/02_collect_faculty.py): candidate faculty collection
- [`scripts/03_enrich_faculty.py`](scripts/03_enrich_faculty.py): evidence enrichment
- [`scripts/04_rank_faculty.py`](scripts/04_rank_faculty.py): scoring + markdown report

## CI

GitHub Actions runs:

```powershell
python -m unittest discover -s tests -v
```

This keeps the project lightweight while still checking the reusable logic.

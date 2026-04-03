# CS PhD Research Scraping

Configurable pipeline for:
- pulling ranked schools from CSRankings
- collecting faculty candidates in chosen top-level areas
- enriching faculty rows from official public pages
- scoring faculty against a configurable profile and prompt

## Project Structure

- `configs/pipeline.toml`: main project configuration
- `configs/scoring_examples.json`: examples showing how the scoring prompt is intended to be applied
- `research_pipeline/config.py`: shared config loader
- `research_pipeline/http.py`: robots-aware HTTP client with retries, throttling, and caching
- `scripts/01_get_csrankings.py`: fetch ranked schools
- `scripts/02_collect_faculty.py`: collect candidate faculty
- `scripts/03_enrich_faculty.py`: enrich faculty with page evidence
- `scripts/04_rank_faculty.py`: score faculty and render markdown
- `data/`: generated outputs

## What Is Configurable

Top-level behavior lives in `configs/pipeline.toml`.

Examples:
- change rank window with `ranking.rank_min` / `ranking.rank_max`
- change faculty collection scope with `faculty_collection.target_parent_areas`
- change ethical crawling defaults with `http.*`
- change the scoring prompt and user profile with `scoring.*`
- point to prompt usage examples with `scoring.examples_path`

## Ethics and Website Respect

This project is designed to be conservative:
- only uses publicly available pages
- uses a project-specific `User-Agent`
- checks `robots.txt` before extraction requests
- applies per-host crawl delays
- retries transient failures with backoff instead of hammering sites
- keeps evidence-driven outputs and avoids inventing facts

Important notes:
- `robots.txt` is not a legal safe harbor by itself, but it is a useful baseline courtesy mechanism.
- Some official university sites have broken SSL chains or flaky hosting. The client can retry carefully, but the safer default is still to skip pages when evidence is unclear.
- You should review each target site's terms before scaling up runs.

## Typical Workflow

```powershell
python scripts/01_get_csrankings.py
python scripts/02_collect_faculty.py
python scripts/03_enrich_faculty.py
python scripts/04_rank_faculty.py
```

## Prompt Configuration

The scoring prompt is loaded from `configs/pipeline.toml`.
Examples of expected usage are stored in `configs/scoring_examples.json`.

This makes it easy to swap profiles, for example:
- computational biology applicant
- systems applicant
- NLP applicant
- HCI applicant

without rewriting the scoring code.

## Publishing

Suggested publish flow:

```powershell
git init
git checkout -b codex/generalize-project
git add .
git commit -m "Generalize CS faculty pipeline"
```

Then create a GitHub repo and push:

```powershell
git remote add origin https://github.com/<your-user>/<your-repo>.git
git push -u origin codex/generalize-project
```

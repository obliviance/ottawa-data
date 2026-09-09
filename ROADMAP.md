# Roadmap

A running plan for turning the catalogue into public-facing work on Ottawa governance.
**This file is kept current** — update the status boxes and the log as things move.

## Goal

For every source worth it: fetch → land in one warehouse → auto-profile → surface
candidate questions → ship something public (a cleaned dataset, a visualization, a
finding). Bias toward **joins** and **unconventional angles**, not one-app-per-source.

## Method

**Phase A — reconnaissance sweep** (wide, shallow, scripted). Every source: ingested,
queryable in `warehouse/`, has a `catalog/<id>.md` tearsheet, and ≥2 rows in
`questions/backlog.csv`. A source is "shipped at recon depth" when its cleaned data +
tearsheet land in `releases/`.

**Phase B — deep builds** (narrow, deep, selective). Pick top questions by
`value × novelty × feasibility`; build the public artifact under `apps/` or `releases/`.

**The spine** (`spine/`) comes first within Phase A — `geography`, `timeline`,
`entities`. Every cross-source question joins to one of these.

## Status

### Scaffold
- [x] `warehouse.py` — DuckDB + Parquet + manifest, `register()` / `con()` / CLI
- [x] `ingest/arcgis_hub.py` — DCAT feed → GeoJSON/CSV per dataset
- [x] `ingest/ckan.py` — package_search → CSV/XLSX/GeoJSON resources
- [x] `profile.py` — tearsheet + templated questions
- [x] `questions/backlog.csv` seeded (20 strategic questions)
- [x] folder structure, `.gitignore`, `requirements.txt`, `CLAUDE.md`
- [ ] `ingest/rolling_csv.py` — scheduled append (311, ASE)
- [ ] `ingest/pdf_tables.py` — pdfplumber → tables + text index (escribe, budgets, AG)
- [ ] `ingest/html_scrape.py` scaffold + per-page parsers
- [ ] `ingest/json_api.py` clients (howtheyvoted, devapps, engage-ottawa)
- [ ] one `apps/` layout+palette template; one `releases/` `datapackage.json` template
- [ ] a task runner (`justfile` / `Makefile`) tying ingest → profile → build

### Spine
- [ ] `spine/geography.py` — wards + ONS + DA + address lookup
- [ ] `spine/timeline.py` — Council/committee items + recorded votes
- [ ] `spine/entities.py` — fuzzy-matched actor list across accountability datasets

### Phase A — ingest by shape

| Shape | Sources (catalogue ids) | Ingester | Status |
| --- | --- | --- | --- |
| **ArcGIS Hub** (~690 datasets behind 12 ids) | `open-ottawa` `ops-data-portal` `crime-map` `collisions` `road-network` `trees-parks` `recreation` `fire-paramedic` `election-results-history` `ncc` `riverkeeper` `open311` + `arcgis-rest-root` `geoottawa` `historical-imagery` | `arcgis_hub.py` | ☐ not started |
| **CKAN** | `data-ontario` `open-canada` `fir` (+ `sunshine-list` `statcan-census` live here too) | `ckan.py` | ☐ not started |
| **Rolling CSV** | `automated-speed-enforcement` `open311` | `rolling_csv.py` | ☐ tool not built |
| **JSON API / feed** | `howtheyvoted` `devapps` `engage-ottawa` `escribe` `octranspo-gtfs` `traffic-ottawa` | `json_api.py` | ☐ tool not built |
| **PDF corpus** | `escribe` `budget-documents` `financial-reports` `auditor-general` `drinking-water` `official-plan` | `pdf_tables.py` | ☐ tool not built |
| **HTML scrape** | `candidate-list` `who-is-running` `office-expenses` `lobbyist-registry` `campaign-finance` `bylaws-az` `procurement` `mfippa-disclosure` `committee-of-adjustment` `olt` `council-structure` `zoning-2026-50` `building-permits` `solid-waste` `social-housing-registry` `hydro-ottawa` `school-boards` `police-services-board` `integrity-commissioner` `ottawa-public-health` `housing-homelessness` + third-party (`ottwatch` `ottawa-lookout` `horizon-vote-tracker` `acorn-voting-records` `ateh` `nei` `ons` `ottawa-insights`) | `html_scrape.py` + parsers | ☐ tool not built |
| **Request / manual** (not automatable) | `mpac` `mfippa-disclosure` `community-data-program` `legacy-agendas` `city-archives` | — track only | ☐ |

### Phase B — picked questions

_(move rows here from `questions/backlog.csv` when `status = picked`; link the shipped artifact)_

| id | question | artifact | status |
| --- | --- | --- | --- |
| — | — | — | — |

## Cadence

- Recon target: ~1 source-profile/hour once ingesters exist → the catalogue in ~2 weeks.
- Weekly: re-score `questions/backlog.csv`; run `python3 tools/verify.py --stale 7`.
- Every ingest run: re-run `python3 tools/profile.py --all` and `python3 tools/build_readme.py`.

## Log

- **2026-09-09** — Scaffold built: warehouse (DuckDB), `arcgis_hub.py` + `ckan.py`
  ingesters, `profile.py`, seeded 20-question backlog, folder structure. Smoke-tested
  ingest (ASE cameras, PSSD 2015) and profiling end to end, then reset the warehouse to
  empty. Next: build the three spine tables, then run `arcgis_hub.py` over `open.ottawa.ca`
  in full.

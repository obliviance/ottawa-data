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
- [x] `ingest/rolling_csv.py` — plain-CSV-at-a-URL (311 current + last year)
- [x] `ingest/howtheyvoted.py` — the council voting record → 4 flat tables
- [x] `ingest/arcgis_hub.py` FeatureServer + zip fallback — yields the PH inspection ZIPs;
      the pure-API path is mostly empty police shells (Hub "API-only" entries are apps)
- [x] `tools/sample.py` — landing-page + small-data capture for bespoke sources → `samples/`
- [ ] `ingest/pdf_tables.py` — generic pdfplumber tables + text index (escribe, budgets, AG)
- [ ] per-source HTML parsers — office-expenses, lobbyist registry, campaign finance,
      candidate list, drinking water, school boards (each ~1–4h; see `samples/<id>/README.md`)
- [ ] eScribe document harvest (enumerate meeting → DocumentId, then parse) — its own project
- [ ] one `apps/` layout+palette template; one `releases/` `datapackage.json` template
- [ ] a task runner (`justfile` / `Makefile`) tying ingest → profile → build

### Spine
- [ ] `spine/geography.py` — wards + ONS + DA + address lookup
- [ ] `spine/timeline.py` — Council/committee items + recorded votes
- [ ] `spine/entities.py` — fuzzy-matched actor list across accountability datasets

### Phase A — ingest by shape

| Shape | Sources (catalogue ids) | Ingester | Status |
| --- | --- | --- | --- |
| **ArcGIS Hub** (~690 datasets behind 12 ids) | `open-ottawa` `ops-data-portal` `crime-map` `collisions` `road-network` `trees-parks` `recreation` `fire-paramedic` `election-results-history` `ncc` `riverkeeper` `open311` + `arcgis-rest-root` `geoottawa` `historical-imagery` | `arcgis_hub.py` | ✅ **288 datasets** (open.ottawa 273 · police 11 · riverkeeper 4); ~400 more expose only a GeoServices API — pending |
| **CKAN** | `data-ontario` `open-canada` `fir` (+ `sunshine-list` `statcan-census` live here too) | `ckan.py` | ◐ 4 datasets (PSSD 2013/2015, Ontario funding). **FIR resource on data.ontario.ca is a mislabelled HTML link → use the EFIS portal.** open.canada / statcan: pending targeted queries |
| **Rolling CSV** | `automated-speed-enforcement` `open311` | `rolling_csv.py` | ✅ 311 current (266k) + last year (372k); ASE is on the ArcGIS hub |
| **JSON API / feed** | `howtheyvoted` `devapps` `engage-ottawa` `escribe` `octranspo-gtfs` `traffic-ottawa` | per-source | ◐ **howtheyvoted done** (612 meetings, 7,621 motions, 6,374 recorded votes since 2022). devapps/engage need browser-assisted extraction; escribe/GTFS pending |
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

- **2026-09-09 (scaffold)** — warehouse (DuckDB), `arcgis_hub.py` + `ckan.py`, `profile.py`,
  seeded 20-question backlog, folder structure.

- **2026-09-09 (first sweep)** — added `rolling_csv.py` + `howtheyvoted.py`; hardened the
  warehouse (lock retry, parquet-write fallback) and profiler (bool / mixed-tz columns).
  Ran the ArcGIS hubs, 311, and howtheyvoted:
  - **299 datasets · ~3.0M rows** in the warehouse (179 MB, gitignored)
  - `catalog/` — 299 tearsheets + `INDEX.md`; `questions/backlog.csv` → 187 rows
  - **Council voting record is now data**: `htv_motions` (7,621) + `htv_votes` (6,374
    recorded councillor-votes since 2022) — the #1 catalogue gap.
  - Found `open_2025_contracts_awarded_greater_than_25000_*` — **procurement contract
    awards ARE on Open Ottawa as CSV** (2023+); worth a `procurement` source-tag + a look.
  - Not done: PDF corpus (escribe / budgets / AG), HTML-scrape sources (office-expenses,
    lobbyist registry, campaign finance, procurement), devapps / engage APIs, the spine.

- **2026-09-09 (unblock + sample)** —
  - `arcgis_hub.py` FeatureServer/zip fallback → **public-health inspection data**
    (food safety: 12,932 businesses / 96,157 inspections / 89,419 violations; +personal
    services, child care, drinking water). ~335 → ~355 datasets.
  - **spine built:** `spine_wards` (24 current), `spine_neighbourhoods` (116 ONS),
    `spine_motions` (7,621), `spine_meetings` (2,071 from the eScribe calendar, 2019→).
  - **XHR-mining pass** over 41 government non-portal sources: **only `devapps` and
    `engage-ottawa` have a real backing data API** (both already known). Everything else
    is server-rendered ottawa.ca with no hidden endpoint → confirmed each needs a bespoke
    parser. No shortcut.
  - **`samples/`** — 38 sources: landing-page HTML + a small data sample where reachable
    (`devapps` API → 813 dev-apps, 10 sampled; 2 Auditor General reports as PDF+text;
    `traffic-ottawa/ase_camera`). Each has a `README.md` stating what a full parser needs.
  - Can't sample: `mpac`, `city-archives`, `community-data-program`, `legacy-agendas`,
    `mfippa-disclosure` (all request-only).

  **Next:** Phase B on backlog questions that only need what's landed — q0004 (ASE siting
  equity), q0005 (311 by ward), q0016 (collision hot-spots), q0018 (vote cohesion). Then
  the per-source HTML parsers, prioritised by `questions/backlog.csv` value.

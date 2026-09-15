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
- [x] `ingest/procurement.py` — folds the half-yearly contract-award releases into one
      `procurement_awards` table; discovers new drops by pattern, not a hard-coded list
- [ ] `ingest/pdf_tables.py` — generic pdfplumber tables + text index (escribe, budgets, AG)
- [ ] per-source HTML parsers — office-expenses, lobbyist registry, campaign finance,
      candidate list, drinking water, school boards (each ~1–4h; see `samples/<id>/README.md`)
- [ ] eScribe document harvest (enumerate meeting → DocumentId, then parse) — its own project
- [ ] one `apps/` layout+palette template; one `releases/` `datapackage.json` template
- [ ] a task runner (`justfile` / `Makefile`) tying ingest → profile → build

### Spine
- [x] `spine/geography.py` — `spine_wards` (24) + `spine_neighbourhoods` (116 ONS); DA + address lookup still to do
- [x] `spine/timeline.py` — `spine_meetings` (2,071) + `spine_motions` (7,621)
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

| id | question | artifact | status |
| --- | --- | --- | --- |
| q0018 | recorded-vote cohesion / bloc structure | `apps/council-recorded-votes` + `releases/council-vote-cohesion` · [page](https://claude.ai/code/artifact/b3fad106-63b0-46c7-bbd7-8b72c69fd16c) | **shipped** |
| q0005 | 311 requests by ward | `releases/311-by-ward` | **shipped** (dataset; viz TODO) |
| q0002 | procurement concentration + sole-sourcing | `apps/procurement-concentration` + `releases/procurement-awards` · [page](https://claude.ai/code/artifact/52143ea2-84f9-429a-86e7-12ef898bec33) | **shipped** |
| q0004 | ASE camera siting equity | — | next (needs census-by-ward income) |
| q0016 | collision hot-spots vs traffic calming | — | next |

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

- **2026-09-10 (first Phase B findings)** —
  - **q0018 shipped:** `explorations/vote_cohesion.py` → `releases/council-vote-cohesion/`
    (per-councillor dissent rates + pairwise agreement over 334 recorded divisions) +
    `apps/council-recorded-votes/` (published page). Finding: only ~4% of motions get a
    recorded vote; on those, S. Menard dissents 53% of the time, M. Sutcliffe 10%;
    Darouze↔Menard agree 23%, but council-wide 30% of pairs agree >80% — not sharply
    factional.
  - **q0005 shipped (dataset):** `explorations/requests_311_by_ward.py` →
    `releases/311-by-ward/`. 574k requests; urban wards close in 2–3 days, rural (West
    Carleton-March, Osgoode) in 11–13. Viz still TODO.
  - `apps/council-recorded-votes/index.html` is now the **template** for finding pages
    (Newsreader / Public Sans / IBM Plex Mono, paper+ink+burgundy, 3-state theme).
  - Note: warehouse is gitignored — re-ingest before re-running an exploration
    (`howtheyvoted.py`, `rolling_csv.py --all`, `spine/*.py`, the relevant `arcgis_hub` filters).

- **2026-09-11 (procurement)** —
  - **q0002 shipped:** `tools/ingest/procurement.py` + `explorations/procurement_concentration.py`
    → `releases/procurement-awards/` + `apps/procurement-concentration/`
    ([page](https://claude.ai/code/artifact/52143ea2-84f9-429a-86e7-12ef898bec33)).
  - The nine half-year contract-award releases are **one table with nine different
    column spellings** (`Amount` / `F_Amount_`, `Item` / `Item_` / `Item__`). The
    normaliser maps by pattern so the next drop needs no edit. **5,648 award actions,
    4,714 contracts, 1,620 vendors, $5.97B, 2022 H2 → 2025 H2.**
  - Findings: **18 vendors take half** of the $5.97B (top 50 = 67%); **19% of awards
    are non-competitive** ($911M) and **clause s.22(1)(D) alone is 70% of that** ($633M);
    **$1.48B — a quarter of all value — is added after award** by amendment or extension.
    Envari Energy Solutions is the largest sole-source recipient at $240M, 100%
    non-competitive, under the same clause used for Microsoft licence renewals.
  - Re-scored q0002 feasibility 2 → 4. It was marked low because it looked like it
    needed a scraper; the data was already in the warehouse from the recon sweep.
    **Worth re-checking the other `f2` rows for the same mistake.**
  - Couldn't retrieve the by-law text: ottawa.ca returns 212 bytes to curl and 0
    characters to headless Chromium. Clause letters are therefore counted, not named —
    naming them needs a human to read the by-law.

  **Next:** q0004 (ASE equity — fetch 2021 census-by-ward income via FeatureServer),
  q0016 (collisions), a 311 map; then the per-source HTML parsers by backlog value.
  Before picking, re-score the `f2` backlog rows — q0002 shows the feasibility
  scores were guessed before the sweep landed and may be wrong elsewhere too.

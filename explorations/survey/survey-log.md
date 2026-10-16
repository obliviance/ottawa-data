# Autonomous survey log (branch `survey-scan`, started 2026-10-16)

Status legend: **verified** = re-checked against a second view; **candidate** = seen once, not yet re-checked.

## Pass 1: liveness and rebuild

- **verified** `verify.py` (stage 0-1): 19 machine-readable, 27 reachable HTML, 24 need a browser, 1 blocked, 1 error (72 sources).
- **candidate** Manifest drift: tracked `warehouse/manifest.json` lists 352 datasets; a fresh rebuild with the default ingesters yields 321. The 31 absent come from non-default ingesters (police/riverkeeper hubs, CKAN, elections, devapps sample, spine, derived). Not a bug, but a clone looks "complete" while being unqueryable.
- **candidate** `procurement.py` crashes (CatalogException) when a half-year release is in the manifest but its parquet is absent. It should skip or re-ingest, not die.
- **candidate** First open.ottawa hub pass: 73 dataset failures. By cause: 51 JSONDecodeError (endpoint returned non-JSON: likely HTML/empty), ~17 HTTP 404 (published links that are dead, two with "blob does not exist"), 2 HTTP 400, 1 DNS failure, 1 403, 1 UTF-8 BOM, 1 URL with control characters (a dataset title with illegal characters). The 51 non-JSON cases are systemic and need a closer look.
- **verified** The 51 non-JSON failures are hub items (dashboards, apps, documents such as "Catch Basin Locator Map", "Housing approvals dashboard", "Job Opportunities API") whose DCAT feed lists a distribution labelled "ArcGIS GeoServices REST API" but whose URL is a plain ottawa.ca HTML page. The hub's format label is wrong for these, so any tool trusting it fetches HTML. Hub counts of "datasets with an API" are inflated by this.

## Pass 2: statistical scan of the warehouse (356 datasets; `scan.py` -> `scan.csv`)

Raw flags are mostly noise (234 mostly-null columns, 95 tiny tables, which are lookups and attribute fields). Three survive a second check:

- **CORRECTED (see Pass 3 re-check)** ~~Open Ottawa's "Theft of motor vehicle" is an empty shell.~~ It is not: the hub returned a `"Up to date download file is being generated"` Pending stub on the first CSV request and `arcgis_hub.py` saved the stub as the table. This is an ingester bug, not a source defect.
- **verified** ASE camera-removal monitoring: `Date_of_Data_Collection` is text like "22-Aug" with no year for 605 of 606 rows. It parses as year 0001, so it can't be used as a date without inferring the year from context.
- **CORRECTED** Riverkeeper PFAS: same stub cause. A re-fetch today returns real data (12.6 KB CSV; batch 4 counted 31 rows, layer edited 2026-09-22).

Not yet done: per-source reading of the 72 catalogued sources and the uncatalogued `hierarchy.md` branches (pass 3), and a second-view check of the remaining pass-1 candidates.

## Pass 3: per-source sampling (6 parallel agents, 72 sources; full reports in `pass3/batch1-6.md`)

Re-checked by me against a second view (**verified**): OttWatch is live again (`/` 200, RSS 200), so the 2026-09-15 "502" note is stale; Forestry tree inventory has 304,207 points and is not in the warehouse; `app06.ottawa.ca/cgi-bin/docs.pl` 302-redirects into ottawa.ca (legacy-agendas retired as an html source); the Hub CSV-stub bug above (both empty parquets contain the stub text). ONS `get-data/neighbourhoods` returns data (shape not yet examined).

Cross-cutting findings (each backed by multiple batch reports; individual claims are marked verified/candidate inside the batch files):
- **ottawa.ca sits behind an Imperva/Incapsula bot challenge.** curl gets a ~1 KB shell with HTTP 200, so `verify.py` stage 0 reports false liveness (`reachable_html`, 212-byte body). Only stage 2 (Chromium) reads those pages. Affects city-archives, housing-homelessness, drinking-water, solid-waste, office-expenses, bylaws-az, budget-documents and others.
- **Catalogue tags/URLs have drifted** (examples): election-results-history (results are xlsx/pdf documents, only ward geometry has an API), arcgis-rest-root (MapServer, no FeatureServer), crime-map (stale mirror, live layer elsewhere), road-network (URL points at a parks layer), zoning (retired 2008-250 service), official-plan (has an 89-layer MapServer, tagged html), open311 (`api` dead, only 2 CSVs), statcan-census (page blocked, WDS API works), open-canada (CKAN API works), nei (has bulk CSV/XLSX), opl (data on Open Ottawa), FIR (CKAN resource is an HTML index; real data is yearly zips on EFIS), OPH (URL 404).
- **Large unlanded data**: OPS portal (98 items; criminal offences 344k, calls for service 1.1M, traffic stops 456k rows), tree inventory (304k), ONS indicator API (884 rows x 116 neighbourhoods), devapps MapServer (3,455 vs 775 via keyed API), Sunshine List 2021-25 (on ontario.ca, not CKAN).
- **Notable real-world facts**: all automated speed cameras were deactivated 2025-11-13 (Bill 56); howtheyvoted per-councillor votes cover ~4.5% of motions; eScribe meeting index reaches back to 2012 (our spine starts 2018); lobbyist registry is scrapable with plain POSTs back to 2012.
- **Delay evidence** is current-state only (traffic closures with planned dates, devapps status dates, a rolling-month GTFS zip, OLT cases); nothing archived. Planned-vs-actual would need scheduled snapshots.

## Pass 4: uncatalogued `hierarchy.md` branches (211 rows, 4 agents; reports in `pass4/probe1-4.md`)

`hierarchy.md` lists bodies by name only, so agents had to locate each site. Blocker: every ottawa.ca path returns an Incapsula shell (HTTP 200, ~1 KB), so ~40 ottawa.ca-hosted rows, plus Cloudflare/Radware-walled sites (OSTA, CLC, IPC, Ombudsman, CRTC, BAnQ, Archives of Ontario, Crime Prevention Ottawa), are unverifiable without a browser (stage 2). Probe 4 and parts of probe 1 used guessed URLs, so their "did not resolve" results are candidates, not confirmed dead sites.

**Re-checked against the Open Ottawa DCAT feed (verified):** red-light camera locations + violations datasets exist (13 titles; CSV + GeoServices) -> row marked "unknown" is wrong, should be open; City Council Meeting Attendance 2022-2026, Ontario Works Caseload 2020-2025, Tree Equity Score 2025 (4 areas), Midblock Volumes 2022-2025, Pay and Display Machines all exist as CSV. No speed-limit / school-zone / community-safety-zone layers exist in the feed (row 44's open status is unsupported; layers may be on maps.ottawa.ca, unchecked). Public-health inspection data: `opendata.ottawa.ca/inspections/*.zip` serves curl a "Pardon Our Interruption" challenge page, **but the data did land in the rebuild** (child care, camps, etc. registered), so it is obtainable; the probe's "could not download" was wrong in practice.

**Candidate status changes (not applied to `hierarchy.md` yet):**
- Closed/unknown -> open/partial: contract awards (delegation-of-authority, city + transit, plus semi-annual >$25k), red-light cameras, Ontario Works caseload, GHG inventory, tree inventory, municipal drains / former landfills / village + agriculture boundaries (maps.ottawa.ca layers), Election Compliance Audit Committee (eScribe meetings + OttWatch RSS), federal MP constituency offices (ourcommons.ca directory).
- Open -> downgrade pending browser check: BAnQ, Archives of Ontario (captcha pages only), Bike Ottawa (no dataset endpoint found), speed-limit/school-zone layers.
- Moved: Canada Lands Company -> `clcl-sicl.ca`; RCMP -> `rcmp.ca`; Carleton CURVE -> `carleton.scholaris.ca`; Labour Council -> `ottawalabour.labourcouncils.ca`; LECA at apex `leca.ca`; OCH Foundation -> `ochfoundation.ca`. Possibly gone (search-based, unprobed): Pineview golf (privately owned), OCLDC (rebranding to "Build Ottawa").
- New machine-readable leads: Tribunals Ontario, Public Health Ontario and EQAO open-data pages (links seen, not fetched); Ontario CKAN `school-information-and-student-demographics` (`package_show` returned success); university repositories (RUOR, Scholaris) with DSpace APIs; CBC Ottawa RSS.
- Four sites unresolved on guessed domains (People's Official Plan, Poverty Reduction Network, Ottawa Community Foundation, CUPE 503): need a real search, not a guess.

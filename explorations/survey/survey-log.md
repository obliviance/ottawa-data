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

- **verified** Open Ottawa's "Theft of motor vehicle" is an empty shell (0 rows). The same data is on the police hub (`ops_theft_of_motor_vehicle_open_data`, 11,720 rows). Anyone using the city portal's entry gets nothing.
- **verified** ASE camera-removal monitoring: `Date_of_Data_Collection` is text like "22-Aug" with no year for 605 of 606 rows. It parses as year 0001, so it can't be used as a date without inferring the year from context.
- **candidate** Riverkeeper PFAS dataset returned 0 rows this run, while the committed manifest records 23 rows from an earlier run. Either the source changed or the endpoint is flaky. Needs a re-pull to tell which.

Not yet done: per-source reading of the 72 catalogued sources and the uncatalogued `hierarchy.md` branches (pass 3), and a second-view check of the remaining pass-1 candidates.

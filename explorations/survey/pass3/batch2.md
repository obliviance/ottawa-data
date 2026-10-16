# Pass 3, batch 2: governance / accountability / finance sources

Probed 2026-10-16 (about 14:15-14:30 UTC) with `curl -m 30`, UA `ottawa-data/0.1 survey`, >=2 s between requests. Downloads kept under the scratchpad `b2/` dir, never executed. Read-only: no repo file touched except this one.

**verified** = checked two independent ways. **candidate** = seen once.

## Cross-cutting finding: ottawa.ca is behind an Imperva/Incapsula bot challenge

Plain `curl` (and `tools/_http.py`-style fetchers) get **HTTP 200 with a ~212-1160 byte challenge shell** from every ottawa.ca page in this batch (bylaws-az, council-structure, integrity-commissioner, office-expenses, financial-reports, budget-documents, both mfippa URLs, forms.ottawa.ca). Body is `<script src="/_Incapsula_Resource?...">` plus a decoy script path, no content. Wayback's capture of the office-expenses landing page (20260909152059) is the same 212-byte shell. **verified** (curl on 8 URLs; Wayback copy; `verification.json` byte counts 1155-1163 for the same URLs).

- `verification/verification.json` records these as `outcome: needs_browser`, `kind: spa`. They are not SPAs; they are bot-challenge pages, so "needs_browser" is right in effect but the label "spa" and the 200 "reachable" status overstate liveness for any non-browser consumer.
- Consequence: every ottawa.ca-hosted source in this batch is only readable through stage 2 (headless Chromium) or Wayback captures. The `html_scrape.py` plan in ROADMAP will need a browser, not `urllib`. **candidate** (not tried a browser UA, deliberately, to avoid evading the control; no Chromium in this sandbox).
- Liveness verdicts for ottawa.ca pages below therefore lean on the stage-2 record (2026-10-16 render, real content) and are marked accordingly.
- `lobbyist.ottawa.ca` is also Imperva-fronted (visid_incap cookies) but served real content to curl.

---

### bylaws-az
**LIVE** (per stage 2 only; curl gets challenge shell). Access tag: **matches** (html).
- **tag-fix / anomaly** (verified): stage 0 listed it `needs_browser/spa`; actual cause is Incapsula, see above. Stage-2 render (title "By-law A-Z | City of Ottawa", 5,697 chars) is real content.
- **anomaly** (candidate): the page's own text says it lists "the by-laws most frequently requested by the public... Persons seeking by-laws not on ottawa.ca are asked to contact the City Clerk via 311". So it is a curated subset, not a complete consolidated register. The sources.json description "Consolidated by-laws in HTML" overstates completeness. Stage-2 sample (first 1,500 chars only) confirms entries like "Auditor General (By-law No. 2021-5)", "Access (By-law No. 2026-139)", "Borrowing ... $220,000,000 (By-law No. 2025-357)", i.e. current through 2026. I could not confirm the description's examples (Procurement 2000-50, Zoning 2026-50, Lobbyist) because the stored sample is truncated and live fetch is blocked.
- **unique**: nothing notable beyond the by-law texts themselves (no machine-readable list; by-law numbers only appear inside link text).

### documents-repo
**LIVE**. Access tag: **matches** (html). Probed `https://documents.ottawa.ca/` (200, 101,481 bytes, Drupal 7 per `X-Generator`), `/robots.txt` (200), a file URL, a search URL.
- **anomaly** (verified, two ways): the home page is just a "latest 150 files" list (150 `/en/files/` links), currently led by a Carling/Churchill LRT corridor evaluation set; the site's own search form posts to `https://ottawa.ca/en/search` (Swiftype), i.e. the repository has **no search of its own** and the search sits behind the Incapsula-protected host. `/en/search?search_api_fulltext=budget` on documents.ottawa.ca is a 404.
- **anomaly** (candidate): file links are `/en/files/<slug>pdf` and `HEAD /en/files/aboutthisstudypdf` returned `200 text/html` (a Drupal node wrapper page, not the PDF). So URLs do not resolve straight to documents; a scraper must follow one more hop.
- **anomaly** (verified): `robots.txt` sets `Crawl-delay: 10`. The repo's 2 s politeness floor is below the site's declared delay; any ingester for this host should use >=10 s.
- sources.json description ("where most linked PDFs live") is plausible, unverifiable at scale. Nothing unique found.

### council-structure
**LIVE** (stage-2 render; curl blocked). Access tag: **matches** (html).
- **anomaly** (verified): same Incapsula issue. Stage-2 render (1,446 chars) shows a menu page only: Standing committees, Advisory committees, Adjudicative bodies, Boards, "Council sponsors groups and liaisons", "Councillor orientation sessions". The page itself holds **no membership, mandates or terms of reference**; those are on child pages. The description ("Membership, mandates and terms of reference...") describes the subtree, not the URL catalogued.
- **unique**: nothing notable at this URL. (Council membership and votes already come from `htv_*` / `spine_*` in the warehouse.)

### auditor-general
**LIVE**. Access tag: **matches** (html), but see PDF note. Probed home, `/reports/audit-reports/` (200, 121 KB), `/news/`, `/robots.txt`, `/sitemap.xml` (200 `text/xml`).
- **anomaly** (verified): the site is an Umbraco build and **PDFs are served from a third-party CDN**, `media-002-ca.cdn.govstack.com/oagottawa-010-ca/media/<id>/<file>.pdf`, not from oagottawa.ca or ottawa.ca. Home links and audit-reports page both use it (86 `.pdf` hrefs on the audit-reports page). URLs are opaque media ids; link rot risk if the vendor changes. Good candidates for Wayback snapshots.
- **verified**: freshness. Audit-reports page lists 2026 tabling dates 30 Apr, 12 May, 19 Jun 2026 and 2025 dates incl. "Tabled on November 28, 2025 - Council Expense Audit", matching the description's "November 2025". No report tabled after 19 Jun 2026 as of today (Oct 16); likely the normal summer gap, not staleness. Machine-discoverable via `https://www.oagottawa.ca/sitemap.xml` (robots points to `/sitemap-xml/`), which the catalogue does not mention.
- **unique**: Fraud & Waste Hotline annual report, semi-annual follow-up reports, an investigation report (OC Transpo recruitment and staffing), annual workplan 2026-2027. Follow-up tables of recommendation status are not elsewhere.
- Description says "Standalone site, separate from ottawa.ca": **verified** (own host, own CMS, own CDN).

### integrity-commissioner
**LIVE** (stage-2 render; curl blocked). Access tag: **matches** (html).
- **anomaly** (verified): stage 2 shows the catalogued URL **redirects to `.../integrity-commissioner/integrity-commissioner-law-no-2021-7`** (title "Integrity Commissioner (By-law No. 2021-7)"). Harmless but the canonical URL changed; consider recording the redirect target.
- **unique** (candidate): submenu includes **"Gifts Registry"**, "Reports and bulletins", "Codes of conduct and related resources". The Gifts Registry (members' disclosed gifts) is not mentioned in sources.json or, as far as this batch shows, anywhere else in the catalogue. Worth a dedicated entry. Could not open the sub-pages (challenge).
- **anomaly** (candidate): the page text says the IC "is one of three statutory officers ... along with the City Manager and Auditor General". The description's "three mandates, one office" (IC + Lobbyist Registrar + Meetings Investigator) is a different "three"; I could not verify it from the rendered sample (cut off at 1,500 chars for the remaining text).

### lobbyist-registry
**LIVE and fresh**. Access tag: **differs / needs nuance**: tagged html. It is a server-side ASP.NET WebForms search (viewstate POST), no JSON API, so `html` is right, but results are scriptable without a browser, unlike ottawa.ca.
- **verified** (curl x6, two different searches): `https://lobbyist.ottawa.ca/search/searchlobbyist.aspx?lang=en` returns 200 with real content to curl. POST (viewstate + `__EVENTVALIDATION` + session cookie) with `txtKeyword=development` returned **875 records, 88 pages** (`lbRecordCount`, `lbPageCount`; page size 10/25/50 selectable). A POST with `dpFromDate_txtbox=01-Jan-2026` returned **139 records**, latest activity dates **30-Sep-2026**. So data runs to within 2 weeks of today.
- **verified**: coverage back to at least 01-Oct-2012 (rows dated 01-Oct-2012, 13-Sep-2012, 22-Jan-2013 in results), consistent with "in force since 1 September 2012".
- **unique**: a "Get All Lobbyists (PDF)..." button (`ButtonGetAll`) suggests a bulk list. My one POST with it returned the same HTML page (34,971 bytes, `text/html`), not a PDF: **candidate** that it needs the full client-side postback flow or a different session state. Worth a browser test.
- **anomaly** (verified): the "Persons Lobbied" column is a concatenation of every contact across a multi-meeting record, with duplicates (one 2013 record lists "Darouze, George - Councillor, Ward 20" ~12 times) and inconsistent case ("hume, Peter E", "smit, john"). Name normalisation needed before joining to `spine_*`/`htv_councillors`.
- **anomaly** (verified): default result order is not chronological (a 2025 Google Cloud/AI introductory meeting sits between 2012-2013 rows); subject matter is a controlled list (Affordable Housing, Planning and Development, Information Technology...); some activity text is truncated with "..." in the grid, full text only on the detail postback.
- **tag-fix** (candidate): note in sources.json that search is scrapable with plain HTTP (viewstate) and the home page is `https://lobbyist.ottawa.ca/` with a separate login at `/Account/Default.aspx`. Both URLs already listed.
- Description "Public search requires no login": **verified**.

### mfippa-disclosure
**DEGRADED for verification (cannot read)**, not dead. Access tag: **matches** (html + request).
- **anomaly** (verified): both catalogued URLs return the Incapsula shell (1,154 and 5,548 bytes; the 5,548 one is the forms.ottawa.ca shell with a decoy `src=` path). Wayback has **no snapshot** at all of the `general-information` URL (availability API returned `{}`).
- **anomaly** (verified): this is the **only source in the batch with no stage-2 record**: `verification_stage2.json` has 41 source keys and `mfippa-disclosure` is not among them (also absent: fir, which is fine as it is CKAN). So the description ("Quarterly list of completed FOI requests... quote the request number to mfippa@ottawa.ca") has never been confirmed against a rendered page. Treat the description as **candidate**.
- stage 3 marks it `unconfirmed (Request / FOI)`, which is correct. Nothing unique can be asserted.

### office-expenses
**LIVE** (via stage 2 and Wayback structure; curl blocked). Access tag: **matches** (html), though it holds far more structure than "html" implies.
- **anomaly** (verified): stage 2 captured the landing page at `...disclosure-office-expenses?page=3035385` (a bogus pager query appended by redirect) with only 767 chars of rendered text: the menu ("2022-2026 Term of Council", "2018-2022 Term of Council", "About the disclosure...") and **no data**. The catalogued URL is an index; the data is on per-member subpages.
- **verified** (Wayback CDX listing plus one captured member page): structure is `/disclosure-office-expenses/<term>/<member>-ward-N-disclosure-office-expenses-<term>`, terms **2010-2014, 2014-2018, 2018-2022, 2022-2026**. One member-month page (Jenna Sudds, Ward 4, Wayback 20230127) has **105 HTML tables**: a "summarized" table (Special Events/Hospitality, Donations and Sponsorships, Memberships, Business Travel, Constituent Communications, External Services, Materials, Staff Costs; Month Actuals and Year to Date) and an **"itemized" table with free-text line items** (e.g. "Sponsorship: The Ottawa Mission - 'Feed the Hungry' - Feb. 12, 2021", $63).
- **unique**: itemised free-text expense lines per member, back to 2010. This is the only per-line councillor spending source; it is HTML-only, no CSV, and is probably the best scrape target in the batch for the `spine` councillor join. The Auditor General's "Council Expense Audit" (tabled 28 Nov 2025) is the natural cross-check.
- **candidate**: description's "$284,648 per ward councillor in 2023; Mayor's $970,646" could not be re-checked (blocked).

### sunshine-list
**LIVE**. Access tag: **bulk, matches, but the home of the bulk data differs by year.**
- **tag-fix** (verified, two ways: CKAN `package_search` and `pssdfiles.json`): **data.ontario.ca CKAN holds only 1996-2020** (25 datasets `public-sector-salary-disclosure-<year>`, last modified 2023-07-03 to 2023-12-11). **2021-2025 are not on CKAN**; they are on ontario.ca itself via an artefact manifest `https://www.ontario.ca/public-sector-salary-disclosure_artifacts/pssdfiles.json` (200, 15 KB) with per-year, per-language CSV/JSON/ODS for Compendium, Addendum and NoSalary. So a CKAN-only ingester (current `ckan.py`) silently stops at 2020.
- **verified**: 2025 compendium CSV downloaded (`.../2025/Compendium/b0f64c65-.../tbs-pssd-compendium-salary-disclosed-2025-en-utf-8-2026-03-23.csv`, 200, 48.7 MB). **404,922 rows**, 8 columns `Sector,Last Name,First Name,Salary,Benefits,Employer,Job Title,Year`. City Of Ottawa = **5,181 rows** (salary $100,008-$455,234, median ~$117.6k).
- **unique**: the list covers far more of Ottawa than "city employees": City Of Ottawa 5,181; **City Of Ottawa - Police Services 1,779; Library Services 29**; Ottawa Community Housing Corporation 124; Ottawa-Carleton DSB 3,847; Ottawa Catholic SB 2,495; The Ottawa Hospital 3,195; University of Ottawa 2,861; CHEO 1,064; Invest Ottawa 23 (all 2025, `Employer` contains "Ottawa"). The description undersells this; police and OCH are otherwise opaque.
- **anomaly** (verified): the dated filenames show re-issues: 2024 files are stamped 2026-01-27/29/30 (a year after the original 2025 publication), 2023 compendium 2025-03-26 vs addendum 2025-01-13. Addenda ("changes, additions and deletions") exist for 2021-2024, so any year's compendium must be merged with its addendum. The 2021 French compendium lacks a CSV (only JSON/ODS).
- **anomaly** (candidate): page says "Updated: May 04, 2026" and lists 2025 data, so the Province publishes ~Mar each year. The 2025-employer names are title-cased ("City Of Ottawa") while older datasets use different casing, so employer joins across years need normalising.
- Warehouse (**verified**): `warehouse/manifest.json` lists `ontario_public_sector_salary_disclosure_2013` (97,916 rows) and `_2015` (115,920 rows) under `sunshine-list`, but **no matching parquet file and no table in `ottawa.duckdb`** (358 tables, none containing "salary"). Same manifest-vs-rebuild drift already noted in survey-log pass 1. Catalog tearsheets exist for both years.

### financial-reports
**LIVE** (stage 2; curl blocked). Access tag: **matches** (html).
- **anomaly** (verified): catalogued URL redirects (stage 2) to `.../financial-reports-and-statements/operating-and-capital-budget-status-reports`; the rendered page is the Q1/Q2 status report page with a sidebar: Annual Year end disposition reports, Annual Financial statements, Annual reports, Long range Financial Plans, Credit Ratings, Fiscal Framework 2007. Description matches that structure.
- **anomaly** (candidate): the budget-documents landing page (below) says "Annual reports from 2024, 2023, 2022, 2021, 2020", consistent with the description's "2020 to 2024 online". As of Oct 2026 no 2025 annual report is listed, plausible (typically tabled mid-year) but worth watching.
- **unique**: quarterly budget-vs-actual by department (Q1/Q2 only on this page, so a 2-of-4 quarter series). Warehouse has `open_budget_2020_capital_status_report_q1` (800 rows) as the only landed relative. Nothing else unique.

### budget-documents
**LIVE** (stage 2). Access tag: **differs: `bulk` is unconfirmed, probably wrong for this URL.**
- **tag-fix** (verified: stage 3 says "unconfirmed - page is HTML; claimed bulk needs a manual check", and the stage-2 render of the landing page has no tables or data links): the page is a menu: "Budget 2026", "Previous Budgets: Budget 2025, 2024, 2023, 2022", annual reports, funding, tax policy. No CSV/XLS here. The `bulk` part rests on the description's "some budget data mirrored to Open Ottawa", which is a different host (the `open_budget_*` datasets in the warehouse). Suggest tagging this URL `html` and putting the Open Ottawa budget datasets under their own entry, or noting `bulk` applies only to the mirror.
- Description "Tabled and adopted budgets, 2022 onward": **verified** (previous budgets 2022-2025, current 2026 on the page).
- **unique**: nothing notable.

### fir
**LIVE**. Access tag `api, bulk`: **differs in practice: the "api" is metadata-only and the datastore is corrupted; real data is bulk ZIPs on EFIS.**
- **anomaly** (verified, two ways): CKAN `package_show` (200) lists a single resource, format `CSV`, URL `https://efis.fma.csc.gov.on.ca/fir/MultiYearReport/MYCIndex.html`: that URL is an **HTML index page**, not a CSV. And `datastore_active: true` on it: `datastore_search?resource_id=0ba84d5e-1532-4c79-8a7f-ad7609a93013&limit=1` returns a record `{"<!DOCTYPE html>": "<html lang=\"en-CA\">"}`, i.e. the Ontario datastore ingested the HTML page as a one-column table. So CKAN "API v2.9.7" works as metadata but there is no queryable FIR data. This matches the ROADMAP note ("mislabelled HTML link"), but the datastore corruption is new detail. The dataset metadata was last modified **2022-12-05** and declares `update_frequency: daily`: stale metadata on live data.
- **verified**: the real bulk surface is `https://efis.fma.csc.gov.on.ca/fir/MultiYearReport/fir_data_<year>.zip`, **2000-2025** (26 zips; the index page lists "Last Updated" per year: 2025 = 20261015, 2024 = 20261015, 2023 = 20261008, 2022 = 20261015, 2021 = 20260921, 2020 = 20260226). `HEAD fir_data_2025.zip` = 200, 8,034,089 bytes, `Last-Modified: Fri, 16 Oct 2026 00:35:38 GMT` (modified today). Downloaded: contains one 143.5 MB CSV, **495,334 rows, 317 municipalities**, 18 columns, **long format** (`MARSYEAR, MUNICIPALITY_DESC, MUNID, SCHEDULE_DESC, SUB_SCHEDULE_DESC, SCHEDULE_LINE_DESC, SCHEDULE_COLUMN_DESC, SLC, DATATYPE_DESC, AMOUNT, VALUE_TEXT`, latin-1 encoded). Ottawa = `Ottawa C`, MUNID 6005, **2,991 rows**, `LAST_UPDATE_DATE` 20260729.
- **tag-fix**: description says "Data back to 1977"; the zips on the CSV page start at **2000**. 1977-1999 are not in this bulk set (candidate: other EFIS reports may hold them; not checked). Also the 2025 return is already online, so "filed by 31 May" data is ~5 months old.
- **anomaly** (candidate): a few `LAST_UPDATE_DATE` values in the 2025 file range 20260323-20261015, so rows are revised in place; a snapshot date must be stored with any pull.
- Also, EFIS is a WordPress site with a `wp-json` endpoint (`/fir/index.php/wp-json/`): not tested, irrelevant to data.
- Warehouse: nothing landed for FIR (no `fir*` parquet).

---

## Three most interesting findings

1. **ottawa.ca serves an Incapsula bot challenge (HTTP 200, ~1 KB) to non-browser clients**, so eight sources in this batch are unreadable to the repo's own fetch helpers, and stage 0 mislabels them as `spa`/needs_browser. The planned `html_scrape.py` must use a browser, and Wayback also stores only the shell. `mfippa-disclosure` has never been rendered at all (no stage-2 record, no Wayback copy).
2. **The Sunshine List is split across two hosts by year**: CKAN (data.ontario.ca) has only 1996-2020, while 2021-2025 (404,922 rows for 2025, 5,181 City of Ottawa plus 1,779 police, 124 OCH, school boards, hospitals, uOttawa) are only on ontario.ca via `pssdfiles.json`, with re-issued files and addenda. The warehouse manifest lists 2013/2015 tables whose parquet files do not exist.
3. **FIR's "api" is hollow**: the CKAN datastore ingested an HTML page as its only resource, while the real multi-year CSV zips (2000-2025, 2025 modified today, Ottawa 2,991 rows in long format) sit on EFIS. Runner-ups: the Lobbyist Registry is fresh to 30-Sep-2026 and scrapable with plain HTTP (875 hits for "development", 139 records in 2026); per-member itemised office-expense pages back to 2010 and the Integrity Commissioner's Gifts Registry are uncatalogued uniques.

# Pass 3, batch 5: live reconnaissance (2026-10-16)

Sources: conservation-authorities, hydro-ottawa, trees-parks, open311, engage-ottawa, opl, recreation, ons, nei, community-data-program, statcan-census, ottawa-insights.
Method: one request at a time, >=2 s between requests per host, curl -m 30, downloads kept in scratchpad only. **verified** = confirmed two independent ways (e.g. live probe plus warehouse/verification record); **candidate** = seen once.

### conservation-authorities
**LIVE.** Access tag `html, bulk`: **differs** (should add `api`; bulk is real).
- **unique** RVCA runs its own open-data catalogue (JKAN on GitHub Pages) at https://rvcagis.github.io/jkan/ (200); the repo `rvcagis/jkan/_datasets` lists 34 dataset records (GitHub API 200). Includes Regulation Limit Approved (O.Reg 174/06 hazard extent, "Last Update 05-29-2026"), flood-risk hazard mapping, catchments, landcover, woodlands, regulated wetlands. **verified**: shapefile https://gis.rvca.ca/openData/regulationLimit_ApprovedSHP.zip returns 200, 10,475,508 B, Last-Modified 2026-10-15; ArcGIS REST .../RVCA_Hazards_publicService/MapServer/6 returns count 503 features (ArcGIS 11.5).
- **tag-fix** add `api` (ArcGIS REST, verified above) to the tag. Stage 3 verdict "unconfirmed bulk" is wrong; the stage-0 `data.json` DCAT probe at rvca.ca was the wrong place to look. **verified**
- **anomaly** sources.json `urls` are the three homepages only; the data entry points (gis.rvca.ca/geoportal, rvcagis.github.io/jkan) are not listed. **verified**
- **anomaly** MVCA (mvc.on.ca, WordPress, `/wp-json/` 200, 2,742 media items, newest page modified 2026-10-14) publishes floodplain/report-card content mostly as PDFs and an ArcGIS Experience; media sample (100 items) was PDF/JPEG/PNG only, no data files. SNC (nation.on.ca, IIS) has "Natural Hazard Mapping" via an ArcGIS Online web viewer only; no download found. **candidate**
- **anomaly** Open Ottawa DCAT record "South Nation Conservation Authority Online Geoportal" has the unrendered description `{{description}}`. **candidate**
- **anomaly** www.rvca.ca/wp-json/ is 404 (not WordPress); MVCA is WordPress. **verified**

### hydro-ottawa
**LIVE.** Tag `html`: **matches**.
- **anomaly** the outage map is not on the catalogued URL. https://hydroottawa.com/ redirects to /en; /en/outages/outage-map is 404. The live map is https://outages.hydroottawa.com/ (200, 1.8 KB shell, "Hydro Ottawa Outage Map", loads Kubra product 5.54.1 scripts), i.e. a Kubra StormCenter SPA that almost certainly reads JSON feeds. Feed not probed. **candidate** (feed existence unverified)
- **anomaly** no open-data page found on the site (homepage links scanned for open-data/reliability; none). Matches sources.json note. **candidate**
- Nothing else notable.

### trees-parks
**LIVE.** Tag `api, bulk`: **matches**.
- **unique** Tree Inventory is a live point layer: https://maps.ottawa.ca/arcgis/rest/services/Forestry/MapServer/0 returns count 304,207 (ArcGIS 10.81, maxRecordCount 1000); newest MODIFYDATE seen is 2026-10-15. Fields include species, DBH, plant date, ownership, park, ward, problem entry, trunk structure. Not in the warehouse (no tree-inventory parquet). **verified** (REST + DCAT record "Tree Inventory", modified 2026-03-27 pointing at that layer; note DCAT date is stale vs. data date)
- **unique** same Forestry MapServer carries layers not obviously in the hub list: Tree Protection Bylaw boundaries (ids 3-7, "effective Jan 1 2021, amended Feb 1 2024"), Ash and Elm injection programmes (10,12,13), "Groups of trees" (1), Potential Hazardous Forest Types for Wildland Fire (8), Tree Equity Score 2025 (19-24). **candidate** (layer list read once; not queried)
- **anomaly** description says "forest cover"; DCAT has Tree Canopy Cover 2017 and 2022 as maps/web-app items (modified 2025-11-19), not downloadable tables. Tree Equity Score 2025 (4 transects) and Tree Protection Bylaw permit statistics 2021-2025 are landed or listed. **candidate**
- 311 requests include forestry work orders (e.g. "Forestry - Determine Tree Health") in the Open311 CSV; complements the inventory. **candidate**
- Warehouse landed: open_parks_and_greenspace (1,374 rows), open_other_park_features (645), open_skateboard_parks (32), open_tree_equity_score_2025_* (20/47/69/80).

### open311
**LIVE.** Tag `api, bulk`: **differs** (should be `bulk` only now; GeoReport v2 API is gone as the description itself says).
- **tag-fix** drop `api`: the only live surface is two Azure Blob CSVs. **verified** (description says so; curl GET of currentyear CSV 200, 48,899,669 B, ~303k lines; lastyear CSV HEAD 200, 59,182,894 B, Last-Modified 2026-10-16 05:38 GMT, i.e. refreshed today). The DCAT feed lists the blob URLs under distribution type "ArcGIS GeoService" (mislabel). **verified**
- **anomaly** location is mostly absent: in warehouse 311-current (303,160 rows, 2026-01-01..2026-10-16) 252,222 rows (83%) have `\N` latitude/longitude; in 311-lastyear (372,069 rows, 2025) 315,838 (85%). Ward is `\N` for 33,751 (11%) / 36,879 (10%) rows. **verified** (warehouse counts and raw CSV head show `\N`).
- **anomaly** last year's file is not closed out: 7,465 of 372,069 2025 requests are still "Active" (2%), 5,808 Cancelled. Current year: 24,151 Active, 3,852 Cancelled. **verified** (warehouse)
- **anomaly** the file has bilingual `English | French` concatenated headers and descriptions ("Type | Type"); only 11-12 distinct `Type` values (department-level), which is what the description calls "responsible department". Channels: Web 153,714, Dispatch 120,784, Data In 21,117, Walk-In 3,626, Email 2,009, Phone 1,801, Voice In 108, Counter 1. **verified**
- **anomaly** DCAT `modified` for "Current Year Service Requests" is 2026-04-01 and for "Previous Year" 2025-04-03 though the blob changes daily; do not use DCAT dates for freshness. **verified** (HEAD vs DCAT)
- **unique** per-year archives: DCAT lists 2013-2022 "Monthly Service Requests" (2022 modified 2025-08-25), "2023/2024 Service Requests", and quarterly 2012 volumes. Not landed. **candidate**
- No 2025 "archive" entry (2025 lives in lastyear file only until rotation on 2027-01-01). **candidate**

### engage-ottawa
**DEGRADED** (site live; documented API not reproducible with plain HTTP). Tag `api, html`: **differs** (api unconfirmed; html only from curl).
- **anomaly** every `https://engage.ottawa.ca/api/v2/*` URL I tried returns 404 with an empty body: /site/, /projects?per_page=..., /home_page_revisions?... (same ones stage 2 saw in-browser). Retried with browser UA, Accept: application/json, X-Requested-With, Referer, session cookies (`_engagementhq_v3`, `X-CSRF-Token`, `_ehq_uid`) and the CSRF meta token: still 404 (content-type switches to application/json). So the API is gated by something a headless fetch did not satisfy. **verified** (4 variants, 8 requests)
- **tag-fix** until reproducible by curl, tag should be `html` (+ note "api/v2 seen only in browser XHR"). **candidate**
- **unique** the HTML at https://engage.ottawa.ca/projects (200, 423 KB) lists every project server-side: 496 project links, `data-state` published 349 and archived 147. That is the scrapable index; /sitemap.xml returns an empty `<hash></hash>`. **verified** (two greps of the page; counts consistent: 488 distinct slugs)
- Platform is EngagementHQ (page string match). Licence "OGL-Ottawa" in stage 3 is inherited from the city and is not stated on this site. **candidate**

### opl
**LIVE.** Tag `html`: **differs** (the operational data is api/bulk, on Open Ottawa).
- **tag-fix** add `api, bulk` (via open.ottawa.ca): warehouse already holds Library Loans Physical Circulation 2020-2025 (~1,070-1,140 rows/yr by branch/collection), Most Requested Titles 2022-2025 (57k-135k rows), Locations 2023/2024 (34 rows, with census geography codes), Bookmobile Stops 2023/24, Service Areas (32), 1-year active cardholders by ONS neighbourhood (116). **verified** (DCAT + landed parquet)
- **anomaly** the catalogued URL https://collections.biblioottawalibrary.ca/ redirects to /en/we-recommend (a BiblioCommons reading-lists page); it is the collections site, not the corporate site. The library home is https://about.biblioottawalibrary.ca/en (redirect from biblioottawalibrary.ca). I found no open-data or stats page there (/en/about-us/open-data 404; only /en/annual-reports). **verified**
- **unique** "Library Programs and Events Feed" (DCAT, modified 2026-07-29) and cardholders-by-ONS-neighbourhood are rare resident-activity measures keyed to neighbourhood. **candidate** (Programs feed not fetched)
- sources.json says "curated local-statistics guides"; none found on the catalogued host. **candidate**

### recreation
**LIVE.** Tag `api, bulk`: **matches** for facilities; description overreaches.
- **verified** City_Facilities MapServer layer 5 "Recreation" count 371 (live) vs 369 landed in open_city_facilities_for_recreation_activities (hub snapshot); also Outdoor Pools (11), Wading Pools (53), Splash Pads, Sports Fields (modified 2026-10-16), Skateboard Parks (32, modified 2026-10-16), Pathway Links (modified 2026-10-16), Beaches/Beach Water Sampling (2026-08-27).
- **anomaly** "programme registration data" is not on the hub: I found only 36 Recreation Guide PDF/link records (2015-2019) and no registration/occupancy dataset. **candidate** (title scan of 703 DCAT entries)
- **anomaly** "Seasonal layers such as outdoor rink conditions update frequently": the landed `ork_ice_conditions_orw` has 6 rows with dates 2021-12-22 to 2022-01-03 (Ottawa River Watch style), i.e. stale; and the DCAT "NCC Rideau Canal Skateway - Ice condition" was last modified 2024-10-15 and is an NCC-hosted external link. No city rink-condition layer found by title scan. **verified** (parquet + DCAT)
- Facilities table has building/element/facility-group columns, bilingual, geometry as GeoJSON text.

### ons
**LIVE.** Tag `bulk, api`: **differs** (api is real and unauthenticated; bulk not found).
- **unique** Custom, unauthenticated REST: https://ons-sqo.ca/wp-json/ons/v1/get-data/{neighbourhoods|data|layers|bins} all return 200 JSON `{columns, rows}`: neighbourhoods 640,668 B (116 rows with polygon vertices and names EN/FR, ONS_ID), data 730,499 B (884 indicator rows by 117 columns: city total `0` plus 116 neighbourhood ids 3001-3117; 227 of 103,426 cells empty), layers 567,007 B (386 indicator metadata rows: category, description, source, date represented/published, French fields), bins 10,513 B. This is the full indicator table behind the map, far above "over 300 indicators" (884 data rows). Not in the warehouse (only Gen 3 boundaries, 116 rows, and Gen 2 hist, 111). **verified** (REST + landed boundary count 116 matches)
- **anomaly** freshness is mixed: layer metadata shows most indicators "May 11, 2021" (Census 2021) published Jan-Feb 2024; a few newer ("April 2024 - March 2025", published April 15, 2026). The `neighbourhoods` CPT (116 posts) last modified 2026-06-12. **verified**
- **anomaly** www.neighbourhoodstudy.ca redirects to https://ons-sqo.ca/ (also for /wp-json/, which returns the HTML home page); sources.json should lead with ons-sqo.ca. **verified**
- **anomaly** WordPress exposes 346 routes, including `mcp` and `wp-abilities/v1` namespaces and `/wp/v2/plugins`; `/ons/v1/lookup/{id}` returns 410 "No neighbourhood found for ID 1" (ids are 3-digit codes). Site counts: 38 pages, 71 posts, 1,008 media. Not probed further. **candidate**
- Licence: stage 3 assigns "ONS terms of use"; no explicit data licence read on the API. **candidate**

### nei
**LIVE.** Tag `html`: **differs** (bulk is real; wp-json also open).
- **tag-fix** add `bulk`: the WordPress media library (https://neighbourhoodequity.ca/wp-json/wp/v2/media, `x-wp-total: 1280`) holds per-indicator CSV and XLSX for the 2024 index (Low-Income, Transit-Score, Walkability, Hate-Crime, Crime, Diabetes, Seniors-Living-Alone, Working-Poor, domain files, NEI-Index_ranks_2024 etc., uploaded 2024-11-01 and 2024-12-17), plus NEI-2024-Documentation.pdf (200, 1,908,291 B) and indicator matrices. Stage 3 said "page mentions download but no direct data link found": missed. **verified** (media list; NEI-Index_ranks_2024_csv.csv GET 200, 13,902 B, 228 lines)
- **anomaly** the ranks CSV and the Open Ottawa hub layer disagree in shape: the CSV is ranked with a 2-row header (rank 1 = University of Ottawa, index 44.2; Heron Gate 45.0), while hub layer "NEI 2024" has 218 rows (e.g. Riverside Park score 63.0) and 2019 has 196 rows. The two are different cuts (CSV 228 lines incl. headers; hub 218 CTs); worth reconciling before joining. **candidate**
- **anomaly** the site has ~100 pages of which more than half are leftover theme demo pages from 2015-2016 ("Pricing Slider", "Parallax", etc.), and /wp-json/ lists 469 routes with plugins `wpdatatables`, `mcp`, `elementor-mcp-composer`. wpDataTables routes may expose table data; not probed. **candidate**
- Newest content change: page "Hate Crime" modified 2026-02-03; documentation 2025-03. Description "renewed 2024" holds.
- Hub copies landed: open_ottawa_neighbourhood_equity_index_nei_2024 (218 rows, 23 cols), _2019 (196 rows, 27 cols). **verified**

### community-data-program
**LIVE.** Tag `request`: **matches** (membership-gated), operator wrong.
- **anomaly** operator is wrong: sources.json says Canadian Council on Social Development; https://communitydata.ca/about says the CDP "has been hosted by the Canadian Community Economic Development Network (CCEDNet) since 2019", est. 2010; the nav still has "CCSD Archives". **verified** (about page + regional page breadcrumb "CCEDNet")
- **anomaly** the "Ottawa-region catalogue" claim is weak: the page (200, 29 KB) lists lead rep (SPC Ottawa), member organisations, consortium boundaries (CSDs 3501, 3502, 3506, 3509, 3547) and links to public reports (ONS housing profile 2024, NEI, SPCO 2021 Census highlights, Ottawa Community Wellbeing Report 2018 PDF) but no data catalogue; products behind login/cart. Membership is "open to any Canadian public, non-profit or community sector organization": an unaffiliated individual does not qualify. **verified**
- Nothing unique beyond the pointers to SPCO publications.

### statcan-census
**DEGRADED** for the catalogued URL; source itself LIVE. Tag `bulk`: **differs** (add `api`).
- **anomaly** https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/index.cfm?Lang=E returns 403 with a Cloudflare "Security Check" page to curl; so does GetFile.cfm (header `cf-mitigated: challenge`). verification.json already records 403 at 13:25 today. The "bulk download" there is not reachable without a browser. **verified** (my probe plus the verification record)
- **tag-fix** add `api`; the WDS is open: POST https://www150.statcan.gc.ca/t1/wds/rest/getCubeMetadata returned SUCCESS for table 98-10-0002 (CSD counts, 2021, release 2022-02-09) and GET getFullTableDownloadCSV/98100002/en returned a zip URL; zip HEAD 200, 551,875 B, Last-Modified 2022-02-09. **verified**
- **anomaly** Census 2026 was taken in May 2026; no 2026 products appear yet (expected). Not checked directly. **candidate**
- Licence stage 3 "Statistics Canada Open Licence": not re-read.

### ottawa-insights
**DEGRADED** (stale). Tag `html`: **differs** (wp-json open, but it holds no data).
- **anomaly** frozen site: /wp-json/wp/v2 shows 9 posts (newest modified 2023-02-14, newest dated 2020-02-12), 10 pages (latest modified 2022-03-29, home 2020-02-12), newest media 2020-02-10, 27 glossary entries. Homepage still claims "up-to-date, reliable local data". **verified** (REST + page text)
- **anomaly** 1,109 media items but a 100-item sample is only PNG/JPEG/SVG; no CSV/XLSX found. The indicator content is rendered by FacetWP/theme templates, not exposed as REST types (types: posts, pages, glossary only). **candidate**
- **tag-fix** none needed for access (`html` right in effect); add a "stale since 2020-2023" flag. /wp-json/ is 200 with 344 routes (Yoast, Wordfence, FacetWP, WPML). **verified**
- Nothing unique; ONS and NEI supersede it.

## Three most interesting findings
1. **ONS has an open JSON API with the full indicator table**: https://ons-sqo.ca/wp-json/ons/v1/get-data/data gives 884 indicators x 116 neighbourhoods plus city total (730 KB), with layer metadata for 386 indicators and polygons; none is in the warehouse. The ons tag `api` was right but neighbourhoodstudy.ca now redirects to ons-sqo.ca.
2. **Open311 data is largely un-geolocated**: 83-85% of rows have null coordinates and ~10% null ward, 2% of 2025 requests still "Active", and DCAT freshness dates are months stale versus the daily blob; the `api` tag is dead. Separately, the Tree Inventory (304,207 live points, updated 2026-10-15) and RVCA's regulation-limit hazard layer (503 polygons, shapefile refreshed 2026-10-15) are unlanded high-value spatial data.
3. **Tag/URL drift across the "html" sources**: NEI really offers per-indicator CSV/XLSX (1,280 media items), RVCA runs a 34-dataset JKAN open-data portal, StatCan's catalogued page is Cloudflare-blocked while its WDS API works, Engage Ottawa's `api/v2` 404s outside a browser, and CDP is now hosted by CCEDNet.

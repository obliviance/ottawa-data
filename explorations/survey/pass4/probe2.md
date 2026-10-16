# Pass 4 probe 2 — uncatalogued Ottawa sources (52 rows)

Probed 2026-10-16. Read-only. Evidence saved under the session scratchpad `p2/`.

## Method caveat (read first)

**All of ottawa.ca is behind an Incapsula/Imperva shell for curl.** Every path returns HTTP 200 with a ~1,050-byte
body (`/_Incapsula_Resource` iframe), including a deliberately nonsense path (`/en/zzz-nonexistent-path`). A 200 from
ottawa.ca therefore proves nothing about a page existing. Every ottawa.ca URL below is **candidate** (URL guessed
from site structure or search, liveness unproven; Wayback availability API returned no snapshot for the one I tried).
`opendata.ottawa.ca/inspections/*.zip` returns a ~6 KB "Pardon Our Interruption" challenge page, also not evidence.

What does work from curl: `open.ottawa.ca` (ArcGIS Hub), its DCAT feed
(`https://open.ottawa.ca/api/feed/dcat-us/1.1.json`, 703 datasets, 2.6 MB), `maps.ottawa.ca/arcgis/rest/services`,
`pub-ottawa.escribemeetings.com`, `documents.ottawa.ca`, and most non-city sites. Most rows are therefore decided by
the open-data catalogue plus ArcGIS REST, not by page probes. **verified** = two independent ways (DCAT listing plus a
live REST/CSV fetch); otherwise **candidate**.

## Table

OD = open.ottawa.ca. REST = maps.ottawa.ca/arcgis/rest/services.

### A. City of Ottawa

| Row | URL | Status / liveness | Machine-readable? | Emoji | Note |
|---|---|---|---|---|---|
| Short-term rentals | ottawa.ca/en/living-ottawa/laws-licences-and-permits/licences-and-permits/short-term-rental-accommodations (guess) | Incapsula shell; unproven | None found: no STR dataset among 703 in DCAT (**verified** absence by DCAT keyword search) | keep 🟡 | Registry/enforcement only in memos and news (candidate) |
| Animal control / licensing | OD `licensed-dog-and-cat-names` | OD page listed in DCAT (candidate; not fetched) | Document-type item only (no CSV/API distribution); "Dogs-in-Parks" is spatial | keep 🟡 | Shelter/enforcement data: none found |
| Property standards / vacant-building | ottawa.ca (guess) | shell; unproven | None in DCAT | keep 🔴 | Candidate; no public endpoint found |
| 911 / dispatch performance | OD `dispatched-calls-for-service` | DCAT updated 2026-09-29; CSV fetch not done for this one | ArcGIS FeatureServer (services7.arcgis.com Calls_For_Service) + CSV | keep 🟡 | This is Ottawa Police calls-for-service, not 911 answer-time performance; the open feed is real and fresh (candidate); Ottawa Police site itself live (200, 77 KB) |
| Board of Health agendas/minutes | https://pub-ottawa.escribemeetings.com/?Year=2026&Expanded=Board%20of%20Health | 200, 267 KB real page, lists "Board of Health" meeting type | HTML/PDF only; no feed seen | keep 🟡 | **verified** (live page + string match) |
| Food/personal-service/pool/tobacco inspections | OD `public-health-inspection-data-food-safety-1` (+ Personal Services, Recreational Water, Child Care, Drinking Water, Recreational Camps) | DCAT lists 8 datasets modified 2025-10-07 | Listed as zip at opendata.ottawa.ca/inspections/yelp_ottawa_healthscores_*.zip (Yelp LIVES format) but that host serves a bot-challenge page to curl | **change to 🟢 (candidate)** | hierarchy says bulk 🔴/⚪; bulk is advertised on OD. Could not download. Tobacco/vaping: not in DCAT. OPH own pages: 404 on guessed paths; site itself 200 |
| City-run long-term care homes | REST CommunitySocialServices/MapServer/10 | **verified** (layer count = 4 City homes; fields name/address/residents/ownership) | ArcGIS REST query works | keep 🟡 (new: the 4 homes as an open spatial layer) | Occupancy/inspection data not open; provincial inspection portal publicreports.mltc.gov.on.ca is live (200) |
| Child care | OD `licensed-child-care-providers`; REST CommunitySocialServices layers 1-8 | OD page in DCAT; layer 1 query errored (400, my query shape) | Document-type on OD; spatial layers exist | keep 🟡 | Subsidy caseload/wait list not found |
| Ontario Works caseload | OD `ontario-works-caseload-data-2020-to-2025` | **verified**: CSV fetched (10 rows, 2015-2025 YTD, households on/applying/leaving) + FeatureServer count 10 | CSV + REST + GeoJSON | **change to 🟢** | Open, but annual averages only (10 rows) |
| Community funding recipients | OD `city-of-ottawa-cultural-funding-results` | **verified**: CSV 69 KB fetched (200 text/csv) + FeatureServer | CSV/REST | **change to 🟢 (cultural funding portion)** | Only cultural funding; wider Community Development Framework lists still in PDFs |
| Newcomer / OLIP | https://olip-plio.ca | 200, 100 KB real WP site | PDFs in /resources/; no data feed | keep 🟡 | **verified** |
| Anti-Racism Secretariat | ottawa.ca (guess) | shell; unproven | none found | keep 🟡 | candidate; related: Neighbourhood Equity Index 2024 is open (CSV/REST in DCAT) |
| Accessibility plan | ottawa.ca (guess) | shell; unproven | none | keep 🟡 | candidate |
| Wastewater / CSO | ottawa.ca/CSO (named in city PDF); https://documents.ottawa.ca/sites/default/files/cso_appendixa_en.pdf | PDF **verified** live (200, application/pdf, 304 KB) says live map covers 13 overflow sites; map page itself unproven | Infrastructure layers: REST WastewaterInfrastructure/MapServer (sanitary, combined, storm, pump stations/plants) | keep 🟡 | Event/volume history only in Council memos. No ROPEC or CSO event dataset in DCAT |
| Ottawa River Action Plan | ottawa.ca (guess) | shell; unproven | none | keep 🟡 | candidate |
| Solid waste / green bin | OD `solid-waste-collection-calendar-collection-days` | in DCAT; REST SolidWasteCollectionCalendar exists | Calendar data + `Curbside Recycling and Waste Tonnages 2005-2016` | keep 🟡 | Tonnages stale (to 2016) |
| Source-water protection | https://www.mrsourcewater.ca | 200 (redirect to /en/), 131 KB real site | plan PDFs; no feed seen | keep 🟡 | **verified** live |
| Climate / GHG | OD `greenhouse-gas-ghg-emissions-inventories-2024`, `greenhouse-gas-emissions-dashboard`; REST Climate_Resiliency (urban heat island 2019/21/23) | **verified**: CSV fetched (1.5 KB) + FeatureServer count 11 | CSV/REST | **change to 🟢 (GHG inventory)** | Climate Change Master Plan itself is PDF |
| Air quality | https://www.airqualityontario.com | 200, 22 KB real | provincial (MECP) | keep 🟡 | Not City data; "Cleaner Air Spaces" layer in REST OttawaPublicHealth |
| Contaminated sites / brownfields | OD `former-landfills`; REST Environmental/MapServer/1 | **verified**: 133 features | Spatial open (former and active landfills) | **change 🔴 to 🟡** | Brownfield/spill registers still none; Ontario brownfields-registry guess 404 |
| Naturalization / forest | REST Forestry/MapServer/0 (Tree Inventory) + OD `tree-inventory` | **verified**: 304,207 features; CSV/GeoJSON in DCAT | REST/CSV/GeoJSON | **change to 🟢 (trees)** | Also Tree Protection Bylaw layer + removal-permit statistics 2021-2025 (OD documents). Woodland/natural-systems: Planning layer 55 |
| Wells & septic | OD `ottawa-rural-clean-water-program`; communal well drinking-water summaries (Vars, Carp, Kings Park, Munster, Shadow Ridge, Richmond West) | DCAT items, modified 2025-2026 | Web-page/document type | **change 🔴 to 🟡 (candidate)** | Private well/septic permits still closed |
| Stormwater / drainage layers | REST WastewaterInfrastructure (Storm), WaterAndSewer, SurfaceWater | **verified** (layer lists fetched) | REST | keep 🟢 | |
| Public art | OD `cultural-spaces-inventory-public-art` | DCAT updated 2026-10-08 | CSV, REST, GeoJSON, KML | **change to 🟢 (candidate)** | OD "Public Art (Historical)" is web-page only |
| Museums Network | ottawa.ca (guess) | shell | none; only children's-programs survey on OD | keep 🟡 | candidate |
| Cultural/festival funding & permits | see Community funding row | **verified** funding CSV | CSV | **change to 🟡→🟢 for funding; permits 🔴** | "Festivals and Events (Historical)" web page only |
| Cemeteries | ottawa.ca/en/living-ottawa/cemeteries (guess) | shell | no cemetery dataset in DCAT | keep 🟡 | candidate |
| Land inventory / surplus pipeline | OD vacant-land surveys (Vacant Urban Residential Land Survey 2015/2019, Vacant Industrial & Business Park Lands) | in DCAT | partly spatial/tabular | keep 🟡 | No surplus-disposal feed found |
| Corporate real estate & leases | ottawa.ca | none found | none | keep 🔴 | candidate |
| Facilities condition | REST City_Facilities/MapServer (8 facility-type layers) | **verified** layer list | spatial inventory only | keep 🟡 | Condition ratings not in the layer list |
| Fleet | OD `green-fleet-initiatives-tracking` | DCAT, modified 2026-08-10 | web-page/document | keep 🟡 | candidate |
| IT / digital | ottawa.ca | none | none | keep 🟡 | open data program itself is live (OD, 200) |
| Municipal drains | REST SurfaceWater/MapServer/2 "Municipal Drains" | **verified**: 7,690 features | REST query works | **change 🔴 to 🟡** | Spatial layer is open; petitions/engineer's reports remain closed |
| Rural / private / unopened roads | REST Road_Information, Planning/19 (Rural Residential Land Survey) | layer exists (candidate) | spatial | keep 🟡 | No private-road/unopened-allowance layer isolated |
| Village plans / settlement boundaries | REST OfficialPlan/MapServer/72 and Planning/166 "Village Boundaries" | **verified**: 26 features | REST | keep 🟡 (spatial part is 🟢) | |
| Agricultural land / prime ag | REST Planning/MapServer/99 "Agriculture Boundary and other Restricting designations" | **verified**: 169 features | REST | keep 🟢 | |
| Public notices | ottawa.ca (guess) | shell | none | keep 🟡 | candidate |
| Media releases | OD `media-advisories-news-releases-and-public-service-announcements-rss-feed` | DCAT lists it; points to ottawa.ca protocols page `#rss-feeds` (shell for curl) | RSS exists (candidate) | **change to 🟢? candidate** | OD also has `library-media-releases` |
| Councillor/city social media | n/a | not probed | platform-dependent | keep 🟡 | no endpoint to test |
| Records-retention schedules | https://documents.ottawa.ca | 200, 101 KB real site | PDFs at best | keep 🟡 | specific schedule not located |

### B. Agencies, boards, commissions

| Row | URL | Status / liveness | Machine-readable? | Emoji | Note |
|---|---|---|---|---|---|
| OCH | https://www.och-lco.ca | 200, 103 KB real | PDFs; guessed /about-us/annual-reports 404 | keep 🟡 | **verified** |
| OCH Foundation | https://ochfoundation.ca | 200, 133 KB real (separate domain) | none | keep 🟡 | **verified**; note foundation has its own domain, /foundation on och-lco.ca is 404 |
| Built Heritage Committee | eScribe (same host as BoH) | page string match "Built Heritage Committee" plus Advisory/Sub-committee variants | HTML/PDF | keep 🟡 | **verified** |
| BIAs | OD `business-improvement-areas`; REST AdministrativeAreas/MapServer/3 (also BIA/MapServer) | **verified**: CSV fetched (3.3 KB) | CSV/REST (boundaries only) | keep 🟡 | Budgets/minutes: no Ottawa coalition site found (ottawabia.ca does not resolve) |
| ByWard Market District Authority | https://www.byward-market.com | 200, 612 KB real | HTML only | keep 🟡 | **verified**; permitting authority for patios/busking |
| Crime Prevention Ottawa | https://www.crimepreventionottawa.ca | **403 Cloudflare "Attention Required"** (curl blocked, also with browser UA) | unknown | keep 🟡 | Challenge page is not live evidence; **candidate** |
| OCLDC | not found | no official site found; search suggests rebrand to "Build Ottawa" (housing); buildottawa.ca does not resolve | none | keep 🟡 | candidate; update the name |
| Election Compliance Audit Committee | ottawa.ca/en/city-hall/your-city-government/elections/2014-elections/election-compliance-audit-committee (search hit; ottawa.ca shell); ECAC is a meeting type in eScribe; OttWatch meeting page https://ottwatch.ca/meeting/b65d6938-... | OttWatch 200 real; eScribe string match | HTML/PDF; OttWatch publishes an RSS (ottwatch.ca/home/index.rss) | **change ⚪ to 🟡** | **verified** (eScribe + OttWatch). Decisions 2019-2025 documented in news; no register |
| Property Standards & Licence Appeal committees | ottawa.ca | none found | none | keep 🔴 | candidate |
| Debenture / Audit Committee | eScribe | string match on live page | HTML/PDF | keep 🟡 | **verified** |
| Pineview Golf | not found as city body; search: privately owned about 12 years (councillor blog) | no official site; pineviewgolf.ca does not resolve | none | **change: remove row or mark stale** | candidate. Not a municipal body any more |
| Rural clean-water / drainage boards | OD `ottawa-rural-clean-water-program` | DCAT item | web page | change 🔴 to 🟡 | candidate; drains boards closed |

### C. School boards

| Row | URL | Status | Machine-readable? | Emoji | Note |
|---|---|---|---|---|---|
| Trustee voting records | https://www.ocsb.ca (200, 166 KB real); ocdsb.ca/our-board/board-meetings (404, guess) | boards live | none found | keep 🔴 | candidate; OD has a "School board achievements and progress" item |

## Not reached / limits

Not probed past a guess or a DCAT listing: Councillor social media; Corporate retention schedule specifics; Anti-Racism and Accessibility pages; Museums; Public notices; Property standards; Real estate. All are ottawa.ca pages that curl cannot test (shell). A browser-based stage-2 run (verify_stage2.py) is the way to settle them.

## Five most notable findings

1. **Several "closed/partial" rows are really open spatial or tabular data on open.ottawa.ca / maps.ottawa.ca.** Verified live: Ontario Works caseload CSV (10 rows), Cultural Funding Results CSV, GHG inventory CSV, Municipal Drains layer (7,690 features), Former Landfills (133), City long-term-care homes layer (4), Tree Inventory (304,207), Village Boundaries (26), Agriculture Boundary (169). Suggested changes: Ontario Works, Climate/GHG, Public art, Trees -> 🟢; Municipal drains, Contaminated sites, Wells -> 🟡.
2. **Public health inspections (food safety, personal services, recreational water, child care, drinking water, camps) are listed on OD with downloadable zips** at opendata.ottawa.ca/inspections/*.zip, but that host serves a "Pardon Our Interruption" bot-challenge to curl. Hierarchy says bulk is closed; it is advertised as open but needs a browser-grade fetch. Not catalogued.
3. **ottawa.ca returns a 1 KB Incapsula shell with 200 for every path, including nonsense paths.** All ottawa.ca page liveness claims, including the guessed URLs here, are unproven; this will also invalidate any stage-0 "alive" result for ottawa.ca pages in verification/ unless body size was checked.
4. **Stale or moved entities.** Pineview golf is privately owned (about 12 years), so it is not a municipal body; OCLDC appears to be rebranding as "Build Ottawa" (no live site found); the OCH Foundation has its own domain (ochfoundation.ca), and och-lco.ca/foundation is a 404; the Election Compliance Audit Committee is not ⚪ (it is a meeting type in eScribe, has OttWatch coverage and a 2025 court-ordered audit of the Menard campaign).
5. **Uncatalogued machine-readable feeds seen:** OD DCAT (703 datasets, `https://open.ottawa.ca/api/feed/dcat-us/1.1.json`), the police `Dispatched Calls For Service` FeatureServer (updated 2026-09-29), OD media-advisories RSS entry, OttWatch RSS (ottwatch.ca/home/index.rss, third-party), and ArcGIS services folders (ActiveTransportation, Forestry, SurfaceWater, WastewaterInfrastructure, Climate_Resiliency, Zoning_Bylaw_2026_50, etc.). Check these against sources.json.

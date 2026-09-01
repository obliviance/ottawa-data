# ottawa-data

A catalogue of public data and information sources for the governance of Ottawa, Ontario —
electoral, legislative, financial, spatial, operational — grouped by domain and tagged by how
machine-readable each source actually is.

**[`sources.json`](sources.json) is the source of truth.** This README is generated from it by
[`build_readme.py`](build_readme.py). Edit the JSON, then run `python3 build_readme.py`.


## Status: Stage 0–1 checked, 2026-09-01

Every entry was first compiled from search-result metadata with no outbound HTTP. A
liveness-and-fingerprint pass ([`verify.py`](verify.py), written to
[`verification.json`](verification.json)) has since **opened every URL** and probed for a
machine-readable surface. It does **not** confirm the access tag or the licence — a page that
loads is not the same as a dataset you can use — so those still need Stage 2 (headless browser)
and Stage 3 (human judgement).

Last run **2026-09-01** over 100 URLs across 72 sources:

| Best result for the source | Sources |
| --- | --- |
| Machine-readable surface confirmed (API / bulk / catalogue feed) | 15 |
| Reachable, plain HTML/PDF — tag & licence unverified | 50 |
| Reachable but needs a browser (JavaScript-rendered, or bot-blocked) | 6 |
| Every catalogued link dead or erroring | 1 |

URL-level totals: 17 machine-readable · 68 HTML ·
9 JavaScript-rendered · 1 bot-blocked ·
0 PDF · 3 dead · 2 erroring.

Entries with `"verify": true` in the JSON carry a specific known doubt and are marked
**[verify]** below.


## Access tags

| Tag | Meaning |
| --- | --- |
| `API` | Live queryable endpoint — REST, GTFS-RT, ArcGIS GeoServices, Open311. |
| `Bulk` | Downloadable CSV / GeoJSON / shapefile / XLS. |
| `HTML` | Web pages or PDFs only; requires scraping or parsing. |
| `Request` | On-site, by freedom-of-information request, or by written request. |


## Contents

1. [Cross-cutting portals and the spatial services root](#1-cross-cutting-portals-and-the-spatial-services-root) — 4 sources
2. [Electoral process, candidates, campaign finance](#2-electoral-process-candidates-campaign-finance) — 5 sources
3. [Council proceedings, decisions, legislation](#3-council-proceedings-decisions-legislation) — 6 sources
4. [Oversight offices, lobbying, disclosure](#4-oversight-offices-lobbying-disclosure) — 6 sources
5. [Budgets, financial reporting, procurement, assessment](#5-budgets-financial-reporting-procurement-assessment) — 5 sources
6. [Development applications, zoning, land use, appeals](#6-development-applications-zoning-land-use-appeals) — 6 sources
7. [Transit, roads, collisions, enforcement](#7-transit-roads-collisions-enforcement) — 5 sources
8. [Policing, fire, paramedic services](#8-policing-fire-paramedic-services) — 4 sources
9. [Public health, housing, homelessness, social services](#9-public-health-housing-homelessness-social-services) — 4 sources
10. [Water, waste, watershed, utilities, green space](#10-water-waste-watershed-utilities-green-space) — 6 sources
11. [311, consultation, library, recreation](#11-311-consultation-library-recreation) — 4 sources
12. [Neighbourhood and demographic statistics](#12-neighbourhood-and-demographic-statistics) — 5 sources
13. [Independent trackers and civic-technology projects](#13-independent-trackers-and-civic-technology-projects) — 6 sources
14. [Non-municipal bodies governing land or services in Ottawa](#14-non-municipal-bodies-governing-land-or-services-in-ottawa) — 4 sources
15. [Historical record](#15-historical-record) — 2 sources


## 1. Cross-cutting portals and the spatial services root

### Open Ottawa / Donnees ouvertes

`API` `Bulk` · *City of Ottawa*

The city's ArcGIS Hub catalogue. Every dataset exposes GeoService and GeoJSON endpoints alongside CSV, shapefile and KML download.

> _Checked 2026-09-01 (stage 0–1): reachable — machine-readable surface confirmed — ArcGIS Hub DCAT feed present (690 datasets)_
- <https://open.ottawa.ca/>
- <https://ouverte.ottawa.ca/>
- <https://open.ottawa.ca/pages/developer-resources>

### City ArcGIS REST services root

`API` · *City of Ottawa*

Raw ArcGIS MapServer directory behind geoOttawa. Observed services include Zoning, Basemap_Ottawa and TopographicMapping (contours, building footprints, pathways). Cleanest bulk-ingestion path for anything spatial.

> _Checked 2026-09-01 (stage 0–1): reachable — machine-readable surface confirmed — ArcGIS REST catalogue: 80 services, 1 folder, v10.81_
- <https://maps.ottawa.ca/arcgis/rest/services/>

### geoOttawa

`HTML` · *City of Ottawa*

Public map viewer over the ArcGIS services. Search by address, intersection, street segment or facility. Use for reconnaissance, then pull the layer from REST.

> _Checked 2026-09-01 (stage 0–1): reachable but JavaScript-rendered — needs a Stage 2 browser check_
- <https://maps.ottawa.ca/geoottawa/>

### Open Data policy and programme

`HTML` · *City of Ottawa*

Licence terms, publication commitments, and the request channel for datasets not yet released.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-data>


## 2. Electoral process, candidates, campaign finance

### Certified candidate list

`HTML` · *City of Ottawa (City Clerk)*

Authoritative roster of registered candidates: mayor, 24 wards, four school boards. Source of truth for who is on the ballot.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://elections.ottawa.ca/CandidateList/CandidateList>

### Who is running in my ward?

`HTML` · *City of Ottawa*

Same roster behind an address lookup. Useful as a ward-boundary geocoding check.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://ottawa.ca/en/city-hall/elections/voters/who-running-my-ward>

### Campaign financial statements and contributions

`HTML` · *City of Ottawa (City Clerk)*

Filed under Municipal Elections Act s.88.25, published free under s.88(9.1). Discloses name, address, date and amount for every contributor of $100 or more. Contribution cap $1,200 per candidate. Filing deadline 2pm the last Friday in March following the election, so 2026 filings land around March 2027.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://ottawa.ca/en/city-hall/elections/candidates/candidate-campaign-finances-and-contributions>
- <https://ottawa.ca/en/city-hall/elections/previous-elections-and-appointment-processes/financial-statements-2022-municipal-elections/candidate-and-third-party-advertiser-compliance-reports>

### Election key dates and candidate information

`HTML` · *City of Ottawa*

Statutory calendar, nomination rules, third-party advertiser registration. 2026: nominations opened 1 May, close 21 August 2pm, Clerk certifies by 24 August, election 26 October.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://ottawa.ca/en/city-hall/elections/learn-more-about-municipal-elections/key-dates-2026-municipal-elections>
- <https://ottawa.ca/en/city-hall/elections/candidates/information-candidates>

### Historical results and ward boundaries

`Bulk` · *City of Ottawa / Wikipedia*

Poll-level results and ward boundary geometries publish to the open data portal. Wikipedia articles are the most convenient freely-licensed tabular version.

> _Checked 2026-09-01 (stage 0–1): reachable — machine-readable surface confirmed — ArcGIS Hub DCAT feed present (690 datasets)_
- <https://open.ottawa.ca/>
- <https://en.wikipedia.org/wiki/2022_Ottawa_municipal_election>
- <https://en.wikipedia.org/wiki/2026_Ottawa_municipal_election>


## 3. Council proceedings, decisions, legislation

### eScribe: agendas, minutes, staff reports

`HTML` · *City of Ottawa*

Every Council, standing committee and board meeting from 18 June 2012 onward. Staff reports attach as filestream.ashx?DocumentId=NNNNNN, a sequential integer, which makes systematic harvesting tractable. Richest untapped corpus in the catalogue.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://pub-ottawa.escribemeetings.com/>

### Legacy agenda system (pre-2012)

`HTML` `Request` · *City of Ottawa*

Older documents. Anything before 2012 not here is held by the City Archives. Video from 2006 to 2012 is by request to Committees@ottawa.ca.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://app06.ottawa.ca/cgi-bin/docs.pl?lang=en>

### Council meeting video and audio

`API` · *City of Ottawa*

Live streams plus archived webcasts migrating from the old portal. Auto-captions make this searchable as text, a realistic route to a speech-level record of debate.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://www.youtube.com/channel/UCUR3i_hvk3-3i8vtrPg6v1Q>

### By-laws A to Z

`HTML` · *City of Ottawa*

Consolidated by-laws in HTML. Includes Procurement (2000-50), Lobbyist Registry, Integrity Commissioner (2021-7), Zoning (2026-50).

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://ottawa.ca/en/living-ottawa/laws-licences-and-permits/laws/laws-z>

### Document repository

`HTML` · *City of Ottawa*

Where most linked PDFs live: annual reports, manuals, primers, guides.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://documents.ottawa.ca/>

### Council and committee structure

`HTML` · *City of Ottawa*

Membership, mandates and terms of reference for standing committees, sub-committees, adjudicative bodies and local boards.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://ottawa.ca/en/city-hall/council-committees-and-boards>


## 4. Oversight offices, lobbying, disclosure

### Office of the Auditor General

`HTML` · *City of Ottawa (independent statutory officer)*

Performance, financial and compliance audits across all departments and agencies. Standalone site, separate from ottawa.ca. Example: Council Expenses Audit, November 2025.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://www.oagottawa.ca/>

### Integrity Commissioner

`HTML` · *City of Ottawa (independent statutory officer)*

Codes of conduct, Municipal Conflict of Interest Act ss.5/5.1/5.2, closed-meeting investigations. Also serves as Lobbyist Registrar and Meetings Investigator: three mandates, one office.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/integrity-commissioner>

### Lobbyist Registry

`HTML` · *City of Ottawa*

Every substantive communication (call, meeting, email) between lobbyists and members of Council or staff. In force since 1 September 2012. Public search requires no login. Pairs naturally with development applications and council votes.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://lobbyist.ottawa.ca/search/searchlobbyist.aspx?lang=en>
- <https://lobbyist.ottawa.ca/>

### MFIPPA disclosure log and access requests

`HTML` `Request` · *City of Ottawa (Access to Information and Privacy Office)*

Quarterly list of completed freedom-of-information requests of public interest. Records obtained by quoting the request number to mfippa@ottawa.ca. The route to anything not proactively published.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/public-disclosure/disclosure-mfippa-requests/general-information>
- <https://forms.ottawa.ca/en/form/occ/policy/mfippa-access-form>

### Members' office expenses and remuneration

`HTML` · *City of Ottawa*

Monthly per-member office expense disclosure plus the annual Statement of Remuneration, Benefits and Expenses required by the Municipal Act. Constituency Services Budget was $284,648 per ward councillor in 2023; the Mayor's was $970,646.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/public-disclosure/disclosure-office-expenses>

### Public Sector Salary Disclosure

`Bulk` · *Government of Ontario*

Provincial, but covers all city employees earning $100,000 or more. Published as bulk data by year and employer.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://www.ontario.ca/page/public-sector-salary-disclosure>


## 5. Budgets, financial reporting, procurement, assessment

### Budget and financial reports

`HTML` · *City of Ottawa*

Audited annual financial statements, annual reports (2020 to 2024 online), and quarterly operating and capital budget status reports showing actual against budget by department.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://ottawa.ca/en/city-hall/budget-finance-and-corporate-planning/financial-reports-and-statements>

### Budget documents by year

`HTML` `Bulk` · *City of Ottawa*

Tabled and adopted budgets, 2022 onward. Line-item detail generally in PDF; some budget data mirrored to Open Ottawa.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://ottawa.ca/en/city-hall/budget-finance-and-corporate-planning>

### Financial Information Return (FIR)

`Bulk` · *Ontario Ministry of Municipal Affairs and Housing*

Province-mandated annual financial return under Municipal Act s.294(1), filed by 31 May. Data back to 1977 in a consistent schema across every Ontario municipality. The only clean way to benchmark Ottawa against peers.

> _Checked 2026-09-01 (stage 0–1): reachable — machine-readable surface confirmed — CKAN API v2.9.7, 2957 datasets_
- <https://efis.fma.csc.gov.on.ca/fir/>
- <https://data.ontario.ca/dataset/financial-information-return-fir-for-municipalities>

### Procurement and tenders **[verify]**

`HTML` · *City of Ottawa (Supply Services)*

Supply Services administers over $1B annually under By-law 2000-50. Bid opportunities post to a third-party e-tendering platform.

> **Verify:** Search results pointed at both Biddingo and third-party aggregators. Confirm the current platform before building against it.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://ottawa.ca/en/business/procurement/procurement>
- <https://ottawa.ca/en/business/procurement/procurement-law>

### MPAC property assessment

`Request` · *Municipal Property Assessment Corporation*

Provincial corporation assessing all Ontario properties. Per-property values are access-restricted; aggregate assessment-roll data by class and municipality is published.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://www.mpac.ca/>


## 6. Development applications, zoning, land use, appeals

### Development Applications Search

`HTML` · *City of Ottawa*

Every planning application with reports, plans, status and comment windows. Stable per-application URLs of the form /en/applications/D07-12-19-0075/details, so the file-number scheme is enumerable. 28-day standard comment period.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://devapps.ottawa.ca/>

### Zoning By-law 2026-50

`HTML` `API` · *City of Ottawa*

Approved 28 January 2026, enacted 11 March 2026, replacing 2008-250 after roughly five years of consultation. Re-consolidated after every Council meeting that amends it, with margin notes flagging provisions under appeal.

> _Checked 2026-09-01 (stage 0–1): reachable — machine-readable surface confirmed — ArcGIS service 'Layers': 8 layers, formats JSON, geoJSON_
- <https://ottawa.ca/en/living-ottawa/laws-licences-and-permits/laws/laws-z/zoning-law-law-no-2026-50>
- <https://maps.ottawa.ca/arcgis/rest/services/Zoning/MapServer>

### Official Plan

`HTML` · *City of Ottawa*

The 2021 Official Plan and its schedules: growth management, transects, urban boundary. The policy layer above zoning.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://ottawa.ca/en/planning-development-and-construction>

### Committee of Adjustment decisions

`HTML` · *City of Ottawa / CanLII*

Ottawa was the first committee of adjustment in Canada to publish decisions on CanLII: keyword-searchable by street, ward or application type, in a citation-stable legal database. Also on eScribe.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check. 1 link bot-blocked (fine in a browser): https://www.canlii.org/_
- <https://www.canlii.org/>
- <https://ottawa.ca/en/planning-development-and-construction/committee-adjustment/find-decision>

### Ontario Land Tribunal

`HTML` · *Government of Ontario*

Appeals of city planning and Committee of Adjustment decisions. Searchable by municipality; also mirrored on CanLII. Decisions older than ten years are by phone request.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://olt.gov.on.ca/decisions/>

### Building permits and land management

`Bulk` · *City of Ottawa*

Permit applications run through the My ServiceOttawa Land Management System. Issued-permit counts appear on Open Ottawa; per-permit detail is less consistently published.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://ottawa.ca/en/planning-development-and-construction/building-and-renovating>


## 7. Transit, roads, collisions, enforcement

### OC Transpo GTFS and GTFS-Realtime

`API` `Bulk` · *OC Transpo / City of Ottawa*

Static GTFS plus GTFS-RT Vehicle Positions and Trip Updates. Free API key via the Azure developer portal; commercial use permitted. Buses report GPS roughly every 30 seconds. Contact octranspo-dev@ottawa.ca.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://www.octranspo.com/en/plan-your-trip/travel-tools/developers/>
- <https://nextrip-public-api.developer.azure-api.net/>
- <https://www.transit.land/feeds/f-f24-octranspo>

### Traffic Ottawa open data

`API` · *City of Ottawa*

Its own open-data surface separate from the main portal: live traffic map, cameras, incidents, and service endpoints including automated speed enforcement camera locations.

> _Checked 2026-09-01 (stage 0–1): reachable — machine-readable surface confirmed_
- <https://traffic.ottawa.ca/en/opendata>
- <https://traffic.ottawa.ca/map/service/ase_camera>

### Traffic collision data

`Bulk` `API` · *City of Ottawa / Ontario MTO*

All reportable collisions including property-damage-only, in CSV and shapefile. Sourced from MTO via Ottawa Police, OPP and RCMP. Every record validated at least once, roughly half twice.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check. 1 of 2 links broken: https://open.ottawa.ca/datasets/ottawa::traffic-collision-data/about → 404_
- <https://open.ottawa.ca/datasets/ottawa::traffic-collision-data/about>
- <https://ottawa.ca/en/parking-roads-and-travel/road-safety/road-safety-action-plan/fatal-and-major-injury-collision-data>

### Automated speed enforcement

`Bulk` · *City of Ottawa*

Month-by-month charge and speed data for every camera location, plus siting methodology.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://ottawa.ca/en/parking-roads-and-travel/road-safety/enforcement/automated-speed-enforcement>

### Road network, pathways, cycling infrastructure

`API` `Bulk` · *City of Ottawa*

Centrelines, sidewalks, multi-use pathways, cycling routes, winter maintenance classes, as spatial layers with GeoJSON endpoints.

> _Checked 2026-09-01 (stage 0–1): reachable — machine-readable surface confirmed — ArcGIS Hub DCAT feed present (690 datasets)_
- <https://open.ottawa.ca/datasets/pathway-links/api>


## 8. Policing, fire, paramedic services

### Ottawa Police Community Safety Data Portal

`API` `Bulk` · *Ottawa Police Service*

Separate ArcGIS Hub launched November 2023, reported as 11 datasets, 7 dashboards and 6 web maps. Dashboards for homicides, shootings and gun seizures, overdose calls, hate- and bias-motivated crime, auto theft, and calls for service by priority. Being an ArcGIS Hub, everything has a GeoJSON endpoint.

> _Checked 2026-09-01 (stage 0–1): reachable — machine-readable surface confirmed — ArcGIS Hub DCAT feed present (98 datasets)_
- <https://data.ottawapolice.ca/>

### Crime Map (year to date)

`Bulk` · *Ottawa Police Service / City of Ottawa*

Mirrored onto the city portal. Criminal offences open data also published directly by Ottawa Police.

> _Checked 2026-09-01 (stage 0–1): reachable — machine-readable surface confirmed — ArcGIS Hub DCAT feed present (690 datasets)_
- <https://open.ottawa.ca/datasets/crime-map-year-to-date/about>

### Police Services Board

`HTML` · *Ottawa Police Services Board*

Board agendas, minutes and reports run through the same eScribe instance as Council: budget, chief's reports, oversight items.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://pub-ottawa.escribemeetings.com/>

### Fire, paramedic and emergency services

`Bulk` · *City of Ottawa*

Station locations, response-time performance and call volumes publish to the open data portal. Service-level detail also appears in annual departmental reports to committee.

> _Checked 2026-09-01 (stage 0–1): reachable — machine-readable surface confirmed — ArcGIS Hub DCAT feed present (690 datasets)_
- <https://open.ottawa.ca/>


## 9. Public health, housing, homelessness, social services

### Ottawa Public Health reports and dashboards

`HTML` · *Ottawa Public Health*

Seasonal respiratory and enteric outbreak surveillance, Diseases of Public Health Significance, COVID-19 vaccination, and the MHASUH dashboard for mental health, addictions and substance use health. Dashboards are interactive; underlying data is not consistently exposed.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://www.ottawapublichealth.ca/en/reports-research-and-statistics/reports-research-and-statistics.aspx>

### Housing and homelessness: plans, facts and data

`HTML` · *City of Ottawa*

City dashboards on housing need and homelessness, plus the 10-Year Housing and Homelessness Plan and its progress reports.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://ottawa.ca/en/family-and-social-services/housing-and-homelessness/plans-facts-and-data>

### Social Housing Registry of Ottawa

`HTML` · *Social Housing Registry of Ottawa (non-profit)*

Administers the centralized rent-geared-to-income wait list under the Housing Services Act, 2011, across roughly 50 providers. Wait list reported at 12,447 households (2023) rising to 15,140 (2024), with 1,155 households housed in 2024. Waits commonly exceed five years.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://housingregistry.ca/>

### Alliance to End Homelessness Ottawa

`HTML` · *Alliance to End Homelessness Ottawa*

Independent annual progress reports and the Ottawa Housing Needs Assessment. Often more pointed than the city's own framing, and a useful cross-check.

> _Checked 2026-09-01 (stage 0–1): reachable but JavaScript-rendered — needs a Stage 2 browser check_
- <https://www.endhomelessnessottawa.ca/>


## 10. Water, waste, watershed, utilities, green space

### Drinking water quality reports

`HTML` · *City of Ottawa*

Annual report per municipal system under the Safe Drinking Water Act, with full parameter-by-parameter test result tables. Roughly 293 million litres treated daily. Summaries also tabled at committee via eScribe.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://ottawa.ca/en/living-ottawa/drinking-water-stormwater-and-wastewater/drinking-water>

### Solid waste data and reports

`HTML` · *City of Ottawa*

Diversion rates by stream and tonnages by programme. Residential diversion reported at 33 percent (2009) rising to 44 percent (2018); stream rates range from 40 percent for green-bin organics to 96 percent for leaf and yard waste.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://ottawa.ca/en/garbage-and-recycling/solid-waste-data-and-reports>

### Ottawa Riverkeeper open data

`API` `Bulk` · *Ottawa Riverkeeper*

Independent watershed monitoring on its own ArcGIS Hub: water quality sampling and river health indicators, fully queryable.

> _Checked 2026-09-01 (stage 0–1): reachable — machine-readable surface confirmed — ArcGIS Hub DCAT feed present (139 datasets)_
- <https://ottawa-riverkeeper-open-data-ork-so.hub.arcgis.com/>

### Conservation authorities (RVCA, MVCA, SNC) **[verify]**

`HTML` `Bulk` · *Rideau Valley, Mississippi Valley and South Nation Conservation Authorities*

Three authorities cover Ottawa's watersheds. Each publishes floodplain mapping, watershed report cards and regulated-area layers: the binding constraint on much development, and often absent from city-only datasets.

> **Verify:** Individual authority URLs were not confirmed in search results.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://www.rvca.ca/>
- <https://mvc.on.ca/>
- <https://www.nation.on.ca/>

### Hydro Ottawa **[verify]**

`HTML` · *Hydro Ottawa (municipally owned)*

Municipally-owned distributor. Outage map is live; rate filings and performance metrics are public through the Ontario Energy Board rather than the utility.

> **Verify:** No open data programme surfaced in searching.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://hydroottawa.com/>

### Trees, parks and green space

`API` `Bulk` · *City of Ottawa*

Tree inventory, forest cover, park and facility locations, sports fields, as spatial layers with GeoJSON endpoints.

> _Checked 2026-09-01 (stage 0–1): reachable — machine-readable surface confirmed — ArcGIS Hub DCAT feed present (690 datasets)_
- <https://open.ottawa.ca/>


## 11. 311, consultation, library, recreation

### Open311 and 311 service requests **[verify]**

`API` `Bulk` · *City of Ottawa (ServiceOttawa)*

GeoReport v2 compliant, GET and POST, with test and production tiers. Raw history publishes as two rolling CSVs on Azure Blob Storage, 311opendata_currentyear.csv (updated daily) and 311opendata_lastyear.csv, carrying ward, responsible department and request description. Reported volume roughly 460,000 requests January 2025 to April 2026.

> **Verify:** apigee.net hosts are frequently migrated. Confirm the endpoint is live before depending on it.

> _Checked 2026-09-01 (stage 0–1): every catalogued link is dead or erroring_
>
> - `https://city-of-ottawa-prod.apigee.net/open311/v2/` → URLError: [Errno -2] Name or service not known
>
> - `https://open.ottawa.ca/documents/ottawa::open311-api/about` → HTTP 404 Not Found
- <https://open.ottawa.ca/documents/ottawa::open311-api/about>
- <https://city-of-ottawa-prod.apigee.net/open311/v2/>

### Engage Ottawa

`HTML` · *City of Ottawa*

Consultation platform: open and closed projects, survey instruments, and published what-we-heard reports. The record of what the public actually said before a decision.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://engage.ottawa.ca/projects>
- <https://ottawa.ca/en/city-hall/public-engagement/public-engagement-project-search>

### Ottawa Public Library

`HTML` · *Ottawa Public Library*

Branch data, circulation statistics and curated local-statistics guides. Partners with the city on open-data outreach and is a practical access point for census and demographic products.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://collections.biblioottawalibrary.ca/>

### Recreation facilities and programmes

`API` · *City of Ottawa*

Facility locations, rinks, pools, programme registration data. Seasonal layers such as outdoor rink conditions update frequently.

> _Checked 2026-09-01 (stage 0–1): reachable — machine-readable surface confirmed — ArcGIS Hub DCAT feed present (690 datasets)_
- <https://open.ottawa.ca/>


## 12. Neighbourhood and demographic statistics

### Ottawa Neighbourhood Study

`Bulk` `API` · *Ottawa Neighbourhood Study*

Over 300 indicators per neighbourhood: demographics, socioeconomic conditions, housing, amenities, built environment, health. Custom boundaries built from census tracts plus fieldwork and stakeholder consultation. Layers also published to Open Ottawa. The richest small-area dataset for Ottawa.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://www.neighbourhoodstudy.ca/>
- <https://ons-sqo.ca/data-stories/>

### Neighbourhood Equity Index

`HTML` · *Ottawa Neighbourhood Study / partners*

Composite equity scoring across neighbourhoods, renewed 2024 with published methodology documentation. Useful as a ready-made weighting when one defensible composite is wanted rather than 300 raw indicators.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://neighbourhoodequity.ca/>

### Community Data Program

`Request` · *Canadian Council on Social Development*

Consortium purchasing custom Statistics Canada tabulations for member organizations. Some products are members-only, but the Ottawa-region catalogue shows what exists.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://communitydata.ca/content/ottawa-and-region>

### Statistics Canada Census Profile

`Bulk` · *Statistics Canada*

Full profiles at census subdivision, metropolitan area, census tract and dissemination area. Bulk download available. Carleton's MacOdrum Library holds Ottawa-Gatineau census geography files back to 1951 for longitudinal work.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/index.cfm?Lang=E>

### Ottawa Insights

`HTML` · *Ottawa Insights (cross-sector partnership)*

Community indicator project pulling city, health and social data into themed narratives: environment, economy, wellbeing.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://www.ottawainsights.ca/>


## 13. Independent trackers and civic-technology projects

### OttWatch

`HTML` · *Independent*

The longest-running Ottawa civic monitor. Automatically scans ottawa.ca and eScribe for new agendas and documents, mirrors the lobbyist registry into a friendlier database, tracks new open-data publications, and maintains its own development application index. Closest thing to prior art for most projects in this space.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://ottwatch.ca/>
- <https://ottwatch.ca/devapp/index>

### Horizon Ottawa Vote Tracker

`HTML` · *Horizon Ottawa (advocacy)*

How each councillor voted across the 2022 to 2026 term, filterable by councillor, topic and committee. Advocacy-run, so vote selection is editorial, but fills a real gap since Ontario does not require municipalities to publish recorded votes.

> _Checked 2026-09-01 (stage 0–1): reachable but JavaScript-rendered — needs a Stage 2 browser check_
- <https://www.horizonottawa.ca/vote_tracker>

### How They Voted **[verify]**

`HTML` · *Independent*

Dedicated Ottawa council voting-record site.

> **Verify:** Currency and maintenance status unclear from search results alone.

> _Checked 2026-09-01 (stage 0–1): reachable but JavaScript-rendered — needs a Stage 2 browser check_
- <https://howtheyvoted.ca/>

### Ottawa Lookout

`HTML` · *Ottawa Lookout (local newsroom)*

Runs the most complete 2026 candidate tracker and per-ward election guides. Journalism rather than data, but consistently ahead of official publication.

> _Checked 2026-09-01 (stage 0–1): reachable but JavaScript-rendered — needs a Stage 2 browser check_
- <https://www.ottawalookout.com/p/meet-the-candidates>
- <https://www.ottawalookout.com/>

### Ottawa Civic Tech

`HTML` · *Volunteer community*

Volunteer community with an active meetup and public GitHub organization. The obvious place to find collaborators or avoid duplicating existing work.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check. 1 of 2 links broken: https://www.ottawacivictech.ca/ → no DNS_
- <https://www.ottawacivictech.ca/>
- <https://github.com/YOWCT>

### ACORN Canada housing voting records

`HTML` · *ACORN Canada (advocacy)*

Issue-specific scorecard on councillors' affordable-housing votes. Narrow and openly advocacy-framed, but sourced to actual votes.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://acorncanada.org/resources/ottawa-voting-records-report/>


## 14. Non-municipal bodies governing land or services in Ottawa

### National Capital Commission

`Bulk` `API` · *National Capital Commission (federal crown corporation)*

Owns the Greenbelt, Gatineau Park, much of the waterfront and many major parkways. Publishes through the federal open government portal and as a layer on Open Ottawa.

> _Checked 2026-09-01 (stage 0–1): reachable — machine-readable surface confirmed — ArcGIS Hub DCAT feed present (690 datasets)_
- <https://open.ottawa.ca/datasets/ncc-open-data-map/about>
- <https://search.open.canada.ca/opendata/?owner_org=ncc-ccn>

### Open Government Canada

`API` `Bulk` · *Government of Canada*

Federal datasets filterable to the National Capital Region: federal property holdings, employment, transfers to municipalities.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://open.canada.ca/>

### Ontario Open Data

`API` `Bulk` · *Government of Ontario*

Provincial datasets that determine much of what the city can do: FIR, health, education, transfers, licensing.

> _Checked 2026-09-01 (stage 0–1): reachable — machine-readable surface confirmed — CKAN API v2.9.7, 2957 datasets_
- <https://data.ontario.ca/>

### School boards (OCDSB, OCSB, CEPEO, CECCE) **[verify]**

`HTML` · *Four Ottawa school boards*

Four boards elect trustees on the municipal ballot but govern independently, with their own budgets, minutes and enrolment data. Frequently omitted from municipal data projects despite appearing on the same ballot.

> **Verify:** Individual board URLs were not confirmed in search results.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check. 1 of 4 links broken: https://ecolecatholique.ca/ → no DNS_
- <https://ocdsb.ca/>
- <https://ocsb.ca/>
- <https://cepeo.on.ca/>
- <https://ecolecatholique.ca/>


## 15. Historical record

### City of Ottawa Archives

`Request` · *City of Ottawa*

Over 20 kilometres of records in climate-controlled vaults at 100 Tallwood Drive, plus photographs, maps, architectural drawings and a 16,000-volume reference library. Holds pre-amalgamation municipal records and everything predating the 2012 eScribe cutover. Mostly paper, consulted on-site; order materials two working days ahead.

> _Checked 2026-09-01 (stage 0–1): reachable (HTML); access tag & licence still need a human check_
- <https://ottawa.ca/en/arts-heritage-and-events/city-ottawa-archives/archives-collection>

### Historical aerial imagery and mapping

`HTML` · *City of Ottawa / university libraries*

geoOttawa carries historical air-photo layers going back decades. Carleton and uOttawa GIS libraries hold digitized historical map series for the region.

> _Checked 2026-09-01 (stage 0–1): reachable but JavaScript-rendered — needs a Stage 2 browser check_
- <https://maps.ottawa.ca/geoottawa/>


## Where the gaps are

Patterns worth noting when deciding what to build.

1. **Recorded votes are not published as data.** Ontario does not require municipalities to
   publish councillor voting records. Ottawa's votes exist only as prose inside eScribe minutes.
   Every vote tracker in the catalogue is a volunteer or advocacy group re-keying them by hand —
   the clearest unmet need here.

2. **eScribe is a corpus, not an API.** Fourteen years of agendas, minutes and staff reports sit
   behind sequential `DocumentId` integers with no search API, no bulk export, and no structured
   metadata. Everything downstream — votes, spending decisions, planning history — is locked in
   PDFs.

3. **Nothing links the accountability datasets to each other.** The lobbyist registry,
   development applications, campaign contributions and council votes are four separate systems
   with no common identifiers. Joining them is the highest-value and hardest work available.

4. **Spatial data is excellent; textual and financial data is not.** Anything with coordinates
   has a clean GeoJSON endpoint. Anything expressed in prose or dollars is a PDF. That asymmetry
   shapes what is currently easy to build.

5. **Candidate platforms exist nowhere structured.** The city publishes who is running; nobody
   publishes what they propose. There is no comparable-positions dataset for the 2026 election.

## Licence

The catalogue itself (`sources.json`, this README) is offered under CC0 — do what you like with
it. The sources it points at carry their own licences; most City of Ottawa data is under the
Open Government Licence, but check each one.

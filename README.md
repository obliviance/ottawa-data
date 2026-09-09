# ottawa-data

A catalogue of public data and information sources for the governance of Ottawa, Ontario —
electoral, legislative, financial, spatial, operational — grouped by domain and tagged by how
machine-readable each source actually is.

**[`sources.json`](sources.json) is the source of truth.** This README is generated from it by
[`tools/build_readme.py`](tools/build_readme.py). Edit the JSON, then run `python3 tools/build_readme.py`.

**[`hierarchy.md`](hierarchy.md)** is the companion map: every institution that produces
information about Ottawa's governance and community, arranged as a tree and tagged open / closed /
unknown — including the branches not yet in this catalogue.

Contributing: [`CLAUDE.md`](CLAUDE.md) for the layout and workflow, [`tools/VERIFYING.md`](tools/VERIFYING.md)
for how sources get verified, [`ROADMAP.md`](ROADMAP.md) for the plan to turn the catalogue into
public-facing work. Scripts in [`tools/`](tools/), verification records in [`verification/`](verification/).


## Status: verified in stages, through 2026-09-09

Every entry was first compiled from search-result metadata with no outbound HTTP. Verification
runs in stages ([`tools/VERIFYING.md`](tools/VERIFYING.md)); each entry below shows how far it has got.

**Stage 0–1** ([`tools/verify.py`](tools/verify.py), 2026-09-09) — opened every URL and probed for a
machine-readable surface. 100 URLs / 72 sources:
17 machine-readable · 48 plain HTML/PDF ·
7 JavaScript-rendered or bot-blocked ·
0 with a dead link.

**Stage 2** ([`tools/verify_stage2.py`](tools/verify_stage2.py), 2026-09-09) — rendered the
41 JavaScript / interactive sources in a real headless Chromium and captured their XHR.
**7** turned out to have a real backing API (council votes as JSON from `howtheyvoted.ca`,
a REST API behind `devapps`, an EngagementHQ API behind Engage Ottawa, an AJAX meeting index
behind eScribe); **34** render fully and can be scraped headlessly; **0** still would not
yield (ottawa.ca and CanLII intermittently serve a bot challenge to headless browsers).

**Stage 3** ([`tools/verify_stage3.py`](tools/verify_stage3.py), 2026-09-09) — confirmed the
access tag and resolved the licence. **55** access tags confirmed as-is; **2** are
*understated* (more open than the tag claims — usually an ArcGIS/CKAN API behind a "Bulk" or
"HTML" tag); **0** overstated; **15** could not be confirmed automatically (needs an API
key, a login, or is a genuine FOI request). Licence resolved by operator: **55** sources fall
under an Open Government Licence; the rest carry site terms or access restrictions, flagged per
entry.

**Snapshots** ([`tools/snapshot.py`](tools/snapshot.py), 2026-09-09) — 79/94 URLs captured to the Wayback Machine.

Entries with `"verify": true` in the JSON carried a specific known doubt and are marked **[verify]** below.


## Access tags

| Tag | Meaning |
| --- | --- |
| `API` | Live queryable endpoint — REST, GTFS-RT, ArcGIS GeoServices, Open311. |
| `Bulk` | Downloadable CSV / GeoJSON / shapefile / XLS. |
| `HTML` | Web pages or PDFs only; requires scraping or parsing. |
| `Request` | On-site, by freedom-of-information request, or by written request. |

Where verification has run, each entry below carries a **Verified** line: the access tag and
licence as confirmed (or corrected), and the stage-by-stage trail. See [`tools/VERIFYING.md`](tools/VERIFYING.md).


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

> **Verified** — access: confirmed
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: machine-readable surface confirmed (ArcGIS Hub DCAT feed present (695 datasets)) · 3 archived_
- <https://open.ottawa.ca/>
- <https://ouverte.ottawa.ca/>
- <https://open.ottawa.ca/pages/developer-resources>

### City ArcGIS REST services root

`API` `Bulk` · *City of Ottawa*

Raw ArcGIS MapServer directory behind geoOttawa. Observed services include Zoning, Basemap_Ottawa and TopographicMapping (contours, building footprints, pathways). Cleanest bulk-ingestion path for anything spatial. Verified: services answer f=json/pjson; FeatureServer layers export GeoJSON/CSV.

> **Verified** — access: confirmed
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: machine-readable surface confirmed (ArcGIS REST catalogue: 80 services, 1 folder, v10.81) · stage 2 2026-09-09: renders fully — a headless scrape works · 1 archived_
- <https://maps.ottawa.ca/arcgis/rest/services/>

### geoOttawa

`HTML` `API` · *City of Ottawa*

Public map viewer over the ArcGIS services. Search by address, intersection, street segment or facility. Use for reconnaissance, then pull the layer from REST. Verified: a Web AppBuilder viewer over the maps.ottawa.ca/arcgis services (see the ArcGIS REST services root) plus tiles.arcgis.com vector tiles.

> **Verified** — access: confirmed
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: reachable but JavaScript-rendered · stage 2 2026-09-09: a real backing data API turned up in the browser · 1 archived_
- <https://maps.ottawa.ca/geoottawa/>

### Open Data policy and programme

`HTML` · *City of Ottawa*

Licence terms, publication commitments, and the request channel for datasets not yet released.

> **Verified** — access: confirmed
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · stage 2 2026-09-09: renders fully — a headless scrape works · 1 archived_
- <https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-data>


## 2. Electoral process, candidates, campaign finance

### Certified candidate list

`HTML` · *City of Ottawa (City Clerk)*

Authoritative roster of registered candidates: mayor, 24 wards, four school boards. Source of truth for who is on the ballot.

> **Verified** — access: confirmed
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · stage 2 2026-09-09: renders fully — a headless scrape works · 1 archived_
- <https://elections.ottawa.ca/CandidateList/CandidateList>

### Who is running in my ward?

`HTML` · *City of Ottawa*

Same roster behind an address lookup. Useful as a ward-boundary geocoding check.

> **Verified** — access: confirmed
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · stage 2 2026-09-09: renders fully — a headless scrape works · 1 archived_
- <https://ottawa.ca/en/city-hall/elections/voters/who-running-my-ward>

### Campaign financial statements and contributions

`HTML` · *City of Ottawa (City Clerk)*

Filed under Municipal Elections Act s.88.25, published free under s.88(9.1). Discloses name, address, date and amount for every contributor of $100 or more. Contribution cap $1,200 per candidate. Filing deadline 2pm the last Friday in March following the election, so 2026 filings land around March 2027.

> **Verified** — access: confirmed
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · stage 2 2026-09-09: renders fully — a headless scrape works · 2 archived_
- <https://ottawa.ca/en/city-hall/elections/candidates/candidate-campaign-finances-and-contributions>
- <https://ottawa.ca/en/city-hall/elections/previous-elections-and-appointment-processes/financial-statements-2022-municipal-elections/candidate-and-third-party-advertiser-compliance-reports>

### Election key dates and candidate information

`HTML` · *City of Ottawa*

Statutory calendar, nomination rules, third-party advertiser registration. 2026: nominations opened 1 May, close 21 August 2pm, Clerk certifies by 24 August, election 26 October.

> **Verified** — access: confirmed
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · stage 2 2026-09-09: renders fully — a headless scrape works · 2 archived_
- <https://ottawa.ca/en/city-hall/elections/learn-more-about-municipal-elections/key-dates-2026-municipal-elections>
- <https://ottawa.ca/en/city-hall/elections/candidates/information-candidates>

### Historical results and ward boundaries

`API` `Bulk` · *City of Ottawa / Wikipedia*

Poll-level results and ward boundary geometries publish to the open data portal. Wikipedia articles are the most convenient freely-licensed tabular version. Verified: on Open Ottawa's ArcGIS Hub (GeoServices API + CSV/GeoJSON/shapefile/KML).

> **Verified** — access: confirmed
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: machine-readable surface confirmed (ArcGIS Hub DCAT feed present (695 datasets)) · 2 archived_
- <https://open.ottawa.ca/>
- <https://en.wikipedia.org/wiki/2022_Ottawa_municipal_election>
- <https://en.wikipedia.org/wiki/2026_Ottawa_municipal_election>


## 3. Council proceedings, decisions, legislation

### eScribe: agendas, minutes, staff reports

`API` `HTML` · *City of Ottawa*

Every Council, standing committee and board meeting from 18 June 2012 onward. Staff reports attach as filestream.ashx?DocumentId=NNNNNN, a sequential integer, which makes systematic harvesting tractable. Richest untapped corpus in the catalogue. Verified: the meeting index (not the documents) is queryable at MeetingsCalendarView.aspx/GetCalendarMeetings; staff reports remain PDFs.

> **Verified** — access: confirmed
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · 1 archived_
- <https://pub-ottawa.escribemeetings.com/>

### Legacy agenda system (pre-2012)

`HTML` `Request` · *City of Ottawa*

Older documents. Anything before 2012 not here is held by the City Archives. Video from 2006 to 2012 is by request to Committees@ottawa.ca.

> **Verified** — access: unconfirmed (Request / FOI / in-person — not auto-verifiable)
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · 1 archived_
- <https://app06.ottawa.ca/cgi-bin/docs.pl?lang=en>

### Council meeting video and audio

`HTML` `API` · *City of Ottawa*

Live streams plus archived webcasts migrating from the old portal. Auto-captions make this searchable as text, a realistic route to a speech-level record of debate. Verified: the channel is a web page; text access is via the YouTube Data API or yt-dlp --write-auto-sub, not a City endpoint.

> **Verified** — access: unconfirmed — page is HTML; claimed `api` needs a key / login / manual check
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · stage 2 2026-09-09: renders fully — a headless scrape works · 1 archived_
- <https://www.youtube.com/channel/UCUR3i_hvk3-3i8vtrPg6v1Q>

### By-laws A to Z

`HTML` · *City of Ottawa*

Consolidated by-laws in HTML. Includes Procurement (2000-50), Lobbyist Registry, Integrity Commissioner (2021-7), Zoning (2026-50).

> **Verified** — access: confirmed
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · stage 2 2026-09-09: renders fully — a headless scrape works · 1 archived_
- <https://ottawa.ca/en/living-ottawa/laws-licences-and-permits/laws/laws-z>

### Document repository

`HTML` · *City of Ottawa*

Where most linked PDFs live: annual reports, manuals, primers, guides.

> **Verified** — access: confirmed
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · stage 2 2026-09-09: renders fully — a headless scrape works · 1 archived_
- <https://documents.ottawa.ca/>

### Council and committee structure

`HTML` · *City of Ottawa*

Membership, mandates and terms of reference for standing committees, sub-committees, adjudicative bodies and local boards.

> **Verified** — access: confirmed
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · stage 2 2026-09-09: renders fully — a headless scrape works · 1 archived_
- <https://ottawa.ca/en/city-hall/council-committees-and-boards>


## 4. Oversight offices, lobbying, disclosure

### Office of the Auditor General

`HTML` · *City of Ottawa (independent statutory officer)*

Performance, financial and compliance audits across all departments and agencies. Standalone site, separate from ottawa.ca. Example: Council Expenses Audit, November 2025.

> **Verified** — access: confirmed
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · stage 2 2026-09-09: renders fully — a headless scrape works · 1 archived_
- <https://www.oagottawa.ca/>

### Integrity Commissioner

`HTML` · *City of Ottawa (independent statutory officer)*

Codes of conduct, Municipal Conflict of Interest Act ss.5/5.1/5.2, closed-meeting investigations. Also serves as Lobbyist Registrar and Meetings Investigator: three mandates, one office.

> **Verified** — access: confirmed
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · stage 2 2026-09-09: renders fully — a headless scrape works · 1 archived_
- <https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/integrity-commissioner>

### Lobbyist Registry

`HTML` · *City of Ottawa*

Every substantive communication (call, meeting, email) between lobbyists and members of Council or staff. In force since 1 September 2012. Public search requires no login. Pairs naturally with development applications and council votes.

> **Verified** — access: confirmed
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · stage 2 2026-09-09: renders fully — a headless scrape works_
- <https://lobbyist.ottawa.ca/search/searchlobbyist.aspx?lang=en>
- <https://lobbyist.ottawa.ca/>

### MFIPPA disclosure log and access requests

`HTML` `Request` · *City of Ottawa (Access to Information and Privacy Office)*

Quarterly list of completed freedom-of-information requests of public interest. Records obtained by quoting the request number to mfippa@ottawa.ca. The route to anything not proactively published.

> **Verified** — access: unconfirmed (Request / FOI / in-person — not auto-verifiable)
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · 2 archived_
- <https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/public-disclosure/disclosure-mfippa-requests/general-information>
- <https://forms.ottawa.ca/en/form/occ/policy/mfippa-access-form>

### Members' office expenses and remuneration

`HTML` · *City of Ottawa*

Monthly per-member office expense disclosure plus the annual Statement of Remuneration, Benefits and Expenses required by the Municipal Act. Constituency Services Budget was $284,648 per ward councillor in 2023; the Mayor's was $970,646.

> **Verified** — access: confirmed
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · stage 2 2026-09-09: renders fully — a headless scrape works · 1 archived_
- <https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/public-disclosure/disclosure-office-expenses>

### Public Sector Salary Disclosure

`Bulk` · *Government of Ontario*

Provincial, but covers all city employees earning $100,000 or more. Published as bulk data by year and employer.

> **Verified** — access: confirmed
> licence: *Open Government Licence – Ontario*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · stage 2 2026-09-09: renders fully — a headless scrape works · 1 archived_
- <https://www.ontario.ca/page/public-sector-salary-disclosure>


## 5. Budgets, financial reporting, procurement, assessment

### Budget and financial reports

`HTML` · *City of Ottawa*

Audited annual financial statements, annual reports (2020 to 2024 online), and quarterly operating and capital budget status reports showing actual against budget by department.

> **Verified** — access: confirmed
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · stage 2 2026-09-09: renders fully — a headless scrape works · 1 archived_
- <https://ottawa.ca/en/city-hall/budget-finance-and-corporate-planning/financial-reports-and-statements>

### Budget documents by year

`HTML` `Bulk` · *City of Ottawa*

Tabled and adopted budgets, 2022 onward. Line-item detail generally in PDF; some budget data mirrored to Open Ottawa.

> **Verified** — access: unconfirmed — page is HTML; claimed `bulk` needs a key / login / manual check
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · stage 2 2026-09-09: renders fully — a headless scrape works · 1 archived_
- <https://ottawa.ca/en/city-hall/budget-finance-and-corporate-planning>

### Financial Information Return (FIR)

`API` `Bulk` · *Ontario Ministry of Municipal Affairs and Housing*

Province-mandated annual financial return under Municipal Act s.294(1), filed by 31 May. Data back to 1977 in a consistent schema across every Ontario municipality. The only clean way to benchmark Ottawa against peers. Verified: mirrored to data.ontario.ca (CKAN API v2.9.7) alongside the EFIS portal.

> **Verified** — access: confirmed
> licence: *Open Government Licence – Ontario*
> _stage 0–1 2026-09-09: machine-readable surface confirmed (CKAN API v2.9.7, 2963 datasets) · 1 archived_
- <https://efis.fma.csc.gov.on.ca/fir/>
- <https://data.ontario.ca/dataset/financial-information-return-fir-for-municipalities>

### Procurement and tenders **[verify]**

`HTML` · *City of Ottawa (Supply Services)*

Supply Services administers over $1B annually under By-law 2000-50. Bid opportunities post to a third-party e-tendering platform.

> **Verify:** Search results pointed at both Biddingo and third-party aggregators. Confirm the current platform before building against it.

> **Verified** — access: confirmed
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · stage 2 2026-09-09: renders fully — a headless scrape works · 2 archived_
- <https://ottawa.ca/en/business/procurement/procurement>
- <https://ottawa.ca/en/business/procurement/procurement-law>

### MPAC property assessment

`Request` · *Municipal Property Assessment Corporation*

Provincial corporation assessing all Ontario properties. Per-property values are access-restricted; aggregate assessment-roll data by class and municipality is published.

> **Verified** — access: unconfirmed (Request / FOI / in-person — not auto-verifiable)
> licence: *MPAC – access-restricted; aggregate roll only*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · 1 archived_
- <https://www.mpac.ca/>


## 6. Development applications, zoning, land use, appeals

### Development Applications Search

`API` `HTML` · *City of Ottawa*

Every planning application with reports, plans, status and comment windows. Stable per-application URLs of the form /en/applications/D07-12-19-0075/details, so the file-number scheme is enumerable. 28-day standard comment period. Verified: a JSON REST API backs the search - devapps-restapi.ottawa.ca/devapps/{feature,apptype,ward}/all - with a client-side authKey shipped to every browser.

> **Verified** — access: confirmed
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: reachable but JavaScript-rendered · stage 2 2026-09-09: a real backing data API turned up in the browser · 1 archived_
- <https://devapps.ottawa.ca/>

### Zoning By-law 2026-50

`HTML` `API` · *City of Ottawa*

Approved 28 January 2026, enacted 11 March 2026, replacing 2008-250 after roughly five years of consultation. Re-consolidated after every Council meeting that amends it, with margin notes flagging provisions under appeal.

> **Verified** — access: confirmed
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: machine-readable surface confirmed (ArcGIS service 'Layers': 8 layers, formats JSON, geoJSON) · stage 2 2026-09-09: renders fully — a headless scrape works · 2 archived_
- <https://ottawa.ca/en/living-ottawa/laws-licences-and-permits/laws/laws-z/zoning-law-law-no-2026-50>
- <https://maps.ottawa.ca/arcgis/rest/services/Zoning/MapServer>

### Official Plan

`HTML` · *City of Ottawa*

The 2021 Official Plan and its schedules: growth management, transects, urban boundary. The policy layer above zoning.

> **Verified** — access: confirmed
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · stage 2 2026-09-09: renders fully — a headless scrape works · 1 archived_
- <https://ottawa.ca/en/planning-development-and-construction>

### Committee of Adjustment decisions

`HTML` · *City of Ottawa / CanLII*

Ottawa was the first committee of adjustment in Canada to publish decisions on CanLII: keyword-searchable by street, ward or application type, in a citation-stable legal database. Also on eScribe.

> **Verified** — access: confirmed
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · stage 2 2026-09-09: renders fully — a headless scrape works · 1 link bot-blocked (fine in a browser) · 1 archived_
- <https://www.canlii.org/>
- <https://ottawa.ca/en/planning-development-and-construction/committee-adjustment/find-decision>

### Ontario Land Tribunal

`HTML` · *Government of Ontario*

Appeals of city planning and Committee of Adjustment decisions. Searchable by municipality; also mirrored on CanLII. Decisions older than ten years are by phone request.

> **Verified** — access: confirmed
> licence: *Open Government Licence – Ontario*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · stage 2 2026-09-09: a real backing data API turned up in the browser · 1 archived_
- <https://olt.gov.on.ca/decisions/>

### Building permits and land management

`Bulk` · *City of Ottawa*

Permit applications run through the My ServiceOttawa Land Management System. Issued-permit counts appear on Open Ottawa; per-permit detail is less consistently published.

> **Verified** — access: unconfirmed — page is HTML; claimed `bulk` needs a key / login / manual check
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · stage 2 2026-09-09: renders fully — a headless scrape works · 1 archived_
- <https://ottawa.ca/en/planning-development-and-construction/building-and-renovating>


## 7. Transit, roads, collisions, enforcement

### OC Transpo GTFS and GTFS-Realtime

`API` `Bulk` · *OC Transpo / City of Ottawa*

Static GTFS plus GTFS-RT Vehicle Positions and Trip Updates. Free API key via the Azure developer portal; commercial use permitted. Buses report GPS roughly every 30 seconds. Contact octranspo-dev@ottawa.ca.

> **Verified** — access: unconfirmed — page is HTML; claimed `api`, `bulk` needs a key / login / manual check
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · stage 2 2026-09-09: renders fully — a headless scrape works · 2 archived_
- <https://www.octranspo.com/en/plan-your-trip/travel-tools/developers/>
- <https://nextrip-public-api.developer.azure-api.net/>
- <https://www.transit.land/feeds/f-f24-octranspo>

### Traffic Ottawa open data

`API` · *City of Ottawa*

Its own open-data surface separate from the main portal: live traffic map, cameras, incidents, and service endpoints including automated speed enforcement camera locations.

> **Verified** — access: unconfirmed — page is HTML; claimed `api` needs a key / login / manual check
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: machine-readable surface confirmed · stage 2 2026-09-09: renders fully — a headless scrape works · 2 archived_
- <https://traffic.ottawa.ca/en/opendata>
- <https://traffic.ottawa.ca/map/service/ase_camera>

### Traffic collision data

`Bulk` `API` · *City of Ottawa / Ontario MTO*

All reportable collisions including property-damage-only, in CSV and shapefile. Sourced from MTO via Ottawa Police, OPP and RCMP. Every record validated at least once, roughly half twice. Verified: now published as per-year datasets on Open Ottawa, each with a GeoServices REST API plus CSV and shapefile.

> **Verified** — access: confirmed
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: machine-readable surface confirmed (ArcGIS Hub DCAT feed present (695 datasets)) · 1 archived_
- <https://open.ottawa.ca/search?q=traffic%20collision>
- <https://ottawa.ca/en/parking-roads-and-travel/road-safety/road-safety-action-plan/fatal-and-major-injury-collision-data>

### Automated speed enforcement

`Bulk` · *City of Ottawa*

Month-by-month charge and speed data for every camera location, plus siting methodology.

> **Verified** — access: unconfirmed — page is HTML; claimed `bulk` needs a key / login / manual check
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · stage 2 2026-09-09: renders fully — a headless scrape works · 1 archived_
- <https://ottawa.ca/en/parking-roads-and-travel/road-safety/enforcement/automated-speed-enforcement>

### Road network, pathways, cycling infrastructure

`API` `Bulk` · *City of Ottawa*

Centrelines, sidewalks, multi-use pathways, cycling routes, winter maintenance classes, as spatial layers with GeoJSON endpoints.

> **Verified** — access: confirmed
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: machine-readable surface confirmed (ArcGIS Hub DCAT feed present (695 datasets)) · 1 archived_
- <https://open.ottawa.ca/datasets/pathway-links/api>


## 8. Policing, fire, paramedic services

### Ottawa Police Community Safety Data Portal

`API` `Bulk` · *Ottawa Police Service*

Separate ArcGIS Hub launched November 2023, reported as 11 datasets, 7 dashboards and 6 web maps. Dashboards for homicides, shootings and gun seizures, overdose calls, hate- and bias-motivated crime, auto theft, and calls for service by priority. Being an ArcGIS Hub, everything has a GeoJSON endpoint.

> **Verified** — access: confirmed
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: machine-readable surface confirmed (ArcGIS Hub DCAT feed present (98 datasets)) · 1 archived_
- <https://data.ottawapolice.ca/>

### Crime Map (year to date)

`API` `Bulk` · *Ottawa Police Service / City of Ottawa*

Mirrored onto the city portal. Criminal offences open data also published directly by Ottawa Police. Verified: Open Ottawa ArcGIS Hub dataset (GeoServices API + CSV/GeoJSON/shapefile/KML).

> **Verified** — access: confirmed
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: machine-readable surface confirmed (ArcGIS Hub DCAT feed present (695 datasets)) · 1 archived_
- <https://open.ottawa.ca/datasets/crime-map-year-to-date/about>

### Police Services Board

`HTML` · *Ottawa Police Services Board*

Board agendas, minutes and reports run through the same eScribe instance as Council: budget, chief's reports, oversight items.

> **Verified** — access: confirmed
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · stage 2 2026-09-09: a real backing data API turned up in the browser · 1 archived_
- <https://pub-ottawa.escribemeetings.com/>

### Fire, paramedic and emergency services

`API` `Bulk` · *City of Ottawa*

Station locations, response-time performance and call volumes publish to the open data portal. Service-level detail also appears in annual departmental reports to committee. Verified: on Open Ottawa's ArcGIS Hub (GeoServices API + bulk formats).

> **Verified** — access: confirmed
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: machine-readable surface confirmed (ArcGIS Hub DCAT feed present (695 datasets)) · 1 archived_
- <https://open.ottawa.ca/>


## 9. Public health, housing, homelessness, social services

### Ottawa Public Health reports and dashboards

`HTML` · *Ottawa Public Health*

Seasonal respiratory and enteric outbreak surveillance, Diseases of Public Health Significance, COVID-19 vaccination, and the MHASUH dashboard for mental health, addictions and substance use health. Dashboards are interactive; underlying data is not consistently exposed.

> **Verified** — access: understated — also found `bulk`
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · stage 2 2026-09-09: renders fully — a headless scrape works · 1 archived_
- <https://www.ottawapublichealth.ca/en/reports-research-and-statistics/reports-research-and-statistics.aspx>

### Housing and homelessness: plans, facts and data

`HTML` · *City of Ottawa*

City dashboards on housing need and homelessness, plus the 10-Year Housing and Homelessness Plan and its progress reports.

> **Verified** — access: confirmed
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · stage 2 2026-09-09: renders fully — a headless scrape works · 1 archived_
- <https://ottawa.ca/en/family-and-social-services/housing-and-homelessness/plans-facts-and-data>

### Social Housing Registry of Ottawa

`HTML` · *Social Housing Registry of Ottawa (non-profit)*

Administers the centralized rent-geared-to-income wait list under the Housing Services Act, 2011, across roughly 50 providers. Wait list reported at 12,447 households (2023) rising to 15,140 (2024), with 1,155 households housed in 2024. Waits commonly exceed five years.

> **Verified** — access: confirmed
> licence: *Site terms – no open-data licence stated*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · stage 2 2026-09-09: renders fully — a headless scrape works · 1 archived_
- <https://housingregistry.ca/>

### Alliance to End Homelessness Ottawa

`HTML` · *Alliance to End Homelessness Ottawa*

Independent annual progress reports and the Ottawa Housing Needs Assessment. Often more pointed than the city's own framing, and a useful cross-check.

> **Verified** — access: confirmed
> licence: *Site terms – no open-data licence stated*
> _stage 0–1 2026-09-09: reachable but JavaScript-rendered · 1 archived_
- <https://www.endhomelessnessottawa.ca/>


## 10. Water, waste, watershed, utilities, green space

### Drinking water quality reports

`HTML` · *City of Ottawa*

Annual report per municipal system under the Safe Drinking Water Act, with full parameter-by-parameter test result tables. Roughly 293 million litres treated daily. Summaries also tabled at committee via eScribe.

> **Verified** — access: confirmed
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · stage 2 2026-09-09: renders fully — a headless scrape works · 1 archived_
- <https://ottawa.ca/en/living-ottawa/drinking-water-stormwater-and-wastewater/drinking-water>

### Solid waste data and reports

`HTML` · *City of Ottawa*

Diversion rates by stream and tonnages by programme. Residential diversion reported at 33 percent (2009) rising to 44 percent (2018); stream rates range from 40 percent for green-bin organics to 96 percent for leaf and yard waste.

> **Verified** — access: confirmed
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · stage 2 2026-09-09: renders fully — a headless scrape works · 1 archived_
- <https://ottawa.ca/en/garbage-and-recycling/solid-waste-data-and-reports>

### Ottawa Riverkeeper open data

`API` `Bulk` · *Ottawa Riverkeeper*

Independent watershed monitoring on its own ArcGIS Hub: water quality sampling and river health indicators, fully queryable.

> **Verified** — access: confirmed
> licence: *Site terms – no open-data licence stated*
> _stage 0–1 2026-09-09: machine-readable surface confirmed (ArcGIS Hub DCAT feed present (139 datasets)) · 1 archived_
- <https://ottawa-riverkeeper-open-data-ork-so.hub.arcgis.com/>

### Conservation authorities (RVCA, MVCA, SNC) **[verify]**

`HTML` `Bulk` · *Rideau Valley, Mississippi Valley and South Nation Conservation Authorities*

Three authorities cover Ottawa's watersheds. Each publishes floodplain mapping, watershed report cards and regulated-area layers: the binding constraint on much development, and often absent from city-only datasets.

> **Verify:** Individual authority URLs were not confirmed in search results.

> **Verified** — access: unconfirmed — page is HTML; claimed `bulk` needs a key / login / manual check
> licence: *Site terms – no open-data licence stated*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · stage 2 2026-09-09: renders fully — a headless scrape works · 3 archived_
- <https://www.rvca.ca/>
- <https://mvc.on.ca/>
- <https://www.nation.on.ca/>

### Hydro Ottawa **[verify]**

`HTML` · *Hydro Ottawa (municipally owned)*

Municipally-owned distributor. Outage map is live; rate filings and performance metrics are public through the Ontario Energy Board rather than the utility.

> **Verify:** No open data programme surfaced in searching.

> **Verified** — access: confirmed
> licence: *Site terms – no open-data licence stated*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · stage 2 2026-09-09: renders fully — a headless scrape works_
- <https://hydroottawa.com/>

### Trees, parks and green space

`API` `Bulk` · *City of Ottawa*

Tree inventory, forest cover, park and facility locations, sports fields, as spatial layers with GeoJSON endpoints.

> **Verified** — access: confirmed
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: machine-readable surface confirmed (ArcGIS Hub DCAT feed present (695 datasets)) · 1 archived_
- <https://open.ottawa.ca/>


## 11. 311, consultation, library, recreation

### Open311 and 311 service requests

`API` `Bulk` · *City of Ottawa (ServiceOttawa)*

Verified 2026-09-09: the GeoReport v2 API (city-of-ottawa-prod.apigee.net) is gone. Data now publishes as two rolling CSVs on Azure Blob Storage - 311opendatastorage.blob.core.windows.net/311data/311opendata_currentyear.csv (updated daily) and 311opendata_lastyear.csv - carrying ward, responsible department and request description; yearly archives back to 2012 on the portal.

> **Verified** — access: confirmed
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: machine-readable surface confirmed (ArcGIS Hub DCAT feed present (695 datasets))_
- <https://open.ottawa.ca/documents/ottawa::current-year-service-requests>
- <https://open.ottawa.ca/documents/ottawa::previous-year-service-requests>

### Engage Ottawa

`API` `HTML` · *City of Ottawa*

Consultation platform: open and closed projects, survey instruments, and published what-we-heard reports. The record of what the public actually said before a decision. Verified: runs on EngagementHQ; engage.ottawa.ca/api/v2/* serves projects, navigation and site metadata.

> **Verified** — access: confirmed
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · stage 2 2026-09-09: a real backing data API turned up in the browser · 1 archived_
- <https://engage.ottawa.ca/projects>
- <https://ottawa.ca/en/city-hall/public-engagement/public-engagement-project-search>

### Ottawa Public Library

`HTML` · *Ottawa Public Library*

Branch data, circulation statistics and curated local-statistics guides. Partners with the city on open-data outreach and is a practical access point for census and demographic products.

> **Verified** — access: confirmed
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · stage 2 2026-09-09: a real backing data API turned up in the browser · 1 archived_
- <https://collections.biblioottawalibrary.ca/>

### Recreation facilities and programmes

`API` `Bulk` · *City of Ottawa*

Facility locations, rinks, pools, programme registration data. Seasonal layers such as outdoor rink conditions update frequently. Verified: on Open Ottawa's ArcGIS Hub (GeoServices API + bulk formats).

> **Verified** — access: confirmed
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: machine-readable surface confirmed (ArcGIS Hub DCAT feed present (695 datasets)) · 1 archived_
- <https://open.ottawa.ca/>


## 12. Neighbourhood and demographic statistics

### Ottawa Neighbourhood Study

`Bulk` `API` · *Ottawa Neighbourhood Study*

Over 300 indicators per neighbourhood: demographics, socioeconomic conditions, housing, amenities, built environment, health. Custom boundaries built from census tracts plus fieldwork and stakeholder consultation. Layers also published to Open Ottawa. The richest small-area dataset for Ottawa.

> **Verified** — access: unconfirmed — page is HTML; claimed `api`, `bulk` needs a key / login / manual check
> licence: *Ottawa Neighbourhood Study – terms of use*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · 2 archived_
- <https://www.neighbourhoodstudy.ca/>
- <https://ons-sqo.ca/data-stories/>

### Neighbourhood Equity Index

`HTML` · *Ottawa Neighbourhood Study / partners*

Composite equity scoring across neighbourhoods, renewed 2024 with published methodology documentation. Useful as a ready-made weighting when one defensible composite is wanted rather than 300 raw indicators.

> **Verified** — access: confirmed
> licence: *Ottawa Neighbourhood Study – terms of use*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · 1 archived_
- <https://neighbourhoodequity.ca/>

### Community Data Program

`Request` · *Canadian Council on Social Development*

Consortium purchasing custom Statistics Canada tabulations for member organizations. Some products are members-only, but the Ottawa-region catalogue shows what exists.

> **Verified** — access: unconfirmed (Request / FOI / in-person — not auto-verifiable)
> licence: *Site terms – no open-data licence stated*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · 1 archived_
- <https://communitydata.ca/content/ottawa-and-region>

### Statistics Canada Census Profile

`Bulk` · *Statistics Canada*

Full profiles at census subdivision, metropolitan area, census tract and dissemination area. Bulk download available. Carleton's MacOdrum Library holds Ottawa-Gatineau census geography files back to 1951 for longitudinal work.

> **Verified** — access: unconfirmed — page is HTML; claimed `bulk` needs a key / login / manual check
> licence: *Statistics Canada Open Licence*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · stage 2 2026-09-09: renders fully — a headless scrape works · 1 archived_
- <https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/index.cfm?Lang=E>

### Ottawa Insights

`HTML` · *Ottawa Insights (cross-sector partnership)*

Community indicator project pulling city, health and social data into themed narratives: environment, economy, wellbeing.

> **Verified** — access: confirmed
> licence: *Site terms – no open-data licence stated*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · 1 archived_
- <https://www.ottawainsights.ca/>


## 13. Independent trackers and civic-technology projects

### OttWatch

`HTML` · *Independent*

The longest-running Ottawa civic monitor. Automatically scans ottawa.ca and eScribe for new agendas and documents, mirrors the lobbyist registry into a friendlier database, tracks new open-data publications, and maintains its own development application index. Closest thing to prior art for most projects in this space.

> **Verified** — access: confirmed
> licence: *Site terms – no open-data licence stated*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · 1 archived_
- <https://ottwatch.ca/>
- <https://ottwatch.ca/devapp/index>

### Horizon Ottawa Vote Tracker

`HTML` · *Horizon Ottawa (advocacy)*

How each councillor voted across the 2022 to 2026 term, filterable by councillor, topic and committee. Advocacy-run, so vote selection is editorial, but fills a real gap since Ontario does not require municipalities to publish recorded votes.

> **Verified** — access: confirmed
> licence: *Site terms – no open-data licence stated*
> _stage 0–1 2026-09-09: reachable but JavaScript-rendered_
- <https://www.horizonottawa.ca/vote_tracker>

### How They Voted

`API` `HTML` · *Independent*

Dedicated Ottawa council voting-record site. Verified 2026-09-09: ships its compiled record as JSON at howtheyvoted.ca/data/ottawa/index.json and /data/ottawa/dates/<YYYY-MM-DD>.json, current to within days. Independent project on ordinary site terms - usable as a secondary source, not re-publishable as open data.

> **Verified** — access: confirmed
> licence: *Site terms – no open-data licence stated*
> _stage 0–1 2026-09-09: reachable but JavaScript-rendered · 1 archived_
- <https://howtheyvoted.ca/>

### Ottawa Lookout

`HTML` · *Ottawa Lookout (local newsroom)*

Runs the most complete 2026 candidate tracker and per-ward election guides. Journalism rather than data, but consistently ahead of official publication.

> **Verified** — access: confirmed
> licence: *All rights reserved (journalism)*
> _stage 0–1 2026-09-09: reachable but JavaScript-rendered · 2 archived_
- <https://www.ottawalookout.com/p/meet-the-candidates>
- <https://www.ottawalookout.com/>

### Ottawa Civic Tech

`HTML` · *Volunteer community*

Volunteer community with an active meetup and public GitHub organization. The obvious place to find collaborators or avoid duplicating existing work. (ottawacivictech.ca was unreachable at last verification; the GitHub org is the live home.)

> **Verified** — access: understated — also found `bulk`
> licence: *Varies by project*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · broken — https://www.ottawacivictech.ca/ → no DNS · 2 archived_
- <https://github.com/YOWCT>
- <https://www.ottawacivictech.ca/>

### ACORN Canada housing voting records

`HTML` · *ACORN Canada (advocacy)*

Issue-specific scorecard on councillors' affordable-housing votes. Narrow and openly advocacy-framed, but sourced to actual votes.

> **Verified** — access: confirmed
> licence: *Site terms – no open-data licence stated*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · 1 archived_
- <https://acorncanada.org/resources/ottawa-voting-records-report/>


## 14. Non-municipal bodies governing land or services in Ottawa

### National Capital Commission

`Bulk` `API` · *National Capital Commission (federal crown corporation)*

Owns the Greenbelt, Gatineau Park, much of the waterfront and many major parkways. Publishes through the federal open government portal and as a layer on Open Ottawa.

> **Verified** — access: confirmed
> licence: *Open Government Licence – Canada*
> _stage 0–1 2026-09-09: machine-readable surface confirmed (ArcGIS Hub DCAT feed present (695 datasets)) · 1 archived_
- <https://open.ottawa.ca/datasets/ncc-open-data-map/about>
- <https://search.open.canada.ca/opendata/?owner_org=ncc-ccn>

### Open Government Canada

`API` `Bulk` · *Government of Canada*

Federal datasets filterable to the National Capital Region: federal property holdings, employment, transfers to municipalities.

> **Verified** — access: unconfirmed — page is HTML; claimed `api`, `bulk` needs a key / login / manual check
> licence: *Open Government Licence – Canada*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · 1 archived_
- <https://open.canada.ca/>

### Ontario Open Data

`API` `Bulk` · *Government of Ontario*

Provincial datasets that determine much of what the city can do: FIR, health, education, transfers, licensing.

> **Verified** — access: confirmed
> licence: *Open Government Licence – Ontario*
> _stage 0–1 2026-09-09: machine-readable surface confirmed (CKAN API v2.9.7, 2963 datasets) · 1 archived_
- <https://data.ontario.ca/>

### School boards (OCDSB, OCSB, CEPEO, CECCE) **[verify]**

`HTML` · *Four Ottawa school boards*

Four boards elect trustees on the municipal ballot but govern independently, with their own budgets, minutes and enrolment data. Frequently omitted from municipal data projects despite appearing on the same ballot.

> **Verify:** Individual board URLs were not confirmed in search results.

> **Verified** — access: confirmed
> licence: *Site terms – no open-data licence stated*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML · stage 2 2026-09-09: renders fully — a headless scrape works · broken — https://ecolecatholique.ca/ → no DNS · 4 archived_
- <https://ocdsb.ca/>
- <https://ocsb.ca/>
- <https://cepeo.on.ca/>
- <https://ecolecatholique.ca/>


## 15. Historical record

### City of Ottawa Archives

`Request` · *City of Ottawa*

Over 20 kilometres of records in climate-controlled vaults at 100 Tallwood Drive, plus photographs, maps, architectural drawings and a 16,000-volume reference library. Holds pre-amalgamation municipal records and everything predating the 2012 eScribe cutover. Mostly paper, consulted on-site; order materials two working days ahead.

> **Verified** — access: unconfirmed (Request / FOI / in-person — not auto-verifiable)
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: reachable, server-rendered HTML_
- <https://ottawa.ca/en/arts-heritage-and-events/city-ottawa-archives/archives-collection>

### Historical aerial imagery and mapping

`HTML` `API` · *City of Ottawa / university libraries*

geoOttawa carries historical air-photo layers going back decades. Carleton and uOttawa GIS libraries hold digitized historical map series for the region. Verified: served through the geoOttawa viewer; the air-photo layers are ArcGIS services under maps.ottawa.ca/arcgis.

> **Verified** — access: confirmed
> licence: *Open Government Licence – City of Ottawa*
> _stage 0–1 2026-09-09: reachable but JavaScript-rendered · stage 2 2026-09-09: a real backing data API turned up in the browser · 1 archived_
- <https://maps.ottawa.ca/geoottawa/>


## Where the gaps are

Patterns worth noting when deciding what to build.

1. **Recorded votes are not published as data.** Ontario does not require municipalities to
   publish councillor voting records. Ottawa's votes exist only as prose inside eScribe minutes.
   Every vote tracker in the catalogue is a volunteer or advocacy group re-keying them by hand —
   the clearest unmet need here. (Stage 2 note: `howtheyvoted.ca` ships its compiled record as
   JSON at `/data/ottawa/…`, and is current — a usable secondary source.)

2. **eScribe is a corpus, not an API.** Fourteen years of agendas, minutes and staff reports sit
   behind sequential `DocumentId` integers with no search API, no bulk export, and no structured
   metadata. Everything downstream — votes, spending decisions, planning history — is locked in
   PDFs. (Stage 2 note: the meeting *index* is reachable via
   `MeetingsCalendarView.aspx/GetCalendarMeetings`; the documents still are not.)

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
Open Government Licence – City of Ottawa, but check each one.

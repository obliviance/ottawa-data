# Ottawa governance & community: an information-source hierarchy

A structural map of *every* institution and organisation that produces information about how
Ottawa is governed and how its community is doing — then each branch is tagged with whether that
information is **open**, **closed**, or **unknown**.

This is a companion to [`sources.json`](sources.json). Where that file is a flat list of 72
catalogued sources, this file is the tree they hang from: it names the branches that are *not*
yet catalogued so the shape of the gap is visible.

## Status vocabulary

| Mark | Meaning |
| --- | --- |
| 🟢 **Open** | Published publicly in a usable form — a live API, a bulk download (CSV / GeoJSON / shapefile / XLS), or HTML structured enough to parse reliably. |
| 🟡 **Partial** | Public but constrained: PDF-only, interactive-dashboard-only with no underlying data, aggregate-only when the unit record is what matters, or unstructured HTML that needs scraping. |
| 🔴 **Closed** | Not available as public data: freedom-of-information / written-request only, paywalled, members-only, in-person only, or simply never published in any form. |
| ⚪ **Unknown** | Existence, publication status, or access form has not been verified. |

The catalogue column links to `sources.json` ids: `[id]` = catalogued, `[id] ⚑` = catalogued
with an open verify-flag, `—` = not yet catalogued.

> **Verification status.** The **72 catalogued rows** (`[id]`) have been opened and checked in
> stages 0–3 — liveness, machine-readable surface, a headless-browser render, and access-tag +
> licence confirmation (records in [`verification/`](verification/), method in
> [`tools/VERIFYING.md`](tools/VERIFYING.md)); their `sources.json` tags and descriptions are
> now corrected. The **uncatalogued rows** (`—`) are still unverified: a 🟢 there means "believed
> public on general knowledge", a lead to check. Marks on split-status rows are best estimates.

---

## A. City of Ottawa — the municipal corporation

### A1. Council & legislative process

| Source | Status | Catalogue |
| --- | --- | --- |
| Council agendas, minutes, staff reports (eScribe, 2012–present) | 🟡 corpus of PDFs behind sequential `DocumentId`; the meeting *index* is queryable (`MeetingsCalendarView.aspx/GetCalendarMeetings`), the documents are not | `[escribe]` |
| Pre-2012 agendas & reports (legacy system + Archives) | 🟡 / 🔴 older material by request | `[legacy-agendas]` |
| Council & committee video / audio (YouTube, auto-captioned) | 🟢 stream + captions; 🔴 pre-2012 video by email request | `[council-video]` |
| **Recorded councillor votes as structured data** | 🔴 **not published** — exist only as prose in minutes; Ontario imposes no requirement | — |
| Motions & directions to staff (tracked status) | 🟡 inside eScribe; no register | — |
| By-laws A–Z (consolidated) | 🟡 HTML, no API, no change-feed | `[bylaws-az]` |
| Committee / sub-committee / advisory-committee structure, mandates, membership | 🟡 HTML | `[council-structure]` |
| Delegated-authority reports (staff decisions under delegated power) | ⚪ tabled to committee; not separately indexed | — |
| Councillor ward pages, newsletters, office activity | 🟡 scattered HTML / mailing lists | — |
| Document repository (reports, manuals, primers) | 🟡 PDF library | `[documents-repo]` |

### A2. Elections & democratic process (City Clerk)

| Source | Status | Catalogue |
| --- | --- | --- |
| Certified candidate list — mayor, 24 wards, 4 school boards | 🟡 HTML roster | `[candidate-list]` |
| "Who is running in my ward?" address lookup | 🟡 HTML | `[who-is-running]` |
| Nomination filings / statutory calendar / third-party advertiser registry | 🟡 HTML | `[election-key-dates]` |
| **Campaign financial statements & contributor lists ($100+ itemised)** | 🔴 per-candidate PDF/HTML; no consolidated contributor dataset; 2026 filings land ~March 2027 | `[campaign-finance]` |
| Compliance-audit committee proceedings & decisions | ⚪ tabled; not indexed as a set | — |
| Poll-level historical results | 🟢 to Open Ottawa; Wikipedia is the convenient tabular form | `[election-results-history]` |
| Ward boundary geometries + boundary-review / OLT appeal record | 🟢 geometry on Open Ottawa; 🟡 review documents in PDF | `[election-results-history]` |
| Voters' list / MPAC enumeration data | 🔴 not public | — |
| Turnout by ward / advance / special ballot | 🟡 in results reports | — |

### A3. Executive & administration

| Source | Status | Catalogue |
| --- | --- | --- |
| Departmental structure / org charts | 🟡 HTML | — |
| Corporate & strategic plans, term-of-council priorities | 🟡 PDF | — |
| Annual reports (2020–2024 online) | 🟡 PDF | `[financial-reports]` |
| Performance / service-standard reporting (City Scorecard etc.) | ⚪ historically intermittent | — |
| Collective agreements (CUPE 503, ATU 279, IAFF, OPSEU, etc.) | 🟡 / 🔴 some tabled, some by request | — |
| Workforce / staffing / diversity data | 🟡 aggregate in annual reports; unit data 🔴 | — |
| Directives, policies, administrative procedures | 🟡 selective HTML; full set 🔴 by request | — |

### A4. Finance

| Source | Status | Catalogue |
| --- | --- | --- |
| Budgets — draft, tabled, adopted (2022–present) | 🟡 line-item detail is PDF; some series mirrored to Open Ottawa | `[budget-documents]` |
| Audited annual financial statements / ACFR | 🟡 PDF | `[financial-reports]` |
| Quarterly operating & capital budget status reports | 🟡 PDF, actual-vs-budget by department | `[financial-reports]` |
| Financial Information Return (province-wide schema, back to 1977) | 🟢 bulk; the one clean cross-municipality benchmark | `[fir]` |
| **Vendor / supplier payment disclosure** (who got paid, how much) | 🔴 not published | — |
| **Contract award register** (winner, value, amendments, sole-source) | 🔴 / ⚪ not published as data | — |
| Bid opportunities / tenders | 🟡 posted to a third-party e-tendering platform + Ottawa Construction Association bulletin; platform identity needs confirming | `[procurement] ⚑` |
| Development charges — rates, background studies, reserve balances | 🟡 PDF | — |
| Reserve funds, debt, long-range financial plan | 🟡 PDF | — |
| Asset management plan (O. Reg. 588/17) | 🟡 PDF; some condition data spatial | — |
| Property tax rates, ratios, levy by class | 🟡 HTML / by-law | — |
| User-fee schedule | 🟡 by-law annex | — |
| Grants & contributions (community, recreation, cultural funding) | 🟡 recipient lists in committee reports | — |
| Investment holdings / ONE Investment | 🟡 in financial statements | — |

### A5. Accountability & oversight offices

| Source | Status | Catalogue |
| --- | --- | --- |
| Office of the Auditor General — performance / financial / compliance audits | 🟡 standalone site, PDF reports | `[auditor-general]` |
| Fraud & Waste Hotline annual reports | 🟡 PDF via OAG | — |
| Integrity Commissioner — inquiry reports, advice, codes of conduct | 🟡 HTML / PDF | `[integrity-commissioner]` |
| Meetings Investigator (closed-meeting investigations) | 🟡 report-by-report | `[integrity-commissioner]` |
| MFIPPA disclosure log (completed FOI requests of public interest) | 🟡 quarterly HTML list; records themselves 🔴 by request number | `[mfippa-disclosure]` |
| MFIPPA access-request form / statistics | 🔴 / 🟡 annual stats to IPC only | `[mfippa-disclosure]` |
| Members' office expense disclosure (monthly) | 🟡 HTML tables | `[office-expenses]` |
| Statement of Remuneration, Benefits and Expenses (annual, Municipal Act) | 🟡 PDF | `[office-expenses]` |
| Public Sector Salary Disclosure ("Sunshine List", $100k+) | 🟢 provincial bulk, by year & employer | `[sunshine-list]` |
| Hospitality / travel / sponsorship disclosure | ⚪ partial, buried | — |
| Ontario Ombudsman — municipal complaints & investigations | 🟡 Ontario-wide reports | — |

### A6. Lobbying & influence

| Source | Status | Catalogue |
| --- | --- | --- |
| Lobbyist Registry — every substantive communication, since Sept 2012 | 🟡 public search, no login, no API/bulk export | `[lobbyist-registry]` |
| Gift Registry (gifts to members of Council) | ⚪ required by code of conduct; publication form unconfirmed | — |
| Sponsorship & advertising agreements | ⚪ | — |

### A7. Land use, planning & development

| Source | Status | Catalogue |
| --- | --- | --- |
| Development Applications Search (OPA, ZBA, subdivision, site plan, consent, minor variance) | 🟢 a JSON REST API backs the search (`devapps-restapi.ottawa.ca/devapps/…`, client-side key); reports still PDF | `[devapps]` |
| Zoning By-law 2026-50 (enacted 11 Mar 2026) | 🟡 HTML text + 🟢 spatial layer | `[zoning-2026-50]` |
| Official Plan (2021) + secondary/​community plans + schedules | 🟡 PDF policy layer | `[official-plan]` |
| Committee of Adjustment decisions | 🟢 on CanLII (citation-stable, searchable) + eScribe | `[committee-of-adjustment]` |
| Ontario Land Tribunal — planning & CofA appeals | 🟡 searchable by municipality; 🟢-ish via CanLII mirror; >10 yrs by phone | `[olt]` |
| Building permits | 🟡 issued-permit counts on Open Ottawa; per-permit detail inconsistent | `[building-permits]` |
| Heritage register, designations, Built Heritage Committee | 🟡 register HTML/PDF; some spatial | — |
| Urban Design Review Panel records | ⚪ | — |
| Community Improvement Plans / brownfield grants | 🟡 PDF | — |
| Parkland dedication / cash-in-lieu accounting | 🔴 / ⚪ | — |
| Site-alteration & tree-protection permits (urban/rural) | ⚪ | — |
| Infrastructure & servicing master plans | 🟡 PDF | — |
| Site plan control agreements / registered conditions | 🔴 on title (see J) | — |

### A8. Transportation & mobility

| Source | Status | Catalogue |
| --- | --- | --- |
| OC Transpo static GTFS + GTFS-Realtime (vehicle positions, trip updates) | 🟢 free key, commercial use allowed | `[octranspo-gtfs]` |
| OC Transpo ridership / route productivity / on-time performance | 🟡 aggregate in reports; route-level 🔴 | — |
| Para Transpo service data | 🔴 / ⚪ | — |
| O-Train / LRT — Stage 1/2/3 status, RTG performance, maintenance, public inquiry record | 🟡 PDF + inquiry archive; reliability data 🟡 | — |
| Road network / centrelines / sidewalks / pathways / cycling routes / winter classes | 🟢 spatial layers, GeoJSON | `[road-network]` |
| Traffic Ottawa open data — live map, cameras, incidents, ASE camera locations | 🟢 own endpoints | `[traffic-ottawa]` |
| Traffic collision data (all reportable, incl. PDO) — CSV + shapefile | 🟢 | `[collisions]` |
| Fatal & major-injury collision detail / Road Safety Action Plan | 🟡 PDF + dataset | `[collisions]` |
| Automated speed enforcement — monthly charges & speeds by camera | 🟢 bulk | `[automated-speed-enforcement]` |
| Red-light camera data | ⚪ likely similar to ASE | — |
| Traffic counts / volumes / turning-movement counts | 🟡 some on portal, patchy | — |
| Parking — on-street inventory, garages, permits, ticket/enforcement volumes | 🟡 / 🔴 ticket data by request | — |
| Road construction / closures / lane occupancy permits | 🟡 map feed | — |
| Transportation Master Plan, Vision Zero, Complete Streets | 🟡 PDF | — |
| Traffic-calming program pipeline & rankings | 🟡 PDF | — |
| Speed limit / school zone / community safety zone layers | 🟢 likely spatial | — |

### A9. Public safety & protective services

| Source | Status | Catalogue |
| --- | --- | --- |
| Ottawa Police Service — Community Safety Data Portal (ArcGIS Hub) | 🟢 datasets + dashboards, GeoJSON endpoints | `[ops-data-portal]` |
| Crime Map / criminal-offences open data | 🟢 mirrored to city portal | `[crime-map]` |
| OPS calls for service by priority / response times | 🟢 dashboard + likely dataset | `[ops-data-portal]` |
| OPS use-of-force reporting | 🟡 annual report | — |
| OPS race-based / traffic-stop data | 🟡 periodic studies; ongoing unit data 🔴 | — |
| OPS budget, business plan, chief's reports | 🟡 via Police Services Board eScribe | `[police-services-board]` |
| Police Services Board agendas / minutes / reports | 🟡 eScribe | `[police-services-board]` |
| Police collective agreement | 🔴 / 🟡 | — |
| Public complaints against police (Law Enforcement Complaints Agency) | 🟡 LECA Ontario-wide stats | — |
| Special Investigations Unit — Ottawa-area cases | 🟡 SIU director's reports | — |
| Ottawa Fire Services — station locations, response times, call volumes, incident types | 🟢 to Open Ottawa | `[fire-paramedic]` |
| Fire prevention / inspection / order data | 🔴 / ⚪ | — |
| Ottawa Paramedic Service — response times, call volumes, offload delay | 🟢 / 🟡 | `[fire-paramedic]` |
| Office of Emergency Management — plans, activations, after-action | 🟡 / 🔴 | — |
| By-law & Regulatory Services — enforcement statistics by type | 🟡 some on portal, patchy | — |
| Business licensing (incl. taxi / limo / TNC / tow) | 🟡 / ⚪ | — |
| Short-term rental registrations & enforcement | 🟡 some dashboards | — |
| Animal control / licensing / shelter data | 🟡 / ⚪ | — |
| Property Standards orders / vacant-building registry | 🔴 / ⚪ | — |
| 911 / dispatch performance | 🟡 aggregate | — |

### A10. Health & human services

| Source | Status | Catalogue |
| --- | --- | --- |
| Ottawa Public Health — reports, surveillance, MHASUH dashboard | 🟡 dashboards interactive; underlying data not consistently exposed | `[ottawa-public-health]` |
| Board of Health agendas / minutes | 🟡 eScribe | — |
| Food / personal-service / pool / tobacco-vaping inspection results | 🟡 public disclosure search; bulk 🔴/⚪ | — |
| Substance-use / harm-reduction / drug-checking / overdose data | 🟡 dashboard | `[ottawa-public-health]` |
| Immunization coverage (school / COVID) | 🟡 dashboard | `[ottawa-public-health]` |
| City-run long-term care homes (4) — occupancy, inspections, quality | 🟡 provincial inspection reports; city ops data 🔴 | — |
| Child care — subsidy caseload, licensed spaces, wait list, registry | 🟡 / 🔴 | — |
| Ontario Works / social-assistance caseload | 🟡 aggregate; provincial | — |
| Housing Services — community housing portfolio, RGI, rent supplement | 🟡 in reports | `[housing-homelessness]` |
| Centralized social-housing wait list (Social Housing Registry) | 🟡 annual figures in reports; unit data 🔴 | `[social-housing-registry]` |
| Homelessness — shelter occupancy, HIFIS, coordinated access, point-in-time counts | 🟡 dashboards + periodic PDF counts | `[housing-homelessness]` |
| 10-Year Housing & Homelessness Plan + progress reports | 🟡 PDF | `[housing-homelessness]` |
| Community funding recipients / Community Development Framework | 🟡 lists in reports | — |
| Newcomer / immigration / settlement (Ottawa Local Immigration Partnership) | 🟡 PDF | — |
| Anti-Racism Secretariat / equity strategy reporting | 🟡 PDF | — |
| Gender / equity / accessibility (Municipal Accessibility Plan) | 🟡 PDF | — |

### A11. Environment, water, waste, utilities

| Source | Status | Catalogue |
| --- | --- | --- |
| Drinking-water quality — annual parameter-by-parameter reports | 🟡 HTML/PDF tables | `[drinking-water]` |
| Wastewater / stormwater — ROPEC performance, combined-sewage-overflow ("sewage tank") data | 🟡 real-time overflow site exists; historical 🟡 | — |
| Ottawa River Action Plan progress | 🟡 PDF | — |
| Solid waste — diversion rates, tonnages by stream, Trail Road landfill | 🟡 HTML/PDF | `[solid-waste]` |
| Solid Waste Master Plan / green-bin / curbside-change monitoring | 🟡 PDF | — |
| Source-water protection (Mississippi-Rideau region) | 🟡 plan + some spatial | — |
| Climate — Climate Change Master Plan, Energy Evolution, GHG inventory | 🟡 PDF; inventory sometimes tabular | — |
| Air quality | 🟡 provincial monitoring (MECP) + advisories | — |
| Contaminated sites / brownfields / spills | 🔴 / ⚪ mostly provincial | — |
| Tree inventory, canopy cover, Urban Forest Management Plan | 🟢 inventory spatial; plan PDF | `[trees-parks]` |
| Naturalization / forest-management / woodland data | 🟡 / 🟢 spatial | — |
| Wells & septic (rural) — permits, inspections | 🔴 / ⚪ | — |
| Stormwater / drainage infrastructure layers | 🟢 likely spatial | — |

### A12. Parks, recreation, culture, facilities

| Source | Status | Catalogue |
| --- | --- | --- |
| Parks & facilities inventory (spatial) | 🟢 GeoJSON | `[trees-parks]` |
| Recreation facilities & programme registration data | 🟢 facility layers; registration data 🟡 | `[recreation]` |
| Outdoor rink conditions / splash pads / beach water quality | 🟢 seasonal layers + beach sampling | `[recreation]` |
| Sports-field inventory & allocation | 🟢 / 🟡 | `[trees-parks]` |
| Public art inventory | 🟡 / 🟢 | — |
| City of Ottawa Museums Network | 🟡 HTML | — |
| Cultural / festival / special-event funding & permits | 🟡 recipient lists; permit data 🔴 | — |
| Cemeteries operated by the city | 🟡 / ⚪ | — |

### A13. Real estate, assets & internal services

| Source | Status | Catalogue |
| --- | --- | --- |
| Land inventory / surplus-land pipeline / property disposals | 🟡 committee reports; 🟢 some spatial | — |
| Corporate real-estate holdings & leases | 🔴 / ⚪ | — |
| Facilities condition assessment | 🟡 aggregate in asset-management plan | — |
| Fleet inventory / electrification | 🟡 in reports | — |
| IT / digital systems, digital master plan, cyber posture | 🟡 / 🔴 | — |

### A14. Rural & agricultural

| Source | Status | Catalogue |
| --- | --- | --- |
| Agriculture & Rural Affairs Committee proceedings | 🟡 eScribe | `[escribe]` |
| Municipal drains / Drainage Act petitions, assessments, engineer's reports | 🔴 / ⚪ mostly paper | — |
| Rural road / private-road / unopened-road-allowance data | 🟡 / ⚪ | — |
| Village plans / rural settlement boundaries | 🟡 PDF + spatial | — |
| Agricultural land / soil-class / prime-ag designations | 🟢 spatial | — |

### A15. Engagement, 311 & communications

| Source | Status | Catalogue |
| --- | --- | --- |
| 311 service requests — rolling CSVs (current + last year) + yearly archives to 2012 | 🟢 `311opendatastorage.blob.core.windows.net/311data/…`; the GeoReport v2 API is **gone** (apigee host dead) | `[open311]` |
| Engage Ottawa — open/closed consultations, surveys, what-we-heard reports | 🟢 EngagementHQ REST API (`engage.ottawa.ca/api/v2/…`) behind the HTML | `[engage-ottawa]` |
| Public notices (planning, road, statutory) | 🟡 HTML feeds | — |
| Media releases / newsroom | 🟡 HTML | — |
| Councillor & city social-media output | 🟡 platform-dependent | — |

### A16. Records & archives

| Source | Status | Catalogue |
| --- | --- | --- |
| City of Ottawa Archives — pre-amalgamation & pre-2012 records, photos, maps, drawings | 🔴 mostly paper, on-site, 2-day retrieval | `[city-archives]` |
| Corporate records-retention schedules | 🟡 / ⚪ | — |
| Historical air-photo & map layers (geoOttawa) | 🟡 viewer; university GIS libraries hold series | `[historical-imagery]` |

### A-cross. Portals & spatial infrastructure

| Source | Status | Catalogue |
| --- | --- | --- |
| Open Ottawa / Données ouvertes (ArcGIS Hub catalogue) | 🟢 GeoService + GeoJSON + CSV + shapefile + KML | `[open-ottawa]` |
| City ArcGIS REST services root (Zoning, Basemap, TopographicMapping) | 🟢 raw MapServer directory | `[arcgis-rest-root]` |
| geoOttawa map viewer | 🟡 reconnaissance UI over the REST services | `[geoottawa]` |
| Open Data policy, licence terms, dataset-request channel | 🟡 HTML | `[open-data-policy]` |

---

## B. Municipal agencies, boards, commissions & corporations (ABCs)

| Body | What it holds | Status | Catalogue |
| --- | --- | --- | --- |
| Ottawa Police Services Board | Agendas, minutes, budget, oversight — see A9 | 🟡 eScribe | `[police-services-board]` |
| Ottawa Board of Health / Ottawa Public Health | See A10 | 🟡 | `[ottawa-public-health]` |
| Ottawa Public Library Board | Board records, branch data, circulation statistics, local-history collections | 🟡 board PDF; 🟢 digitised collections; circulation 🟡 | `[opl]` |
| Ottawa Community Housing Corp. (OCH) | ~15,500 homes, ~33,000 tenants; annual reports, AGM to Council, tenant surveys | 🟡 annual report PDF (och-lco.ca); unit-level portfolio / arrears / turnover 🔴 | — |
| Ottawa Community Housing Foundation | Grants, programmes | 🟡 annual report | — |
| Hydro Ottawa Holding Inc. (Hydro Ottawa Ltd., Envari, Portage Power) | Distribution performance, rate applications, annual report, outage map | 🟢 live outage map; 🟡 OEB rate filings; no open-data programme surfaced | `[hydro-ottawa] ⚑` |
| Committee of Adjustment | Minor-variance & consent decisions — see A7 | 🟢 CanLII | `[committee-of-adjustment]` |
| Built Heritage Committee | Heritage designations & permits — see A7 | 🟡 eScribe | — |
| Business Improvement Areas (~19, each a local board) | Individual budgets, levies, board minutes, AGMs | 🟡 / 🔴 varies wildly by BIA | — |
| ByWard Market District Authority (Municipal Services Corp., est. 14 Jun 2023) | Manages ByWard + Parkdale public markets; annual report to Council; vendor/stall data | 🟡 annual report; operational data 🔴 | — |
| Crime Prevention Ottawa | Research reports, community-safety data syntheses | 🟡 PDF | — |
| Ottawa Community Lands Development Corp. (OCLDC) | Municipal land development (e.g. Greystone, Rochester) | 🟡 / 🔴 project pages | — |
| Election Compliance Audit Committee | Campaign-finance audit applications & decisions | ⚪ tabled, not indexed | — |
| Property Standards & Licence Appeal committees | Appeal decisions | 🔴 / ⚪ | — |
| Debenture Committee / Audit Committee | Debt issuance, audit workplan | 🟡 eScribe | — |
| Pineview Municipal Golf Club | Board records, financials | 🔴 / ⚪ | — |
| Rural clean-water / drainage boards | See A14 | 🔴 | — |

---

## C. School boards (trustees elected on the municipal ballot; govern independently)

| Body | What it holds | Status | Catalogue |
| --- | --- | --- | --- |
| Ottawa-Carleton District School Board (OCDSB) | Board & committee agendas/minutes, budget, enrolment, capital & accommodation plans, attendance boundaries, director's reports | 🟡 board portal + PDF; boundaries sometimes spatial | `[school-boards] ⚑` |
| Ottawa Catholic School Board (OCSB) | Same categories | 🟡 | `[school-boards] ⚑` |
| Conseil des écoles publiques de l'Est de l'Ontario (CEPEO) | Same categories | 🟡 | `[school-boards] ⚑` |
| Conseil des écoles catholiques du Centre-Est (CECCE) | Same categories | 🟡 | `[school-boards] ⚑` |
| Trustee voting records | 🔴 not published as data (same gap as Council) | — |
| Ottawa Student Transportation Authority (OSTA — OCDSB/OCSB consortium) | Routes, eligibility, delays/cancellations, contracts | 🟡 cancellation feed; route & contract data 🔴 | — |
| EQAO assessment results (by school) | 🟢 provincial, downloadable | — |
| Ministry of Education school-facility & funding data (SIF, capital priorities) | 🟢 / 🟡 provincial | — |

---

## D. Watershed governance — conservation authorities

| Body | What it holds | Status | Catalogue |
| --- | --- | --- | --- |
| Rideau Valley Conservation Authority (RVCA) | Floodplain mapping, regulated-area layers, s.28/Section 28 permits, watershed report cards, water-quality & stream monitoring, conservation lands | 🟡 / 🟢 report cards + some spatial; permit data 🔴; **URLs unconfirmed** | `[conservation-authorities] ⚑` |
| Mississippi Valley Conservation Authority (MVCA) | Same categories | 🟡 / ⚪ | `[conservation-authorities] ⚑` |
| South Nation Conservation (SNC) | Same categories | 🟡 / ⚪ | `[conservation-authorities] ⚑` |
| Mississippi-Rideau Source Protection Region | Source-protection plan, vulnerable-area mapping | 🟡 plan + spatial | — |
| Ottawa River Regulation Planning Board (federal-provincial) | River flow/level forecasts, flood coordination | 🟢 real-time levels; 🟡 governance | — |

---

## E. Federal government & the National Capital

| Body | What it holds | Status | Catalogue |
| --- | --- | --- | --- |
| National Capital Commission (NCC) | Greenbelt, Gatineau Park, parkways, waterfront, official residences; federal land-use / design / transaction approvals; master plans; board minutes; real-estate portfolio | 🟢 layer on Open Ottawa + federal portal; 🟡 approvals & minutes PDF | `[ncc]` |
| Canada Lands Company | LeBreton Flats, Wateridge Village (ex-CFB Rockcliffe), Booth St. complex | 🟡 project pages | — |
| Public Services & Procurement Canada (PSPC) | Federal building inventory, Parliamentary precinct, Long Term Vision & Plan; federal lease footprint in Ottawa | 🟢 Directory of Federal Real Property; 🟡 precinct | — |
| Parks Canada — Rideau Canal (UNESCO) | Canal water levels, lock operations, management plan, heritage | 🟢 levels; 🟡 plan | — |
| Department of National Defence | Bases/campuses (Uplands, Connaught, NDHQ Carling) | 🔴 / 🟡 land only | — |
| Ottawa International Airport Authority / Transport Canada | Passenger volumes, noise-management, master plan, NAV CANADA | 🟡 annual report; noise 🟡 | — |
| Library and Archives Canada | Regional & federal records, historical photos (Topley etc.), census microdata | 🟢 / 🔴 mixed; much digitised | — |
| Statistics Canada | Census Profile (CSD, CMA, CT, DA), National Household Survey successor, CHASS/PUMF | 🟢 bulk | `[statcan-census]` |
| Elections Canada | Federal poll-level results, electoral geography for NCR ridings, financial returns | 🟢 bulk | — |
| Open Government Canada | Federal datasets filterable to the NCR; transfers to municipality; federal employment | 🟢 API + bulk | `[open-canada]` |
| RCMP | Federal policing; some NCR protective operations | 🔴 / 🟡 | — |
| CMHC | Rental Market Survey, Housing Market Assessment, starts & completions (Ottawa CMA) | 🟢 / 🟡 tables + portal | — |
| Federal MP constituency offices | Casework themes, householder mailings | 🔴 / 🟡 | — |

---

## F. Provincial government & regulators

| Body | What it holds | Status | Catalogue |
| --- | --- | --- | --- |
| Ministry of Municipal Affairs & Housing | FIR, Provincial Planning Statement, Minister's Zoning Orders, Building Code, municipal performance | 🟢 FIR; 🟡 policy | `[fir]` |
| Ontario Land Tribunal | Planning / CofA / expropriation / assessment appeals — see A7 | 🟡 decisions site + CanLII | `[olt]` |
| Municipal Property Assessment Corporation (MPAC) | Assessment roll; per-property values | 🔴 per-property restricted; 🟡 aggregate roll by class & municipality | `[mpac]` |
| Ministry of Transportation Ontario | Provincial highways (416, 417, 174 corridor, 7), MTO collision source data (ARIS) | 🟡 / 🔴 | `[collisions]` |
| Ontario Health / regional hospitals (Ottawa Hospital, CHEO, Montfort, Queensway Carleton, Royal) | Wait times, ER performance, quality indicators, financials | 🟢 wait-times site; 🟡 hospital annual reports | — |
| Ontario Health atHome (former Champlain LHIN / home care) | Home-care volumes, wait times | 🟡 aggregate | — |
| Public Health Ontario | Communicable-disease surveillance, Ottawa PHU snapshots | 🟢 / 🟡 | — |
| Courts (Ontario Court of Justice, Superior Court — Elgin St.) | Dockets, judgments | 🟡 CanLII for reported decisions; dockets 🔴 | `[committee-of-adjustment]` (CanLII) |
| Provincial Offences Act court (administered by the City under transfer agreement) | Charge volumes, revenue, disposition | 🟡 revenue in budget; charge data 🔴 | — |
| Landlord and Tenant Board | Application volumes, eviction orders (Ottawa) | 🟡 aggregate via Tribunals Ontario; unit data 🔴 | — |
| Law Enforcement Complaints Agency (ex-OIPRD) | Police-complaint statistics | 🟡 Ontario-wide | — |
| Special Investigations Unit | Director's reports on Ottawa-area incidents | 🟡 | — |
| Ontario Energy Board | Hydro Ottawa & Enbridge rate cases, performance scorecards | 🟢 filings + scorecards | `[hydro-ottawa] ⚑` |
| Elections Ontario | Provincial poll-level results, electoral geography, party/candidate finance | 🟢 bulk | — |
| Alcohol and Gaming Commission of Ontario | Liquor / cannabis / gaming / lottery licences (Ottawa premises) | 🟡 licence lookup | — |
| Technical Standards & Safety Authority | Elevating devices, fuels, boilers — inspection/order data | 🔴 / 🟡 | — |
| Ontario Heritage Trust | Provincial heritage easements & plaques in Ottawa | 🟡 | — |
| Ontario Ministry of Children, Community & Social Services | OW caseloads, child-care funding, licensed child-care locations | 🟢 / 🟡 | — |
| Ontario open data catalogue (data.ontario.ca) | FIR, health, education, transfers, licensing | 🟢 API + bulk | `[data-ontario]` |
| Public Sector Salary Disclosure | $100k+ across every broader-public-sector employer | 🟢 bulk | `[sunshine-list]` |
| OMERS | Pension plan covering city staff — plan-level only | 🟡 aggregate | — |
| Information and Privacy Commissioner of Ontario | MFIPPA appeal orders involving the City | 🟢 orders on site + CanLII | — |
| Auditor General of Ontario | Value-for-money audits touching Ottawa (transit, housing, etc.) | 🟡 PDF | — |

---

## G. Cross-boundary & regional bodies

| Body | What it holds | Status | Catalogue |
| --- | --- | --- | --- |
| Ville de Gatineau | Neighbouring half of the metro; council, budget, planning (in French, Quebec regime) | 🟡 | — |
| Société de transport de l'Outaouais (STO) | Cross-river transit, GTFS | 🟢 GTFS; 🟡 ridership | — |
| Ottawa–Gatineau CMA (StatCan) | Metro-level census & labour-force geography spanning two provinces | 🟢 bulk | `[statcan-census]` |
| Neighbouring municipalities (Prescott-Russell, Lanark County, Renfrew County, Rideau Lakes, etc.) | Their own councils, planning, services at the boundary | 🟡 each separately | — |
| National Capital Region planning coordination | Interprovincial transit, crossings (interprovincial-bridge studies) | 🟡 study PDFs | — |

---

## H. Courts, tribunals & external accountability

| Body | What it holds | Status | Catalogue |
| --- | --- | --- | --- |
| CanLII | Reported decisions: Ottawa CofA, OLT, LTB, IPC, courts | 🟢 free, citation-stable | `[committee-of-adjustment]` |
| Office of the Chief Coroner — inquests | Deaths in custody, pedestrian/cyclist fatalities, systemic recommendations | 🟡 verdicts & recommendations | — |
| Public inquiries (e.g. Ottawa LRT Commission, Public Order Emergency Commission) | Evidence archives, transcripts, final reports | 🟢 dedicated archives | — |
| Ontario Ombudsman | Municipal complaint themes & investigations | 🟡 | — |

---

## I. Utilities & infrastructure operators (non-municipal)

| Body | What it holds | Status | Catalogue |
| --- | --- | --- | --- |
| Enbridge Gas | Gas-distribution footprint, rate cases (via OEB), system expansion | 🟡 via OEB | — |
| Hydro One | Transmission + some rural distribution near Ottawa | 🟡 via OEB | — |
| Independent Electricity System Operator (IESO) | Zonal demand, supply mix, transmission constraints (Ottawa area) | 🟢 data directory | — |
| Bell / Rogers / Telus / others | Telecom & broadband coverage | 🟡 CRTC coverage maps; carrier data 🔴 | — |
| CRTC | Broadband availability by hexagon, complaints | 🟢 | — |
| Railways (VIA, CN, CP, Ottawa Central) | Corridors, crossings, grade-separation studies | 🟡 / 🔴 | — |
| Pipelines (TC Energy Canadian Mainline crosses the region) | Route, safety filings | 🟡 via Canada Energy Regulator | — |

---

## J. Land & property records

| Source | Status | Catalogue |
| --- | --- | --- |
| Ontario Land Registry Access (OnLand / Teranet) — deeds, mortgages, easements, registered plans, parcel registers | 🔴 **paywalled** — pay-per-search / per-document, Teranet exclusive operator | — |
| MPAC assessment roll | 🔴 per-property; 🟡 aggregate — see F | `[mpac]` |
| City property-tax accounts | 🔴 owner-only | — |
| Condominium Authority of Ontario — condo-corporation registry | 🟡 public registry lookup | — |
| Property surveys / reference plans | 🔴 via OnLand or surveyor | — |
| Title insurance / transaction data | 🔴 commercial | — |
| Teranet–National Bank House Price Index (Ottawa) | 🟢 index series | — |

---

## K. Civil society — advocacy & community organisations

| Body | Focus | Status |
| --- | --- | --- |
| Horizon Ottawa | Municipal-politics advocacy; runs a councillor **vote tracker** (2022–26) | 🟡 web tool — `[horizon-vote-tracker]` |
| ACORN Ottawa | Tenant / low-income advocacy; **housing-vote scorecard** | 🟡 report — `[acorn-voting-records]` |
| Alliance to End Homelessness Ottawa | Independent progress reports, Housing Needs Assessment | 🟡 PDF — `[ateh]` |
| Ecology Ottawa | Climate, trees, active transport campaigns; canvassing data | 🟡 / 🔴 |
| Bike Ottawa | Cycling advocacy; **PODS** (bike-network stress map), collision/"ninja" map | 🟢 open map layers |
| Healthy Transportation Coalition / Free Transit Ottawa | Transit-equity advocacy | 🟡 |
| People's Official Plan | Grassroots planning critique | 🟡 |
| Federation of Citizens' Associations (FCA) | Umbrella for ~65 community associations | 🟡 |
| Community & tenants' associations (100+) | Hyperlocal newsletters, development positions, traffic petitions | 🟡 / 🔴 scattered, ephemeral |
| Council on Aging of Ottawa | Seniors' policy research | 🟡 PDF |
| Ottawa Poverty Reduction Network / Make Poverty History | Income & social-policy monitoring | 🟡 |
| Greater Ottawa Home Builders' Association (GOHBA) | Industry positions, permit/starts commentary | 🟡 / 🔴 |
| Ottawa Riverkeeper | Independent watershed monitoring, own ArcGIS Hub | 🟢 API + bulk — `[riverkeeper]` |
| Environmental Defence / other national ENGOs (local files) | Campaign-specific analysis | 🟡 |
| Faith, cultural & service organisations | Community-need signal, settlement support | 🔴 / 🟡 |

---

## L. Civil society — journalism

| Outlet | Type | Status |
| --- | --- | --- |
| Ottawa Lookout | Digital-native newsletter; most complete 2026 candidate tracker & ward guides | 🟡 — `[ottawa-lookout]` |
| CBC Ottawa | Public broadcaster; investigations, data journalism | 🟡 |
| CTV Ottawa / Bell Media | Broadcast | 🟡 |
| Ottawa Citizen / Ottawa Sun (Postmedia) | Legacy dailies; archive back to 1845 (paywalled) | 🟡 / 🔴 |
| Le Droit | French-language daily (co-op) | 🟡 |
| Capital Current (Carleton J-school) | Local coverage, student-produced | 🟡 |
| Apt613 / community papers (Kitchissippi Times, Orléans Star, West Carleton Review, etc.) | Neighbourhood coverage | 🟡 |
| Ottawa Business Journal / OBJ | Business, development, procurement wins | 🟡 |
| CFRA / talk radio | Call-in issue signal | 🔴 ephemeral |

---

## M. Civil society — civic technology & open-data projects

| Project | What it does | Status |
| --- | --- | --- |
| OttWatch | Scrapes ottawa.ca + eScribe for new documents; mirrors lobbyist registry; tracks open-data publications; own dev-app index | 🟡 web app — `[ottwatch]` |
| Horizon Ottawa Vote Tracker | Hand-keyed councillor votes 2022–26 | 🟡 — `[horizon-vote-tracker]` |
| How They Voted (howtheyvoted.ca) | Dedicated Ottawa voting-record site | 🟢 ships the compiled record as JSON at `/data/ottawa/*.json`, verified current — `[howtheyvoted]` (site terms, not open data) |
| ACORN housing-vote scorecard | Issue-specific vote compilation | 🟡 — `[acorn-voting-records]` |
| Ottawa Civic Tech / YOWCT | Volunteer community + GitHub org | 🟡 — `[ottawa-civic-tech]` |
| Bike Ottawa PODS / maps | Network-stress & collision mapping | 🟢 |
| Ad-hoc hackathon / student projects | Varies | ⚪ |

---

## N. Research & academic

| Body | What it holds | Status |
| --- | --- | --- |
| Ottawa Neighbourhood Study (uOttawa / Bruyère) | 300+ indicators per neighbourhood; custom small-area boundaries | 🟢 bulk + API + layers on Open Ottawa — `[ons]` |
| Neighbourhood Equity Index | Composite equity score, published methodology (renewed 2024) | 🟡 — `[nei]` |
| uOttawa Institute of Fiscal Studies and Democracy (IFSD) | Municipal fiscal analysis | 🟡 PDF |
| Carleton — School of Public Policy & Administration; MacOdrum Library data services & historical census geography (1951–) | Research outputs; data-access support | 🟡 / 🔴 |
| Smart Prosperity Institute (uOttawa) | Environment-economy policy, land-use modelling | 🟡 |
| Local university theses & GIS-library holdings | Historical maps, air-photo series | 🟡 / 🔴 |

---

## O. Community-indicator & philanthropic data projects

| Body | What it holds | Status |
| --- | --- | --- |
| Ottawa Insights | Themed community indicators (environment, economy, wellbeing) drawn from city/health/social data | 🟡 web narratives — `[ottawa-insights]` |
| Ottawa Community Foundation — Vital Signs | Periodic community check-up report | 🟡 PDF |
| United Way East Ontario | Community-need data, funded-agency outcomes | 🟡 |
| Ottawa Food Bank — Hunger Report | Food-insecurity volume & demographics | 🟡 PDF |
| Community Data Program (CCSD consortium) | Custom StatCan tabulations; Ottawa-region catalogue | 🔴 members-only (catalogue visible) — `[community-data-program]` |
| Ontario 211 / Community Information Centre of Ottawa | Service-directory usage data | 🟡 / 🔴 |

---

## P. Economic & business information

| Body | What it holds | Status |
| --- | --- | --- |
| Ottawa Board of Trade | Business-climate surveys, advocacy positions | 🟡 |
| Invest Ottawa / Bluesky Strategy | Economic-development metrics, sector data, Ottawa tech scene | 🟡 |
| Ottawa Tourism | Visitor volumes, economic impact | 🟡 |
| Ottawa Real Estate Board (OREB) | MLS resale statistics (monthly), price & volume by district | 🟡 press-release tables; unit data 🔴 |
| CMHC | Starts, completions, under-construction, rental-vacancy, core-housing-need (Ottawa CMA) | 🟢 / 🟡 — see E |
| Rentals.ca / PadMapper / commercial listing scrapes | Asking-rent series | 🟡 commercial reports |
| Statistics Canada — Labour Force Survey, Business Register (Ottawa CMA) | Employment, unemployment, business counts by sector | 🟢 |
| Business Improvement Areas | See B | 🟡 / 🔴 |

---

## Q. Labour organisations

| Body | What it holds | Status |
| --- | --- | --- |
| CUPE 503 (inside/outside city workers), ATU 279 (OC Transpo), IAFF 162 (fire), OPSEU, CUPE 4266 (OCH), teacher locals (ETFO/OECTA/OSSTF/AEFO) | Bargaining positions, grievance patterns, strike votes | 🔴 / 🟡 |
| Ottawa & District Labour Council | Cross-sector labour signal | 🟡 |
| Collective agreements (settled) | Wage grids, benefits, staffing rules | 🟡 some tabled to Council; full set 🔴 |

---

## R. Historical & archival institutions

| Body | What it holds | Status |
| --- | --- | --- |
| City of Ottawa Archives | Pre-2012 & pre-amalgamation municipal records, photos, maps, drawings; 16,000-vol. reference library | 🔴 mostly paper, on-site — `[city-archives]` |
| Library and Archives Canada | Federal + regional records, Topley/other photo collections, historical maps | 🟢 / 🔴 much digitised — see E |
| Bibliothèque et Archives nationales du Québec (Gatineau) | Quebec-side regional records | 🟢 / 🔴 |
| Archives of Ontario | Provincial records touching Ottawa, historical land records | 🟢 / 🔴 |
| OPL — Ottawa Room (Main branch) | Local-history collection, digitised photos, city directories | 🟢 digitised subset — `[opl]` |
| Historical societies (Historical Society of Ottawa, Bytown Museum, Gloucester/Nepean/Cumberland/Osgoode societies) | Local histories, oral history, photo collections | 🟡 / 🔴 |
| National Air Photo Library (NRCan) | Historical aerial imagery | 🟡 / 🔴 |
| Newspapers.com / Postmedia archive / LAC newspaper microfilm | Historical Ottawa Citizen & predecessors | 🔴 paywalled — see L |
| Cemetery & parish records (Beechwood — National Cemetery, Notre-Dame, Pinecrest) | Burial & genealogical records | 🟡 / 🔴 |

---

## S. Commercial data providers (relevant, mostly closed)

| Provider | Product | Status |
| --- | --- | --- |
| Environics Analytics | PRIZM segmentation, demographic modelling to postal code | 🔴 licensed |
| Teranet | Land-registry data, HPI, parcel data | 🔴 licensed / pay-per-use |
| Local Logic / mappedin / Mapbox | Location scores, foot-traffic, indoor maps | 🔴 licensed |
| Real-estate portals (Realtor.ca, Zolo, HouseSigma) | Listing & sold data | 🟡 / 🔴 |
| Credit-bureau & telco mobility data | Consumer & movement analytics | 🔴 licensed |

---

## Roll-up: where things stand

### By status (rough count of the ~180 leaf rows above)

| Status | Share | Character |
| --- | --- | --- |
| 🟢 Open | ~20% | Almost entirely **spatial** (anything with coordinates has a GeoJSON endpoint) plus a handful of well-run bulk series: FIR, GTFS, the police ArcGIS Hub, collisions, ASE, the sunshine list, StatCan, ONS. |
| 🟡 Partial | ~50% | The bulk of municipal governance: agendas, budgets, audits, disclosure logs, planning files, health dashboards — all real, all public, all trapped in PDF, HTML or dashboards with no underlying data. |
| 🔴 Closed | ~20% | Two sub-types: **access-restricted** (land registry, MPAC per-property, FOI-only records, collective agreements, commercial data) and **never produced** (recorded votes as data, vendor payments, contract awards, candidate platforms). |
| ⚪ Unknown | ~10% | Whole branches nobody has checked: BIAs, rural drainage, property-standards orders, delegated-authority decisions, gift registry, most agency operational data — plus four catalogue rows verification could not settle (`procurement`, `hydro-ottawa`, `conservation-authorities`, `school-boards`). |

### The patterns that actually matter

1. **The open/closed split is a format split, not a secrecy split.** Very little of Ottawa's
   governance information is *secret*. It is *unusable*: published as a 400-page PDF, or as a
   dashboard with the CSV removed, or as HTML with no API. The work is almost never FOI; it is
   parsing.

2. **Coordinates are open; prose and dollars are not.** Every spatial layer has a clean
   endpoint. Every financial and textual record is a document. A project's difficulty is
   predictable from which side of that line it sits on.

3. **eScribe is the chokepoint.** Council, every committee, the Police Services Board, the Board
   of Health, OCH's AGM and school-board-adjacent items all flow through one meeting-management
   system with sequential `DocumentId` integers and no search, no bulk export, no structured
   metadata. Unlock eScribe and a dozen downstream datasets become possible: votes, spending
   decisions, planning history, lobbying-to-decision chains. (Verification did find a hook: the
   meeting *calendar* is queryable at `MeetingsCalendarView.aspx/GetCalendarMeetings` — enough
   to enumerate meetings, not the documents.)

4. **The accountability datasets don't share keys.** Lobbyist registry, development
   applications, campaign contributions, council votes, contract awards — five systems, no
   common identifier for a person, company, address or file. Joining them is the highest-value
   and hardest work in the catalogue.

5. **"Never produced" is a policy gap, not a technical one.** Recorded votes, vendor payments,
   contract awards and candidate platforms are missing because nobody is required to publish
   them — not because they are hard. These are the items where advocacy moves the needle faster
   than code. (Partial exception on votes: `howtheyvoted.ca` publishes its hand-compiled record
   as JSON and is current — a usable secondary source, though on site terms, not open data.)

6. **The non-municipal layer is real and unstitched.** The NCC, three conservation authorities,
   four school boards, Hydro Ottawa, the airport authority, the province and the federal
   government each govern part of Ottawa. No project joins these layers, and the conservation
   authorities in particular hold the binding constraint on much development while being absent
   from every city-only dataset.

### Implications for `sources.json`

**Uncatalogued branches worth adding** (high value, believed public):
`Ottawa Community Housing` · `ByWard Market District Authority` · `Business Improvement Areas` ·
`Ontario Land Registry Access / Teranet` (as a 🔴 reference point) · `CMHC Ottawa CMA housing data` ·
`Elections Ontario / Elections Canada poll-level results` · `IESO / OEB filings` ·
`Ottawa LRT Public Inquiry archive` · `Ontario hospital wait-times` · `Bike Ottawa PODS` ·
`EQAO by-school results` · `Ottawa Student Transportation Authority` · `Coroner's inquest verdicts` ·
`Ottawa Community Foundation Vital Signs` · `Ottawa Food Bank Hunger Report` ·
`Combined-sewage-overflow real-time data` · `Provincial Offences Act court (city-administered)`.

**Verification priorities.** Done for the catalogued sources (stages 0–3, 2026-09-09): 55 access
tags confirmed, 2 understated, 15 unconfirmed. Still open:
`procurement` platform identity · `conservation-authorities` URLs & data · `hydro-ottawa`
open-data programme (likely none) · `school-boards` data portals ·
whether budget line-items are mirrored to Open Ottawa in any usable form · whether OCH publishes
portfolio data below the annual-report level · `ecolecatholique.ca` / `ottawacivictech.ca` (both
failed to resolve at verification — may be transient) · and all of the uncatalogued rows above.

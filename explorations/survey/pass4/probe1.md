# Pass 4 probe 1 — uncatalogued Ottawa rows (53 rows, section A)

Probed 2026-10-16 with curl (browser UA). Method per row: open.ottawa.ca OGC search API (`/api/search/v1/collections/dataset/items?q=`), direct HEAD/GET of the official host where known, Wayback availability for ottawa.ca pages.

**Key limitation.** Every `ottawa.ca` / `www.ottawa.ca` URL returns HTTP 200 with a ~1 KB Incapsula shell (`_Incapsula_Resource`), including robots.txt (212 B), even with a Firefox UA. That is NOT live evidence. archive.org's availability API returned 429 for every call, so no second route to ottawa.ca pages. All ottawa.ca page rows are therefore **candidate** at best. Page paths for them were guessed from memory and could not be checked, so no ottawa.ca URL below is confirmed. Stage-2 browser verification is needed (no Chromium in this sandbox).
Claims marked **verified** have two independent confirmations (HTTP probe plus API content); everything else is **candidate**.

Open-data portal: `open.ottawa.ca` HEAD 200 and API returns JSON (**verified**). Datasets are ArcGIS FeatureServer/MapServer, so machine-readable via REST (CSV/GeoJSON export).

| row | URL | status / liveness | machine-readable? | emoji | note |
|---|---|---|---|---|---|
| 1 Recorded councillor votes | https://pub-ottawa.escribemeetings.com/ | 200, 268 KB real page (**verified** live) | No votes dataset on portal (search "councillor vote" returns wards/budget only) | keep 🔴 | eScribe carries minutes as prose; no vote table found. Candidate. |
| 2 Motions & directions to staff | pub-ottawa.escribemeetings.com/Meetings.aspx | 200, 28 KB | no | keep 🟡 | no register; portal has no hits. Candidate. |
| 3 Delegated-authority reports | open.ottawa.ca datasets "Contracts awarded under delegation of authority for Jan-Jun ...", "Transit Contracts awarded under DOA" | portal API **verified** | **Yes (ArcGIS)** for contracts awarded under DOA | change ⚪ -> 🟡 | The contract-DOA slice is open data; other delegated decisions still not indexed. |
| 4 Councillor ward pages | ottawa.ca (guess, unverifiable) | Incapsula shell | Portal has Wards 2026-2030, Wards 2022-2026, Council Meeting Attendance 2022-2026 | keep 🟡 (consider noting the attendance dataset) | Council attendance dataset is open; check whether catalogued. |
| 5 Compliance audit committee | not found | not found; portal no hits | no | keep ⚪ | candidate |
| 6 Voters' list / MPAC | voterlookup.ca (MPAC) | HTTP 000 (no connection) | no | keep 🔴 | Voters' list is restricted by statute (candidates/electors on request). Candidate. |
| 7 Turnout by ward | ottawa.ca elections (unverifiable) | shell | portal no hits | keep 🟡 | candidate |
| 8 Dept structure / org charts | ottawa.ca (unverifiable) | shell | no | keep 🟡 | candidate |
| 9 Corporate & strategic plans | ottawa.ca (unverifiable) | shell | no (PDF/HTML) | keep 🟡 | candidate |
| 10 Performance / City Scorecard | not found | portal no hits | no | keep ⚪ | candidate |
| 11 Collective agreements | ottawa.ca (unverifiable) | shell | no | keep 🟡 | candidate |
| 12 Workforce / diversity | portal no hits | shell | no | keep 🟡 | candidate |
| 13 Directives/policies/APs | ottawa.ca (unverifiable) | shell | no | keep 🟡 | candidate |
| 14 Vendor / supplier payments | none; portal no hits | n/a | no | keep 🔴 | Only contracts >$25k are published (row 15), not payments. Candidate. |
| 15 Contract award register | open.ottawa.ca: "2025 Contracts Awarded greater than 25,000 Jan-Jun", "... Jul-Dec", 2024 Jul-Dec (FeatureServer `.../Contracts_awarded_for_Q3_Q4_2024`, modified 2025-05) | API **verified** (plus ottawa.bidsandtenders.ca returns 403, bot-gated) | **Yes** (ArcGIS FeatureServer, half-year files) | **change 🔴 -> 🟡** | Winner/value lists are open as semi-annual datasets; amendments and sole-source detail not confirmed. Most notable finding. |
| 16 Development charges | ottawa.ca (unverifiable) | shell | portal budget explorer datasets only | keep 🟡 | candidate |
| 17 Reserves / debt / LRFP | ottawa.ca (unverifiable); Wayback none | shell | budget explorer datasets (2024-2026) cover budget, not reserves | keep 🟡 | candidate |
| 18 Asset management plan | ottawa.ca (unverifiable) | shell | no | keep 🟡 | candidate |
| 19 Property tax rates | ottawa.ca (unverifiable) | shell | portal no relevant hits | keep 🟡 | candidate |
| 20 User-fee schedule | ottawa.ca (unverifiable) | shell | Draft Budget Explorer datasets 2024/2025/2026 on portal | keep 🟡 | Budget Explorer datasets are open data; verify if catalogued. |
| 21 Grants & contributions | ottawa.ca (unverifiable) | shell | portal no hits | keep 🟡 | candidate |
| 22 Investment holdings / ONE | https://www.oneinvestment.ca/ | 200, 60 KB real page (**verified** live) | no | keep 🟡 | Program site; City holdings are in financial statements. |
| 23 Fraud & Waste Hotline | www.ottawa.ca/.../auditor-general | 200 but 1 KB Incapsula shell (not evidence) | no | keep 🟡 | candidate |
| 24 Hospitality / travel / sponsorship | ottawa.ca (unverifiable) | shell | portal no hits | keep ⚪ | candidate |
| 25 Ontario Ombudsman | https://www.ombudsman.on.ca/ | 403, 5.4 KB (WAF block, not a live-confirmation) | not determined | keep 🟡 | Reachable only via browser. Candidate. |
| 26 Gift registry | ottawa.ca (unverifiable) | shell | no | keep ⚪ | candidate |
| 27 Sponsorship agreements | not found | portal no hits | no | keep ⚪ | candidate |
| 28 Heritage register | ottawa.ca (unverifiable) | shell | portal has only "Cultural Spaces Inventory - Heritage", not the heritage register | keep 🟡 | Register itself may exist as map layer on maps.ottawa.ca; not checked. |
| 29 Urban Design Review Panel | ottawa.ca (unverifiable) | shell; portal no hits | no | keep ⚪ | candidate |
| 30 CIP / brownfield | open.ottawa.ca "Community Improvement Plans Active" and "Inactive" | API **verified** | **Yes** (spatial CIP areas, not grant awards) | keep 🟡 | Spatial layers open; grants awarded not. |
| 31 Parkland cash-in-lieu | none | portal no hits | no | keep 🔴 | candidate |
| 32 Tree / site-alteration permits | none for permits; portal has Tree Equity Score 2025 (4 areas) | API verified for TES only | permits no; TES yes | keep ⚪ | Tree Equity Score open data may be uncatalogued. |
| 33 Servicing master plans | ottawa.ca (unverifiable) | shell | no | keep 🟡 | candidate |
| 34 Site plan agreements | none | portal no hits | no | keep 🔴 | on title (land registry) |
| 35 OC Transpo ridership | https://www.octranspo.com/en/plan-your-trip/travel-tools/developers/ | 200, 146 KB real page (**verified**); portal has "OC Transpo Stops" | GTFS/developer page exists (stops on portal) | keep 🟡 | Ridership and on-time data not found as data; schedule feeds (GTFS) are open. |
| 36 Para Transpo | www.octranspo.com/.../para-transpo/ | **404** (guessed path) | portal no hits | keep 🔴 | candidate |
| 37 O-Train / LRT | portal "O-Train Line - Stage 2"; ottawalrtinquiry.ca HTTP 000; octranspo guessed path 404 | partial | spatial line layer yes | keep 🟡 | Inquiry domain guess did not resolve (do not trust). |
| 38 Red-light camera data | open.ottawa.ca "Red Light Camera Locations", "Red Light Camera Violations 2016, 2025, 2026" (FeatureServer, modified 2026-03) | API **verified** | **Yes** | **change ⚪ -> 🟢** | Open, annual violation counts plus locations. |
| 39 Traffic counts | open.ottawa.ca "Midblock Volume 2022", "Intersection Volume 2022", "Transportation Midblock Volume 2023/2025", Traffic Collisions by Location 2014-2018 | API **verified** | **Yes** | keep 🟡 (could be 🟢) | Midblock and intersection volumes are open; "patchy" still fair (turning-movement incl.). |
| 40 Parking | open.ottawa.ca "Paid Parking Spaces" (maps.ottawa.ca/arcgis/.../Parking/MapServer/2), "Pay and Display Machines" | API **verified** | **Yes** inventory | keep 🟡 | Ticket data still request-only. |
| 41 Road construction / closures | portal "Road Centrelines", "Upcoming construction facilities, culverts, parks, bridges" | API verified | partial | keep 🟡 | candidate |
| 42 TMP / Vision Zero | ottawa.ca (unverifiable) | shell; portal no hits | no | keep 🟡 | candidate |
| 43 Traffic calming | ottawa.ca (unverifiable) | shell; portal no hits | no | keep 🟡 | candidate |
| 44 Speed limit / school zone / CSZ layers | portal: "Automated Speed Enforcement Camera Removal - Monitoring Speed Data" (monthly, 8 pilot sites, created Jan 2026); no speed-limit, school-zone or CSZ layers by search | API verified for ASE only | ASE yes; limit layers **not found** | **change 🟢 -> 🟡** | "School zone", "community safety zone", "speed limit" searches did not find the layers (maybe on maps.ottawa.ca REST, unchecked). ASE cameras deactivated 2025-11-13 (Bill 56) per dataset text. |
| 45 OPS use of force | www.ottawapolice.ca | 403, 97 B (WAF block) | not determined | keep 🟡 | Guessed paths; candidate |
| 46 OPS race-based data | www.ottawapolice.ca | 403, 97 B | not determined | keep 🟡 | candidate |
| 47 Police collective agreement | ottawapolice.ca 403; https://www.ottawapoliceboard.ca/ 200 (2 KB) | board site live | no | keep 🔴 | candidate |
| 48 LECA | https://leca.ca/ | 200, 63 KB real page (**verified**: HTTP plus WebSearch). `www.leca.ca`, `leca-ontario.ca`, `lecaontario.ca` all HTTP 000 | page only; no data endpoint checked | keep 🟡 | Use apex `leca.ca` (no www). Formerly OIPRD. Policy and service complaints now go to Inspectorate of Policing. |
| 49 SIU | https://www.siu.on.ca/ (meta-refresh) -> /en/directors_reports.php | 200, 39 KB (**verified**) | HTML/PDF reports, no feed seen | keep 🟡 | |
| 50 Fire inspection | none | portal no hits | no | keep 🔴 | candidate |
| 51 Emergency Management | ottawa.ca (unverifiable) | shell | no | keep 🟡 | candidate |
| 52 By-law enforcement stats | none on portal | shell | no | keep 🟡 | candidate |
| 53 Business licensing | portal "Street Food Vendors 2025" | API verified | partial (street food vendors only) | keep 🟡 | Taxi/TNC/tow data not found. |

## Five most notable findings
1. **Contract awards are open data**, not 🔴: open.ottawa.ca publishes semi-annual "Contracts Awarded greater than 25,000" (2024 H2, 2025 H1, 2025 H2) plus DOA contract datasets (city and transit) as ArcGIS FeatureServers. Rows 3 and 15 should move up (15: 🔴 -> 🟡; 3: ⚪ -> 🟡). Vendor payments (row 14) remain absent.
2. **Red-light camera violations and locations are open (🟢)**, annual datasets 2016/2025/2026, so row 38 ⚪ -> 🟢.
3. **Speed-limit / school-zone / CSZ layers (row 44, currently 🟢) were not found** on the portal search. Only the ASE camera-removal monitoring dataset surfaced (cameras deactivated 2025-11-13). Downgrade to 🟡 until layers are located.
4. **ottawa.ca is entirely behind Incapsula for curl** (even robots.txt), and archive.org throttles. No ottawa.ca-hosted row can be liveness-verified without a browser. 29 of 53 rows depend on this. LECA moved/should be listed as apex `leca.ca` (www fails). ottawa.bidsandtenders.ca, ombudsman.on.ca and ottawapolice.ca return 403 WAF blocks.
5. Likely uncatalogued open data on the portal: Council Meeting Attendance 2022-2026, Wards 2026-2030/2022-2026, Draft Budget Explorer datasets (2024-2026), Midblock/Intersection Volume 2022-2025, Tree Equity Score 2025, Community Improvement Plans, Paid Parking Spaces. Check these against sources.json.

Not reached: nothing skipped, but per-row ottawa.ca page URLs were unverifiable (see above). Raw output: scratchpad `p1/out1.txt`.

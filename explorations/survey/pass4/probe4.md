# Pass 4 probe — uncatalogued sections K-S (probed 2026-10-16)

Method: `curl -sIL` + one GET per row (UA "Mozilla/5.0 (research probe)"), up to 2 extra guesses for URLs that failed. "verified" = HEAD and GET agree on status and body content inspected (title / size / feed link tags). Anything else is "candidate". Machine-readable column is based on page link tags (RSS/atom) and known APIs; no row's data was downloaded beyond the front page, except where stated. URL guesses were mine (no search tool used); "not reached" means my guesses failed (000 = no connection/DNS), not that the body is dead.

| row | URL | status / liveness | machine-readable? | emoji | note |
|---|---|---|---|---|---|
| People's Official Plan | peoplesofficialplan.ca, peoplesop.ca (guesses) | 000 on both - **not found** | n/a | keep 🟡, flag | Real URL unknown; candidate dead/moved. Needs a search to locate. |
| Federation of Citizens' Associations | https://fca-fac.ca/ | 200, 111 KB real page, title "Federation of Citizen's Associations of Ottawa" (**verified**) | RSS link tags (WordPress) | keep 🟡 | Advocacy / position papers; html only. |
| Community & tenants' associations | https://www.ottawa.ca/en/city-hall/get-know-your-city/community-associations | 200 but 212-byte body with Incapsula marker - **bot shell, not live evidence** | unknown | keep 🟡 | City page listing associations unverifiable from curl; need stage-2 browser. |
| Council on Aging of Ottawa | https://coaottawa.ca/ | 200, 266 KB real (**verified**) | RSS + wp json | keep 🟡 | Reports as PDFs/html. |
| Ottawa Poverty Reduction Network / Make Poverty History | https://www.makepovertyhistory.ca/ (200, 72 KB, "Make Poverty History", **verified**); OPRN own site not found (ottawapovertyreduction.ca, oprn-rrpo.ca, povertyfreeottawa.ca all 000) | MPH live; OPRN **not found** | RSS only | keep 🟡 | makepovertyhistory.ca is the Ottawa-area coalition site per title; OPRN domain unresolved. |
| GOHBA | https://www.gohba.ca/ | 200, 330 KB real (**verified**) | RSS | keep 🟡 | Housing-start / market commentary html. |
| Environmental Defence | https://environmentaldefence.ca/ | 200, 287 KB real (**verified**) | RSS | keep 🟡 | National; little Ottawa-specific. |
| Faith, cultural & service orgs | n/a | closed/fragmented, no single endpoint | none | keep 🔴 | One-line confirm: no public aggregate endpoint. |
| CBC Ottawa | https://www.cbc.ca/webfeed/rss/rss-canada-ottawa | 200 application/xml 24 KB, real RSS (**verified**: HEAD+GET) | **RSS yes** | keep 🟡 | Headlines only; article text paywall-free but terms restrict reuse. |
| CTV Ottawa | https://www.ctvnews.ca/ottawa/ | 200, 1.7 MB real | none seen in tags | keep 🟡 | html only (candidate; no feed link found). |
| Ottawa Citizen / Sun | https://ottawacitizen.com/ | 200, 618 KB real | RSS link tag | keep 🟡 | Paywalled metered; RSS headlines. |
| Le Droit | https://www.ledroit.com/ | 200, 787 KB real | none seen | keep 🟡 | html only; paywall. |
| Capital Current | https://capitalcurrent.ca/ | 200, 337 KB real (**verified**) | RSS | keep 🟡 | Student newsroom; "bot" grep hits are likely captcha form scripts, page is real. |
| Apt613 / Kitchissippi Times | https://apt613.ca/ (200, 75 KB), https://kitchissippi.com/ (200, 375 KB, RSS) | live | Kitchissippi RSS; Apt613 none seen | keep 🟡 | Orléans Star/others not probed. |
| OBJ | https://obj.ca/ | 200, 615 KB real | RSS | keep 🟡 | Paywall partial. |
| CFRA / talk radio | https://www.iheart.com/live/cfra-1700/ | 404 (my guessed path); cfra.com not tested | none | keep 🔴 | Audio only, no transcripts; one-line confirm. |
| Bike Ottawa PODS / maps | https://bikeottawa.ca/ | 200, 113 KB real; mentions "open data" | RSS; PODS data not located on front page | **candidate: change to 🟡** | 🟢 not supported by this probe; no dataset endpoint found. Check for a map/GeoJSON in a follow-up. |
| Ad-hoc hackathon / student projects | n/a | no single endpoint | none | keep ⚪ | |
| IFSD (uOttawa) | https://ifsd.ca/ | 200, 152 KB real (**verified**) | RSS | keep 🟡 | Reports PDFs, some data tools. |
| Carleton SPPA | https://carleton.ca/sppa/ | 200, 191 KB real | none | keep 🟡 | |
| Smart Prosperity Institute | https://institute.smartprosperity.ca/ | 200, 29 KB real | RSS | keep 🟡 | |
| Theses / GIS library | https://ruor.uottawa.ca/ (200, 601 KB, DSpace/Scholaris API links); https://curve.carleton.ca/ redirects to https://carleton.scholaris.ca/home (200) | live; **CURVE moved** | **API yes** (hundreds of /api/ refs, atom+rss) | keep 🟡, note API | Both are DSpace-style repositories with REST/OAI; not tested beyond front page (candidate). Carleton repo now on scholaris.ca. |
| Ottawa Community Foundation Vital Signs | ottawacommunityfoundation.com / .ca (guesses) | 000 all - **not found** | n/a | keep 🟡, flag | Domain guess wrong or unreachable; candidate needs a search. |
| United Way East Ontario | https://www.unitedwayeo.ca/ | first run 503, retry 200, 314 KB real (**verified** on retry) | none seen | keep 🟡 | Intermittent 503. |
| Ottawa Food Bank Hunger Report | https://ottawafoodbank.ca/ | **403** 103-byte "Error 403 Forbidden" on HEAD+GET (also /hunger-report/) | unknown | keep 🟡, flag | Blocks my UA; not evidence of dead. Report is a PDF per prior knowledge (candidate). |
| Ontario 211 | https://211ontario.ca/ | 200, 22 KB real | none seen (211 has a partner API, keyed - candidate) | keep 🟡 | |
| Ottawa Board of Trade | https://www.ottawabot.ca/ | 200, 85 KB real | none | keep 🟡 | |
| Invest Ottawa | https://www.investottawa.ca/ | 200, 304 KB real | none | keep 🟡 | |
| Ottawa Tourism | https://ottawatourism.ca/en | 200, 95 KB (redirect from www) | none | keep 🟡 | |
| OREB | https://www.oreb.ca/ | 200, 54 KB real (**verified**); /market-statistics/ is 404 | RSS only | keep 🟡 | Stats pages moved; PDFs monthly. |
| CMHC | https://www.cmhc-schl.gc.ca/professionals/housing-markets-data-and-research/housing-data-statistics-sources-datasets (redirected from the data-tables URL) | 200, 168 KB real; HMIP legacy table URL returned 500 | **bulk yes** (HMIP tables export CSV/XLS; data-tables page links, candidate) | keep 🟢 | HMIP deep link I guessed returned 500 "breakdown not supported" - wrong table ID, not a dead site. |
| Rentals.ca / PadMapper | https://rentals.ca/national-rent-report | 403, "Just a moment..." Cloudflare challenge, 5 KB | monthly report page exists; unverified | keep 🟡 | Bot challenge: no live evidence. Zolo also Cloudflare-blocked. |
| Statistics Canada LFS | https://www150.statcan.gc.ca/t1/wds/rest/getAllCubesListLite | **200 application/json 5.05 MB real** (**verified**: API); but /n1/en/type/data page returned a bilingual "We're sorry! website currently unavailable" 200 page | **API + bulk yes** (WDS) | keep 🟢 | HTML page was serving a maintenance banner at probe time; WDS API live. |
| Business Improvement Areas | https://www.ottawa.ca/en/business/business-improvement-areas | 200 1.1 KB Incapsula shell - **not live evidence** | unknown | keep 🟡 | Same for biaott guess (1 KB shell). City BIA list also on open data portal (not probed here). |
| CUPE 503 / ATU 279 | cupe503.ca/.org (000, **not found**); https://atu279.com/ (200, 237 KB real) | ATU live, CUPE not reached | none | keep 🔴 | Internal docs/members-only. |
| Ottawa & District Labour Council | https://ottawalabour.org/ -> https://ottawalabour.labourcouncils.ca/ | 200, 47 KB real; **moved** | none | keep 🟡 | |
| Collective agreements (settled) | https://www.ottawa.ca/en/city-hall/employment-city-ottawa | 1.2 KB Incapsula shell - not live evidence | unknown | keep 🟡 | Not verified. |
| Library and Archives Canada | https://library-archives.canada.ca/eng/ -> https://www.canada.ca/en/library-archives.html (302); https://search.open.canada.ca/opendata/?owner_org=lac-bac (200, 298 KB) | live; **site moved to canada.ca** | **LAC datasets on open.canada.ca (CKAN)**; Collection Search (recherche-collection-search.bac-lac.gc.ca) returned 403 security-check page | keep 🟢 | Collection Search needs a browser; open.canada.ca route works. |
| BAnQ Gatineau | https://www.banq.qc.ca/ | 200 32 KB but title "Radware Bot Manager Block" - **bot shell** | unknown | **change to ⚪** (candidate) | Cannot confirm 🟢 from curl. |
| Archives of Ontario | https://www.archives.gov.on.ca/en/ | 200 15 KB "Radware Captcha Page" - **bot shell** (also /en/access/) | unknown | **change to ⚪** (candidate) | AO has known online catalogue AccessON; unverified here. |
| Historical societies | https://www.historicalsocietyottawa.ca/ | 200, 158 KB real (**verified**) | RSS + atom | keep 🟡 | |
| National Air Photo Library | two NRCan guessed paths | 404 both (guessed paths) | n/a | keep 🟡 | URL not found; NRCan page moved or my guess wrong. |
| Newspapers.com / Postmedia archive | https://www.newspapers.com/ | 403 Cloudflare "Attention Required" 5 KB - bot shell | none | keep 🔴 | Paywalled commercial. |
| Cemetery & parish records (Beechwood) | https://beechwoodottawa.ca/ | 200, 592 KB real | RSS; search is a web form | keep 🟡 | |
| Environics Analytics | https://environicsanalytics.com/ | 200, 134 KB real | none | keep 🔴 | Commercial licence. |
| Teranet | https://www.teranet.ca/ | 200, 381 KB real | none (commercial) | keep 🔴 | |
| Local Logic / Mapbox | https://locallogic.co/ | 200, 257 KB real | commercial API, keyed | keep 🔴 | Mapbox not probed. |
| Real-estate portals | realtor.ca (403 "blocked", 9 KB), zolo.ca (403 Cloudflare), housesigma.com (200, 5 KB SPA shell) | bot-blocked / SPA | none public | keep 🟡 (or 🔴) | ToS forbid scraping; no public API. |
| Credit-bureau & telco mobility | https://www.equifax.ca/personal/ (200) | consumer site only | none | keep 🔴 | One-line confirm: no public endpoint. |
| Roll-up rows (Open/Partial/Closed/Unknown) | n/a | not sources | n/a | n/a | Counts only; recompute after edits above. |

## 5 most notable findings

1. **Several URLs are unreachable under my guesses (000): People's Official Plan, Ottawa Poverty Reduction Network, Ottawa Community Foundation (Vital Signs), CUPE 503.** Candidate dead/moved; each needs a real search to locate its site. Not confirmed dead.
2. **Bot walls hide the three "🟢 archives" rows**: BAnQ and Archives of Ontario return Radware captcha shells (200, ~15-32 KB), LAC Collection Search returns a 403 security check. Only LAC's open.canada.ca CKAN route is verified open. Suggest BAnQ/AO to ⚪ until a stage-2 browser check (candidate).
3. **StatCan WDS API is verified live (5 MB JSON cube list)** although the front data page showed an "unavailable" banner at probe time: 🟢 is right, but do not use the HTML page as the liveness probe.
4. **Moved sites**: Carleton CURVE now at carleton.scholaris.ca; Ottawa & District Labour Council now at ottawalabour.labourcouncils.ca; LAC homepage now canada.ca/en/library-archives.html; OREB /market-statistics/ is 404. ottawa.ca pages (community associations, BIAs, employment/collective agreements) returned only ~1 KB Incapsula shells, so they are unverified.
5. **Bike Ottawa 🟢 looks unsupported**: real site, only an "open data" string and RSS found; no dataset endpoint located (candidate: 🟡). Also, uOttawa RUOR and Carleton Scholaris are DSpace-style repositories exposing /api/ plus atom/RSS: an uncatalogued machine-readable surface for theses and GIS holdings (candidate; front page only). CBC Ottawa RSS (24 KB, verified) is likewise an open feed.

Not reached: Mapbox, CFRA own site, Orléans Star, Ottawa Food Bank beyond 403. Probe files saved under /tmp/claude-1000/-workspace/4a16e5ff-6228-45a3-8866-10d5bdbb0655/scratchpad/p4/.

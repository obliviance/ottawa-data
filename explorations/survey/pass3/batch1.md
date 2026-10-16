# Survey pass 3, batch 1 (probed live 2026-10-16)

Method: curl (UA `ottawa-data-recon/0.1`), at most about 8 requests per source, 2s spacing. Downloads kept under the scratchpad `b1/`. "verified" means checked two independent ways; "candidate" means seen once.

**Cross-cutting finding (verified):** every `ottawa.ca` URL (open-data-policy, campaign-finance, election-key-dates, the who-is-running page, legacy-agendas after redirect) returns a 1.1 KB Incapsula bot-challenge shell to curl, with both our UA and a Chrome UA, and with 200 status. The stage-0 record (`verification.json`) shows `bytes: 212`/`1158`, `title: null`, and still scored `reachable_html`. Those are false-positive liveness results. Stage 2 (real Chromium, 2026-09-09) did render them. So the pages are html-accessible only through a real browser, not curl or `_http.py`. The eScribe document downloader is similarly Cloudflare-challenged (see escribe).

### open-ottawa
LIVE. Access tag `api, bulk`: matches, but "every dataset" is overstated.
- **verified** DCAT feed `https://open.ottawa.ca/api/feed/dcat-us/1.1.json` returns 200, 2.67 MB, 703 datasets (stage 0 saw 695 on earlier dates, so it is growing). `ouverte.ottawa.ca` 200 (French mirror) and `/pages/developer-resources` 200, but the latter has the same title and about the same size as the home page (a Hub SPA shell; its content is JS-rendered).
- **anomaly (verified)** The description "Every dataset exposes GeoService and GeoJSON endpoints" is false. Distribution counts in DCAT: 364 of 703 have "ArcGIS GeoServices REST API"; 289 have CSV/GeoJSON/KML; 301 ZIP; 12 each XLSX/GPKG/TXT; 21 OGC WMS. The other 339 are Hub "documents" or pages (a Web Page link only), e.g. `2022 Elections Official Results`, `2026 Municipal Elections – Nominated candidates` (an xlsx file under `arcgis.com/sharing/rest/content/items/<id>/data`, 200, 24,831 bytes).
- **anomaly (verified)** Licence drift. 443 of 703 DCAT `license` fields point to `ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-version-2-0`; about 99 and 29 link the policy/about page; 39 are empty. The ottawa.ca nav (stage 2) lists "Open Data licence version 2.0" and "Open Data License change: FAQ", but the policy page body (same capture) still says "Open Government License". `sources.json` and stage 3 say "Open Government Licence – City of Ottawa" for everything, which is probably stale.
- **anomaly (verified)** DCAT contains an unrendered template record (`modified: "{{modified:toISO}}"`, description `{{description}}`, e.g. "Election Data and Resources", a page rather than a dataset). Count the 703 as roughly 702 real items.
- **unique** Freshness signal: `modified` dates cluster in 2026 (411 of 703), many 2026-08-10 (mass re-save, not real updates); latest 2026-10-16. 2026 election items: `2026 Elections Voting Subdivision Map` 2026-10-14, `Wards 2026-2030` 2026-09-24 (layer `Planning/MapServer/277`, 24 features, `LAST_EDITED_DATE` 2026-05-25).

### arcgis-rest-root
LIVE. Access tag `api, bulk`: matches (bulk only via query `f=geojson`).
- **tag-fix / anomaly (verified)** Description says "FeatureServer layers export GeoJSON/CSV". The root `?f=pjson` (200, v10.81) lists 80 services: 77 MapServer, 2 GeocodeServer, 1 GPServer, plus folder `Utilities` (GeometryServer + 2 GPServer). There are zero FeatureServer entries. GeoJSON works through MapServer: `Planning/MapServer/277/query?where=1=1&f=geojson` returned 200 and 24 features (count query 200 `{"count":24}`); `Wards/MapServer` advertises capabilities `Map,Query,Data`, maxRecordCount 1000, WMSServer extension. Say "MapServer query f=geojson", not FeatureServer.
- **unique (candidate)** Historic imagery services `Basemap_Imagery_1928, 1958, 1965, 1976, 1991, 1999, 2002...2022` (about 22 vintages); `Zoning_Bylaw_2026_50` alongside `Zoning_Bylaw_2008_250` (new bylaw, not yet in the catalogue prose); `Development_Applications`, `ConstructionForecastData`, `Wards`, `OPS_Geographies`.
- **anomaly (candidate)** `rest/info` shows token-based security enabled (`tokenServicesUrl .../arcgis/tokens/`), yet root and queries are anonymous; unauthenticated for the services listed, a secured service (`securedPrint`) exists.

### geoottawa
LIVE (SPA). Access tag `html, api`: matches (the viewer itself is html; the API is the REST root).
- **candidate** `https://maps.ottawa.ca/geoottawa/` 200, 4,625 bytes, IIS/10; a Web AppBuilder loader (`jimu.js`, `init.js`) plus a Google Analytics UA property (`UA-36718000-4`, the sunset Universal Analytics ID). Needs a browser, as stage 0 says. Nothing unique beyond the REST root.

### open-data-policy
DEGRADED for programmatic access (Incapsula challenge to curl; renders in a browser). Tag `html`: matches.
- **verified** curl with both UAs returns 200 and a 1,155-byte challenge page; stage 2 shows it redirects to `.../open-data/about-open-data` and renders 899 chars.
- **anomaly (verified)** The URL in `sources.json` redirects; the page body says "Open Government License" while its own nav has "Open Data licence version 2.0" (see open-ottawa). The licence text sits on a separate page not yet catalogued; it is the real licence record.

### candidate-list
LIVE. Access tag `api, html`: matches. (Stage 3 record is stale: it still says `claimed html`.)
- **verified** `https://elections.ottawa.ca/ws/api/Candidates/Councillors/` 200, 87 rows; `/Mayors/` 14; `/Trustees/` 80; total 181 = the warehouse `election_candidates` row count (87/14/80 by office), so no change since the last ingest. `/Wards` 25 entries (24 wards plus one extra; no `WardNumber` 0/25 named); `/SchoolBoards` 5 entries (four boards plus a "Not Eligible / N/E" placeholder, `Name` fields like "English Public School Board").
- **anomaly (verified)** The description's "four school boards" is right, but the API returns five including N/E. Wards 16 and 21 have exactly one councillor candidate each (probable acclamations); ward 6 has 9. Latest `NominationDate` 2026-08-21; the earliest 2026-05-01.
- **anomaly (candidate)** No `Status`/withdrawn field in the JSON (keys: `NominationDate, RebateProgram, WardNumber, WardName, TelephoneNumber, EmailAddress, SocialMediaInfo, Id, Locale, Name`), so withdrawals are invisible here. The open-data xlsx `List_Nominated_Candidates_Open_Data_2026_BIL.xlsx` (6 sheets: mayor, councillor, OCSB, OCDSB, CECCE, CEPEO) has a "Date withdrawal of nomination filed" column. Mayor sheet has 14 nomination dates, same as the API; I did not reconcile the other sheets (layouts differ).
- **unique (candidate)** The web service also exposes `ForVoter/<voterID>` and `Trustees/ForAddress/<addr>/<schoolSupportID>` routes (seen in page JS). Candidate rows carry personal-looking phone and email (public by design, but note for any privacy/COI reasoning).

### who-is-running
DEGRADED for the address flow; the roster is shared with candidate-list. Tag `api, html`: matches in principle.
- **verified** The base `.../Candidates/Councillors/ForAddress/` returns 404 (as in stage 0; it needs an id suffix, so the catalogued URL is not itself a live endpoint). `Streets/Mask/Bank` returns 200 and 5 rows (`BANK ST` id `1b04ae4c-...`).
- **anomaly (candidate)** The documented next step `Addresses/<streetNumber>/<streetId>` returned 204 No Content for numbers 1, 110 and 300 on Bank St, so I could not complete the address-to-candidates chain. The correct parameter order or format may differ from the description's `Addresses/<id>`; the page JS uses `Addresses/<nr>/<streetId>`, which is what I tried. Not confirmed broken, only unconfirmed; worth a browser capture.
- The ottawa.ca page is Incapsula-walled to curl (see cross-cutting).

### campaign-finance
DEGRADED (walled to curl), and no data yet. Tag `html`: matches.
- **verified** Both listed URLs return the 212/1.1 KB challenge shell to curl; stage 2 renders them (the first redirects to `.../campaign-period`). The compliance-reports page (2022 filings) is the actual data page.
- **candidate** Description says 2026 filings land about March 2027 (consistent with stage-2 text mentioning March). Nothing to fetch today. Whether the 2022 reports are PDFs or a table was not checkable by curl.

### election-key-dates
DEGRADED for curl; renders in a browser. Tag `html`: matches.
- **verified** Stage 2 text confirms 1 May 2026 start, 21 Aug 2pm nomination day, 26 Oct 2026 election. Both sources.json URLs are walled to curl.
- **candidate** The "information for candidates" page points to a "Certified and acclaimed candidates" list, so acclamations are an official category (consistent with wards 16 and 21 above). Nothing else notable.

### election-results-history
LIVE, but the tag is partly wrong. Tag `api, bulk`: differs.
- **tag-fix (verified)** Poll-level results are NOT served as a GeoServices API. In DCAT, `2022 Elections Official Results`, `Elections 2010 results poll by poll`, and the nominated-candidate lists have only a "Web Page" distribution (they are Hub documents; downloads are xlsx/pdf files). The API layer applies only to geometry (`Wards 2026-2030` / `2022-2026` / `2014` / `2010` / `2006` / `2003` historical, and voting subdivision areas). Suggest tagging the results part `bulk` (file) and the geometry `api, bulk`.
- **unique (verified)** The warehouse has poll-level 2022 results: `election_results_2022_polls` 16,701 rows over 24 wards (623,148 votes summed), totals 121 rows (Councillor 107, Mayor 14). Also landed: 2010/2014/2018/2022 voting places and subdivisions, turnout 2010. The catalogue holds a ward-history series back to 2003 (DCAT titles "Wards 2003 (Historical)" and "Wards 2006 (Historical)", modified 2026-10-07).
- **verified** Wikipedia both pages 200: 2026 article 157 KB, last revised 2026-10-12; 2022 article 206 KB, revised 2026-09-19; 71 wikitables on the 2026 page. The 2026 page is a live, edited article so it is volatile (election 26 Oct).
- **anomaly (candidate)** Poll-level results for 2014 appear only as "Statement of votes cast (Poll by Poll)" (a document) and 2018 as "Ottawa 2018 Election Results"; neither is a tabular dataset in the warehouse (the warehouse has 2022 only).

### escribe
LIVE (calendar JSON), DEGRADED for documents. Tag `api, html`: matches for the index; documents are blocked.
- **verified** POST `https://pub-ottawa.escribemeetings.com/MeetingsCalendarView.aspx/GetCalendarMeetings` with `{"calendarStartDate":..,"calendarEndDate":..}` returns 200 JSON: 11 meetings in Oct 2026 (Council 2026-10-08, ARAC, Committee of Adjustment panels, Police Board committees); for June to July 2012, 13 meetings (earliest 2012/06/19 Environment Committee in my window), which confirms the pre-2018 depth.
- **unique (verified)** Each record carries `MeetingDocumentLink` (Agenda PDF/FR PDF `FileStream.ashx?DocumentId=NNNNN`; e.g. 2012-07-04 Transportation agenda = 15207, Council 2012-07-11 = 12836), `HasVideo`, `HasLiveVideo`, `AllowPublicComments`, `IsMP3`, `DelegationRequestLink`. So a meeting-to-document-id map is available from the index alone, no scraping.
- **anomaly (verified)** The document endpoint is blocked: `GET /FileStream.ashx?DocumentId=15207` returns 403 with `cf-mitigated: challenge` (307 KB Cloudflare page), for both GET and range request, also HEAD. The description's "systematic harvesting tractable" holds for the index but not for PDF fetches from curl/urllib. Document ids are also not sequential in time (15207 for 2012-07-04 vs 12836 for 2012-07-11), so an id sweep does not map to dates.
- **anomaly (verified)** Warehouse `spine_meetings` (2,290 rows) starts 2018-01-11, while eScribe goes back to 2012 (observed 2012-06/07). About 8 years of meeting index are not yet landed; 570 spine rows are in howtheyvoted. Warehouse includes scheduled meetings through 2026-10-20 (future rows match the live feed).

### legacy-agendas
DEAD as catalogued (redirect), the old app was live a year ago. Tag `html, request`: differs.
- **verified** Live `https://app06.ottawa.ca/cgi-bin/docs.pl?lang=en` returns 302 to `https://ottawa.ca/en/node/1029405` (final 200, 1,050-byte Incapsula shell to curl); `app06.ottawa.ca/` returns 301 to `https://ottawa.ca`. Wayback `20250908205131` shows the same URL serving the "City Council & Committee Agendas & Minutes" CGI app (25,106 bytes, 200). Wayback has no capture of `node/1029405` before the repo's 2026-09-09 snapshot (query at 2024-01-01 returned empty). So the legacy application was retired and replaced with a redirect sometime between Sept 2025 and Sept 2026.
- **tag-fix (candidate)** Drop `html`; the pre-2012 route now looks `request` only (plus Wayback for 2025-era copies and the City Archives). What `node/1029405` says could not be read without a browser. Stage 3 also marked it `observed: html` only.

### council-video
LIVE. Access tag `html, api`: partly differs.
- **verified** Channel `https://www.youtube.com/channel/UCUR3i_hvk3-3i8vtrPg6v1Q` 200 (stage 2: "Ottawa City Council", @ottcitycouncil, 1.4k videos). The keyless RSS feed `https://www.youtube.com/feeds/videos.xml?channel_id=UCUR3i_hvk3-3i8vtrPg6v1Q` returns 200, 15 entries, newest 2026-10-10 (Police Board Finance and Audit Committee 2026-10-09, Council & Media Availability 2026-10-08, Planning and Housing Committee 2026-10-07). Channel feed oldest `published` shown 2017-09-05 on the feed header.
- **tag-fix (candidate)** "api" is real but not from the City: either the keyless RSS (last 15 only) or the YouTube Data API (needs a key). Not tested: yt-dlp is not installed here, so the auto-caption claim stays unverified.
- **unique (verified)** eScribe meetings flag `HasVideo`/`HasLiveVideo` per meeting, so the eScribe index is the natural join key to the video list (and 1,4xx channel videos vs 2,290 spine meetings).
- **anomaly (candidate)** Subscriber counts differ between captures (stage 2: 6.12k; page now shows "12.3 thousand" and "831" labels, probably the related channels in the page JSON, not the channel; unreliable).

## Three most interesting findings
1. **Incapsula wall on all ottawa.ca pages:** stage-0 `reachable_html` for 5 sources of this batch is a false positive (212-byte shell, `title: null`). A plain-HTTP tool cannot read them; only stage-2 Chromium can. Re-score stage 0 for `ottawa.ca` hosts.
2. **legacy-agendas is gone:** `app06.ottawa.ca/cgi-bin/docs.pl` now 302s to `ottawa.ca/en/node/1029405`; Wayback shows the CGI app live on 2025-09-08 with 25 KB of content. The tag should drop `html`.
3. **Description/tag errors in the election and GIS entries:** poll-level results are file documents, not a GeoServices API (`election-results-history`); `arcgis-rest-root` has 77 MapServers and no FeatureServer; and `open-ottawa` "every dataset exposes GeoService and GeoJSON" is true for only 364 of 703. In addition, eScribe's index goes back to 2012 but the warehouse spine starts in 2018, and its PDF endpoint is Cloudflare-challenged.

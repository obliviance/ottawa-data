# Probe pass 4, batch 3 (uncat3 rows)

Method: per row, `curl -sIL` then a GET (UA `Mozilla/5.0 ... ottawa-data-probe`), 2 s apart, one extra retry for failures. Date 2026-10-16. Saved bodies in scratchpad `p3/` (untrusted, never executed). "verified" = HEAD and GET agree plus body inspected; "candidate" = single signal or no probe. Machine-readable = only what the probed pages or one API call showed, not exhaustive.

Caveat: canada.ca returns HTTP/2 INTERNAL_ERROR to curl from this host (twice), so PSPC, DND, LAC (final hop) were not reachable. Two "SSL certificate problem: unable to get local issuer certificate" errors (Ottawa Hospital, Teranet HPI) are probably this host's CA bundle, not site failure; treat as unreached.

| row | URL | status / liveness | machine-readable? | emoji correct? | note |
|---|---|---|---|---|---|
| OSTA | https://www.ottawaschoolbus.ca/ | 403 + Cloudflare "Just a moment" shell (5 KB) on HEAD and GET: **not live evidence** | unknown | keep 🟡 (candidate) | Cannot confirm cancellation feed from here; needs stage-2 browser. |
| EQAO results | https://www.eqao.com/results/ | 200, 584 KB real page (verified); `/about-eqao/open-data/` linked | yes, open-data page linked (not downloaded) | keep 🟢 (verified live, candidate for bulk) | Next step: fetch open-data page. |
| MinEdu school data | https://data.ontario.ca/dataset/school-information-and-student-demographics | 200; CKAN `package_show` API returned `success:true, access_level:open` (verified two ways) | yes, CKAN API + downloads | keep 🟢 | This is the Ontario CKAN, ingestible with tools/ingest/ckan.py. |
| Mississippi-Rideau SPR | https://www.mrsourcewater.ca/en/ | 301 -> 200, 131 KB, Apache (verified) | none seen in homepage | keep 🟡 | Plans/reports as HTML/PDF. |
| Ottawa River Regulation Planning Board | https://www.ottawariver.ca/ | 301 -> 200, 80 KB (verified) | none seen on homepage; board publishes flows/levels pages (candidate, not probed) | keep 🟢 | Domain `ottawariver.ca` redirects to www. |
| Canada Lands Company | https://www.clcl-sicl.ca/ | `clc-sic.ca` 302 -> `clcl-sicl.ca`, then 403 Cloudflare challenge | unknown | keep 🟡 (candidate) | **Domain moved** to clcl-sicl.ca; old domain still redirects. |
| PSPC | https://www.canada.ca/en/public-services-procurement.html | not reached (HTTP/2 INTERNAL_ERROR) | candidate: open.canada.ca datasets, CanadaBuys (not probed) | keep 🟢 (candidate) | Not reached. |
| Parks Canada Rideau | https://parks.canada.ca/lhn-nhs/on/rideau | 200, 52 KB, IIS (verified) | none on page; Rideau water-level/ops data not probed | keep 🟢 | |
| DND | https://www.canada.ca/en/department-national-defence.html | not reached | closed/FOI: no public endpoint confirmed (candidate) | keep 🔴 (candidate) | ATIP only; DND also publishes proactive disclosure on canada.ca (not probed). |
| Ottawa Airport / Transport Canada | https://www.yow.ca/ | `yow.ca` 301 -> www; HEAD 403 but GET 200, 250 KB real page (HEAD/GET disagree, body real: verified live) | none seen | keep 🟡 | Cloudflare treats HEAD differently from GET. |
| Library and Archives Canada | https://library-archives.canada.ca/ | 302 -> canada.ca/en/library-archives.html (BigIP); target not reached | candidate: open.canada.ca, Collection Search | keep 🟢 (candidate) | Domain now a redirect into canada.ca. |
| Elections Canada | https://www.elections.ca/ | 200, 4.5 KB splash page (language chooser), real site | not probed (candidate: Open data on elections.ca) | keep 🟢 (candidate) | 4.5 KB is a bilingual splash, not a challenge. |
| RCMP | https://rcmp.ca/en | `rcmp-grc.gc.ca/en` 301 -> `rcmp.ca/en`, 200, 26 KB (verified) | none seen | keep 🔴 (candidate) | **Domain moved** to rcmp.ca. |
| CMHC | https://www.cmhc-schl.gc.ca/ | 200, 151 KB (verified); chal-regex hit is a sign-in link, not a challenge | none seen on homepage (Housing Market Information Portal is separate, not probed) | keep 🟢 (candidate) | |
| Federal MP constituency offices | https://www.ourcommons.ca/members/en | 200, 134 KB; HEAD chain odd (302->404 ErrorPage) but GET 200 | member list pages public (offices/addresses listed per MP, HTML); XML/CSV export exists on ourcommons (candidate, not probed) | **change 🔴 -> 🟡** (candidate) | Constituency office addresses are public per MP; "closed" is wrong at the directory level. |
| Ontario Health / Ottawa Hospital | https://www.ontariohealth.ca/ ; https://www.ottawahospital.on.ca/ | OH 200, 71 KB (verified). Ottawa Hospital not reached (SSL local-issuer error) | none seen | keep 🟢 (candidate) | |
| Ontario Health atHome | https://ontariohealthathome.ca/ | 200, 105 KB (verified) | none seen | keep 🟡 | Live under the new name. |
| Public Health Ontario | https://www.publichealthontario.ca/ | 200, 140 KB; links `/en/Data-and-Analysis/Using-Data/Open-Data` (verified link) | yes, open-data page + Snapshots (not downloaded) | keep 🟢 | |
| Provincial Offences Act court | https://www.ontario.ca/page/provincial-offences-act-courts | **404** (my guessed path; no real URL found) | unknown | keep 🟡 (candidate) | "not found"; do not use this URL. |
| Landlord and Tenant Board | https://tribunalsontario.ca/ltb/ | 200, 65 KB; links `/en/about/open-data/` | yes, Tribunals Ontario open-data page (not downloaded) | **change 🟡 -> 🟢?** (candidate) | Open-data page exists; check content/format and that it covers Ottawa before changing. |
| Law Enforcement Complaints Agency | not found | `leca.ca` no response; `lecaontario.ca` does not resolve | unknown | keep 🟡 (candidate) | Site not located; needs search. |
| SIU | https://www.siu.on.ca/ | 200, 267-byte meta-refresh to `/en/index.php` (a redirect stub, not a challenge) | not probed | keep 🟡 (candidate) | Case directory public HTML (candidate). |
| Elections Ontario | https://www.elections.on.ca/ | 200, 11 KB landing (verified) | not probed (candidate: results/finance data downloads) | keep 🟢 (candidate) | |
| AGCO | https://www.agco.ca/en | 301 -> 200, 416 KB, Fastly (verified) | none seen | keep 🟡 | |
| TSSA | https://www.tssa.org/ | 200, 60 KB, nginx (verified) | none seen | **keep 🔴?** (candidate) | Site is live but data openness unprobed; a pure "closed" tag may be harsh if public registers exist. |
| Ontario Heritage Trust | https://www.heritagetrust.on.ca/ | 200, 132 KB (verified) | none seen | keep 🟡 | |
| MCCSS | https://www.ontario.ca/page/ministry-children-community-social-services | **404** (guessed path) | unknown | keep 🟢 (candidate) | Not found at guessed path. |
| OMERS | https://www.omers.com/ | 200, 398 KB (verified) | none seen | keep 🟡 | |
| IPC Ontario | https://www.ipc.on.ca/ | 403 Cloudflare "Attention Required" (HEAD and GET): **not live evidence** | unknown | keep 🟢 (candidate) | IPC decisions are public, but needs browser stage. |
| Auditor General of Ontario | https://www.auditor.on.ca/ | 200, 41 KB (verified) | none seen (reports PDF/HTML) | keep 🟡 | |
| Ville de Gatineau | https://www.gatineau.ca/portail/default.aspx?p=accueil | 200 after 2 redirects, 35 KB, IIS (verified) | none seen on homepage (open data is a sub-page, not probed) | keep 🟡 (candidate) | |
| STO | https://www.sto.ca/ | 200, 78 KB (verified); `/en/open-data` guess **404** | none found on homepage; GTFS not located | keep 🟢 for GTFS only as **candidate**; unverified | I could not find GTFS link in 3 requests. |
| Neighbouring municipalities | https://www.prescott-russell.on.ca/ | 200, 151 KB (verified; Cloudflare in front but real page) | RSS feeds (news/summary) on homepage | keep 🟡 | Lanark/others not probed. |
| NCC planning coordination | https://ncc-ccn.gc.ca/ | 200, 112 KB (verified) | not probed | keep 🟡 (candidate) | |
| Chief Coroner inquests | https://www.ontario.ca/page/office-chief-coroner | **404** (guessed path) | unknown | keep 🟡 (candidate) | Not found. |
| Public inquiries | https://publicorderemergencycommission.ca/ ; ottawalrtinquiry.ca | POEC 200, 46 KB (verified). `ottawalrtinquiry.ca` **does not resolve** | POEC: documents HTML/PDF | keep 🟢 | LRT inquiry real domain is different (not found); my guess is wrong, not necessarily dead. |
| Ontario Ombudsman | https://www.ombudsman.on.ca/ | 403 Cloudflare challenge: **not live evidence** | unknown | keep 🟡 (candidate) | |
| Enbridge Gas | https://www.enbridgegas.com/ | 200, 103 KB (verified) | none seen | keep 🟡 | |
| Hydro One | https://www.hydroone.com/ | 200, 102 KB (verified) | none seen | keep 🟡 | |
| IESO | https://www.ieso.ca/ | 200, 60 KB (verified) | none on homepage, though IESO publishes reports data (candidate) | keep 🟢 (candidate) | |
| Bell / Rogers / Telus | https://www.bell.ca/ | 200, 298 KB (Bell only) | none | keep 🟡 | Others not probed. |
| CRTC | https://crtc.gc.ca/ | 403 Cloudflare "Security Check" (21 KB): **not live evidence** | unknown (CRTC publishes open data on open.canada.ca, candidate) | keep 🟢 (candidate) | |
| Railways | https://www.viarail.ca/en | 302 -> 200, 547 KB (VIA only; verified) | none seen | keep 🟡 | CN/CP/Ottawa Central not probed. |
| Pipelines (CER) | https://www.cer-rec.gc.ca/en/ | 200, 41 KB (verified); root is a 5 KB language splash | not probed (CER has open data/Energy Futures, candidate) | keep 🟡 (candidate) | |
| OnLand | https://www.onland.ca/ui | 302 -> 200, 61 KB (verified) | paywalled searches | keep 🔴 (candidate) | |
| City property-tax accounts | https://ottawa.ca/en/living-ottawa/taxes-and-assessments | 200 but only 1 KB with bot-challenge markers: **not live evidence** | none; account lookup is per-account | keep 🔴 (candidate) | Per-account only, so no bulk endpoint; city-wide assessment roll is MPAC (not probed). |
| Condominium Authority of Ontario | https://www.condoauthorityontario.ca/ | 200, 267 KB (verified) | public registry search (HTML); no bulk seen | keep 🟡 | |
| Property surveys / reference plans | https://www.aols.org/ (professional body) | 200, 37 KB (verified) | none; plans held in OnLand (paywall) | keep 🔴 (candidate) | No public endpoint found. |
| Title insurance / transaction data | not found | FSRA (`fsrao.ca`) 403 Cloudflare challenge | none | keep 🔴 (candidate) | Private-sector data; no public endpoint. |
| Teranet-NB HPI | https://housepriceindex.ca/ | not reached (SSL local-issuer error; `www.` same) | candidate: index series publicly published | keep 🟢 (candidate) | Retry from another host. |
| Ecology Ottawa | https://www.ecologyottawa.ca/ | 301 -> 200, 176 KB (verified) | none | keep 🟡 | |
| Bike Ottawa | https://bikeottawa.ca/ | 200, 113 KB (verified) | none seen | keep 🟢 | Advocacy site; "open" means public information, not data. |
| Healthy Transportation Coalition / Free Transit Ottawa | https://www.healthytransportation.ca/ | **404**, 0 bytes, Cloudflare | unknown | keep 🟡 (candidate) | Guessed domain, likely wrong or dead; not found. |

## Rows not reached or inconclusive
PSPC, DND, LAC (canada.ca failures); Ottawa Hospital, Teranet HPI (local SSL); OSTA, CLC, IPC, Ombudsman, CRTC, FSRA (Cloudflare challenge pages); LECA, LRT Inquiry (no domain found); POA court, MCCSS, Coroner (my guessed ontario.ca paths 404); Healthy Transportation (404).

## Five most notable findings
1. **Domain moves**: Canada Lands Company is now `clcl-sicl.ca` (old `clc-sic.ca` 302s there); RCMP is now `rcmp.ca` (old `rcmp-grc.gc.ca` 301s). Update any catalogued URLs. LAC `library-archives.canada.ca` now redirects into canada.ca.
2. **Possible wrong emoji, Federal MP constituency offices**: ourcommons.ca member directory is a live public page listing offices per MP, so 🔴 looks wrong (suggest 🟡). Candidate.
3. **New open surface not catalogued**: Tribunals Ontario publishes an open-data page (`tribunalsontario.ca/en/about/open-data/`) linked from the LTB site; check whether it has Ottawa-level LTB case data (LTB row may merit 🟢). Also Public Health Ontario `Open-Data` page and EQAO `/about-eqao/open-data/` are linked and uncatalogued, candidates for ingest.
4. **Verified open API**: Ontario CKAN `data.ontario.ca` `package_show` for school-information-and-student-demographics returns `success:true`, open access (two-way verified). Ministry of Education school data row is a clean CKAN ingest target.
5. **Bot-challenge traps**: OSTA, IPC, Ombudsman, CRTC, FSRA, CLC and the City tax page (1 KB shell) returned challenge pages; their 200/403 is not evidence either way, so those rows' emojis stay unconfirmed pending a stage-2 browser run. Also two guessed domains did not resolve (`ottawalrtinquiry.ca`, `lecaontario.ca`); correct domains not found.

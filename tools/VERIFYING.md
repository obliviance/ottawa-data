# Verifying the catalogue

Every entry in [`sources.json`](../sources.json) started as a guess: it was compiled from
search-result snippets in an environment with no outbound HTTP. This file describes how the
guesses become confirmed facts, and what the tooling here does automatically.

## The stage model

| Stage | Question | Tool | Cost |
| --- | --- | --- | --- |
| **0 — liveness** | Does the URL resolve? Status, redirects, content-type, size, timing. | [`verify.py`](verify.py) | seconds |
| **1 — fingerprint** | Is there a machine-readable surface? ArcGIS REST, ArcGIS Hub / DCAT, CKAN, Socrata, Open311 discovery, GTFS zip, PDF. | [`verify.py`](verify.py) | seconds |
| **2 — browser** | What does a JavaScript page actually render, and which XHR does it call? | [`verify_stage2.py`](verify_stage2.py) — headless Chromium over CDP | ~15 s per page |
| **3 — access + licence** | Is the access tag right? What licence applies? | [`verify_stage3.py`](verify_stage3.py) — metadata APIs + page reads, heuristic | ~1 s per source |
| **archive** | Snapshot the evidence before it rots. | [`snapshot.py`](snapshot.py) — Wayback Machine | ~6 s per URL |

All five are implemented. Stage 3 is heuristic — it is good at spotting a source that is *more*
open than its tag claims (an ArcGIS/CKAN API behind a `Bulk` tag), and honest when it cannot
reach a keyed or JS-gated download (`unconfirmed`), but its verdicts are leads, not gospel.
`Request` (FOI / in-person) it cannot check at all.

Each run writes its own JSON, checked into `verification/` as the record; `build_readme.py` folds them
all into README.md. The files are machine-written — do not hand-edit them. Stage 2 captures live
XHR URLs, so `redact()` strips any `access_token` / `authKey` / `key` query value before writing
(some Ottawa apps ship a client-side key to every browser — public, but not ours to republish).

## Running it

```
pip install playwright                        # stage 2 only; the browser binary is remote

python3 verify.py                              # stage 0-1  -> verification.json
python3 verify.py --stale 30                   #   skip URLs that passed within 30 days
python3 verify_stage2.py                       # stage 2    -> verification_stage2.json
python3 verify_stage2.py --only devapps        #   one source
python3 verify_stage3.py                       # stage 3    -> verification_stage3.json
python3 snapshot.py --delay 8                  # wayback     -> snapshots.json
python3 build_readme.py                        # fold all of the above into README.md
```

### Stage 2 needs a Chromium over CDP

`verify_stage2.py` connects to a running headless Chromium via the Chrome DevTools Protocol at
`$CHROMIUM_CDP_URL` (default `http://chromium:9222`). That endpoint enforces Chrome's
Host-header check, so the script fetches `/json/version` with `Host: localhost` and rewrites the
websocket URL to the container IP — see `cdp_ws()`. Point `--cdp` elsewhere if your browser
lives somewhere else; any `chrome --headless --remote-debugging-port=9222` will do.

### Politeness

Stage 0-1 serialises requests per domain with a delay + jitter, sets a descriptive User-Agent,
retries once on a transient failure, and does **not** enumerate search indexes or walk
`DocumentId` ranges — that is a per-source decision to make with the site's terms in view.
`snapshot.py` respects the Wayback Machine's rate limit.

### Stage 0-1 outcomes

| Outcome | Meaning |
| --- | --- |
| `machine-readable` | A probe confirmed an API / catalogue feed / GTFS zip. |
| `pdf` | The URL serves a PDF. |
| `reachable_html` | Loads as server-rendered HTML with real content. |
| `needs_browser` | Loads, but the body is a JavaScript shell — hand to Stage 2. |
| `blocked` | HTTP 401/403/429 — the server answered but refused this client (bot filter). |
| `error` / `dead` | HTTP 4xx/5xx / no DNS. |

## What verification has found so far

### Stale or dead links (fix these in sources.json)

- **`open311`** — `city-of-ottawa-prod.apigee.net/open311/v2/` no longer resolves and the docs
  page 404s. The verify-flag was right; the entry needs a live endpoint or a downgrade.
- **`collisions`** and several others — the `open.ottawa.ca/datasets/ottawa::<slug>/about` URL
  format 404s. The current form is `/datasets/<id>`.
- **`ottawa-civic-tech`** — `ottawacivictech.ca` does not resolve (the GitHub org link is fine).
- **`school-boards`** — `ecolecatholique.ca` (CECCE) does not resolve for the harness.

### Access tags that are understated (Stage 3 — the data is more open than the tag says)

- **`howtheyvoted`** (`HTML` → has an API) — ships its compiled Ottawa council voting record as
  JSON at `howtheyvoted.ca/data/ottawa/index.json` and `…/dates/<YYYY-MM-DD>.json`, current to
  within days. A real secondary source for the "recorded votes" gap.
- **`devapps`** (`HTML` → has an API) — `devapps-restapi.ottawa.ca/devapps/{feature,apptype,ward}/all`
  returns JSON. (An `authKey` is shipped to every browser; treat it as public, not a secret.)
- **`engage-ottawa`** (`HTML` → has an API) — runs on EngagementHQ; `engage.ottawa.ca/api/v2/…`
  serves projects, navigation and site metadata.
- **`escribe`** (`HTML` → partial API) — `MeetingsCalendarView.aspx/GetCalendarMeetings` returns
  the meeting *index* as data. The staff reports and minutes behind it are still unstructured PDFs.
- **`geoottawa` / `historical-imagery`** — a Web AppBuilder viewer over the already-catalogued
  `maps.ottawa.ca/arcgis` services plus `tiles.arcgis.com/tiles/G6F8XLCl5KtAlZ2G/` vector tiles.
- **`fir`, `crime-map`, `fire-paramedic`, `election-results-history`, `recreation`,
  `ottawa-public-health`, `arcgis-rest-root`** — an ArcGIS GeoServices or CKAN API sits behind
  what the catalogue tagged `Bulk` or `HTML`.

### Could not confirm automatically (`unconfirmed` — needs a key, a login, or is FOI)

`octranspo-gtfs` (free API key), `open-canada` / `statcan-census` (JS-gated bulk download),
`budget-documents` / `conservation-authorities` (claimed `Bulk`, only a PDF page seen),
`mpac`, `community-data-program`, `city-archives`, `legacy-agendas`, `mfippa-disclosure`
(genuine request / restricted access).

### Bot filters

`canlii.org` and, intermittently, `ottawa.ca` serve a challenge page to non-browser clients and
sometimes to headless Chromium too. CanLII content is real; verify it in an ordinary browser or
via the CanLII API (free key on request).

## Licence

Resolved by operator. **City of Ottawa / OC Transpo / Ottawa Police / OPH / OPL** → Open
Government Licence – City of Ottawa. **Province** → Open Government Licence – Ontario.
**Federal / NCC** → Open Government Licence – Canada. **Statistics Canada** → its own open
licence. **Wikipedia** text → CC BY-SA. **CanLII** → terms of use, reproduction restricted.
Advocacy sites, newsrooms and `howtheyvoted.ca` carry ordinary site terms with no open-data
grant — usable as sources, but not re-publishable as open data without asking.

## Cost, in short

Money: ~zero. Every target is public. The only pay-per-hit surface in the wider
[`hierarchy.md`](../hierarchy.md) is the Ontario land registry (Teranet / OnLand); confirming it is
paywalled needs no purchase. Optional spend: an LLM for Stage 3 triage (cents per source), a
hosted headless browser if you have none.

Time: stages 0-1 and 3 are minutes each; stage 2 is ~15 s per page; a full snapshot run is
~10 minutes. Extending all of it to the `hierarchy.md` branches is 2-3 days of mostly Stage 3.

## Keeping it current

A scheduled job running `verify.py --stale 7` weekly (plus `verify_stage2.py` monthly) catches
link rot and re-checks the JavaScript sources; wire it to open a PR when `verification*.json`
changes. **OttWatch** and **Ottawa Civic Tech** have already verified a large slice of this —
ask before re-walking it.

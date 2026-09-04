# Verifying the catalogue

Every entry in [`sources.json`](sources.json) started as a guess: it was compiled from
search-result snippets in an environment with no outbound HTTP. This file describes how the
guesses get turned into confirmed facts, and what the tooling here does automatically.

## The stage model

| Stage | Question | Who / what | Cost |
| --- | --- | --- | --- |
| **0 — liveness** | Does the URL resolve? Status, redirects, content-type, size, timing. | [`verify.py`](verify.py), automated | seconds of compute |
| **1 — fingerprint** | Is there a machine-readable surface behind the page? ArcGIS REST, ArcGIS Hub / DCAT feed, CKAN, Socrata, Open311 discovery, GTFS zip, PDF. | [`verify.py`](verify.py), automated | seconds of compute |
| **2 — browser** | What does a JavaScript page actually render, and which XHR does it call? (The lobbyist registry, dev-apps search and Engage Ottawa each have an internal JSON endpoint the SPA talks to.) | headless browser (Playwright), semi-automated | ~1 min per SPA |
| **3 — judgement** | Is the access tag right? Is "Bulk" a real CSV or a Tableau embed? What is the licence? What is the file-number scheme? | human, or LLM triage spot-checked by a human | ~5–15 min per source |

Stages 0–1 are implemented. Stages 2–3 are manual and tracked in the per-entry notes the
README now carries.

## Running Stage 0–1

```
python3 verify.py                     # check every URL in sources.json
python3 verify.py --only escribe fir  # just these source ids
python3 verify.py --stale 30          # skip URLs that passed within the last 30 days
python3 verify.py --jobs 8 --delay 2  # 8 domains in parallel, 2s between same-domain hits
python3 build_readme.py               # fold the results into README.md
```

Output is [`verification.json`](verification.json) — checked into the repo as the record.
It is machine-written; do not hand-edit it. Stdlib only, no dependencies.

The harness is polite: requests are serialised per domain with a delay + jitter, it identifies
itself with a descriptive User-Agent, and it retries once on a transient failure. It does **not**
enumerate search indexes or walk `DocumentId` ranges — that is a Stage 2+ decision to make
per source, with the site's terms in view.

### What the outcomes mean

| Outcome | Meaning | What's left |
| --- | --- | --- |
| `machine-readable` | A probe confirmed an API / catalogue feed / GTFS zip. | Confirm the specific layers/datasets and the licence (Stage 3). |
| `pdf` | The URL serves a PDF. | Confirm whether tables are extractable (Stage 3). |
| `reachable_html` | Loads as server-rendered HTML with real content. | The access tag and licence are still unverified (Stage 3). |
| `needs_browser` | Loads, but the body is a JavaScript shell with no content. | Stage 2 — open it in a real browser, capture the XHR. |
| `error` | HTTP 4xx/5xx. | Find the moved URL or drop the entry. |
| `dead` | No DNS / no connection. | Find the moved URL or drop the entry. |

## What Stage 0–1 already found (run 2026-09-01)

- **`open311`** — the catalogued endpoint `city-of-ottawa-prod.apigee.net/open311/v2/` no
  longer resolves, and the docs page 404s. The verify-flag was right; the entry needs a new
  endpoint or a downgrade.
- **`collisions`** — the `open.ottawa.ca/datasets/ottawa::…/about` URL 404s. The `ottawa::`
  slug format is stale across several Open Ottawa links; the current form is `/datasets/<id>`.
- **`ottawa-civic-tech`** — `ottawacivictech.ca` does not resolve (the GitHub org link is fine).
- **`school-boards`** — `ecolecatholique.ca` (CECCE) does not resolve for the harness; confirm
  the board's current domain.
- **15 sources** have a confirmed machine-readable surface, including the two open-data portals
  (ArcGIS Hub DCAT feeds), the city ArcGIS REST root (80 services), the Ottawa Police Hub
  (98 datasets), `data.ontario.ca` (CKAN, ~3,000 datasets), and the Riverkeeper Hub.
- **~10 sources** are JavaScript-rendered and need a browser pass: `geoottawa`, `devapps`,
  `bylaws-az`, `committee-of-adjustment` (the city side), `horizon-vote-tracker`, `howtheyvoted`,
  `ottawa-lookout`, `ateh`, `legacy-agendas`, `historical-imagery`.

## Cost, in short

Money: ~zero. Every target is public. The only pay-per-hit surface in the wider hierarchy is
the Ontario land registry (Teranet / OnLand); confirming that it is paywalled needs no purchase.
Optional spend is an LLM for Stage 3 triage (cents per URL) and a hosted headless browser if you
don't run Playwright locally.

Time: Stage 0–1 is minutes. A full Stage 2–3 pass over the 72 catalogued sources is roughly
1–2 focused days; extending it to the [`hierarchy.md`](hierarchy.md) branches is another 2–3.

## Tools that would make this faster / more accurate / more comprehensive

- **Playwright / Playwright MCP** — the single biggest accuracy unlock; without a real browser
  most `*.ottawa.ca` app subdomains cannot be verified at all.
- **Subagents** — fan the catalogue out to several agents, each taking a slice through Stages 1–3.
- **ArcGIS Hub `/data.json` + CKAN `/api/3/action/package_search`** — one call each enumerates a
  whole portal, turning verification into discovery (datasets the hand-built list missed).
- **`gtfs-validator`, Open311 `/discovery.json`, `transitland` API** — authoritative format checks.
- **`pdfplumber` / `pymupdf`** — confirm "PDF-only" and whether the tables are extractable.
- **archive.org Save Page Now** — snapshot every URL at verification time so evidence doesn't rot.
- **A scheduled CI job** (weekly `verify.py --stale 7`) — catches link rot and opens a PR on change.
- **OttWatch and Ottawa Civic Tech** — have already verified a large slice; ask before re-walking it.

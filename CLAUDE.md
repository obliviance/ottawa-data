# CLAUDE.md

Guidance for an agent working in this repository.

## What this is

A catalogue of **public data and information sources for the governance of Ottawa, Ontario** —
electoral, legislative, financial, spatial, operational. It is a reference, not an application:
no build, no server, no dependencies for the core artifact.

## The data model

```
sources.json   ── source of truth: 72 entries, each {id, name, category, operator,
   │                urls[], access[], description, verify, verify_note?}
   ▼
tools/build_readme.py   ── regenerates README.md from sources.json + the verification/ files
   ▼
README.md      ── generated; DO NOT hand-edit (your changes will be overwritten)
```

**To change a catalogued source: edit `sources.json`, then run `python3 tools/build_readme.py`.**
Commit `sources.json` and `README.md` together.

`hierarchy.md` is a **hand-written** companion: the full institutional tree (every body that
produces information about Ottawa governance/community, ~180 leaves), tagged 🟢 open / 🟡 partial
/ 🔴 closed / ⚪ unknown, cross-referenced to `sources.json` ids. It names the branches *not* yet
in the catalogue. Edit it directly.

### `access` vocabulary

`api` (live queryable endpoint) · `bulk` (downloadable CSV/GeoJSON/shapefile/XLS) ·
`html` (web pages / PDFs only) · `request` (FOI, in-person, written). A source can carry several.

## Layout

```
sources.json          source of truth (the catalogue)
hierarchy.md          hand-written institutional tree
README.md             generated
ROADMAP.md            running plan for the exploration work — keep it current
CLAUDE.md             this file
tools/
  build_readme.py     sources.json (+ verification/) -> README.md
  verify.py           stage 0-1: liveness + machine-readable fingerprint
  verify_stage2.py    stage 2: headless-browser render + XHR capture (needs a Chromium over CDP)
  verify_stage3.py    stage 3: access-tag + licence confirmation (heuristic)
  snapshot.py         Wayback Machine snapshot per URL
  VERIFYING.md        the verification method, in full — read before touching verify*.py
  warehouse.py        DuckDB + Parquet store: register() / con() / CLI
  profile.py          dataset -> catalog/<id>.md tearsheet + questions/backlog.csv rows
  ingest/             one ingester per source SHAPE (arcgis_hub.py, ckan.py, …)
  _http.py            shared polite fetch helpers
  requirements.txt
verification/         machine-written records — DO NOT hand-edit
  verification*.json · snapshots.json
warehouse/            DuckDB + Parquet — GITIGNORED except manifest.json (rebuild via ingesters)
catalog/              generated tearsheets, one per warehouse dataset
questions/backlog.csv the running investigation list
spine/                geography / timeline / entities reference tables (build first)
releases/  apps/  explorations/   published datasets · visualizations · scratch
```

## Running verification

```
python3 tools/verify.py                 # stage 0-1, all URLs (~4 min, polite)
python3 tools/verify.py --stale 7       # only URLs not checked OK in 7 days
python3 tools/verify_stage2.py          # stage 2, the JavaScript/interactive sources
python3 tools/verify_stage3.py          # stage 3
python3 tools/snapshot.py -u --delay 10 # Wayback (slow; archive.org rate-limits)
python3 tools/build_readme.py           # fold everything into README.md
```

Stage 2 connects to a headless Chromium at `$CHROMIUM_CDP_URL` (default `http://chromium:9222`).
If that isn't set, stage 2 is skipped — the other stages and `build_readme.py` still work.

## Exploration workflow (see ROADMAP.md)

```
pip install -r tools/requirements.txt
python3 tools/warehouse.py init
python3 tools/ingest/arcgis_hub.py --limit 20        # land data (one ingester per shape)
python3 tools/ingest/ckan.py --query "ottawa" --limit 10
python3 tools/profile.py --all                       # tearsheets + backlog questions
python3 tools/warehouse.py query "SELECT ..."        # ad-hoc SQL; datasets are views d_<id>
```

Two phases: **A** recon sweep (ingest + profile every source, ship cleaned data to
`releases/`), then **B** deep builds on the top `questions/backlog.csv` rows. Build the
`spine/` tables first. **Update `ROADMAP.md`** (status boxes + Log) whenever work moves.

**Long runs:** always background them (`run_in_background`) and watch the log; the scripts flush
output and write their JSON incrementally. Do not `pgrep -f verify` — it matches your own shell.

## Conventions

- Commits authored as `claude <noreply@anthropic.com>`; feature branches, not direct-to-main.
- `sources.json` house style: string arrays inline (`["a", "b"]`), 2-space indent. `build_readme.py`
  doesn't care, but keep diffs reviewable.
- Verification JSON is regenerated, not edited. If a run looks wrong, fix the script and re-run.
- When verification corrects a source, edit `sources.json` (tag + a "Verified: …" note in the
  description), clear the `verify` flag if resolved, and update the matching row in `hierarchy.md`.
- CC0 for the catalogue itself; sources carry their own licences (see `verification_stage3.json`).

## Current state (2026-09-09)

Stages 0-3 have run on all 72 catalogued sources. **55** access tags confirmed, **2** understated,
**15** unconfirmed (need an API key / login / are genuine FOI). Notable corrections already folded
in: `howtheyvoted` and `devapps` have JSON APIs; `engage-ottawa` runs on an EngagementHQ API;
`open311`'s GeoReport endpoint is dead (data is now rolling CSVs on Azure Blob); `escribe` exposes
a meeting-index endpoint.

**Still unverified:** `procurement`, `hydro-ottawa`, `conservation-authorities`, `school-boards`,
and every uncatalogued branch in `hierarchy.md` (see its "Verification priorities"). `hierarchy.md`
also lists high-value sources not yet in `sources.json` (Ottawa Community Housing, BIAs, CMHC,
Elections Ontario/Canada, …).

# spine/

The reference tables everything else joins to. Build these **first** — most
non-obvious findings come from connecting a source to a backbone nobody else
connected it to. Each is produced by a script here that lands a `shape="spine"`
dataset in the warehouse.

## 1. `geography` — the spatial backbone

Ward boundaries (24 + mayor), ONS neighbourhoods, census dissemination areas, with
a crosswalk between them and a lookup from address / point → all three. Every
point or address dataset joins here.

Sources: `election-results-history` (ward geometry on Open Ottawa), the Ottawa
Neighbourhood Study (`ons`), StatCan DA boundaries.

## 2. `timeline` — the decision backbone

One row per Council / committee / board agenda item: date, body, item type
(motion, report, by-law, planning application, appointment), title, disposition,
and — where recoverable — the recorded vote. Built from `escribe` (meeting index
via `MeetingsCalendarView.aspx/GetCalendarMeetings`, then the item PDFs) and
`howtheyvoted` (JSON at `/data/ottawa/*.json`).

Everything "what happened / what did they decide" hangs off this.

## 3. `entities` — the actor backbone

One row per distinct organisation or person appearing across the accountability
datasets, with a fuzzy-matched canonical id linking their appearances in:
lobbyist registry · campaign contributions · development applications · contract
awards · board & committee memberships · the salary disclosure.

This is the hard one and the highest-value one — it's what turns "who lobbied on
this file" into "…and here's how the councillors they lobbied then voted, and the
contract that followed."

## Status

None built yet. See `../ROADMAP.md`.

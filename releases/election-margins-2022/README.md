# Ottawa 2022 municipal election — margins by race

25 races (Mayor + 24 wards), from the city's own poll-by-poll Statement of Votes
Cast. Source: Open Ottawa (`election-results-history`), OGL – City of Ottawa. Every
candidate's vote total here is cross-checked against the sum of their own poll-level
results in the same file and matches exactly.

## Findings

- **0 acclaimed** (one candidate, no vote): none.
- **Closest contested races** (margin as % of valid votes cast):
  - Councillor ward 20 (Osgoode): George Darouze beat Doug Thompson by 238 votes (2.23%)
  - Councillor ward 5 (West Carleton-March): Clarke Kelly beat Sasha Duguay by 242 votes (2.6%)
  - Councillor ward 12 (Rideau-Vanier): Stéphanie Plante beat Laura Shantz by 323 votes (2.6%)
  - Councillor ward 3 (Barrhaven West): David Hill beat Taayo Simmonds by 1,493 votes (10.54%)
  - Councillor ward 23 (Kanata South): Allan Hubley beat Erin Coffin by 1,723 votes (10.94%)
- **Widest contested margins:**
  - Councillor ward 13 (Rideau-Rockcliffe): Rawlson King beat Clayton Fitzsimmons by 72.05%
  - Councillor ward 7 (Bay): Theresa Kavanagh beat Robert Hill by 71.71%
  - Councillor ward 11 (Beacon Hill-Cyrville): Tim Tierney beat Miranda Gray by 68.35%
  - Councillor ward 17 (Capital): Shawn Menard beat Rebecca Bromwich by 65.03%
  - Councillor ward 4 (Kanata North): Cathy Curry beat Viorel Copil by 63.38%
- **Turnout range:** Rideau-Vanier lowest at 37.18%,
  Kitchissippi highest at 52.98%.

## Caveats

- **Mayor and ward races are not directly comparable on turnout**: `registered_voters`
  for Mayor is the whole city; a ward's is that ward's own list, so the two `turnout_pct`
  figures answer the same question at different scopes, not a ranking across all 25 rows.
- **Margin % denominator is valid candidate votes, not `times_cast`.** `times_cast`
  includes declined and (for the tallying process) spoiled ballots, which is the right
  figure for turnout but would understate a margin computed against candidates alone.
- School-board trustee races are not included — see `tools/ingest/election_results.py`'s
  module docstring for why (no ward crosswalk exists for the trustee zones yet).
- This is 2022 only. Whether a close 2022 race stays close in 2026 depends on who is
  actually running again — join to `d_election_candidates` (2026 roster) for that, not
  assumed here.

Full detail: `race_margins.csv`.

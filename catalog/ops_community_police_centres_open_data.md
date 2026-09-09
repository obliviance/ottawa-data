# Community Police Centres Open Data

`ops_community_police_centres_open_data` · shape **arcgis-hub** · source `ops-data-portal`

- origin: <https://data.ottawapolice.ca/datasets/738d0ea71cd6497d9ebac44a604e8d76_0>
- fetched 2026-09-09 · **8 rows** · 7 columns
- csv · licence: https://data.ottawapolice.ca/pages/about#termsofuse

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `FID` | num | 100% | 8 | 1.00 · p25 2.75 · p50 4.50 · p95 7.65 · max 8.00  █▁█▁█▁█▁▁█▁█▁█▁█ |
| `Name` | cat | 100% | 8 | Kanata/Stittsville - CPC 12%, Manotick - CPC 12%, Greely - CPC 12%, West Carleton - CPC 12%, Wellington - CPC 12%, Vanier - CPC 12% |
| `Address` | cat | 100% | 8 | 211 Huntmar Dr. 12%, 5669 Manotick Main Stree 12%, 1448 Meadow Dr. 12%, 5670 Carp Rd. 12%, 1064 Wellington St. 12%, 252 McArthur Rd. 12% |
| `Division` | cat | 100% | 3 | West 50%, Central 25%, East 25% |
| `Google Maps Navigation To` | cat | 100% | 8 | https://maps.app.goo.gl/ 12%, https://maps.app.goo.gl/ 12%, https://maps.app.goo.gl/ 12%, https://maps.app.goo.gl/ 12%, https://maps.app.goo.gl/ 12%, https://maps.app.goo.gl/ 12% |
| `x` | num | 100% | 8 | -8,476,643 · p25 -8,435,219 · p50 -8,423,117 · p95 -8,406,890 · max -8,404,668  █▁▁▁▁█▁▁▁▁██████ |
| `y` | num | 100% | 8 | 5,656,170 · p25 5,666,563 · p50 5,686,219 · p95 5,695,114 · max 5,698,090  ▄▁▄▁▄▁▁▁▁▁▁██▁▁▄ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py ops_community_police_centres_open_data`_

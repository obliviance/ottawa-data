# Pathway Links

`open_pathway_links` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::pathway-links-1>
- fetched 2026-09-09 · **609 rows** · 14 columns
- geojson · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 609 | 1.00 · p25 153 · p50 305 · p95 579 · max 609  █▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ |
| `PARK_ID` | num | 80% | 492 | 1,569 · p25 1,881 · p50 2,044 · p95 2,370 · max 2,449  ▁▁▁▇▇█▆▇▅▇▆▆▆▇▃▃ |
| `FACILITYID` | num | 100% | 573 | 34,947 · p25 35,086 · p50 35,215 · p95 51,600 · max 59,019  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `NAME` | cat | 100% | 2 | Pathway Link 100%, Luigi Caparelli Walkway 0% |
| `NAME_FR` | cat | 100% | 2 | Sentier de liaison 100%, Passerelle Luigi Caparel 0% |
| `ADDRESS` | id/text | 100% | 607 | e.g. 50 GRENRILL PL Kanata, 52 GLEN MEADOWS CIRC K, 36 PERIGRINE CRES Kana |
| `ADDRESS_FR` | id/text | 100% | 607 | e.g. 50, PLACE GRENRILL, Ka, 52, CERCLE GLEN MEADOW, 36, CROISSANT PERIGRIN |
| `ACCESSIBLE` | text | 0% | 0 | e.g.  |
| `OPEN` | text | 0% | 0 | e.g.  |
| `MODIFIED_DATE` | date | 100% | 100 | 2016-02-05 → 2023-06-07, 15 gaps >30d |
| `CREATED_DATE` | date | 19% | 102 | 2015-04-10 → 2023-06-07, 18 gaps >30d |
| `Shape_Length` | num | 100% | 609 | 44.92 · p25 120 · p50 182 · p95 580 · max 2,123  █▆▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Shape_Area` | num | 100% | 609 | 38.66 · p25 211 · p50 346 · p95 1,926 · max 9,615  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `geometry` | id/text | 100% | 609 | e.g. {"type": "Polygon", "c, {"type": "Polygon", "c, {"type": "Polygon", "c |

## Candidate questions

- Trend / seasonality of open_pathway_links over `MODIFIED_DATE`; structural breaks?
- Spatial clustering of open_pathway_links; overlay wards + the decision timeline
- Concentration in `NAME` — which actors dominate? (join entity spine)

_profiled 2026-09-09 · `python3 tools/profile.py open_pathway_links`_

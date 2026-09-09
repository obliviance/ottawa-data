# Community Design Plan Boundaries

`open_community_design_plan_boundaries` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::community-design-plan-boundaries>
- fetched 2026-09-09 · **40 rows** · 24 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 40 | 387 · p25 399 · p50 410 · p95 1,037 · max 1,042  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `NUMBERONMA` | num | 85% | 34 | 1.00 · p25 10.00 · p50 18.00 · p95 32.40 · max 34.00  ▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅█ |
| `NAME_EN` | id/text | 100% | 40 | e.g. Cyrville TOD, Escarpment Area Distri, Richmond Road / Westbo |
| `NAME_FR` | id/text | 100% | 40 | e.g. Cyrville AATC, District de la zone de, Du chemin Richmond / W |
| `STATUS_EN` | cat | 100% | 1 | Completed Plan 100% |
| `STATUS_FR` | cat | 100% | 1 | Plan achevé 100% |
| `SHAPE_Length` | num | 100% | 40 | 2,945 · p25 7,889 · p50 9,547 · p95 23,341 · max 34,007  ▄▄█▇▂▂▁▂▃▂▁▁▁▁▁▁ |
| `SHAPE_Area` | num | 100% | 40 | 223,206 · p25 1,829,215 · p50 3,396,561 · p95 17,187,930 · max 51,185,069  █▄▁▁▂▁▁▁▁▁▁▁▁▁▁▁ |
| `ANNEX_FR` | cat | 100% | 1 | Plan achevé 100% |
| `SECONDARYPLAN_LINK_FR` | cat | 100% | 19 | N/A 38%, https://documents.ottawa 12%, https://documents.ottawa 8%, https://documents.ottawa 5%, https://documents.ottawa 2%, https://documents.ottawa 2% |
| `LINK_EN` | id/text | 100% | 35 | e.g. https://documents.otta, https://ottawa.ca/en/p, https://ottawa.ca/en/p |
| `PLAN_UPDATE_EN` | cat | 97% | 1 | N/A 100% |
| `LINK_FR` | id/text | 100% | 35 | e.g. https://documents.otta, https://ottawa.ca/fr/u, https://ottawa.ca/fr/u |
| `PLAN_UPDATE_FR` | cat | 97% | 1 | N/A 100% |
| `DOCUMENT` | cat | 97% | 2 | Annex 5 85%, Annex 7 15% |
| `DATE_APPROVED` | date | 95% | 30 | 2003-03-26 → 2021-02-24, 25 gaps >30d |
| `DOCUMENT_TITLE_EN` | id/text | 100% | 40 | e.g. Transit-Oriented Devel, Escarpment Area Distri, Richmond Road/Westboro |
| `ZONE` | cat | 97% | 2 | Urban 85%, Rural 15% |
| `ANNEX_EN` | cat | 100% | 1 | Completed Plan 100% |
| `ALL_PLANS` | text | 0% | 0 | e.g.  |
| `SECONDARYPLAN_LINK_EN` | cat | 100% | 19 | N/A 38%, https://documents.ottawa 12%, https://documents.ottawa 8%, https://documents.ottawa 5%, https://documents.ottawa 2%, https://documents.ottawa 2% |
| `DOCUMENT_TITLE_FR` | id/text | 100% | 40 | e.g. Plans d’aménagement ax, Plan de district de la, Plan de conception com |
| `GLOBALID` | id/text | 100% | 40 | e.g. {ABAC15B2-8039-4027-91, {FA47D8D8-EC4E-4A02-B6, {0E7D9F41-A9DD-4411-92 |
| `geometry` | id/text | 100% | 40 | e.g. {"type": "Polygon", "c, {"type": "Polygon", "c, {"type": "Polygon", "c |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_community_design_plan_boundaries`_

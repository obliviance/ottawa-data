# Enteric Outbreaks

`open_enteric_outbreaks` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::enteric-outbreaks>
- fetched 2026-09-09 · **37 rows** · 10 columns
- csv · licence: https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Week_Number` | num | 100% | 37 | 1.00 · p25 10.00 · p50 35.00 · p95 51.20 · max 53.00  █▆▆█▆▂▁▁▁▁▄█▆▆▆█ |
| `Start_of_the_Week` | id/text | 100% | 37 | e.g. 2026/03/08, 2026/03/15, 2026/04/05 |
| `Number_of_Enteric_Outbreaks_in_Schools__Camps__and_Licensed_Child_Care` | num | 100% | 10 | 0.00 · p25 1.00 · p50 2.00 · p95 8.80 · max 17.00  █▅▄▁▃▂▁▂▁▁▁▁▁▁▁▁ |
| `Number_of_Enteric_Outbreaks_in_Healthcare_Institutions` | num | 100% | 6 | 0.00 · p25 0.00 · p50 1.00 · p95 4.80 · max 8.00  ▆█▁▂▁▅▁▂▁▁▁▁▁▁▁▂ |
| `Number_of_Enteric_Outbreaks_in_Congregate_Care` | num | 100% | 2 | 0.00 · p25 0.00 · p50 0.00 · p95 0.20 · max 1.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Previous_3_Season_Average_of_Enteric_Outbreaks_in_Schools__Camps__and_Child_Care` | num | 100% | 18 | 0.00 · p25 1.70 · p50 2.70 · p95 5.82 · max 7.70  ▄▅▃▃█▄▆▃▆▃▁▂▁▂▁▂ |
| `Previous_3_Season_Average_of_Enteric_Outbreaks_in_Healthcare_Institutions` | num | 100% | 11 | 0.00 · p25 0.30 · p50 0.70 · p95 3.76 · max 4.00  ▇█▄▁▁▂▂▃▁▃▃▁▁▁▂▂ |
| `Previous_3_Season_Average_of_Enteric_Outbreaks_in_Congregate_Care` | num | 100% | 3 | 0.00 · p25 0.00 · p50 0.00 · p95 0.30 · max 0.70  █▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁ |
| `ObjectId` | text | 0% | 0 | e.g.  |
| `ObjectId2` | num | 100% | 37 | 1.00 · p25 10.00 · p50 19.00 · p95 35.20 · max 37.00  █▅▅█▅▅▅█▅▅▅█▅▅▅█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_enteric_outbreaks`_

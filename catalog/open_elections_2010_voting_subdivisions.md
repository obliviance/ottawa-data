# Elections 2010 Voting Subdivisions

`open_elections_2010_voting_subdivisions` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::elections-2010-voting-subdivisions>
- fetched 2026-09-09 · **1,069 rows** · 7 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `FID` | num | 100% | 1,069 | 1.00 · p25 268 · p50 535 · p95 1,016 · max 1,069  ████▇███▇███▇███ |
| `VOT_SUBD` | id/text | 100% | 1,069 | e.g. 01-009.6, 01-001.3, 01-011.4 |
| `WARD` | num | 100% | 23 | 1.00 · p25 7.00 · p50 12.00 · p95 23.00 · max 23.00  ▇▄▄▂▃█▄▇▃▃▇▃▄▅▂▆ |
| `WARD_EN` | cat | 100% | 23 | COLLEGE 7%, ORLÉANS 6%, KANATA SOUTH 5%, RIDEAU-VANIER 5%, RIVER 5%, GLOUCESTER-SOUTHGATE 5% |
| `WARD_FR` | cat | 100% | 23 | COLLÈGE 7%, ORLÉANS 6%, KANATA-SUD 5%, RIDEAU-VANIER 5%, RIVIÈRE 5%, GLOUCESTER-SOUTHGATE 5% |
| `Shape__Area` | num | 100% | 1,069 | 1,214 · p25 303,418 · p50 501,619 · p95 40,217,632 · max 239,305,582  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `Shape__Length` | num | 100% | 1,069 | 143 · p25 2,637 · p50 3,531 · p95 30,687 · max 65,640  █▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |

## Candidate questions

- `WARD` by `WARD` — equity gradient? (join ONS income)

_profiled 2026-09-09 · `python3 tools/profile.py open_elections_2010_voting_subdivisions`_

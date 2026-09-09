# Sledding Hills

`open_sledding_hills` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::sledding-hills>
- fetched 2026-09-09 · **75 rows** · 23 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `X` | num | 100% | 75 | -8,465,297 · p25 -8,434,720 · p50 -8,424,229 · p95 -8,401,102 · max -8,387,923  ▁▁▂▂▃▅▅▃▆▃▄▂█▃▁▁ |
| `Y` | num | 100% | 75 | 5,642,221 · p25 5,671,569 · p50 5,677,840 · p95 5,697,431 · max 5,702,989  ▁▁▁▁▂▄▆▂█▅▃▃▄█▇▁ |
| `OBJECTID` | num | 100% | 75 | 1.00 · p25 19.50 · p50 38.00 · p95 71.30 · max 75.00  ██▆██▆██▆█▆██▆██ |
| `PARK_ID` | num | 96% | 71 | 2.00 · p25 344 · p50 696 · p95 2,322 · max 2,632  ▅▇█▇▅▅▃▃▁▃▃▂▂▁▁▃ |
| `FACILITYID` | num | 100% | 75 | 34,744 · p25 34,774 · p50 34,803 · p95 59,072 · max 59,085  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▃ |
| `NAME` | cat | 100% | 5 | Sledding Hill 95%, Anne Heggtviet Sledding  1%, Conroy Pit Sledding Hill 1%, Bruce Pit Sledding Hill 1%, Sledding Hill (Ottawa Pu 1% |
| `NAME_FR` | cat | 100% | 6 | Pente de traîneau 93%, Piste de luge Anne Heggt 1%, Pente de traîneau du Sab 1%, Pente de traîneau du Sab 1%, Pente de traîneau (Bibli 1%, Pente de traineau 1% |
| `ADDRESS` | id/text | 100% | 74 | e.g. 937 Clyde Avenue, Otta, 1485 Duford Drive, Cum, 1899 Du Clairvaux Road |
| `ADDRESS_FR` | id/text | 100% | 74 | e.g. 937, avenue Clyde, Ott, 1485, promenade Duford, 1899, chemin Du Clairv |
| `ASSESSMENT` | cat | 100% | 2 | Approved site - Conditio 85%, Approved site 15% |
| `ASSESSMENT_FR` | cat | 100% | 2 | Emplacement approuvé - s 85%, Emplacement approuvé 15% |
| `OBSERVATIONS` | id/text | 100% | 73 | e.g. Very large hill with l, Small local man-made b, Small local man-made h |
| `OBSERVATIONS_FR` | id/text | 100% | 74 | e.g. Très grand monticule e, Petits talus et montic, Petit monticule artifi |
| `PERILS_CONDITIONS_NOTED` | id/text | 85% | 63 | e.g. Caution restricted use, Caution restricted use, Caution restricted use |
| `PERILS_CONDITIONS_NOTED_FR` | id/text | 92% | 64 | e.g. Mise en garde : usage , Mise en garde : usage , Mise en garde : usage  |
| `ACCESSIBLE` | cat | 96% | 1 | no/non 100% |
| `OPEN` | text | 0% | 0 | e.g.  |
| `MODIFIED_DATE` | date | 100% | 75 | 2024-01-24 → 2024-01-24 |
| `CREATED_DATE` | date | 30% | 23 | 2014-12-11 → 2024-01-16, 4 gaps >30d |
| `PARKNAME` | id/text | 93% | 69 | e.g. Carlington Park, Queenswood Heights Cen, Gérald Poulin Park |
| `PARKNAME_FR` | id/text | 93% | 69 | e.g. Parc Carlington, Centre communautaire e, Parc Gérald-Poulin |
| `PARKADDRESS` | id/text | 93% | 69 | e.g. 937 Clyde Avenue, Otta, 1485 Duford Drive, Cum, 1899 Du Clairvaux Road |
| `PARKADDRESS_FR` | id/text | 93% | 69 | e.g. 937, avenue Clyde, Ott, 1485, promenade Duford, 1899, chemin Du Clairv |

## Candidate questions

- Concentration in `NAME` — which actors dominate? (join entity spine)

_profiled 2026-09-09 · `python3 tools/profile.py open_sledding_hills`_

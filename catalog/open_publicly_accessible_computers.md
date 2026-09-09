# Publicly Accessible Computers

`open_publicly_accessible_computers` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::publicly-accessible-computers>
- fetched 2026-09-09 · **87 rows** · 20 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `X` | num | 100% | 83 | -8,483,234 · p25 -8,435,176 · p50 -8,426,974 · p95 -8,406,300 · max -8,400,574  ▁▁▁▁▁▁▃▁▄▄█▇▅▂▂▂ |
| `Y` | num | 100% | 83 | 5,642,475 · p25 5,675,904 · p50 5,681,628 · p95 5,695,661 · max 5,700,439  ▂▂▁▁▂▂▁▃▄▇█▆▆▇▃▂ |
| `OBJECTID` | num | 100% | 87 | 1.00 · p25 22.50 · p50 44.00 · p95 82.70 · max 87.00  █▆█▆▆█▆█▆▆█▆▆█▆█ |
| `SITE_NO` | num | 100% | 87 | 1.00 · p25 22.50 · p50 44.00 · p95 82.70 · max 87.00  █▆█▆▆█▆█▆▆█▆▆█▆█ |
| `WIFI` | cat | 100% | 2 | wifi 51%,   49% |
| `SITENAME_EN` | id/text | 100% | 80 | e.g. Bibliothèque Ottawa Li, Bibliothèque Ottawa Li, Bibliothèque Ottawa Li |
| `ADDRESS_EN` | id/text | 100% | 84 | e.g. 1599 Tenth Line, 1910 St-Laurent, 1547 Merivale |
| `ACCESSHOURS_EN` | text | 100% | 47 | e.g. Mon - Thurs 10-9, Fri , Mon-Thurs 10-8:30, Fri, Mon 5:30-8:30, Tues-We |
| `COMPUTERS` | num | 100% | 23 | 1.00 · p25 2.00 · p50 5.00 · p95 28.30 · max 82.00  █▂▃▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `ACCESSIBLECOMPUTERS` | num | 100% | 3 | 0.00 · p25 0.00 · p50 0.00 · p95 1.00 · max 2.00  █▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁ |
| `ACCESSCRITERIA_EN` | cat | 100% | 7 | Library card or "interne 38%, sign-in 26%, none 21%, sign in 6%, Employment Resource Area 5%, members only 3% |
| `LOCATIONTYPE_EN` | cat | 100% | 7 | C. Ottawa Public Librari 38%, B. City Recreation Centr 23%, D. Employment Ontario Ce 14%, E. Community Houses 8%, G. Community Health and  8%, F. Other Community Acces 5% |
| `LOCATIONTYPE_FR` | cat | 100% | 7 | C. Bibliotheque publique 38%, B. Centres récréatifs, C 23%, D. Centres de ressources 14%, E. Maisons communautaire 8%, G. Centres de ressources 8%, F.Autres points d'access 5% |
| `SITENAME_FR` | id/text | 100% | 80 | e.g. Bibliothèque Ottawa Li, Bibliothèque Ottawa Li, Bibliothèque Ottawa Li |
| `ADDRESS_FR` | id/text | 100% | 87 | e.g. 1599 Tenth Line, 1910 St-Laurent, 1547 Merivale |
| `ACCESSHOURS_FR` | text | 100% | 51 | e.g. lundi - jeudi 10h - 21, lundi-jeudi 10h - 20h , lundi 5:30-8:30, mardi |
| `ACCESSCRITERIA_FR` | cat | 100% | 6 | Carte de bibliothèque ou 38%, avec inscription 32%, aucun 21%, Sections de ressources à 5%, membres seulement 3%, Femmes et enfants 1% |
| `URL_EN` | id/text | 93% | 79 | e.g. https://biblioottawali, https://biblioottawali, https://biblioottawali |
| `URL_FR` | id/text | 100% | 80 | e.g. https://biblioottawali, https://biblioottawali, https://biblioottawali |
| `GLOBALID` | id/text | 100% | 87 | e.g. {EEDBFA25-20AD-4654-A8, {1ECC649B-E6E1-4E77-B8, {140EA763-8779-4EDA-BE |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_publicly_accessible_computers`_

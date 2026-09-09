# Tennis Courts

`open_tennis_courts` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::tennis-courts>
- fetched 2026-09-09 · **132 rows** · 38 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `X` | num | 100% | 132 | -8,464,461 · p25 -8,432,945 · p50 -8,424,834 · p95 -8,400,844 · max -8,387,127  ▁▁▂▂▂▃▃▆█▇▂▃▂▂▁▁ |
| `Y` | num | 100% | 132 | 5,642,174 · p25 5,674,331 · p50 5,679,591 · p95 5,696,028 · max 5,702,882  ▁▁▁▁▂▂▂▂▅█▄▄▅▄▃▁ |
| `OBJECTID` | num | 100% | 132 | 1.00 · p25 33.75 · p50 66.50 · p95 125 · max 132  █▇▇▇▇█▇▇▇▇█▇▇▇▇█ |
| `PARK_ID` | num | 90% | 118 | 9.00 · p25 328 · p50 653 · p95 2,507 · max 2,633  █▆█▅▃▅▆▃▁▂▂▁▁▁▁▄ |
| `FACILITYID` | num | 100% | 132 | 3,166 · p25 3,797 · p50 27,028 · p95 52,332 · max 57,567  ▅▁▁▁▁▁▁█▁▃▁▁▁▁▁▁ |
| `COURT_ID` | num | 100% | 96 | 0.00 · p25 10.00 · p50 29.50 · p95 88.45 · max 95.00  █▄▄▃▂▂▂▂▂▂▂▂▂▂▂▂ |
| `PARKNAME` | id/text | 90% | 118 | e.g. Harold Barnhart Park, Steve MacLean Park, Jack Purcell Park |
| `PARKNAME_FR` | id/text | 90% | 118 | e.g. Parc Harold-Barnhart, Parc Steve-MacLean, Parc Jack-Purcell |
| `CLUB` | text | 100% | 42 | e.g. Public Tennis Courts, Long Park Tennis Club, Lindenlea Tennis Club |
| `CLUB_FR` | text | 100% | 42 | e.g. Courts de tennis publi, Club de tennis de Long, Club de tennis de Lind |
| `SURFACE_COLOUR` | cat | 100% | 6 | Green Acrylic 48%, Asphalt 27%, Blue Acrylic 19%, Clay 3%, Clay / Green Acrylic 2%, Clay / Blue Acrylic 1% |
| `ADDRESS` | id/text | 100% | 131 | e.g. 5650 Scobie Crescent, , 1190 Deer Park Road, N, 320 Jack Purcell Lane, |
| `ADDRESS_FR` | id/text | 100% | 131 | e.g. 5650, croissant Scobie, 1190, chemin Deer Park, 320, ruelle Jack-Purce |
| `NO_COURTS` | num | 100% | 14 | 0.00 · p25 2.00 · p50 2.00 · p95 8.00 · max 19.00  ▂█▁▂▁▁▁▁▁▁▁▁▁▁▁▁ |
| `INDOOR_COURT` | num | 100% | 4 | 0.00 · p25 0.00 · p50 0.00 · p95 0.00 · max 8.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `OUTDOOR_COURT` | num | 100% | 12 | 0.00 · p25 2.00 · p50 2.00 · p95 7.45 · max 18.00  ▂█▁▂▁▁▁▁▁▁▁▁▁▁▁▁ |
| `LIGHTS` | cat | 98% | 2 | no/non 51%, yes/oui 49% |
| `CLUBHOUSE` | cat | 99% | 2 | no/non 79%, yes/oui 21% |
| `BENCHES` | cat | 99% | 2 | yes/oui 60%, no/non 40% |
| `FENCE` | cat | 99% | 2 | yes/oui 97%, no/non 3% |
| `PRACTICE_COURT` | cat | 99% | 2 | no/non 93%, yes/oui 7% |
| `BACKWALL` | cat | 99% | 2 | no/non 82%, yes/oui 18% |
| `COURT_TYPE` | cat | 100% | 5 | Public Courts 70%, Membership Clubs 19%, Private Clubs 5%, School Board Sites 5%, Practice Ball Wall 1% |
| `COURT_TYPE_FR` | cat | 100% | 5 | Courts publics 70%, Abonnement des clubs 19%, Clubs privés 5%, Emplacement des conseils 5%, Mur d'entraînement 1% |
| `ACCESSIBLE` | cat | 99% | 2 | no/non 95%, yes/oui 5% |
| `OPEN` | cat | 0% | 1 | no/non 100% |
| `MODIFIED_DATE` | date | 100% | 109 | 2018-01-17 → 2025-06-16, 10 gaps >30d |
| `CREATED_DATE` | date | 12% | 16 | 2014-05-23 → 2022-07-22, 9 gaps >30d |
| `SURFACE_COLOUR_FR` | cat | 99% | 6 | acrylique vert 48%, asphalte 28%, acrylique bleu 18%, argile 3%, argile / acrylique vert 2%, argile / acrylique bleu 1% |
| `PARKADDRESS` | id/text | 90% | 118 | e.g. 5650 Scobie Crescent, , 1190 Deer Park Road, N, 320 Jack Purcell Lane, |
| `PARKADDRESS_FR` | id/text | 90% | 118 | e.g. 5650, croissant Scobie, 1190, chemin Deer Park, 320, ruelle Jack-Purce |
| `LINK` | cat | 0% | 1 | http://www.generalburnst 100% |
| `LINK_FR` | cat | 0% | 1 | http://www.generalburnst 100% |
| `LINK_LABEL` | cat | 0% | 1 | Tennis Club 100% |
| `LINK_LABEL_FR` | cat | 0% | 1 | Club de tennis 100% |
| `LINK_DESCRIPTION` | text | 0% | 0 | e.g.  |
| `LINK_DESCRIPTION_FR` | text | 0% | 0 | e.g.  |
| `PICKLEBALL` | num | 99% | 6 | 0.00 · p25 0.00 · p50 1.00 · p95 2.50 · max 8.00  █▂▁▇▁▁▁▁▁▁▁▁▁▁▁▁ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_tennis_courts`_

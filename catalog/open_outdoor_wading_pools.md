# Outdoor Wading Pools

`open_outdoor_wading_pools` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::outdoor-wading-pools>
- fetched 2026-09-09 · **53 rows** · 41 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `X` | num | 100% | 53 | -8,438,242 · p25 -8,431,212 · p50 -8,424,902 · p95 -8,418,642 · max -8,417,526  ▄▃▁▃▅▅▅▃▄▃██▅▆▃▅ |
| `Y` | num | 100% | 53 | 5,675,873 · p25 5,679,628 · p50 5,683,713 · p95 5,690,499 · max 5,692,880  ▂▆▆▆▃▆▃▆█▅▃▃▄▅▂▂ |
| `OBJECTID` | num | 100% | 53 | 1.00 · p25 14.00 · p50 27.00 · p95 50.40 · max 53.00  █▆▆█▆▆▆█▆▆▆█▆▆▆█ |
| `PARK_ID` | num | 100% | 53 | 7.00 · p25 170 · p50 376 · p95 1,064 · max 1,186  █▆▆▆▆▃▅▂▄▂▅▆▁▄▃▃ |
| `FACILITYID` | num | 100% | 53 | 3,501 · p25 3,517 · p50 3,536 · p95 26,085 · max 26,153  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `NAME` | id/text | 100% | 53 | e.g. Jules Morin / Angelsea, Lions Park Wading Pool, Chaudiere Park Wading  |
| `NAME_FR` | id/text | 100% | 53 | e.g. Pataugeoire du parc Ju, Pataugeoire du parc Li, Pataugeoire du parc Ch |
| `ADDRESS` | id/text | 100% | 53 | e.g. 400 Clarence St. E., 294 Elmgrove Ave., 68 Elm St. |
| `ADDRESS_FR` | id/text | 100% | 53 | e.g. 400, rue Clarence E., 294, av. Elmgrove, 68, rue Elm |
| `ACCESSIBLE` | cat | 100% | 2 | no/non 83%, yes/oui 17% |
| `OPEN` | cat | 100% | 1 | yes/oui 100% |
| `NOTES` | cat | 100% | 11 | District 2 19%, District 5 19%, District 3 17%, District 1 17%, District 4 11%, Complex / POS Pools 8% |
| `MODIFIED_DATE` | date | 100% | 3 | 2024-06-29 → 2025-06-24, 1 gaps >30d |
| `CREATED_DATE` | text | 0% | 0 | e.g.  |
| `SEASON` | cat | 100% | 11 | June 29 to August 23 28%, June 22 to August 16 23%, June 30 to August 23 9%, June 22 to August 15 8%, June 23 to August 15 8%, June 23 to August 16 8% |
| `SEASON_FR` | cat | 100% | 10 | 29 juin au 23 août 28%, 22 juin au 16 août 23%, 23 juin au 15 août 9%, 30 juin au 23 août 9%, 23 juin au 16 août 8%, 29 juin au 22 août 6% |
| `MONDAY` | cat | 100% | 3 | 11 am to 6 pm 66%, Closed 32%, 10 am to 5 pm 2% |
| `MONDAY_FR` | cat | 100% | 3 | 11 h à 18 h 66%, fermé 32%, 10 h à 17 h 2% |
| `TUESDAY` | cat | 100% | 3 | Noon to 7 pm 87%, Closed 11%, 10 am to 5 pm 2% |
| `TUESDAY_FR` | cat | 100% | 3 | 12 h à 19 h 87%, fermé 11%, 10 h à 17 h 2% |
| `WEDNESDAY` | cat | 100% | 3 | Noon to 7 pm 85%, Closed 13%, 10 am to 5 pm 2% |
| `WEDNESDAY_FR` | cat | 100% | 3 | 12 h à 19 h 85%, fermé 13%, 10 h à 17 h 2% |
| `THURSDAY` | cat | 100% | 3 | Noon to 7 pm 85%, Closed 13%, 10 am to 5 pm 2% |
| `THURSDAY_FR` | cat | 100% | 3 | 12 h à 19 h 85%, fermé 13%, 10 h à 17 h 2% |
| `FRIDAY` | cat | 100% | 3 | 11 am to 6 pm 91%, Closed 8%, 10 am to 5 pm 2% |
| `FRIDAY_FR` | cat | 100% | 3 | 11 h à 18 h 91%, fermé 8%, 10 h à 17 h 2% |
| `SATURDAY` | cat | 100% | 2 | Noon to 5 pm 89%, Closed 11% |
| `SATURDAY_FR` | cat | 100% | 2 | 12 h à 17 h 89%, fermé 11% |
| `SUNDAY` | cat | 100% | 2 | Noon to 5 pm 68%, Closed 32% |
| `SUNDAY_FR` | cat | 100% | 2 | 12 h à 17 h 68%, fermé 32% |
| `LINK` | cat | 100% | 1 | https://ottawa.ca/en/res 100% |
| `LINK_FR` | cat | 100% | 1 | https://ottawa.ca/fr/res 100% |
| `LINK_LABEL` | cat | 100% | 1 | Wading Pools 100% |
| `LINK_LABEL_FR` | cat | 100% | 1 | Pataugeoires 100% |
| `LINK_DESCRIPTION` | text | 0% | 0 | e.g.  |
| `LINK_DESCRIPTION_FR` | text | 0% | 0 | e.g.  |
| `PARKNAME` | id/text | 100% | 53 | e.g. Jules Morin Park, Lion's Park, Chaudière Park |
| `PARKNAME_FR` | id/text | 100% | 53 | e.g. Parc Jules-Morin, Parc Lion's, Parc Chaudière |
| `PARKADDRESS` | id/text | 100% | 53 | e.g. 400 Clarence Street Ea, 294 Elmgrove Avenue, O, 68 Elm Street, Ottawa |
| `PARKADDRESS_FR` | id/text | 100% | 53 | e.g. 400, rue Clarence Est,, 294, avenue Elmgrove, , 68, rue Elm, Ottawa |
| `DOGS_DAYS_TIMES` | text | 0% | 0 | e.g.  |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_outdoor_wading_pools`_

# Public Washrooms

`open_public_washrooms` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::public-washrooms>
- fetched 2026-09-09 · **177 rows** · 50 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `X` | num | 100% | 177 | -8,483,242 · p25 -8,437,232 · p50 -8,425,976 · p95 -8,401,019 · max -8,386,502  ▁▁▁▁▁▃▁▃▅█▄▂▂▃▁▁ |
| `Y` | num | 100% | 177 | 5,642,457 · p25 5,670,682 · p50 5,680,464 · p95 5,700,421 · max 5,703,216  ▂▂▁▁▂▄▃▂▄██▆▅▂▂▃ |
| `OBJECTID` | num | 100% | 177 | 1.00 · p25 45.00 · p50 89.00 · p95 168 · max 177  █▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ |
| `NAME` | id/text | 100% | 162 | e.g. Carlington Park, Walter Upton-Collins P, Lynda Lane Park |
| `NAME_FR` | id/text | 97% | 159 | e.g. Parc Carlington, Parc Walter-Upton-Coll, Parc Lynda-Lane |
| `FACILITY_GROUP_NAME` | cat | 69% | 6 | RECREATION 59%, ARTS AND CULTURE 28%, CIVIC ADMINISTRATION 8%, PROTECTIVE SERVICES 2%, GENERAL PURPOSE 1%, SOCIAL SERVICES 1% |
| `FACILITY_GROUP_NAME_FR` | cat | 69% | 6 | INSTALLATIONS DE LOISIRS 59%, ARTS ET CULTURE
ARTS ET  28%, ADMINISTRATION MUNICIPAL 8%, SERVICES DE PROTECTION 2%, USAGES MULTIPLES 1%, SERVICES SOCIAUX 1% |
| `ADDRESS` | id/text | 100% | 156 | e.g. 937 Clyde Ave, 894 River Road, Glouce, 580 Smyth Rd. |
| `ADDRESS_FR` | id/text | 99% | 157 | e.g. 937 av. Clyde, 894, chemin River, Glo, 580, ch. Smyth |
| `SEASONAL` | num | 100% | 2 | 0.00 · p25 0.00 · p50 0.00 · p95 1.00 · max 1.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅ |
| `SEASON_START` | cat | 38% | 5 | MAY 74%, APR 16%, JUN 4%, SEP 4%, OCT 1% |
| `SEASON_END` | cat | 38% | 6 | OCT 46%, SEP 30%, AUG 14%, JUN 6%, JUL 1%, MAR 1% |
| `HOURS_SUNDAY_OPEN` | cat | 96% | 15 | 05:00 32%, Closed 23%, 09:00 11%, 08:00 9%, 07:00 6%, 13:00 4% |
| `HOURS_SUNDAY_CLOSED` | cat | 96% | 24 | 23:00 35%, Closed 23%, 17:00 8%, 16:00 5%, 19:00 4%, 20:00 4% |
| `HOURS_SUNDAY_SPECIAL` | cat | 15% | 24 | Closed early June to ear 18%, closed July, August & ho 4%, April-Sept only open whe 4%, Summer Open 11:00 AM to  4%, 8 am to 8 pm on Statutor 4%, Closed 4% |
| `HOURS_MONDAY_OPEN` | cat | 98% | 18 | 05:00 31%, 09:00 13%, 10:00 11%, 08:00 9%, 06:00 6%, 08:30 6% |
| `HOURS_TUESDAY_OPEN` | cat | 98% | 17 | 05:00 32%, 09:00 13%, 10:00 12%, 08:00 9%, 07:00 6%, 06:00 6% |
| `HOURS_TUESDAY_CLOSED` | cat | 98% | 17 | 23:00 36%, 21:00 15%, 20:30 14%, 22:00 9%, 16:30 4%, 17:00 3% |
| `HOURS_TUESDAY_SPECIAL` | id/text | 15% | 26 | e.g. closed holidays, April-Sept only open w, 2:30 PM-5:30 PM, 6:30  |
| `HOURS_WEDNESDAY_OPEN` | cat | 98% | 18 | 05:00 32%, 09:00 14%, 10:00 13%, 08:00 9%, 06:00 6%, 08:30 6% |
| `HOURS_WEDNESDAY_CLOSED` | cat | 98% | 17 | 23:00 36%, 21:00 15%, 20:30 13%, 22:00 9%, 17:00 6%, xxxx 3% |
| `HOURS_WEDNESDAY_SPECIAL` | id/text | 16% | 28 | e.g. closed holidays, April-Sept only open w, 2:30 PM-5:30 PM, 6:30  |
| `HOURS_THURSDAY_OPEN` | cat | 99% | 20 | 05:00 31%, 09:00 13%, 10:00 11%, 08:00 9%, 07:00 6%, 06:00 6% |
| `HOURS_THURSDAY_CLOSED` | cat | 99% | 15 | 23:00 36%, 21:00 15%, 20:30 14%, 22:00 9%, 17:00 5%, 16:30 4% |
| `HOURS_THURSDAY_SPECIAL` | id/text | 15% | 27 | e.g. closed holidays, April-Sept only open w, 2:30 PM-5:30 PM, 6:30  |
| `HOURS_FRIDAY_OPEN` | cat | 98% | 19 | 05:00 32%, 09:00 14%, 13:00 10%, 08:00 9%, 06:00 6%, 07:00 6% |
| `HOURS_FRIDAY_CLOSED` | cat | 98% | 18 | 23:00 35%, 18:00 13%, 21:00 13%, 22:00 8%, 17:00 7%, Closed 4% |
| `HOURS_FRIDAY_SPECIAL` | cat | 13% | 23 | 8:00-4:00 Jun-Aug 8%, close at 6:00 pm July &  4%, April-Sept only open whe 4%, closed last 2 weeks in D 4%, Summer Open 9:00 AM to 9 4%, 8 am to 8 pm on Statutor 4% |
| `HOURS_SATURDAY_OPEN` | cat | 98% | 14 | 05:00 32%, 10:00 19%, 09:00 13%, 08:00 10%, Closed 9%, 07:00 5% |
| `HOURS_SATURDAY_CLOSED` | cat | 98% | 25 | 23:00 34%, 17:00 18%, Closed 9%, 14:00 5%, 16:00 5%, 20:00 3% |
| `HOURS_SATURDAY_SPECIAL` | cat | 13% | 24 | closed for holidays 4%, April-Sept only open whe 4%, Summer Open 11:00 AM to  4%, 8 am to 8 pm on Statutor 4%, closed 4%, Times may vary for speci 4% |
| `STAT_HOLIDAY_AVAILABILITY` | num | 88% | 2 | 0.00 · p25 0.00 · p50 0.00 · p95 1.00 · max 1.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▆ |
| `CHANGE_STATION_CHILD` | num | 98% | 2 | 0.00 · p25 0.00 · p50 1.00 · p95 1.00 · max 1.00  ▇▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |
| `CHANGE_STATION_ADULT` | num | 93% | 2 | 0.00 · p25 0.00 · p50 0.00 · p95 1.00 · max 1.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `FAMILY_TOILET` | num | 92% | 2 | 0.00 · p25 0.00 · p50 0.00 · p95 1.00 · max 1.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂ |
| `ACCESSIBILITY` | num | 100% | 4 | 0.00 · p25 0.00 · p50 1.00 · p95 3.00 · max 3.00  ▇▁▁▁▁█▁▁▁▁▅▁▁▁▁▅ |
| `REPORT_TELEPHONE` | num | 100% | 1 | 311 · p25 311 · p50 311 · p95 311 · max 311   |
| `SPECIAL_TOILET_TYPE` | num | 100% | 2 | 0.00 · p25 0.00 · p50 0.00 · p95 1.00 · max 1.00  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▄ |
| `X_COORDINATE` | num | 100% | 171 | -76.21 · p25 -75.79 · p50 -75.69 · p95 -75.47 · max -75.34  ▁▁▁▁▁▃▁▃▅█▄▂▂▃▁▁ |
| `Y_COORDINATE` | num | 100% | 171 | 45.13 · p25 45.31 · p50 45.37 · p95 45.50 · max 45.52  ▂▂▁▁▂▄▃▂▄██▆▅▂▂▃ |
| `JURISDICTION` | cat | 100% | 1 | OTTAWA 100% |
| `HOURS_MONDAY_CLOSED` | cat | 98% | 17 | 23:00 36%, 21:00 15%, 20:30 13%, 22:00 9%, 17:00 3%, xxxx 3% |
| `HOURS_MONDAY_SPECIAL` | id/text | 15% | 26 | e.g. close at 6:00 pm July , April-Sept only open w, 2:30 PM-5:30 PM, 6:30  |
| `HOURS_SUNDAY_SPECIAL_FR` | cat | 15% | 23 | Fermée du début juin au  18%, L'horaire peut varier po 7%, Fermé en juillet, en aoû 4%, D'avril à septembre, ouv 4%, Durant l'été, ouvert de  4%, 8 h à 20 h les jours fér 4% |
| `HOURS_MONDAY_SPECIAL_FR` | cat | 14% | 25 | 8 h à 16 h, de juin à ao 8%, Fermeture à 18 h en juil 4%, D'avril à septembre, ouv 4%, 14 h 30 à 17 h 30, 18 h  4%, Fermé les deux dernières 4%, Durant l'été, ouvert de  4% |
| `HOURS_TUESDAY_SPECIAL_FR` | cat | 14% | 22 | 10 h à 13 h, 17 h 30 à 2 12%, Fermé les jours fériés 8%, 8 h à 16 h, de juin à ao 8%, D'avril à septembre, ouv 4%, 14 h 30 à 17 h 30, 18 h  4%, Fermé les deux dernières 4% |
| `HOURS_WEDNESDAY_SPECIAL_FR` | cat | 15% | 25 | Fermé les jours fériés 7%, 8 h à 16 h, de juin à ao 7%, L'horaire peut varier po 7%, D'avril à septembre, ouv 4%, 14 h 30 à 17 h 30, 18 h  4%, Fermé les deux dernières 4% |
| `HOURS_THURSDAY_SPECIAL_FR` | cat | 15% | 23 | Fermé les jours fériés 7%, 8 h à 16 h, de juin à ao 7%, L'horaire peut varier po 7%, 13 h 30 à 17 h, 18 h à 2 7%, D'avril à septembre, ouv 4%, 14 h 30 à 17 h 30, 18 h  4% |
| `HOURS_FRIDAY_SPECIAL_FR` | cat | 12% | 21 | 8 h à 16 h, de juin à ao 9%, L'horaire peut varier po 9%, Fermeture à 18 h en juil 4%, D'avril à septembre, ouv 4%, Fermé les deux dernières 4%, Durant l'été, ouvert de  4% |
| `HOURS_SATURDAY_SPECIAL_FR` | cat | 12% | 21 | L'horaire peut varier po 9%, Fermé en juillet et en a 9%, Fermé les jours fériés 4%, D'avril à septembre, ouv 4%, Durant l'été, ouvert de  4%, 8 h à 20 h les jours fér 4% |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_public_washrooms`_

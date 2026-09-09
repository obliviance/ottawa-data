# Cultural Spaces Inventory - Venue

`open_cultural_spaces_inventory_venue` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::cultural-spaces-inventory-venue>
- fetched 2026-09-09 · **275 rows** · 49 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `X` | num | 100% | 271 | -8,524,686 · p25 -8,430,012 · p50 -8,426,246 · p95 -8,413,245 · max -8,400,350  ▁▁▁▁▁▁▁▁▁▁▁▂█▂▁▁ |
| `Y` | num | 100% | 271 | 5,635,923 · p25 5,683,105 · p50 5,686,362 · p95 5,693,549 · max 5,722,184  ▁▁▁▁▁▁▁▁▂█▁▁▁▁▁▁ |
| `OBJECTID` | num | 100% | 275 | 15,610 · p25 16,986 · p50 17,517 · p95 19,034 · max 19,125  ▂▁▂▂▂▄█▅▅▁▁▄▄▇▄▆ |
| `UNIQUE_ID` | num | 100% | 275 | 1.00 · p25 290 · p50 590 · p95 1,230 · max 1,420  ▄▁▃█▁▁▇▃▁▃▂▁▅▂▁▂ |
| `CATEGORY` | text | 100% | 42 | e.g. Venue, Learning, Venue, Venue, Food |
| `CATEGORY_FR` | text | 0% | 0 | e.g.  |
| `SUB_CATEGORY` | text | 100% | 87 | e.g. Gallery/Exhibition, Re, Event, Gallery/Exhibition |
| `SUB_CATEGORY_FR` | text | 0% | 0 | e.g.  |
| `TAGS` | text | 100% | 213 | e.g. Visual Art, Crafts, Co, Entrepreneurship, Rent, Visual Art, Contempora |
| `NAME` | id/text | 100% | 275 | e.g. Snow Goose Gallery, CoWorkly - Westboro, Âjagemô |
| `NAME_FR` | id/text | 100% | 275 | e.g. Snow Goose Gallery, CoWorkly - Westboro, Âjagemô |
| `ADDRESS` | id/text | 100% | 250 | e.g. 83 Sparks St, 371A Richmond Rd, 150 Elgin St |
| `ADDRESS_FR` | id/text | 100% | 247 | e.g. 83, rue Sparks, 371A ch Richmond, 150, rue Elgin |
| `LOCATION_NOTES` | cat | 12% | 23 | University of Ottawa 12%, Lansdowne Park 9%, Shenkman Arts Centre 9%, Nepean Sportsplex 6%, Irving Greenberg Theatre 6%, Arts Court 6% |
| `LOCATION_NOTES_FR` | text | 0% | 0 | e.g.  |
| `CITY` | cat | 100% | 10 | Ottawa 96%, Gatineau 1%, Wakefield 0%, Stittsville 0%, Richmond 0%, Burnstown 0% |
| `PROVINCE` | cat | 100% | 2 | ON 98%, QC 2% |
| `POSTAL_CODE` | id/text | 100% | 225 | e.g. K1P 5A5, K2A 0E7, K1P 5V8 |
| `PHONE` | id/text | 52% | 142 | e.g. 613-232-2213, (613) 596-5783, (613) 241-2727 |
| `EMAIL` | id/text | 58% | 154 | e.g. info@snowgoose.ca, info.ASU@canadacouncil, Penelope.Kokkinos@otta |
| `WEBSITE` | id/text | 88% | 235 | e.g. http://www.snowgoose.c, https://www.coworkly.c, http://canadacouncil.c |
| `WEBSITE_FR` | id/text | 49% | 136 | e.g. http://conseildesarts., http://ottawa.ca/fr/re, http://www.nouvellesce |
| `OUTDOOR_COMPONENT` | cat | 100% | 2 | No 91%, Yes 9% |
| `ACTIVE` | cat | 100% | 2 | Yes 89%, No 11% |
| `SEASONAL_CONSTRAINTS` | cat | 0% | 1 | SEPTEMBER 100% |
| `ADDITIONAL_NOTES` | id/text | 12% | 30 | e.g. Kathleen Edwards had b, changed street from Ma, An award-winning sex s |
| `ADDITIONAL_NOTES_FR` | cat | 1% | 4 | Le Centre d’artistes Voi 25%, Le stade TD Place est un 25%, Un centre d'artistes aut 25%, La Foire de Carp célèbre 25% |
| `ADDITIONAL_NOTES_2` | cat | 0% | 1 | The Poets’ Pathway is a  100% |
| `ADDITIONAL_NOTES_2_FR` | text | 0% | 0 | e.g.  |
| `ADDITIONAL_NOTES_3` | text | 0% | 0 | e.g.  |
| `ADDITIONAL_NOTES_3_FR` | text | 0% | 0 | e.g.  |
| `ACCESSIBILITY` | text | 0% | 0 | e.g.  |
| `APT613_LINK` | cat | 4% | 11 | https://apt613.ca/gigspa 9%, https://apt613.ca/tag/da 9%, https://apt613.ca/tag/na 9%, https://apt613.ca/tag/th 9%, https://apt613.ca/studio 9%, https://apt613.ca/eba-26 9% |
| `LATITUDE` | num | 100% | 271 | 4,994,871 · p25 5,028,063 · p50 5,030,333 · p95 5,035,570 · max 5,055,263  ▁▁▁▁▁▁▁▁▂█▂▁▁▁▁▁ |
| `LONGITUDE` | num | 100% | 271 | 298,649 · p25 365,215 · p50 367,849 · p95 376,959 · max 385,990  ▁▁▁▁▁▁▁▁▁▁▁▂█▂▁▁ |
| `COMMUNITY` | cat | 13% | 1 | Yes 100% |
| `VENUE` | cat | 100% | 1 | Yes 100% |
| `LEARNING` | cat | 20% | 1 | Yes 100% |
| `SPORT` | cat | 4% | 1 | Yes 100% |
| `HERITAGE` | cat | 5% | 1 | Yes 100% |
| `FOOD` | cat | 20% | 1 | Yes 100% |
| `STUDIO` | cat | 10% | 1 | Yes 100% |
| `STORE` | cat | 6% | 1 | Yes 100% |
| `NATURE` | cat | 2% | 1 | Yes 100% |
| `PUBLIC_ART` | cat | 0% | 1 | Yes 100% |
| `EXTERNAL` | text | 0% | 0 | e.g.  |
| `CREATED_DATE` | date | 100% | 1 | 2022-12-16 → 2022-12-16 |
| `LAST_EDITED_DATE` | date | 100% | 1 | 2022-12-16 → 2022-12-16 |
| `GLOBALID` | id/text | 100% | 275 | e.g. {C7684B38-0DF7-4D92-B5, {AEA36E52-5DDC-48AB-B9, {3FE5036A-C621-45A2-8F |

## Candidate questions

- `UNIQUE_ID` by `COMMUNITY` — equity gradient? (join ONS income)
- Spatial clustering of open_cultural_spaces_inventory_venue; overlay wards + the decision timeline

_profiled 2026-09-09 · `python3 tools/profile.py open_cultural_spaces_inventory_venue`_

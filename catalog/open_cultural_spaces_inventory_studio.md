# Cultural Spaces Inventory - Studio

`open_cultural_spaces_inventory_studio` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::cultural-spaces-inventory-studio>
- fetched 2026-09-09 · **150 rows** · 49 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `X` | num | 100% | 141 | -8,584,233 · p25 -8,430,965 · p50 -8,427,083 · p95 -8,417,149 · max -8,405,527  ▁▁▁▁▁▁▁▁▁▁▁▁▁▆█▁ |
| `Y` | num | 100% | 141 | 5,648,097 · p25 5,679,993 · p50 5,684,809 · p95 5,692,153 · max 5,697,542  ▁▁▁▁▁▁▁▁▃▃▅▅█▅▁▁ |
| `OBJECTID` | num | 100% | 150 | 15,776 · p25 17,133 · p50 17,442 · p95 19,060 · max 19,119  ▂▁▁▂▁▇█▅▂▁▂▁▆▅▃▇ |
| `UNIQUE_ID` | num | 100% | 150 | 5.00 · p25 609 · p50 720 · p95 789 · max 1,417  ▁▁▁▂▁▁▁▃█▁▁▁▁▁▁▁ |
| `CATEGORY` | cat | 100% | 16 | Studio 75%, Studio, Venue 7%, Venue, Studio 5%, Learning, Studio 3%, Venue, Studio, Learning 1%, Venue, Learning, Studio 1% |
| `CATEGORY_FR` | text | 0% | 0 | e.g.  |
| `SUB_CATEGORY` | text | 100% | 33 | e.g. Performance, Park, Creation, Performance, Creation, |
| `SUB_CATEGORY_FR` | text | 0% | 0 | e.g.  |
| `TAGS` | text | 100% | 93 | e.g. Public Art, Indie, Vis, Architecture, Design, , Broadcasting, Film, Vi |
| `NAME` | id/text | 100% | 150 | e.g. Dunbar Bridge Graffiti, Nevado Artistic Plaste, Skycron |
| `NAME_FR` | id/text | 100% | 150 | e.g. Dunbar Bridge Graffiti, Nevado Artistic Plaste, Skycron |
| `ADDRESS` | id/text | 100% | 140 | e.g. Dunbar Bridge, Bronson, 22 Cleopatra Drive, 16 Capella Court |
| `ADDRESS_FR` | id/text | 100% | 137 | e.g. av Bronson, 22, prom Cleopatra, 16, Capella |
| `LOCATION_NOTES` | cat | 7% | 8 | Shenkman Arts Centre 27%, University of Ottawa 18%, La Nouvelle Scène Gilles 9%, The Gladstone Theatre 9%, Irving Greenberg Theatre 9%, Arts Court 9% |
| `LOCATION_NOTES_FR` | text | 0% | 0 | e.g.  |
| `CITY` | cat | 100% | 4 | Ottawa 98%, Carp 1%, Gatineau 1%, Griffin 1% |
| `PROVINCE` | cat | 100% | 2 | ON 99%, QC 1% |
| `POSTAL_CODE` | id/text | 100% | 133 | e.g. K1S 5T1, K2G 0B3, K2E 7V6 |
| `PHONE` | id/text | 64% | 95 | e.g. 613-228-0743, 613-902-0134, (613) 241-2727 |
| `EMAIL` | id/text | 56% | 83 | e.g. info@nevadoartisticpla, cory@skycron.com, nicolas@nouvellescene. |
| `WEBSITE` | id/text | 88% | 130 | e.g. http://www.nevadoartis, http://skycron.com, http://www.twelfthroot |
| `WEBSITE_FR` | id/text | 20% | 31 | e.g. OUTDOOR, http://skycron.com, http://www.nouvellesce |
| `OUTDOOR_COMPONENT` | cat | 100% | 2 | No 99%, Yes 1% |
| `ACTIVE` | cat | 100% | 2 | Yes 77%, No 23% |
| `SEASONAL_CONSTRAINTS` | text | 0% | 0 | e.g.  |
| `ADDITIONAL_NOTES` | cat | 4% | 7 | The objectives of the Ot 14%, Community radio station  14%, Studio space for rent. 14%, North America's second l 14%, Gallery 101 is a non-pro 14%, A professional artist-ru 14% |
| `ADDITIONAL_NOTES_FR` | cat | 0% | 1 | Un centre d'artistes aut 100% |
| `ADDITIONAL_NOTES_2` | text | 0% | 0 | e.g.  |
| `ADDITIONAL_NOTES_2_FR` | text | 0% | 0 | e.g.  |
| `ADDITIONAL_NOTES_3` | text | 0% | 0 | e.g.  |
| `ADDITIONAL_NOTES_3_FR` | text | 0% | 0 | e.g.  |
| `ACCESSIBILITY` | text | 0% | 0 | e.g.  |
| `APT613_LINK` | cat | 2% | 4 | https://apt613.ca/studio 25%, https://apt613.ca/?s=CHU 25%, https://apt613.ca/ottawa 25%, https://apt613.ca/eba-26 25% |
| `LATITUDE` | num | 100% | 142 | 5,003,360 · p25 5,025,884 · p50 5,029,274 · p95 5,034,448 · max 5,038,356  ▁▁▁▁▁▁▁▁▃▃▅▅█▆▂▁ |
| `LONGITUDE` | num | 100% | 142 | 256,576 · p25 364,598 · p50 367,275 · p95 374,227 · max 382,375  ▁▁▁▁▁▁▁▁▁▁▁▁▁▅█▁ |
| `COMMUNITY` | cat | 1% | 1 | Yes 100% |
| `VENUE` | cat | 20% | 1 | Yes 100% |
| `LEARNING` | cat | 10% | 1 | Yes 100% |
| `SPORT` | cat | 0% | 1 | Yes 100% |
| `HERITAGE` | text | 0% | 0 | e.g.  |
| `FOOD` | cat | 0% | 1 | Yes 100% |
| `STUDIO` | cat | 100% | 1 | Yes 100% |
| `STORE` | cat | 1% | 1 | Yes 100% |
| `NATURE` | text | 0% | 0 | e.g.  |
| `PUBLIC_ART` | cat | 0% | 1 | Yes 100% |
| `EXTERNAL` | text | 0% | 0 | e.g.  |
| `CREATED_DATE` | date | 100% | 1 | 2022-12-16 → 2022-12-16 |
| `LAST_EDITED_DATE` | date | 100% | 1 | 2022-12-16 → 2022-12-16 |
| `GLOBALID` | id/text | 100% | 150 | e.g. {DA0D4CC7-7DC4-4FE5-96, {55172E66-F631-4CD3-B6, {79C986B6-03AB-4496-B8 |

## Candidate questions

- `UNIQUE_ID` by `COMMUNITY` — equity gradient? (join ONS income)

_profiled 2026-09-09 · `python3 tools/profile.py open_cultural_spaces_inventory_studio`_

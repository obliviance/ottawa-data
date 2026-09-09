# Cultural Spaces Inventory - Learning

`open_cultural_spaces_inventory_learning` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::cultural-spaces-inventory-learning>
- fetched 2026-09-09 · **231 rows** · 49 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `X` | num | 100% | 185 | -8,520,554 · p25 -8,429,113 · p50 -8,425,435 · p95 -8,392,515 · max -8,392,511  ▁▁▁▁▁▁▁▁▁▁▁█▃▁▁▃ |
| `Y` | num | 100% | 186 | 5,610,090 · p25 5,681,878 · p50 5,687,423 · p95 5,703,403 · max 5,703,424  ▁▁▁▁▁▁▁▁▁▁▁▂▆█▂▄ |
| `OBJECTID` | num | 100% | 231 | 15,610 · p25 16,737 · p50 17,310 · p95 18,900 · max 19,131  ▂▃▂▃▅▅█▃▅▂▂▄▆▄▄▃ |
| `UNIQUE_ID` | num | 100% | 231 | 9.00 · p25 138 · p50 593 · p95 1,380 · max 1,418  ▂█▁▁▁▁▄▄▁▁▂▁▁▁▁▇ |
| `CATEGORY` | text | 100% | 33 | e.g. Venue, Learning, Learning, Learning, Heritage |
| `CATEGORY_FR` | text | 0% | 0 | e.g.  |
| `SUB_CATEGORY` | text | 100% | 50 | e.g. Gallery/Exhibition, Re, Library, Library, Education |
| `SUB_CATEGORY_FR` | text | 0% | 0 | e.g.  |
| `TAGS` | text | 100% | 124 | e.g. Visual Art, Crafts, Co, Library, Free, Worksho, Library, Free, Local H |
| `NAME` | id/text | 100% | 231 | e.g. Snow Goose Gallery, Ottawa Public Library , Centre de recherche en |
| `NAME_FR` | id/text | 100% | 230 | e.g. Snow Goose Gallery, Bibliothèque publique , Centre de recherche en |
| `ADDRESS` | id/text | 100% | 191 | e.g. 83 Sparks St, 3911 Carp Rd, 65 University Private |
| `ADDRESS_FR` | id/text | 100% | 192 | e.g. 83, rue Sparks, 3911, chemin Carp, 65, University Priv |
| `LOCATION_NOTES` | cat | 23% | 15 | Cumberland Heritage Vill 63%, University of Ottawa 6%, Shenkman Arts Centre 6%, Arts Court 4%, Lansdowne Park 4%, Ottawa City Hall 2% |
| `LOCATION_NOTES_FR` | text | 0% | 0 | e.g.  |
| `CITY` | cat | 100% | 6 | Ottawa 97%, Gatineau 1%, McDonalds Corners 0%, Vernon 0%, Orléans 0%, Kanata 0% |
| `PROVINCE` | cat | 100% | 2 | ON 99%, QC 1% |
| `POSTAL_CODE` | text | 100% | 162 | e.g. K1P 5A5, K0A 1L0, K1N 6N5 |
| `PHONE` | text | 72% | 87 | e.g. 613-232-2213, (613) 580-2940, 613 562-5877 |
| `EMAIL` | text | 52% | 82 | e.g. info@snowgoose.ca, InfoService@BiblioOtta, crccf@uOttawa.ca |
| `WEBSITE` | text | 96% | 171 | e.g. http://www.snowgoose.c, http://biblioottawalib, http://arts.uottawa.ca |
| `WEBSITE_FR` | id/text | 48% | 110 | e.g. http://biblioottawalib, http://arts.uottawa.ca, http://biblioottawalib |
| `OUTDOOR_COMPONENT` | cat | 100% | 2 | No 96%, Yes 4% |
| `ACTIVE` | cat | 100% | 2 | Yes 96%, No 4% |
| `SEASONAL_CONSTRAINTS` | cat | 0% | 1 | Y 100% |
| `ADDITIONAL_NOTES` | cat | 5% | 10 | City of Ottawa community 25%, Converted to apartments 8%, An award-winning sex sho 8%, The objectives of the Ot 8%, moved from Laurier, has  8%, Studio space for rent. 8% |
| `ADDITIONAL_NOTES_FR` | cat | 0% | 2 | Apprécié pour son import 50%, Un centre d'artistes aut 50% |
| `ADDITIONAL_NOTES_2` | cat | 0% | 1 | Extensive network of tra 100% |
| `ADDITIONAL_NOTES_2_FR` | cat | 0% | 1 | Important réseau de sent 100% |
| `ADDITIONAL_NOTES_3` | text | 0% | 0 | e.g.  |
| `ADDITIONAL_NOTES_3_FR` | text | 0% | 0 | e.g.  |
| `ACCESSIBILITY` | text | 0% | 0 | e.g.  |
| `APT613_LINK` | cat | 1% | 4 | https://apt613.ca/ottawa 25%, https://apt613.ca/extrem 25%, https://apt613.ca/oag-op 25%, https://apt613.ca/canadi 25% |
| `LATITUDE` | num | 100% | 187 | 4,976,373 · p25 5,027,219 · p50 5,031,107 · p95 5,042,580 · max 5,042,594  ▁▁▁▁▁▁▁▁▁▁▁▂▇█▂▄ |
| `LONGITUDE` | num | 100% | 187 | 301,529 · p25 365,900 · p50 368,424 · p95 391,422 · max 391,425  ▁▁▁▁▁▁▁▁▁▁▁█▃▁▁▄ |
| `COMMUNITY` | cat | 5% | 1 | Yes 100% |
| `VENUE` | cat | 23% | 1 | Yes 100% |
| `LEARNING` | cat | 100% | 1 | Yes 100% |
| `SPORT` | cat | 2% | 1 | Yes 100% |
| `HERITAGE` | cat | 36% | 1 | Yes 100% |
| `FOOD` | cat | 0% | 1 | Yes 100% |
| `STUDIO` | cat | 6% | 1 | Yes 100% |
| `STORE` | cat | 9% | 1 | Yes 100% |
| `NATURE` | cat | 1% | 1 | Yes 100% |
| `PUBLIC_ART` | text | 0% | 0 | e.g.  |
| `EXTERNAL` | text | 0% | 0 | e.g.  |
| `CREATED_DATE` | date | 100% | 1 | 2022-12-16 → 2022-12-16 |
| `LAST_EDITED_DATE` | date | 100% | 1 | 2022-12-16 → 2022-12-16 |
| `GLOBALID` | id/text | 100% | 231 | e.g. {C7684B38-0DF7-4D92-B5, {41CC4B1C-0711-4AC0-84, {3CF3AE15-6408-46DA-A3 |

## Candidate questions

- `UNIQUE_ID` by `COMMUNITY` — equity gradient? (join ONS income)
- Spatial clustering of open_cultural_spaces_inventory_learning; overlay wards + the decision timeline

_profiled 2026-09-09 · `python3 tools/profile.py open_cultural_spaces_inventory_learning`_

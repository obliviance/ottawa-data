# Ottawa Public Library Locations 2023 

`open_ottawa_public_library_locations_2023` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::ottawa-public-library-locations-2023->
- fetched 2026-09-09 · **34 rows** · 33 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `Name` | id/text | 100% | 34 | e.g. Alta Vista, Beaverbrook, Blackburn Hamlet |
| `Acronym` | id/text | 100% | 34 | e.g. AL, BE, BH |
| `Street_Address` | id/text | 100% | 34 | e.g. 2516 Alta Vista, 2500 Campeau, 199 Glen Park |
| `City` | cat | 100% | 1 | Ottawa 100% |
| `Province` | cat | 100% | 1 | ON 100% |
| `Postal_Code` | id/text | 100% | 34 | e.g. K1V 7T1, K2K 2W3, K1B 5B8 |
| `F_LATITUDE` | num | 100% | 34 | 45.13 · p25 45.27 · p50 45.36 · p95 45.47 · max 45.50  ▃▃▂▁▃▃▂▂▃▆▅▅▃█▅▂ |
| `F_LONGITUDE` | num | 100% | 34 | -76.22 · p25 -75.81 · p50 -75.68 · p95 -75.48 · max -75.46  ▁▁▁▁▁▁▂▁▂▃▃█▃▃▂▃ |
| `F_Canada_Code` | num | 100% | 1 | 1.00 · p25 1.00 · p50 1.00 · p95 1.00 · max 1.00   |
| `F_Canada_Name` | cat | 100% | 1 | Canada 100% |
| `F_Province_Code` | num | 100% | 1 | 35.00 · p25 35.00 · p50 35.00 · p95 35.00 · max 35.00   |
| `F_Province_Name` | cat | 100% | 1 | Ontario 100% |
| `F_Census_Division_Code` | num | 100% | 1 | 3,506 · p25 3,506 · p50 3,506 · p95 3,506 · max 3,506   |
| `F_Census_Division_Name` | cat | 100% | 1 | Ottawa, ON (CDR) 100% |
| `F_Census_Subdivision_Code` | num | 100% | 1 | 3,506,008 · p25 3,506,008 · p50 3,506,008 · p95 3,506,008 · max 3,506,008   |
| `F_Census_Subdivision_Name` | cat | 100% | 1 | Ottawa, ON (CV) 100% |
| `F_Federal_Electoral_District__2` | num | 100% | 8 | 35,041 · p25 35,075 · p50 35,078 · p95 35,088 · max 35,088  ▃▁▁▁▁▁▁▂▁▁▁▄█▁▁▆ |
| `F_Federal_Electoral_District__3` | cat | 100% | 8 | Carleton, ON 26%, Kanata--Carleton, ON 15%, Ottawa--Vanier, ON 15%, Ottawa South, ON 12%, Orléans, ON 9%, Ottawa West--Nepean, ON 9% |
| `F_Dissemination_Area_Code` | num | 100% | 34 | 35,060,014 · p25 35,060,629 · p50 35,061,134 · p95 35,061,653 · max 35,061,794  ▃▄▂▂▂▂▄▃▂▂█▄▅▃▂▃ |
| `F_Dissemination_Area_Name` | id/text | 100% | 34 | e.g. 35061701, ON, 35060739, ON, 35061235, ON |
| `F_Aggregate_Dissemination_Area_` | num | 100% | 31 | 35,060,008 · p25 35,060,043 · p50 35,060,104 · p95 35,060,145 · max 35,060,152  ▃▃▅▃▁▂▂▂▃▂▃▂█▆▃▃ |
| `F_Aggregate_Dissemination_Area1` | id/text | 100% | 31 | e.g. 35060044, ON, 35060084, ON, 35060019, ON |
| `F_Census_Metropolitan_Area_Code` | num | 100% | 1 | 505 · p25 505 · p50 505 · p95 505 · max 505   |
| `F_Census_Metropolitan_Area_Name` | cat | 100% | 1 | Ottawa - Gatineau, ON/QC 100% |
| `F_Census_Tract_Code` | num | 100% | 33 | 5,050,001 · p25 5,050,055 · p50 5,050,137 · p95 5,050,300 · max 5,050,302  ▆▂▄▂▁▃▅█▄▁█▁▁▁▁▄ |
| `F_Census_Tract_Name` | id/text | 100% | 33 | e.g. Ottawa - Gatineau (000, Ottawa - Gatineau (016, Ottawa - Gatineau (012 |
| `F_Forward_Sortation_Area__Q4__2` | cat | 100% | 25 | K0A 26%, K1V 6%, K2K 3%, K1B 3%, K2A 3%, K2H 3% |
| `F_Forward_Sortation_Area__Q4__3` | cat | 100% | 25 | K0A (Almonte, ON) 26%, K1V (Ottawa, ON) 6%, K2K (Ottawa, ON) 3%, K1B (Ottawa, ON) 3%, K2A (Ottawa, ON) 3%, K2H (Ottawa, ON) 3% |
| `F_Precision` | cat | 100% | 2 | Street 71%, Unique ePCCF 29% |
| `ObjectId` | num | 100% | 34 | 1.00 · p25 9.25 · p50 17.50 · p95 32.35 · max 34.00  █▅▅▅▅▅▅▅▅▅▅▅▅▅▅█ |
| `geometry` | id/text | 100% | 34 | e.g. {"type": "Point", "coo, {"type": "Point", "coo, {"type": "Point", "coo |
| `longitude` | num | 100% | 34 | -76.22 · p25 -75.81 · p50 -75.68 · p95 -75.48 · max -75.46  ▁▁▁▁▁▁▂▁▂▃▃█▃▃▂▃ |
| `latitude` | num | 100% | 34 | 45.13 · p25 45.27 · p50 45.36 · p95 45.47 · max 45.50  ▃▃▂▁▃▃▂▂▃▆▅▅▃█▅▂ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_ottawa_public_library_locations_2023`_

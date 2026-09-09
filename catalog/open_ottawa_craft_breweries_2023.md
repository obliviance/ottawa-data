# Ottawa Craft Breweries 2023

`open_ottawa_craft_breweries_2023` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::ottawa-craft-breweries-2023>
- fetched 2026-09-09 · **40 rows** · 14 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `X` | num | 95% | 32 | -8,464,177 · p25 -8,447,589 · p50 -8,427,805 · p95 -8,401,684 · max -8,394,251  ▁▂▁▅▃▁▁▂█▂▃▂▁▁▁▂ |
| `Y` | num | 95% | 32 | 5,649,194 · p25 5,673,989 · p50 5,685,605 · p95 5,694,916 · max 5,703,379  ▂▁▁▁▃▁▃▆▁▁█▆▁▂▁▁ |
| `Name` | id/text | 100% | 40 | e.g. Ashton Brewing Company, Beyond the Pale, Bicycle Craft Brewey |
| `Street_Address` | id/text | 100% | 36 | e.g. 113 Old Mill Rd, 106-250 City Centre Av, 12-850 Industrial Ave |
| `Postcode` | id/text | 100% | 34 | e.g. K0A 1B0, K1R 6K7, K1G 4K2 |
| `Latitude` | num | 95% | 32 | 45.18 · p25 45.33 · p50 45.41 · p95 45.46 · max 45.52  ▂▁▁▁▃▁▃▇▁▁██▁▂▁▁ |
| `Longitude` | num | 95% | 32 | -76.03 · p25 -75.89 · p50 -75.71 · p95 -75.47 · max -75.41  ▁▂▁▅▃▁▁▂█▂▃▂▁▁▁▂ |
| `Ward` | cat | 100% | 16 | Ward 14 - Somerset 12%, Ward 18 - Alta Vista 10%, Ward 4 - Kanata North 10%, Ward 8 - College 10%, Ward 21 - Rideau-Jock 8%, Ward 11 - Beacon Hill-Cy 8% |
| `Beer_Types` | id/text | 100% | 40 | e.g. IPA,Blueberry,Black IP, Gose,Lager,Stout,Belgi, Non-alcoholic,IPA,Pils |
| `Year_Opened` | num | 100% | 14 | 1,996 · p25 2,014 · p50 2,016 · p95 2,020 · max 2,021  ▁▁▁▁▁▁▁▁▂▁▃▅█▃▆▃ |
| `Year_Closed` | num | 15% | 5 | 2,008 · p25 2,018 · p50 2,018 · p95 2,021 · max 2,021  ▄▁▁▁▁▁▁▁▁▁▁▁█▄▄▄ |
| `Status` | cat | 100% | 3 | Active 80%, Closed 15%, Unknown 5% |
| `Website` | id/text | 95% | 38 | e.g. https://www.ashtonbrew, https://btpshop.ca/, http://bicyclecraftbre |
| `ObjectId` | num | 100% | 40 | 1.00 · p25 10.75 · p50 20.50 · p95 38.05 · max 40.00  █▅█▅█▅█▅▅█▅█▅█▅█ |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_ottawa_craft_breweries_2023`_

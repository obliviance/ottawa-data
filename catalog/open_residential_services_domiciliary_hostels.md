# Residential Services (Domiciliary Hostels)

`open_residential_services_domiciliary_hostels` · shape **arcgis-hub** · source `open-ottawa`

- origin: <https://open.ottawa.ca/datasets/ottawa::residential-services-domiciliary-hostels>
- fetched 2026-09-09 · **31 rows** · 17 columns
- csv · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `X` | num | 100% | 31 | -8,447,528 · p25 -8,431,622 · p50 -8,425,973 · p95 -8,388,422 · max -8,388,033  ▃▂▂▃▆▇█▂▂▁▁▁▁▁▂▅ |
| `Y` | num | 100% | 31 | 5,651,830 · p25 5,679,274 · p50 5,682,662 · p95 5,691,790 · max 5,703,073  ▂▁▁▁▁▁▁▄▁█▅▄▅▁▁▁ |
| `OBJECTID` | num | 100% | 31 | 1.00 · p25 8.50 · p50 16.00 · p95 29.50 · max 31.00  ████████▄███████ |
| `REGION` | cat | 100% | 5 | West 35%, East 32%, Outside East 16%, Downtown 13%, Outside South West 3% |
| `NAME` | id/text | 100% | 31 | e.g. Alexander House, Kimberlane Residence, Bruce House |
| `NAME_FR` | id/text | 100% | 31 | e.g. Maison Alexander, Résidence Kimberlane, Maison Bruce |
| `ADDRESS` | id/text | 100% | 31 | e.g. 716 Edison Avenue , 712 Edison Avenue , 461 Evered Ave  |
| `ADDRESS_FR` | id/text | 100% | 31 | e.g. 716, avenue Edison, 712, avenue Edison, 461, avenue Evered |
| `POSTAL_CODE` | id/text | 96% | 26 | e.g. K2A 1W1, K2P 1X2, K2A 1W5 |
| `PHONE` | id/text | 96% | 29 | e.g. (613) 728-8827, (613) 729-0911, (613) 729-2398 |
| `LINK` | cat | 96% | 1 | http://www.ottawa.ca/en/ 100% |
| `LINK_FR` | cat | 96% | 1 | http://www.ottawa.ca/fr/ 100% |
| `MODIFIED_DATE` | date | 96% | 1 | 2014-11-05 → 2014-11-05 |
| `CREATED_DATE` | text | 0% | 0 | e.g.  |
| `MODIFIED_BY` | cat | 96% | 1 | bedfordwa 100% |
| `CREATED_BY` | text | 0% | 0 | e.g.  |
| `GlobalID` | id/text | 100% | 31 | e.g. {D3E2EC25-19A3-415F-AE, {4DFD268D-49B3-4AE1-87, {67BF263B-3534-4A40-A9 |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_residential_services_domiciliary_hostels`_

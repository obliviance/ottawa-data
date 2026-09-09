# Street Lights

`open_street_lights` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::street-lights>
- fetched 2026-09-09 · **80,670 rows** · 22 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 80,670 | 1.00 · p25 20,168 · p50 40,336 · p95 76,637 · max 80,670  █████▇████▇█████ |
| `POLE_ID` | num | 100% | 12,420 | 0.00 · p25 0.00 · p50 0.00 · p95 2,094,271 · max 33,553,619  █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `INSTALL_POLE` | text | 100% | 1,191 | e.g. 2009-02-01T00:00:00Z, 2008-06-29T00:00:00Z, 2010-10-01T00:00:00Z |
| `INSTALL_LIGHT` | text | 100% | 1,435 | e.g. 1899-12-30T00:00:00Z, 2020-01-17T00:00:00Z, 2015-11-16T00:00:00Z |
| `HEAD_STYLE` | text | 100% | 230 | e.g. COBRA HEAD, CLDM, GCJ120H 3K T3 |
| `REFRACTOR` | text | 100% | 36 | e.g. FLAT GLASS,  , DROP GLASS |
| `LIGHT_TYPE` | cat | 100% | 7 | SL 93%, PL 5%, LL 2%, WP 1%, SLS 0%, REC 0% |
| `BRACKET_LEN` | num | 100% | 35 | 0.00 · p25 0.00 · p50 1.40 · p95 3.00 · max 10.00  █▁▆▅▂▁▁▁▁▁▁▁▁▁▁▁ |
| `POLE_HEIGHT` | num | 100% | 83 | 0.00 · p25 0.00 · p50 9.10 · p95 11.20 · max 107  ▆█▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `POLE_TYPE` | text | 100% | 55 | e.g. NEWPORT, CONCRETE, ALUMINUM |
| `LIGHTS_NUM` | num | 100% | 12 | 0.00 · p25 1.00 · p50 1.00 · p95 1.00 · max 13.00  ▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁ |
| `LIGHT_SOUR` | cat | 100% | 11 | HPS 66%, LED 32%, MH 2%, LIGHT BULB 0%, RECEPTACLE 0%, MV 0% |
| `WATTAGE` | num | 100% | 99 | 0.00 · p25 70.00 · p50 100 · p95 250 · max 1,250  █▇▂▃▁▁▁▁▁▁▁▁▁▁▁▁ |
| `YEAR_1_LE` | text | 100% | 99 | e.g.  , 41, 51 |
| `STREET_NAM` | text | 100% | 7,080 | e.g. JOSHUA STREET, JOURNEYMAN STREET, JOYCE CRESCENT |
| `ENERGY_JUR` | cat | 100% | 12 | HO 85%, H1 13%, BIA 1%, OH 0%,   0%, H0 0% |
| `GLOBALID` | id/text | 100% | 80,670 | e.g. {10512103-CBB0-469F-9C, {97AB4A62-F35A-4DAD-BD, {9E395CDC-3423-4E5A-8F |
| `CREATED_DATE` | text | 0% | 0 | e.g.  |
| `MODIFIED_DATE` | text | 0% | 0 | e.g.  |
| `geometry` | id/text | 99% | 74,962 | e.g. {"type": "Point", "coo, {"type": "Point", "coo, {"type": "Point", "coo |
| `longitude` | num | 99% | 74,931 | -76.33 · p25 -75.77 · p50 -75.70 · p95 -75.48 · max -75.27  ▁▁▁▁▁▁▃▂▄█▄▂▃▁▁▁ |
| `latitude` | num | 99% | 74,924 | 3.20 · p25 45.30 · p50 45.37 · p95 45.47 · max 45.53  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█ |

## Candidate questions

- Trend / seasonality of open_street_lights over `YEAR_1_LE`; structural breaks?
- Spatial clustering of open_street_lights; overlay wards + the decision timeline

_profiled 2026-09-09 · `python3 tools/profile.py open_street_lights`_

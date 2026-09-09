# Construction Road resurfacing, watermain, sewer, multi-use pathways, bike lanes

`open_construction_road_resurfacing_watermain_sewer_multi_use_pathways_b` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::construction-road-resurfacing-watermain-sewer-multi-use-pathways-bike-lanes>
- fetched 2026-09-09 · **2,174 rows** · 13 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `OBJECTID` | num | 100% | 2,174 | 44.00 · p25 15,546 · p50 34,016 · p95 35,698 · max 35,874  ▁▁▁▁▁▁▃▁▁▁▁▁▁▁▁█ |
| `FEATURE_TYPE` | text | 100% | 42 | e.g. RD_SURF, RS, GNWP |
| `FEATURE_TYPE_FR` | text | 100% | 42 | e.g. RD_SURF, RS, GNWP |
| `STATUS` | cat | 100% | 3 | PLANNED 96%, INPROGRESS 4%, APPROVED 0% |
| `STATUS_FR` | cat | 100% | 3 | PLANNED 96%, INPROGRESS 4%, APPROVED 0% |
| `TARGETED_START` | cat | 100% | 5 | This Year 42%, 1-2 Years 22%, 2-3 Years 14%, 3-5 Years 12%, 4-7 Years 11% |
| `TARGETED_START_FR` | cat | 100% | 5 | Cette année 42%, 1 à 2 ans 22%, 2 à 3 ans 14%, 3 à 5 ans 12%, 4 à 7 ans 11% |
| `PROJECT_MANAGER` | text | 92% | 82 | e.g. Alchawa, Houssam, Strampel, Matthew C, Ritchie, Jon |
| `PROJECTWEBPAGE` | cat | 2% | 3 | WCC 85%, https://www.oeb.ca/appli 13%, TEST 2% |
| `PROJECTWEBPAGE_FR` | cat | 0% | 2 | AAC 95%, TEST FR 5% |
| `TRAFFICIMPACTS` | text | 21% | 54 | e.g. East Complex Access fr, None, Minor traffic impacts  |
| `Coordination` | cat | 1% | 8 | Impacts:Colonel By Dr-Gr 56%, Canterbury Ave, Plesser  19%, Construction not schedul 7%, 7 crossings in 2023 : Bo 4%, Work to be scheduled aro 4%, During Construction 4% |
| `geometry` | id/text | 100% | 2,170 | e.g. {"type": "LineString",, {"type": "LineString",, {"type": "LineString", |

## Candidate questions

- Spatial clustering of open_construction_road_resurfacing_watermain_sewer_multi_use_pathways_b; overlay wards + the decision timeline

_profiled 2026-09-09 · `python3 tools/profile.py open_construction_road_resurfacing_watermain_sewer_multi_use_pathways_b`_

# Ottawa Public Library Service Areas

`open_ottawa_public_library_service_areas` · shape **arcgis-hub** · source `open-ottawa` · **spatial**

- origin: <https://open.ottawa.ca/datasets/ottawa::ottawa-public-library-service-areas>
- fetched 2026-09-09 · **32 rows** · 10 columns
- geojson · licence: https://ottawa.ca/en/city-hall/get-know-your-city/open-data#open-data-licence-ve

## Columns

| column | kind | non-null | distinct | summary |
| --- | --- | --- | --- | --- |
| `FID` | num | 100% | 32 | 1.00 · p25 8.75 · p50 16.50 · p95 30.45 · max 32.00  ████████████████ |
| `OBJECTID_1` | num | 100% | 32 | 1.00 · p25 12.00 · p50 32.00 · p95 92.45 · max 94.00  █▅▆▃▂▅▂▁▂▁▁▃▂▃▆▅ |
| `OBJECTID` | num | 100% | 32 | 1.00 · p25 12.00 · p50 32.00 · p95 98.45 · max 100  █▄▄▄▂▃▂▁▂▁▂▂▂▄▃▅ |
| `NAMESE2016` | id/text | 100% | 32 | e.g. Edwards - Carlsbad Spr, Blackburn Hamlet, Beaverbrook |
| `NAMESF2016` | id/text | 100% | 32 | e.g. Edwards - Carlsbad Spr, Blackburn Hamlet, Beaverbrook |
| `POPEST2016` | num | 100% | 32 | 139 · p25 5,029 · p50 7,432 · p95 20,532 · max 26,674  ▂▃█▆▅▄▅▅▁▁▂▁▁▁▂▂ |
| `Branch` | id/text | 100% | 32 | e.g. Greely, Blackburn Hamlet, Beaverbrook |
| `Shape__Area` | num | 100% | 32 | 3,459,438 · p25 23,190,263 · p50 47,461,913 · p95 661,832,084 · max 900,770,018  █▂▁▁▂▁▁▁▁▁▁▁▁▁▁▁ |
| `Shape__Length` | num | 100% | 32 | 11,294 · p25 32,540 · p50 42,381 · p95 204,775 · max 257,382  ▅█▃▂▃▁▁▁▂▁▂▁▁▁▁▁ |
| `geometry` | id/text | 100% | 32 | e.g. {"type": "Polygon", "c, {"type": "Polygon", "c, {"type": "Polygon", "c |

## Candidate questions

- (none templated)

_profiled 2026-09-09 · `python3 tools/profile.py open_ottawa_public_library_service_areas`_

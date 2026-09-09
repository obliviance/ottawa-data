# releases/

Public dataset releases. One folder per release:

```
releases/<slug>/
  data.csv  (or .parquet / .geojson)
  datapackage.json     — Frictionless Data descriptor (schema, licence, sources)
  README.md            — what it is, how it was built, caveats, refresh command
```

A release is the minimum shippable unit: even a source explored only to recon
depth ships its cleaned data + tearsheet here. Snapshot each release URL to the
Wayback Machine (`tools/snapshot.py`).

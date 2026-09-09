# warehouse/

A DuckDB database (`ottawa.duckdb`) plus one Parquet file per dataset. Both are
**gitignored** — they rebuild from the ingesters in `tools/ingest/`. Only
`manifest.json` (the small, human-readable index) is committed.

```
python3 tools/warehouse.py init                 # create empty
python3 tools/ingest/arcgis_hub.py --limit 20   # land some data
python3 tools/warehouse.py list                 # what's here
python3 tools/warehouse.py query "SELECT ..."   # ad-hoc SQL; each dataset is view d_<id>
```

From Python / a notebook:

```python
import sys; sys.path.insert(0, "tools")
import warehouse
con = warehouse.con()          # every dataset attached as a view
con.sql("SELECT * FROM d_open_traffic_collisions LIMIT 5").df()
```

Datasets are named `d_<dataset_id>` in SQL (dashes → underscores). The
`_datasets` table holds the metadata that's also in `manifest.json`.

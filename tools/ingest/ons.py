#!/usr/bin/env python3
"""Ingest the Ottawa Neighbourhood Study (ONS) indicator tables from its open WordPress API.

    python3 tools/ingest/ons.py

`https://ons-sqo.ca/wp-json/ons/v1/get-data/<tab>` serves four sheet-shaped tabs as
{"columns": [...], "rows": [[...], ...]} with no key (survey 2026-10-16):

  neighbourhoods  116 rows: name, description, geometry (polygon + bounds), ONS_ID, name_fr
  data            884 indicator rows x [id, 0 (city total), 3001..3117 (ONS_ID)]; "NA" = suppressed
  layers          386 rows of indicator metadata (categories, dates, source); its
                  `Polygon attribute` column holds the indicator id used in `data`
                  (355 distinct ids: a few metadata rows share one id)
  bins            map legend classes (not analytically useful; kept for completeness)

Registers `ons_neighbourhoods`, `ons_indicator_values` (long: indicator_id, ons_id, value,
raw), `ons_indicator_layers`, `ons_bins`. Values are strings in the source; `value` is the
numeric parse, `raw` keeps the original (so "NA" suppression stays visible).
"""
from __future__ import annotations

import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
import warehouse  # noqa: E402
from _http import get_json  # noqa: E402

BASE = "https://ons-sqo.ca/wp-json/ons/v1/get-data/"
SRC = "ons"


def _tab(name: str):
    import pandas as pd
    j = get_json(BASE + name)
    return pd.DataFrame(j["rows"], columns=j["columns"])


def main() -> None:
    import pandas as pd

    hoods = _tab("neighbourhoods")
    hoods["geometry"] = hoods["geometry"].map(lambda g: json.dumps(g) if not isinstance(g, str) else g)
    warehouse.register("ons_neighbourhoods", hoods, source_id=SRC, shape="json-api",
                       title="Ottawa Neighbourhood Study — neighbourhoods (Gen 3)",
                       origin_url=BASE + "neighbourhoods",
                       notes="geometry = JSON {position, bounds, latLngs}; ONS_ID joins ons_indicator_values")

    data = _tab("data")
    long = data.melt(id_vars="id", var_name="ons_id", value_name="raw").rename(columns={"id": "indicator_id"})
    long["value"] = pd.to_numeric(long["raw"], errors="coerce")
    long["ons_id"] = pd.to_numeric(long["ons_id"], errors="coerce").astype("Int64")
    # 47 indicator ids appear twice in `data` with identical values (checked on the
    # 2026-10-24 fetch); keep one row per (indicator, neighbourhood) but fail loudly if
    # a duplicate ever disagrees, since that would mean the API changed meaning.
    conflict = long.groupby(["indicator_id", "ons_id"])["raw"].nunique(dropna=False).max()
    if conflict > 1:
        raise RuntimeError("duplicate ONS indicator rows disagree; inspect before ingesting")
    long = long.drop_duplicates(["indicator_id", "ons_id"]).reset_index(drop=True)
    warehouse.register("ons_indicator_values", long, source_id=SRC, shape="json-api",
                       title="Ottawa Neighbourhood Study — indicator values by neighbourhood",
                       origin_url=BASE + "data",
                       notes="ons_id 0 = city total; 'NA' in raw = suppressed/unavailable (value is null)")

    warehouse.register("ons_indicator_layers", _tab("layers"), source_id=SRC, shape="json-api",
                       title="Ottawa Neighbourhood Study — indicator metadata",
                       origin_url=BASE + "layers",
                       notes="`Polygon attribute` = indicator_id in ons_indicator_values")
    warehouse.register("ons_bins", _tab("bins"), source_id=SRC, shape="json-api",
                       title="Ottawa Neighbourhood Study — map legend bins", origin_url=BASE + "bins")


if __name__ == "__main__":
    main()

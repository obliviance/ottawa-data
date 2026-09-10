#!/usr/bin/env python3
"""q0005 — 311 service requests by ward: volume, mix, and how long they stay open.

~640k requests across the current + previous rolling-year files. Each row carries a
Ward, a Type, and Opened/Closed dates.

Produces:
  releases/311-by-ward/
    by_ward.csv          per ward: request count, share, median days-to-close
    by_ward_type.csv     per ward × top request type
    datapackage.json + README.md

Run: python3 explorations/requests_311_by_ward.py   (needs d_311_current, d_311_lastyear)
"""
from __future__ import annotations

import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent / "tools"))
import warehouse  # noqa: E402

OUT = pathlib.Path(__file__).parent.parent / "releases" / "311-by-ward"


def main() -> None:
    c = warehouse.con()
    # the columns are "Name | Nom"; quote and alias them
    df = c.execute(r'''
        SELECT "Ward | Quartier"                              AS ward,
               "Type | Type"                                  AS type,
               try_strptime("Opened Date | Date d'ouverture", ['%Y-%m-%d %H:%M:%S','%Y-%m-%dT%H:%M:%S','%Y-%m-%d']) AS opened,
               try_strptime("Closed Date | Date de fermeture", ['%Y-%m-%d %H:%M:%S','%Y-%m-%dT%H:%M:%S','%Y-%m-%d']) AS closed
        FROM (SELECT * FROM d_311_current UNION ALL BY NAME SELECT * FROM d_311_lastyear)
        WHERE "Ward | Quartier" NOT IN ('', '\N') AND "Ward | Quartier" IS NOT NULL
    ''').df()
    names = c.execute("SELECT CAST(ward_num AS VARCHAR) ward, ward_name FROM d_spine_wards").df()
    c.close()
    df = df.merge(names, on="ward", how="left")
    df["ward"] = df["ward"] + "  " + df["ward_name"].fillna("?")

    import numpy as np
    import pandas as pd
    df["days_open"] = (df["closed"] - df["opened"]).dt.total_seconds() / 86400
    df.loc[(df.days_open < 0) | (df.days_open > 730), "days_open"] = np.nan

    by_ward = (df.groupby("ward")
               .agg(requests=("type", "size"),
                    median_days_to_close=("days_open", "median"),
                    pct_closed=("closed", lambda s: s.notna().mean()))
               .assign(share=lambda d: (d.requests / d.requests.sum()).round(4),
                       median_days_to_close=lambda d: d.median_days_to_close.round(1),
                       pct_closed=lambda d: d.pct_closed.round(3))
               .sort_values("requests", ascending=False)
               .reset_index())

    top_types = df["type"].value_counts().head(15).index
    by_wt = (df[df["type"].isin(top_types)]
             .groupby(["ward", "type"]).size().rename("requests").reset_index()
             .sort_values(["ward", "requests"], ascending=[True, False]))

    OUT.mkdir(parents=True, exist_ok=True)
    by_ward.to_csv(OUT / "by_ward.csv", index=False)
    by_wt.to_csv(OUT / "by_ward_type.csv", index=False)

    span = f"{df.opened.min():%Y-%m-%d} to {df.opened.max():%Y-%m-%d}"
    (OUT / "datapackage.json").write_text(json.dumps({
        "name": "311-by-ward",
        "title": "Ottawa 311 service requests by ward",
        "description": f"{len(df):,} requests, {span}, aggregated by ward and request type.",
        "licenses": [{"name": "OGL-Ottawa", "title": "Open Government Licence – City of Ottawa"}],
        "sources": [{"title": "Ottawa 311 open data (rolling CSVs)",
                     "path": "https://open.ottawa.ca/documents/ottawa::current-year-service-requests"}],
        "resources": [{"path": "by_ward.csv", "format": "csv"},
                      {"path": "by_ward_type.csv", "format": "csv"}],
    }, indent=2) + "\n")

    hi, lo = by_ward.iloc[0], by_ward.iloc[-1]
    slow = by_ward.sort_values("median_days_to_close", ascending=False).iloc[0]
    fast = by_ward.dropna(subset=["median_days_to_close"]).sort_values("median_days_to_close").iloc[0]
    (OUT / "README.md").write_text(f"""# Ottawa 311 service requests by ward

{len(df):,} requests, {span}. Source: Ottawa's two rolling 311 CSVs (OGL – City of Ottawa).

## Findings

- **Highest volume:** {hi.ward} — {hi.requests:,} requests ({hi.share:.0%} of the city
  total). **Lowest:** {lo.ward} — {lo.requests:,}.
- **Slowest to close:** {slow.ward}, median {slow.median_days_to_close:.0f} days open.
  **Fastest:** {fast.ward}, {fast.median_days_to_close:.0f} days.
- Raw volume tracks population and urban density, not need — normalise by ward
  population (2021 census ward data) before reading anything into it. The
  time-to-close spread is the more interesting signal.

## Files

`by_ward.csv` — count, share, median days-to-close, % closed per ward.
`by_ward_type.csv` — ward × the 15 commonest request types.

Regenerate: `python3 explorations/requests_311_by_ward.py`
""")
    print(f"releases/311-by-ward/ — {len(df):,} requests, {by_ward.ward.nunique()} wards")
    print(by_ward.to_string(index=False))


if __name__ == "__main__":
    main()

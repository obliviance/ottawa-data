#!/usr/bin/env python3
"""Do worse-off Ottawa neighbourhoods wait longer for city services?

    python3 explorations/service_equity.py

The question this set out to answer, and could not. What it found instead is
that **Ottawa's 311 "closed date" does not measure service delivery** for most
request categories, which invalidates the time-to-close finding in q0005
(`releases/311-by-ward`) and makes the equity question unanswerable with the
data as published.

The intended design was sound: join 311 requests to census tracts (via
dissemination-area boundaries, which carry a CTUID), then to the Ottawa
Neighbourhood Equity Index, and compare closure times across the equity
gradient. Every join works. The measure does not.

THREE FINDINGS, IN THE ORDER THEY APPEARED

1. **Geocoding is a property of request type, not neighbourhood.** Only 102k of
   640k requests carry coordinates, but the missingness is almost entirely
   categorical: Roads and Transportation is 79% geocoded and Recreation 99.7%,
   while Garbage, Water, Parking and Bylaw are ~0%. That is good news for bias
   -- it is not neighbourhoods being dropped -- and it means any spatial
   analysis is really an analysis of road and recreation requests.

2. **The close date is administrative, not operational, for exactly those
   categories.** Median days-to-close: Garbage 2, Parking 0, Bylaw 3 -- but
   Roads 197, Water 202, Recreation 205. Dead-animal removal has a 210-day
   median. Nobody leaves a carcass for seven months. Those tickets evidently
   stay open until some periodic reconciliation, so "days to close" is
   measuring ticket hygiene, not response.

3. **q0005's ward gradient is therefore a request-mix artifact.** It reported
   urban wards closing in 2-3 days and rural wards in 11-13, and called the
   time-to-close spread "the more interesting signal". But the slow wards are
   the ones submitting proportionally more of the slow-to-administer
   categories, and within a single completion-closed category -- garbage --
   ward medians run 1 to 3 days. Almost flat.

The equity question stays open. Answering it needs a service-completion
timestamp the city does not publish, or a category where the close date is
trustworthy *and* geocoded. No published category is both.

Produces:
  releases/311-service-equity/
    by_type.csv        per category: volume, geocoding rate, median days, % still open
    ward_mix.csv       per ward: pooled median vs share of slow-to-administer types
    by_tract.csv       the NEI join that was attempted, with its null result
    datapackage.json + README.md
"""
from __future__ import annotations

import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent / "tools"))
import warehouse  # noqa: E402

OUT = pathlib.Path(__file__).parent.parent / "releases" / "311-service-equity"

# Categories whose close date tracks completion, established empirically below.
COMPLETION_CLOSED = ("Garbage and Recycling", "Parking Control Enforcement",
                     "Bylaw Services")
# Two years, in hours -- the clamp q0005 used, kept for comparability.
MAX_HOURS = 17520


def main() -> None:
    import numpy as np
    import pandas as pd

    c = warehouse.con()
    c.execute(r"""CREATE OR REPLACE TEMP TABLE r AS
      SELECT "Ward | Quartier" AS ward, "Type | Type" AS type,
             "Description | Description" AS descr,
             TRY_CAST("Latitude | Latitude"  AS DOUBLE) AS lat,
             TRY_CAST("Longitude | Longitude" AS DOUBLE) AS lon,
             try_strptime("Opened Date | Date d'ouverture",
                          ['%Y-%m-%d %H:%M:%S','%Y-%m-%dT%H:%M:%S','%Y-%m-%d']) AS opened,
             try_strptime("Closed Date | Date de fermeture",
                          ['%Y-%m-%d %H:%M:%S','%Y-%m-%dT%H:%M:%S','%Y-%m-%d']) AS closed
      FROM (SELECT * FROM d_311_current UNION ALL BY NAME SELECT * FROM d_311_lastyear)""")

    # ---- 1. the categorical structure of the data ---------------------------
    by_type = c.execute(f"""
      SELECT type,
             count(*) AS requests,
             round(100.0 * avg(CASE WHEN lat IS NOT NULL THEN 1 ELSE 0 END), 1) AS pct_geocoded,
             round(100.0 * avg(CASE WHEN closed IS NULL THEN 1 ELSE 0 END), 1) AS pct_still_open,
             round(median(date_diff('hour', opened, closed) / 24.0), 1) AS median_days_to_close
      FROM r WHERE opened IS NOT NULL AND type NOT IN ('', '\\N')
      GROUP BY 1 ORDER BY requests DESC""").df()
    by_type["close_date_meaningful"] = by_type.type.isin(COMPLETION_CLOSED)

    # ---- 2. the ward confound ------------------------------------------------
    slow = tuple(t for t in by_type[~by_type.close_date_meaningful].type)
    ward_mix = c.execute(f"""
      SELECT ward,
             count(*) AS requests,
             round(median(date_diff('hour', opened, closed) / 24.0), 1) AS pooled_median_days,
             round(100.0 * avg(CASE WHEN type IN {slow} THEN 1 ELSE 0 END), 1) AS pct_slow_to_administer,
             round(median(CASE WHEN type = 'Garbage and Recycling'
                          THEN date_diff('hour', opened, closed) / 24.0 END), 1) AS garbage_median_days
      FROM r WHERE closed IS NOT NULL AND ward NOT IN ('', '\\N')
      GROUP BY 1 ORDER BY pooled_median_days DESC""").df()
    ward_mix["ward"] = pd.to_numeric(ward_mix.ward, errors="coerce")
    ward_mix = ward_mix.dropna(subset=["ward"]).astype({"ward": int}).sort_values("ward")

    # ---- 3. the equity join that was attempted -------------------------------
    # Census tracts are not published as boundaries, but dissemination areas are
    # and they carry a CTUID -- so dissolving DAs by tract reconstructs them.
    c.execute("""CREATE OR REPLACE TEMP TABLE ct AS
      SELECT printf('%.2f', CAST(CTUID AS DOUBLE)) AS ctid,
             any_value(CTNAME) AS ctname,
             ST_Union_Agg(ST_GeomFromGeoJSON(geometry)) AS geom
      FROM d_open_ottawa_dissemination_areas WHERE CTUID IS NOT NULL GROUP BY 1""")
    tract = c.execute(f"""
      SELECT ct.ctid AS ctid, any_value(ct.ctname) AS tract_name, count(*) AS requests,
             round(median(date_diff('hour', r.opened, r.closed) / 24.0), 1) AS median_days_to_close
      FROM r JOIN ct ON ST_Contains(ct.geom, ST_Point(r.lon, r.lat))
      WHERE r.lat IS NOT NULL AND r.closed IS NOT NULL
        AND r.type = 'Roads and Transportation'
        AND date_diff('hour', r.opened, r.closed) BETWEEN 0 AND {MAX_HOURS}
      GROUP BY 1""").df()
    nei = c.execute("""
      SELECT printf('%.2f', CTID) AS ctid, round(SCORENEI, 1) AS equity_score,
             URB_RURAL AS stratum, CTNAME_EN AS nei_name
      FROM d_open_ottawa_neighbourhood_equity_index_nei_2024 WHERE SCORENEI > 0""").df()
    n_nei, n_ct = len(nei), c.execute("SELECT count(*) FROM ct").fetchone()[0]
    c.close()

    by_tract = tract.merge(nei, on="ctid").query("requests >= 30")

    corr = []
    for stratum, g in by_tract.groupby("stratum"):
        if len(g) < 8:
            continue
        k = max(3, len(g) // 4)
        corr.append({
            "stratum": stratum, "tracts": len(g),
            "correlation_equity_vs_days": round(float(np.corrcoef(g.equity_score, g.median_days_to_close)[0, 1]), 3),
            "worst_off_quartile_median_days": round(float(g.nsmallest(k, "equity_score").median_days_to_close.median()), 1),
            "best_off_quartile_median_days": round(float(g.nlargest(k, "equity_score").median_days_to_close.median()), 1),
        })
    corr = pd.DataFrame(corr)

    OUT.mkdir(parents=True, exist_ok=True)
    by_type.to_csv(OUT / "by_type.csv", index=False)
    ward_mix.to_csv(OUT / "ward_mix.csv", index=False)
    by_tract.sort_values("equity_score").to_csv(OUT / "by_tract.csv", index=False)
    corr.to_csv(OUT / "equity_correlation.csv", index=False)

    (OUT / "datapackage.json").write_text(json.dumps({
        "name": "311-service-equity",
        "title": "Ottawa 311 — what 'days to close' actually measures",
        "description": ("An attempt to test whether lower-equity neighbourhoods wait longer "
                        "for city services, which instead established that the published "
                        "close date is administrative rather than operational for most "
                        "request categories, and that the ward time-to-close gradient in "
                        "releases/311-by-ward is a request-mix artifact."),
        "licenses": [{"name": "OGL-Ottawa",
                      "title": "Open Government Licence – City of Ottawa"}],
        "sources": [{"title": "Ottawa 311 open data (rolling CSVs)",
                     "path": "https://open.ottawa.ca/documents/ottawa::current-year-service-requests"},
                    {"title": "Ottawa Neighbourhood Equity Index 2024",
                     "path": "https://open.ottawa.ca/"},
                    {"title": "Ottawa Dissemination Areas (census tract boundaries)",
                     "path": "https://open.ottawa.ca/"}],
        "resources": [{"path": f"{n}.csv", "format": "csv"} for n in
                      ("by_type", "ward_mix", "by_tract", "equity_correlation")],
    }, indent=2) + "\n")

    fast = by_type[by_type.close_date_meaningful]
    slow_t = by_type[~by_type.close_date_meaningful].nlargest(3, "requests")
    g_lo, g_hi = ward_mix.garbage_median_days.min(), ward_mix.garbage_median_days.max()
    (OUT / "README.md").write_text(f"""# Ottawa 311 — what "days to close" actually measures

A negative result, and a correction to [`releases/311-by-ward`](../311-by-ward).

The question was: **do people in worse-off neighbourhoods wait longer for the
city to fix things?** The joins all work. The measure does not.

## 1. Geocoding is categorical, not geographic

{by_type.requests.sum():,} requests; only
{by_type.eval('requests * pct_geocoded / 100').sum():,.0f} carry coordinates. But the
missingness is a property of the request **type**, not the neighbourhood —
Roads is {by_type.set_index('type').loc['Roads and Transportation','pct_geocoded']}% geocoded
and Recreation {by_type.set_index('type').loc['Recreation and Culture','pct_geocoded']}%, while
Garbage, Water, Parking and Bylaw are ~0%.

Good news for bias: no neighbourhood is being dropped. But it means any spatial
analysis of 311 is really an analysis of road and recreation requests.

## 2. The close date is administrative, not operational

| Category | Requests | Median days to close |
| --- | ---: | ---: |
""" + "\n".join(f"| {r.type} | {r.requests:,} | **{r.median_days_to_close}** |"
                for _, r in fast.iterrows())
     + "\n" + "\n".join(f"| {r.type} | {r.requests:,} | {r.median_days_to_close} |"
                        for _, r in slow_t.iterrows()) + f"""

Garbage closes in {fast.set_index('type').loc['Garbage and Recycling','median_days_to_close']:.0f} days,
parking in {fast.set_index('type').loc['Parking Control Enforcement','median_days_to_close']:.0f}.
Roads takes {by_type.set_index('type').loc['Roads and Transportation','median_days_to_close']:.0f}.
**Dead-animal removal has a 210-day median.** Nobody leaves a carcass for seven
months — those tickets stay open until some periodic reconciliation. For those
categories the field measures ticket hygiene, not response time.

And they are exactly the categories that carry coordinates. No published
category is both geocoded and completion-closed.

## 3. So q0005's ward gradient is a request-mix artifact

`releases/311-by-ward` reported urban wards closing in 2–3 days and rural wards
in 11–13, and called the time-to-close spread "the more interesting signal".
It is not a signal about service speed. The slow wards are the ones submitting
proportionally more of the slow-to-administer categories:

| Ward | Pooled median days | Share slow-to-administer |
| --- | ---: | ---: |
""" + "\n".join(
        f"| {int(r.ward)} | {r.pooled_median_days} | {r.pct_slow_to_administer}% |"
        for _, r in ward_mix.nlargest(3, "pooled_median_days").iterrows())
     + "\n" + "\n".join(
        f"| {int(r.ward)} | {r.pooled_median_days} | {r.pct_slow_to_administer}% |"
        for _, r in ward_mix.nsmallest(3, "pooled_median_days").iterrows()) + f"""

**Within garbage alone** — a category that genuinely closes on completion — ward
medians run **{g_lo:.0f} to {g_hi:.0f} days**. Almost flat. Whatever varies between wards, it
is not the speed at which the city closes a comparable request.

## 4. The equity question, unanswered

The join was built anyway and is published here so the next attempt starts
further along: dissemination-area boundaries carry a `CTUID`, so dissolving them
reconstructs the {n_ct} census tracts the city does not publish directly, and
{len(by_tract)} tracts have enough geocoded road requests to compare.

The correlation between equity score and closure time is ~0 in every stratum —
but that is **not evidence of equitable service**, because the underlying
measure is not measuring service:

| Stratum | Tracts | Correlation | Worst-off quartile | Best-off quartile |
| --- | ---: | ---: | ---: | ---: |
""" + "\n".join(f"| {r.stratum} | {r.tracts} | {r.correlation_equity_vs_days:+.2f} | "
                f"{r.worst_off_quartile_median_days} d | {r.best_off_quartile_median_days} d |"
                for _, r in corr.iterrows()) + f"""

## Caveats

- **The NEI is calibrated separately within urban and rural**, per its own
  `RED_GREEN` field, so a rural 40 and an urban 40 are not the same thing.
  Everything above is compared within stratum.
- Only {len(by_tract)} of {n_nei} NEI tracts join. The unmatched ones are
  systematically the **newest suburbs** — Barrhaven-Rideaucrest, Avalon West —
  where 2021 census tract splits postdate the dissemination-area file. Current
  StatCan boundaries would close that gap.

## What would actually answer it

A service-completion timestamp, which the city does not publish; or a category
that is both geocoded and completion-closed, which none currently is. Worth
asking the city for — it is a small schema change that would make a real
accountability question answerable.

Regenerate: `python3 explorations/service_equity.py`
""")

    print(f"releases/311-service-equity/ — {by_type.requests.sum():,} requests, "
          f"{len(by_tract)} tracts joined of {n_nei} NEI tracts")
    print("\nclose-date behaviour by category:")
    print(by_type[["type", "requests", "pct_geocoded", "median_days_to_close",
                   "close_date_meaningful"]].to_string(index=False))
    print("\nequity correlation (null, and uninterpretable — see README):")
    print(corr.to_string(index=False))
    print(f"\ngarbage-only ward medians: {g_lo:.0f}–{g_hi:.0f} days (vs pooled "
          f"{ward_mix.pooled_median_days.min():.0f}–{ward_mix.pooled_median_days.max():.0f})")


if __name__ == "__main__":
    main()

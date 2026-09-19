# Ottawa 311 — what "days to close" actually measures

A negative result, and a correction to [`releases/311-by-ward`](../311-by-ward).

The question was: **do people in worse-off neighbourhoods wait longer for the
city to fix things?** The joins all work. The measure does not.

## 1. Geocoding is categorical, not geographic

639,809 requests; only
102,299 carry coordinates. But the
missingness is a property of the request **type**, not the neighbourhood —
Roads is 78.8% geocoded
and Recreation 99.7%, while
Garbage, Water, Parking and Bylaw are ~0%.

Good news for bias: no neighbourhood is being dropped. But it means any spatial
analysis of 311 is really an analysis of road and recreation requests.

## 2. The close date is administrative, not operational

| Category | Requests | Median days to close |
| --- | ---: | ---: |
| Garbage and Recycling | 208,222 | **2.0** |
| Bylaw Services | 102,884 | **3.0** |
| Parking Control Enforcement | 90,096 | **0.0** |
| Roads and Transportation | 107,044 | 197.0 |
| Water and the Environment | 98,948 | 202.0 |
| Recreation and Culture | 14,072 | 205.0 |

Garbage closes in 2 days,
parking in 0.
Roads takes 197.
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
| 5 | 13.0 | 44.3% |
| 20 | 11.0 | 41.4% |
| 21 | 6.0 | 34.8% |
| 8 | 2.0 | 36.6% |
| 13 | 2.0 | 25.7% |
| 14 | 2.0 | 26.0% |

**Within garbage alone** — a category that genuinely closes on completion — ward
medians run **1 to 3 days**. Almost flat. Whatever varies between wards, it
is not the speed at which the city closes a comparable request.

## 4. The equity question, unanswered

The join was built anyway and is published here so the next attempt starts
further along: dissemination-area boundaries carry a `CTUID`, so dissolving them
reconstructs the 204 census tracts the city does not publish directly, and
178 tracts have enough geocoded road requests to compare.

The correlation between equity score and closure time is ~0 in every stratum —
but that is **not evidence of equitable service**, because the underlying
measure is not measuring service:

| Stratum | Tracts | Correlation | Worst-off quartile | Best-off quartile |
| --- | ---: | ---: | ---: | ---: |
| Rural | 14 | -0.07 | 187.0 d | 184.0 d |
| Suburban | 52 | +0.10 | 164.5 d | 184.0 d |
| Urban | 109 | +0.13 | 184.5 d | 203.0 d |

## Caveats

- **The NEI is calibrated separately within urban and rural**, per its own
  `RED_GREEN` field, so a rural 40 and an urban 40 are not the same thing.
  Everything above is compared within stratum.
- Only 178 of 217 NEI tracts join. The unmatched ones are
  systematically the **newest suburbs** — Barrhaven-Rideaucrest, Avalon West —
  where 2021 census tract splits postdate the dissemination-area file. Current
  StatCan boundaries would close that gap.

## What would actually answer it

A service-completion timestamp, which the city does not publish; or a category
that is both geocoded and completion-closed, which none currently is. Worth
asking the city for — it is a small schema change that would make a real
accountability question answerable.

Regenerate: `python3 explorations/service_equity.py`

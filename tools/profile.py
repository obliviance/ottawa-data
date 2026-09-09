#!/usr/bin/env python3
"""Profile a warehouse dataset: write a one-page tearsheet to catalog/<id>.md and
append candidate questions to questions/backlog.csv.

    python3 tools/profile.py <dataset_id>
    python3 tools/profile.py --all
    python3 tools/profile.py --all --no-questions
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import warehouse  # noqa: E402

REPO = pathlib.Path(__file__).parent.parent
CATALOG = REPO / "catalog"
BACKLOG = REPO / "questions" / "backlog.csv"
BACKLOG_COLS = ["id", "question", "datasets", "join_type", "value", "feasibility",
                "novelty", "status", "added"]

SPARK = "▁▂▃▄▅▆▇█"
WARDISH = re.compile(r"\b(ward|quartier|neighbourhood|neighborhood|voisinage|community|"
                     r"communaut|hood|onsid|da_?id|census|recensement|dissemination|geo|"
                     r"secteur|area_name|region|région)\b", re.I)
ENTITYISH = re.compile(r"\b(name|nom|company|entreprise|soci[ée]t[ée]|vendor|fournisseur|"
                       r"supplier|firm|applicant|requérant|owner|propri[ée]taire|lobbyist|"
                       r"lobbyiste|organization|organisation|organisme|contractor|client|"
                       r"employer|employeur)\b", re.I)
DATEISH = re.compile(r"(date|time|year|ann[ée]e|_dt|timestamp|created|updated|issued|"
                     r"re[çc]u|received|d[ée]but|fin)", re.I)


def sparkline(series, bins: int = 16) -> str:
    import pandas as pd
    s = pd.to_numeric(series, errors="coerce").dropna()
    if s.nunique() < 2:
        return ""
    counts = pd.cut(s, bins=bins).value_counts(sort=False).to_numpy()
    hi = counts.max() or 1
    return "".join(SPARK[min(len(SPARK) - 1, int(c / hi * (len(SPARK) - 1)))] for c in counts)


def col_summary(name: str, s) -> tuple[str, int, int, str]:
    """(type label, non-null %, distinct, one-line summary)."""
    import pandas as pd
    n = len(s)
    nonnull = int(s.notna().sum())
    distinct = int(s.nunique(dropna=True))
    pct = f"{100 * nonnull // n if n else 0}%"

    num = pd.to_numeric(s, errors="coerce")
    is_num = num.notna().sum() >= 0.9 * max(nonnull, 1) and nonnull
    year_like = is_num and num.dropna().between(1850, 2100).all() and (num.dropna() % 1 == 0).all()
    parsed_dt = None
    if not year_like and (DATEISH.search(name) or str(s.dtype).startswith("datetime")):
        parsed_dt = pd.to_datetime(s, errors="coerce", format="mixed")
        if parsed_dt.notna().sum() < 0.5 * max(nonnull, 1):
            parsed_dt = None

    if parsed_dt is not None and parsed_dt.notna().any():
        lo, hi = parsed_dt.min(), parsed_dt.max()
        days = parsed_dt.dropna().sort_values()
        gaps = int((days.diff().dt.days.fillna(0) > 30).sum())
        return ("date", pct, distinct,
                f"{lo:%Y-%m-%d} → {hi:%Y-%m-%d}" + (f", {gaps} gaps >30d" if gaps else ""))
    if is_num and not (parsed_dt is not None):
        q = num.quantile([0, .25, .5, .95, 1]).tolist()
        fmt = (lambda v: f"{v:,.0f}" if abs(v) >= 100 else f"{v:,.2f}")
        return ("num", pct, distinct,
                f"{fmt(q[0])} · p25 {fmt(q[1])} · p50 {fmt(q[2])} · p95 {fmt(q[3])} · "
                f"max {fmt(q[4])}  {sparkline(num)}")
    if distinct <= 25 and distinct:
        vc = s.value_counts(normalize=True).head(6)
        top = ", ".join(f"{str(k)[:24]} {v:.0%}" for k, v in vc.items())
        return ("cat", pct, distinct, top)
    ex = ", ".join(str(x)[:22] for x in s.dropna().unique()[:3])
    kind = "id/text" if distinct > 0.8 * max(nonnull, 1) else "text"
    return (kind, pct, distinct, f"e.g. {ex}")


def tearsheet(did: str, meta: dict) -> list[str]:
    import pandas as pd
    df = pd.read_parquet(warehouse.WH / meta["parquet"])
    rows = [
        f"# {meta['title']}", "",
        f"`{did}` · shape **{meta['shape']}**"
        + (f" · source `{meta['source_id']}`" if meta.get("source_id") else "")
        + (f" · **spatial**" if meta.get("spatial") else ""),
        "",
        f"- origin: <{meta['origin_url']}>" if meta.get("origin_url") else "- origin: —",
        f"- fetched {meta['fetched_at'][:10]} · **{len(df):,} rows** · {len(df.columns)} columns",
    ]
    if meta.get("notes"):
        rows.append(f"- {meta['notes']}")
    rows += ["", "## Columns", "",
             "| column | kind | non-null | distinct | summary |",
             "| --- | --- | --- | --- | --- |"]
    for c in df.columns:
        kind, pct, distinct, summ = col_summary(c, df[c])
        rows.append(f"| `{c}` | {kind} | {pct} | {distinct:,} | {summ} |")
    qs = questions_for(did, df)
    rows += ["", "## Candidate questions", ""]
    rows += [f"- {q}" for q in qs] or ["- (none templated)"]
    rows += ["", f"_profiled {dt.date.today()} · `python3 tools/profile.py {did}`_", ""]
    return rows


def questions_for(did: str, df) -> list[str]:
    cols = list(df.columns)
    ward = next((c for c in cols if WARDISH.search(c)), None)
    ent = next((c for c in cols if ENTITYISH.search(c)), None)
    date = next((c for c in cols if DATEISH.search(c)), None)
    import pandas as pd
    nums = [c for c in cols if pd.to_numeric(df[c], errors="coerce").notna().mean() > 0.8
            and df[c].nunique() > 8 and not DATEISH.search(c)]
    out = []
    if ward and nums:
        out.append(f"Distribution of `{nums[0]}` across `{ward}` — is there an equity gradient? "
                   f"(join to ONS neighbourhood income)")
    if date and len(df) > 100:
        out.append(f"Trend and seasonality of {did} over `{date}`; any structural break?")
    if df.attrs.get("spatial") or {"latitude", "longitude"} <= set(c.lower() for c in cols):
        out.append(f"Spatial clustering of {did}; overlay ward geography and the decision timeline")
    if ent:
        out.append(f"Concentration in `{ent}` — which entities dominate? (join to the entity spine: "
                   f"lobbyists, contributors, applicants, contract winners)")
    out.append(f"Negative space — which wards / streets / periods have **zero** {did} rows, and why?")
    return out


def append_questions(did: str, questions: list[str]) -> int:
    BACKLOG.parent.mkdir(exist_ok=True)
    existing = []
    if BACKLOG.exists():
        existing = list(csv.DictReader(BACKLOG.open()))
    seen = {(r["question"], r["datasets"]) for r in existing}
    nextnum = 1 + max((int(re.sub(r"\D", "", r["id"]) or 0) for r in existing), default=0)
    added = 0
    with BACKLOG.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=BACKLOG_COLS)
        w.writeheader()
        w.writerows(existing)
        for q in questions:
            if (q, did) in seen:
                continue
            w.writerow({"id": f"q{nextnum:04d}", "question": q, "datasets": did,
                        "join_type": "", "value": "", "feasibility": "", "novelty": "",
                        "status": "new", "added": dt.date.today().isoformat()})
            nextnum += 1
            added += 1
    return added


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("dataset_id", nargs="?")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--no-questions", action="store_true")
    a = ap.parse_args()

    m = warehouse._load_manifest()["datasets"]
    if not m:
        sys.exit("warehouse is empty — run an ingester first")
    targets = list(m) if a.all else [a.dataset_id]
    if not a.all and (not a.dataset_id or a.dataset_id not in m):
        sys.exit(f"unknown dataset_id. Have: {', '.join(sorted(m))}")

    CATALOG.mkdir(exist_ok=True)
    total_q = 0
    for did in targets:
        import pandas as pd
        df = pd.read_parquet(warehouse.WH / m[did]["parquet"])
        (CATALOG / f"{did}.md").write_text("\n".join(tearsheet(did, m[did])))
        if not a.no_questions:
            total_q += append_questions(did, questions_for(did, df))
        print(f"  catalog/{did}.md")
    if not a.no_questions:
        print(f"\n+{total_q} questions → {BACKLOG.relative_to(REPO)}")


if __name__ == "__main__":
    main()

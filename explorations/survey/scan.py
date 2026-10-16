#!/usr/bin/env python3
"""Per-dataset statistical anomaly scan over warehouse/*.parquet -> survey/scan.csv"""
import pathlib, sys, csv, warnings
import pandas as pd
warnings.filterwarnings("ignore")
WH = pathlib.Path(__file__).resolve().parents[2] / "warehouse"
out = []
for p in sorted(WH.glob("*.parquet")):
    try:
        df = pd.read_parquet(p)
    except Exception as e:
        out.append((p.stem, 0, f"UNREADABLE: {e}"[:120])); continue
    flags = []
    n = len(df)
    if n == 0: flags.append("empty")
    else:
        if n <= 50: flags.append(f"tiny({n})")
        try:
            dup = int(df.astype(str).duplicated().sum())
            if dup / n > 0.02: flags.append(f"dup_rows={dup} ({dup/n:.0%})")
        except Exception: pass
        for c in df.columns:
            s = df[c]
            nn = s.isna().mean() + (s.astype(str).isin(["", "None", "nan", "\\N"]).mean() if s.dtype == object else 0)
            if nn > 0.95 and n > 20: flags.append(f"mostly_null:{str(c)[:25]}")
            if s.dtype.kind in "M" or any(k in str(c).lower() for k in ("date", "time", "opened", "closed", "created")):
                try:
                    d = pd.to_datetime(s, errors="coerce", utc=True).dropna()
                    if len(d):
                        if d.max() > pd.Timestamp.now(tz="UTC") + pd.Timedelta(days=366): flags.append(f"future_date:{str(c)[:20]}={d.max().date()}")
                        if d.min().year < 1900: flags.append(f"ancient_date:{str(c)[:20]}={d.min().date()}")
                except Exception: pass
    out.append((p.stem, n, "; ".join(flags[:6])))
with open(pathlib.Path(__file__).parent / "scan.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["dataset", "rows", "flags"]); w.writerows(out)
print(len(out), "datasets;", sum(1 for o in out if o[2]), "flagged")

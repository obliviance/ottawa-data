#!/usr/bin/env python3
"""Ingest Ontario Financial Information Returns (FIR) from the EFIS multi-year bulk zips.

    python3 tools/ingest/fir.py                       # Ottawa + peer cities, 2000-latest
    python3 tools/ingest/fir.py --year 2025 --all     # every municipality for one year

Why not CKAN: the data.ontario.ca FIR resource is an HTML index page and its datastore holds that
page as a one-column table (survey 2026-10-16). The real data is
`https://efis.fma.csc.gov.on.ca/fir/MultiYearReport/fir_data_<year>.zip` (2000 onward; each zip
holds one long-format CSV, ~495k rows / 317 municipalities per year, 143 MB unzipped). Columns:
MARSYEAR, MUNICIPALITY_DESC, MUNID, SCHEDULE_DESC, SUB_SCHEDULE_DESC, SCHEDULE_LINE_DESC,
SCHEDULE_COLUMN_DESC, SLC (schedule-line-column code), DATATYPE_DESC, AMOUNT, VALUE_TEXT.

Default keeps Ottawa and a fixed peer set (large Ontario single- and upper-tier cities) so the
benchmarking the catalogue promises works without 12M rows; --all keeps every municipality.
Registers one table per year, `fir_<year>`. 1977-1999 are not in this bulk set.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import io
import pathlib
import re
import sys
import tempfile
import zipfile

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
import warehouse  # noqa: E402
from _http import download  # noqa: E402

URL = "https://efis.fma.csc.gov.on.ca/fir/MultiYearReport/fir_data_{year}.zip"
PEERS = re.compile(r"^(Ottawa|Toronto|Hamilton|London|Windsor|Greater Sudbury|Kingston|Brampton|"
                   r"Mississauga|Markham|Vaughan|Barrie|Guelph|Waterloo R|Peel R|York R|Halton R|Durham R)\b", re.I)


def main() -> None:
    import pandas as pd

    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--year", type=int, action="append")
    ap.add_argument("--all", action="store_true", help="keep every municipality")
    a = ap.parse_args()

    years = a.year or range(2000, dt.date.today().year + 1)
    for year in years:
        with tempfile.TemporaryDirectory() as td:
            zp = pathlib.Path(td) / "f.zip"
            try:
                download(URL.format(year=year), zp, max_bytes=int(3e8))
            except Exception as e:  # noqa: BLE001
                print(f"  {year}: {type(e).__name__} (not published yet?)")
                continue
            parts = []
            with zipfile.ZipFile(zp) as z:
                name = next(n for n in z.namelist() if n.lower().endswith(".csv"))
                with z.open(name) as f:
                    rdr = csv.reader(io.TextIOWrapper(f, encoding="utf-8-sig", errors="replace"))
                    header = [c.strip() for c in next(rdr)]
                    ncol, muni = len(header), header.index("MUNICIPALITY_DESC")
                    buf, fixed = [], 0
                    for row in rdr:
                        if len(row) > ncol:  # unquoted comma in the free-text last field: rejoin
                            row = row[:ncol - 1] + [",".join(row[ncol - 1:])]
                            fixed += 1
                        elif len(row) < ncol:
                            row = row + [""] * (ncol - len(row))
                        if a.all or PEERS.match(row[muni].strip()):
                            buf.append(row)
                    if fixed:
                        print(f"  {year}: rejoined {fixed:,} rows with unquoted commas in VALUE_TEXT")
                    parts.append(pd.DataFrame(buf, columns=header, dtype=str).replace("", None))
        df = pd.concat(parts, ignore_index=True)
        df["MUNID"] = df["MUNID"].str.strip()
        df["AMOUNT"] = pd.to_numeric(df["AMOUNT"], errors="coerce")
        warehouse.register(f"fir_{year}", df, source_id="fir", shape="html",
                           title=f"Ontario Financial Information Return {year} "
                                 f"({'all municipalities' if a.all else 'Ottawa + peer cities'})",
                           origin_url=URL.format(year=year),
                           notes="EFIS multi-year long-format CSV; AMOUNT numeric, text answers in VALUE_TEXT")


if __name__ == "__main__":
    main()

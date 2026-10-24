#!/usr/bin/env python3
"""Ingest the Ontario Public Sector Salary Disclosure ("Sunshine List") for 2021-2025.

    python3 tools/ingest/sunshine.py                # all years in the manifest
    python3 tools/ingest/sunshine.py --year 2025

`ckan.py` stops at 2020: data.ontario.ca CKAN holds 1996-2020 only. From 2021 the files are
on ontario.ca itself, indexed by an artefact manifest
`https://www.ontario.ca/public-sector-salary-disclosure_artifacts/pssdfiles.json`
({year: {Compendium|Addendum|NoSalary: {en|fr: {csv|json|ods: path}}}}). Files are re-issued
with a new date and GUID in the path, so the manifest is read every run rather than any path
being hard-coded. This lands the English CSV of each year's Compendium (salaries as first
disclosed) and Addendum (late or corrected disclosures; 2025 has none yet) as one table
`ontario_sunshine_<year>` with a `kind` column. NoSalary (employers disclosing no salary
rows) is skipped. All employers are kept - filter `Employer` for the City of Ottawa
(5,181 rows in 2025), OPS, OCH, school boards and hospitals. Salary-and-benefits columns are
text with `$` and commas in the source; `salary_paid` / `taxable_benefits` are numeric parses.
"""
from __future__ import annotations

import argparse
import pathlib
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
import warehouse  # noqa: E402
from _http import download, get_json  # noqa: E402

BASE = "https://www.ontario.ca"
MANIFEST = BASE + "/public-sector-salary-disclosure_artifacts/pssdfiles.json"


def _num(series):
    import pandas as pd
    return pd.to_numeric(series.astype(str).str.replace(r"[^0-9.\-]", "", regex=True), errors="coerce")


def main() -> None:
    import pandas as pd

    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--year", type=int, action="append")
    a = ap.parse_args()

    man = get_json(MANIFEST)
    for year in sorted(man):
        if a.year and int(year) not in a.year:
            continue
        frames = []
        for kind in ("Compendium", "Addendum"):
            path = man[year].get(kind, {}).get("en", {}).get("csv")
            if not path:
                continue
            with tempfile.TemporaryDirectory() as td:
                dest = pathlib.Path(td) / "f.csv"
                download(BASE + path, dest, max_bytes=int(5e8))
                df = pd.read_csv(dest, low_memory=False, encoding="utf-8-sig", dtype=str)
            df["kind"] = kind.lower()
            df["source_file"] = path.rsplit("/", 1)[-1]
            frames.append(df)
        if not frames:
            print(f"  {year}: no English CSV in manifest")
            continue
        out = pd.concat(frames, ignore_index=True)
        out.columns = [c.strip() for c in out.columns]
        # Column names differ by year ("Salary Paid" / "Salary", "Taxable Benefits" / "Benefits").
        sal = next((c for c in out.columns if c.lower().startswith("salary")), None)
        ben = next((c for c in out.columns if "benefit" in c.lower()), None)
        if sal:
            out["salary_paid"] = _num(out[sal])
        if ben:
            out["taxable_benefits"] = _num(out[ben])
        out["disclosure_year"] = int(year)  # not `year`: the source already has a Year column
        warehouse.register(f"ontario_sunshine_{year}", out, source_id="sunshine-list", shape="html",
                           title=f"Ontario Public Sector Salary Disclosure {year}",
                           origin_url="https://www.ontario.ca/page/public-sector-salary-disclosure",
                           notes="English CSV of Compendium + Addendum from ontario.ca artefact manifest; "
                                 "all employers; salary_paid / taxable_benefits parsed numeric")


if __name__ == "__main__":
    main()

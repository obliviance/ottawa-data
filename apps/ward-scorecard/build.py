#!/usr/bin/env python3
"""Inline releases/ward-scorecard/scorecard.json into template.html -> index.html.

The page carries its data rather than fetching it: an artifact is a single file,
and a voter guide that breaks when a host goes away is worse than useless. Run
`explorations/ward_scorecard.py` first, then this.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).parent
DATA = HERE.parent.parent / "releases" / "ward-scorecard" / "scorecard.json"

payload = json.loads(DATA.read_text())
# Compact: 24 wards of nested candidate records is the bulk of the page weight.
blob = json.dumps(payload, separators=(",", ":"), ensure_ascii=False)
# </script> inside a JSON string would close the block early.
blob = blob.replace("</", "<\\/")

html = (HERE / "template.html").read_text().replace("__DATA__", blob)
(HERE / "index.html").write_text(html)
print(f"index.html — {len(html):,} bytes ({len(blob):,} of data, "
      f"{len(payload['wards'])} wards, "
      f"{sum(len(w['candidates']) for w in payload['wards'])} councillor candidates)")

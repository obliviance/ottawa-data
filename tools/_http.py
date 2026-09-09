"""Small shared HTTP helpers for the ingest + profile scripts. Stdlib only.

Polite by default: a descriptive User-Agent, one retry on a transient failure, and a
caller-controlled delay. Not for high-volume scraping - that's a per-source decision
to make with the site's terms in view (see tools/VERIFYING.md)."""
from __future__ import annotations

import gzip
import json
import pathlib
import time
import urllib.error
import urllib.request

UA = "ottawa-data/0.1 (+https://github.com/obliviance/ottawa-data; catalogue exploration)"
TIMEOUT = 60


def _open(url: str, timeout: int = TIMEOUT):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    return urllib.request.urlopen(req, timeout=timeout)


def get(url: str, *, retries: int = 2, backoff: float = 3.0) -> bytes:
    """GET url, return the (decompressed) body. Raises on final failure."""
    last = None
    for attempt in range(retries + 1):
        try:
            with _open(url) as r:
                body = r.read()
                if r.headers.get("Content-Encoding", "").lower() == "gzip":
                    body = gzip.decompress(body)
                return body
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, OSError) as e:
            last = e
            code = getattr(e, "code", None)
            if code and code not in (429, 500, 502, 503, 504):
                raise
            if attempt < retries:
                time.sleep(backoff * (attempt + 1))
    raise last


def get_json(url: str, **kw):
    return json.loads(get(url, **kw).decode("utf-8", "replace"))


def download(url: str, dest: pathlib.Path, *, retries: int = 2, backoff: float = 3.0) -> pathlib.Path:
    """Stream url to dest. Returns dest."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    last = None
    for attempt in range(retries + 1):
        try:
            with _open(url) as r, open(dest, "wb") as f:
                while chunk := r.read(1 << 16):
                    f.write(chunk)
            return dest
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, OSError) as e:
            last = e
            code = getattr(e, "code", None)
            if code and code not in (429, 500, 502, 503, 504):
                raise
            if attempt < retries:
                time.sleep(backoff * (attempt + 1))
    raise last

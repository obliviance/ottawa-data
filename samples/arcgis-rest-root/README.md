# sample — City ArcGIS REST services root

- source id `arcgis-rest-root` · catalogue access `['api', 'bulk']` · operator *City of Ottawa*
- url <https://maps.ottawa.ca/arcgis/rest/services/>
- captured: `page.html`
- headless render: 2,677 chars, no backing data API

**Sample status:** landing page only — data is one navigation step deeper

**A full parser needs:**

the raw MapServer directory — crawl /rest/services?f=json recursively; this is the ingest path for anything spatial not on the Hub.

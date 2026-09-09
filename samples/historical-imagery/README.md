# sample — Historical aerial imagery and mapping

- source id `historical-imagery` · catalogue access `['html', 'api']` · operator *City of Ottawa / university libraries*
- url <https://maps.ottawa.ca/geoottawa/>
- captured: `page.html`
- headless render: 3,492 chars, 20 data XHR
- backing endpoints seen: `https://maps.ottawa.ca/arcgis/rest/services/Basemap_Ottawa/MapServer?f=json`; `https://tiles.arcgis.com/tiles/G6F8XLCl5KtAlZ2G/arcgis/rest/services/Canopy/VectorTileServ`; `https://tiles.arcgis.com/tiles/G6F8XLCl5KtAlZ2G/arcgis/rest/services/Tree_Canopy_2022_Exte`

**Sample status:** landing page only — data is one navigation step deeper

**A full parser needs:**

air-photo layers in the geoOttawa viewer (ArcGIS services under maps.ottawa.ca/arcgis).

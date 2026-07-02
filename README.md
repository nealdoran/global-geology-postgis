# Global Land Surface Exposure by Geologic Period

A PostGIS spatial analysis combining two USGS datasets to quantify what fraction 
of Earth's land surface exposes rocks from each geologic period.

## Data Sources
- USGS World Energy Project Geology Tiles (OFR 97-470, 14 regional tiles)
- USGS State Geologic Map Compilation (SGMC, Data Series 1052)
- Total mapped area: 148.3M km² (99.6% of global land reference)

## Method
Shapefiles were harmonized in Google Colab (Python/GeoPandas), crosswalked to 
ICS 2023 period definitions, reprojected to EPSG:8857 (Equal Earth equal-area), 
and loaded into a PostGIS database. Surface area fractions were computed with 
a single SQL GROUP BY query.

## Key Query
```sql
SELECT 
  CASE WHEN period IN ('Pleistocene','Holocene') THEN 'Quaternary' 
       ELSE period END AS period,
  ROUND(SUM(area_km2)::numeric/148335381*100, 2) AS pct_surface
FROM surface_polygons_attributes
WHERE period NOT IN ('Cenozoic','Mesozoic','Paleozoic','Precambrian',
                     'Tertiary','multi','UNMAPPED','no-age')
GROUP BY 1
ORDER BY pct_surface DESC;
```

## Key Finding
Quaternary sediments blanket 17.9% of global land — more than any other period. 
Cretaceous rocks are second at 11.8%, reflecting widespread marine carbonate 
deposition. The Triassic (6.0%) outpaces the Jurassic (2.9%), a pattern driven 
by large continental interior basins--something worth further investigation.

## Tools
- Python, GeoPandas, pyogrio, shapely
- PostgreSQL 18 + PostGIS
- matplotlib

## Files
- `query.sql` — PostGIS query
- `make_chart_final.py` — figure generation script
- `surface_by_period_final.csv` — output data
- `surface_by_period_final.png` — figure

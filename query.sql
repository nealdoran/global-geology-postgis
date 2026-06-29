-- Global Land Surface Exposure by Geologic Period
-- Source: USGS World Energy Geology Tiles + SGMC (148.3M km2)
-- Database: PostgreSQL + PostGIS

SELECT 
  CASE WHEN period IN ('Pleistocene','Holocene') THEN 'Quaternary' 
       ELSE period END AS period,
  ROUND(SUM(area_km2)::numeric/148335381*100, 2) AS pct_surface
FROM surface_polygons_attributes
WHERE period NOT IN ('Cenozoic','Mesozoic','Paleozoic','Precambrian',
                     'Tertiary','multi','UNMAPPED','no-age')
GROUP BY 1
ORDER BY pct_surface DESC;

import geoarrow.pyarrow as ga
import geoarrow.pyarrow.io as io

table = io.read_geoparquet_table('data/random.parquet')
print(table)
print(ga.format_wkt(table["geometry"])[:5])

# Geodata Frame
gdf = ga.to_geopandas(table)
print(gdf)

# Geodata Frame to GeoJSON file
gdf.to_file('data/random.geojson', driver='GeoJSON')

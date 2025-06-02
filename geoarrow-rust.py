from geoarrow.rust.io import read_parquet, write_parquet

table = read_parquet("data/random-write.parquet")
print(table)

# Write with default GeoParquetEncoding.WKB
write_parquet(table, 'data/random-write.parquet')


# url = "https://raw.githubusercontent.com/opengeospatial/geoparquet/v1.0.0/examples/example.parquet"
# table = read_parquet(url)
# print(table)

# Read by bounding box from remote Parquet file
# from geoarrow.rust.io import ParquetFile, ObjectStore
from geoarrow.rust.io import ParquetDataset
from geoarrow.rust.io.store import S3Store
import requests

# options = {
# }
# store = ObjectStore('s3://overturemaps-us-west-2/release/2025-05-21.0', options=options)
store = S3Store.from_url("s3://overturemaps-us-west-2", config={"SKIP_SIGNATURE": "True", "REGION": "us-west-2"})
print(store)
manifest_url = "https://raw.githubusercontent.com/OvertureMaps/explore-site/refs/heads/main/site/src/manifests/2025-04-23.json"
manifest = requests.get(manifest_url).json()
print(manifest)
# pf = ParquetFile('theme=base/type=place', store)
# print(pf)

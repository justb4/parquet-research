import pyarrow.parquet as pq
table = pq.read_table('data/random.parquet')
print(table)
ng_table = pq.read_table('data/random_nogeom.parquet')
print(ng_table)

df = table.to_pandas()
print(df)

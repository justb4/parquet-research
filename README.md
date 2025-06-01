# Parquet/GeoParquet Research

Some research using Python libs for arrow, geoarrow, and getting open data from [OvertureMaps](https://overturemaps.org/).

## Links

See 

* https://geoparquet.org/
* https://medium.com/radiant-earth-insights/interview-with-kyle-barron-on-geoarrow-and-geoparquet-and-the-future-of-geospatial-data-analysis-c4dd30864930
* https://medium.com/radiant-earth-insights/sharing-some-tools-for-working-with-geoparquet-fc5667b27373
* https://arrow.apache.org/docs/python/parquet.html#parquet
* https://github.com/geoarrow/geoarrow-python and https://geoarrow.org/geoarrow-python/main/index.html
* https://github.com/geopython/pygeoapi/tree/master/tests/data sample parquet (random_nogeom.parquet) and geoparquet (random.parquet) files
* https://github.com/cholmes/duckdb-geoparquet-tutorials
* https://github.com/OvertureMaps/overturemaps-py for downloading (GeoParquet) data from OvertureMaps on S3

## Environment and Deps
```
$ pyenv virtualenv 3.12.3 parquet
$ pyenv activate parquet

$ pip install -r requirements.txt 
# requirements.txt:
pandas
geopandas
numpy
pyarrow
geoarrow-pyarrow
overturemaps

$ pip freeze
certifi==2025.4.26
click==8.2.1
geoarrow-c==0.3.0
geoarrow-pyarrow==0.2.0
geoarrow-types==0.3.0
geopandas==1.0.1
numpy==2.2.6
overturemaps==0.14.0
packaging==25.0
pandas==2.2.3
pyarrow==20.0.0
pyogrio==0.11.0
pyproj==3.7.1
python-dateutil==2.9.0.post0
pytz==2025.2
shapely==2.1.1
six==1.17.0
tzdata==2025.2

```


## Parquet Read


```python
import pyarrow.parquet as pq
table = pq.read_table('data/random.parquet')
print(table)
ng_table = pq.read_table('data/random_nogeom.parquet')
print(ng_table)

df = table.to_pandas()
print(df)

```
Output:
```
pyarrow.Table
lat: double
lon: double
time: timestamp[us, tz=UTC]
geometry: binary
id: int64
----
lat: [[-58.017774,56.909984,60.63901,17.35044,-43.550597,...,-78.973024,-27.647392,-24.884741,-27.369171,38.167674]]
lon: [[114.386131,51.174536,106.214013,127.302361,119.844457,...,154.709904,167.550565,-35.324799,159.407139,-56.645312]]
time: [[2022-02-14 14:34:26.000000Z,2022-03-15 20:54:53.000000Z,2022-09-24 13:20:03.000000Z,2022-12-24 20:54:45.000000Z,2022-04-14 17:10:20.000000Z,...,2022-01-28 08:55:58.000000Z,2022-09-08 18:55:03.000000Z,2022-02-09 22:51:44.000000Z,2022-01-17 03:08:05.000000Z,2022-09-06 11:06:25.000000Z]]
geometry: [[0101000000323ECC5EB6985C400C5C1E6B46024DC0,0101000000C2FC1532579649400FF10F5B7A744C40,0101000000CEFA9463B28D5A4092E86514CB514E40,01010000007FA5F3E159D35F40D235936FB6593140,010100000036785F950BF65D404B2366F679C645C0,...,010100000096E99788B7566340478E740646BE53C0,010100000050AA7D3A9EF1644029B16B7BBBA53BC0,010100000002637D0393A941C02B6EDC627EE238C0,0101000000A33D5E4807ED6340B2A19BFD815E3BC0,0101000000B1DB679599524CC0DB31755776154340]]
id: [[1,2,3,4,5,...,96,97,98,99,100]]
pyarrow.Table
lat: double
lon: double
time: timestamp[us, tz=UTC]
id: int64
----
lat: [[-58.017774,56.909984,60.63901,17.35044,-43.550597,...,-78.973024,-27.647392,-24.884741,-27.369171,38.167674]]
lon: [[114.386131,51.174536,106.214013,127.302361,119.844457,...,154.709904,167.550565,-35.324799,159.407139,-56.645312]]
time: [[2022-02-14 14:34:26.000000Z,2022-03-15 20:54:53.000000Z,2022-09-24 13:20:03.000000Z,2022-12-24 20:54:45.000000Z,2022-04-14 17:10:20.000000Z,...,2022-01-28 08:55:58.000000Z,2022-09-08 18:55:03.000000Z,2022-02-09 22:51:44.000000Z,2022-01-17 03:08:05.000000Z,2022-09-06 11:06:25.000000Z]]
id: [[1,2,3,4,5,...,96,97,98,99,100]]
           lat         lon                      time                                           geometry
id                                                                                                     
1   -58.017774  114.386131 2022-02-14 14:34:26+00:00  b'\x01\x01\x00\x00\x002>\xcc^\xb6\x98\\@\x0c\\...
2    56.909984   51.174536 2022-03-15 20:54:53+00:00  b'\x01\x01\x00\x00\x00\xc2\xfc\x152W\x96I@\x0f...
3    60.639010  106.214013 2022-09-24 13:20:03+00:00  b'\x01\x01\x00\x00\x00\xce\xfa\x94c\xb2\x8dZ@\...
4    17.350440  127.302361 2022-12-24 20:54:45+00:00  b'\x01\x01\x00\x00\x00\x7f\xa5\xf3\xe1Y\xd3_@\...
5   -43.550597  119.844457 2022-04-14 17:10:20+00:00  b'\x01\x01\x00\x00\x006x_\x95\x0b\xf6]@K#f\xf6...
..         ...         ...                       ...                                                ...
96  -78.973024  154.709904 2022-01-28 08:55:58+00:00  b'\x01\x01\x00\x00\x00\x96\xe9\x97\x88\xb7Vc@G...
97  -27.647392  167.550565 2022-09-08 18:55:03+00:00  b'\x01\x01\x00\x00\x00P\xaa}:\x9e\xf1d@)\xb1k{...
98  -24.884741  -35.324799 2022-02-09 22:51:44+00:00  b'\x01\x01\x00\x00\x00\x02c}\x03\x93\xa9A\xc0+...
99  -27.369171  159.407139 2022-01-17 03:08:05+00:00  b'\x01\x01\x00\x00\x00\xa3=^H\x07\xedc@\xb2\xa...
100  38.167674  -56.645312 2022-09-06 11:06:25+00:00  b'\x01\x01\x00\x00\x00\xb1\xdbg\x95\x99RL\xc0\...

[100 rows x 4 columns]
```

## GeoParquet Read

```python
import geoarrow.pyarrow as ga
import geoarrow.pyarrow.io as io

table = io.read_geoparquet_table('data/random.parquet')
print(table)
print(ga.format_wkt(table["geometry"])[:5])

df = ga.to_geopandas(table)
print(df)

```

Output:

```
pyarrow.Table
lat: double
lon: double
time: timestamp[us, tz=UTC]
geometry: extension<geoarrow.wkb<WkbType>>
id: int64
----
lat: [[-58.017774,56.909984,60.63901,17.35044,-43.550597,...,-78.973024,-27.647392,-24.884741,-27.369171,38.167674]]
lon: [[114.386131,51.174536,106.214013,127.302361,119.844457,...,154.709904,167.550565,-35.324799,159.407139,-56.645312]]
time: [[2022-02-14 14:34:26.000000Z,2022-03-15 20:54:53.000000Z,2022-09-24 13:20:03.000000Z,2022-12-24 20:54:45.000000Z,2022-04-14 17:10:20.000000Z,...,2022-01-28 08:55:58.000000Z,2022-09-08 18:55:03.000000Z,2022-02-09 22:51:44.000000Z,2022-01-17 03:08:05.000000Z,2022-09-06 11:06:25.000000Z]]
geometry: [[0101000000323ECC5EB6985C400C5C1E6B46024DC0,0101000000C2FC1532579649400FF10F5B7A744C40,0101000000CEFA9463B28D5A4092E86514CB514E40,01010000007FA5F3E159D35F40D235936FB6593140,010100000036785F950BF65D404B2366F679C645C0,...,010100000096E99788B7566340478E740646BE53C0,010100000050AA7D3A9EF1644029B16B7BBBA53BC0,010100000002637D0393A941C02B6EDC627EE238C0,0101000000A33D5E4807ED6340B2A19BFD815E3BC0,0101000000B1DB679599524CC0DB31755776154340]]
id: [[1,2,3,4,5,...,96,97,98,99,100]]
[
  [
    "POINT (114.386131 -58.017774)",
    "POINT (51.174536 56.909984)",
    "POINT (106.214013 60.63901)",
    "POINT (127.302361 17.35044)",
    "POINT (119.844457 -43.550597)"
  ]
]
           lat         lon                      time                     geometry
id                                                                               
1   -58.017774  114.386131 2022-02-14 14:34:26+00:00  POINT (114.38613 -58.01777)
2    56.909984   51.174536 2022-03-15 20:54:53+00:00    POINT (51.17454 56.90998)
3    60.639010  106.214013 2022-09-24 13:20:03+00:00   POINT (106.21401 60.63901)
4    17.350440  127.302361 2022-12-24 20:54:45+00:00   POINT (127.30236 17.35044)
5   -43.550597  119.844457 2022-04-14 17:10:20+00:00   POINT (119.84446 -43.5506)
..         ...         ...                       ...                          ...
96  -78.973024  154.709904 2022-01-28 08:55:58+00:00   POINT (154.7099 -78.97302)
97  -27.647392  167.550565 2022-09-08 18:55:03+00:00  POINT (167.55056 -27.64739)
98  -24.884741  -35.324799 2022-02-09 22:51:44+00:00   POINT (-35.3248 -24.88474)
99  -27.369171  159.407139 2022-01-17 03:08:05+00:00  POINT (159.40714 -27.36917)
100  38.167674  -56.645312 2022-09-06 11:06:25+00:00   POINT (-56.64531 38.16767)

[100 rows x 4 columns]

```

## GeoParquet download from OvertureMaps

From: https://docs.overturemaps.org/getting-data/overturemaps-py/

Download Places in Mostar centre.
`bbox=17.800,43.345,17.810,43.350`

To help find bounding boxes of interest, we like this [bounding box tool](https://boundingbox.klokantech.com/)
from [Klokantech](https://www.klokantech.com/). Choose the CSV format and copy the value directly into
the `--bbox` field here.

```
overturemaps download --bbox=17.800,43.345,17.810,43.350 -f geojson --type=place -o data/mostar-places.geojson
overturemaps download --bbox=17.800,43.345,17.810,43.350 -f geoparquet --type=place -o data/mostar-places.geoparquet
```

Compare filesizes:

```
ls -lh data
total 608
-rw-r--r--  1 just  staff   176K Jun  1 17:00 mostar-places.geojson
-rw-r--r--  1 just  staff    63K Jun  1 17:08 mostar-places.geoparquet
```
Output:

```
{"type": "FeatureCollection", "features": [
{"type":"Feature","geometry":{"type":"Point","coordinates":[17.8004269,43.3460268]},"properties":{"id":"08f1ef6c2a4d5a0003f1d2da81c66057","type":"place","version":0,"sources":[{"property":"","dataset":"meta","record_id":"318314138289147","update_time":"2025-02-24T08:00:00.000Z","confidence":0.847457627118644}],"names":{"primary":"Martimex","common":null,"rules":null},"categories":{"primary":"beauty_salon","alternate":["hotel"]},"confidence":0.847457627118644,"socials":["https://www.facebook.com/318314138289147"],"phones":["+38736313630"],"addresses":[{"freeform":"Ulica Ferhadija 14a","locality":"Sarajevo","postcode":"71000","region":null,"country":"BA"}]}},
{"type":"Feature","geometry":{"type":"Point","coordinates":[17.8005039,43.346074]},"properties":{"id":"08f1ef6c2a4d5b1e0359fba47f59dd5e","type":"place","version":0,"sources":[{"property":"","dataset":"meta","record_id":"443187042370909","update_time":"2025-02-24T08:00:00.000Z","confidence":0.93596425912137}],"names":{"primary":"Prodajni Centar Mostar","common":null,"rules":null},"categories":{"primary":"shopping_center","alternate":["shopping","cafe"]},"confidence":0.93596425912137,"websites":["http://prodajnicentarmostar.com/"],"socials":["https://www.facebook.com/443187042370909"],"phones":["+38736326339"],"addresses":[{"freeform":"Ulica Stjepana Radi\u0107a 29","locality":"Mostar","postcode":"88000","region":null,"country":"BA"}]}},
{"type":"Feature","geometry":{"type":"Point","coordinates":[17.8004843,43.346183]},"properties":{"id":"08f1ef6c2a4c64ac0351bde6fefa816d","type":"place","version":0,"sources":[{"property":"","dataset":"meta","record_id":"335507720163212","update_time":"2025-02-24T08:00:00.000Z","confidence":0.31844029244516653}],"names":{"primary":"Butik Angels","common":null,"rules":null},"categories":{"primary":"women's_clothing_store","alternate":null},"confidence":0.3184402924451666,"socials":["https://www.facebook.com/335507720163212"],"phones":["+38736322360"],"addresses":[{"freeform":"Ulica Stjepana Radi\u0107a 29","locality":"Mostar","postcode":"88000","region":null,"country":"BA"}]}},
{"type":"Feature","geometry":{"type":"Point","coordinates":[17.8000666,43.3462614]},"properties":{"id":"08f1ef6c2a4f30f3030a056c9f933fc5","type":"place","version":0,"sources":[{"property":"","dataset":"meta","record_id":"560423634113731","update_time":"2025-02-24T08:00:00.000Z","confidence":0.9793990828827596}],"names":{"primary":"Song","common":null,"rules":null},"categories":{"primary":"cafe","alternate":["coffee_shop","bar"]},"confidence":0.9793990828827596,"socials":["https://www.facebook.com/560423634113731"],"phones":["+38736328404"],"addresses":[{"freeform":"Ulica Stjepana Radi\u0107a 29","locality":"Mostar","postcode":"88000","region":null,"country":"BA"}]}},
{"type":"Feature","geometry":{"type":"Point","coordinates":[17.8000366,43.3464389]},"properties":{"id":"08f1ef6c2a4f38c4033d7ac553e68b8f","type":"place","version":0,"sources":[{"property":"","dataset":"meta","record_id":"328265017504551","update_time":"2025-02-24T08:00:00.000Z","confidence":0.93596425912137}],"names":{"primary":"D.o.o Borsa","common":null,"rules":null},"categories":{"primary":"fashion","alternate":["bags_luggage_company","shoe_store"]},"confidence":0.93596425912137,"socials":["https://www.facebook.com/328265017504551"],"phones":["+38763314991"],"addresses":[{"freeform":"Ulica Stjepana Radi\u0107a 29","locality":"Mostar","postcode":"88000","region":null,"country":"BA"}]}},

```

```python
import geoarrow.pyarrow as ga
import geoarrow.pyarrow.io as io

table = io.read_geoparquet_table('data/mostar-places.geoparquet')
print(table)
print(ga.format_wkt(table["geometry"])[:5])

# Geodata Frame
gdf = ga.to_geopandas(table)
print(gdf)

```

Output

```
pyarrow.Table
id: string
geometry: extension<geoarrow.wkb<WkbType>>
bbox: struct<xmin: float, xmax: float, ymin: float, ymax: float> not null
  child 0, xmin: float
  child 1, xmax: float
  child 2, ymin: float
  child 3, ymax: float
type: string
version: int32
sources: list<element: struct<property: string, dataset: string, record_id: string, update_time: string, confidence: double>>
  child 0, element: struct<property: string, dataset: string, record_id: string, update_time: string, confidence: double>
      child 0, property: string
      child 1, dataset: string
      child 2, record_id: string
      child 3, update_time: string
      child 4, confidence: double
names: struct<primary: string, common: map<string, string ('common')>, rules: list<element: struct<variant: string, language: string, value: string, between: list<element: double>, side: string>>>
  child 0, primary: string
  child 1, common: map<string, string ('common')>
      child 0, common: struct<key: string not null, value: string> not null
          child 0, key: string not null
          child 1, value: string
  child 2, rules: list<element: struct<variant: string, language: string, value: string, between: list<element: double>, side: string>>
      child 0, element: struct<variant: string, language: string, value: string, between: list<element: double>, side: string>
          child 0, variant: string
          child 1, language: string
          child 2, value: string
          child 3, between: list<element: double>
              child 0, element: double
          child 4, side: string
categories: struct<primary: string, alternate: list<element: string>>
  child 0, primary: string
  child 1, alternate: list<element: string>
      child 0, element: string
confidence: double
websites: list<element: string>
  child 0, element: string
socials: list<element: string>
  child 0, element: string
emails: list<element: string>
  child 0, element: string
phones: list<element: string>
  child 0, element: string
brand: struct<wikidata: string, names: struct<primary: string, common: map<string, string ('common')>, rules: list<element: struct<variant: string, language: string, value: string, between: list<element: double>, side: string>>>>
  child 0, wikidata: string
  child 1, names: struct<primary: string, common: map<string, string ('common')>, rules: list<element: struct<variant: string, language: string, value: string, between: list<element: double>, side: string>>>
      child 0, primary: string
      child 1, common: map<string, string ('common')>
          child 0, common: struct<key: string not null, value: string> not null
              child 0, key: string not null
              child 1, value: string
      child 2, rules: list<element: struct<variant: string, language: string, value: string, between: list<element: double>, side: string>>
          child 0, element: struct<variant: string, language: string, value: string, between: list<element: double>, side: string>
              child 0, variant: string
              child 1, language: string
              child 2, value: string
              child 3, between: list<element: double>
                  child 0, element: double
              child 4, side: string
addresses: list<element: struct<freeform: string, locality: string, postcode: string, region: string, country: string>>
  child 0, element: struct<freeform: string, locality: string, postcode: string, region: string, country: string>
      child 0, freeform: string
      child 1, locality: string
      child 2, postcode: string
      child 3, region: string
      child 4, country: string
----
id: [["08f1ef6c2a4d5a0003f1d2da81c66057","08f1ef6c2a4d5b1e0359fba47f59dd5e","08f1ef6c2a4c64ac0351bde6fefa816d","08f1ef6c2a4f30f3030a056c9f933fc5","08f1ef6c2a4f38c4033d7ac553e68b8f",...,"08f1ef6c2a70a18d03e0ec19ab582939","08f1ef6c2a70a18d039fd852fc328c84","08f1ef6c2a70b4f203433c3dcdb62a90","08f1ef6c2a72b099039ac06592ef440f","08f1ef6c2a7280ca037033454be72a3a"]]
geometry: [[00000000014031CCE8C6FE56B34045AC4A9B2EC50F,00000000014031CCEDD2D6D2094045AC4C271FFF7A,00000000014031CCEC8A0176224045AC4FB97BB731,00000000014031CCD12A299F364045AC524B266F00,00000000014031CCCF32D89A604045AC581C20C7F7,...,00000000014031CF342EDBB59E4045AC9AFE1DA7B1,00000000014031CF342EDBB59E4045AC9AFE1DA7B1,00000000014031CF5624CFC3214045AC95A5EF1272,00000000014031CF4A5233A97B4045ACBF727136A4,00000000014031CF3B9354053B4045ACCCACEC5CB5]]
bbox: [
  -- is_valid: all not null
  -- child 0 type: float
[17.800426,17.8005,17.800484,17.800066,17.800034,...,17.80939,17.80939,17.809908,17.809725,17.8095]
  -- child 1 type: float
[17.800428,17.800505,17.800486,17.800068,17.800037,...,17.809393,17.809393,17.80991,17.809729,17.809504]
  -- child 2 type: float
[43.34602,43.346073,43.346176,43.34626,43.346436,...,43.348476,43.348476,43.348316,43.349586,43.349995]
  -- child 3 type: float
[43.346027,43.34608,43.346184,43.346268,43.34644,...,43.34848,43.34848,43.348324,43.349594,43.350002]]
type: [["place","place","place","place","place",...,"place","place","place","place","place"]]
version: [[0,0,0,0,0,...,0,0,0,0,0]]
sources: [[    -- is_valid: all not null
    -- child 0 type: string
[""]
    -- child 1 type: string
["meta"]
    -- child 2 type: string
["318314138289147"]
    -- child 3 type: string
["2025-02-24T08:00:00.000Z"]
    -- child 4 type: double
[0.847457627118644],    -- is_valid: all not null
    -- child 0 type: string
[""]
    -- child 1 type: string
["meta"]
    -- child 2 type: string
["443187042370909"]
    -- child 3 type: string
["2025-02-24T08:00:00.000Z"]
    -- child 4 type: double
[0.93596425912137],...,    -- is_valid: all not null
    -- child 0 type: string
[""]
    -- child 1 type: string
["meta"]
    -- child 2 type: string
["206524672718343"]
    -- child 3 type: string
["2025-02-24T08:00:00.000Z"]
    -- child 4 type: double
[0.93596425912137],    -- is_valid: all not null
    -- child 0 type: string
[""]
    -- child 1 type: string
["meta"]
    -- child 2 type: string
["118164691613332"]
    -- child 3 type: string
["2025-02-24T08:00:00.000Z"]
    -- child 4 type: double
[0.9233926128590971]]]
names: [
  -- is_valid: all not null
  -- child 0 type: string
["Martimex","Prodajni Centar Mostar","Butik Angels","Song","D.o.o Borsa",...,"Dental clinic Pinjić","Apartments Nera","Media Forte d.o.o","Daleka obala","Gradski bazen"]
  -- child 1 type: map<string, string ('common')>
[null,null,null,null,null,...,null,null,null,null,null]
  -- child 2 type: list<element: struct<variant: string, language: string, value: string, between: list<element: double>, side: string>>
[null,null,...,null,null]]
categories: [
  -- is_valid: all not null
  -- child 0 type: string
["beauty_salon","shopping_center","women's_clothing_store","cafe","fashion",...,"dentist","service_apartments","marketing_agency","dance_club","swimming_pool"]
  -- child 1 type: list<element: string>
[["hotel"],["shopping","cafe"],...,["swimming_pool","lounge"],["pool_cleaning","stadium_arena"]]]
confidence: [[0.847457627118644,0.93596425912137,0.3184402924451666,0.9793990828827596,0.93596425912137,...,0.9793990828827596,0.8770555990602976,0.8770555990602976,0.93596425912137,0.9233926128590971]]
websites: [[null,["http://prodajnicentarmostar.com/"],...,null,null]]
...
[
  [
    "POINT (17.8004269 43.3460268)",
    "POINT (17.8005039 43.346074)",
    "POINT (17.8004843 43.346183)",
    "POINT (17.8000666 43.3462614)",
    "POINT (17.8000366 43.3464389)"
  ]
]
                                   id                   geometry                                               bbox   type  ...  emails          phones brand                                          addresses
0    08f1ef6c2a4d5a0003f1d2da81c66057  POINT (17.80043 43.34603)  {'xmin': 17.800426483154297, 'xmax': 17.800428...  place  ...    None  [+38736313630]  None  [{'freeform': 'Ulica Ferhadija 14a', 'locality...
1    08f1ef6c2a4d5b1e0359fba47f59dd5e   POINT (17.8005 43.34607)  {'xmin': 17.800500869750977, 'xmax': 17.800504...  place  ...    None  [+38736326339]  None  [{'freeform': 'Ulica Stjepana Radića 29', 'loc...
2    08f1ef6c2a4c64ac0351bde6fefa816d  POINT (17.80048 43.34618)  {'xmin': 17.80048370361328, 'xmax': 17.8004856...  place  ...    None  [+38736322360]  None  [{'freeform': 'Ulica Stjepana Radića 29', 'loc...
3    08f1ef6c2a4f30f3030a056c9f933fc5  POINT (17.80007 43.34626)  {'xmin': 17.800065994262695, 'xmax': 17.800067...  place  ...    None  [+38736328404]  None  [{'freeform': 'Ulica Stjepana Radića 29', 'loc...
4    08f1ef6c2a4f38c4033d7ac553e68b8f  POINT (17.80004 43.34644)  {'xmin': 17.800033569335938, 'xmax': 17.800037...  place  ...    None  [+38763314991]  None  [{'freeform': 'Ulica Stjepana Radića 29', 'loc...
..                                ...                        ...                                                ...    ...  ...     ...             ...   ...                                                ...
245  08f1ef6c2a70a18d03e0ec19ab582939  POINT (17.80939 43.34848)  {'xmin': 17.809389114379883, 'xmax': 17.809392...  place  ...    None  [+38736313600]  None  [{'freeform': 'Ulica Kardinala Stepinca 12', '...
246  08f1ef6c2a70a18d039fd852fc328c84  POINT (17.80939 43.34848)  {'xmin': 17.809389114379883, 'xmax': 17.809392...  place  ...    None  [+38761491504]  None  [{'freeform': 'Ulica Kardinala Stepinca 12', '...
247  08f1ef6c2a70b4f203433c3dcdb62a90  POINT (17.80991 43.34832)  {'xmin': 17.809907913208008, 'xmax': 17.809909...  place  ...    None  [+38763173520]  None  [{'freeform': 'Ulica Kardinala Stepinca 12', '...
248  08f1ef6c2a72b099039ac06592ef440f  POINT (17.80973 43.34959)  {'xmin': 17.809724807739258, 'xmax': 17.809728...  place  ...    None  [+38763178888]  None  [{'freeform': 'Dr. Mile Budaka', 'locality': N...
249  08f1ef6c2a7280ca037033454be72a3a      POINT (17.8095 43.35)  {'xmin': 17.809499740600586, 'xmax': 17.809503...  place  ...    None  [+38763178888]  None  [{'freeform': 'Dr. Mile Budaka bb', 'locality'...

[250 rows x 15 columns]
/Users/just/.pyenv/versions/parquet/lib/python3.12/site-packages/pyogrio/geopandas.py:710: UserWarning: 'crs' was not provided.  The output dataset will not have projection information defined and may not be usable in other systems.
  write(

```

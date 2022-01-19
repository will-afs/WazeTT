from geopandas import read_file
from shapefile import (Reader, Writer)
from io import BytesIO as IO

# Path to the Shapefile
shapefile_name = "HAIE"

# Display the shapefile in GeoJson format
try:
    f = read_file(shapefile_name+'.shp')
except :
    with IO() as shpio, IO() as dbfio:  # Don't overwrite existing .shp, .dbf
        with Reader(shapefile_name) as r, Writer(shp=shpio, dbf=dbfio, shx=shapefile_name+'.shx') as w:
            w.fields = r.fields[1:]  # skip first deletion field
            for rec in r.iterShapeRecords():
                w.record(*rec.record)
                w.shape(rec.shape)
    w.close()
    f = read_file(shapefile_name+'.shp')

#print(f)

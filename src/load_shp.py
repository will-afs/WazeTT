import shapefile
from geopandas import read_file

# Path to the Shapefile
shapefile_name = 'HAIE.shp'

# Display the element of the Shapefile
# r = shapefile.Reader(shapefile_name)

# Display the shapefile in GeoJson format
f = read_file(shapefile_name)

#print(f)
"""
        Get Shapefile bounding box coordinates (WGS84 coordinates system (lat, long))
"""

shapefile_dir_path = '/home/william/Programming/WazeTT/data/input/bd_topo/ZONE_VEGETATION/' # '/home/bertrand/Documents/Projet Indus/WazeTT/data/input/bd_topo/'
shapefile_name = 'ZONE_VEGETATION.shp'
shapefile_path = shapefile_dir_path + shapefile_name

# xml_path = gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox
import xml.etree.ElementTree as ET
metadata_file_name = 'metadonnees.xml'
tree = ET.parse(shapefile_dir_path + metadata_file_name)
root = tree.getroot()

namespaces = {
                'gmd': '{http://www.isotc211.org/2005/gmd}',
                'gco': '{http://www.isotc211.org/2005/gco}'
            } # add more as needed

EX_GeographicBoundingBox_element = list(root.iter(namespaces['gmd']+'EX_GeographicBoundingBox'))[0]

west_bound_longitude_element = list(EX_GeographicBoundingBox_element.iter(namespaces['gmd']+'westBoundLongitude'))[0]
west_bound_longitude_decimal_element = list(west_bound_longitude_element.iter(namespaces['gco']+'Decimal'))[0]
west_bound_longitude_decimal_value = list(west_bound_longitude_decimal_element.itertext())[0]
print('west_bound_longitude_decimal_value : {}'.format(west_bound_longitude_decimal_value))

east_bound_longitude_element = list(EX_GeographicBoundingBox_element.iter(namespaces['gmd']+'eastBoundLongitude'))[0]
east_bound_longitude_decimal_element = list(east_bound_longitude_element.iter(namespaces['gco']+'Decimal'))[0]
east_bound_longitude_decimal_value = list(east_bound_longitude_decimal_element.itertext())[0]
print('east_bound_longitude_decimal_value : {}'.format(east_bound_longitude_decimal_value))

south_bound_latitude_element = list(EX_GeographicBoundingBox_element.iter(namespaces['gmd']+'southBoundLatitude'))[0]
south_bound_latitude_decimal_element = list(south_bound_latitude_element.iter(namespaces['gco']+'Decimal'))[0]
south_bound_latitude_decimal_value = list(south_bound_latitude_decimal_element.itertext())[0]
print('south_bound_latitude_decimal_value : {}'.format(south_bound_latitude_decimal_value))

north_bound_latitude_element = list(EX_GeographicBoundingBox_element.iter(namespaces['gmd']+'northBoundLatitude'))[0]
north_bound_latitude_decimal_element = list(north_bound_latitude_element.iter(namespaces['gco']+'Decimal'))[0]
north_bound_latitude_decimal_value = list(north_bound_latitude_decimal_element.itertext())[0]
print('north_bound_latitude_decimal_value : {}'.format(north_bound_latitude_decimal_value))
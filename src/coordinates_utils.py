from pyproj import Transformer
lamb93_epsg_code = "2154" # The Lamb93 coordinates system -> https://epsg.io/2154
wgs84_epsg_code = "4326" # The WGS84 coordinates system -> https://epsg.io/4326

def lamb93_to_wgs84(coordinates_lamb93):
    transformer = Transformer.from_crs("epsg:"+wgs84_epsg_code, "epsg:"+lamb93_epsg_code)
    coordinates_wgs84 = transformer.transform(
                                                coordinates_lamb93[0],
                                                coordinates_lamb93[1]
                                            )
    return coordinates_wgs84

def wgs84_to_lamb93(coordinates_wgs84):
    transformer = Transformer.from_crs("epsg:"+lamb93_epsg_code, "epsg:"+wgs84_epsg_code)
    coordinates_lamb93 = transformer.transform(
                                                coordinates_wgs84[0],
                                                coordinates_wgs84[1]
                                            )
    return coordinates_lamb93

def bb_bounds_to_coord(bb_bounds) -> dict: # bb_bounds = (min_x, min_y, max_x, max_y)
    bb_coord = {}
    bb_coord['nw'] = (bb_bounds[0], bb_bounds[3])
    bb_coord['ne'] = (bb_bounds[2], bb_bounds[3])
    bb_coord['se'] = (bb_bounds[2], bb_bounds[1])
    bb_coord['sw'] = (bb_bounds[0], bb_bounds[1])

    return bb_coord




from shapely.geometry import Polygon
from coordinates_utils import lamb93_to_wgs84


class AltiData():
    def calc_bb_coordinates(self, format='lamb93') -> dict:
        #     # TODO : docstring
        #     # TODO : test
        west_bound_xll_lamb93 = self.xllcorner_lamb93
        east_bound_xll_lamb93 = self.xllcorner_lamb93 + self.cellsize*self.ncols
        south_bound_yll_lamb93 = self.yllcorner_lamb93 - self.cellsize*self.nrows
        north_bound_yll_lamb93 = self.yllcorner_lamb93

        bb_coord = {}
        bb_coord['nw'] = (west_bound_xll_lamb93, north_bound_yll_lamb93)
        bb_coord['ne'] = (east_bound_xll_lamb93, north_bound_yll_lamb93)
        bb_coord['se'] = (east_bound_xll_lamb93, south_bound_yll_lamb93)
        bb_coord['sw'] = (west_bound_xll_lamb93, south_bound_yll_lamb93)
        return bb_coord
        
    def __init__(self, ascii_file_path):
        self._load_ascii_file_data(ascii_file_path)
        # self._calc_bb_coordinates() # ascii_table_bb_coord_lamb93 (mask for loading polygons from shapefiles)
        # elf._calc_bb_polygon() # ascii_table_bb_polygon_wsg84 (to plot with follium)

    def _load_ascii_file_data(self, ascii_file_path) -> dict:
        # TODO : docstring
        # TODO : test
        with open(ascii_file_path, 'r') as ascii_file:
            self.ncols = int(ascii_file.readline().replace('ncols', '').replace(' ', '').replace('\n', ''))
            self.nrows = int(ascii_file.readline().replace('nrows', '').replace(' ', '').replace('\n', ''))
            self.xllcorner_lamb93 = float(ascii_file.readline().replace('xllcorner', '').replace(' ', '').replace('\n', ''))
            self.yllcorner_lamb93 = float(ascii_file.readline().replace('yllcorner', '').replace(' ', '').replace('\n', ''))
            self.cellsize = int(float(ascii_file.readline().replace('cellsize', '').replace(' ', '').replace('\n', '')))
            self.NODATA_value = float(ascii_file.readline().replace('NODATA_value', '').replace(' ', '').replace('\n', ''))
            self.alti_table = []
            for line in ascii_file.readlines():
                ascii_line = line.split(' ')
                ascii_line.remove('')
                self.alti_table.append([float(cell) for cell in ascii_line])

    # def _calc_bb_polygon(self, format='wgs84'):
    #     # TODO : docstring
    #     # TODO : test
    #     ascii_table_nw_bound_coord_lamb93 = (ascii_table_west_bound_xll_lamb93, ascii_table_north_bound_yll_lamb93)
    #     ascii_table_ne_bound_coord_lamb93 = (ascii_table_east_bound_xll_lamb93, ascii_table_north_bound_yll_lamb93)
    #     ascii_table_se_bound_coord_lamb93 = (ascii_table_east_bound_xll_lamb93, ascii_table_south_bound_yll_lamb93)
    #     ascii_table_sw_bound_coord_lamb93 = (ascii_table_west_bound_xll_lamb93, ascii_table_south_bound_yll_lamb93)

      

    #     ascii_table_bb_polygon_lamb93 = Polygon([
    #                                         ascii_table_nw_bound_coord,
    #                                         ascii_table_ne_bound_coord,
    #                                         ascii_table_se_bound_coord,
    #                                         ascii_table_sw_bound_coord
    #                                     ])
    #     print(ascii_table_bb_polygon_lamb93)

    def _calc_bb_meta_coordinates(self, format='lamb93'):
        '''
        format : default to lamb93, otherwise to wgs84
        '''
        # TODO : docstring
        # TODO : test
        west_bound_xll_lamb93 = self.xllcorner_lamb93
        east_bound_xll_lamb93 = self.xllcorner_lamb93 + self.cellsize*self.ncols
        south_bound_yll_lamb93 = self.yllcorner_lamb93 - self.cellsize*self.nrows
        north_bound_yll_lamb93 = self.yllcorner_lamb93

        bb_coord_lamb93 = (
                                west_bound_xll_lamb93,
                                east_bound_xll_lamb93,
                                south_bound_yll_lamb93,
                                north_bound_yll_lamb93
                            )
        if format not in ['lamb93', 'wgs84']:
            raise KeyError('Expected format in [\'lamb93\', \'wgs84\'], got \'{}\''.format(format))
        elif format == 'lamb93':
            return bb_coord_lamb93
        # else :
        #     bb_coord_wgs84 = 
        #     return bb_coord_wgs84 = lamb93_to_wgs84


            
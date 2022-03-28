from shapely.geometry import Polygon
from coordinates_utils import lamb93_to_wgs84


class AltiData():
    def calc_bb_bound_coordinates(self, format:str='lamb93') -> dict:
        if format == 'lamb93' or format =='wgs84':
            bb_bounds_coord_lamb93 = {}
            bb_bounds_coord_lamb93['xmin'] = self.xllcorner_lamb93
            bb_bounds_coord_lamb93['xmax'] = self.xllcorner_lamb93 + self.cellsize*self.ncols
            bb_bounds_coord_lamb93['ymin'] = self.yllcorner_lamb93 - self.cellsize*self.nrows
            bb_bounds_coord_lamb93['ymax'] = self.yllcorner_lamb93
            if format == 'lamb93':
                return bb_bounds_coord_lamb93
        if format == 'wgs84':
            bb_bounds_coord_wgs84 = {}
            bb_bounds_coord_wgs84['xmin'] = lamb93_to_wgs84(bb_bounds_coord_lamb93['xmin'])
            bb_bounds_coord_wgs84['xmax'] = lamb93_to_wgs84(bb_bounds_coord_lamb93['xmax'])
            bb_bounds_coord_wgs84['ymin'] = lamb93_to_wgs84(bb_bounds_coord_lamb93['ymin'])
            bb_bounds_coord_wgs84['ymax'] = lamb93_to_wgs84(bb_bounds_coord_lamb93['ymax'])
            return bb_bounds_coord_wgs84
        else:
            raise ValueError('Wrong value for \'format\'argument')
        
    def calc_bb_polygon(self, format:str='lamb93') -> Polygon:
        bb_angle_coordinates = self.calc_bb_angle_coordinates(format)
        bb_polygon_lamb93 = Polygon([
                            bb_angle_coordinates['nw'],
                            bb_angle_coordinates['ne'],
                            bb_angle_coordinates['se'],
                            bb_angle_coordinates['sw']
                        ])
        return bb_polygon_lamb93

    def calc_bb_angle_coordinates(self, format:str='lamb93') -> dict:
        if format == 'lamb93' or format =='wgs84':
            bb_angle_coord_lamb93 = {}
            bb_angle_coord_lamb93['nw'] = (self.xllcorner_lamb93, self.yllcorner_lamb93)
            bb_angle_coord_lamb93['ne'] = (self.xllcorner_lamb93 + self.cellsize*self.ncols, self.yllcorner_lamb93)
            bb_angle_coord_lamb93['se'] = (self.xllcorner_lamb93 + self.cellsize*self.ncols, self.yllcorner_lamb93 - self.cellsize*self.nrows)
            bb_angle_coord_lamb93['sw'] = (self.xllcorner_lamb93, self.yllcorner_lamb93 - self.cellsize*self.nrows)
            if format == 'lamb93':
                return bb_angle_coord_lamb93
            if format == 'wgs84':  
                bb_angle_coord_wgs84 = {}
                bb_angle_coord_wgs84['nw'] = lamb93_to_wgs84(bb_angle_coord_lamb93['nw'])
                bb_angle_coord_wgs84['ne'] = lamb93_to_wgs84(bb_angle_coord_lamb93['ne'])
                bb_angle_coord_wgs84['se'] = lamb93_to_wgs84(bb_angle_coord_lamb93['se'])
                bb_angle_coord_wgs84['sw'] = lamb93_to_wgs84(bb_angle_coord_lamb93['sw'])
                return bb_angle_coord_wgs84
        else:
            raise ValueError('Wrong value for \'format\'argument')
            
    def __init__(self, ascii_file_path):
        self._load_ascii_file_data(ascii_file_path)

    def _load_ascii_file_data(self, ascii_file_path) -> dict:
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

    def _calc_bb_meta_coordinates(self, format='lamb93'):
        '''
        format : default to lamb93, otherwise to wgs84
        '''
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
        else:
            bb_coord_wgs84 = (
                                lamb93_to_wgs84(bb_coord_lamb93[0]),
                                lamb93_to_wgs84(bb_coord_lamb93[1]),
                                lamb93_to_wgs84(bb_coord_lamb93[2]),
                                lamb93_to_wgs84(bb_coord_lamb93[3]),
            )
            return bb_coord_wgs84
    
    def calc_cell_center_coordinates(self):
        cells_center_coordinates = [[None for col in range(self.ncols)] for row in range(self.nrows)]

        # start coordinates
        nw_coord_ref_lamb93 = (
                                self.xllcorner_lamb93 + self.cellsize/2, # x_coord
                                self.yllcorner_lamb93 - self.cellsize/2  # y_coord
                            )


        for row in range(len(cells_center_coordinates)):
            for col in range(len(cells_center_coordinates[0])):
                cell_center_coord = (
                    nw_coord_ref_lamb93[0]+(col+1)*self.cellsize, # x_coord
                    nw_coord_ref_lamb93[1]-(row+1)*self.cellsize  # y_coord
                )
                cells_center_coordinates[row][col] = cell_center_coord
        
        return cells_center_coordinates


            
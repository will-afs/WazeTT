from typing import List


def vectorize_polygon(polygon) -> List:
    x,y = polygon.exterior.coords.xy
    vectorized_polygon = []
    for i in range(len(x)):
        coordinates = (x[i],y[i])
        vectorized_polygon.append(coordinates)
    return vectorized_polygon
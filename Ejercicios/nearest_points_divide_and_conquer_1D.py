import numpy as np
from math import inf


def nearest_points(points: 'nparray', linf: int, lsup: int) -> 'nparray':
    size = lsup - linf + 1
    if size>1:
        half = (linf + lsup) // 2
        nearest_points_left, positions_left, distance_left = nearest_points(points, linf, half)
        nearest_points_right, positions_right, distance_right = nearest_points(points, half + 1, lsup)
        nearest_points_central, positions_central, distance_central = [points[half],
                                                                       points[half + 1]], \
                                                                      [half, half + 1], \
                                                                      distance(points, half, half + 1)
        if distance_left <= distance_right:
            if distance_left <= distance_central:
                return nearest_points_left, positions_left, distance_left
        else:
            if distance_right <= distance_central:
                return nearest_points_right, positions_right, distance_right

        return nearest_points_central, positions_central, distance_central
    else:
        return None, None, inf


def nearest_points_divide_and_conquer_1D(points: 'nparray') -> 'nparray':
    points = np.sort(points, kind='heapsort')
    return nearest_points(points, 0, points.size-1)


def distance(points:'nparray', i:int, j:int)->float:
    return abs(points[i] - points[j])


points = np.random.randint(1, 10001, size=1000)
nearest_points, positions, distance = nearest_points_divide_and_conquer_1D(points)

print('Los puntos más cercanos son el', nearest_points[0], 'y el',
      nearest_points[1], 'que están en la posición', positions[0],'y',
      positions[1], 'respectivamente', 'y a una distancia de', distance)

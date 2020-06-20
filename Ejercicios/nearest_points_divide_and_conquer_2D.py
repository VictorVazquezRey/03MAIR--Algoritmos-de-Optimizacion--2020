import numpy as np
from math import inf
from math import sqrt

def calculate_central(min_distance:float, points:'nparray',linf:int, lsup:int, half:int):
    pass


def nearest_points(points: 'nparray', linf: int, lsup: int) -> 'nparray':
    size = lsup - linf + 1
    if size>1:
        half = (linf + lsup) // 2
        nearest_points_left, distance_left = nearest_points(points, linf, half)
        nearest_points_right, distance_right = nearest_points(points, half + 1, lsup)
        nearest_points_central, distance_central = calculate_central(min(distance_left,
                                                                                            distance_right),
                                                                                        points,
                                                                                        linf,
                                                                                        lsup,
                                                                                        half)
        if distance_left <= distance_right:
            if distance_left <= distance_central:
                return nearest_points_left, positions_left, distance_left
        else:
            if distance_right <= distance_central:
                return nearest_points_right, positions_right, distance_right

        return nearest_points_central,distance_central
    else:
        return None, inf


def nearest_points_divide_and_conquer_2D(points: 'nparray') -> 'nparray':
    points = np.array(sorted(points, lambda point:point[0]))
    return nearest_points(points, 0, points.shape[0]-1)


# La distancia euclidea
def distance(points:'nparray', i:int, j:int)->float:
    result = 0
    for x,y in zip(points[i],points[j]):
        result += (x-y)**2
    return sqrt(result)


# Esta instrucción ya obtiene 1000 puntos en 2D aleatorios con coordenadas entre 1 y 10000
points = np.random.randint(1, 10001, size=(1000,2))
nearest_points, distance = nearest_points_divide_and_conquer_2D(points)

print('Los puntos más cercanos son el', nearest_points[0], 'y el',
      nearest_points[1], 'que están a una distancia de', distance)
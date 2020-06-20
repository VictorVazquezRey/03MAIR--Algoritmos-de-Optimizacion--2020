import numpy as np
from math import inf
from math import sqrt

def calculate_central(min_distance:float, points:'nparray', half: int):
    middle = [points[half]]
    i = half-1
    while i>0 and distance_1D(points,i,half) < min_distance:
        middle.insert(0, points[i])
        i -= 1
    i = half+1
    while i < points.shape[0] and distance_1D(points, i, half) < min_distance:
        middle.append(points[i])
        i += 1
    middle = np.array(sorted(middle, key=lambda point: point[1]))

    min = inf
    nearest_points = []

    for i,point in enumerate(middle):
        j = i+1
        while j<middle.shape[0] and distance_1D(middle, i, j, axis=1) < min_distance:
            actual_distance = distance(middle,i,j)
            if actual_distance < min_distance:
                min = actual_distance
                nearest_points = [middle[i], middle[j]]
            j += 1
    return nearest_points, min


def nearest_points(points: 'nparray') -> 'nparray':
    if points.shape[0]==2:
        return points, distance(points,0,1)
    elif points.shape[0]>2:
        half = points.shape[0] // 2
        nearest_points_left, distance_left = nearest_points(points[0:half])
        nearest_points_right, distance_right = nearest_points(points[half:])
        nearest_points_central, distance_central = calculate_central(min(distance_left,distance_right),
                                                                     points,
                                                                     half)
        if distance_left <= distance_right:
            if distance_left <= distance_central:
                return nearest_points_left, distance_left
        else:
            if distance_right <= distance_central:
                return nearest_points_right, distance_right

        return nearest_points_central,distance_central
    else:
        return None, inf


# Como la ordenación es estable en sorted a partir de este punto el array points
# y todas sus vistas estarán ordenados según la coordenada x.
def nearest_points_divide_and_conquer_3D(points: 'nparray') -> 'nparray':
    points = np.array(sorted(points, key=lambda point:point[0]))
    return nearest_points(points)


# La distancia euclidea
def distance(points:'nparray', i:int, j:int)->float:
    result = 0
    for x,y in zip(points[i],points[j]):
        result += (x-y)**2
    return sqrt(result)

def distance_1D(points:'nparray', i:int, j:int, axis: int=0)->float:
    return abs(points[i][axis] - points[j][axis])


# Esta instrucción ya obtiene 1000 puntos en 2D aleatorios con coordenadas entre 1 y 10000
points = np.random.randint(1, 10001, size=(1000, 3))
nearest_points, distance = nearest_points_divide_and_conquer_3D(points)

print('Los puntos más cercanos son el', nearest_points[0], 'y el',
      nearest_points[1], 'que están a una distancia de', "{:.4f}".format(distance))
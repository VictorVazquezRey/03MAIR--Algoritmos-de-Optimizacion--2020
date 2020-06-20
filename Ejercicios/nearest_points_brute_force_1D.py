import numpy as np
from math import inf 

def nearest_points_brute_force_1D(points:'nparray')->'nparray':
    min_distance = inf
    nearest_points = []
    positions = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            actual_distance = distance(points, i, j)
            if actual_distance < min_distance:
                nearest_points = [points[i], points[j]]
                positions = [i, j]
                min_distance = actual_distance
    return nearest_points, positions, min_distance

def distance(points:'nparray', i:int, j:int)->float:
    return abs(points[i] - points[j])


points = np.random.randint(1, 10001, size=1000)
nearest_points, positions, distance = nearest_points_brute_force_1D(points)
print('Los puntos más cercanos son el', nearest_points[0], 'y el', 
      nearest_points[1], 'que están en la posición', positions[0],'y',
      positions[1], 'respectivamente', 'y a una distancia de', distance)
import numpy as np
import itertools as it
from math import inf

def cost(cost_matrix:'nparray', assignament: tuple)->float:
    cost = 0
    for job, agent in enumerate(assignament):
        cost += costs_matrix[agent][job]
    return cost

def assignaments(cost_matrix:'nparray')->tuple:
    dimension = costs_matrix.shape[0]
    min_cost = inf
    result = ()
    for assignament in list(it.permutations(range(dimension))):
        actual_cost = cost(costs_matrix, assignament)
        if actual_cost < min_cost:
            min_cost = actual_cost
            result = assignament

    return result, min_cost


dimension = 4
#generación automática y aleatoria de la matriz de costes.
costs_matrix = np.random.randint(1, 26, size=(dimension, dimension))
print(costs_matrix)
assignament, assignament_cost = assignaments(costs_matrix)
print('La mejor asignación de tareas es:', assignament,'con un coste total de:', assignament_cost)

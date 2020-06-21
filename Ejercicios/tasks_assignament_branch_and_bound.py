import numpy as np
from math import inf


def cost(costs_matrix: 'nparray', assignament: tuple) -> float:
    cost = 0
    for job, agent in enumerate(assignament):
        cost += costs_matrix[agent][job]
    return cost

def lower_bound_cost(costs_matrix: 'nparray', assignament: tuple) -> float:
    dimension = costs_matrix.shape[0]
    fixed_cost = cost(costs_matrix, assignament)

    unassigned_tasks = set(range(dimension)) - set(assignament)
    unassigned_agents = range(len(assignament), dimension)

    estimated_cost = 0
    for agent in unassigned_agents:
        estimated_cost += min([costs_matrix[agent][task]  for task in unassigned_tasks])

    return fixed_cost + estimated_cost


def branch(parent: tuple, dimension:int)->list:
    to_expand = set(range(dimension)) - set(parent)
    return [parent+(task,) for task in to_expand]


def assignaments(cost_matrix: 'nparray') -> tuple:
    dimension = costs_matrix.shape[0]
    min_cost = inf
    result = ()

    return result, min_cost


dimension = 4
# generación automática y aleatoria de la matriz de costes.
costs_matrix = np.random.randint(1, 26, size=(dimension, dimension))

import numpy as np
from math import inf


class Task_Asignament:
    dimension = None
    costs_matrix = None

    def __init__(self, dimension, costs_matrix=None, less_cost=1, high_cost=25):
        self.dimension = dimension
        if costs_matrix is None:
            self.costs_matrix = np.random.randint(less_cost,
                                                  high_cost + 1,
                                                  size=(dimension, dimension))
        else:
            self.costs_matrix = costs_matrix


    def cost(self, assignament: tuple) -> float:
        cost = 0
        for agent, job in enumerate(assignament):
            cost += self.costs_matrix[agent][job]
        return cost

    def lower_and_upper_bound_cost(self, assignament: tuple) -> tuple:
        fixed_cost = self.cost(assignament)

        unassigned_tasks = set(range(self.dimension)) - set(assignament)
        unassigned_agents = range(len(assignament), self.dimension)

        estimated_min_cost = 0
        estimated_max_cost = 0
        for agent in unassigned_agents:
            costs_for_agent_rest_of_tasks = [self.costs_matrix[agent][task] for task in unassigned_tasks]
            estimated_min_cost += min(costs_for_agent_rest_of_tasks)
            estimated_max_cost += max(costs_for_agent_rest_of_tasks)

        return fixed_cost + estimated_max_cost, fixed_cost + estimated_min_cost

    def branch(self, parent: dict) -> list:
        to_expand = set(range(self.dimension)) - set(parent['node'])
        childs = []
        for task in to_expand:
            node = parent['node'] + (task,)
            max, min = self.lower_and_upper_bound_cost(node)
            childs.append({'node': node, 'lb': min, 'ub': max})

        return childs

    def assignaments(self) -> tuple:
        min_cost = inf
        result = ()

        return result, min_cost


# dimension = 4
# generación automática y aleatoria de la matriz de costes.
# costs_matrix = np.random.randint(1, 26, size=(dimension, dimension))

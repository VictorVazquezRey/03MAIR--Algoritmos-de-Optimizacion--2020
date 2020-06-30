import numpy as np
from math import inf


class Node:
    info = ()
    lb = 0
    ub = 0

    def __init__(self, info: tuple = (), lb: int = 0, up: int = 0):
        self.info = info
        self.lb = lb
        self.ub = up

    def __repr__(self):
        return "Node(info:{},lb:{},ub:{})".format(self.info, self.lb, self.ub)

    def __str__(self):
        return "[info:{},lb:{},ub:{}]".format(self.info, self.lb, self.ub)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.info == other.info and self.lb == other.lb and self.ub == other.ub
        return False

    def __lt__(self, other):
        if isinstance(other, Node):
            return self.lb < other.lb
        return False


class Task_Asignament:
    dimension = None
    costs_matrix = None
    nodes = []
    upper = inf

    def __init__(self, dimension, costs_matrix=None, less_cost=1, high_cost=25):
        self.dimension = dimension
        self.upper = inf
        if costs_matrix is None:
            self.costs_matrix = np.random.randint(less_cost,
                                                  high_cost + 1,
                                                  size=(dimension, dimension))
        else:
            self.costs_matrix = costs_matrix

    # O(len(assignament)
    def cost(self, assignament: tuple) -> float:
        cost = 0
        for agent, job in enumerate(assignament):
            cost += self.costs_matrix[agent][job]
        return cost

    #O((n-len(assignament))^2)
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

    def branch(self, parent: Node) -> list:
        to_expand = set(range(self.dimension)) - set(parent.info)
        children = []
        for task in to_expand:
            info = parent.info + (task,)
            max, min = self.lower_and_upper_bound_cost(info)
            # Si cumple la condición de poda no se expande.
            if min < self.upper:
                if max < self.upper:
                    self.upper = max
                node = Node(info, min, max)
                children.append(node)
            # Esta condición es de solución y por tanto la poda puede ser más dramática.
            elif min==max and min == self.upper:
                self.nodes = []
                return [Node(info, min, max)]

        return sorted(children)

    def assignaments(self) -> list:
        self.nodes = self.branch(Node())
        solution = None
        while self.nodes and not solution:
            # print('expandidos:', self.nodes)
            candidate = self.nodes.pop(0)
            # print('candidato:', candidate, 'lsup:', self.upper)
            if len(candidate.info) < self.dimension:
                b = self.branch(candidate)
                self.nodes = self.nodes + b
                self.nodes.sort()
            else:
                return [candidate.info, candidate.ub]
        return None


# generación automática y aleatoria de la matriz de costes.
dimension = 15
# costs_matrix = np.array([i for i in range(1, dimension * dimension + 1)]) \
#                         .reshape((dimension, dimension))
costs_matrix = np.random.randint(1, 26, size=(dimension, dimension))
ta = Task_Asignament(dimension, costs_matrix)
print(ta.assignaments())

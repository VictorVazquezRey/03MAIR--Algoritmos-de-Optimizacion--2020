from traveling_salesman_problem import TSP
from functools import reduce
from operator import add
import numpy as np
from math import inf

class AntColony:
    def __init__(self, tsp:TSP):
        self.tsp = tsp
        self.trails = {}
        self.ants = []
        self.ants_distances = []
        self.alpha = .1
        self.beta = .1
        self.rho = .1
        self.generations_number = 10
        self.number_of_ants = 100
        self.initial_theta = .1
        self.Q =1000

    def init_trails(self):
        self.trails = {k: 1 for k in self.tsp.edges}

    def init_ants(self):
        self.ants = [[0] for _ in range(self.number_of_ants)]
        self.ants_distances = [inf for _ in range(self.number_of_ants)]

    def desiderability(self, edge : tuple) -> float:
        return 1/self.tsp.weight(edge[0], edge[1])

    def choose_next_node(self, ant: int):
        # this calculates reachable edges from last position visited by ant
        last_node = self.ants[ant][-1]
        left_nodes = list(set(self.tsp.nodes)-set(self.ants[ant]))
        reachable_edges = [edge for edge in tsp.edges if edge[0] == last_node and edge[1] in left_nodes]
        # calculate denominator of probability term
        sum_factors = reduce(add, [(self.trails[edge]**self.alpha) * (self.desiderability(edge)**self.beta) for edge in reachable_edges])
        # list of probabilities for each edge to be selected
        probabilities = [(self.trails[edge]**self.alpha) * (self.desiderability(edge)**self.beta) / sum_factors for edge in reachable_edges]
        # choice a position with calculated probabilities return a list of positions (only one because the second parameter)
        to_return = np.random.choice(range(len(probabilities)),
                                     1,
                                     replace=False,
                                     p=probabilities)

        return reachable_edges[to_return[0]][1]

    def increase_trail(self):
        for ant in range(self.number_of_ants):
            ant_s = self.ants[ant]
            ant_s_distance = self.ants_distances[ant]

            for i in range(self.tsp.dimension - 1):
                self.trails[(ant_s[i], ant_s[i+1])] += self.Q / ant_s_distance

            self.trails[(ant_s[-1], ant_s[0])] += self.Q / ant_s_distance

    def decrease_trails(self):
        self.trails = {k: max(v  - self.rho, self.initial_theta) for k, v in self.trails.items()}

    def ant_colony(self, number_of_ants: int = 42, alpha: float = 2, beta: float = 2,
                   rho: float = .2, generations_number: int = 20, initial_theta: float = 0.01,
                   q: float = 500):
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.generations_number = generations_number
        self.number_of_ants = number_of_ants
        self.initial_theta = initial_theta
        self.Q = q
        self.init_trails()

        best_solution = []
        distance_best_solution = inf

        for gen in range(self.generations_number):
            self.init_ants()
            for ant in range(number_of_ants):
                for _ in range(self.tsp.dimension - 1):
                    new_node = self.choose_next_node(ant)
                    self.ants[ant].append(new_node)

                self.ants_distances[ant] = self.tsp.distance(self.ants[ant]) #Just to optimize calculations
                # select best ant
                if self.ants_distances[ant] < distance_best_solution:
                    distance_best_solution = self.ants_distances[ant]
                    best_solution = self.ants[ant]

            self.increase_trail()
            self.decrease_trails()



        print(self.trails)
        return best_solution, distance_best_solution




url = 'http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/swiss42.tsp'
tsp = TSP(url)
rs = AntColony(tsp)

solution, distance = rs.ant_colony()
print("La mejor solución es {} con una distancia de {}".format(solution, distance))
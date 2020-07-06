from traveling_salesman_problem import TSP
import numpy as np
from itertools import combinations


class LocalSearch:
    def __init__(self, tsp:TSP):
        self.tsp = tsp

    # best-improvement
    def find_best_neighbor(self, solution: 'nparray'):

        best_solution = solution
        distance_best_solution = self.tsp.distance(solution)

        for i, j in combinations(np.array(self.tsp.nodes[1:]), 2):
            neighbor = np.copy(solution)
            self.tsp.swap(neighbor, i, j)
            distance_neighbor = self.tsp.distance(neighbor)

            if distance_neighbor < distance_best_solution:
                distance_best_solution = distance_neighbor
                best_solution = neighbor

        return best_solution, distance_best_solution

    def local_search(self):

        solution = self.tsp.create_solution()
        best_solution = solution
        distance_best_solution = self.tsp.distance(best_solution)

        while True:
            neighbor, distance_neighbor = self.find_best_neighbor(solution)
            if distance_neighbor < distance_best_solution:
                best_solution = neighbor
                distance_best_solution = distance_neighbor
            else:
                return best_solution, distance_best_solution

            solution = neighbor

url = 'http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/swiss42.tsp'
tsp = TSP(url)
rs = LocalSearch(tsp)

solution, distance = rs.local_search()
print("La mejor solución es {} con una distancia de {}".format(solution, distance))
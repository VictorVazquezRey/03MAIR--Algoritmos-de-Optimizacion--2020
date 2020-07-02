from urllib import request
from requests.sessions import Session
import tsplib95
import numpy as np
from functools import reduce
from operator import add
from itertools import combinations
from random import sample, random
from math import exp, log
from enum import Enum


class Descend_Type(Enum):
    EXPONENTIAL = 1
    BOLTZMAN = 2
    CAUCHY = 3


class TSP:
    def __init__(self, url: str):
        with Session() as s:
            response = s.get(url)
            content = response.content.decode('utf-8')

        self.problem = tsplib95.parse(content)
        self.nodes = list(self.problem.get_nodes())
        self.edges = list(self.problem.get_edges())
        self.dimension = len(self.nodes)
        self.temperature_0 = 1000
        self.temperature_k = 1000
        self.descend_type = Descend_Type.EXPONENTIAL
        self.k = 1
        self.alfa = .999

    def create_solution(self) -> list:
        solution = np.array(self.nodes)
        np.random.shuffle(solution[1:])
        return solution

    def weight(self, a: int, b: int) -> int:
        return self.problem.get_weight(a, b)

    def distance(self, solution: list) -> int:
        return reduce(add, map(self.weight, solution[:-1], solution[1:]))

    def swap(self, solution: 'nparray', pos1: int, pos2: int):
        solution[pos1], solution[pos2] = solution[pos2], solution[pos1]

    def random_search(self, iterations: int = 100) -> int:

        best_solution = self.create_solution()
        distance_best_solution = self.distance(best_solution)

        for it in range(iterations):
            actual_solution = self.create_solution()
            distance_actual_solution = self.distance(actual_solution)

            if distance_actual_solution < distance_best_solution:
                best_solution = actual_solution
                distance_best_solution = distance_actual_solution

        return best_solution, distance_best_solution

    def find_neighbor(self, solution: 'nparray'):
        i, j = sample(range(1, self.dimension), 2)
        neighbor = np.copy(solution)
        self.swap(neighbor, i, j)
        distance_neighbor = self.distance(neighbor)

        return neighbor, distance_neighbor

    # best-improvement
    def find_best_neighbor(self, solution: 'nparray'):

        best_solution = solution
        distance_best_solution = self.distance(solution)

        for i, j in combinations(np.array(self.nodes[1:]), 2):
            neighbor = np.copy(solution)
            self.swap(neighbor, i, j)
            distance_neighbor = self.distance(neighbor)

            if distance_neighbor < distance_best_solution:
                distance_best_solution = distance_neighbor
                best_solution = neighbor

        return best_solution, distance_best_solution

    def local_search(self):

        solution = self.create_solution()
        best_solution = solution
        distance_best_solution = self.distance(best_solution)

        while True:
            neighbor, distance_neighbor = self.find_best_neighbor(solution)
            if distance_neighbor < distance_best_solution:
                best_solution = neighbor
                distance_best_solution = distance_neighbor
            else:
                return best_solution, distance_best_solution

            solution = neighbor

    def lower_the_temperature(self):
        if self.descend_type == Descend_Type.EXPONENTIAL:
            self.temperature_k *= self.alfa
        elif self.descend_type == Descend_Type.BOLTZMAN:
            self.temperature_k = self.temperature_0 / (1 + log(self.k))
            self.k += 1
        elif self.descend_type == Descend_Type.CAUCHY:
            self.temperature_k = self.temperature_0 / (1 + self.k)
            self.k += 1
        else:
            raise ValueError('Descend_Type unkown')

    def is_accepted(self, d_n: int, d_s: int):
        if d_n >= d_s:
            return random() <= exp(-1 * (d_n - d_s) / self.temperature_k)
        return True

    def simulated_annealing(self, temperature: float, delta: float = .0001,
                            descend_type=Descend_Type.EXPONENTIAL, alfa:float=.999):
        self.temperature_0 = temperature
        self.temperature_k = temperature
        self.descend_type = descend_type
        self.alfa = alfa
        solution = self.create_solution()
        distance_solution = self.distance(solution)
        best_solution = solution
        distance_best_solution = distance_solution

        while self.temperature_k > delta:
            neighbor, distance_neighbor = self.find_neighbor(solution)
            if distance_neighbor < distance_best_solution:
                best_solution = neighbor
                distance_best_solution = distance_neighbor

            if self.is_accepted(distance_neighbor, distance_solution):
                solution = neighbor
                distance_solution = distance_neighbor

            self.lower_the_temperature()

        return best_solution, distance_best_solution


url = 'http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/swiss42.tsp'
tsp = TSP(url)
solution, distance = tsp.random_search()
solution_local_search, distance_local_search = tsp.local_search()
solution_simulated_annealing, distance_simulated_annealing = tsp.simulated_annealing(1000)
print("La mejor solución es {} con una distancia de {}".format(solution, distance))
print("La mejor solución es {} con una distancia de {}".format(solution_local_search, distance_local_search))
print("La mejor solución es {} con una distancia de {}".format(solution_simulated_annealing, distance_simulated_annealing))

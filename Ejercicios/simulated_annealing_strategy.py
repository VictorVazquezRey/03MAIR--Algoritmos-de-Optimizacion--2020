from traveling_salesman_problem import TSP
from enum import Enum
from math import exp, log
from random import random


class Descend_Type(Enum):
    EXPONENTIAL = 1
    BOLTZMAN = 2
    CAUCHY = 3


class SimulatedAnnealing:
    def __init__(self, tsp: TSP, temperature: float = 1000,
                 descend_type=Descend_Type.EXPONENTIAL, alpha: float = .999):
        self.descend_type = descend_type
        self.tsp = tsp
        self.temperature_0 = temperature
        self.temperature_k = temperature
        self.k = 1
        self.alpha = alpha

    def lower_the_temperature(self):
        if self.descend_type == Descend_Type.EXPONENTIAL:
            self.temperature_k *= self.alpha
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

    def simulated_annealing(self, temperature: float = 1000, delta: float = .0001,
                            descend_type=Descend_Type.EXPONENTIAL, alpha: float = .999):
        self.temperature_0 = temperature
        self.temperature_k = temperature
        self.descend_type = descend_type
        self.alpha = alpha
        solution = self.tsp.create_solution()
        distance_solution = self.tsp.distance(solution)
        best_solution = solution
        distance_best_solution = distance_solution

        while self.temperature_k > delta:
            neighbor, distance_neighbor = self.tsp.find_neighbor(solution)
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
rs = SimulatedAnnealing(tsp)

solution, distance = rs.simulated_annealing()
print("La mejor solución es {} con una distancia de {}".format(solution, distance))

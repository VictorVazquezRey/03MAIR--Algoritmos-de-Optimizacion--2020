from requests.sessions import Session
import tsplib95
import numpy as np
from functools import reduce
from operator import add
from random import sample, random, choice

class TSP:
    def __init__(self, url: str):
        with Session() as s:
            response = s.get(url)
            content = response.content.decode('utf-8')

        self.problem = tsplib95.parse(content)
        self.nodes = list(self.problem.get_nodes())
        self.edges = list(self.problem.get_edges())
        self.dimension = len(self.nodes)

    def create_solution(self) -> list:
        solution = np.array(self.nodes)
        np.random.shuffle(solution[1:])
        return solution

    def weight(self, a: int, b: int) -> int:
        return self.problem.get_weight(a, b)

    def distance(self, solution: list) -> int:
        return reduce(add, map(self.weight, solution[:-1], solution[1:])) + \
               self.weight(solution[self.dimension - 1], solution[0])

    def swap(self, solution: 'nparray', pos1: int, pos2: int):
        solution[pos1], solution[pos2] = solution[pos2], solution[pos1]

    def find_neighbor(self, solution: 'nparray'):
        i, j = sample(range(1, self.dimension), 2)
        neighbor = np.copy(solution)
        self.swap(neighbor, i, j)
        distance_neighbor = self.distance(neighbor)

        return neighbor, distance_neighbor


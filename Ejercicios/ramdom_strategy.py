from traveling_salesman_problem import TSP
class RandomSearch:
    def __init__(self, tsp:TSP, iterations: int = 100):
        self.tsp = tsp
        self.iterations = iterations

    def random_search(self, iterations: int = 100) -> int:

        best_solution = self.tsp.create_solution()
        distance_best_solution = self.tsp.distance(best_solution)

        for it in range(iterations):
            actual_solution = self.tsp.create_solution()
            distance_actual_solution = self.tsp.distance(actual_solution)

            if distance_actual_solution < distance_best_solution:
                best_solution = actual_solution
                distance_best_solution = distance_actual_solution

        return best_solution, distance_best_solution

url = 'http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/swiss42.tsp'
tsp = TSP(url)
rs = RandomSearch(tsp)

solution, distance = rs.random_search()
print("La mejor solución es {} con una distancia de {}".format(solution, distance))
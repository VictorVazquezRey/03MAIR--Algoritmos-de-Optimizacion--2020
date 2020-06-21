import unittest
import tasks_assignament_branch_and_bound as to_test
import numpy as np

class MyTestCase(unittest.TestCase):
    dimension = 4
    costs_matrix = np.array([i for i in range(1, dimension*dimension + 1)]).reshape((dimension,dimension))
    # [[1  2  3  4]
    #  [5  6  7  8]
    #  [9 10 11 12]
    #  [13 14 15 16]]

    def test_brach(self):
        self.assertEqual([(0,1), (0,2), (0,3)], to_test.branch((0,),self.dimension))
        self.assertEqual([(0, 2, 1), (0, 2, 3)], to_test.branch((0,2), self.dimension))


    def test_lower_bound_cost(self):
        self.assertEqual(33, to_test.lower_bound_cost(self.costs_matrix,(0,1)))

if __name__ == '__main__':
    unittest.main()

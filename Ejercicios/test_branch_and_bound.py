import unittest
import tasks_assignament_branch_and_bound as to_test
import numpy as np


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.dimension = 4
        self.costs_matrix = np.array([i for i in range(1, self.dimension * self.dimension + 1)])\
                                    .reshape((self.dimension, self.dimension))
        self.ta = to_test.Task_Asignament(self.dimension,costs_matrix=self.costs_matrix)
        # [[1  2  3  4]
        #  [5  6  7  8]
        #  [9 10 11 12]
        #  [13 14 15 16]]

    def test_brach(self):
        {'assig':(0,), 'lb':0, 'ub':0}
        self.assertListEqual([{'node': (0, 1), 'lb': 33, 'ub': 35},
                              {'node': (0, 2), 'lb': 32, 'ub': 36},
                              {'node': (0, 3), 'lb': 33, 'ub': 35}],
                             self.ta.branch({'node': (0,), 'lb': 0, 'ub': 0}))

        self.assertEqual([{'lb': 34, 'node': (0, 2, 1), 'ub': 34},
                          {'lb': 34, 'node': (0, 2, 3), 'ub': 34}],
                         self.ta.branch({'node': (0, 2), 'lb': 0, 'ub': 0}))

    def test_lower_bound_cost(self):
        max, min = self.ta.lower_and_upper_bound_cost((0, 1))
        self.assertEqual(33, min)
        self.assertEqual(35, max)


if __name__ == '__main__':
    unittest.main()

import unittest
from tasks_assignament_branch_and_bound import Node,Task_Asignament
import numpy as np


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.dimension = 4
        self.costs_matrix = np.array([i for i in range(1, self.dimension * self.dimension + 1)])\
                                    .reshape((self.dimension, self.dimension))
        self.ta = Task_Asignament(self.dimension,costs_matrix=self.costs_matrix)
        # [[1  2  3  4]
        #  [5  6  7  8]
        #  [9 10 11 12]
        #  [13 14 15 16]]

    def test_brach(self):
        node = Node((0,))
        self.assertListEqual([Node((0, 2), 32, 36),
                              Node((0, 1), 33, 35),
                              Node((0, 3), 33, 35)],
                             self.ta.branch(node))

        node = Node((0, 2))
        self.assertListEqual([Node((0, 2, 1), 34, 34),
                              Node((0, 2, 3), 34, 34)],
                             self.ta.branch(node))

    def test_lower_bound_cost(self):
        max, min = self.ta.lower_and_upper_bound_cost((0, 1))
        self.assertEqual(33, min)
        self.assertEqual(35, max)

        max, min = self.ta.lower_and_upper_bound_cost( (0, 2, 1))
        self.assertEqual(34, min)
        self.assertEqual(34, max)


if __name__ == '__main__':
    unittest.main()

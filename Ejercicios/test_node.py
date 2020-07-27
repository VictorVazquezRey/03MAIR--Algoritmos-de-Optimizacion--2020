import unittest
from node import Node


class MyTestCase(unittest.TestCase):

    def test_is_empty(self):
        self.assertTrue(Node.is_empty([]))
        self.assertFalse(Node.is_empty([2,3,5,1]))

    def test_root_node(self):
        root = Node()
        self.assertEqual(None, root.eval_node())

    def test_value_only_node(self):
        value = 2
        value_only = Node([value])
        self.assertEqual(value, value_only.eval_node())
        
    def test_basic_node(self):
        basic = Node([2,3],['*'])
        self.assertEqual(6, basic.eval_node())
        
    def test_construction(self):
        to_construct = Node([2,3],['*'])
        to_construct.add_operation('-')
        to_construct.add_number(4)
        self.assertEqual(2, to_construct.eval_node())

if __name__ == '__main__':
    unittest.main()

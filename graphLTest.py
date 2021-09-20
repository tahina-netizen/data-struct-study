import unittest
from graphL import *

class GraphLTest(unittest.TestCase):

    def setUp(self):
        self.g1 = GraphL()
        self.g2 = GraphL()

        self.g2_vertices = list(range(9))
        self.g2_edges = [(0, 1), (0, 6), (0, 3), (1, 6), (1, 4), (3, 8), (3, 6), (4, 7), (5, 6), (5, 7), (2, 5)]

        for _ in self.g2_vertices:
            self.g2.add_vertex()

        for (v1, v2) in self.g2_edges:
            self.g2.add_edge(v1, v2)

    def test_construct_works(self):
        GraphL()

    def test_is_null_with_null_graph(self):
        self.assertTrue(self.g1.is_null())

    def test_is_null_with_non_null_graph(self):
        self.assertFalse(self.g2.is_null())

    def test_order(self):
        self.assertEqual(0, self.g1.order())
        self.assertEqual(9, self.g2.order())

    def test_degree_with_unknown_vertex(self):
        with self.assertRaises(Exception):
            self.g2.degree(1024)
            
    def test_degree_with_known_vertex(self):
        self.assertEqual(1, self.g2.degree(2))
        self.assertEqual(3, self.g2.degree(1))

    def test_vertices(self):
        self.assertEqual([], self.g1.vertices())
        self.assertEqual(self.g2_vertices, self.g2.vertices())

    def test_size(self):
        self.assertEqual(0, self.g1.size())
        self.assertEqual(11, self.g2.size())

    def test_add_vertex(self):
        v = self.g1.add_vertex()
        self.assertEqual([v], self.g1.vertices())

        v = self.g2.add_vertex()
        self.assertEqual(self.g2_vertices + [v], self.g2.vertices())

if __name__ == '__main__':
    unittest.main()
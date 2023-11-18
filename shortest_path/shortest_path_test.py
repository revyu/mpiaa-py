import unittest
from graph import Graph  
from shortest_path import shortest_path 

class TestShortestPath(unittest.TestCase):
    def test_empty_graph(self):
        g = Graph()
        self.assertEqual(shortest_path(g, 0, 1), [])

    def test_single_vertex_path(self):
        g = Graph([(0, 1, 2.5), (0, 2, 3.0)])
        self.assertEqual(shortest_path(g, 0, 0), [0])

    def test_one_edge(self):
        g = Graph([(0, 1, 2.5)])
        self.assertEqual(shortest_path(g, 0, 1), [0, 1])

    def test_two_edges(self):
        g = Graph([(0, 1, 2.5), (0, 2, 1.0)])
        self.assertEqual(shortest_path(g, 0, 1), [0, 1])

    def test_three_edges(self):
        g = Graph([(0, 1, 2.5), (0, 2, 1.0), (2, 1, 0.7)])
        self.assertEqual(shortest_path(g, 0, 1), [0, 2, 1])

    def test_many_edges(self):
        g = Graph([(0, 1, 3.0), (1, 2, 0.5), (2, 3, 0.5), (3, 4, 1.0),
                   (0, 2, 2.0), (0, 4, 5.0), (1, 3, 2.0), (2, 4, 2.0)])
        self.assertEqual(shortest_path(g, 0, 4), [0, 2, 3, 4])
        self.assertEqual(shortest_path(g, 4, 0), [4, 3, 2, 0])
        self.assertEqual(shortest_path(g, 1, 4), [1, 2, 3, 4])

    def test_unreachable_vertex(self):
        g = Graph([(0, 1, 2.5), (1, 2, 1.0), (0, 2, 1.0), (3, 4, 0.7)])
        self.assertEqual(shortest_path(g, 0, 4), [])
        self.assertEqual(shortest_path(g, 3, 0), [])

if __name__ == '__main__':
    unittest.main()
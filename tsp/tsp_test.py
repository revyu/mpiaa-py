import unittest
from tsp import TSP,TSP_BnB
from graph import Graph
 
 
 
class TestTSP(unittest.TestCase):
    def test_empty_graph(self):
        g = Graph()
        self.assertEqual(TSP(g,0), [])
        self.assertEqual(TSP_BnB(g,0)[0], [])
 
    def test_single_vertex(self):
        g = Graph()
        g.add_vertex(0)
        self.assertEqual(TSP(g,0), [])
        self.assertEqual(TSP_BnB(g,0)[0], [])
 
    def test_one_edge(self):
        g = Graph([(0, 1, 2.5)])
        result = TSP(g,0)
        expected = [0, 1,0]
        self.assertEqual(result, expected)
        result=TSP_BnB(g,0)[0]
        self.assertEqual(result, expected)
 
    def test_three_vertices_three_edges(self):
        g = Graph([(0, 1, 2.5), (0, 2, 0.5), (1, 2, 1.0)])
        result = TSP(g,0)
        expected = [0, 1, 2,0]
        self.assertEqual(result, expected)
        result = TSP_BnB(g,0)[0]
        self.assertEqual(result, expected)
 
    def test_four_vertices(self):
        g = Graph([(0, 1, 6.0), (0, 2, 4.0), (0, 3, 1.0),
                   (1, 2, 3.5), (1, 3, 2.0),
                   (2, 3, 5.0)])
        result = TSP(g,0)
        expected = [0, 2, 1, 3,0]
 
        self.assertEqual(result, expected)
        result=TSP_BnB(g,0)[0]
        self.assertEqual(result, expected)
 
 
    def test_five_vertices(self):
        g = Graph([(0, 1, 2.0), (0, 2, 4.0), (0, 3, 1.0), (0, 4, 2.5),
                   (1, 2, 3.6), (1, 3, 6.0), (1, 4, 3.0),
                   (2, 3, 7.0), (2, 4, 5.0),
                   (3, 4, 9.0)])
        result = TSP(g,0)
        expected = [0, 3, 2, 1, 4,0]
        self.assertEqual(result, expected)
        result = TSP_BnB(g,0)[0]
        self.assertEqual(result, expected)
 
 
    def test_six_vertices(self):
        g = Graph([(0, 1, 2.0), (0, 2, 4.0), (0, 3, 1.0), (0, 4, 2.5), (0, 5, 3.2),
                   (1, 2, 3.6), (1, 3, 6.0), (1, 4, 3.0), (1, 5, 0.1),
                   (2, 3, 7.0), (2, 4, 5.0), (2, 5, 9),
                   (3, 4, 9.0), (3, 5, 0.5),
                   (4, 5, 1.0)])
        result = TSP(g,0)
        expected = [0, 3, 5, 1, 2, 4,0]
        self.assertEqual(result, expected)
        result = TSP_BnB(g,0)[0]
        self.assertEqual(result, expected)
 
 
if __name__ == '__main__':
 
    unittest.main()
import unittest
from graph import Graph

class TestGraph(unittest.TestCase):
    def empty_graph(self):
        g=Graph()
        self.assertFalse(g.has_vertex(0))
        self.assertFalse(g.has_edge(0,1))

    def one_vertex(self):
        g=Graph()
        g.add_vertex(0)
        self.assertTrue(g.has_vertex(0))
        self.assertFalse(g.has_vertex(1))
        self.assertFalse(g.has_edge(0,1))

    def test_two_vertices(self):
        g = Graph()
        g.add_vertex(0)
        g.add_vertex(1)
        self.assertTrue(g.has_vertex(0))
        self.assertTrue(g.has_vertex(1))
        self.assertFalse(g.has_edge(0, 1))

    def test_one_edge(self):
        g = Graph()
        g.add_edge(0, 1, 5.0)
        self.assertTrue(g.has_vertex(0))
        self.assertTrue(g.has_vertex(1))
        self.assertTrue(g.has_edge(0, 1))
        self.assertTrue(g.has_edge(1, 0))
        self.assertEqual(g.edge_weight(0, 1), 5.0)
        self.assertFalse(g.has_edge(0, 0))
    
    def test_loop(self):
        g = Graph()
        g.add_edge(0, 0)
        g.add_edge(1, 1)
        self.assertTrue(g.has_vertex(0))
        self.assertTrue(g.has_vertex(1))
        self.assertTrue(g.has_edge(0, 0))
        self.assertTrue(g.has_edge(1, 1))

    def test_two_edges(self):
        g = Graph()
        g.add_edge(0, 1)
        g.add_edge(0, 3)
        self.assertTrue(g.has_vertex(0))
        self.assertTrue(g.has_vertex(1))
        self.assertTrue(g.has_vertex(3))
        self.assertTrue(g.has_edge(0, 1))
        self.assertTrue(g.has_edge(0, 3))
        self.assertTrue(g.has_edge(1, 0))
        self.assertTrue(g.has_edge(3, 0))
        self.assertFalse(g.has_edge(1, 3))

    def test_get_vertices(self):
        g = Graph()
        g.add_vertex(0)
        g.add_edge(0, 1)
        g.add_vertex(3)
        self.assertEqual(sorted(g.vertices), [0, 1, 3])

    def test_get_adjacent_vertices(self):
        g = Graph()
        g.add_vertex(0)
        g.add_edge(0, 1)
        g.add_edge(0, 2, 4.5)
        g.add_edge(1, 2, 3.0)
        g.add_edge(1, 3)
        self.assertEqual(sorted(g.get_adjacent_vertices(0)), [1, 2])
        self.assertEqual(sorted(g.get_adjacent_vertices(1)), [0, 2, 3])
        self.assertEqual(sorted(g.get_adjacent_vertices(2)), [0, 1])
        self.assertEqual(sorted(g.get_adjacent_vertices(3)), [1])
        with self.assertRaises(KeyError):
            g.get_adjacent_vertices(4)

    def test_get_adjacent_edges(self):
        g = Graph()
        g.add_edge(0, 1)
        g.add_edge(0, 2, 4.5)
        g.add_edge(1, 2, 3.0)
        g.add_edge(3, 1, 7.2)
        self.assertEqual(sorted(g.get_adjacent_edges(0)), [[0, 1, 0.0], [0, 2, 4.5]])
        self.assertEqual(sorted(g.get_adjacent_edges(1)), [[1, 0, 0.0], [1, 2, 3.0], [1, 3, 7.2]])
        self.assertEqual(sorted(g.get_adjacent_edges(2)), [[2, 0, 4.5], [2, 1, 3.0]])
        self.assertEqual(sorted(g.get_adjacent_edges(3)), [[3, 1, 7.2]])
        with self.assertRaises(KeyError):
            g.get_adjacent_vertices(4)

    def test_replace_an_edge(self):
        g = Graph()
        g.add_edge(1, 5, 3.5)
        g.add_edge(5, 1, 4.7)
        self.assertTrue(g.has_edge(1, 5))
        self.assertTrue(g.has_edge(5, 1))
        self.assertEqual(g.edge_weight(1, 5), 4.7)
        self.assertEqual(g.edge_weight(5, 1), 4.7)

    def test_remove_vertices_and_edges(self):
        g = Graph()
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(0, 3)
        g.add_edge(0, 4)
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 3)
        g.add_edge(2, 4)
        g.remove_vertex(2)
        self.assertFalse(g.has_vertex(2))
        with self.assertRaises(KeyError):
            g.has_edge(1,2)
        with self.assertRaises(KeyError):
            g.has_edge(3,2)
        
        with self.assertRaises(KeyError):
            g.has_edge(2,4)
        self.assertTrue(g.has_edge(0, 1))
        self.assertTrue(g.has_edge(0, 4))
        self.assertTrue(g.has_edge(1, 3))
        g.remove_edge(0, 1)
        self.assertFalse(g.has_edge(0, 1))
        self.assertTrue(g.has_vertex(0))
        self.assertTrue(g.has_vertex(1))

if __name__ == '__main__':
    unittest.main()
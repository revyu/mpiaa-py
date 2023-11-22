import unittest
from graph import Graph

from min_spanning_tree import kruskal

def to_set(lis):
    result=set()
    for l in lis:
        result.add(frozenset(l))

# переписать с ребрами bloodtrail 
class TestKruskal(unittest.TestCase):

    def test_empty_graph(self):#ok
        g = Graph()
        k = Graph()
        self.assertEqual(to_set(kruskal(g).get_all_edges()), to_set(k.get_all_edges()))

    def test_single_vertex_graph(self):#ok
        g = Graph()
        g.add_vertex(0)
        k= Graph()
        self.assertEqual(to_set(kruskal(g).get_all_edges()), to_set(k.get_all_edges()))

    def test_one_edge(self): #ok
        g = Graph([(0, 1, 2.5)])
        k= Graph([(0,1,2.5)])
        self.assertEqual(to_set(kruskal(g).get_all_edges()), to_set(k.get_all_edges()))

    def test_two_edges(self):#
        g = Graph([(0, 1, 2.5), (1, 2, 1.0)])
        k = Graph([(0, 1, 2.5), (1, 2, 1.0)])
        self.assertEqual(to_set(kruskal(g).get_all_edges()), to_set(k.get_all_edges()))

    def test_three_edges(self):
        g = Graph([(0, 1, 2.5), (1, 2, 1.0), (0, 2, 0.7)])
        k = Graph([(0, 2,0.7), (1, 2,1.0)])
        self.assertEqual(to_set(kruskal(g).get_all_edges()), to_set(k.get_all_edges()))

    def test_many_edges(self):
        g = Graph([(0, 1, 4.0), (0, 7, 9.0),
                   (1, 2, 8.0), (1, 7, 11.0),
                   (2, 3, 7.0), (2, 5, 4.0), (2, 8, 2.0),
                   (3, 4, 9.0), (3, 5, 14.0),
                   (4, 5, 10.0),
                   (5, 6, 2.0),
                   (6, 7, 1.0), (6, 8, 6.0),
                   (7, 8, 7.0)])
        k= Graph([(0, 1, 4.0),
                  (1, 2, 8.0),
                  (2, 3, 7.0),(2, 5, 4.0),(2, 8, 2.0),
                  (3, 4, 9.0),
                  (5, 6, 2.0),
                  (6, 7, 1.0)
                ])
        self.assertEqual(to_set(kruskal(g).get_all_edges()), to_set(k.get_all_edges()))

if __name__ == '__main__':
    unittest.main()
from graph import Graph
from tsp import TSP,TSP_BnB,TSP_greedy


g = Graph([(0, 1, 4.0), (0, 7, 9.0),
                   (1, 2, 8.0), (1, 7, 11.0),
                   (2, 3, 7.0), (2, 5, 4.0), (2, 8, 2.0),
                   (3, 4, 9.0), (3, 5, 14.0),
                   (4, 5, 10.0),
                   (5, 6, 2.0),
                   (6, 7, 1.0), (6, 8, 6.0),
                   (7, 8, 7.0)])

print(TSP_greedy(g,0))
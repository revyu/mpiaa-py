import numpy as np
from graph import Graph
from shortest_path import shortest_path

g = Graph([(0, 1, 3.0), (1, 2, 0.5), (2, 3, 0.5), (3, 4, 1.0),
           (0, 2, 2.0), (0, 4, 5.0), (1, 3, 2.0), (2, 4, 2.0)])




print(shortest_path(g,0,4))
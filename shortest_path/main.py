import numpy as np
import numpy.random as r
from graph import Graph
from shortest_path import shortest_path
import time

def get_random_graph(size:int)-> Graph:
    g=Graph()
    #будем добавлять вершины по одной на каждом шаге сохраняя связность
    g.add_vertex(g.order)
    g.add_vertex(g.order)
    g.add_edge(1,2)
    while g.order<size:


        add_new=r.rand()<0.2
        #добавлять ли новую вершину
        if  add_new:
            v=r.choice(list(g.vertices.keys()))
            g.add_vertex(g.order)
            g.add_edge(v,g.order,r.randint(2))
        else:
            v=r.choice(list(g.vertices.keys()))
            u=r.choice(list(g.vertices.keys()-[v]))
            g.add_edge(v,u,r.randint(20))
    
    return g
            

for size in range(2,7):
    #size
    summ=0
    for i in range(10):
        g=get_random_graph(5**size)
        start=time.time()
        shortest_path(g,0,g.order)
        end=time.time()
        summ+=(start-end)
    print(f"overall time for size:{5**size} is {summ/10}")
        
    






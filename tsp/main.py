from tsp import TSP,TSP_BnB,TSP_greedy,two_opt_improve,TSP_LS,TSP_Gen
from graph import Graph
from numpy import random as r
import time
import numpy as np

def get_Kn(n:int):
    edges=[]
    for i in range(n-1):
        for j in range(i+1,n):
            edges.append([i,j,r.randint(0,20)])
    return Graph(edges)

def get_len_path(g:Graph,path:list):
    weight=0
    current=path[0]
    for i in range(1,len(path)):
        weight+=g.edge_weight(current,path[i])
        current=path[i]
    return weight

r.seed(161)

for i in range(6,10):
    g=get_Kn(i)
    start=time.time()
    path=TSP(g,0)
    end=time.time()
    print(f"For size{i} time TSP is {end-start} with weight {get_len_path(g,path)}")


    start=time.time()
    path,weight=TSP_BnB(g,0)
    end=time.time()
    print(f"For size{i} time TSP_BnB is {end-start} with weight {weight}")

    start=time.time()
    path=TSP_greedy(g,0)
    end=time.time()
    print(f"For size{i} time TSP_greedy is {end-start} with weight {get_len_path(g,path)}")

    start=time.time()
    path=TSP_LS(g)
    end=time.time()
    print(f"For size{i} time TSP_LS is {end-start} with weight {get_len_path(g,path)}")

    start=time.time()
    path,weight=TSP_Gen(g,i//2,i//3,20,0.5)
    end=time.time()
    print(f"For size{i} time TSP_gen is {end-start} with weight {weight}")
    print("\n\n")


def doit():
    for i in range(4,10):
        g=get_Kn(i*3)


        start=time.time()
        path=TSP_LS(g)
        end=time.time()
        print(f"For size{i*3} time TSP_LS is {end-start} with weight {get_len_path(g,path)}")




        start=time.time()
        path,weight=TSP_Gen(g,i//2,i//2,20,0.5)
        end=time.time()
        print(f"For size{i*3} time TSP_Gen is {end-start} with weight {weight}")

        print("\n\n")

doit()







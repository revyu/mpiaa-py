from graph import Graph
from itertools import permutations as ps
from math import inf

def TSP(g:Graph,start_vertex):
    paths=ps(g.vertices.keys()-[start_vertex])
    paths=[list(path) for path in paths]
    for i in range(len(paths)):#замкнули пути
        paths[i]=[start_vertex]+paths[i]+[start_vertex]

    min_weight=inf
    min_path=[]
    
    for path in paths:
        weight=0
        current=path[0]
        path_is_valid=True
        for v in range(1,len(path)):
            if g.has_edge(current,path[v]):
                weight+=g.edge_weight(current,path[v])
                current=path[v]
            else:
                path_is_valid=False
                break
        
        if weight<min_weight and path_is_valid:
            min_weight=weight
            min_path=path
    
    return min_path

def lower_bound(graph,path):
    lower_bound = 0
    
    # добавляем веса посещенных ребер
    for i in range(len(path) - 1):
        lower_bound += graph.edge_weight(path[i], path[i + 1])
    
    # добавляем минимальные веса для завершения пути через все вершины
    for vertex in graph.vertices.keys():
        if vertex not in path:
            min_weight = min(graph.edge_weight(path[-1], v) for v in graph.vertices.keys() if v != path[-1])
            lower_bound += min_weight
    
    return lower_bound


def BnB(graph, current_path, current_cost, min_path, min_cost):
    # если путь содержит все вершины, проверяем и обновляем минимальный путь и его стоимость
    if len(current_path) == len(graph.vertices):
        current_cost += graph.edge_weight(current_path[-1], current_path[0])  # замыкаем путь
        if current_cost < min_cost:
            return current_path + [current_path[0]], current_cost # замыкаем путь
        else:
            return min_path, min_cost
    
    # разветвление - перебираем все вершины, которые еще не входят в путь
    for vertex in graph.vertices.keys():
        if vertex not in current_path:
            new_path = current_path + [vertex]
            new_cost = current_cost + graph.edge_weight(current_path[-1], vertex)
            if lower_bound(graph,new_path) < min_cost:  # проверяем, стоит ли продолжать разветвление
                min_path, min_cost = BnB(graph,new_path, new_cost, min_path, min_cost)
    
    return min_path, min_cost

def TSP_BnB(graph,start):
    
    if graph.order<2:
        return [] , 0
    
    initial_path = [start]
    initial_cost = 0
    min_path,min_cost= BnB(graph,initial_path, initial_cost, initial_path, float('inf'))
    
    return min_path , min_cost


def TSP_greedy(g:Graph,start):
    current=start
    path=[current]
    
    while len(path)!=len(g.vertices.keys()):
        min_weight=inf
        for v in g.get_adjacent_vertices(current):
            if v not in path and g.edge_weight(v,current)<min_weight:
                min_weight=g.edge_weight(v,current)
                next_vertex=v
        if next_vertex!=current:
            path.append(next_vertex)
        else:
            return []
        current=next_vertex


    return path
                


if __name__=="__main__":

    g = Graph([(0, 1, 4.0), (0, 7, 9.0),
                   (1, 2, 8.0), (1, 7, 11.0),
                   (2, 3, 7.0), (2, 5, 4.0), (2, 8, 2.0),
                   (3, 4, 9.0), (3, 5, 14.0),
                   (4, 5, 10.0),
                   (5, 6, 2.0),
                   (6, 7, 1.0), (6, 8, 6.0),
                   (7, 8, 7.0)]) 
    print(TSP(g,0))

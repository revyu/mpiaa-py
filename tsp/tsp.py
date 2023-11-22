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

def get_len_path(g,path):
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
    
    if path_is_valid:
        return weight
    else:
        return inf

def lower_bound(g,visited:list):
    edges_from_path=[]
    current=visited[0]
    for i in range(len(visited)):
        edges_from_path.append([current,visited[i],g.edge_weight(current,visited[i])])
    
    graph_of_path=Graph(edges_from_path)

    total_weight=0

    for v in g.vertices:
        #dirt так как будем убирать копии ребер
        #сначала пишем смотрим на ребра из path потом на ребра из остального графа
        preferable_edges_dirt=sorted(graph_of_path.get_adjacent_edges(v),key=lambda i:i[2])
        preferable_edges_dirt=preferable_edges_dirt+sorted(g.get_adjacent_edges(v),key=lambda i:i[2])
        preferable_edges=[]
        for edge in preferable_edges_dirt:
            if not(edge in preferable_edges or [edge[1],edge[0],edge[2]] in preferable_edges):
                preferable_edges.append(edge)

        
        if len(preferable_edges)<2:
            return inf
        else:
            total_weight+=preferable_edges[0][2]
            total_weight+=preferable_edges[1][2]
    
    return total_weight/2
        

def BnB(g,visited:list,best_path):
    if len(visited)==len(g.vertices.keys()):
        return min(get_len_path(g,best_path),get_len_path(g,visited))
    for v in set(g.vertices.keys())-set(visited):
        vnext=visited+[v]
        if lower_bound(g,vnext)<get_len_path(best_path):
            path=BnB(g,visited,best_path)
            best_path=min(get_len_path(path),get_len_path(best_path))
    return best_path


#все написано максимально по псевдокоду читай методичку
def TSP_BnB(g,start):
    best_path=[]
    visited=[start]
    return BnB(g,visited,best_path)


                


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

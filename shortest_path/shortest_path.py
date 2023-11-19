from graph import Graph
from math import inf

#https://chat.openai.com/share/4ec5963e-e542-471c-9dd1-d0cd08507fb1
def shortest_path(graph, start, end):
    Q=graph.vertices.copy()
    distances = {vertex: inf for vertex in graph.vertices.keys()}
    distances[start] = 0
    parents = {} # parents[u]=v

    while Q:
        u = min(Q, key=lambda vertex: distances[vertex])
        #выбрали вершину из Q с минимальной меткой  

        if u == end:
            return build_path(parents, start, end)

        del Q[u]

        for v in graph.get_adjacent_vertices(u):
            if distances[v] > distances[u] + graph.edge_weight(u, v):
                distances[v] = distances[u] + graph.edge_weight(u, v)
                parents[v] = u

    return build_path(parents, start, end)

def build_path(parents, start, end):
    path = []
    current = end

    while current != start:
        path.append(current)
        current = parents.get(current) #если ключа нет то вернет none

        if current is None:
            return []

    path.append(start)
    path.reverse()
    return path

            
                 


    
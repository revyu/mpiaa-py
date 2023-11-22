from graph import Graph

def unity(g,k)->Graph:
    U=Graph(g.get_all_edges()) #создали копию g
    k_edges=k.get_all_edges()
    for edge in k_edges:#добавили все ребра из k в U
        U.add_edge(edge[0],edge[1],edge[2])
    return U


def kruskal(g:Graph)->Graph:

    CCS={i: Graph() for i in g.vertices} 
    #Connected Components

    MST=Graph()

    #получим все ребра графа
    edges=g.get_all_edges()
    

    for edge in edges:
        u=edge[0]
        v=edge[1]

        if not(CCS[u].has_vertex(v)):
            CCS[u].add_edge(edge[0],edge[1],edge[2])
            CCS[u]=unity(CCS[u],CCS[v])
            # в питоне нет указателей так что приходится вручную 
            # обновлять компоненты связности для каждой вершины 
            for vertex in CCS[u].vertices:
                CCS[vertex]=CCS[u]

            MST.add_edge(edge[0],edge[1],edge[2])
            

    return MST
        
        

from graph import Graph
from math import inf


def build_path(parent:list ,start_vertex:int,end_vertex:int ):
    return parent

def shortest_path(g:Graph,start_vertex,end_vertex)->list:
    # Return shortest path in the graph from start vertex to end vertex as array of vertices.
    # First item in the result should be start vertex, last - end vertex.
    # Return empty array if there is no path.

    # Your implementation here.
    distances=[inf for i in g.vertices.keys()]

    distances[start_vertex]=0
    min_dist=0
    min_vertex=start_vertex

    visited=set()

    parent=[]
    while len(visited)!=g.order:
        #из ещё не посещённых вершин выбирается вершина min_vertex  имеющая минимальную метку.
        for i in g.vertices:
            if (i not in visited) and (distances[i]<min_dist):
                min_dist=distances[i]
                min_vertex=i
        
        #Мы рассматриваем всевозможные маршруты, в которых min_vertex является предпоследним пунктом.
        #Для каждого соседа вершины min_vertex, кроме отмеченных как посещённые, рассмотрим новую длину пути, 
        # равную сумме значений текущей метки min_vertex и длины ребра, соединяющего min_vertex с этим соседом.


        for i in g.get_adjacent_vertices(min_vertex):
            if (i not in visited) and distances[i]>distances[min_vertex]+g.edge_weight(min_vertex,i):
                # Если полученное значение длины меньше значения метки соседа, 
                # заменим значение метки полученным значением длины
                distances[i]=distances[min_vertex]+g.edge_weight(min_vertex,i)
                parent.append(i)
        
        visited.add(min_vertex)

        return [start_vertex]+parent
                

                


    
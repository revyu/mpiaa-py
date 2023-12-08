from graph import Graph
from itertools import permutations as ps
from math import inf
from numpy import random as r

def isequal(list1,list2):
    if len(list1)!=len(list2):
        return False
    for i in range(len(list1)):
        if list1[i]!=list2[i]:
            return False
    
    return True

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

def get_weight(g:Graph,path):
    weight=0
    current=path[0]
    for i in range(1,len(path)):
        next=path[i]
        weight+=g.edge_weight(current,next)
        current=next
    return weight
        
def transform(path,a,b,c,d):
    path_dict={path[i]:path[(i+1)%len(path)] for i in range(len(path)-1)}
    #от родителя к предку
    path_dict_reversed={path[(i+1)%len(path)]:path[i] for i in range(len(path)-1)}
    #от предка к родителю

    new_path=[]

    new_path.append(a)

    current=c
    while current!=b:
        new_path.append(current)
        current=path_dict_reversed[current]
    else:
        new_path.append(current)

    current=d
    while current!=a:
        new_path.append(current)
        current=path_dict[current]
    else:
        new_path.append(current)

    return new_path 


def two_opt_improve(g:Graph,path):

    edges_from_path=[[path[i],path[(i+1)%len(path)]] for i in range(len(path)-1)]
    non_adjacent_edges=[]

    for i in edges_from_path:
        for j in edges_from_path:
            a,b=i
            c,d=j
            if len(set([a,b,c,d]))==4:
                non_adjacent_edges.append([[a,b],[c,d]])


    for i in non_adjacent_edges:
        a=i[0][0]
        b=i[0][1]
        c=i[1][0]
        d=i[1][1]
        old_weight=g.edge_weight(a,b)+g.edge_weight(c,d)
        new_weight=g.edge_weight(a,c)+g.edge_weight(b,d)
        if new_weight<old_weight:
            return transform(path,a,b,c,d)
    
    return path

        
                 
def TSP_LS(g:Graph):
    path=list(g.vertices.keys())
    path=path+[path[0]]#замкнули путь
    while True:
        improved_path=two_opt_improve(g,path)
        while get_weight(g,improved_path)<get_weight(g,path):
            path=improved_path
        else:
            return path

def SUS(generation,generation_weights,N):
    F=0
    for i in generation_weights:
        F+=i
    dist=F/N
    start=r.rand()*dist
    chosen=[]
    k=0
    sumweight=generation_weights[0]
    for i in range(N):
        point=start+i*dist
        while sumweight<point:
            k+=1
            sumweight+=generation_weights[k]
        chosen.append(generation[k])
    return chosen



def CrossoverER(g:Graph,dad,mom):
    

    edges_from_dad=[]
    edges_from_mom=[]

    current_dad=dad[0]
    current_mom=mom[0]
    for i in range(1,len(dad)):#получаем ребра из путей   mom и dad
        next_dad=dad[i]
        next_mom=mom[i]
        edges_from_dad.append([current_dad,next_dad,g.edge_weight(current_dad,next_dad)])
        edges_from_mom.append([current_mom,next_mom,g.edge_weight(current_mom,next_mom)])
        current_dad=next_dad
        current_mom=next_mom
    
    edge_map={i:[] for i in g.vertices.keys()}

    for i in g.vertices.keys():
        for j in edges_from_dad:
            if j[0]==i or j[1]==i:# проверка смежности
                edge_map[i].append(j)
        for j in edges_from_mom:
            if j[0]==i or j[1]==i:# проверка смежности
                edge_map[i].append(j)
    

    offspring=[]

    current=r.choice(list(g.vertices.keys()))
    offspring.append(current)
    
    while len(offspring)<len(dad)-1:
        edges=[]
        
        #аналог numpy.flatten()
        for key in edge_map:
            edges.extend(edge_map[key])



        candidates=Graph(edges).get_adjacent_vertices(current)

        #здесь сложное поведение массива когда удаляем ребро из него его размер
        #сокращается изза этого иногда не удаляется второе ребро
        #поэтому приходится неявно изменять счетчик
        
        for j in edge_map.keys():
            e=0
            while e<len(edge_map[j]):# ищем смежные с current вершины в edge map и удаляем их
                if current==edge_map[j][e][0] or current==edge_map[j][e][1]:
                    edge_map[j].remove(edge_map[j][e])
                    e-=1
                e+=1
       
        
        # сколько раз встречается в edge_map
        found_in_edge_map={i:0 for i in candidates}

        for i in candidates:
            for j in edge_map.keys():
                for edge in edge_map[j]:
                    if edge[0]==i or edge[1]==i:# проверка смежности
                        found_in_edge_map[i]+=1

        next=min(found_in_edge_map, key=found_in_edge_map.get)

        current=next
        offspring.append(current)

    return offspring+[offspring[0]]
        

def TSP_Gen(g:Graph,p:int,N:int,maxIt:int,pm:float):
    
    v=list(g.vertices.keys())
    generation=[]
    generation_weights=[0 for i in range(p)]
    for i in range(p):
        r.shuffle(v) #перемешивает маршрут
        _=v+[v[0]]
        generation.append(_)
        
        
    
    for i in range(maxIt):
        max_weight=0
        for i in range(p):
            generation_weights[i]=get_weight(g,generation[i])
            if generation_weights[i]>max_weight:
                max_weight=generation_weights[i]
        
        
        for i in range(p):
            generation_weights[i]=max_weight-generation_weights[i]


        parents=SUS(generation,generation_weights,N)
        childs=[]
        for i in range(p):
            dad=parents[r.randint(0,len(parents)-1)]
            mom=parents[r.randint(0,len(parents)-1)]
            
            childs.append(CrossoverER(g,dad,mom))
        
        for i in range(p):
            if r.rand()>pm:
                childs[i]=two_opt_improve(g,childs[i])
        generation=childs
    

    min_weight=inf
    min_ind=0
    
    for i in range(p):
        weight=get_weight(g,generation[i])
        if weight<min_weight:
            min_weight=weight
            min_ind=i
    
    return generation[min_ind],min_weight

if __name__=="__main__":

    g = Graph([(0, 1, 4.0), (0, 2, 3.0),(0,3,4),
                   (1, 2, 8.0), (1, 3, 11.0),
                   (2, 3, 7.0)]) 
    import random
    for i in range(10):
        print(random.choices([0,1],k=2))
    #print(TSP_Gen(g,p=5,N=3,maxIt=20,pm=0.5))

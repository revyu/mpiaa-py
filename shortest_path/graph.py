import numpy as np

 
class Graph():
    def __init__(self,_edges:list=[]):
        self.order:int=0 
        #извлекли номера вершин из списка ребер , выкинули копии
        self.weight_matrix:np.array=np.full((self.order,self.order),np.nan)
        self.vertices:dict={}
        for edge in _edges:
            self.add_edge(edge[0],edge[1],edge[2])

    def has_vertex(self,vertex):
        return vertex in self.vertices       
         
    def add_vertex(self,vertex):
        if(not self.has_vertex(vertex)):
            self.order+=1# увеличили порядок на 1
            self.vertices[vertex]=self.order-1 
            #добавили новую вершину в словарь вершин(-1 т.к первая вершина 
            # отвечает за нулевую строчку в матрице весов)
            self.weight_matrix=np.pad(self.weight_matrix,((0,1),(0,1)), mode="constant",constant_values=np.nan)
            #расширили матрицу весов

    def add_edge(self,start_vertex,end_vertex,weight=0):
        self.add_vertex(start_vertex)
        self.add_vertex(end_vertex)
        self.weight_matrix[self.vertices[start_vertex]][self.vertices[end_vertex]]=weight
        self.weight_matrix[self.vertices[end_vertex]][self.vertices[start_vertex]]=weight

    def get_adjacent_vertices(self,src_vertex)->list:
        result:list=[]
        if not self.has_vertex(src_vertex):
            raise KeyError(f"Vertex {src_vertex} not in {self}")
        for i in range(self.order):
            if self.has_edge(src_vertex,self.vertices[i]):
                result.append(self.vertices[i])
        return result
    
    def get_adjacent_edges(self,src_vertex)->list:
        result:list=[]
        if not self.has_vertex(src_vertex):
            raise KeyError(f"Vertex {src_vertex} not in {self}")
        for i in range(self.order):
            if self.has_edge(src_vertex,self.vertices[i]):
                result.append([self.vertices[src_vertex],
                               self.vertices[i],
                               self.weight_matrix[self.vertices[src_vertex]][i]])
        return result
    
    def has_edge(self,start_vertex,end_vertex)->bool:
        weight=self.weight_matrix[self.vertices[start_vertex]][self.vertices[end_vertex]]
        return weight==weight
    
    def edge_weight(self,start_vertex,end_vertex):
        weight=self.weight_matrix[self.vertices[start_vertex]][self.vertices[end_vertex]]
        if weight!=weight:
            raise KeyError(f"Edge {start_vertex, end_vertex} not in {self}")
        else:
            return weight



    def remove_vertex(self,vertex):
        #adjacent_vertexs:list=self.get_adjacent_vertices(vertex)
        #for i in adjacent_vertexs:
            #self.remove_edge(vertex,i)
        #удалили все инцидентные ребра
        index:int =self.vertices[vertex]
        self.weight_matrix=np.delete(np.delete(self.weight_matrix, index, axis=0), index, axis=1)
        #удалили соответствующий вершине столбец и строку  

        for i in range(index+1,self.order):
            self.vertices[i]-=1
        
        del self.vertices[vertex]
        #сдвинули метки соответсвующих вершин

        self.order-=1

    def remove_edge(self,start_vertex,end_vertex):
        self.weight_matrix[self.vertices[start_vertex]][self.vertices[end_vertex]]=np.nan
        self.weight_matrix[self.vertices[end_vertex]][self.vertices[start_vertex]]=np.nan


if __name__=="__main__":
    pass



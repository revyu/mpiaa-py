import numpy as np

#запрещены пути с нулевой 
class Graph():
    def __init__(self,_edges:list=[]):
        self.order:int=0 
        #извлекли номера вершин из списка ребер , выкинули копии
        self.weight_matrix:np.array=np.zeros((self.order,self.order))
        self.vertices:dict=()
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
            self.weight_matrix=np.pad(self.weight_matrix,((0,1),(0,1)), mode="constant",constant_values=0)
            #расширили матрицу весов

    def add_edge(self,start_vertex,end_vertex,weight):
        self.add_vertex(start_vertex)
        self.add_vertex(end_vertex)
        self.weight_matrix[self.vertices[start_vertex]][self.vertices[end_vertex]]=weight

    def get_adjacent_vertices(self,src_vertex)->list:
        result:list=[]
        for i in range(len(self.order)):
            if self.weight_matrix[self.vertices[src_vertex]][i]!=0:
                result.append(self.vertices[i])
        return result
    
    def get_adjacent_edges(self,src_vertex)->list:
        result:list=[]
        for i in range(len(self.order)):
            if self.weight_matrix[self.vertices[src_vertex]][i]!=0:
                result.append([self.vertices[src_vertex],
                               self.vertices[i],
                               self.weight_matrix[self.vertices[src_vertex]][i]])
        return result
    
    def has_edge(self,start_vertex,end_vertex)->bool:
        return self.weight_matrix[self.vertices[start_vertex]][self.vertices[end_vertex]]!=0
    
    def remove_vertex(self,vertex):
        adjacent_vertexs:list=self.get_adjacent_vertex(vertex)
        for i in adjacent_vertexs:
            self.remove_edge(vertex,i)
        #удалили все инцидентные ребра
        index:int =self.vertices[vertex]
        np.delete(np.delete(self.weight_matrix, index, axis=0), index, axis=1)
        #удалили соответствующий вершине столбец и строку  

        for i in range(index+1,self.order):
            self.vertices[i]-=1
        #сдвинули метки соответсвующих вершин

        self.order-=1

    def remove_edge(self,start_vertex,end_vertex):
        self.weight_matrix[self.vertices[start_vertex]][self.vertices[end_vertex]]=0


if __name__=="__main__":
    pass



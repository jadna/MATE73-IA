from collections import defaultdict
from collections import deque

class Graph:
    
    def __init__(self, n):

        """ Numero de vertices """
        self.vertices = n
        
        """ Dicionario default do Grafo"""
        self.graph = defaultdict(list)

    def addEdge(self, u, v):

        """ Função que add aresta ao vertice 
            O grafo é direcionado"""
        self.graph[u].append(v) 
        #self.graph[v] = list()
        self.graph[v].append(u) 
        graph = self.graph


        return graph


    def bfs(self, graph, start, end):
        """ Encontra o menos caminho entre start e end
        Se o caminho não existir retorn none """
        if start == end:
            return [start]
        visited = {start}
        queue = deque([(start, [])])

        while queue:
            current, path = queue.popleft()
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor == end:
                    return path + [current, neighbor]
                if neighbor in visited:
                    continue
                queue.append((neighbor, path + [current]))
                visited.add(neighbor)   
        return None  


vertices, edge = input().split()
vertices = int(vertices)
edge = int(edge)

bfs = Graph(vertices)

i = 0
while i < edge:
    u, v = input().split()
    graph = bfs.addEdge(u, v)
    i += 1

print(graph)
""" Define os nos de incio e fim e imprime os caminhos """
start, end = input().split()


bfs_result = bfs.bfs(graph,start, end)
print(bfs_result)


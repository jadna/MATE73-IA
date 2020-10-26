from collections import defaultdict


class Graph:

    def __init__(self, n_vertices):

        """ Numero de vertices """
        self.vertices = n_vertices
        #print(type(self.vertices))

        """ Dicionario default do Grafo"""
        self.graph = defaultdict(list)

    def add_edge(self, u, v):

        graph = self.graph

        """ Função que add aresta ao vertice """
        graph[u].append(v) 
        print(graph)

    def all_paths(self, u, d, visited, path): 

         """ Uma função recursiva para imprimir todos os caminhos do nó inicial ao nó final.
            visited mantém o controle dos vértices no caminho atual.
            path armazena vértices reais e path_index é indice atual do caminho """ 
        
        visited[u] = True
        path.append(u) 

        """ Imprime se o vertice atual for igual ao vertice destino"""
        if u == d: 
            print (path) 
        else: 
            """ Se o vertice atual nao for o de destino, pecorre todos os vertices adjacentes ao vertice atual """ 
            for i in self.graph[u]: 
                if visited[i] == False: 
                    self.all_paths(i, d, visited, path) 

        # Remove current vertex from path[] and mark it as unvisited 
        path.pop() 
        visited[u]= False







""" Pega o numero de nos e relacoes """
num_nodes, num_relations = input().split()
num_nodes = int(num_nodes)
num_relations = int(num_relations)

dfs = Graph(num_nodes)

""" Laco para salvar as relacoes """
i = 0
while i < num_relations:

    """ a e o no, b nos relacionais com a"""
    u, v = input().split()

    dfs.add_edge(u, v)

    i += 1

""" Define os nos de incio e fim e imprime os caminhos """
start, end = input().split()
start = int(start)
end = int(end)
#dfs.print_paths(start, end)


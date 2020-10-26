from collections import deque

def bfs2(graph, start, goal):
    """
    finds a shortest path in undirected `graph` between `start` and `goal`. 
    If no path is found, returns `None`
    """
    if start == goal:
        return [start]
    visited = {start}
    queue = deque([(start, [])])

    while queue:
        current, path = queue.popleft()
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor == goal:
                return path + [current, neighbor]
            if neighbor in visited:
                continue
            queue.append((neighbor, path + [current]))
            visited.add(neighbor)   
    return None  # no path found. not strictly needed

def add_edge(u, v):

    """ Função que add aresta ao vertice """
    graph[u].append(v) 
    graph[v] = list()
    print("add_edge graph[u]: {}".format(graph[u]))

    return graph

if __name__ == '__main__':
    graph = {
        'A': set(['B', 'C']),  
        'B': set(['A', 'D', 'E']),
        'C': set(['A', 'F']),   
        'D': set(['B']),     
        'E': set(['B', 'F']),             
        'F': set(['C', 'E']),
    }

    print(graph)
    #graph = add_edge()
    """ Pega o numero de nos e relacoes """
    num_nodes, num_relations = input().split()
    num_nodes = int(num_nodes)
    num_relations = int(num_relations)

    #dfs = Graph(num_nodes)

    """ Laco para salvar as relacoes """
    i = 0

    while i < num_relations:

        a, b = input().split()
        
        add_edge(a, b)

        i += 1

    """ Define os nos de incio e fim e imprime os caminhos """
    start, end = input().split()
    """start = int(start)
    end = int(end)"""

    path = bfs2(graph, 'A', 'F')
    if path:
        print(path)
    else:
        print('no path found')
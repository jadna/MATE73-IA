from collections import defaultdict

def readGraph():
    graph = defaultdict(list)

    # Nó e Relações unidirecionais
    entry = input().rstrip()
    nodes, rel = entry.split(' ')
    
    # Insere relações
    for i in range(1, int(rel)+1):

        entry = input().rstrip()
        a, b = entry.split(' ')

        graph[int(a)].append(int(b))
     
    return graph

def __findPathDFS(graph, current, goal, visited):
    if current == goal:
        return [current]
    
    if current in graph:
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add( neighbor )
                path = __findPathDFS(graph, neighbor, goal, visited)
                
                if path is not None:
                    path.insert(0, current)
                    return path

    return None
    
def findPathDFS(graph, start, goal):

    if start in graph or goal in graph:
        return False
    
    #visited = set()
    visited = {start}
    
    return __findPathDFS(graph, start, goal, visited)
    

# Nó e Relações unidirecionais
"""entry = input().rstrip()
nodes, rel = entry.split(' ')
rel = int(rel)

graph = defaultdict(list)

# Insere relações
i = 1
while i <= rel:
    entry = input().rstrip()
    a, b = entry.split(' ')
    graph[str(a)].append(str(b))

    i += 1

# Le início e objetivo
entry = input().rstrip()
start, goal = entry.split(' ')"""
#start = int(start)
#goal = int(end)

graph = readGraph()

# Le início e objetivo
entry = input().rstrip()
start, goal = entry.split(' ')

print( findPathDFS(graph, int(start), int(goal)) )
from collections import defaultdict

def __findPathDFS(graph, current, goal, visited):
    if current == goal:
        return [current]
    
    if current in graph:
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                print("visited{}".format(visited))
                path = __findPathDFS(graph, neighbor, goal, visited)
                if path is not None:
                    path.insert(0, current)
                    print(path)
                    return path

    return None

def findPathDFS(graph, start, goal):

    print(graph)
    print(start)
    print(goal)
    if start not in graph or goal not in graph:
        return False
    
    visited = set()
    visited = {start}
    
    return __findPathDFS(graph, start, goal, visited)

# Nó e Relações unidirecionais
entry = input().rstrip()
nodes, rel = entry.split(' ')
rel = int(rel)

graph = defaultdict(list)

# Insere relações
i = 1
while i <= rel:
    entry = input().rstrip()
    a, b = entry.split(' ')
    graph[str(a)].append(str(b))
    graph[str(b)].append(str(a))

    i += 1

# Le início e objetivo
entry = input().rstrip()
start, goal = entry.split(' ')

result = findPathDFS(graph, str(start), str(goal))
print("-".join(result))
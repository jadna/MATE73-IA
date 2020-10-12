from collections import defaultdict
from collections import deque

def dfs(graph, start, end):
    """ Encontra o menor caminho entre start e end
    Se o caminho não existir retorn none """
    if start == end:
        return [start]

    visited = {start}
    queue = deque([(start, [])])

    while queue:
        current, path = queue.popleft()
        visited.add(current)
        if current == end:
            result = path + [current]
            return result

        for neighbor in graph[current]:
            if neighbor == end:
                result = path + [current, neighbor]

                result = list(visited)
                result.append(neighbor)
                result.sort(key=int)
            
                return result
                
            if neighbor in visited:
                continue
            queue.append((neighbor, path + [current]))
            visited.add(neighbor)  
            #print("visited: {}".format(visited))
            #print("queue: {}".format(queue)) 
    return None


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

    i += 1

# Le início e objetivo
entry = input().rstrip()
start, end = entry.split(' ')

dfs_result = dfs(graph, start, end)
result = "-".join(dfs_result)
print(result)


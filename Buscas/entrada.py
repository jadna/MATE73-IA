from collections import defaultdict 



def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        teste = graph[vertex] - set(path)
        for next in teste:
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))
    print(path)

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
start, goal = entry.split(' ')

list(dfs_paths(graph, 1, 3))
#dfs_result = dfs_paths(graph, start, goal)
#result = "-".join(dfs_result)
#print(result)


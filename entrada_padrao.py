from collections import defaultdict

# Nó e Relações unidirecionais
entry = input().rstrip()
nodes, rel = entry.split(' ')

graph = defaultdict(list)

# Insere relações
for i in range(1, int(rel)+1):
    entry = input().rstrip()
    a, b = entry.split(' ')
    graph[str(a)].append(str(b))

print(graph)
# Le início e objetivo
entry = input().rstrip()
start, objective = entry.split(' ')
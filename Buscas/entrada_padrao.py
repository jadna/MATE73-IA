from collections import defaultdict

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

print(graph)
# Le início e objetivo
entry = input().rstrip()
start, objective = entry.split(' ')
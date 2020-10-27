from collections import defaultdict


entry = input().rstrip()
nodes, rel = entry.split(' ')
rel = int(rel)
nodes = int(nodes)

#graph = {}
graph = defaultdict(list)
folhas = defaultdict(list)

for i in range(rel):
    entry = input().rstrip()
    a, b = entry.split(' ')

    graph[a].append(b)
    folhas[b]


n = input().rstrip()
n = int(n)

for i in range(n):
    entry = input().rstrip()
    a, b = entry.split(' ')

    if(a in folhas):
        folhas[a].append(b)

# Elimina as folhas vazias
folhas = { key: folhas[key] for key in folhas if folhas[key] != [] }

print(graph)
print(folhas)

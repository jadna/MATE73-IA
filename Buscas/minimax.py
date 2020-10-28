from collections import defaultdict

# Toggle True => Max, False=> Min
def minimax(graph, folhas, node, toggle):

    valores = []
    if(node in folhas):
        return folhas[node]

    for i in graph[node] :
        valores.append(minimax(graph, folhas, i, not toggle))

    if(toggle):
        valor_minmax = max(valores)
    else:
        valor_minmax = min(valores)    

    return valor_minmax

entry = input().rstrip()
nodes, rel = entry.split(' ')
rel = int(rel)
nodes = int(nodes)

#graph = {}
graph = defaultdict(list)
#folhas = defaultdict(list)
folhas = {}

for i in range(rel):
    entry = input().rstrip()
    a, b = entry.split(' ')

    graph[a].append(b)
    folhas[b] = None


n = input().rstrip()
n = int(n)

for i in range(n):
    entry = input().rstrip()
    a, b = entry.split(' ')

    if(a in folhas):
        folhas[a] = int(b)

# Elimina as folhas vazias
folhas = { key: folhas[key] for key in folhas if folhas[key] != None }

resultado = minimax(graph, folhas, '1', True)
print(resultado)

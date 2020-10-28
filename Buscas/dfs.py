from collections import defaultdict

def __dfs(graph, node, goal, visitados):
    
    if node == goal:
        return [node]
    
    if node in graph:
        for neighbor in graph[node]:
           
            if neighbor not in visitados:
                visitados.append( neighbor )
                path = __dfs(graph, neighbor, goal, visitados)

                if path is not None:
                    #path.insert(0, node)
                    path = visitados
                    return path
            
    return None
    
def dfs(graph, start, goal):

    visitados = []
    visitados.append(start)

    resultado = __dfs(graph, start, goal, visitados)
    print("-".join(resultado))
    
    return __dfs(graph, start, goal, visitados)



# Nó e Relações unidirecionais
entry = input().rstrip()
nodes, rel = entry.split(' ')
#rel = int(rel)

graph = defaultdict(list)

# Insere relações
for i in range(int(rel)):
    entry = input().rstrip()
    a, b = entry.split(' ')
    graph[str(a)].append(str(b))


# Le início e objetivo
entry = input().rstrip()
start, goal = entry.split(' ')

dfs(graph, start, goal)
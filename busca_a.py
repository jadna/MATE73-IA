def bestrela(cur, goal, graph, nrels, visited):
    visited.append(cur)
    if cur == goal:
        return True
    if nrels :
        cur_node = nrels[0]
        nrels = nrels[1:]
        cost_path = cur_node[1]-graph[cur][0]
    else:
        cost_path = 0
    rels = [ (no,  cost_path + c + graph[no][0]) for no, c in graph[cur][1:]]

    rels += nrels
    rels = sorted(rels, key= lambda rel: rel[1])

    bestrela(rels[0][0], goal, graph, rels,  visited)
   

if __name__ == '__main__':
    n = int(input().rstrip())

    graph = {}

    for i in range(1, n+1):
        i = str(i)
        if i not in graph:
            graph[i] = []
        graph[i].append(int(input().rstrip()))


    e = int(input().rstrip())
   
    for i in range(e):
        entry = input().rstrip()
        a, b, c = entry.split(' ')
        graph[a].append((b, int(c)))


    entry = input().rstrip()
   
    x, y = entry.split(' ')

    visited = []
    bestrela(x, y, graph, [], visited)
    resultado = visited
    resultado.sort(key=int)

    #print('-'.join(visited))
    print("-".join(resultado))
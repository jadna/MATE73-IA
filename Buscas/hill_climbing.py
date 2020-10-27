
import sys

def hill_climbing(cur, goal, graph, visited, cost):
    
    visited.append(cur)
    
    if cur == goal:
        return True
    
    rels = graph[cur][1:]
    rels = [ (no, c + graph[no][0]) for no, c in rels]

    if(goal in [no for no, cost in rels]):
        hill_climbing(goal, goal, graph, visited, cost+rels[0][1])
    else:
        rels = sorted(rels, key= lambda rel: rel[1])    
        hill_climbing(rels[0][0], goal, graph, visited, cost+rels[0][1])
   

if __name__ == '__main__':
    
    if sys.version_info.major == 2:
        
        n = input()
        n = int(n)
        graph = {}

        for i in range(1, n+1):
            i = str(i)
            if i not in graph:
                graph[i] = []
            graph[i].append(int(input()))

        e = int(input())
    
        for i in range(e):
            a, b, c = raw_input().split(" ") 
            graph[a].append((b, int(c)))

        x, y = raw_input().split(" ") 

    elif sys.version_info.major == 3:
        n = input().rstrip()
        n = int(n)

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

    print(graph)
    visited = []
    hill_climbing(x, y, graph, visited, 0)
    print('-'.join(visited))
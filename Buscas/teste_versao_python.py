import sys

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

    print(graph)



elif sys.version_info.major == 3:
    n = input().rstrip()
    n = int(n)
    graph = {}

    for i in range(1, n+1):
        i = str(i)
        if i not in graph:
            graph[i] = []
        graph[i].append(int(input().rstrip()))


    #e = int(input().rstrip())
    e = int(input())
   
    for i in range(e):
        entry = input().rstrip()
        a, b, c = entry.split(' ')
        graph[a].append((b, int(c)))

    entry = input().rstrip()   
    x, y = entry.split(' ')



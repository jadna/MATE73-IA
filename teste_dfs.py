# Python program to print all paths from a source to destination. 

from collections import defaultdict 

# This class represents a directed graph 
# using adjacency list representation 
class Graph: 

    def __init__(self, n_vertices): 
        # No. of n_vertices 
        self.V = n_vertices 

        # default dictionary to store graph 
        self.graph = defaultdict(list) 

    # function to add an edge to graph 
    def addEdge(self, u, v): 

        self.graph[u].append(v) 
        print("add_edge graph[u]: {}".format(self.graph[u]))
        
    '''A recursive function to print all paths from 'u' to 'd'. 
    visited[] keeps track of n_vertices in current path. 
    path[] stores actual n_vertices and path_index is current 
    index in path[]'''
    def printAllPathsUtil(self, u, d, visited, path): 

        # Mark the current node as visited and store in path 
        visited[u]= True
        path.append(u) 

        # If current vertex is same as destination, then print 
        # current path[] 
        if u == d: 
            print (path) 
        else: 
            # If current vertex is not destination 
            # Recur for all the n_vertices adjacent to this vertex 
            for i in self.graph[u]: 
                if visited[i]== False: 
                    self.printAllPathsUtil(i, d, visited, path) 

        # Remove current vertex from path[] and mark it as unvisited 
        path.pop() 
        visited[u]= False


    # Prints all paths from 's' to 'd' 
    def printAllPaths(self, s, d): 

        # Mark all the vertices as not visited 
        visited =[False]*(self.V) 

        # Create an array to store paths 
        path = [] 

        # Call the recursive helper function to print all paths 
        self.printAllPathsUtil(s, d, visited, path) 



# Create a graph given in the above diagram 

g = Graph(4) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(0, 3) 
#g.addEdge(2, 0) 
#g.addEdge(2, 1) 
g.addEdge(1, 3)

s = 2 ; d = 3
print ("Following are all different paths from % d to % d :" %(s, d)) 
g.printAllPaths(s, d) 
# This code is contributed by Neelam Yadav 

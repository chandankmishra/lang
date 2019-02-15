#https://www.geeksforgeeks.org/longest-path-for-directed-acyclic-graphs/

# Python program to find single source longest paths 
# for Directed Acyclic Graphs Complexity :OV(V+E) 
from collections import defaultdict 
  
# Graph is represented using adjacency list. Every 
# node of adjacency list contains vertex number of 
# the vertex to which edge connects. It also contains 
# weight of the edge 
class Graph: 
    def __init__ (self): 
        self.graph = {}
  
    def addEdge(self, u, v, w): 
        if u not in self.graph:
            self.graph[u] = set()
        if v not in self.graph:
            self.graph[v] = set()
            
        self.graph[u].add((v, w)) 
  
    def topologicalSortUtil(self,v,seen,stack): 
        seen.add(v)

        # Recur for all the vertices adjacent to this vertex 
        if v in self.graph.keys(): 
            for node, weight in self.graph[v]: 
                if node not in seen:
                    self.topologicalSortUtil(node, seen, stack) 
  
        # Push current vertex to stack which stores topological sort 
        stack.append(v) 
  
    def longestPath(self, source): 
        seen = set()
        stack =[] 
  
        # get topological sorted path from source to all vertexes 
        self.topologicalSortUtil(source, seen, stack) 
  
        # Initialize distances to all vertices as infinite and 
        # distance to source as 0 
        dist = [float("-inf")] * len(self.graph) 
        dist[source] = 0
  
        # Process vertices in topological order 
        while stack: 
            # Get the next vertex from topological order 
            i = stack.pop() 
  
            # Update distances of all adjacent vertices 
            for node, weight in self.graph[i]: 
                if dist[node] < dist[i] + weight: 
                    dist[node] = dist[i] + weight 
  
        # Print the calculated longest distances 
        for i in self.graph: 
            print ("i=", i, "dist", dist[i]) if dist[i] != float("Inf") else  print("i=",i, "dist", "inf")
  
  
g = Graph() 
g.addEdge(0, 1, 5) 
g.addEdge(0, 2, 3) 
g.addEdge(1, 3, 6) 
g.addEdge(1, 2, 2) 
g.addEdge(2, 4, 4) 
g.addEdge(2, 5, 2) 
g.addEdge(2, 3, 7) 
g.addEdge(3, 4, -1) 
g.addEdge(4, 5, -2) 
  
source = 1 #source
print ("Following are longest distances from source %d " % source) 
g.longestPath(source) 

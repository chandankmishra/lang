from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
 
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    def BFS(self, s):
        visited = set()
        queue = list()
        queue.append(s)
        visited.add(s)
 
        while queue:
            s = queue.pop(0)
            print (s,",", end='')
            for i in self.graph[s]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)

    def DFSUtil(self, s, visited):
        visited.add(s)
        print (s,",", end='')
        for i in self.graph[s]:
            if i not in visited:
                self.DFSUtil(i, visited)
        
    def DFS(self, s):
        visited = set()
        self.DFSUtil(s, visited)

# Test Program
g = Graph()

g.addEdge('A', 'B')
g.addEdge('A', 'C')
g.addEdge('B', 'C')
g.addEdge('C', 'A')
g.addEdge('C', 'D')
g.addEdge('D', 'D')

print ("Breadth First Traversal (from C)")
g.BFS('C')
print ("")
print ("Depth First Traversal (from C)")
g.DFS('C')
print ("")

#end of file

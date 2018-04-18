from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def find_parent(self, parent,i):
        if parent[i] == -1:
            return i
        if parent[i]!= -1:
            return self.find_parent(parent,parent[i])

    def union(self,parent,x,y):
        x_set = self.find_parent(parent, x)
        y_set = self.find_parent(parent, y)
        parent[x_set] = y_set

    def isCyclic(self):
        parent = [-1]*(self.V)
        # Iterate through all edges of graph, find subset of both
        # vertices of every edge, if both subsets are same, then
        # there is cycle in graph.
        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_parent(parent, i)
                y = self.find_parent(parent, j)
                if x == y: return True
                self.union(parent,x,y)
        return False


# Create a graph given in the above diagram
g = Graph(5)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
print (g.isCyclic())
g.addEdge(3, 4)
print (g.isCyclic())

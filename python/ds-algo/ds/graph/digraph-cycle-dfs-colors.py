from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isCycleUtilDfs(self, v, color):
        color[v] = "GRAY"

        if v not in self.graph:
            return False

        for neighbour in self.graph[v]:
            if neighbour not in color:
                continue
            if color[neighbour] == "GRAY":
                return True
            if color[neighbour] == "WHITE" and self.isCycleUtilDfs(neighbour, color):
                return True

        color[v] = "BLACK"
        return False


    def isCycleDfs(self):
        color = defaultdict() 
        for v in self.graph:
            color[v] = "WHITE"

        for v in self.graph:
            if color[v] == "WHITE":
                if self.isCycleUtilDfs(v, color) is True:
                    return True
        return False

# Driver Program
graph = Graph(5)

graph.addEdge('A', 'B')
graph.addEdge('A', 'C')
graph.addEdge('A', 'D')
graph.addEdge('E', 'A')

# Check cycle
print (graph.isCycleDfs())

# Create cycle
graph.addEdge('B', 'E')
print (graph.isCycleDfs())

from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isCycleUtilDfs(self, v, visited, recstack):
        visited.add(v)
        recstack.add(v)

        if v not in self.graph:
            return False

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                if self.isCycleUtilDfs(neighbour, visited, recstack):
                    return True
            elif neighbour in recstack:
                return True
        if v in recstack: recstack.remove(v)
        return False


    def isCycleDfs(self):
        visited = set()
        recstack = set()
        for v in self.graph:
            if self.isCycleUtilDfs(v, visited, recstack):
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

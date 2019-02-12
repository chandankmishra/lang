from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.V = V
        self.vertex_list = defaultdict(list)

    def addEdge(self, u, v):
        self.vertex_list[u].append(v)

    def isCycleUtilDfs(self, v, seen, path):
        if v in path: return True
        if v in seen: return False
        seen.add(v)
        path.add(v)

        if v not in self.vertex_list: return False

        for neighbour in self.vertex_list[v]:
            if self.isCycleUtilDfs(neighbour, seen, path):
                return True

        if v in path: path.remove(v)
        return False

    def isCycleDfs(self):
        seen = set()
        path = set()
        for v in self.vertex_list:
            if self.isCycleUtilDfs(v, seen, path):
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

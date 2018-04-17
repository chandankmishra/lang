from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def isCycleUtilDfs(self, v, visited, parent):
        visited.add(v)
        #print (v, ",", end='')

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                if self.isCycleUtilDfs(neighbour, visited, v):
                    return True
            elif parent != neighbour:
                return True
        return False

    def isCycleDfs(self, v):
        visited = set()
        return self.isCycleUtilDfs(v, visited, -1)

graph = Graph(5)
graph.addEdge('A', 'B')
graph.addEdge('A', 'C')
graph.addEdge('A', 'D')
graph.addEdge('B', 'E')

# Check for the cycle
print (graph.isCycleDfs('A'))

# Now create the cycle
graph.addEdge('C', 'D')
print (graph.isCycleDfs('A'))



# Python program to print topological sorting of a DAG
from collections import defaultdict

# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A recursive function used by topologicalSort
    def topologicalSortUtil(self, v, visited, stack):

        # Mark the current node as visited.
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        # Push current vertex to stack which stores result
        stack.insert(0, v)

    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False] * self.V
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        # Print contents of stack
        print (stack)

g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
print ("Following is a Topological Sort of the given graph")
g.topologicalSort()


'''
def topologicalSortUtil(graph, v, visited, stack):
    visited.add(v)
    # print (v, graph[v])
    if v not in graph:
        stack.insert(0, v)
        return

    for i in graph[v]:
        # print (i)
        if i not in visited:
            topologicalSortUtil(graph, i, visited, stack)
    stack.insert(0, v)


def topologicalSort(graph):
    visited = set()
    stack = []
    for v in graph:
        if v not in visited:
            topologicalSortUtil(graph, v, visited, stack)
    print (stack)


# graph1 = {'A': ['B', 'C', 'E'],
#           'B': ['C', 'E'],
#           'C': ['A'],
#           'D': ['C'],
#           'E': ['F'],
#           'F': ['C']}
# print ("TopologicalSort: ", end='')
# topologicalSort(graph1)

graph2 = {5: [2, 0],
          4: [0, 1],
          2: [3],
          3: [1]}
print ("TopologicalSort: ", end='\n')
topologicalSort(graph2)
'''

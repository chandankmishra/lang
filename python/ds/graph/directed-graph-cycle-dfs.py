def isCycleUtilDfs(graph, v, visited, recstack):
    visited.add(v)
    recstack.add(v)

    if v not in graph:
        return False

    for neighbour in graph[v]:
        if neighbour not in visited:
            if isCycleUtilDfs(graph, neighbour, visited, recstack):
                return True
        elif neighbour in recstack:
            return True
    if neighbour in recstack:
        recstack.remove(neighbour)
    return False


def isCycleDfs(graph):
    visited = set()
    recstack = set()
    for i in graph:
        return isCycleUtilDfs(graph, i, visited, recstack)


graph1 = {'A': ['B', 'C', 'E'],
          'B': ['C', 'E'],
          'C': ['A'],
          'D': ['C'],
          'E': ['F'],
          'F': ['C']}

graph2 = {'A': ['B'],
          'B': ['E'],
          'C': ['D'],
          #'D': ['E'],
          'E': ['F'],
          'F': ['C']}

print (isCycleDfs(graph1))
print (isCycleDfs(graph2))

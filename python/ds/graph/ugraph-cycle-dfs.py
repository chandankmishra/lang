def isCycleUtilDfs(graph, v, visited, parent):
    visited.add(v)
    #print (v, ",", end='')

    for neighbour in graph[v]:
        if neighbour not in visited:
            if isCycleUtilDfs(graph, neighbour, visited, v):
                return True
        elif parent != neighbour:
            return True
    return False


def isCycleDfs(graph, v):
    visited = set()
    return isCycleUtilDfs(graph, v, visited, -1)


# graph = {'A': ['B', 'C', 'E'],
#          'B': ['C', 'E'],
#          'C': ['A'],
#          'D': ['C'],
#          'E': ['F'],
#          'F': ['C']}

graph = {'A': ['B'],
         'B': ['E'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}

print (graph)
print (isCycleDfs(graph, 'A'))

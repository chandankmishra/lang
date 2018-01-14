def isCycleUtilDfs(graph, v, color):
    color[v] = "GRAY"

    if v not in graph:
        return False

    for neighbour in graph[v]:
        if neighbour not in color:
            continue
        if color[neighbour] == "GRAY":
            return True
        if color[neighbour] == "WHITE" and isCycleUtilDfs(graph, neighbour, color):
            return True

    color[v] = "BLACK"
    return False


def isCycleDfs(graph):
    vLen = len(graph)
    color = {}
    for i in graph:
        color[i] = "WHITE"

    for i in graph:
        if color[i] == "WHITE":
            if isCycleUtilDfs(graph, i, color) is True:
                return True
    return False


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

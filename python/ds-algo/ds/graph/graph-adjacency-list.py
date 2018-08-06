def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        print (start, end)
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            print (node)
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

# Function to print a BFS of graph


def BFS(graph, s):
    visited = set()
    queue = []

    queue.append(s)
    visited.add(s)

    while queue:
        s = queue.pop(0)
        print (s, ",", end='')

        for i in graph[s]:
            if i not in visited:
                queue.append(i)
                visited.add(i)


def DFSUtil(graph, v, visited):
    visited.add(v)
    print (v, ",", end='')

    for i in graph[v]:
        if i not in visited:
            DFSUtil(graph, i, visited)

# Function to print a DFS of graph
def DFS(graph, v):
    visited = set()
    DFSUtil(graph, v, visited)


graph = {'A': ['B', 'C', 'E'],
         'B': ['C', 'E'],
         'C': ['A'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}

print (graph)
print ("path from A->D", find_path(graph, 'A', 'D'))
print ("all paths from A->D", find_all_paths(graph, 'A', 'D'))
print ("shortest path from A->D", find_shortest_path(graph, 'A', 'D'))
print ("BFS: ")
BFS(graph, 'A')
print ("")
print ("DFS: ")
DFS(graph, 'A')

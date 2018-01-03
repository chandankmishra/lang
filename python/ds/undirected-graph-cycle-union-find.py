    def find_parent(parent, i):
        if i not in parent:
            return i
        if parent[i] == -1:
            return i
        if parent[i] != -1:
            return find_parent(parent, parent[i])

    # A utility function to do union of two subsets

    def union(parent, x, y):
        x_set = find_parent(parent, x)
        y_set = find_parent(parent, y)
        parent[x_set] = y_set

    # The main function to check whether a given graph
    # contains cycle or not

    def isCyclicUnionFind(graph):
        # Allocate memory for creating V subsets and
        # Initialize all subsets as single element sets
        parent = {}
        for i in graph:
            parent[i] = -1

        for i in graph:
            for j in graph[i]:
                x = find_parent(parent, i)
                y = find_parent(parent, j)
                print (x, y)
                if x == y:
                    return True
                union(parent, x, y)
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
              #'D': ['C'],
              'E': ['F'],
              'F': ['C']}

    print (isCyclicUnionFind(graph1))
    print (isCyclicUnionFind(graph2))

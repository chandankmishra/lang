# Python program for Kruskal's algorithm to fineSet
# Minimum Spanning Tree of a given connected,
# undirected and weighted graph

#         Time complexity - O(ElogE)
#         Space complexity - O(E + V)

from collections import defaultdict

# Class to represent a graph


class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []  # default dictionary to store graph

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # A utility function to fineSet set of an element i
    # (uses path compression technique)
    def fineSet(self, parent, i):
        if parent[i] == i:
            return i
        parent[i] = self.fineSet(parent, parent[i])
        return parent[i]

    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.fineSet(parent, x)
        yroot = self.fineSet(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # The main function to construct MST using Kruskal's
    # algorithm
    def KruskalMST(self):
        result, parent, rank = [], [], []
        i = 0  # An index variable, used for sorted edges
        e = 0  # An index variable, used for result[]

        self.graph = sorted(self.graph, key=lambda item: item[2])

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            root1 = self.fineSet(parent, u)
            root2 = self.fineSet(parent, v)

            if root1 != root2:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, root1, root2)
        return result


# Driver code
g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)
print (g.graph)

result = g.KruskalMST()
print ("Following are the edges in the constructed MST")
for u, v, weight in result:
    # print str(u) + " -- " + str(v) + " == " + str(weight)
    print ("%d -- %d == %d" % (u, v, weight))

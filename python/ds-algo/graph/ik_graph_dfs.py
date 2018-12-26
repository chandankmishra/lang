class Vertex:
    def __init__(self, label):
        self.neighbors = set()
        self.label = label


class Graph:
    def __init__(self):
        self.vertex_list = set()

    def add_edge(self, u, v):
        u.neighbors.add(v)
        self.vertex_list.add(u)


def explore_dfs(cur, seen, component):
    seen.add(cur.label)
    component.append(cur.label)

    for nxt in cur.neighbors:
        if nxt.label not in seen:
            explore_dfs(nxt, seen, component)


def dfs(vertex_list):
    seen = set()
    for cur in vertex_list:
        if cur.label not in seen:
            component = []
            explore_dfs(cur, seen, component)
            print(component)


v1 = Vertex(1)
v2 = Vertex(2)
v3 = Vertex(3)
v4 = Vertex(4)
v5 = Vertex(5)
v6 = Vertex(6)
v7 = Vertex(7)

graph = Graph()
graph.add_edge(v1, v2)
graph.add_edge(v2, v5)
graph.add_edge(v1, v3)
graph.add_edge(v1, v4)
graph.add_edge(v6, v7)


dfs(graph.vertex_list)

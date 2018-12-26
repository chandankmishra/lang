class Vertex:
    def __init__(self, label):
        self.neighbors = []
        self.label = label


class Graph:
    def __init__(self):
        self.vertex_list = []

    def add_edge(self, u, v):
        u.neighbors.append(v)
        self.vertex_list.append(u)


def explore_bfs(cur, seen, component):
    seen.add(cur.label)
    component.append(cur.label)
    q = [cur]
    while q:
        cur = q.pop(0)
        for nxt in cur.neighbors:
            if nxt.label not in seen:
                component.append(nxt.label)
                seen.add(nxt.label)
                q.append(nxt)


def bfs(vertex_list):
    seen = set()
    for vertex in vertex_list:
        if vertex.label not in seen:
            component = []
            explore_bfs(vertex, seen, component)
            print(component)


# v1 = Vertex(1)
# v2 = Vertex(2)
# v3 = Vertex(3)
# v4 = Vertex(4)
# v5 = Vertex(5)

# v6 = Vertex(6)
# v7 = Vertex(7)

# graph = Graph()
# graph.add_edge(v1, v2)
# graph.add_edge(v2, v5)
# graph.add_edge(v1, v3)
# graph.add_edge(v1, v4)
# graph.add_edge(v6, v7)

v1 = Vertex(1)
v2 = Vertex(2)
v3 = Vertex(3)
v4 = Vertex(4)
v5 = Vertex(5)

graph = Graph()
graph.add_edge(v1, v2)
graph.add_edge(v2, v3)
graph.add_edge(v4, v5)

seen = bfs(graph.vertex_list)
# print(seen)

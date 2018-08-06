class Vertex:
    def __init__(self, label):
        self.neighbors = []
        self.label = label


class Graph:
    def __init__(self):
        self.adj_list = []

    def add_edge(self, u, v):
        u.neighbors.append(v)
        self.adj_list.append(u)


def build_path(prev, target):
    path = []
    cur = target
    while prev[cur.label]:
        path.append(cur.label)
        cur = prev[cur.label]
    path.append(cur.label)
    path.reverse()
    return path


def explore_bfs(num_vertices, start, target):
    """ return the distance and the path to the target."""
    seen = set()
    dist = [0] * (num_vertices + 1)
    prev = [None] * (num_vertices + 1)
    q = []
    seen.add(start.label)
    dist[start.label] = 0
    q.append(start)
    while q:
        cur = q.pop(0)
        if cur.label == target.label:
            return dist[target.label], build_path(prev, target)

        for nxt in cur.neighbors:
            if nxt.label not in seen:
                seen.add(nxt.label)
                dist[nxt.label] = dist[cur.label] + 1
                prev[nxt.label] = cur
                q.append(nxt)
    return 0, []


v1 = Vertex(1)
v2 = Vertex(2)
v3 = Vertex(3)
v4 = Vertex(4)
v5 = Vertex(5)
v6 = Vertex(6)
v7 = Vertex(7)
v8 = Vertex(8)
v9 = Vertex(9)
v10 = Vertex(10)
v11 = Vertex(11)

graph = Graph()
graph.add_edge(v1, v2)
graph.add_edge(v1, v3)
graph.add_edge(v2, v4)
graph.add_edge(v3, v4)
graph.add_edge(v3, v5)
graph.add_edge(v4, v6)
graph.add_edge(v4, v7)
graph.add_edge(v5, v6)
graph.add_edge(v5, v7)
graph.add_edge(v5, v8)
graph.add_edge(v6, v9)
graph.add_edge(v7, v9)
graph.add_edge(v7, v10)
graph.add_edge(v8, v11)

num_vertices = len(graph.adj_list)
dist, path = explore_bfs(num_vertices, v1, v11)
print(f"Path from {v1.label} to {v11.label} is {path} and distance {dist}")

class UF:
    def __init__(self):
        self.vertex_list = {}
        self.parent = {}

    def add_edge(self, u, v):
        if u not in self.vertex_list:
            self.vertex_list[u] = set()
        if v not in self.vertex_list:
            self.vertex_list[v] = set()
        self.vertex_list[u].add(v)
        self.parent[v] = v
        self.parent[u] = u
		count += 2

    def find(self, v):
        if self.parent[v] == v:
            return v
        self.parent[v] = self.find(self.parent[v]) #path compression
        return self.parent[v]

    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)
        if u_root != v_root:
            self.parent[v_root] = u_root

    def isCyclic(self):
        for cur in self.vertex_list:
            for nxt in self.vertex_list[cur]:
                x = self.find(cur)
                y = self.find(nxt)
                if x == y:
                    return True
                self.union(x, y)
        return False

g = UF()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
print (g.isCyclic())
g.add_edge(3, 4)
print (g.isCyclic())
print (g.vertex_list)
print (g.parent)

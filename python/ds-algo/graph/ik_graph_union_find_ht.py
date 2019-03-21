class Solution:
    def numIslands2(self, m, n, positions):
        result = []
        islands = Union()
        for cur in map(tuple, positions):
            islands.add(cur)
            for nei in (0, 1), (0, -1), (1, 0), (-1, 0):
                nxt = (cur[0] + nei[0], cur[1] + nei[1])
                if nxt in islands.parent:
                    islands.union(cur, nxt)
            result += [islands.components]
        return result

class Union:
    def __init__(self):
        self.parent = {}
        self.components = 0

    def add(self, p):
        self.parent[p] = p
        self.components += 1

    def find(self, v):
        if self.parent[v] == v:
            return v
        self.parent[v] = self.find(self.parent[v]) #path compression
        return self.parent[v]

    def union(self, u, v):
        u_root, v_root = self.find(u), self.find(v)
        if u_root == v_root:
            return
        self.parent[u_root] = v_root
        self.components -= 1

s = Solution()
arr = [[0,0],[0,1],[1,2],[2,1]]
print(s.numIslands2(3,3,arr))

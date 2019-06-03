
class Solution:
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sortedA = sorted(A)
        sortedB = sorted(B)

        # assigned[b] = list of a that are assigned to beat b
        # remaining = list of a that are not assigned to any b
        # assigned = {b: [] for b in B}
        assigned = {b: [] for b in B}

        # print(assigned)
        remaining = []

        # populate (assigned, remaining) appropriately
        # sortedB[j] is always the smallest unassigned element in B
        j = 0
        for a in sortedA:
            if a > sortedB[j]:
                assigned[sortedB[j]].append(a)
                j += 1
            else:
                remaining.append(a)
        print(B, assigned, remaining)
        # Reconstruct the answer from annotations (assigned, remaining)
        res = []
        for b in B:
            if assigned[b]:
                res.append(assigned[b].pop())
            else:
                res.append(remaining.pop())

        return res


obj = Solution()

# A = [2, 7, 11, 15]
# B = [1, 10, 4, 11]
# print(obj.advantageCount(A, B))

A = [12, 24, 8, 32]
B = [13, 25, 32, 11]
print(obj.advantageCount(A, B))

# A = [8, 2, 4, 4, 5, 6, 6, 0, 4, 7]
# B = [0, 8, 7, 4, 4, 2, 8, 5, 2, 0]
# print(obj.advantageCount(A, B))

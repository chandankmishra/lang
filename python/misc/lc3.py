
class Solution:
    def __init__(self):
        self.res = None
        self.max_cnt = 0

    def get_adv_cnt(self, A, B, l):
        count = 0
        for i in range(l):
            if A[i] > B[i]:
                count += 1
        if count > self.max_cnt:
            self.max_cnt = count
            self.res = A.copy()
            # print(self.res, count, self.max_cnt)
            # print(A)
        return count

    def get_permutation(self, A, B, start):
        l = len(A)
        if start == l - 1:
            # print(A)
            if self.get_adv_cnt(A, B, l) == l:
                return True
            return False

        for i in range(start, l):
            A[start], A[i] = A[i], A[start]
            if self.get_permutation(A, B, start + 1) is True:
                return True
            A[start], A[i] = A[i], A[start]
        return False

    def advantageCount(self, A, B):
        # print(A, B)
        # self.res = A
        self.get_permutation(A, B, 0)
        return self.res


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

def maxCount(m, n, ops):
    """
    :type m: int
    :type n: int
    :type ops: List[List[int]]
    :rtype: int
    """
    if not ops:
        return m * n

    return min(op[0] for op in ops) * min(op[1] for op in ops)

    # following solution is not optimized
    #mat = [[0] * m for i in range(n)]
    #max = 0
    #count = 0
    #for o in ops:
    #    for i in range(0, o[0]):
    #        for j in range(0, o[1]):
    #            mat[i][j] += 1
    #
    #for i in range(0, m):
    #    for j in range(0, n):
    #        if max < mat[i][j]:
    #            max = mat[i][j]
    #            count = 1
    #        elif max == mat[i][j]:
    #            count += 1
    #return count


l = [[2, 2], [3, 3]]
print(maxCount(3, 3, l))

l = []
print(maxCount(3, 3, l))

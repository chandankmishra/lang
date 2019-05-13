def find_missing_positive(A):
    n = len(A)
    '''
    i = 1
    while i <= n:
        x = A[i - 1]
        if 1 <= x < n and A[x - 1] != x:
            A[i - 1], A[x - 1] = A[x - 1], x
        else:
            i += 1
    '''
    print (A)
    for i in range(n):
        if A[i] <= 0 or A[i] > n:
            A[i] = n + 1

    for i in range(n):
        num = abs(A[i])
        if num > n:
            continue
        num = num - 1
        if A[num] > 0:
            A[num] = -1 * A[num]

    for i in range(n):
        if A[i] >= 0:
            return i + 1
    return n + 1


testcases = [
    [4, 2, 1, 3],
    [1, -1, 2, 3, 4, 5, 6, 10, 22, 33],
    [4, 2, 1, -1]
]

for testcase in testcases:
    print (find_missing_positive(testcase))

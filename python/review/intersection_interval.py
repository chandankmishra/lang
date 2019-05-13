def intersection(A, B):
    A = A + B
    A.sort(key=lambda x: x[0])
    n = len(A)
    result = []
    for i in range(1, n):
        if A[i - 1][1] >= A[i][0]:
            result.append([A[i][0], min(A[i - 1][1], A[i][1])])
        A[i][1] = max(A[i - 1][1], A[i][1])
    return result


def intersection2(A, B):
    n, m = len(A), len(B)


A = [[0, 2], [5, 10], [13, 23], [24, 25]]
B = [[1, 5], [8, 12], [15, 24], [25, 26]]
print (intersection(A, B))

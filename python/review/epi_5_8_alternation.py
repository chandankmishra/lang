def rearrange(A):
    n = len(A)
    for idx in range(n - 1):
        if idx % 2 == 0:
            if A[idx] > A[idx + 1]:
                A[idx], A[idx + 1] = A[idx + 1], A[idx]
        else:
            if A[idx] < A[idx + 1]:
                A[idx], A[idx + 1] = A[idx + 1], A[idx]
    return A


def longest_increasing_subarray(A):
    n = len(A)
    end = 0
    max_len, cur_len = 0, 1
    for i in range(1, n):
        if A[i - 1] < A[i]:
            cur_len = cur_len + 1
            if cur_len > max_len:
                max_len = cur_len
                end = i
        else:
            cur_len = 1
    return A[end - max_len + 1:end + 1]


A = [5, 6, 3, 5, 7, 8, 9, 1, 2]
# print (rearrange(A))
print (longest_increasing_subarray(A))

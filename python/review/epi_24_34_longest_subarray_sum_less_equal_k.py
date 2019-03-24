import itertools
import functools

# Time complexity O(n)
# Space Complexity O(1)
def find_logest_subarray_less_equal_k(A, k):
    prefix_sum = []
    psum = 0
    for num in A:
        psum += num
        prefix_sum.append(psum)

    if prefix_sum[-1] <= k:
        return len(A)

    start = end = max_length = 0
    while end < len(A) and start < len(A):
        min_curr_sum = (prefix_sum[end] - prefix_sum[start])
        if min_curr_sum <= k:
            curr_length = end - start
            if curr_length > max_length:
                max_length = curr_length
            end += 1
        else:
            start += 1

    return max_length


# Time complexity O(n^2)
# Space Complexity O(n)
def find_logest_subarray_less_equal_k1(A, k):
    n = len(A)
    P = [0]
    psum = 0
    for num in A:
        psum += num
        P.append(psum)

    max_len = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            if P[j] - P[i] <= k:
                max_len = max(max_len, j - i)
    return max_len


A = [2, 4, 5, 66, 1, 20, 1, 10, 1, 10, 1, 40, 4, 2, 1, 0, 1]
print(find_logest_subarray_less_equal_k(A, 5))
print(find_logest_subarray_less_equal_k1(A, 5))

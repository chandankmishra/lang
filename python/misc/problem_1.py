def helper(arr, n, i, psum, k, count):
    l = len(arr)
    if l == 0:
        return False
    if l == 1:
        return True if arr[0] == k else False
    if psum == k and count > 0:
        return True
    if i == n:
        return False

    if helper(arr, n, i + 1, psum, k, count) is True:
        return True
    if helper(arr, n, i + 1, psum + arr[i], k, count + 1) is True:
        return True
    return False


def check_if_sum_possible(arr, k):
    print(arr, k)

    return helper(arr, len(arr), 0, 0, k, 0)


arr = [
    -2
    - 1,
    3,
    # -1,
    # -1,
    # -3,
    2,
    1,
    # -1,
    1,
    # -4,
    # -2,
    3,
    # 0,
    4,
    2,
    # -4,
    # -4
]
k = 16

print(check_if_sum_possible(arr, k))

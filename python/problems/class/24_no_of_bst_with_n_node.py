def helper(lst, n):
    if len(lst) == 0:
        return 0

    if n == 1:
        print(lst)
        return 1
    count = 1
    for i in range(n):
        left = lst[:i]
        right = lst[i + 1:]
        print(left, right)
        if len(left) > 1:
            count += helper(left, len(left))
        if len(right) > 1:
            count += helper(right, len(right))
    return count


def how_many_BSTs(n):
    lst = [i for i in range(1, n + 1)]
    return helper(lst, n)


print(how_many_BSTs(3))

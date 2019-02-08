def should_swap(arr, start, current):
    for i in range(start, current):
        if arr[i] == arr[current]:
            return False
    return True


def helper(arr, start, result):
    n = len(arr)
    if start == n - 1:
        result.append(''.join(list(arr)))
        return

    for i in range(start, n):
        check = should_swap(arr, start, i)
        if check:
            arr[start], arr[i] = arr[i], arr[start]
            helper(arr, start + 1, result)
            arr[start], arr[i] = arr[i], arr[start]


def permuate(arr):
    result = []
    helper(arr, 0, result)
    return result


text = 'aba'
print (permuate(list(text)))

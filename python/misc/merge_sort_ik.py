def merge(arr, start, mid, end):
    left, right = [], []
    i, j = 0, 0
    for k in range(start, mid + 1):
        left.append(arr[k])
    for k in range(mid + 1, end + 1):
        right.append(arr[k])

    i, j, k = 0, 0, start
    ll = len(left)
    lr = len(right)
    while i < ll and j < lr:
        if left[i] <= right[j]:
            arr[k], k, i = left[i], k + 1, i + 1
        else:
            arr[k], k, j = right[j], k + 1, j + 1
    while i < ll:
        arr[k], k, i = left[i], k + 1, i + 1
    while j < lr:
        arr[k], k, j = right[j], k + 1, j + 1


def merge_sort(arr, start, end):
    if start >= end:
        return
    mid = start + (end - start) // 2
    merge_sort(arr, start, mid)
    merge_sort(arr, mid + 1, end)
    merge(arr, start, mid, end)


arr = [50, 100, 10, 20, 30, 40]
merge_sort(arr, 0, len(arr) - 1)
print(arr)

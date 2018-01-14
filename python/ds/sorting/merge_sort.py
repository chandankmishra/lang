def merge(left, right, arr):
    ll, lr, la = len(left), len(right), len(arr)
    i, j, k = 0, 0, 0
    while (i < ll and j < lr):
        if left[i] < right[j]:
            arr[k], k, i = left[i], k + 1, i + 1
        else:
            arr[k], k, j = right[j], k + 1, j + 1
    while (i < ll):
        arr[k], k, i = left[i], k + 1, i + 1
    while (j < lr):
        arr[k], k, j = right[j], k + 1, j + 1


def merge_sort(arr):
    l = len(arr)
    if l < 2:
        return
    m = l // 2
    left, right = [], []
    for i in range(m):
        left.append(arr[i])
    for i in range(m, l):
        right.append(arr[i])
    merge_sort(left)
    merge_sort(right)
    merge(left, right, arr)


arr = [5, 2, 4, 3, 1]
print (arr)
merge_sort(arr)
print (arr)

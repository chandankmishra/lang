def partition(arr, start, end):
    pivot = arr[end]
    pindex = start
    for i in range(start, end):
        if arr[i] <= pivot:
            arr[i], arr[pindex] = arr[pindex], arr[i]
            pindex += 1
    arr[end], arr[pindex] = arr[pindex], arr[end]
    return pindex


def quick_sort(arr, start, end):
    if start >= end:
        return
    pindex = partition(arr, start, end)
    quick_sort(arr, start, pindex - 1)
    quick_sort(arr, pindex + 1, end)


arr = [5, 8, 2, 4, 6, 3, 7, 1]
l = len(arr)
print (arr)
quick_sort(arr, 0, l - 1)
print (arr)

def selection_sort(arr):
    l = len(arr)
    for i in range(l):
        imin = i
        for j in range(i + 1, l):
            if arr[j] < arr[imin]:
                imin = j
        arr[imin], arr[i] = arr[i], arr[imin]
    return arr


arr = [5, 2, 4, 3, 1]
print (selection_sort(arr))

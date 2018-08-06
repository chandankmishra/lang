def insertion_sort(arr):
    l = len(arr)
    for i in range(1, l):
        key = arr[i]
        hole = i - 1
        while hole >= 0 and key < arr[hole]:
            arr[hole + 1] = arr[hole]
            hole -= 1
        arr[hole + 1] = key
    return arr


arr = [5, 2, 4, 3, 1]
print (insertion_sort(arr))

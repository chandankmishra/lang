def bubble_sort(arr):
    l = len(arr)
    for i in range(1, l - 1):
        value = arr[i]
        hole = i
        while hole > 0 and arr[hole] - 1 > value:
            arr[hole] = arr[hole - 1]
            hole -= 1
        arr[hole] = value
    return arr


arr = [5, 2, 4, 3, 1]
print (bubble_sort(arr))

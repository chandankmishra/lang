def selection_sort(arr):
    l = len(arr)
    for i in range(l - 1):
        flag = False
        for j in range(0, l - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True
        if flag is False:
            break
    return arr


arr = [5, 2, 4, 3, 1]
print (selection_sort(arr))

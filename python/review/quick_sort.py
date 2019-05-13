def partition(arr, start, end):
    # swap pivot element with last element
    p_index_before = (start + end) // 2
    arr[end], arr[p_index_before] = arr[p_index_before], arr[end]
    pivot = arr[end]
    i = start
    for curr in range(start, end):
        if arr[curr] < pivot:
            arr[curr], arr[i] = arr[i], arr[curr]
            i += 1
    arr[end], arr[i] = arr[i], arr[end]
    return i


def quick_sort_rec(arr, start, end):
    # base cases
    if start == end:
        return  # array has 1 element
    if start == end + 1:
        return  # array has 0 element

    # get the pivot index
    p_index = partition(arr, start, end)
    # recursively call the quick_sort
    quick_sort_rec(arr, start, p_index - 1)
    quick_sort_rec(arr, p_index + 1, end)


def quick_sort_iter(arr, left, right):
    # Create an auxiliary stack
    size = right - left + 1
    stack = [0] * (size)
    top = -1
    top = top + 1
    stack[top] = left
    top = top + 1
    stack[top] = right
    print (left, right, stack)

    while top >= 0:
        right = stack[top]
        top = top - 1
        left = stack[top]
        top = top - 1

        p_index = partition(arr, left, right)
        if p_index - 1 > left:
            top = top + 1
            stack[top] = left
            top = top + 1
            stack[top] = p_index - 1

        if p_index + 1 < right:
            top = top + 1
            stack[top] = p_index + 1
            top = top + 1
            stack[top] = right


arr = [50, 100, 10, 20, 30, 40]
quick_sort_iter(arr, 0, len(arr) - 1)
print(arr)

def choose_pivot(arr, start, end):
    return start

# Partition with 2 pointers
def partition(arr, start, end, p_index_before):
    # swap pivot element with last element
    arr[end], arr[p_index_before] = arr[p_index_before], arr[end]
    pivot = arr[end]
    i = start
    for curr in range(start, end):
        if arr[curr] < pivot:
            arr[curr], arr[i] = arr[i], arr[curr]
            i += 1
    arr[end], arr[i] = arr[i], arr[end]
    return i


def quick_sort(arr, start, end):
    # base cases
    if start == end:
        return  # array has 1 element
    if start == end + 1:
        return  # array has 0 element

    # get the pivot index
    p_index_before = choose_pivot(arr, start, end)
    p_index = partition(arr, start, end, p_index_before)
    # recursively call the quick_sort
    quick_sort(arr, start, p_index - 1)
    quick_sort(arr, p_index + 1, end)


arr = [50, 100, 10, 20, 30, 40]
quick_sort(arr, 0, len(arr) - 1)
print(arr)


# method #1 Partition using 2 pointers
# arr_new = []
# arr_new[le_count - 1] = arr[p_index_before]
# for idx, ele in zip(arr):
#     if idx == p_index_before:
#         continue
#     if ele <= p_val:
#         arr_new.append(ele)

# for idx, ele in zip(arr):
#     if idx == p_index_before:
#         continue
#     if ele > p_val:
#         arr_new.append(ele)
# return le_count - 1

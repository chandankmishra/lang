import heapq


def merge_k_sorted_arrays(narr, k, n):
    sorted_array_iter = []
    for arr in narr:
        sorted_array_iter.append(iter(arr))

    heap = []
    for i in range(k):
        element = next(sorted_array_iter[i], None)
        if element is not None:
            heapq.heappush(heap, (element, i))

    output = []
    while heap:
        smallest_entry, small_arr_i = heapq.heappop(heap)
        output.append(smallest_entry)
        next_element = next(sorted_array_iter[small_arr_i], None)
        if next_element is not None:
            heapq.heappush(heap, (next_element, small_arr_i))

    return output


k = 3
n = 4
narr = [[1, 3, 5, 7],
        [2, 4, 6, 8],
        [0, 9, 10, 11]]
print(merge_k_sorted_arrays(narr, k, n))

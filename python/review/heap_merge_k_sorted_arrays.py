import heapq


def merge_k_sorted_arrays(sorted_arrays):
    heap = []
    for i, sorted_array in enumerate(sorted_arrays):
        heapq.heappush(heap, (sorted_array[0], i, 0))

    result = []
    while heap:
        min_val, arr_idx, idx = heapq.heappop(heap)
        result.append(min_val)
        if idx + 1 < len(sorted_arrays[arr_idx]):
            heapq.heappush(heap, (sorted_arrays[arr_idx][idx + 1], arr_idx, idx + 1))
    return result


arr_list = [[5, 10, 15], [3, 6, 9, 12, 15], [8, 16, 24]]
print (merge_k_sorted_arrays(arr_list))

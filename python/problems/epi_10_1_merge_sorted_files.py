import heapq


def mergeSortedArrays(sorted_arrays):
    min_heap = list()
    sorted_arrays_iters = [iter(x) for x in sorted_arrays]
    for i, it in enumerate(sorted_arrays_iters):
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))
            print (first_element, i)

    result = []
    while min_heap:
        smalltest_entry, smalltest_array_i = heapq.heappop(min_heap)
        smalltest_array_iter = sorted_arrays_iters[smalltest_array_i]
        result.append(smalltest_entry)
        next_element = next(smalltest_array_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smalltest_array_i))
    return result


l1, l2, l3 = [3, 5, 7], [0, 6], [0, 6, 28]
sorted_arrays = [l1, l2, l3]

# Solution #1
print (mergeSortedArrays(sorted_arrays))

# Solution #2 (Pytonic way)
print (list(heapq.merge(*sorted_arrays)))
# print(mergeSortedArrays(sorted_arrays))

import heapq


def mergeSortedArrays(sorted_arrays):
    min_heap = []
    max_row = len(sorted_arrays)
    max_len = 0
    for arr in sorted_arrays:
        arr_len = len(arr)
        if max_len < arr_len:
            max_len = arr_len

    for i in range(max_len):
        for j in range(max_row):
            if sorted_arrays[j][i]:
                heapq.heappush(min_heap, sorted_arrays[i][j])
    print (min_heap)

    return 0
    # for i in range(0, len(sorted_arrays)):
    #     heapq.heappush(min_heap, sorted_arrays[i])

    # for arr in sorted_arrays:
    #     for var in arr:
    #         heapq.heappush(min_heap, var)
    # print (min_heap)

    # rlist = []
    # while min_heap:
    #     rlist.append(heapq.heappop(min_heap))
    # return rlist


l1, l2, l3 = [3, 5, 7], [0, 6], [0, 6, 28]
sorted_arrays = [l1, l2, l3]
print(mergeSortedArrays(sorted_arrays))

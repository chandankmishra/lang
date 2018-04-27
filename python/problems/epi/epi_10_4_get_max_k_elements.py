import heapq


def get_max_k_elements(arr, k):
    max_heap = []
    for num in arr:
        heapq.heappush(max_heap, num)
        if len(max_heap) == k + 1:
            heapq.heappop(max_heap)
    res = []
    while max_heap:
        res.append(heapq.heappop(max_heap))
    res.reverse()
    return res


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 20, 30, 40, 44, 34, 234, 66, 786, 4556]
print (get_max_k_elements(arr, 10))

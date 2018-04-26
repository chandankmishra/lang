from collections import defaultdict
import heapq


def top_k_most_frequent(arr, k):
    ahash = defaultdict(int)
    res = list()

    for i in arr:
        ahash[i] += 1

    for i in set(arr):
        heapq.heappush(res, (ahash[i], i))
        if len(res) > 2:
            heapq.heappop(res)
    print (res)

    result = list()
    for i in range(len(res)):
        var = heapq.heappop(res)
        result.append(var[1])
    return (result)


arr = [3, 1, 1, 1, 1, 4, 4, 5, 2, 6, 1, 5, 5, 6, 6]
print (top_k_most_frequent(arr, 2))

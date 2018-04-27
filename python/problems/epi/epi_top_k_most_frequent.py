from collections import defaultdict
import heapq


def top_k_most_frequent(arr, k):
    ahash = defaultdict(int)
    res = list()

    for num in arr:
        ahash[num] += 1

    for num in set(arr):
        heapq.heappush(res, (ahash[num], num))
        if len(res) > k:
            heapq.heappop(res)
    print (res)

    result = list()
    while res:
        var = heapq.heappop(res)
        result.append(var[1])
    result.reverse()
    return result


arr = [3, 1, 1, 1, 1, 4, 4, 5, 2, 6, 1, 5, 5, 6, 6]
print (top_k_most_frequent(arr, 3))

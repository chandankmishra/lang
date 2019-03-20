import heapq


def k_largest_in_binary_heap(A, k):
    if k <= 0:
        return []

    candidate_max_heap = []
    result = []
    candidate_max_heap.append((-A[0], 0))
    for _ in range(k):
        candidate_idx = candidate_max_heap[0][1]
        result.append(-heapq.heappop(candidate_max_heap)[0])
        left_child_idx = 2 * candidate_idx + 1
        if left_child_idx < len(A):
            heapq.heappush(candidate_max_heap, (-A[left_child_idx], left_child_idx))
        right_child_idx = 2 * candidate_idx + 1
        if right_child_idx < len(A):
            heapq.heappush(candidate_max_heap, (-A[right_child_idx], right_child_idx))
    result = [i * -1 for i in result]
    return result


A = [10, 20, 30, 40, 50, 60, 100, 90, 80, 70]
A = [i * -1 for i in A]
heapq.heapify(A)
print (k_largest_in_binary_heap(A, 3))

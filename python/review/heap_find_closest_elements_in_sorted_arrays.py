
# first method using RBTree
import bintrees


def find_closest_elements_in_sorted_arrays(sorted_arrays):
    min_distance_so_far = float('inf')
    tree = bintrees.RBTree()
    for idx, sorted_array in enumerate(sorted_arrays):
        tree.insert((sorted_array[0], idx), 0)

    result = []
    while len(tree) == 3:
        result = []
        min_value, aidx = tree.min_key()  # O(k)
        max_value, aidx = tree.max_key()  # O(k)
        if min_distance_so_far > max_value - min_value:
            min_distance_so_far = max_value - min_value
            result = []
            for node in tree:
                result.append(node[0])
        key, idx = tree.pop_min()     # O(k)
        next_min, arr_idx = key
        if idx + 1 < len(sorted_arrays[arr_idx]):
            tree.insert((sorted_arrays[arr_idx][idx + 1], arr_idx), idx + 1)  # O(k)
    return (min_distance_so_far, result)


arr_list = [[5, 10, 15], [3, 6, 9, 12, 15], [8, 16, 24]]
print ("result:", find_closest_elements_in_sorted_arrays(arr_list))

# Second method using heap
import heapq


def find_closest_elements_in_sorted_arrays(sorted_arrays):
    heap = []
    min_distnace_so_far = float('inf')
    for i, sorted_array in enumerate(sorted_arrays):
        heapq.heappush(heap, (sorted_array[0], i, 0))

    result = []
    while len(heap) == 3:
        v1, v2, v3 = heap[0][0], heap[1][0], heap[2][0]
        min_value, max_value = min(v1, v2, v3), max(v1, v2, v3)
        if min_distnace_so_far > max_value - min_value:
            result = [v1, v2, v3]
            min_distnace_so_far = max_value - min_value
        val, arr_idx, idx = heapq.heappop(heap)
        if idx + 1 < len(sorted_arrays[arr_idx]):
            heapq.heappush(heap, (sorted_arrays[arr_idx][idx + 1], arr_idx, idx + 1))
    return min_distnace_so_far, result


arr_list = [[5, 10, 15], [3, 6, 9, 12, 15], [8, 16, 24]]
print ("result:", find_closest_elements_in_sorted_arrays(arr_list))

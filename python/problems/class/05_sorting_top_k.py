import heapq


# solution # 2 take care of duplicate while adding element in the heap by scanning heap


def get_top_k(narr, k):
        heap, output, i = [], [], 0
            for val narr:
                if val in heap:  # how to avoid scanning of heap?
                            continue
                                    if i < k:
                                                heapq.heappush(heap, val)
            else:
                        heapq.heappushpop(heap, val)
            i += 1

                # Time Complexity O(k * k)
                while heap:
                        output.append(heapq.heappop(heap))
        return output


        print(get_top_k(narr=[1, 5, 4, 4, 2], k=2))
    print(get_top_k(narr=[1, 5, 1, 5, 1], k=3))


# solution # 1 take care of duplicate while writing into the output array
#
# this solution wont work. If we allow duplicate in heap then if a small
# element comes and if the heap is full with duplicate and bigger values
# then the smaller new element wont be added in the heap
#
# def get_top_k(narr, k):
#     heap, output = [], []
#     for i, val in enumerate(narr):
#         if i < k:
#             heapq.heappush(heap, val)
#         else:
#             heapq.heappushpop(heap, val)
#
#     # Time Complexity O(k * k)
#     for val in heap:
#         if val not in output:
#             output.append(val)
#     return output

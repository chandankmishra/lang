import heapq


def mergeKLists(self, lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    from itertools import count
    heap = []
    count = 0
    for i, llist in enumerate(lists):
        if llist:
            heapq.heappush(heap, (llist.val, count, llist))
            count += 1

    output = []
    head = dummyiter = ListNode(-1)
    while heap:
        smallest_entry, count, small_head = heapq.heappop(heap)
        dummyiter.next = small_head  # ListNode(smallest_entry)
        next_node = small_head.next
        if next_node:
            heapq.heappush(heap, (next_node.val, count, next_node))
            count += 1
        dummyiter = dummyiter.next

    return head.next

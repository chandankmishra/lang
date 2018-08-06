from collections import deque


def max_in_sliding_window(nums, k):
    # following solution is O(nk)
    # queue, output = deque(), []
    # for i, val in enumerate(nums):
    #     if i < k:
    #         queue.append(val)
    #         if i == (k-1):
    #             output.append(max(queue))
    #     else:
    #         queue.popleft()
    #         queue.append(val)
    #         output.append(max(queue))
    # return output

    #
    # Following solution is O(n)
    queue, output = deque(), []
    for i, val in enumerate(nums):
        while queue and queue[0] < (i - k + 1):
            queue.popleft()

        while queue and nums[queue[-1]] < val:
            queue.pop()

        queue.append(i)

        if i >= k - 1:
            output.append(nums[queue[0]])
    return output


print(max_in_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))

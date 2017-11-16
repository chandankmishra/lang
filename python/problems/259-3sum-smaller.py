def threeSumSmaller(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    n = len(nums)
    count = 0
    for i in range(0, n):
        for j in range(0, i):
            for k in range(0, j):
                if (i < j and j < k) and (nums[i] + nums[j] + nums[k] < target):
                    count += 1
    return count


nums = []
target = 0
print(threeSumSmaller(nums, target))

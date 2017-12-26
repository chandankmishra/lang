"""
287. Find the Duplicate Number

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""


def findDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int

    # first method
    n = len(nums) - 1
    sum_of_n = n * (n + 1) // 2

    total_sum = 0
    for i in nums:
        total_sum = total_sum + i
    if len(set(nums)) == 1:
        return nums[0]
    return total_sum - sum_of_n

    # next method
    for n in nums:
        if nums.count(n) > 1:
            return n
    return 0
    """
    # third method
    nset = set(nums)
    return (sum(nums) - sum(nset)) // (len(nums) - len(nset))


nums = [2, 2, 2, 2, 2]
print(findDuplicate(nums))

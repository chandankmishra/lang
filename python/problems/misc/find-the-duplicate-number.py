"""
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
    """
    n = len(nums) - 1
    sum_of_n = n * (n + 1) // 2

    total_sum = 0
    for i in nums:
        total_sum = total_sum + i

    return total_sum - sum_of_n


arr = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9]
print(findDuplicate(arr))

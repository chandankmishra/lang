"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""


def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    total = n * (n + 1) // 2

    sum = 0
    for i in nums:
        sum = sum + i

    return total - sum


arr = [0, 1, 3]
print (missingNumber(arr))

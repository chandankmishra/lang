"""
260. Single Number III
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""


def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    xor = nums[0]
    for i in range(1, len(nums)):
        xor = xor ^ nums[i]
    bit = xor & ~(xor - 1)

    ret = []
    num1 = 0
    num2 = 0
    for i in nums:
        if i & bit > 0:
            num1 ^= i
        else:
            num2 ^= i

    return [num1, num2]


nums = [1, 2, 1, 3, 2, 5]
print(singleNumber(nums))

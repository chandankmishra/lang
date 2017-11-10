"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

"""


def singleNumber(nums):
    final = nums[0]
    for i in range(1, len(nums)):
        final = final ^ nums[i]
    return final


arr = [2, 2, 3, 3, 4, 5, 6, 5, 6]
print (singleNumber(arr))

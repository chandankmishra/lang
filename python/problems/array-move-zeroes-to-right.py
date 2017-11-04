"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    i = 0
    j = 0
    while i < len(nums):
        while j < len(nums) and nums[j] == 0:
            j = j + 1
        if j < len(nums):
            nums[i] = nums[j]
            j = j + 1
        else:
            nums[i] = 0
        i = i + 1


arr = [0, 1, 0, 3, 12]
print (arr)
moveZeroes(arr)
print (arr)

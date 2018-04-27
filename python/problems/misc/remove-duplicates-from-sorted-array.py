"""
Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
"""


def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max = len(nums)
    i = 0
    j = 0
    while j < max:
        while nums[i] == nums[j]:
            j += 1
            if j >= max:
                return max if max == 0 else (i + 1)
        i += 1
        nums[i] = nums[j]
        j += 1
    return max if max == 0 else (i + 1)


arr = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4]
# arr = []
print(arr)
print(removeDuplicates(arr))
print (arr)

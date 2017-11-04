"""
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
"""


def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    data = set()
    for i in nums:
        if i in data:
            return True
        data.add(i)
    return False


arr = [1, 2, 3, 4, 5, 6, 4]
print (containsDuplicate(arr))

"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
"""


def findShortestSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_repeat = 0
    repeat = 0
    j = 0
    for i in nums:
        if i == j:
            repeat += 1
        else:
            if max_repeat < repeat:
                # print (max_repeat, repeat)
                max_repeat = repeat
            repeat = 0
        j = i
    return max_repeat + 1 if repeat < max_repeat else repeat + 1


# arr = [1, 2, 2, 3, 3, 3, 1, 1, 1, 1, 1, 6, 6, 6, 2, 2, 2, 2, 2, 2, 4]
# print(findShortestSubArray(arr))

arr = [1, 2, 2, 3, 1, 4, 2]
print(findShortestSubArray(arr))

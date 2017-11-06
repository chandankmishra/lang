"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
"""

def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    nums = []
    l1 = len(nums1)
    l2 = len(nums2)
    l = l1 if l1 < l2 else l2

    if l1 == 0 or l2 == 0:
        return nums

    j = 0
    istart = 0
    jstart = 0
    for i in range(0, l):
        if nums1[i] != nums2[j]
            j += 1
        print (i)
        istart = 1
        jstart = j
        i += 1
        j += 1
    return nums


arr1 = [1, 2, 2, 1]
arr2 = [2, 2]
print(intersection(arr1, arr2))

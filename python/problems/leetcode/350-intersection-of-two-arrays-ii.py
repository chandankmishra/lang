"""
350. Intersection of Two Arrays II

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

"""


def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """

    l1 = len(nums1)
    l2 = len(nums2)
    j = 0
    i = 0
    ret1 = []
    ret2 = []
    while i < l1 and j < l2:
        if nums1[i] == nums2[j]:
            ret1.append(nums1[i])
            j += 1
            i += 1
        else:
            ret1 = []
            j = j + 1

    while i < l1 and j < l2:
        if nums1[i] == nums2[j]:
            ret2.append(nums2[j])
            j += 1
            i += 1
        else:
            ret2 = []
            i = i + 1

    print ("ret1", ret1)
    print ("ret2", ret2)
    return ret1 if len(ret1) > len(ret2) else ret2


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersect(nums1, nums2))


nums1 = [1, 2, 2, 1]
nums2 = [2, 2, 1, 3, 5, 1, 2, 2, 1, 3]
print(intersect(nums1, nums2))

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
    nset1 = set(nums1)
    nset2 = set(nums2)

    return list(nset1 & nset2)


n1 = [1, 2, 2, 1]
n2 = [2, 2]
print (intersection(n1, n2))

# following soluation is incomplete
# l1 = len(nums1)
# l2 = len(nums2)

# if l1 == 0 or l2 == 0:
#     return []

# i2 = 0
# i1 = 0
# ret = []
# if l1 < l2:
#     for i1 in range(0, l1):
#         while nums1[i1] != nums2[i2]:
#             i2 += 1
#             print (nums1[i1], nums2[i2])
#         l1.append(nums1[i1])
# return []

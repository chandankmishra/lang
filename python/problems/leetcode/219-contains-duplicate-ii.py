"""
219. Contains Duplicate II

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
"""


def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    nmap = {}
    for i in range(0, len(nums)):
        if nums[i] not in nmap:
            nmap[nums[i]] = i
        else:
            if (abs(nmap[nums[i]] - i) <= k):
                return True
            nmap[nums[i]] = i
    return False


nums = []
k = 0
print (containsNearbyDuplicate(nums, k))

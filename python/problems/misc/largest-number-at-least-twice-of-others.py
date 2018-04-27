def dominantIndex(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l = len(nums)
    if l < 2:
        return 0
    tmp = nums.copy()
    tmp.sort()

    print (tmp, nums)
    if tmp[l - 1] >= 2 * tmp[l - 2]:
        return nums.index(tmp[l - 1])
    return -1


nums = [1]
print (dominantIndex(nums))

# nums = [3, 6, 1, 0]
# print (dominantIndex(nums))
# nums = [1, 2, 3, 4]
# print (dominantIndex(nums))

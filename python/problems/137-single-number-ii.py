def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    return (3 * sum(set(nums)) - sum(nums)) // 2


l = [3, 3, 3, 6, 6, 6, 2]
print(singleNumber(l))

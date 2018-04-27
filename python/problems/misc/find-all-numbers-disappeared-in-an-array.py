def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    newlist = list()
    for i in range(1, len(nums) + 1):
        newlist.append(i)
    for i in nums:
        if i in newlist:
            newlist.remove(i)
    return newlist


arr = [4, 3, 2, 7, 8, 2, 3, 1]
print(findDisappearedNumbers(arr))

def findDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # Method 1 with extra space (set)
    # tset = set()
    # res = []
    # for i in nums:
    #     if i not in tset:
    #         tset.add(i)
    #     else:
    #         res.append(i)
    # return newl

    # Method 2: O(1) space not including the input and output variables
    # The idea is we do a linear pass using the input array itself as a hash to
    # store which numbers have been seen before. We do this by making elements at
    # certain indexes negative. See the full explanation here
    res = []
    # print (nums)
    for x in nums:
        # print (x, abs(x), abs(x) - 1, nums[abs(x) - 1])
        if nums[abs(x) - 1] < 0:
            res.append(abs(x))
        else:
            nums[abs(x) - 1] *= -1
    return res


lst = [4, 3, 2, 7, 8, 2, 3, 1]
print(findDuplicates(lst))

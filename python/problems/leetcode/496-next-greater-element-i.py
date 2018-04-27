def nextGreaterElement(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    ret = []
    len2 = len(nums2)

    for n in nums1:
        if nums2.count(n) == 0:
            ret.append(-1)
            continue
        else:
            idx = nums2.index(n)
            if idx == len2 - 1:
                ret.append(-1)
                continue
            else:
                for i in range(idx + 1, len2):
                    if nums2[i] > n:
                        ret.append(nums2[i])
                        break
                    if i == len2 - 1:
                        ret.append(-1)
    return ret


n1 = [4, 1, 2]
n2 = [1, 3, 4, 2]
print (nextGreaterElement(n1, n2))

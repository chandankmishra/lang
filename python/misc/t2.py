def alternatve_pos_neg(nums):
    pos_count, neg_count = 0, 0
    pos, neg = [], []
    for num in nums:
        if num < 0:
            neg_count += 1
            neg.append(num)
        else:
            pos_count += 1
            pos.append(num)
    if not pos_count or not neg_count:
        return nums

    nums = []
    i, j, turn = 0, 0, 1
    while i < pos_count and j < neg_count:
        nums.append(pos[i])
        nums.append(neg[j])
        i, j = i + 1, j + 1
    if i != pos_count:
        nums += pos[i:]

    if j != neg_count:
        nums += neg[j:]
    return nums


print (alternatve_pos_neg([2, 3, -4, -9, -1, -7, 1, -5, -6]))

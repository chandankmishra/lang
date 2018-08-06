def binary_search_range(lst, num):
    start, end = -1, -1
    found = False
    for i, val in enumerate(lst):
        if val == num:
            if found is False:
                found = True
                start = i
            end = i
    return start, end

    # l = 0
    # r = len(lst)-1
    # while l < r:
    #     mid = (l+r+1) // 2
    #     if num < lst[mid]:
    #         l+=1
    #     elif num > lst[mid]:
    #         r-=1
    #     else:

    #         l+=1
    #         r-=1
    # pass


lst = [1, 1, 1, 2, 2, 2, 2, 3]
print(binary_search_range(lst, 2))

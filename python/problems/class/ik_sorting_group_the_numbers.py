# even, odd grouping (non stable!)
def group_numbers(narr):
    sidx, eidx = 0, len(narr) - 1
    while sidx < eidx:
        if narr[sidx] % 2 != 0 and narr[eidx] % 2 == 0:
            narr[sidx], narr[eidx] = narr[eidx], narr[sidx]
            sidx, eidx = sidx + 1, eidx - 1
        elif narr[sidx] % 2 != 0:
            eidx -= 1
        elif narr[eidx] % 2 == 0:
            sidx += 1
        else:
            sidx, eidx = sidx + 1, eidx - 1

# even, odd grouping (stable) - pending!


narr = [1, 2, 3, 4]
group_numbers(narr)
print(narr)

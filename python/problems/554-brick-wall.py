def leastBricks(wall):
    """
    :type wall: List[List[int]]
    :rtype: int
    """

    wdict = {}
    maxbrick = 0
    for row in wall:
        sum = 0
        for col in row[:-1]:
            sum += col
            if sum not in wdict:
                wdict[sum] = 1
            else:
                wdict[sum] += 1
            if maxbrick < wdict[sum]:
                maxbrick = wdict[sum]
    return (len(wall) - maxbrick)


wall = [[1, 2, 2, 1],
        [3, 1, 2],
        [1, 3, 2],
        [2, 4],
        [3, 1, 2],
        [1, 3, 1, 1]]

print(leastBricks(wall))

def numberOfBoomerangs(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    print (points)
    pmap = {}
    for point in points:
        pmap[point[0], point[1]] = 1

    print (pmap[0, 0])
    print (pmap.keys())
    print (pmap)
    count = 0
    for point1 in points:
        for point2 in points:
            data = str((point1[0] + point2[0]) / 2) + "-" + str((point1[1] + point2[1]) / 2)
            print (data)
            if data in pmap:
                count += 1
    # print(pmap)
    return count


arr = [[0, 0], [1, 0], [2, 0]]
print (numberOfBoomerangs(arr))

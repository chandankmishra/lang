"""
356. Line Reflection

Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points.

Example 1:
Given points = [[1,1],[-1,1]], return true.

Example 2:
Given points = [[1,1],[-1,-1]], return false.

Follow up:
Could you do better than O(n2)?
"""


def isReflected(points):
    """
    :type points: List[List[int]]
    :rtype: bool
    """
    sumx = 0
    n = len(points)
    if n % 2 != 0:
        return False

    for point in points:
        sumx += point[0]

    if sumx % 2 != 0:
        return False

    yaxis = sumx // n

    return {(x, y) for x, y in points} == {(yaxis - x, y) for x, y in points}


lst = [[1, 1], [-1, 1]]
print (isReflected(lst))

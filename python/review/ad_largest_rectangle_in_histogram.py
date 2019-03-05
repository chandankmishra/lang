'''
84. Largest Rectangle in Histogram
https://leetcode.com/problems/largest-rectangle-in-histogram/description/
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
'''


def largestRectangleArea(heights):
    # Using Stack Time Complexity O(n). Space Complexity O(n)
    # index is list of pillar index
    indices, max_area = [], 0
    for i, h in enumerate(heights + [0]):
        while indices and heights[indices[-1]] >= h:
            height = heights[indices.pop()]
            if indices:
                width = i - indices[-1] - 1
            else:
                width = i
            max_area = max(max_area, height * width)
        indices.append(i)
    return max_area

print (largestRectangleArea([2, 1, 5, 6, 2, 3]))  # ans=10


def largestRectangleAreaBF(heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    # Time Complexity O(n2). Space Complexity O(1)
    n = len(heights)
    max_area = 0
    for i in range(n):
        min_height = float("inf")
        for j in range(i, n):
            min_height = min(min_height, heights[j])
            max_area = max(max_area, min_height * (j - i + 1))
    return max_area
print (largestRectangleAreaBF([2, 1, 5, 6, 2, 3]))  # ans=10

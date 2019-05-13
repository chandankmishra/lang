class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # Using Stack Time Complexity O(n). Space Complexity O(n)
        indices, max_area = [], 0
        heights = heights + [0]

        for index, h in enumerate(heights):
            while indices and heights[indices[-1]] >= h:
                height = heights[indices.pop()]
                if indices:
                    width = index - indices[-1] - 1
                else:
                    width = index
                max_area = max(max_area, height * width)
            indices.append(index)
        return max_area

    def maximalRectangle(self, matrix):
        # Space compleity O(n) TimeComplexity O(n*m)
        rows = len(matrix)
        if rows == 0:
            return 0
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '1':
                    heights[c] += 1
                else:
                    heights[c] = 0
            max_area = max(max_area, self.largestRectangleArea(heights))
        return max_area


s = Solution()
matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
print(s.maximalRectangle(matrix))

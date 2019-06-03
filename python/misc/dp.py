class Solution:
    def uniquePaths(self, cols, rows):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
        dp[rows-1][cols-1] = 1
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1,-1):
                if i == rows-1 and j == cols-1:
                    continue
                dp[i][j] = dp[i+1][j]+dp[i][j+1]
        return dp[0][0]
        
###################################################

class Solution:
    def __init__(self):
        self.dict = {}
        
    def helper(self, grid, n, m, i, j):
        dp = [[[0] for _ in range(m+1)] for _ in range(n+1)]
        for i in range(n+1):
            dp[i][m] = float("inf")
        for i in range(m+1):
            dp[n][i] = float("inf")

        dp[n-1][m-1] = grid[n-1][m-1]
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if i == n-1 and j == m-1:
                    continue
                dp[i][j] = grid[i][j] + min(dp[i][j+1], dp[i+1][j])
        return dp[0][0]
        
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        return self.helper(grid, n, m, 0, 0)
        
###################################################

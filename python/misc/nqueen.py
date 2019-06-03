class Solution:
    def check_valid(self, col_placement, row1, col1):
        for row2 in range(row1):
            col2 = col_placement[row2]
            if col1 == col2:
                return False
            if abs(col2 - col1) == abs(row2 - row1):
                return False
        return True

    def helper(self, col_placement, n, row):
        count = 0
        if row == n:
            # All queens are legally placed
            return 1
        
        for col in range(n):
            if self.check_valid(col_placement, row, col):
                col_placement[row] = col
                count += self.helper(col_placement, n, row+1)
        return count

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        col_placement = [0] * n
        count = self.helper(col_placement, n, 0)
        return count
 
s = Solution()
print (s.totalNQueens(10))

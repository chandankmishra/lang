''' 70. Climbing Stairs
Formula:
dp[0] = 1
dp[n] = dp[n-1] + dp[n-2]
'''


def climb_stairs(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(n + 1):
        for step in [1, 2]:
            if i - step >= 0:
                dp[i] = dp[i] + dp[i - step]
    return dp[-1]


# print (climb_stairs(15))
###################################################
''' 198. House Robber
Formula:
dp[1] = nums[0]
dp[n] = max(dp[n-1], dp[n-2]+nums[n-1])
'''


def house_robber(nums):
    n = len(nums)
    dp = [0] * (n + 1)
    dp[1] = nums[0]
    for i in range(2, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
    return dp[n]


# print (house_robber([1, 2, 3, 1]))  # 4
# print (house_robber([2, 7, 9, 3, 1]))  # 12
######################################################
''' 322. Coin Change
Formula
dp[0] = 0
dp[n] = min((dp[i-d0], dp[i-d1].... dp[i-di], ... dp[i-dn-1]) + 1
'''


def coin_change(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for i in range(amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin]) + 1
    if dp[amount] == float("inf"):
        return -1
    return dp[amount]


# print (coin_change([1, 2, 5], 11))
# print (coin_change([2], 3))
######################################################
''' 518. Coin Change 2 https://leetcode.com/problems/coin-change-2/description/
Formula
The outer loop should be for coin. So that came coin should not be counted multiple time for different amounts
# dp[0] = 1
# dp[n] = sum((dp[i-d0], dp[i-d1].... dp[i-di], ... dp[i-dn-1]) (i-dk >=0)
'''


def coin_change2(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(amount + 1):
            if i - coin >= 0:
                dp[i] = dp[i] + dp[i - coin]
    return dp[amount]


# print (coin_change2([1, 2, 5], 5))
# print (coin_change2([2], 3))


######################################################
'''
64. Minimum Path Sum
Formula:
dp[n-1][m-1] = grid[n-1][m-1]
dp[r][c] = min(dp[r + 1][c], dp[r][c + 1]) + grid[r][c]
'''


def min_path_sum(grid):
    n = len(grid)
    m = len(grid[0])
    dp = [[float("inf") for _ in range(m + 1)] for _ in range(n + 1)]
    for r in range(n - 1, -1, -1):
        for c in range(m - 1, -1, -1):
            if r == n - 1 and c == m - 1:
                dp[r][c] = grid[r][c]
                continue
            dp[r][c] = min(dp[r + 1][c], dp[r][c + 1]) + grid[r][c]
    return dp[0][0]


arr = [[1, 3, 1], [1, 50, 10], [4, 2, 1]]
# print(min_path_sum(arr))

######################################################
'''
62. Unique Paths
Formula:
dp[rows-1][cols-1] = 1
dp[r][c] = dp[r+1][c] + dp[r][c+1]
'''


def unique_paths(cols, rows):
    dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
    for r in range(rows - 1, -1, -1):
        for c in range(cols - 1, -1, -1):
            if r == rows - 1 and c == cols - 1:
                dp[r][c] = 1
                continue
            dp[r][c] = dp[r + 1][c] + dp[r][c + 1]
    return dp[0][0]


# print (unique_paths(3, 2))  # 3
# print (unique_paths(7, 3))  # 28
######################################################
'''
63. Unique Paths II https://leetcode.com/problems/unique-paths-ii/description/
Formula:
# dp[rows-1][cols-1] = 1
# dp[r][c] = dp[r+1][c] + dp[r][c+1]
if grid[r][c] == 1 continue 0=>OK 1=>Obstracles
'''


def unique_paths(grid):
    rows = len(grid)
    cols = len(grid[0])
    dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
    for r in range(rows - 1, -1, -1):
        for c in range(cols - 1, -1, -1):
            if grid[r][c] == 1:
                continue
            if r == rows - 1 and c == cols - 1:
                dp[r][c] = 1
                continue
            dp[r][c] = dp[r + 1][c] + dp[r][c + 1]
    return dp[0][0]


arr = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
# print (unique_paths(arr))

######################################################
'''
583. Delete Operation for Two Strings (Longest Common Subsequence)
https://leetcode.com/problems/delete-operation-for-two-strings/description/
Formula:
dp[i][j] = dp[i-1][j-1] + 1 if word1[i-1] == word2[j-1]
dp[i][j] = max(dp[i-1][j], dp[i][j-1]) else
'''


def lcs(word1, word2):
    n1, n2 = len(word1), len(word2)
    dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n1][n2]


# print (lcs("aabcdex", "abcdefg"))
'''
97. Interleaving String
https://leetcode.com/problems/interleaving-string/description/
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
Formula:
dp[i][j] = True if dp[i-1][j] and s1[i-1] == s3[i+j-1]
                or dp[i][j-1] and s2[j-1] == s3[i+j-1]
'''


def isInterleave(s1, s2, s3):
    n1, n2, n3 = len(s1), len(s2), len(s3)
    if n1 + n2 != n3:
        return False
    dp = [[False for _ in range(n2 + 1)] for _ in range(n1 + 1)]
    dp[0][0] = True
    for i in range(0, n1 + 1):
        for j in range(0, n2 + 1):
            if ((i > 0 and dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or
                    (j > 0 and dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])):
                dp[i][j] = True
    return dp[n1][n2]


s1, s2, s3 = "aabcc", "dbbca", "aadbbcbcac"
# print (isInterleave(s1, s2, s3))
s1, s2, s3 = "aabcc", "dbbca", "aadbbbaccc"
# print (isInterleave(s1, s2, s3))

'''
221. Maximal Square
https://leetcode.com/problems/maximal-square/description/
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
Formula:
dp[n][0] = grid[n][0] # not required if dp table size is n+1, m+1
dp[0][m] = grid[0][m] # not required if dp table size is n+1, m+1
dp[r][c] = min(dp[r-1][c-1], dp[r-1][c], dp[r][c-1]) +1
'''


def maximalSquare(matrix):
    n, m = len(matrix), len(matrix[0])
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    max_square = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if matrix[i - 1][j - 1] == '1':
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                max_square = max(max_square, dp[i][j])
    return max_square * max_square


matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
# print (maximalSquare(matrix))

'''
416. Partition Equal Subset Sum
https://leetcode.com/problems/partition-equal-subset-sum/description/
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
Formula:


'''


def canPartition(nums):
    return False


print (canPartition([1, 5, 11, 5]))
print (canPartition([1, 2, 3, 5]))

'''
https://leetcode.com/problems/climbing-stairs/description/                      DONE
https://leetcode.com/problems/house-robber/description/                         DONE
https://leetcode.com/problems/coin-change/
https://leetcode.com/problems/coin-change-2/description/                        #PENDING
https://leetcode.com/problems/minimum-path-sum/                                 DONE
https://leetcode.com/problems/unique-paths/                                     DONE
https://leetcode.com/problems/unique-paths-ii/description/                      DONE
https://leetcode.com/problems/min-cost-climbing-stairs/description/             #PENDING
https://leetcode.com/problems/maximal-square/description/                       DONE
https://www.geeksforgeeks.org/maximum-product-cutting-dp-36/                    #PENDING
https://leetcode.com/problems/delete-operation-for-two-strings/description/     DONE
https://leetcode.com/problems/edit-distance/description/                        DONE
https://leetcode.com/problems/interleaving-string/description/                  DONE

https://leetcode.com/problems/partition-equal-subset-sum/description/           #PENDING
https://leetcode.com/problems/word-break/description/                           #PENDING
https://leetcode.com/problems/word-break-ii/description/                        #PENDING

https://leetcode.com/problems/cherry-pickup/
https://leetcode.com/problems/dungeon-game/


'''

''' 70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/description/
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
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
https://leetcode.com/problems/house-robber/description/
Constriant: Two consecutive houses can not be robbed.
Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
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
https://leetcode.com/problems/coin-change/
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
Formula
dp[0] = 0
dp[n] = min((dp[i-d0], dp[i-d1]..... dp[i-dn-1]) + 1
'''


def coin_change(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for i in range(amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    if dp[amount] == float("inf"):
        return -1
    return dp[amount]


# print (coin_change([1, 2, 5], 11))
# print (coin_change([2], 3))
######################################################
''' 518. Coin Change 2
https://leetcode.com/problems/coin-change-2/description/
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.
Formula
The outer loop should be for coin. So that came coin should not be counted multiple time for different amounts
# dp[0] = 1
# dp[n] = sum((dp[i-d0], dp[i-d1]..... dp[i-dn-1]) (i-dk >=0)
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
https://leetcode.com/problems/minimum-path-sum/
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Formula:
dp[n-1][m-1] = grid[n-1][m-1]
dp[r][c] = min(dp[r + 1][c], dp[r][c + 1]) + grid[r][c]
'''


def min_path_sum(grid):
    n = len(grid)
    m = len(grid[0])
    dp = [[float("inf") for _ in range(m + 1)] for _ in range(n + 1)]
    dp[n - 1][m - 1] = grid[n - 1][m - 1]
    for r in range(n - 1, -1, -1):
        for c in range(m - 1, -1, -1):
            if r == n - 1 and c == m - 1:
                continue
            dp[r][c] = min(dp[r + 1][c], dp[r][c + 1]) + grid[r][c]
    return dp[0][0]


arr = [[1, 3, 1], [1, 50, 10], [4, 2, 1]]
# print(min_path_sum(arr))

######################################################
'''
62. Unique Paths
https://leetcode.com/problems/unique-paths/
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?
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
63. Unique Paths II
https://leetcode.com/problems/unique-paths-ii/description/
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
Now consider if some obstacles are added to the grids. How many unique paths would there be?
Formula:
# dp[rows-1][cols-1] = 1
# dp[r][c] = dp[r+1][c] + dp[r][c+1]
if grid[r][c] == 1 continue 0=>OK 1=>Obstracles
'''


def unique_paths(grid):
    rows = len(grid)
    cols = len(grid[0])
    dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
    dp[n - 1][m - 1] = 1
    for r in range(rows - 1, -1, -1):
        for c in range(cols - 1, -1, -1):
            if grid[r][c] == 1:
                continue
            if r == rows - 1 and c == cols - 1:
                continue
            dp[r][c] = dp[r + 1][c] + dp[r][c + 1]
    return dp[0][0]


arr = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
# print (unique_paths(arr))

######################################################
'''
583. Delete Operation for Two Strings (Longest Common Subsequence)
https://leetcode.com/problems/delete-operation-for-two-strings/description/
Given two sequences, find the length of longest subsequence present in both of them
Formula:
if word1[i-1] == word2[j-1]: dp[i][j] = dp[i-1][j-1] + 1
else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
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
if n1 + n2 != n3: return False
dp[0][0] = True
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
Knight's tour!
How many different phone numbers of given length can be formed starting from the
given digit? The constraint is that the movement from one digit to the next is
similar to the movement of the Knight in a chess game.

Formula:
dp[digit][num_digit] = (dp[0][num_digit - 1], dp[1][num_digit - 1],.... dp[i][num_digit - 1]) for i in range(moves[digit])

'''


def num_phone_numbers(startdigit, phonenumberlength):
    move = [[4, 6], [8, 6], [7, 9], [4, 8], [3, 9, 0], [None], [1, 7, 0], [2, 6], [1, 3], [2, 4]]
    dp = [[0 for _ in range(phonenumberlength + 1)] for _ in range(10)]

    for i in range(10):
        dp[i][1] = 1

    for c in range(2, phonenumberlength + 1):
        for r in range(10):
            for num in move[r]:
                if num is not None:
                    dp[r][c] += dp[num][c - 1]
    return dp[startdigit][phonenumberlength]


# print (num_phone_numbers(1, 3))

'''
72. Edit Distance
https://leetcode.com/problems/edit-distance/description/
Formula:
dp[0][i] = i
dp[j][0] = j
if W1[i-1] == W2[j-1]:
    dp[i][j] = dp[i-1][j-1]
else:
    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
'''


def minDistance(w1, w2):
    n1, n2 = len(w1), len(w2)
    if n1 == 0 or n2 == 0:
        return n1 or n2

    dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

    # base cases
    for i in range(n1 + 1):
        dp[i][0] = i
    for j in range(n2 + 1):
        dp[0][j] = j

    # recursive code
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if w1[i - 1] == w2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
    return dp[n1][n2]


# print (minDistance("horse", "ros"))  # 3
# print (minDistance("intention", "execution"))  # 5


'''
Cut The Rope
https://www.geeksforgeeks.org/maximum-product-cutting-dp-36/
Given a rope of length n meters, cut the rope in different parts of integer lengths in a way that maximizes product of lengths of all parts. You must make at least one cut. Assume that the length of rope is more than 2 meters.

Formula:
dp[0] = dp[1] = 0
dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j])) [1<=i<=n]
'''


def helper(n, cache):
    # Base cases
    if (n == 0 or n == 1):
        cache[n] = 0
        return 0
    if n in cache:
        return cache[n]

    # Make a cut at different places
    # and take the maximum of all
    max_val = 0
    for i in range(1, n):
        max_val = max(max_val, max(i * (n - i), i * helper(n - i, cache)))

    # Return the maximum of all values
    cache[n] = max_val
    return cache[n]


def maxProdMemo(n):
    return helper(n, {})


def maxProdDp(n):
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 0
    for i in range(1, n + 1):
        for j in range(1, i // 2 + 1):
            dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]))
    return dp[n]


# print("Maximum Product is ", maxProdMemo(5))
# print("Maximum Product is ", maxProdMemo(10))
# print("Maximum Product is ", maxProdDp(5))
# print("Maximum Product is ", maxProdDp(10))


'''
139. Word Break
https://leetcode.com/problems/word-break/description/
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
'''


def wordBreakDP(s, wordDict):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    wordDict = set(wordDict)
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break
    return dp[n]


def helper(s, start, wordDict, cache):
    n = len(s)
    if start == n:
        return True

    if start in cache:
        return cache[start]

    for end in range(start + 1, n + 1):
        if s[start:end] not in wordDict:
            continue
        if helper(s, end, wordDict, cache):
            cache[start] = True
            return True
    cache[start] = False
    return False


def wordBreakMemo(s, wordDict):
    return helper(s, 0, set(wordDict), {})


# print ("leetcode", wordBreakMemo("leetcode", ["leet", "code"]))
# print ("applepenapple", wordBreakMemo("applepenapple", ["apple", "pen"]))
# print ("catsandog", wordBreakMemo("catsandog", ["cats", "dog", "sand", "and", "cat"]))


'''
140. Word Break II
https://leetcode.com/problems/word-break-ii/description/
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.
'''


def wordBreak2DP(s, wordDict):
    n = len(s)
    dp = [[]] * (n + 1)
    wordDict = set(wordDict)
    for i in range(1, n + 1):
        new_lst = []
        for j in range(i):
            right = s[j:i]
            if right in wordDict:
                remainder = dp[j]
                if remainder:
                    for x in remainder:
                        new_lst.append(x + " " + right)
                elif j == 0:
                    new_lst.append(right)
        dp[i] = new_lst
    return dp[-1]


def helper2(s, start, wordDict, cache):
    n = len(s)
    if start == n:
        return []

    if start in cache:
        return cache[start]

    new_lst = []
    for end in range(start + 1, n + 1):
        left = s[start:end + 1]
        # print (left, start, end)
        if left not in wordDict:
            continue

        remainder = helper2(s, end + 1, wordDict, cache)
        if remainder:
            for x in remainder:
                new_lst.append(left + " " + x)
        elif (end == n - 1):
            new_lst.append(left)
    cache[start] = new_lst
    return cache[start]


def wordBreak2Memo(s, wordDict):
    return helper2(s, 0, set(wordDict), {})


# print (wordBreak2Memo("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
# print (wordBreak2DP("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
# print (wordBreak2DP("leetcode", ["leet", "code"]))
# print (wordBreak2DP("applepenapple", ["apple", "pen"]))
# print (wordBreak2DP("catsandog", ["cats", "dog", "sand", "and", "cat"]))


'''
416. Partition Equal Subset Sum
https://leetcode.com/problems/partition-equal-subset-sum/description/
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
Formula:
'''


def findSum(nums, start, target, memo):
    if (start, target) in memo:
        return memo[(start, target)]

    if target < 0:
        return False
    elif target == 0:
        return True

    for i in range(start, len(nums)):
        if findSum(nums, i + 1, target - nums[i], memo):
            return True
    memo[(start, target)] = False
    return False


def canPartition2Subset(nums):
    s = sum(nums)
    if s % 2:
        return False
    s = s / 2
    return findSum(nums, 0, s, {})


testcases = [
    [1, 5, 11, 5],
    [1, 2, 3, 5],
    [1, 2, 3, 5, 8]
]
for testcase in testcases:
    print ("canPartition2Subset", testcase, canPartition2Subset(testcase))


'''
698. Partition to K Equal Sum Subsets
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.
Formula:
'''


def helper1(nums, visited, k, start, cur_sum, target):
    if k == 1:
        return True

    n = len(nums)
    if cur_sum == target:
        return helper1(nums, visited, k - 1, 0, 0, target)

    for i in range(start, n):
        if visited[i] == 0:
            visited[i] = 1
            if helper1(nums, visited, k, i + 1, cur_sum + nums[i], target):
                return True
            visited[i] = 0
    return False


def canPartitionKSubset(nums, k):
    nsum = sum(nums)
    n = len(nums)
    if k <= 0 or nsum % k:
        return False

    visited = [0] * n
    target = nsum // k
    return helper1(nums, visited, k, 0, 0, target)


testcases = [
    [[4, 3, 2, 3, 5, 2, 1], 4],
    [[2, 2, 2, 2], 4],
    [[2, 2, 2, 2], 3]
]

for testcase in testcases:
    print ("canPartitionKSubset", testcase[0], testcase[1],
           canPartitionKSubset(testcase[0], testcase[1]))

'''
410. Split Array Largest Sum
https://leetcode.com/problems/split-array-largest-sum/
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.
nums = [7,2,5,10,8] m = 2
Output: 18
'''


def splitArray(nums, m):
    nlen = len(nums)

    presum = [0] * (nlen + 1)
    for i, n in enumerate(nums):
        presum[i + 1] = n + presum[i]

    dp = [[float("inf")] * (m + 1) for _ in range(nlen + 1)]
    dp[0][0] = 0
    for i in range(1, nlen + 1):
        for j in range(1, m + 1):
            for k in range(i):
                dp[i][j] = min(dp[i][j], max(dp[k][j - 1], presum[i] - presum[k]))
    return dp[nlen][m]


testcases = [
    [[7, 2, 5, 10, 8], 2],
    [[4, 3, 2, 3, 5, 2, 1], 4],
    [[2, 2, 2, 2], 4],
    [[2, 2, 2, 2], 3]
]
for testcase in testcases:
    print ("splitArray", testcase[0], testcase[1],
           "ans", splitArray(testcase[0], testcase[1]))

'''
741. Cherry Pickup
https://leetcode.com/problems/cherry-pickup/
In a N x N grid representing a field of cherries, each cell is one of three possible integers.
0 means the cell is empty, so you can pass through;
1 means the cell contains a cherry, that you can pick up and pass through;
-1 means the cell contains a thorn that blocks your way.
'''
def dp(grid, memo, r1, c1, c2):
    N = len(grid)
    r2 = r1 + c1 - c2
    if (N == r1 or N == r2 or N == c1 or N == c2 or grid[r1][c1] == -1 or grid[r2][c2] == -1):
        return float('-inf')
    elif r1 == c1 == r2 == c2 == N-1:
        return grid[r1][c1]
    elif memo[r1][c1][c2] is not None:
        return memo[r1][c1][c2]
    else:
        if r1 == r1 and c1 == c2:
            ans = grid[r1][c1]
        else:
            ans = grid[r1][c1] + grid[r2][c2]

        ans += max(dp(grid, memo, r1, c1+1, c2+1), dp(grid, memo, r1+1, c1, c2+1),
            dp(grid, memo, r1, c1+1, c2), dp(grid, memo, r1+1, c1, c2))
    memo[r1][c1][c2] = ans
    return ans

def cherryPickup(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    N = len(grid)
    memo = [[[None] * N for _ in range(N)] for _ in range(N)]
    return max(0, dp(grid, memo, 0, 0, 0))

grid = [[0,1,-1],[1,0,-1],[1,1,1]]
print ("cherryPickup", grid, cherryPickup(grid))

'''
174. Dungeon Game
https://leetcode.com/problems/dungeon-game/
'''
def calculateMinimumHP(d):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    n = len(d)
    m = len(d[0])
    dp = [[float("inf") for _ in range(m+1)] for _ in range(n+1)]
    dp[n-1][m] = dp[n][m-1] = 1

    for i in range(n-1, -1, -1):
        for j in range(m-1,-1,-1):
            need = min(dp[i+1][j], dp[i][j+1]) - d[i][j]
            dp[i][j] = 1 if need <= 0 else need
    return dp[0][0]

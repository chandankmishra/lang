''' 70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/description/
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
''' 518. Coin Change 2
https://leetcode.com/problems/coin-change-2/description/
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
https://leetcode.com/problems/minimum-path-sum/
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
https://leetcode.com/problems/unique-paths/
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

def helper(nums, start, target, memo):
    n = len(nums)
    if target < 0 or start == n:
        return False

    if target == 0:
        return True

    if memo[start][target] is not None:
        return memo[start][target]
    # target - nums[start] includes nums[start] in the target sum
    # other case excludes the nums[start] from the target sum
    if helper(nums, start + 1, target, memo) or helper(nums, start + 1, target - nums[start], memo):
        memo[start][target] = True
        return True

    memo[start][target] = False
    return False


def canPartition(nums):
    target = sum(nums)
    if target % 2 == 1:
        return False
    target = target // 2
    n = len(nums)
    memo = [[None for _ in range(target + 1)] for _ in range(n)]
    return helper(nums, 0, target, memo)


#print (canPartition([1, 5, 11, 5]))
#print (canPartition([1, 2, 3, 5]))

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


print (wordBreakMemo("leetcode", ["leet", "code"]))
print (wordBreakMemo("applepenapple", ["apple", "pen"]))
print (wordBreakMemo("catsandog", ["cats", "dog", "sand", "and", "cat"]))


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

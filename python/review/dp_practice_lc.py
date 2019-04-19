'''
300. Longest Increasing Subsequence
https://leetcode.com/problems/longest-increasing-subsequence/description/
Given an unsorted array of integers, find the length of longest increasing subsequence.

Formula:
if nums[i] > nums[j]:
    dp[i] = max(dp[i], dp[j] + 1)


'''


def lengthOfLIS(nums):
    n = len(nums)
    dp = [1] * n
    max_val = 0
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        max_val = max(max_val, dp[i])
    return max_val


# print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 101, 102, 18]))

'''
53. Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
'''


def maxSubArray(A):
    max_so_far = 0
    current_sum = 0
    for num in A:
        if current_sum < 0:
            current_sum = 0
        current_sum += num
        max_so_far = max(max_so_far, current_sum)
    return max_so_far


print (maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print (maxSubArray([-2, 1, -3, 4, -1, 2, 1, 1, 20, -10, 22, 14, 25, 21, -3, -5, 4]))

'''
139. Word Break
https://leetcode.com/problems/word-break/description/
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
'''


def wordBreakMemo(s, wordDict):
    pass


# print (wordBreakMemo("leetcode", ["leet", "code"]))
# print (wordBreakMemo("applepenapple", ["apple", "pen"]))
# print (wordBreakMemo("catsandog", ["cats", "dog", "sand", "and", "cat"]))

'''
516. Longest Palindromic Subsequence
https://leetcode.com/problems/longest-palindromic-subsequence/description/
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.
'''


def longestPalindromeSubseq(s):
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    print (n)
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            print ("i", i, "j", j)
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return (dp[0][n - 1])


print (longestPalindromeSubseq("bbbab"))


def check_if_sum_possible(arr, k):
    if k == 0 and k not in arr:
        return False
    dp = [False] * (k + 1)
    dp[0] = True
    for num in arr:
        for i in range(k + 1):
            if i - num < 0:
                continue
            if dp[i - num]:
                dp[i] = True
    return dp[k]


print (check_if_sum_possible([2, 4, 8], 6))

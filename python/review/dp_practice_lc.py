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
        current_sum += num
        if current_sum < 0:
            current_sum = 0
        max_so_far = max(max_so_far, current_sum)
    return max_so_far


# print (maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# print (maxSubArray([-2, 1, -3, 4, -1, 2, 1, 1, 20, -10, 22, 14, 25, 21, -3, -5, 4]))

'''
139. Word Break
https://leetcode.com/problems/word-break/description/
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
'''


def wordBreakMemo(s, wordDict):
    pass


print (wordBreakMemo("leetcode", ["leet", "code"]))
print (wordBreakMemo("applepenapple", ["apple", "pen"]))
print (wordBreakMemo("catsandog", ["cats", "dog", "sand", "and", "cat"]))

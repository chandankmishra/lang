"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""
import string

def longestPalindrome(s):
    """
    :type s: str
    :rtype: int
    """
    total = 0
    repeat_odd = False
    for i in string.ascii_lowercase:
        cnt = s.count(i)
        if cnt == len(s):
            return cnt

        if cnt % 2 == 0:
            total += cnt
        else:
            repeat_odd = True
            total += cnt - 1

    for i in string.ascii_uppercase:
        cnt = s.count(i)
        if cnt == len(s):
            return cnt
        if cnt % 2 == 0:
            total += cnt
        else:
            repeat_odd = True
            total += cnt - 1

    return (total + 1) if repeat_odd is True else total


print (longestPalindrome("bananas"))
print (longestPalindrome("ccc"))
print (longestPalindrome("ananan"))

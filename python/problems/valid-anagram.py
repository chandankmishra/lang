"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
import string
from string import ascii_lowercase


def isAnagram(s, t):
    for i in string.ascii_lowercase:
        if s.count(i) != t.count(i):
            return False

    return True

# def isAnagram(s, t):
#     """
#     :type s: str
#     :type t: str
#     :rtype: bool
#     """
#     if len(s) != len(t):
#         return False
#
#     map1 = {}
#     for i in s:
#         io = ord(i)
#         if io in map1:
#             map1[io] += 1
#         else:
#             map1[io] = 1
#
#     map2 = {}
#     for i in t:
#         io = ord(i)
#         if io in map2:
#             map2[io] += 1
#         else:
#             map2[io] = 1
#
#     for i in map1:
#         if i not in map2:
#             return False
#         if map1[i] != map2[i]:
#             return False
#     return True


s = "aacc"
t = "ccac"
print(isAnagram(s, t))

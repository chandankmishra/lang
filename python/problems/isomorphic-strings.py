"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
"""


def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    return len(set(s)) == len(set(zip(s, t))) == len(set(t))

# def isIsomorphic(s, t):
#     """
#     :type s: str
#     :type t: str
#     :rtype: bool
#     """
#     d = dict()
#     r = set()
#     for a, b in zip(s, t):
#         if a in d:
#             if d[a] != b:
#                 return False
#         else:
#             if b in r:
#                 return False
#             d[a] = b
#             r.add(b)
#     return True

# def isIsomorphic(s, t):
#     """
#     :type s: str
#     :type t: str
#     :rtype: bool
#     """
#     map1 = {}
#     map2 = {}
#     for i in range(0, len(s)):
#         if s[i] not in map1:
#             map1[s[i]] = t[i]
#         else:
#             print (s, t, i)
#             print (map1[s[i]], t[i])
#             if map1[s[i]] != t[i]:
#                 return False
#         if t[i] not in map2:
#             map2[t[i]] = s[i]
#         else:
#             print (s, t, i)
#             print (map2[t[i]], s[i])
#             if map2[t[i]] != s[i]:
#                 return False

#     return True


# print(isIsomorphic("egg", "add"))
print(isIsomorphic("eggsta", "addtkm"))

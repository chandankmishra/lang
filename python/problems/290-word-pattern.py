"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
"""


def wordPattern(pattern, str):
    """
    :type pattern: str
    :type str: str
    :rtype: bool
    """
    if not pattern or not str:
        return False

    wlist = str.split(' ')
    if len(pattern) != len(wlist):
        return False

    pmap = {}
    pset = set()
    j = 0
    for i in pattern:
        if i not in pmap:
            pmap[i] = wlist[j]
            if wlist[j] in pset:
                return False
            pset.add(wlist[j])
        else:
            if pmap[i] != wlist[j]:
                return False
        j += 1

    return True


print (wordPattern("abba", "dog cat cat dog"))
print (wordPattern("abba", "dog cat cat fish"))
print (wordPattern("aaaa", "dog cat cat dog"))
print (wordPattern("abba", "dog dog dog dog"))
print (wordPattern("aaaa", "dog dog dog dog"))

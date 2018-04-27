"""
Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.
"""
import string

def canPermutePalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    aset = set()
    odd_cnt = 0
    for i in s:
        # if the charactor is present in the set then continue
        if i in aset:
            continue

        cnt = s.count(i)
        if cnt == len(s):
            return True
        # if the charactor with odd count is more than one then
        # number can not be palindrome. Return False.
        if cnt % 2 != 0:
            if odd_cnt > 0:
                return False
            odd_cnt += 1

        # add charactor in the set
        aset.add(i)

    return True


print (canPermutePalindrome("aabbccc"))
print (canPermutePalindrome("code"))
print (canPermutePalindrome("aab"))
print (canPermutePalindrome("carerac"))
print (canPermutePalindrome("AaBb//a"))

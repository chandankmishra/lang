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

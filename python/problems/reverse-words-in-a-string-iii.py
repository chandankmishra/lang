def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    n = len(s)
    for i in range(0, n // 2):
        s[i] = s[n - 1 - i]


def reverseString(s):
    fstr = ""
    bstr = ""
    mstr = ""
    n = len(s)
    for i in range(0, n // 2):
        fstr = s[i] + fstr
        bstr = bstr + s[n - 1 - i]
    if n % 2 != 0:
        mstr = s[n // 2 + 1]
    return bstr + mstr + fstr


data = "Let's take LeetCode contest"
print (reverseString(data))

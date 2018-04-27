
"""
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""
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

def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    wlist = s.split(' ')
    max = len(wlist)
    finalstr = ""
    j = 0
    for i in wlist:
        finalstr = finalstr + reverseString(i) + ("" if (j == (max - 1)) else " ")
        j += 1
    return finalstr


data = "Let's take LeetCode contest"
print (data)
print (reverseWords(data))

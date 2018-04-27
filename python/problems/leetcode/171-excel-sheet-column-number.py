"""
171. Excel Sheet Column Number

Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.
"""


def titleToNumber(s):
    """
    :type s: str
    :rtype: int
    """
    sum = 0
    for i in s:
        sum = sum * 26 + (ord(i) - (ord('A') - 1))
    return sum


print (titleToNumber('A'))
print (titleToNumber('AA'))
print (titleToNumber('AZ'))
print (titleToNumber('BA'))
print (titleToNumber('AAA'))

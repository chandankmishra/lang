"""
8. String to Integer (atoi)

Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
"""

import string

INT_MAX = 2147483647
INT_MIN = -2147483648


def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    l = []
    if len(str) == 0:
        return 0
    digitBegin = False
    neg = False
    preNeg = False
    prePos = False
    for i in str:
        if i == '-':
            if digitBegin is True or prePos is True:
                return 0
            neg = True
            preNeg = True
            continue

        if i == '+':
            if digitBegin is True or preNeg is True:
                return 0
            prePos = True
            continue

        if i in string.digits:
            digitBegin = True
            l.append(ord(i) - ord('0'))

        preNeg = False
        prePos = False

    if len(l) == 0:
        return 0

    final = 0
    for j in l:
        final = (final * 10) + j

    if final > INT_MAX or final < INT_MIN:
        return 0

    if neg is True:
        final = final * (-1)
    return final


print(myAtoi("  -+1"))
print(myAtoi("  +-152"))
print(myAtoi(""))
print(myAtoi("    "))
print(myAtoi("1"))
print(myAtoi("12"))
print(myAtoi("23442"))
print(myAtoi("  352"))
print(myAtoi("  -152"))

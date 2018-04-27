"""
246. Strobogrammatic Number

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.
"""


def isStrobogrammatic(num):
    """
    :type num: str
    :rtype: bool
    """
    l = len(num)

    if l == 1:
        if num[0] == "0" or num[0] == "1" or num[0] == "8":
            return True
        else:
            return False

    for i in range(0, (l // 2) + 1):
        if num[i] == num[l - 1 - i]:
            # print ("#1 ", num[i], " - ", num[l - 1 - i])
            if num[i] == "0" or num[i] == "1" or num[i] == "8":

                continue
            else:
                return False
        else:
            # print ("#2 ", num[i], " - ", num[l - 1 - i])
            if (num[i] == "9" and num[l - 1 - i] == "6") or (num[i] == "6" and num[l - 1 - i] == "9"):

                continue
            else:
                return False

    return True


s = "96801866069810896"
print(isStrobogrammatic(s))

s = "659"
print(isStrobogrammatic(s))

s = "1"
print(isStrobogrammatic(s))

s = "11"
print(isStrobogrammatic(s))

s = "2"
print(isStrobogrammatic(s))

s = "88"
print(isStrobogrammatic(s))

s = "818"
print(isStrobogrammatic(s))

s = "181"
print(isStrobogrammatic(s))

s = "182"
print(isStrobogrammatic(s))

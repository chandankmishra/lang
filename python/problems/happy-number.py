"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""

# Solve using iteration


def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    amap = set()
    amap.add(n)
    print (amap)
    while n != 1:
        sum = 0
        while n > 0:
            sum = sum + (n % 10) * (n % 10)
            n = n // 10
        print (sum, amap)
        if sum in amap:
            return False
        else:
            amap.add(sum)
        n = sum
    return True


num = 19
print(isHappy(num))

# Solve using recursion


def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    if n == 1:
        return True

    sum = 0
    while n > 0:
        sum = sum + (n % 10) * (n % 10)
        n = n // 10
    return isHappy(sum)

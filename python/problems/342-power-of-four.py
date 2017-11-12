"""
342. Power of Four

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?
"""


def isPowerOfFour(num):
    """
    :type num: int
    :rtype: bool
    """
    if num <= 0:
        return False

    count = 0
    for i in range(0, 32):
        if num & (1 << i):
            count += 1
            if i % 2 != 0:
                return False

    if count != 1:
        return False

    return True


print (1, isPowerOfFour(1))
print (2, isPowerOfFour(2))
print (3, isPowerOfFour(3))
print (4, isPowerOfFour(4))
print (5, isPowerOfFour(5))
print (8, isPowerOfFour(8))
print (16, isPowerOfFour(16))

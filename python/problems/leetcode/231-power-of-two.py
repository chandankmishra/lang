"""
231. Power of Two
Given an integer, write a function to determine if it is a power of two.
"""
def isPowerOfTwo(n):
    """
    :type n: int
    :rtype: bool
    """
    if n <= 0:
        return False

    count = 0
    for i in range(0, 32):
        if n & (1 << i):
            count += 1

    if count != 1:
        return False

    return True


print (isPowerOfTwo(6))

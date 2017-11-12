"""
326. Power of Three

Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?
"""
Max3PowerInt = 1162261467  # 3^19, 3^20 = 3486784401 > MaxInt32
MaxInt32 = 2147483647  # 2^31 - 1


def isPowerOfThree(n):
    """
    :type n: int
    :rtype: bool
    """
    # if (n <= 0 or n > Max3PowerInt):
    #     return False
    # return Max3PowerInt % n == 0

    m = n
    while m > 1:
        if m % 3 != 0:
            return False
        else:
            m = m / 3
    return True if m == 1 else False

print(isPowerOfThree(3))

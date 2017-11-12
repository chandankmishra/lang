"""
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

Example 1:
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101
"""


def hasAlternatingBits(n):
    """
    :type n: int
    :rtype: bool
    """
    prev = n % 2
    n = n // 2
    while (n > 0):
        curr = n % 2
        if curr == prev:
            return False
        prev = curr
        n = n // 2

    return True


print(hasAlternatingBits(15))

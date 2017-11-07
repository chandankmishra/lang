"""
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
"""


def findNthDigit(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 9:
        return n

    nth = 9
    for i in range(10, n + 1):
        while i > 0:
            if nth == n:
            print (n % 10)
            i = i // 10

    return 10


print (findNthDigit(1))

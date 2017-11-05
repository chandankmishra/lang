"""
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
"""

num = 5


def findComplement(num):
    new = 0
    while num > 0:
        new = new * 2 + 1 if num % 2 == 0 else 0
        #print (new)
        num = num // 2
    return (new)


# findComplement(num)
print(findComplement(num))


print (5 >> 1)

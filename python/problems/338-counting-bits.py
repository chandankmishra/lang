"""
338. Counting Bits

Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
"""


def countBits(num):
    """
    :type num: int
    :rtype: List[int]
    """
    n = [0 for i in range(0, num + 1)]
    for i in range(0, num + 1):
        count = 0
        for j in range(0, 32):
            if i & (1 << j):
                count += 1
        n[i] = count
    return n


print(countBits(15))

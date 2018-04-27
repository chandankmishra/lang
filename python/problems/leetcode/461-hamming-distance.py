"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:
Input: x = 1, y = 4
Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""
a = 0x1
b = 0x4


def get_hamming_distance(a, b):
    count = 0
    while a > 0 or b > 0:
        if a % 2 != b % 2:
            count = count + 1
        print ("a =", a % 2, "b =", b % 2)
        a = a // 2
        b = b // 2
    return count


print (get_hamming_distance(a, b))

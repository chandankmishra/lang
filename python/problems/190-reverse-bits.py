"""
190. Reverse Bits
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?
"""


def reverseBits(n):
    k = 0
    for i in range(0, 32):
        if n & (1 << i):
            k |= (1 << 31 - i)
    return k


print(reverseBits(43261596))
print(reverseBits(2147483648))

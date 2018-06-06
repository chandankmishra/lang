def get_parity(num):
    count = 0
    while num:
        num = num & (num - 1)
        count += 1
    print(count)
    return count % 2


print(get_parity(0x3d))

'''
If parity needs to be computed for very large number of intergers then we
can store the parity of 0-15 and we break the 64 bit number into 4 parts
and compute the parity of earch part separtely by array lookup. Then we
add them and return the mod 2 as result.
'''

'''
Another way to calculate parity is by calculating the parity of the xor
of the first & second half.
'''


def get_parity1(num):
    num ^= num >> 32
    num ^= num >> 16
    num ^= num >> 8
    num ^= num >> 4
    num ^= num >> 2
    num ^= num >> 1
    return num & 0x1


print(get_parity1(0x3d))

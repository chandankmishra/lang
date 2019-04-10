"""
EPI 24.18 Find an element that aprears only once
All other other elements apreas 3 time

A=[2,4,2,5,2,5,5] ans = 4
"""


def handle_negative(n):
    if n < 2 ** 31:
        return n
    else:
        return n - 2 ** 32


def find_element_apears_once(A):
    count = [0] * 32
    for num in A:
        for i in range(32):
            if num & 1:
                count[i] += 1
            num >>= 1

    nsum = 0
    for i, c in enumerate(count):
        if c % 3:
            nsum += (1 << i)
    return handle_negative(nsum)


A = [2, 40, 2, 5, 2, 5, 5, 7, 7, 7]
print(find_element_apears_once(A))

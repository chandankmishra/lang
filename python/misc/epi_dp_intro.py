from itertools import *


def fibonacchi(n):
    if n <= 1:
        return n
    f_minus_2, f_minus_1 = 0, 1

    for i in range(1, n):
        f = f_minus_2 + f_minus_1
        f_minus_2, f_minus_1 = f_minus_1, f
    return f_minus_1


print("fibonacchi", fibonacchi(10))


def find_maximum_subarray(arr):
    i = 0
    max_sum, min_sum = 0, 0
    for running_sum in accumulate(arr):
        min_sum = min(min_sum, running_sum)
        max_sum = max(max_sum, running_sum - min_sum)
        i += 1
    return max_sum


lst = [904, -4000, 500, 223, 2342, 523, 12, -3135, -385, -124, 481, -31]
print("find_maximum_subarray", find_maximum_subarray(lst))


# a = accumulate([904, 40, 523, 12, -335, -385, -124, 481, -31])
# for ai in a:
#     print(ai)

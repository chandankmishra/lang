def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    maxInt32 = 2147483647
    minInt32 = -2147483648
    num = 0

    neg = True if x < 0 else False
    if neg is True:
        x = (-1) * x

    while x != 0:
        num = 10 * num + x % 10
        x = x // 10

    if num > maxInt32 or num < minInt32:
        num = 0
    if neg is True:
        num = (-1) * num
    return num


a = 123
print(reverse(a))

a = -2342
print(reverse(a))

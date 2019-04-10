##################### x + y #################
def get_addition(x, y):
    if y == 0:
        return x
    return get_addition(x ^ y, (x & y) << 1)

##################### x * y #################


def get_multiplication1(x, y):
    nsum = 0
    if x < y:
        x, y = y, x
    for _ in range(y):
        nsum = get_addition(x, nsum)
    return nsum


def helper(x, y):
    if y == 1:
        return x
    half = helper(x, y >> 1)
    if y & 1:
        return half + half + x
    else:
        return half + half


def get_multiplication2(x, y):
    if x < y:
        x, y = y, x
    return helper(x, y)

##################### x ^ y #################


def power(x, y):
    result, power = 1.0, y
    if y < 0:
        power, x = -power, 1.0 / x
    while power:
        if power & 1:
            result *= x
        x, power = x * x, power >> 1
    return result

##################### x / y #################


def divide1(x, y):
    result, power = 0, 32
    y_power = y << power
    while x >= y:
        while y_power > x:
            y_power >>= 1
            power -= 1
        result += 1 << power
        x -= y_power
    return result


def divide(divident, divisor):
    remainder = divident % divisor
    quotient = divident // divisor
    result = [str(quotient)]

    if remainder:
        result.append(".")

    hmap = {}
    hmap[remainder] = len(result)
    repeat = False
    while remainder != 0:
        remainder = remainder * 10
        quotient = remainder // divisor
        remainder = remainder % divisor
        result.append(str(quotient))
        if remainder in hmap:
            repeat = True
            break
        hmap[remainder] = len(result)
    if repeat is False:
        return ''.join(result)
    else:
        return ''.join(result[:hmap[remainder]]) + "(" + ''.join(result[hmap[remainder]:]) + ")"


# print (get_multiplication1(100, 5))
# print (get_multiplication2(100, 5))
# print (power(100, 5))
# print (divide(100, 5))
print (divide(1, 2))
print (divide(1, 3))
print (divide(2, 3))
print (divide(1, 16))

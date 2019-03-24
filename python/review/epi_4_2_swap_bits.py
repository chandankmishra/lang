# epi_4.8 reverse digits
def reverse_digits(num):
    result, abs_num = 0, abs(num)
    while abs_num:
        result = result * 10 + abs_num % 10
        abs_num = abs_num // 10
    return -result if num < 0 else result


# print (reverse_digits(17))
# print (reverse_digits(357))
# print (reverse_digits(-217))

# epi_4.9 check if a decimal integer is palindrome
def check_num_palindrome(num):
    return num == reverse_digits(num)


print (check_num_palindrome(1))
print (check_num_palindrome(13))
print (check_num_palindrome(353))


# epi_4.4
def closest_int_same_weight(num):
    for i in range(31):
        if (num >> i) & 1 != (num >> (1 + i)) & 1:
            bit_mask = (1 << i) | (1 << (i + 1))
            num = num ^ bit_mask
            break
    return num


# print (closest_int_same_weight(7))
# print (closest_int_same_weight(12342))

# epi_4.3


def reverse_bits(num):
    print (bin(num))
    print (bin(num))
    return num


# print (reverse_bits(2342))

# epi_4.2
def swap_bits(num, i, j):
    bit_mask = (1 << i) | (1 << j)
    num ^= bit_mask
    return num


# print (swap_bits(2342, 5, 0))

romanToInt1 = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

romanToInt2 = {
    'IV': 4,
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900,
}


def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    sum = 0
    l = len(s)
    skip_next = False
    for i in range(0, l):
        if skip_next is True:
            skip_next = False
            continue

        if i == l - 1:
            if s[i] in romanToInt1:
                sum += romanToInt1[s[i]]
                return sum
            else:
                return 0

        digit2 = s[i] + s[i + 1]
        if digit2 in romanToInt2:
            sum += romanToInt2[digit2]
            skip_next = True
        elif s[i] in romanToInt1:
            sum += romanToInt1[s[i]]
        else:
            return 0

    return sum


print (romanToInt("DCXXI"))

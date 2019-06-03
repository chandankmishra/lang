def get_char(ch, shift):
    val = ord(ch) - ord('a')
    val = (val + shift) % 26 + ord('a')
    return chr(val)


def shiftingLetters(S, shifts):
    """
    :type S: str
    :type shifts: List[int]
    :rtype: str
    """

    l = len(shifts)
    tmp = 0
    print(S, shifts, l)
    for i in range(l - 1, -1, -1):
        tmp += shifts[i]
        shifts[i] = tmp

    ret_str = ""
    for i, ch in enumerate(S):
        ret_str += get_char(S[i], shifts[i])
    return ret_str


print(shiftingLetters("abc", [3, 5, 9]))

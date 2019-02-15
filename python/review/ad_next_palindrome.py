def nearestPalindromic(n: 'str') -> 'str':
    l = len(n)
    # with different digits width, it must be either 10...01 or 9...9
    candidates = set()
    candidates.add(str(10 ** l + 1))  # 100001
    candidates.add(str(10 ** (l - 1) - 1))  # 99999
    # the closest must be in middle digit +1, 0, -1, then flip left to right
    prefix = int(n[:(l + 1) // 2])
    prefix_list = map(str, (prefix - 1, prefix, prefix + 1))
    for i in prefix_list:
        if l & 1:
            right = i[:-1][::-1]  # for odd length remove last char. 123 -> 21
        else:
            right = i[::-1]  # for even length dont remove last char 12 -> 21
        candidates.add(i + right)
    candidates.discard(n)

    # convert candiate and n from str to int
    candidates = map(int, candidates)
    n = int(n)
    delta, result = float("inf"), 0
    for candidate in candidates:
        if abs(n - candidate) < delta:
            delta = abs(n - candidate)
            result = candidate
    return result


print (nearestPalindromic("12345"))

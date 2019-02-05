def shortest_substring(text, nset):
    n, m = len(text), len(nset)
    ndict = {}
    for ch in nset:
        ndict[ch] = ndict.get(ch, 0) + 1
    missing = len(ndict)
    start_idx = -1
    min_len = float("inf")

    i, j = 0, 0
    while j < n:
        ch1 = text[j]
        if ch1 in ndict:
            ndict[ch1] -= 1
            if ndict[ch1] == 0:
                missing -= 1
        j += 1
        while missing == 0:
            if min_len > j - i:
                min_len = j - i
                start_idx = i

            ch2 = text[i]
            if ch2 in ndict:
                ndict[ch2] += 1
                if ndict[ch2] == 1:
                    missing += 1
            i += 1
    if start_idx != -1:
        return text[start_idx: start_idx + min_len]
    else:
        return ""


print(shortest_substring("helloworld", 'lwr'))
print(shortest_substring("ADOBECODEBANC", 'ABC'))
print(shortest_substring("aa", "aa"))


# Brute Force
# def is_found(text, nset):
#     tset = set(text)
#     for ch in nset:
#         if ch not in tset:
#             return False
#     return True


# def shortest_substring(text, nset):
#     n = len(text)
#     l = 3
#     for i in range(n):
#         for j in range(i, n - l + 1):
#             if is_found(text[j:j + l], nset):
#                 return text[j:j + l]
#         l += 1
#     return ""

# print(shortest_substring("helloworld", set('lwr')))

"""
s=ADOBECODEBANC
p=ABC
r=BANC
"""


def mininum_window_substring(s, p):
    ndict = {}
    for ch in p:
        ndict[ch] = ndict.get(ch, 0) + 1
    missing = len(ndict)
    start, end = 0, 0
    n = len(s)
    min_len, start_idx = float("inf"), -1
    while end < n:
        ch = s[end]
        if ch in ndict:
            ndict[ch] -= 1
            if ndict[ch] == 0:
                missing -= 1
        end = end + 1

        while missing == 0:
            if end - start < min_len:
                min_len = end - start
                start_idx = start
            ch = s[start]
            if ch in ndict:
                ndict[ch] += 1
                if ndict[ch] == 1:
                    missing += 1
            start = start + 1
    if start_idx == -1:
        return ""
    else:
        return s[start_idx:start_idx + min_len]


s = "ADOBECODEBANC"
p = "ABC"
print (mininum_window_substring(s, p))

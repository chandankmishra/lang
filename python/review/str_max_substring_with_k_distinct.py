def lengthOfLongestSubstringKDistinct(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    n = len(s)
    if n < 1: return 0
    ndict = {}
    start, end = 0, 0
    counter = 0
    max_len = 0
    while end < n:
        ch = s[end]
        ndict[ch] = ndict.get(ch, 0) + 1
        if ndict[ch] == 1:
            counter += 1
        end = end + 1
        
        while counter > k:
            ch = s[start]
            ndict[ch] -= 1
            if ndict[ch] == 0:
                counter -= 1
            start = start + 1
        max_len = max(max_len, end-start)
    return max_len

print (lengthOfLongestSubstringKDistinct("eceba", 2)) #2
print (lengthOfLongestSubstringKDistinct("aa", 1)) #2

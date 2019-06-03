def countOfAnagramSubstring(s):

    # Returns total number of anagram
    # substrings in s
    n = len(s)
    mp = dict()

    # loop for length of substring
    for i in range(n):
        sb = ''
        for j in range(i, n):
            sb = ''.join(sorted(sb + s[j]))
            mp[sb] = mp.get(sb, 0) + 1

    ans = 0
    # loop over all different dictionary
    # items and aggregate substring count
    for k, v in mp.items():
        ans += (v * (v - 1)) // 2
    return ans


# Driver Code
s = "xyyx"
print(countOfAnagramSubstring(s))

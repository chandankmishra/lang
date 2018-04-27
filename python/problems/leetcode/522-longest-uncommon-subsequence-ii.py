def findLUSlength(strs):
    """
    :type strs: List[str]
    :rtype: int
    """
    maxl = 0
    all_equal = True
    last_str = strs[0]
    for s in strs:
        print (last_str, s, last_str != s)
        if last_str != s:
            all_equal = False

        last_str = s
        str_len = len(s)
        if maxl < str_len:
            maxl = str_len

    if all_equal is True:
        return -1
    return maxl


s = ["aaa", "aaa", "aa"]
print(findLUSlength(s))

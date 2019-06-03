def min_window(s, t):
    table = {}
    counter = 0
    for ch in t:
        table[ch] = table[ch] + 1 if ch in table else 1

    ans = ""
    start, end = 0, 0
    counter = len(table)
    llen = float("inf")

    while (end < len(s)):
        endchar = s[end]
        if endchar in table:
            table[endchar] -= 1
            if table[endchar] == 0:`
                counter -= 1
        end = end + 1
        print(start, end, table, counter)
        while counter == 0:
            if end - start < llen:
                llen = end - start
                ans = s[start: end]

            startchar = s[start]
            if startchar in table:
                table[startchar] += 1
                if table[startchar] > 0:
                    counter += 1
            print("#", start, end, table, counter)
            start += 1

    return ans


S = "ADOBECODEBANC"
T = "ABC"

print(min_window(S, T))

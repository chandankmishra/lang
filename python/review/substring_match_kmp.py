def KMP(txt, pat):
    result = []
    M, N = len(pat), len(txt)
    lps = [0] * M
    j = 0  # index for pat[]

    computeLPSArray(pat, lps)

    i = 0  # index for txt[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            result.append(i - j)
            j = lps[j - 1]
        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    if len(result) == 0:
        result.append(-1)
    return result


def computeLPSArray(pat, lps):
    M = len(pat)
    j = 0
    lps[0] = 0
    i = 1
    while i < M:
        if pat[i] == pat[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1


print(KMP("abcdefabc", "abc"))

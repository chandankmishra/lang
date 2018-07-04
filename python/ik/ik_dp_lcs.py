'''
In cases where the new element on both new row and column become same then diag+1 gives the new max.
In cases the new row & col chars are different then max of previous row or col gives the new max.
'''
def lcs(a, b):
    alen, blen = len(a), len(b)
    dp = [[0 for _ in range(blen+1)] for _ in range(alen+1)]
    for ai in range(alen+1):
        for bi in range(blen+1):
            if ai == 0 or bi == 0:
                continue
            # ai-1, bi-1 not ai, bi because a, b are string which are one less chr then dp[][]
            if  a[ai-1] == b[bi-1]:
                dp[ai][bi] = dp[ai-1][bi-1]+1
            else:
                dp[ai][bi] = max(dp[ai-1][bi], dp[ai][bi-1])
    return dp[alen][blen]


a = "bcc"
b = "bbcac"
print(lcs(a,b))

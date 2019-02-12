'''
Formula:
dp[1][e] = 1
dp[n][1] = n
dp[i][j] = min(dp[n-i][j], dp[i-1][j-1]) + 1
'''


def egg_drop(floors, eggs):
    dp = [[0 for _ in range(eggs + 1)] for _ in range(floors + 1)]

    for e in range(eggs + 1):
        dp[1][e] = 1

    for f in range(floors + 1):
        dp[f][1] = f

    for f in range(2, floors + 1):
        for e in range(2, eggs + 1):
            dp[f][e] = float("inf")
            for i in range(1, f):
                dp[f][e] = min(dp[f][e], max(dp[floors - f][e], dp[f - 1][e - 1]) + 1)
    return dp[floors][eggs]


print (egg_drop(6, 2))

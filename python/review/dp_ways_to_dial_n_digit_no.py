
'''
Formula for number of ways to create a number of length l which ends at 0.
nw(l, 0) = nw(l-1, 8)
nw(l, 1) = nw(l-1, 2) + nw(l-1, 4)
... so on.

'''
def num_of_ways(n, prev):
    dp = [[0 for _ in range(2)] for _ in range(10)]
    # set # of ways for 1 digit number
    for i in range(10):
        dp[i][1] = 1

    for l in range(2, n + 1):
        for d in range(10):
            for p in prev[d]:
                dp[d][l % 2] += dp[p][(l + 1) % 2]

    result = 0
    for d in range(10):
        result += dp[d][n % 2]
    return result


prev = [[8], [2, 4], [1, 3, 5], [2, 6], [1, 5, 7], [2, 4, 6, 8], [3, 5, 9], [4, 8], [5, 7, 9, 0], [6, 8]]
print(num_of_ways(1, prev))

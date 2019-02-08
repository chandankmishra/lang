def helper(coins, dp, a, b):
    if a > b:
        return 0
    if dp[a][b] == 0:
        max_a = coins[a] + min(helper(coins, dp, a + 2, b), helper(coins, dp, a + 1, b - 1))
        max_b = coins[b] + min(helper(coins, dp, a + 1, b - 1), helper(coins, dp, a, b - 2))
        dp[a][b] = max(max_a, max_b)
    return dp[a][b]


def optimalStrategyRecursive(coins, n):
    dp = [[0 for i in range(n)]
          for i in range(n)]
    return helper(coins, dp, 0, n - 1)


def optimalStrategyIterative(arr, n):
    table = [[0 for i in range(n)]
             for i in range(n)]

    for gap in range(n):
        for j in range(gap, n):
            i = j - gap
            x = 0
            if((i + 2) <= j):
                x = table[i + 2][j]
            y = 0
            if((i + 1) <= (j - 1)):
                y = table[i + 1][j - 1]
            z = 0
            if(i <= (j - 2)):
                z = table[i][j - 2]
            table[i][j] = max(arr[i] + min(x, y),
                              arr[j] + min(y, z))
    return table[0][n - 1]


# Driver Code
arr1 = [8, 15, 3, 7]
n = len(arr1)
print(optimalStrategyRecursive(arr1, n))

arr2 = [2, 2, 2, 2]
n = len(arr2)
print(optimalStrategyRecursive(arr2, n))

arr3 = [20, 30, 2, 2, 2, 10]
n = len(arr3)
print(optimalStrategyIterative(arr3, n))

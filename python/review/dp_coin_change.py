def coin_chagne(A, coins):
    dp = [float("inf") for _ in range(A + 1)]
    # base case
    dp[0] = 0

    # implementation of recurssive formulation
    for a in range(1, A + 1):
        for coin in coins:
            if a - coin >= 0:
                dp[a] = min(dp[a], dp[a - coin])
        if dp[a] != float("inf"):
            dp[a] = dp[a] + 1
    print (dp)
    # return dp[A]
    return dp


def print_coin_recursive(dp, A, coins):
    if A < 0:
        print ("Error")
        return
    if A == 0:
        return

    for coin in coins:
        if dp[A - coin] == dp[A] - 1:
            print (coin)
            return print_coin_recursive(dp, A - coin, coins)
    print ("Error")


def print_coin_iterative(dp, a, coins):
    while a != 0 and dp[a] != float("inf"):
        for coin in coins:
            if dp[a - coin] == dp[a] - 1:
                print (coin)
                a = a - coin
                break
    if a != 0:
        print ("Error")


A = 8
d = [2, 3, 5]
dp = coin_chagne(A, d)
print_coin_recursive(dp, A, d)
print_coin_iterative(dp, A, d)

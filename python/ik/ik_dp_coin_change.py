class Solution(object):
    def __init__(self):
        self.dict = {}
#     def helper(self, coins, amount):
#         if amount == 0:
#             return 0
#         if amount < 0:
#             return float("inf")

#         if amount in self.dict:
#             return self.dict[amount]

#         nmin = float("inf")
#         for coin in coins:
#             ret = self.helper(coins, amount-coin)
#             if ret < nmin:
#                 nmin = ret
#         self.dict[amount] = nmin + 1
#         return nmin + 1
    def printCoinsR(self, dp, coins, stack, a):
        if a < 0:
            raise ValueError('incorrect value')
        if a == 0:
            print(stack)
            return

        for d in coins:
            if dp[a - d] == dp[a] - 1:
                stack.append(d)
                # print(d, end=' ')
                self.printCoinsR(dp, coins, stack, a - d)
                stack.pop()

    def printCoinsMainR(self, dp, coins):
        print("Print Coins Recursive")
        A = len(dp) - 1
        result, stack = [], []
        return self.printCoinsR(dp, coins, stack, A)

    def printCoinsMainI(self, dp, coins):
        print("Print Coins Iterative")
        a = len(dp) - 1
        while a > 0:
            for d in coins:
                if dp[a] - 1 == dp[a - d]:
                    print(d, end=' ')
                    a = a - d
                    break
        if a != 0:
            raise ValueError('incorrect value')
        print('')

    def helper(self, coins, amount):
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for k in coins:
                if k > i:
                    continue
                dp[i] = min(dp[i], dp[i - k])
            dp[i] = dp[i] + 1
        # print(dp)
        return dp[amount]

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        print("coins", coins)
        print("amount", amount)
        print('Minimum # of Coins to make sum ', amount)
        ret = self.helper(coins, amount)
        return -1 if ret == float("inf") else ret


s = Solution()
coins = [1, 2, 5]
amont = 11
# print(s.coinChange(coins, 11))
dp = [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3]
s.printCoinsMainR(dp, coins)
print('')
# s.printCoinsMainI(dp, coins)

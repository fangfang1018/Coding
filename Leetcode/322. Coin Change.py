coins = [1, 2, 5]
amount = 11

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort()
        inf = float("inf")
        dp = [0] + [1 if i in coins else inf for i in xrange(1, amount+1)]
        for i in xrange(1, amount+1) :
            if dp[i] == inf:
                continue
            for coin in coins:
                if i+coin <= amount:
                    dp[i+coin] = min(dp[i+coin], dp[i]+1)
                else:
                    break
        return dp[amount] if dp[amount] != inf else -1

coins = [1, 3]
amount = 2
s = Solution()
s.coinChange(coins, amount)
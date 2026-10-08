class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        memo = {}
        ##either 0 or 1 state decides outcome
        def dfs(i,buy):
            if i >= len(prices):
                return 0
            if (i,buy) in memo:
                return memo[(i,buy)]

            if buy:
                profit = max(prices[i] + dfs(i + 1, 0), dfs(i + 1, 1))
            else:
                profit = max(-prices[i] + dfs(i + 1, 1), dfs(i + 1, 0))
            memo[(i,buy)] = profit
            return profit
        
        return dfs(0,0)
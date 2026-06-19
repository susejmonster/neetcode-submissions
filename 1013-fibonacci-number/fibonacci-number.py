class Solution:
    def fib(self, n: int) -> int:
        dp = [-1]*(n+1)
        def gen(n,dp):
            if n <= 1:
                return n
        
            if dp[n]!=-1:
                return dp[n]
        
            dp[n] = gen(n-2,dp)+gen(n-1,dp)
            return dp[n]
        return gen(n,dp)
        
        
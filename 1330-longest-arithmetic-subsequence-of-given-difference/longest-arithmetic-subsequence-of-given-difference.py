class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        dp = {}
        
        LIS = 1
        if n < 2:
            return n
        
        for i in range(0,n):
            num  = arr[i]
            if num-difference in dp:
                dp[num] = dp[num-difference]+1
            else:
                dp[num]=1
            
            LIS = max(LIS,dp[num])
        
        return LIS
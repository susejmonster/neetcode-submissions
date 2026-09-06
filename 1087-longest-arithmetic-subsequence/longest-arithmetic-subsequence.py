class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return len(nums)
        
        mx = 2
        dp = [{}for _ in range(len(nums))]

        for i in range(len(nums)):
            for j in range(0,i):
                diff = nums[i]-nums[j]
                dp[i][diff] = dp[j].get(diff,1)+1
                mx = max(mx,dp[i][diff])
        return mx
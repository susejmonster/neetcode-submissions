class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [-1]*len(nums)

        def dp(i):
            if memo[i]!=-1:
                return memo[i]

            LIS = 1
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    LIS = max(LIS,1+dp(j))
            
            memo[i] = LIS
            return LIS

        return max(dp(i) for i in range(len(nums)))
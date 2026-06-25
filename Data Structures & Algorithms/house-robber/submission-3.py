class Solution:
    def rob(self, nums: List[int]) -> int:
        robbed = [None]*len(nums)

        def dp(n):
            if n==len(nums)-1:
                return nums[n]
            if n>=len(nums):
                return 0 
            
            if robbed[n]!=None:
                return robbed[n]
            
            res = max(nums[n] + dp(n + 2), dp(n + 1))
            robbed[n] = res

            return res

        return max(dp(0) , dp(1))
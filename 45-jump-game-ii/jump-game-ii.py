class Solution:
    def jump(self, nums: List[int]) -> int:
        
        memo = {}
        def dp(i):
            if i >=len(nums)-1:
                return 0
            if nums[i] == 0:
                return 1000000
            if i in memo:
                return memo[i]
            
            end = min(len(nums) - 1, i + nums[i])
            chose = 1000000
            for j in range(i+1,end+1):
                chose = min(chose,1+dp(j))
            memo[i] = chose
            return chose        
        return dp(0)
        
         
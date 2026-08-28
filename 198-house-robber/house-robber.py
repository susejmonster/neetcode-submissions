class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1]*len(nums)
        def trav(idx):
            if idx>=len(nums):
                return 0
            if memo[idx]!=-1:
                return memo[idx]
            
            memo[idx] = max(trav(idx+1),nums[idx]+trav(idx+2)) 
            return memo[idx]
        

        return trav(0)
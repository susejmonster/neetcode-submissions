class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []#actual result
        subset = []#curretn branch
        nums.sort()

        def dfs(i):
            #base case
            if i == len(nums):
                res.append(subset.copy())#handover
                return 
            
            #adding to subset
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()#backtracking

            while i + 1 < len(nums) and nums[i] == nums[i+1]:##make extra decision here
                i+=1    
            
            dfs(i+1)

        
        dfs(0)
        return res
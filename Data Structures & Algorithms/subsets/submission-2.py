class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] #actual result
        subset = [] #current branch

        def dfs(idx):
            #base case
            if idx == len(nums):
                res.append(subset.copy())#handover to result
                return 
            #add to list from array
            subset.append(nums[idx])
            dfs(idx+1)#move to next branch
            subset.pop()#backtrack last value
            dfs(idx+1)



        #init tree
        dfs(0)
        return res


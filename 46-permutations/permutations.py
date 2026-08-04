class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack([],nums,[False]*len(nums))
        return self.res
    def backtrack(self,perm,nums,vis):
        if len(perm)==len(nums):
            self.res.append(perm[:])
            return 
        
        for i in range(len(nums)):
            if not vis[i]:
                perm.append(nums[i])
                vis[i] = True
                self.backtrack(perm,nums,vis)
                perm.pop()
                vis[i] = False
    
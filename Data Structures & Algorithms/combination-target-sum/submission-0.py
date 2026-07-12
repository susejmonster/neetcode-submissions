class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ans  = []

        def comsum(i,res,target):
            if target == 0:
                ans.append(res.copy())
                return 
            
            if i >= len(nums) or target < 0:
                return 
            
            
            res.append(nums[i])
            comsum(i,res,target-nums[i])
            res.pop()
            comsum(i+1,res,target)

        comsum(0,[],target)
        return ans


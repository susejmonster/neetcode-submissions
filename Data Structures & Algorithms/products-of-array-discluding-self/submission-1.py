class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = []
        for i in range(0,len(nums)):
            mult = 1
            for j in range(0,len(nums)):
                if i!=j:
                    mult = mult*nums[j]
            res.append(mult)
        return res
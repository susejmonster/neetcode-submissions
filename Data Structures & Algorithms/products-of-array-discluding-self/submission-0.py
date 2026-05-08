class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i,n in enumerate(nums):
            if(len(nums) > 1):
                product = 1
            else:
                product = nums[0]
                
            for j in range(0,len(nums)):
                if(j!=i):
                    product = product*nums[j] 
            output.append(product)    
        return output
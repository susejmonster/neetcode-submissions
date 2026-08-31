class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = nums[0]
        s=0
        for i in range(0,len(nums)):
            s+=nums[i]
            if s > mx:
                mx=s
            if s<0:
                s =0
            
        return mx
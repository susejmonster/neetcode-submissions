class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        
        ans = [0]*len(nums)
        for i in range(0,len(nums)):
            #8
            cnt = 0
            for j in range(0 , len(nums)):
                #1,2,2,3
                if i!=j and nums[j]<nums[i]:
                    cnt+=1
                    ans[i]=cnt
            
        return ans
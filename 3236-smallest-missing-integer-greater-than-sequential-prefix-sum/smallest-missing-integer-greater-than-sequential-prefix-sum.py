class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix = nums[0]

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                prefix = prefix + nums[i]
            else:
                break
        nums.sort()      
        for i in range(0,len(nums)):
            if nums[i] == prefix:
                prefix+=1
        return prefix


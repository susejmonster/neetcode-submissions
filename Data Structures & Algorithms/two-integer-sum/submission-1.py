class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(0,len(nums)):
            diff = target - nums[i]
            for j in range(0,len(nums)):
                if nums[j] == diff and i!=j:
                    return [i,j]
        return -1
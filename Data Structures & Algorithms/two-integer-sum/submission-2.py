class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mp = {}

        for j in range(0,len(nums)):
            diff = target - nums[j]
            if diff in mp:
                return [mp[diff] , j]
            mp[nums[j]] = j
        return -1
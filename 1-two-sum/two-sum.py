class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twopass = {}
        
        for i in range(0,len(nums)):
            twopass[nums[i]] = i

        for i in range(0,len(nums)):
            diff = target - nums[i]
            if diff in twopass and twopass[diff] != i:
                return [i,twopass[diff]]
        
            
        
        return None

            

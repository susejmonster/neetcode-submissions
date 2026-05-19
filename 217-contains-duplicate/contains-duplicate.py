class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = set()
        
        for i in range(0,len(nums)):
            if nums[i] in freq:
                return True
            freq.add(nums[i])
        return False
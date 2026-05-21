class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_to_idx = {}
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in val_to_idx:
                return [val_to_idx[diff], i]
            val_to_idx[num] = i
            
        
        return None

            

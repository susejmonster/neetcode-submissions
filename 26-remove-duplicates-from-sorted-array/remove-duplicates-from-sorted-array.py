class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        seen = [nums[0]]

        for i in range(1,len(nums)):
            if nums[i] not in seen:
                seen.append(nums[i])
        
        nums[:] = seen

        return len(nums)
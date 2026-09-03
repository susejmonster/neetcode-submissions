class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        freq = {}
        for i in range(0,len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0)+1

            if freq[nums[i]]>1:
                return nums[i]
        return -1
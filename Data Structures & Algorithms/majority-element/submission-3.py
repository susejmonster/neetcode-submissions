class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        freq = {}
        count = 0 
        mx = None
        for i in range(0,len(nums)):
            freq[nums[i]] = freq.get(nums[i],0)+1
            if freq[nums[i]]>=count:
                count = freq[nums[i]]
                mx = nums[i]
        
        return mx
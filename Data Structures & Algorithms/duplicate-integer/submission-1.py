class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        mp = {}
        for i in range(len(nums)):
            mp[nums[i]] = mp.get(nums[i],0)+1
        for m in mp:
            if mp[m]>1:
                return True
        return False
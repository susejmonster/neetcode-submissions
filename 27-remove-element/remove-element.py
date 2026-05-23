class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) < 1:
            return 0
        elif len(nums) == 1 and nums[0] == val:
            return 0
        
        
        i = 0 
        j = len(nums)-1

        while i<=j:
            if nums[i] != val:
                i+=1
            else:
                nums[i]  = 51
            
            if nums[j] != val:
                j-=1
            else:
                nums[j] = 51
        nums.sort()
        count = 0
        for i in nums:
            if i != 51:
                count+=1
        return count
        
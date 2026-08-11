class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up = 0
        down = 0
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                up = down+1
            elif nums[i]<nums[i-1]:
                down = up+1

        return 1+max(up,down)

            

        
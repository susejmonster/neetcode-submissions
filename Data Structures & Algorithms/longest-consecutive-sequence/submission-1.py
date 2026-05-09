class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        nums.sort()
        res = 0
        streak = 1
        curr = nums[0]

        for i in range(0, len(nums)):
            if nums[i] == nums[i - 1]:
                continue                      # skip duplicates
            elif nums[i] == nums[i - 1] + 1:
                streak += 1                   # extend streak
            else:
                streak = 1                    # reset streak

            res = max(res, streak)

        return res

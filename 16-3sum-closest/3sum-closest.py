class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_diff = nums[0] + nums[1] + nums[2]
        nums.sort()
        #three pointer approach
        for i in range(0,len(nums)-2):
            #inward window
            left,right = i+1, len(nums)-1

            while left < right:
                sum1 = nums[i] + nums[left] + nums[right]

                if abs(target - sum1) < abs(target - min_diff):
                    min_diff = sum1
                
                if sum1 == target:
                    return target
                elif sum1 < target:
                    left+=1
                else:
                    right-=1
              
        return min_diff
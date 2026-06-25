class Solution:
    
    
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        result = 0
        prefix_sum = []

        for num in nums:

            if len(prefix_sum) == 0:
                prefix_sum.append(num)
            else:
                prefix_sum.append(prefix_sum[-1] + num)

        n = len(nums)
                    
        for index in range(n):
            for next_index in range(index, n):

                if index == next_index:
                    subarray_sum = nums[index]
                else:
                    if index > 0:
                        subarray_sum = prefix_sum[next_index] - prefix_sum[index - 1]
                    else:
                        subarray_sum = prefix_sum[next_index]
                        
                digits = str(subarray_sum)
                            
                if int(digits[0]) == x and int(digits[-1]) == x:
                    result = result + 1

        return result
            


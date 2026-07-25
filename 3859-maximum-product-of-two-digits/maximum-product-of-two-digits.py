class Solution:
    def maxProduct(self, n: int) -> int:
        nums = []
        while n>0:
            digit = n%10
            nums.append(digit)
            n = n//10
        
        nums.sort()
        mx = 0 
        for l in range(0,len(nums)):
            for r in range(l+1,len(nums)):
                max_mult = nums[r]*nums[l]
                if max_mult > mx:
                    mx = max_mult
        return mx

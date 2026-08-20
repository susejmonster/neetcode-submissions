class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        stack = {}

        for i in nums:
            stack[i] = stack.get(i,0)+1
            if stack[i]>1:
                return i 
        return None
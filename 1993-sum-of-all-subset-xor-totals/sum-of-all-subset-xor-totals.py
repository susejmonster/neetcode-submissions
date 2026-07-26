class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        res = []

        def backtrack(idx,stack):
            if idx >= len(nums):
                if stack:
                    res.append(stack[-1])
                else:
                    res.append(0)
                return None

            if stack:
                XOR_1 = stack[-1]^nums[idx]
                stack.append(XOR_1)
            else:
                stack.append(nums[idx])
            
            backtrack(idx+1,stack)
            stack.pop()
            backtrack(idx+1,stack)
        
        backtrack(0,[])
        return sum(res)
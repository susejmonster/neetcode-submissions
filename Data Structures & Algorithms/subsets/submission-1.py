class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []#pen
        subset = []#paper

        def rec(i):
            #stopping case
            if i>=len(nums):
                res.append(subset.copy())
                return
            
            #take dont take
            subset.append(nums[i])#put in subset list
            rec(i+1)#move one step forward in original list
            subset.pop()
            rec(i+1)

        rec(0)#base case
        return res


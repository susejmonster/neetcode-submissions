class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n_mp = {}
        for i in range(0,len(nums)):
            n_mp[nums[i]] = i #0:3 , 1:0
        print(n_mp)
        for i in range(0,len(nums)+1):#0m,1,2,3,...
            print(i)
            if i not in n_mp:
                return i

        return -1
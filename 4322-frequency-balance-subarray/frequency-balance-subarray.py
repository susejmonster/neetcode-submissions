class Solution:
    def getLength(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(0,len(nums)):
            mp = {}
            freq  = [0] * (n + 1)#has to be static array
            mx = 0
            s = 0
            for j in range(i,len(nums)):
                old = mp.get(nums[j],0)#get key safely
                if old:
                    freq[old] -= 1
                mp[nums[j]] = old + 1
                freq[old+1]+=1

                if old+1>mx:
                    mx = old+1
                    s = 1
                elif old+1==mx:
                    s+=1
            
                distinct = len(mp)
                if distinct == 1:
                    ans = max(ans,j-i+1)
                elif(mx%2 == 0 and s<distinct and freq[mx//2] == distinct-s):
                    ans = max(ans,j-i+1)
    
        return ans
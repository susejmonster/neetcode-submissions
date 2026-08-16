class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        dup = set()
        l = 0
        res = 0
        for r in range(0,len(s)):
            while s[r] in dup:
                dup.remove(s[l])
                l+=1
            dup.add(s[r])
            if res < r-l+1:
                res = r-l+1
           
        
        return res
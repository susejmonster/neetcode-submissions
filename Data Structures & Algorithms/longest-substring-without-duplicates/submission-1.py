class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            if len(s) <= 0:
                return 0
           
            window = set()
            i = 0
            Max = 0
            for j in range(0,len(s)):
                while s[j] in window:
                    window.remove(s[i])
                    i += 1
                window.add(s[j])
                Max = max(Max, j - i + 1)
                      
            return Max
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        last = len(s)-1
        start  = 0
        while s[last] == " ":
            last -= 1
        
        start = last 
        while s[start] != " " and start >= 0:
            start -= 1
        
        return last - start
        
